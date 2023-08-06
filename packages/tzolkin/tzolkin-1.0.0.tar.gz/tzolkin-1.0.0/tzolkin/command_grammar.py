import os
import parsimonious
from attr import attr, attrs
from typing import List

TZOLKEN_COMMAND_GRAMMAR_FILENAME = os.path.join(
    os.path.dirname(__file__),
    'command.grammar'
)

with open(TZOLKEN_COMMAND_GRAMMAR_FILENAME) as recipe_grammar_file:
    TZOLKEN_COMMAND_GRAMMAR = parsimonious.grammar.Grammar(
        recipe_grammar_file.read()
    )


@attrs(repr=False)
class TzolkinCommandArgument:
    value = attr()
    name = attr(default=None)

    def __repr__(self):
        if self.name is None:
            return '(%s)' % self.value
        else:
            return '(%s=%s)' % (self.name, self.value)


@attrs(repr=False)
class TzolkinCommand:
    identifier: str = attr()
    arguments: List[TzolkinCommandArgument] = attr(factory=list)
    is_explicit_alias = attr(default=False)

    @property
    def args(self):
        return [
            arg.value
            for arg in self.arguments
            if arg.name is None
        ]

    @property
    def kwargs(self):
        kwargs = {}
        for arg in self.arguments:
            if arg.name is None:
                continue
            if arg.name in kwargs:
                raise ValueError("Repeated keyword argument.")
            kwargs[arg.name] = arg.value
        return kwargs

    def __repr__(self):
        if self.is_explicit_alias:
            assert len(self.arguments) == 0
            return '@%s' % self.identifier
        else:
            return '%s%s' % (
                self.identifier,
                ''.join(map(repr, self.arguments))
            )


@attrs(repr=False)
class TzolkinCommands:
    commands: List[TzolkinCommand] = attr(factory=list)

    def __repr__(self):
        return 'TzolkinCommands(%s)' % '.'.join(map(repr, self.commands))


class TzolkenCommandParser:
    """A generic class for traversing parse trees / ASTs."""

    @classmethod
    def parse(cls, timeset_string):
        return cls().visit(
            TZOLKEN_COMMAND_GRAMMAR.parse(timeset_string.strip())
        )

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.expr_name
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # noqa: D102
        children = [
            self.visit(child)
            for child in node.children
        ]
        children = list(children)

        if len(children) == 0 and node.expr_name == '':
            return None
        return (node.expr_name, children)

    def visit_literal(self, node) -> str:  # noqa: D102
        return node.text

    def visit_identifier(self, node) -> str:  # noqa: D102
        return node.text

    def visit_timeset(self, node):  # noqa: D102
        _, params = self.generic_visit(node)
        first = params[0][1][0]
        rest = params[2]
        if rest is None:
            rest = []
        else:
            rest = list(map(
                lambda command: command[1][2],
                rest[1]
            ))
        return TzolkinCommands([first] + rest)

    def visit_alias(self, node):  # noqa: D102
        _, params = self.generic_visit(node)
        return TzolkinCommand(
            identifier=params[1],
            is_explicit_alias=True,
        )

    def visit_command(self, node):  # noqa: D102
        _, params = self.generic_visit(node)
        arglist = params[1]
        if arglist is None:
            arglist = []
        else:
            arglist = list(map(
                lambda arg: arg[1][1],
                arglist[1]
            ))
        return TzolkinCommand(
            identifier=params[0],
            arguments=arglist,
        )

    def visit_argument(self, node):
        _, params = self.generic_visit(node)
        kw = params[2]
        if kw is not None:
            kw = kw[1][0][1][0]
        return TzolkinCommandArgument(
            name=kw,
            value=params[3].strip()
        )
