from .utils import maya_dts
from hypothesis import given
from tzolkin.time_sets import SingletonTimeSet

@given(maya_dts(), maya_dts())
def test_singleton_time_set(event_time, now):
    ts = SingletonTimeSet(event_time)

    next_event_time = ts.next_after(now)

    if next_event_time is None:
        assert now >= event_time
    else:
        assert now < event_time
        assert next_event_time == event_time