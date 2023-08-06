from .job import Job
from .time_set_builder import TimeSetBuilder
from abc import ABC
from abc import abstractmethod
from attr import attr
from attr import attrs


@attrs
class JobBuilder:
    schedule: 'Schedule' = attr()
    time_set_builder: TimeSetBuilder = attr(factory=TimeSetBuilder)

    def do(self, callback):
        job = Job(
            callback=callback,
            time_set=self.time_set_builder.build()
        )
        self.schedule.add_job(job)
        return job

    def __getattr__(self, attr):
        """Override the default attrs behavior.

        This code hooks up TimeSetBuilder so that schedules have nice fluent
        syntax much like the original schedule module.

        e.g. `schedule.at(time).do(callback)`
        """
        if hasattr(self.time_set_builder, attr):
            time_set_builder_attr = getattr(self.time_set_builder, attr)

            def wrapper(*args, **kwargs):
                self.time_set_builder = time_set_builder_attr(*args, **kwargs)
                return self
            return wrapper

        # Ensure we handle attr misses correctly.
        return super().__getattribute__(attr)


class Schedule(ABC):
    @abstractmethod
    def add_job(self, job: Job):
        pass

    # TODO(woursler): Cancel job?

    @abstractmethod
    def start(self):
        """Start the scheduler.

        No callbacks should be called before this function is called.
        Depending on the implementation of the scheduler, this may block, or may
        start the scheduler in another thread and return."""
        pass

    @abstractmethod
    def join(self):
        """Block until the scheduler has processed all pending jobs."""
        pass

    def start_blocking(self):
        self.start()
        self.join()

    def __getattr__(self, attr):
        """Override the default attrs behavior.

        This code hooks up JobBuilder so that schedules have nice fluent
        syntax much like the original schedule module.

        e.g. `schedule.at(time).do(callback)`
        """
        if hasattr(TimeSetBuilder, attr):
            job_builder = JobBuilder(self)

            time_set_builder_attr = getattr(job_builder.time_set_builder, attr)

            def wrapper(*args, **kwargs):
                job_builder.time_set_builder = time_set_builder_attr(
                    *args, **kwargs)
                return job_builder
            return wrapper

        # Ensure we handle attr misses correctly.
        return super().__getattribute__(attr)

    def __call__(self, pattern):
        """Override call behavior to call smart_parse."""
        return JobBuilder(self, TimeSetBuilder.create(pattern))
