import maya

from abc import ABC
from abc import abstractmethod
from maya import MayaDT
from maya import MayaInterval
from typing import List
from typing import Optional


class TimeSet(ABC):
    """A countable set of timestamps.

    Includes utilities for looking up the next member after any given time."""

    @abstractmethod
    def next_after(self, time: MayaDT) -> Optional[MayaDT]:
        """The next time, if any, in this timeset after the given time.

        Note: the returned time should be strictly greater than the given time.
        This way, a sequence of calls to next_after can step through future
        elements of the time set."""
        pass

    @property
    def next(self) -> Optional[MayaDT]:
        """The next time, if any, in this timeset after the current moment."""
        return self.next_after(maya.now())

    def activations_during(
            self,
            interval: MayaInterval,
            maximum_activations=10**3) -> List[MayaDT]:
        cursor = interval.start
        activations: List[MayaDT] = []
        while cursor < interval.end \
                and len(activations) < maximum_activations:
            cursor = self.next_after(cursor)
            if cursor is None:
                break
            activations.append(cursor)
        return activations
