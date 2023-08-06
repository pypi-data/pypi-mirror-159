from .utils import maya_dts
from hypothesis import given
from hypothesis.strategies import lists
from hypothesis.strategies import sets
from tzolkin.time_sets import CombinedTimeSet
from tzolkin.time_sets import ExplicitTimeSet

@given(
    lists(sets(maya_dts(), min_size=1), min_size=1),
    maya_dts()
)
def test_singleton_time_set(event_timesets, now):
    combined_timeset = CombinedTimeSet([
        ExplicitTimeSet(event_times)
        for event_times in event_timesets
    ])

    next_event_time = combined_timeset.next_after(now)

    merged_event_times = set()
    for event_times in event_timesets:
        merged_event_times.update(event_times)

    if next_event_time is None:
        assert now >= max(merged_event_times)
    else:
        assert next_event_time in merged_event_times
        min_next_event_time = min(
            time
            for time in merged_event_times
            if time > now
        )
        assert next_event_time == min_next_event_time