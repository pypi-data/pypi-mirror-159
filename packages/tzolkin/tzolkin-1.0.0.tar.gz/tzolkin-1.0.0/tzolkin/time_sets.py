import croniter
import random
import snaptime.main as snaptime

from .time_set import TimeSet
from attr import attr
from attr import attrs
from datetime import datetime
from datetime import timedelta
from maya import MayaDT
from maya import MayaInterval
from sortedcontainers import SortedSet
from typing import List
from typing import Set


@attrs
class SingletonTimeSet(TimeSet):
    time: MayaDT = attr()

    def next_after(self, time):
        if time < self.time:
            return self.time
        return None


@attrs
class ExplicitTimeSet(TimeSet):
    times: Set[MayaDT] = attr(converter=SortedSet)

    def next_after(self, time):
        next_index = self.times.bisect_right(time)

        if next_index >= len(self.times):
            return None

        next_time = self.times[next_index]

        # Ensure that we always return at time
        # after the given time.
        if self.times[next_index] == time:
            next_index += 1
            if next_index >= len(self.times):
                return None

        return self.times[next_index]


@attrs
class CombinedTimeSet(TimeSet):
    timesets: List[TimeSet] = attr(converter=list)

    def next_after(self, time):
        return min(
            filter(
                lambda t: t is not None,
                (ts.next_after(time) for ts in self.timesets)
            ),
            default=None,
        )


@attrs
class SnapTimeSet(TimeSet):
    """A timeset based on a snaptime instruction.

    Powered by snaptime.

    This module works based on the observation that each snap pattern produces
    a countable set of points.

    Importantly there is a unique timedelta interval between the snap points.
    This allows us to determine the next snap point (from the current moment)
    using only snapped value of the current moment
    (which is most likely in the past).

    Note that the provided instruction *MUST* include at least one snap transform.
    Otherwise, there would not be a countable number of snap points.
    """
    snap_instruction = attr()

    interval: str = attr(init=False)

    # The number of intervals usually required to find the next snap point
    # strictly in the future. This doesn't have to be right, but it helps if it's
    # not wildly wrong. For snaps without any DeltaTransforms, this is 1.
    #
    # Will be automatically corrected.
    offset_guess: int = attr(default=1)

    def __attrs_post_init__(self):
        snap_units = set([
            instruction.unit
            for instruction in snaptime.parse(self.snap_instruction)
            if isinstance(instruction, snaptime.SnapTransformation)
        ])
        if len(snap_units) == 0:
            raise snaptime.SnapParseError(
                "SnapTimeSets must include one or more snaps."
            )

        # Now we have to determine the interval.
        if snaptime.YEARS in snap_units:
            self.interval = snaptime.YEARS
        elif snaptime.MONTHS in snap_units:
            self.interval = snaptime.MONTHS
        elif snaptime.WEEKS in snap_units:
            self.interval = snaptime.WEEKS
        elif snaptime.DAYS in snap_units:
            self.interval = snaptime.DAYS
        elif snaptime.HOURS in snap_units:
            self.interval = snaptime.HOURS
        elif snaptime.MINUTES in snap_units:
            self.interval = snaptime.MINUTES
        elif snaptime.SECONDS in snap_units:
            self.interval = snaptime.SECONDS
        else:
            raise snaptime.SnapUnitError(
                "Unsupported snaptime unit in tzolkin."
            )

        # TODO(woursler): Consider compiling the transformation into another
        # pattern that will just give the correct answer...

    def next_after(self, time):
        offset = self.offset_guess

        def snapped_offset_time(offset):
            return time.add(**{
                self.interval: offset
            }).snap(self.snap_instruction)

        while snapped_offset_time(offset) > time:
            offset -= 1

        while snapped_offset_time(offset) <= time:
            offset += 1

        if self.offset_guess != offset:
            self.offset_guess = offset

        return snapped_offset_time(offset)


@attrs
class CronPatternTimeSet(TimeSet):
    """A TimeSet based on a cron pattern.

    Powered by croniter."""

    cron_pattern: str = attr()

    def next_after(self, time):
        citer = croniter.croniter(self.cron_pattern, time.datetime())
        return MayaDT.from_datetime(citer.get_next(datetime))


@attrs
class PseudorandomTimeSet(TimeSet):
    """Take a TimeSet, jitter amount, and seed, consistently apply random deltas to each point."""

    timeset: TimeSet = attr()
    maximum_jitter: timedelta = attr()
    seed = attr(factory=random.random)

    def next_after(self, time):
        # If we didn't apply jitter, this would be the next time.
        unaltered_next_after = self.timeset.next_after(time)

        # If there are no times in the future -- it doesn't much matter when
        # we pick to end the interval.
        if unaltered_next_after is None:
            unaltered_next_after = time

        # This is the interval where the jittered next time could actually
        # occur.
        interval = MayaInterval(
            time - 2*self.maximum_jitter,
            unaltered_next_after + 2*self.maximum_jitter,
        )

        activations_times = self.timeset.activations_during(interval)
        jittered_activation_times = [
            t + random.Random(
                (self.seed, t)
            ).uniform(-1, 1) * self.maximum_jitter
            for t in activations_times
        ]

        return min(
            filter(
                lambda t: t is not None and time < t,
                (t for t in jittered_activation_times)
            ),
            default=None,
        )
