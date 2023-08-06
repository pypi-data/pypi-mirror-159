from attr import attr, attrs
from attr import evolve as attrevolve
from maya import MayaDT
import maya
import croniter
import snaptime
import parsimonious
from typing import Set
from pytimeparse.timeparse import timeparse as parse_duration

from .time_set import TimeSet
from .time_sets import SingletonTimeSet
from .time_sets import ExplicitTimeSet
from .time_sets import SnapTimeSet
from .time_sets import CronPatternTimeSet
from .command_grammar import TzolkenCommandParser


class UnsupportedTimeSetError(ValueError):
    pass


# TODO(woursler): Move alias stuff to a seperate module, make values Union[Alias, TimeSetBuilderFactory?]
PATTERN_ALIASES = {

    ###
    # Standard cron nicknames.
    ###

    '@reboot': UnsupportedTimeSetError(
        # Note: We cannot support @reboot because it cannot be made into a
        # proper TimeSet. We include it because we support all the other cron
        # nicknames and would like to provide a clear error message.
        'Reboots are not scheduled in advance, and therefore are not TimeSets.'
    ),
    '@hourly': '0 * * * *',
    '@daily':  '0 0 * * *',
    '@weekly': '0 0 * * 0',
    '@monthly': '0 0 1 * *',
    '@yearly':  '0 0 1 1 *',
    '@annually': '@yearly',
    '@midnight': '@daily',

    ##
    # Non-standard cron-like nicknames.
    ##

    '@every_year': '@yearly',
    '@every_month': '@monthly',
    '@every_week': '@weekly',
    '@every_day': '@daily',
    '@every_hour': '@hourly',
    '@every_minute': '* * * * *',
    '@every_second': '@second',  # snaptime-based; cron only goes to minutes.

    '@sunday': '0 0 * * sun',
    '@monday': '0 0 * * mon',
    '@tuesday': '0 0 * * tue',
    '@wednesday': '0 0 * * wed',
    '@thursday': '0 0 * * thu',
    '@friday': '0 0 * * fri',
    '@saturday': '0 0 * * sat',

    '@sundays': '@sunday',
    '@mondays': '@monday',
    '@tuesdays': '@tuesday',
    '@wednesdays': '@wednesday',
    '@thursdays': '@thursday',
    '@fridays': '@friday',
    '@saturdays': '@saturday',

    '@every_sunday': '@sunday',
    '@every_monday': '@monday',
    '@every_tuesday': '@tuesday',
    '@every_wednesday': '@wednesday',
    '@every_thursday': '@thursday',
    '@every_friday': '@friday',
    '@every_saturday': '@saturday',
}


@attrs
class TimeSetBuilder(object):
    """Class that allows for human interpretable job specifications.

    The focus here is on being human-interpretable.
    """

    # At most one of the following should be non-None at a time.
    at_times: MayaDT = attr(default=None)

    snap_instruction: str = attr(default=None)

    cron_pattern: str = attr(default=None)

    @staticmethod
    def create(pattern):
        """Attempt to construct a TimeSetBuilder from the given pattern string."""
        pattern = pattern.strip()

        # (Case 1) Apply any aliases.
        while pattern in PATTERN_ALIASES:
            pattern = PATTERN_ALIASES[pattern]
        # Some aliases are for invalid concepts and provide an exception to raise.
        if isinstance(pattern, UnsupportedTimeSetError):
            raise pattern

        # (Case 2) Attempt to parse as a cron pattern using croniter.
        try:
            croniter.croniter.expand(pattern)
        except croniter.CroniterBadCronError:
            # Most likely not intended as a cron pattern.
            # Continue on to try other patterns.
            pass
        except croniter.CroniterBadDateError:
            raise UnsupportedTimeSetError(
                "'%s' appears to be a malformed cron pattern (BadDate)." % pattern
            )
        except croniter.CroniterNotAlphaError:
            raise UnsupportedTimeSetError(
                "'%s' appears to be a malformed cron pattern (NotAlpha)." % pattern
            )
        else:
            return TimeSetBuilder().from_cron_pattern(pattern)

        # (Case 3) Attempt to parse as a snaptime command
        try:
            snaptime.main.parse(pattern)
        except snaptime.main.SnapParseError:
            # Most likely not intended as a snaptime pattern.
            # Continue on to try other patterns.
            pass
        except snaptime.main.SnapUnitError as e:
            pass
        else:
            return TimeSetBuilder().from_snap_instruction(pattern)

        # (Case 4) Attempt to parse as a tzolkin command sequence.
        # This is by far the most complex case, since it can invoke any part of the
        # builder implicitly.
        try:
            # TODO(woursler): Snaptime?
            parsed_commands = TzolkenCommandParser.parse(pattern)

            builder = TimeSetBuilder()
            for command in parsed_commands.commands:
                if command.is_explicit_alias:
                    builder = TimeSetBuilder.create("@" + command.identifier)
                else:
                    builder = getattr(
                        builder,
                        command.identifier
                    )(
                        *command.args,
                        **command.kwargs
                    )

            return builder
        except parsimonious.exceptions.ParseError:
            # Most likely not intended as a tzolkin command.
            pass

        # At this point, we're out of ideas.
        raise UnsupportedTimeSetError(
            "Unable to find a parser for '%s'." % pattern
        )

    # TODO(woursler): python-crontab integration. Allow for the builder to use
    # python-crontab's job directly?
    # May need to port into a CronPatternBuilder --
    # not clear if things work similarly (e.g. evolve)

    # TODO(woursler): xatu integration...
    # i.e. schedule.after(3*s).do(...)
    def build(self) -> TimeSet:
        """Build the TimeSet described by this builder."""
        # TODO(woursler): Verify at most one TimeSet? Trust builders?

        if self.at_times is not None and len(self.at_times) == 1:
            return SingletonTimeSet(min(self.at_times))
        if self.at_times is not None:
            return ExplicitTimeSet(self.at_times)
        if self.snap_instruction is not None:
            return SnapTimeSet(self.snap_instruction)
        if self.cron_pattern is not None:
            return CronPatternTimeSet(self.cron_pattern)
        raise NotImplementedError(
            "Unable to determine a unique TimeSet. " +
            "Please check the docs for supported builder patterns."
        )

    def _evolve(self, **kwargs):
        return attrevolve(self, **kwargs)

    def at_all(self, times: Set[MayaDT]):
        # TODO(woursler): Verify no conflicting timespec set...
        return self._evolve(at_times=times)

    def from_snap_instruction(self, snap_instruction: str):
        # TODO(woursler): Verify no conflicting timespec set...
        # TODO(woursler): Verify that the instruction parses?
        return self._evolve(snap_instruction=snap_instruction)

    def from_cron_pattern(self, cron_pattern: str):
        # TODO(woursler): Verify no conflicting timespec set...
        # TODO(woursler): Verify that the pattern parses?
        return self._evolve(cron_pattern=cron_pattern)

    # TODO(woursler): Other _evolve-based methods...

    def at(self, time: MayaDT):
        """Create a singleton job to run at a particular timestep."""
        # TODO(woursler): Support things like at("2:35 PM")
        # effectively a cron pattern for every day at 2:35 PM
        return self.at_all(set([time]))

    # TODO(woursler) .and_at(time) ? Confusing semantics with .at().and_at().add()

    def after(self, duration=None, **kwargs):
        """Use MayaDT.add to make a singleton timeset after the current time.

        e.g.

        >>> ROOT.after(seconds=2)
        >>> ROOT.at(event_time).after(seconds=10)

        Note: after affects ALL times in the builder, not just the most recent.
        """

        # TODO(woursler): Also need to view this as a delay for cron / snaptime.

        if duration is not None:
            kwargs = {
                'seconds': parse_duration(duration)
            }
        if self.at_times is None:
            return self.at(maya.now()).after(**kwargs)
        else:
            return self.add(**kwargs)

    def add(self, **kwargs):
        """Maps MayaDT.add across self.at_times.

        Note: after affects ALL times in the builder, not just the most recent.
        """
        assert self.at_times is not None
        return self.at_all(set(time.add(**kwargs) for time in self.at_times))

    def snap(self, snap_instruction):
        # TODO(woursler): Include TZ?

        # Modify existing snap instructions by appending.
        if self.snap_instruction is not None:
            return self._snap_instruction(self.snap_instruction + snap_instruction)

        # Modify the set of times by snapping each time according to the pattern.
        if self.at_times is not None:
            return self.at_all(set(time.snap(snap_instruction) for time in self.at_times))

        raise NotImplementedError(
            "TimeSetBuilder does not specify anything which can be snapped. " +
            "If you are trying to create a snap-based pattern, use every() instead."
        )

    def every(self, snap_instruction):
        # TODO(woursler): Make this work using SnapTimePattern?
        # TODO(woursler): Allow for every('second') syntax...
        # TODO(woursler): every 5 seconds? Not currently supported by snap time.
        return self.from_snap_instruction(snap_instruction)


def parse_time_set(pattern: str):
    return TimeSetBuilder.create(pattern).build()
