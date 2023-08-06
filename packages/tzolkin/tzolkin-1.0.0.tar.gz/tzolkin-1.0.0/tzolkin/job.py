from attr import attr, attrs
from maya import MayaDT
from typing import Callable
from functools import total_ordering

from .time_set import TimeSet


class CancelJob(object):
    """
    Can be returned from a job to remove itself from the schedule, even if
    there are future elements in the TimeSet.
    """

    @classmethod
    def is_instance(cls, obj):
        return isinstance(obj, CancelJob) or (obj is CancelJob)


@total_ordering
@attrs(hash=False, cmp=False)
class Job:
    callback: Callable[[], None] = attr()

    # The set of times this job should be run at.
    time_set: TimeSet = attr()

    @property
    def next_run_time(self) -> MayaDT:
        return self.time_set.next

    def run(self):
        return self.callback()

    def __eq__(self, other):
        assert isinstance(other, Job)
        if self.next_run_time is None or other.next_run_time is None:
            return self.next_run_time is None and other.next_run_time is None
        return self.next_run_time == other.next_run_time

    def __lt__(self, other: 'Job'):
        if self.next_run_time is None:
            return False
        if other.next_run_time is None:
            return self.next_run_time is not None
        return self.next_run_time < other.next_run_time
