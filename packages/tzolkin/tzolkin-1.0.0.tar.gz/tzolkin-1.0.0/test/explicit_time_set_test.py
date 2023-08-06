from .utils import maya_dts
from hypothesis import given
from tzolkin.time_sets import ExplicitTimeSet
from hypothesis.strategies import sets

@given(sets(maya_dts(), min_size=1), maya_dts())
def test_singleton_time_set(event_times, now):
    ts = ExplicitTimeSet(event_times)

    next_event_time = ts.next_after(now)

    if next_event_time is None:
        assert now >= max(event_times)
    else:
        assert next_event_time in event_times
        min_next_event_time = min(
            time
            for time in event_times
            if time > now
        )
        assert next_event_time == min_next_event_time