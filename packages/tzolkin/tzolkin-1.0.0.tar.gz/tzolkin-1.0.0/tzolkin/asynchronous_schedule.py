import maya
import queue
import threading
import time

from attr import attr
from attr import attrs
from heapq import heappop
from heapq import heappush
from maya import MayaDT
from typing import List
from typing import Tuple

from .job import CancelJob
from .job import Job
from .schedule import Schedule


@attrs
class AsynchronousSchedule(Schedule):
    # TODO(woursler): Bad name. Improve this to the point it can be just synchronous scheduler.
    # TODO(woursler): This class has some really dumb bugs. It should be overhauled.
    #
    # If it sleeps to long it can call jobs the wrong number of times, for instance.
    sleep_interval_secs: float = attr()

    thread = attr(default=None)

    job_heap: List[Tuple[MayaDT, Job]]  = attr(factory=list)

    def add_job(self, job: Job):
        nrt = job.next_run_time
        if nrt is not None:
            heappush(self.job_heap, (nrt, job))

    def run_pending_jobs(self):
        while len(self.job_heap) > 0 and self.job_heap[0][0] <= maya.now():
            job = heappop(self.job_heap)[1]
            # TODO(woursler): It's possible the job should be run multiple times...
            ret = job.run()

            # If the job specifies we should cancel it, don't put it back on the heap.
            if not CancelJob.is_instance(ret):
                # This will check for finite time sets implicitly.
                self.add_job(job)

    def job_loop(self):
        # while len(self.job_heap) > 0:
        while True:
            self.run_pending_jobs()
            # TODO(woursler): If we know we need to sleep for less time, then sleep for that long...
            time.sleep(self.sleep_interval_secs)

    def start(self):
        assert self.thread is None
        self.thread = threading.Thread(target=self.job_loop)
        self.thread.start()
        # TODO(woursler): Add an option to run forever? Add an option to exit fast?

    def join(self):
        """Block until schedule is complete.

        Since this class is synchronous, the schedule is already completed when
        join is called."""
        assert self.thread is not None
        return self.thread.join()


# TODO(woursler): Shape this code into a Schedule class.

# The time module uses schedule as a backend.
'''jobqueue = queue.Queue()


def job_worker():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()


# TODO(woursler): Start multiple workers?
job_worker_thread = threading.Thread(target=job_worker)
job_worker_thread.start()


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)  # TODO(woursler): Tighten this up?


scheduler_thread = threading.Thread(target=run_schedule)
scheduler_thread.start()'''
