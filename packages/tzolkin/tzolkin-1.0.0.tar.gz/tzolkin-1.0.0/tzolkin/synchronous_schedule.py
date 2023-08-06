from attr import attr, attrs
from heapq import heappop, heappush
import maya
import time
from maya import MayaDT
from typing import List
from typing import Tuple

from .schedule import Schedule
from .job import Job
from .job import CancelJob


@attrs
class SynchronousSchedule(Schedule):
    # TODO(woursler): This class has some really dumb bugs.
    # It should be overhauled.
    #
    # If it sleeps to long it can call jobs the wrong number of times,
    # for instance.
    sleep_interval_secs: float = attr()

    job_heap: List[Tuple[MayaDT, Job]] = attr(factory=list)

    # What function to use for sleeping. Some things require alternatives (see liveplot example.)
    sleep = attr(default=time.sleep)

    def add_job(self, job: Job):
        nrt = job.next_run_time
        if nrt is not None:
            heappush(self.job_heap, (nrt, job))

    def run_pending_jobs(self):
        while len(self.job_heap) > 0 and self.job_heap[0][0] <= maya.now():
            job = heappop(self.job_heap)[1]
            # TODO(woursler): It's possible the job should be run
            # multiple times...
            ret = job.run()

            # If the job specifies we should cancel it,
            # don't put it back on the heap.
            if not CancelJob.is_instance(ret):
                # This will check for finite time sets implicitly.
                self.add_job(job)

    def start(self):
        # TODO(woursler): Add an option to run forever?
        # Add an option to exit fast?
        while len(self.job_heap) > 0:
            self.run_pending_jobs()
            # TODO(woursler): If we know we need to sleep for less time,
            # then sleep for that long...
            self.sleep(self.sleep_interval_secs)
        print("EXITING TZOL SCHEDULE")

    def join(self):
        """Block until schedule is complete.

        Since this class is synchronous, the schedule is already completed
        when join is called."""
        return
