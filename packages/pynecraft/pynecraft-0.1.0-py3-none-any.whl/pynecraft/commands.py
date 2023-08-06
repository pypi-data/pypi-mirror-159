"""
Mechanisms for writing Minecraft commands in python. The idea is twofold:

1. To allow syntax checking and other regular language tooling for checking the commands.
2. To provide simplified syntax. Some of that is here, and some in the simpler package.
"""

from __future__ import annotations

import copy
import re
import textwrap
from abc import ABC
from collections import UserDict, UserList
from functools import wraps
from pathlib import Path
from typing import Callable, Iterable, Mapping, Optional, Tuple, TypeVar, Union

from .base import BLUE, COLORS, ColumnPosition, Coord, DIMENSION, GREEN, IntColumnPos, JSON_COLORS, JsonHolder, Nbt, \
    NbtDef, PINK, PURPLE, Position, RED, RelCoord, TIME_SPEC, TIME_TYPES, Time, WHITE, YELLOW, _ToMinecraftText, _bool, \
    _ensure_size, _float, _in_group, _not_ify, _quote, _to_list, good_facing, good_name, good_names, good_resource, \
    good_resource_path, good_resources, to_id, to_name
from .enums import Advancement, Effect, Enchantment, GameRule, Particle, ScoreCriteria, TeamOption

_user_re = re.compile(r'\w+$')
_uuid_re = re.compile(r'(?:[a-fA-F0-9]+-){3}[a-fA-F0-9]+$')
_time_re = re.compile(r'[0-9]+(\.[0-9]+)?[dst]?$')
_team_re = re.compile(r'[\w+.-]{1,16}$')
_display_name_re = re.compile('[A-Z |]')
_slot_re = re.compile(r'\w+(\.\d+)?')
_axes_re = re.compile(r'^[xyz]+')


def _fluent(method):
    @wraps(method)
    def inner(self, *args, **kwargs):
        obj = copy.deepcopy(self)
        return method(obj, *args, **kwargs)

    return inner


def _score_strs(*scores: ScoreName) -> [str, ...]:
    return (str(good_score(x)) for x in scores)


def good_target(target: Target) -> TargetSpec | None:
    """Checks if the argument is a valid target for commands, such as (the equivaent of) '@p' or user names,
    or None. If not, it raises a ValueError.

    Valid targets are subclasses of TargetSpec, a '*', or a user name.
    :param target: The (probable) target.
    :return: a TargetSpec object, created if need be, or None.
    """
    if target is None:
        return None
    if isinstance(target, TargetSpec):
        return target
    elif target == '*':
        return Star()
    else:
        try:
            return User(target)
        except TypeError:
            raise ValueError(f'{target}: Invalid target')


def good_data_target(dt: DataTarget | None) -> Iterable[any] | None:
    """Checks if the argument is a valid data target for commands like `data merge`, or None. If not, it raises ValueError.

    A tuple or list argument is presumed to be intended as a position on which good_position will be called; a
    TargetSpec is an entity target, and a string is presumed to be intended as a resource path.

    :param dt: The (probable) data target.
    :return: a tuple, whose first value is 'block', 'entity', or 'storage', and whose second element is an appropriate object: the result of good_position for 'block', the TargetSpec input for 'entity', the result of good_resource_path on a string. A None argument returns None.
    """
    if dt is None:
        return None
    if isinstance(dt, (tuple, list)):
        return 'block', *good_position(dt)
    if isinstance(dt, TargetSpec):
        return 'entity', dt
    if isinstance(dt, str):
        return 'storage', good_resource_path(dt)
    raise ValueError(f'{dt}: Invalid data target (must be position, entity selector, or resource name)')


def data_target_str(data_target: DataTarget) -> str:
    """Returns a single string for a target, as returned by good_data_target.

    :param data_target: The data target.
    :return: A single string, such as 'block 1 2 3'.
    """
    return ' '.join(str(x) for x in good_data_target(data_target))


def good_position(pos: Position) -> Position:
    """Checks if the argument is a valid position.

    A valid position is a tuple or list of three numbers and/or RelCoords.

    :param pos: The (probable) position.
    :return: The input value.
    """
    if isinstance(pos, (tuple, list)):
        if len(pos) != 3:
            raise ValueError(f'{pos}: Position must have 3 values')
        for c in pos:
            if not isinstance(c, (int, float, RelCoord)):
                raise ValueError(f'{c}: not a coordinate')
        return pos
    raise ValueError(f'{str(pos)}: Invalid position')


def good_user(name: str) -> str:
    """Checks if the argument is a valid user name.

    :param name: The (probable) user name.
    :return: The input value.
    """
    if not _user_re.match(name):
        raise ValueError(f'{name}: Invalid user name')
    return name


def good_uuid(uuid: str) -> str:
    """Checks if the string is a valid UUID as four numbers separated by dashes.

    :param uuid: The (probable) uuid.
    :return: the input value.
    """
    if not _uuid_re.match(uuid):
        raise ValueError(f'{uuid}: Invalid UUID string')
    return uuid


def good_team(team: str) -> str | None:
    """Checks if the argument is a valid team name, or None.

    :param team: The (probable) team name.
    :return: The input value.
    """
    if team is None:
        return team
    if not _team_re.match(team):
        raise ValueError(f'{team}: Invalid team name')
    return team


def good_time(time: Time) -> Time | None:
    """Checks if the argument is a valid time duration specification, or None.

    A valid time is an int, which is in game ticks, or a string that is a number followed by a 't' (ticks),
    's' (seconds), or 'd' (days).

    :param time: The (probable) duration.
    :return: The input value.
    """
    if time is None:
        return time
    if isinstance(time, int):
        return time
    if not _time_re.match(time):
        raise ValueError(f'{time}: Invalid time')
    return time


def good_range(range: Range) -> str:
    """Checks if the argument is a valid numeric range.

     "Valid" means a single number, or a two-element list or tuple that define the endpoints. One of the
     endpoints may be None to define an open end.

    :param range: The (probable) range.
    :return: A string for the range, either the single number of a range using
    '..' between the two values.
    """
    if isinstance(range, float) or isinstance(range, int):
        return str(range)
    s = '' if range[0] is None else range[0]
    e = '' if range[1] is None else range[1]
    if isinstance(s, float) and isinstance(e, float) and s > e:
        raise ValueError('Start is greater than end')
    return str(s) + '..' + str(e)


def good_block(block: BlockDef | None) -> Block | None:
    """Checks if the argument is a valid block specification, or None.

    "Valid" means a string block name, or valid arguments to the Block constructor.

    :param block: The (probable) block.
    :return: a Block object for the argument, or None.
    """
    if block is None:
        return None
    if isinstance(block, str):
        return Block(block)
    if isinstance(block, Iterable):
        return Block(*block)
    return block


def good_entity(entity: EntityDef | None) -> Entity | None:
    """Checks if the argument is a valid entity specification, or None.

    "Valid" means a string entity name, or valid arguments to the Entity constructor.

    :param entity: The (probable) entity
    :return: an Entity object for the argument, or None.
    """
    if entity is None:
        return None
    if isinstance(entity, str):
        return Entity(entity)
    if isinstance(entity, Iterable):
        return Entity(*entity)
    return entity


def good_score(score: ScoreName | None) -> Score | None:
    """Checks if the argument is a valid score, or None.

    "Valid" means a Score object, or a target/objective pair in a tuple or list.

    :param score: The (probable) score.
    :return: a Score object, or None.
    """
    if score is None:
        return score
    if isinstance(score, Score):
        return score
    if not isinstance(score, str):
        return Score(score[0], score[1])
    raise ValueError(f'{str(score)}: Invalid score')


def commands(*commands: str | Command) -> str:
    """Return a single multiline string for all the commands in the input."""
    return '\n'.join(str(x) for x in commands)


def good_color_num(color: int | str | None) -> int | None:
    """Checks if the argument is a valid color number specification, or None.

    "Valid" means an int, or a string that names a known color from which a color number can be inferred.
    Color numbers range from 0 to 15. (See `good_color` for a documentation on color names.)

    :param color:
    :return:
    """
    if color is None:
        return color
    if isinstance(color, str):
        color_num = COLORS.index(color)
        if color_num < 0:
            raise ValueError(f'{color}: Unknown color')
        return color_num
    if color not in range(0, len(COLORS)):
        raise ValueError(f'{color}: Unknown color')
    return color


def good_color(color: int | str | None) -> str | None:
    """Checks if the argument is a valid color name, or None.

    "Valid" means one of the 16 known colors, such as those used for wool. These are stored in the
    `COLORS` array.

    :param color: The ((probable) color name.
    :return: the color name, in lower case.
    """
    if color is None:
        return color
    color_num = good_color_num(color)
    return COLORS[color_num]


def good_slot(slot: str | None) -> str | None:
    """Checks if the argument is a valid slot specification, or None.

    "Valid" means valid for the `item` command.

    :param slot: The (probable) slot name.
    :return: the input value.
    """
    if slot is None:
        return None
    if not _slot_re.match(slot):
        raise ValueError(f'{slot}: Bad slot specification')
    return slot


NEAREST = 'nearest'
FURTHEST = 'furthest'
RANDOM = 'random'
ARBITRARY = 'arbitrary'
SORT = [NEAREST, FURTHEST, RANDOM, ARBITRARY]
"""Valid ways to sort target specifications."""

SURVIVAL = 'survival'
CREATIVE = 'creative'
ADVENTURE = 'adventure'
SPECTATOR = 'spectator'
GAMEMODE = [SURVIVAL, CREATIVE, ADVENTURE, SPECTATOR]
"""Valid game modes."""

EYES = 'eyes'
FEET = 'feet'
ENTITY_ANCHOR = [EYES, FEET]
"""Valid entity anchors."""

ALL = 'all'
MASKED = 'masked'
SCAN_MODE = [ALL, MASKED]
"""Valid scan modes for blocks subpart of /execut commands."""

FORCE = 'force'
MOVE = 'move'
NORMAL = 'normal'
CLONE_FLAGS = [FORCE, MOVE, NORMAL]
"""Valid clone flags."""

RESULT = 'result'
SUCCESS = 'success'
STORE_WHAT = [RESULT, SUCCESS]
"""Valid things to store from /execute commands."""

BYTE = 'byte'
SHORT = 'short'
INT = 'int'
LONG = 'long'
FLOAT = 'float'
DOUBLE = 'double'
DATA_TYPE = [BYTE, SHORT, INT, LONG, FLOAT, DOUBLE]
"""Valid data types."""

EVERYTHING = 'everything'
ONLY = 'only'
FROM = 'from'
THROUGH = 'through'
UNTIL = 'until'
ADVANCEMENT = [EVERYTHING, ONLY, FROM, THROUGH, UNTIL]
"""Valid behavior specifications for the /advancment command."""

VALUE = 'value'
MAX = 'max'
BOSSBAR = [VALUE, MAX]
"""Valid bossbar values for storage."""

COLOR = 'color'
MAX = 'max'
NAME = 'name'
PLAYERS = 'players'
STYLE = 'style'
VALUE = 'value'
VISIBLE = 'visible'
BOSSBAR_VALUES = [COLOR, MAX, NAME, PLAYERS, STYLE, VALUE, VISIBLE]
"""Valid bossbar values."""

BOSSBAR_COLORS = [BLUE, GREEN, PINK, PURPLE, RED, WHITE, YELLOW]

NOTCHED_6 = 'notched_6'
NOTCHED_10 = 'notched_10'
NOTCHED_12 = 'notched_12'
NOTCHED_20 = 'notched_20'
PROGRESS = 'progress'
BOSSBAR_STYLES = [NOTCHED_6, NOTCHED_10, NOTCHED_12, NOTCHED_20, PROGRESS]
"""Valid bossbar styles."""

ENABLE = 'enable'
DISABLE = 'disable'
DATAPACK_ACTIONS = [ENABLE, DISABLE]
"""Valid actions on a datapack."""

FIRST = 'first'
LAST = 'last'
BEFORE = 'before_cmds'
AFTER = 'after_cmds'
ORDER = [FIRST, LAST, BEFORE, AFTER]
"""Valid command order specifications."""

AVAILABLE = 'available'
ENABLED = 'enabled'
DATAPACK_FILTERS = [AVAILABLE, ENABLED]
"""Valid data filter specifications."""

EASY = 'easy'
HARD = 'hard'
NORMAL = 'normal'
PEACEFUL = 'peaceful'
DIFFICULTIES = [EASY, HARD, NORMAL, PEACEFUL]
"""Valid difficulty levels."""

LEVELS = 'levels'
POINTS = 'points'
EXPERIENCE_POINTS = [LEVELS, POINTS]
"""Valid experience specifications for the /experience command."""

STRUCTURE = 'structure'
BIOME = 'biome'
POI = 'poi'
LOCATABLE = [STRUCTURE, BIOME, POI]
"""Valid categories of things for the /locate command."""

MAINHAND = 'mainhand'
OFFHAND = 'offhand'
HANDS = [MAINHAND, OFFHAND]
"""Valid hand names."""

DISPLAY_NAME = 'displayname'
RENDER_TYPE = 'rendertype'
SCOREBOARD_OBJECTIVES_MODIFIABLE = [DISPLAY_NAME, RENDER_TYPE]
"""Valid modifiable scoreboard objective values."""

HEARTS = 'hearts'
INTEGER = 'integer'
SCOREBOARD_RENDER_TYPES = [HEARTS, INTEGER]
"""Valid scoreboard render values."""

LIST = 'list'
SIDEBAR = 'sidebar'
BELOW_NAME = 'belowName'
DISPLAY_SLOTS = [LIST, SIDEBAR, BELOW_NAME]
"""Valid scoreboard dispay slots."""

SIDEBAR_TEAM = 'sidebar.team.'

LT = '<'
LE = '<='
EQ = '='
GE = '>='
GT = '>'
RELATION = [LT, LE, EQ, GE, GT]

PLUS = '+='
MINUS = '-='
MULT = '*='
DIV = '/='
MOD = '%='
MIN = '<'
# 'MAX' has another value, so special casing required
SWAP = '><'
SCORE_OPERATIONS = [PLUS, MINUS, MULT, DIV, MOD, EQ, MIN, MAX, SWAP]

PARTICLE_MODES = [FORCE, NORMAL]

REPLACE = 'replace'
APPEND = 'append'
SCHEDULE_ACTIONS = [APPEND, REPLACE]

DESTROY = 'destroy'
KEEP = 'keep'
SETBLOCK_ACTIONS = [DESTROY, KEEP, REPLACE]

NEVER = 'never'
HIDE_FOR_OTHER_TEAMS = 'hideForOtherTeams'
HIDE_FOR_OWN_TEAM = 'hideForOwnTeam'
ALWAYS = 'always'
NAMETAG_VISIBILITY_VALUES = [NEVER, HIDE_FOR_OTHER_TEAMS, HIDE_FOR_OWN_TEAM, ALWAYS]
DEATH_MESSAGE_VISIBILITY_VALUES = NAMETAG_VISIBILITY_VALUES

PUSH_OTHER_TEAMS = 'pushOtherTeams'
PUSH_OWN_TEAM = 'pushOwnTeam'
COLLISION_RULE_VALUES = [NEVER, PUSH_OTHER_TEAMS, PUSH_OWN_TEAM, ALWAYS]

CLEAR = 'clear'
RESET = 'reset'
TITLE = 'title'
SUBTITLE = 'subtitle'
ACTION_BAR = 'actionbar'
TITLE_GIVEN = [TITLE, SUBTITLE, ACTION_BAR]
TITLE_ACTIONS = [CLEAR, RESET] + TITLE_GIVEN

RAIN = 'rain'
THUNDER = 'thunder'
WEATHER_TYPES = [CLEAR, RAIN, THUNDER]

BOOTS = 'boots'
LEGGINGS = 'leggings'
CHESTPLATE = 'chestplate'
HELMET = 'helmet'
LEFT = 'left'
RIGHT = 'right'
ENTITY_PLACES = [BOOTS, LEGGINGS, CHESTPLATE, HELMET, LEFT, RIGHT]

GIVE = 'give'
GIVE_CLEAR = [GIVE, CLEAR]

TAKE = 'take'
GIVE_TAKE = [GIVE, TAKE]

GRANT = 'grant'
REVOKE = 'revoke'
GRANT_REVOKE = [GRANT, REVOKE]

GIVELIKE = [GIVE, GRANT]
CLEARLIKE = [CLEAR, REVOKE, TAKE]

GIVE_GRANT = GIVE_CLEAR + GRANT_REVOKE

MAX_EFFECT_SECONDS = 1000000

NOT_GIVEN = 'notGiven'
"""Marker value used for None when that would be ambiguous"""


def _to_donate(action: str, group_list: list[str]):
    if action in GIVELIKE:
        return group_list[0]
    elif action in CLEARLIKE:
        return group_list[1]
    _in_group(group_list, action)


class Command:
    """
    Base class for all command parts. It builds up the string version of the command through the various calls.
    """

    def __init__(self):
        self._rep = ''

    def __str__(self):
        return self._rep.strip()

    def __eq__(self, other):
        return type(self) == type(other) and str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    def clone(self: T) -> T:
        """Returns a deep copy of this object."""
        return copy.deepcopy(self)

    def _add(self, *objs: any, space: object = True):
        s = ' '.join(str(x) for x in map(lambda x: _float(x) if isinstance(x, float) else x, objs))
        if not self._rep:
            self._rep = ''
        elif space and not self._rep.endswith(' '):
            self._rep += ' '
        self._rep += s

    def _add_if(self, s: str):
        if self._rep:
            self._rep += s

    def _add_opt(self, *objs: any):
        for o in objs:
            if o is not None:
                self._add(o)

    def _add_opt_pos(self, pos: Position = None):
        if pos is not None:
            self._add_opt(*pos)

    def _start(self, start: T) -> T:
        start._rep = self._rep + ' '
        return start


T = TypeVar('T', bound=Command)


class _ScoreClause(Command):
    @_fluent
    def is_(self, relation: str, score: ScoreName) -> _ExecuteMod:
        self._add(_in_group(RELATION, relation), good_score(score))
        return self._start(_ExecuteMod())

    @_fluent
    def matches(self, range: Range) -> _ExecuteMod:
        self._add('matches', good_range(range))
        return self._start(_ExecuteMod())


class _AdvancementCriteria(Command):
    def __init__(self, advancement: Advancement | str, criteria: bool | tuple[str, bool]):
        super().__init__()
        advancement = Advancement(advancement)
        if isinstance(criteria, bool):
            self._add(f'{advancement}={_bool(criteria)}')
        else:
            self._add(f'{advancement}={{{good_resource_path(criteria[0])}={_bool(criteria[1])}}}')


class _JsonTextMod:
    def __init__(self, jt: JsonText, ev: NbtDef):
        self._jt = jt
        self._ev = ev


class _JsonTextHoverAction(_JsonTextMod):
    def show_text(self, txt: JsonText | str) -> JsonText:
        self._ev['action'] = 'show_text'
        self._ev['contents'] = txt
        return self._jt

    def show_item(self, id: str, count: int = None, tag: str = None) -> JsonText:
        self._ev['action'] = 'show_item'
        self._ev['id'] = good_resource(id)
        if count is not None:
            self._ev['count'] = count
        if tag is not None:
            self._ev['tag'] = tag
        return self._jt

    def show_entity(self, type: str, uuid: str, name: JsonText | str = None) -> JsonText:
        self._ev['action'] = 'show_entity'
        self._ev['type'] = good_resource(type)
        self._ev['id'] = good_uuid(uuid)
        if name is not None:
            self._ev['name'] = name
        return self._jt


class _JsonTextClickEventAction(_JsonTextMod):
    def open_url(self, url: str) -> JsonText:
        self._ev.update({'action': 'open_url', 'value': url})
        return self._jt

    def open_file(self, path: str) -> JsonText:
        Path(path)
        self._ev.update({'action': 'open_file', 'value': path})
        return self._jt

    @staticmethod
    def _good_command(command):
        if not isinstance(command, str):
            command = str(command)
        return command.strip()

    def run_command(self, command: str | Command) -> JsonText:
        command = self._good_command(command)
        # The '/' is optional for signs, but required every else, so this is safest
        if command[0] != '/':
            command = '/' + command
        self._ev.update({'action': 'run_command', 'value': command})
        return self._jt

    def suggest_command(self, chat: str | Command) -> JsonText:
        self._good_command(chat)
        self._ev.update({'action': 'suggest_command', 'value': chat})
        return self._jt

    def change_page(self, page: str) -> JsonText:
        self._ev.update({'action': 'change_page', 'value': page})
        return self._jt

    def copy_to_clipboard(self, txt: str) -> JsonText:
        self._ev.update({'action': 'copy_to_clipboard', 'value': txt})
        return self._jt


class TargetSpec(Command, ABC):
    """Superclass of all target specification classes."""
    pass


class User(TargetSpec):
    """A user name as a target."""

    def __init__(self, name: str):
        super().__init__()
        good_user(name)
        self._add(name)


class Uuid(TargetSpec):
    """A uuid as a target."""

    def __init__(self, u1: int, u2: int, u3: int, u4: int):
        super().__init__()
        self._add([u1, u2, u3, u4])


class Star(TargetSpec):
    def __init__(self):
        super().__init__()
        self._add('*')


# noinspection PyProtectedMember
def p():
    """A target selector for `@p`."""
    return Selector(Selector._create_key, '@p')


# noinspection PyProtectedMember
def random():
    """A target selector for `@r`. (No single-character version of this exists because it interferes with the `r()`
    function that returns relative coordinates.) """
    return Selector(Selector._create_key, '@r')


# noinspection PyProtectedMember
def a():
    """A target selector for `@a`."""
    return Selector(Selector._create_key, '@a')


# noinspection PyProtectedMember
def e():
    """A target selector for `@e`."""
    return Selector(Selector._create_key, '@e')


# noinspection PyProtectedMember
def s():
    """A target selector for `@s`."""
    return Selector(Selector._create_key, '@s')


def entity():
    """Equivalent to `e()`."""
    return e()


def player():
    """Equivalent to `p()`."""
    return p()


def all_():
    """Equivalent to `a()`."""
    return a()


class Selector(TargetSpec):
    """This class represents a target selector. You start with one of the selector methods `p`, `random`, `s`, `a`,
    and `e`, and then possibly add qualifiers from the methods here. These can be chained, so for example,
    `e().tag("foo").limit( 1)` is equivalent to the minecraft target selector `@e[tag=foo,limit=1]`. """
    _create_key = object()

    def __init__(self, create_key, selector):
        super().__init__()
        assert (create_key == Selector._create_key), 'Private __init__, use creation methods'
        self._selector = selector
        self._args = {}

    def __str__(self):
        if len(self._args) == 0:
            return self._selector
        return self._selector + '[' + super().__str__() + ']'

    @_fluent
    def literal(self, string: str):
        """Allow user to add literal text in the selector arguments. No checks."""
        self._append(string)

    def _add_arg(self, key: str, value: any):
        v = str(value)
        if v.find('=') < 0 or v[0] == '{':
            v = f'{key}={v}'
        if key in self._args:
            self._args[key] += ',' + v
        else:
            self._args[key] = v
        self._append(v)
        return self

    def _append(self, v):
        self._add_if(',')
        self._add(v)

    def _unique_arg(self, key: str, value: any):
        if key in self._args:
            raise KeyError(f'{key}: Already set in target')
        self._add_arg(key, value)
        return self

    def _multi_args(self, key: str, value: any, values):
        self._add_arg(key, value)
        for v in values:
            self._add_arg(key, v)
        return self

    def _not_args(self, key: str, value, values):
        self._add_arg(key, _not_ify(value))
        for v in values:
            self._add_arg(key, _not_ify(v))
        result = self._args[key]
        value_count = result.count('=')
        neg_count = result.count('!')
        if value_count > 1 and neg_count != value_count:
            raise KeyError(f'{key}: Cannot repeat unless all are negated: {result}')
        return self

    @_fluent
    def pos(self, pos: Position) -> Selector:
        """Add an x,y,z position to the selector."""
        return self._unique_arg('pos', 'x=%s,y=%s,z=%s' % pos)

    @_fluent
    def distance(self, distance: Range) -> Selector:
        """Add a distance (radius) to the selector."""
        return self._unique_arg('distance', good_range(distance))

    @_fluent
    def volume(self, values: Tuple[float, float, float]) -> Selector:
        """Add a volume to the selector. Must have three values in the list or tuple."""
        dx, dy, dz = values
        return self._unique_arg('delta', f'dx={str(dx)},dy={str(dy)},dz={str(dz)}')

    @_fluent
    def scores(self, *score_specs: str) -> Selector:
        """Add one or more score criteria to the selector."""
        return self._unique_arg('score_specs', '{' + ','.join(score_specs) + '}')

    @_fluent
    def tag(self, tag: str, *tags: str) -> Selector:
        """Add one or more tags to the selector. You can use '!' for 'not'."""
        return self._multi_args('tag', good_name(tag, allow_not=True), good_names(*tags, allow_not=True))

    @_fluent
    def not_tag(self, tag: str, *tags: str) -> Selector:
        """Add one or more 'not' tags to the selector. You need not specify the '!' in the string."""
        return self.tag(_not_ify(good_name(tag, allow_not=True)), *_not_ify(good_names(*tags, allow_not=True)))

    @_fluent
    def team(self, team: str) -> Selector:
        """Add a team to the selector."""
        return self._unique_arg('team', good_name(team, allow_not=True))

    @_fluent
    def not_team(self, team: str, *teams) -> Selector:
        """Add one or more 'not' teams to the selector. You need not specify the '!' in the string."""
        return self._not_args('team', good_name(team, allow_not=True), good_names(*teams, allow_not=True))

    @_fluent
    def sort(self, sorting: str) -> Selector:
        """Add a sort criteria to the selector."""
        return self._unique_arg('sort', _in_group(SORT, sorting))

    @_fluent
    def limit(self, limit: int) -> Selector:
        """Add a result limit to the selector."""
        return self._unique_arg('limit', str(limit))

    @_fluent
    def level(self, level_range: Range) -> Selector:
        """Add a level range to the selector."""
        return self._unique_arg('level', good_range(level_range))

    @_fluent
    def gamemode(self, gamemode: str) -> Selector:
        """Add a gamemode to the selector."""
        return self._unique_arg('gamemode', _in_group(GAMEMODE, gamemode))

    @_fluent
    def not_gamemode(self, gamemode: str, *gamemodes: str) -> Selector:
        """Add one or more 'not' gamemodes to the selector. You need to specify the '!' in the string."""
        _in_group(GAMEMODE, gamemode)
        for g in gamemodes:
            _in_group(GAMEMODE, g)
        return self._not_args('gamemode', gamemode, gamemodes)

    @_fluent
    def name(self, name: str) -> Selector:
        """Add a name criteria to the selector."""
        return self._unique_arg('name', good_name(name, allow_not=True))

    @_fluent
    def not_name(self, name: str, *names: str) -> Selector:
        """Add one or more 'not' names to the selector. You need to specify the '!' in the string."""
        return self._not_args('name', good_name(name, allow_not=True), good_names(*names, allow_not=True))

    @_fluent
    def x_rotation(self, rot_range: Range) -> Selector:
        """Add an X rotation to the selector."""
        return self._unique_arg('x_rotation', good_range(rot_range))

    @_fluent
    def y_rotation(self, rot_range: Range) -> Selector:
        """Add a Y rotation to the selector."""
        self._unique_arg('y_rotation', good_range(rot_range))
        return self

    @_fluent
    def type(self, type_: str) -> Selector:
        """Add a type to the selecctor."""
        return self._unique_arg('type', good_resource(type_, allow_not=True))

    @_fluent
    def not_type(self, type_: str, *types: str):
        """Add one or more 'not' types to the selector. You need to specify the '!' in the string."""
        return self._not_args('type', good_resource(type_, allow_not=True), good_resources(*types, allow_not=True))

    @_fluent
    def nbt(self, nbt: NbtDef, *nbts: NbtDef) -> Selector:
        """Add NBT criteria to the selector."""
        return self._multi_args('nbt', Nbt.as_nbt(nbt), (Nbt.as_nbt(x) for x in nbts))

    @_fluent
    def advancements(self, advancement: _AdvancementCriteria, *advancements: _AdvancementCriteria) -> Selector:
        """Add advancements to the selector."""
        adv = [advancement, ]
        for a in advancements:
            adv.append(a)
        return self._unique_arg('advancements', '{' + ','.join(str(x) for x in adv) + '}')

    @_fluent
    def predicate(self, predicate: str, *predicates: str) -> Selector:
        """Add a predicate to the selector."""
        return self._multi_args('predicate', predicate, predicates)


class _IfClause(Command):
    @_fluent
    def block(self, pos: Position, block: BlockDef) -> _ExecuteMod:
        self._add('block', *pos, good_block(block))
        return self._start(_ExecuteMod())

    @_fluent
    def blocks(self, start_pos: Position, end_pos: Position, dest_pos: Position, mode: str) -> _ExecuteMod:
        self._add('blocks', *start_pos, *end_pos, *dest_pos, _in_group(SCAN_MODE, mode))
        return self._start(_ExecuteMod())

    @_fluent
    def data_block(self, pos: Position, nbt_path: str) -> _ExecuteMod:
        self._add('data', 'block', *pos, nbt_path)
        return self._start(_ExecuteMod())

    @_fluent
    def data_entity(self, target: Target, nbt_path: str) -> _ExecuteMod:
        self._add('data', 'entity', good_target(target), nbt_path)
        return self._start(_ExecuteMod())

    @_fluent
    def data_storage(self, source: str, nbt_path: str) -> _ExecuteMod:
        self._add('data', 'storage', source, nbt_path)
        return self._start(_ExecuteMod())

    @_fluent
    def entity(self, target: Target) -> _ExecuteMod:
        self._add('entity', good_target(target))
        return self._start(_ExecuteMod())

    @_fluent
    def predicate(self, predicate: str) -> _ExecuteMod:
        self._add('predicate', predicate)
        return self._start(_ExecuteMod())

    @_fluent
    def score(self, score: ScoreName) -> _ScoreClause:
        self._add('score', good_score(score))
        return self._start(_ScoreClause())


class _StoreClause(Command):
    @_fluent
    def block(self, pos: Position, nbt_path: str, data_type: str, scale: float) -> _ExecuteMod:
        self._add('block', *pos, nbt_path, _in_group(DATA_TYPE, data_type), scale)
        return self._start(_ExecuteMod())

    @_fluent
    def bossbar(self, id: str, param: str) -> _ExecuteMod:
        self._add('bossbar', id, _in_group(BOSSBAR, param))
        return self._start(_ExecuteMod())

    @_fluent
    def entity(self, target: Target, nbt_path: str, data_type: str, scale: float) -> _ExecuteMod:
        self._add('entity', good_target(target), nbt_path, _in_group(DATA_TYPE, data_type), scale)
        return self._start(_ExecuteMod())

    @_fluent
    def score(self, score: ScoreName) -> _ExecuteMod:
        self._add('score', good_score(score))
        return self._start(_ExecuteMod())

    @_fluent
    def storage(self, target: Target, nbt_path: str, data_type: str, scale: float) -> _ExecuteMod:
        self._add('storage', good_target(target), nbt_path, _in_group(DATA_TYPE, data_type), scale)
        return self._start(_ExecuteMod())


class _ExecuteMod(Command):
    @_fluent
    def align(self, axes: str) -> _ExecuteMod:
        if not _axes_re.match(axes):
            raise ValueError(f'{axes}: Must be combination of x, y, and/or z')
        self._add('align', axes)
        return self

    @_fluent
    def anchored(self, anchor: str) -> _ExecuteMod:
        self._add('anchored', _in_group(ENTITY_ANCHOR, anchor))
        return self

    @_fluent
    def as_(self, target: Target) -> _ExecuteMod:
        self._add('as', good_target(target))
        return self

    @_fluent
    def at(self, target: Target) -> _ExecuteMod:
        self._add('at', good_target(target))
        return self

    @_fluent
    def facing(self, pos: Position) -> _ExecuteMod:
        self._add('facing', *pos)
        return self

    @_fluent
    def facing_entity(self, target: Target, anchor: str) -> _ExecuteMod:
        self._add('facing entity', good_target(target), _in_group(ENTITY_ANCHOR, anchor))
        return self

    @_fluent
    def in_(self, dimension: str) -> _ExecuteMod:
        self._add('in', _in_group(DIMENSION, dimension))
        return self

    @_fluent
    def positioned(self, pos: Position) -> _ExecuteMod:
        self._add('positioned', *pos)
        return self

    @_fluent
    def positioned_as(self, target: Target) -> _ExecuteMod:
        self._add('positioned as', good_target(target))
        return self

    @_fluent
    def rotated(self, yaw: float, pitch: float) -> _ExecuteMod:
        self._add('rotated', yaw, pitch)
        return self

    @_fluent
    def rotated_as(self, target: Target) -> _ExecuteMod:
        self._add('rotated as', good_target(target))
        return self

    @_fluent
    def if_(self) -> _IfClause:
        self._add('if')
        return self._start(_IfClause())

    @_fluent
    def unless(self) -> _IfClause:
        self._add('unless')
        return self._start(_IfClause())

    @_fluent
    def store(self, what: str) -> _StoreClause:
        self._add('store', _in_group(STORE_WHAT, what))
        return self._start(_StoreClause())

    @_fluent
    def run(self, cmd: str | Command | Commands, *other_cmds: str | Command) -> str | tuple[str]:
        """
        If cmds is empty, expect the command to follow.
        Otherwise, return an 'execute' command for each element of cmds.
        If there is only one element, return a single string, otherwise return a tuple of them.
        """
        cmds = _to_list(cmd)
        cmds.extend(other_cmds)
        self._add('run')
        cmds = lines(*cmds)
        results = []
        for c in cmds:
            selfish = self.clone()
            selfish._add(str(c))
            results.append(str(selfish))
        if len(cmds) == 1:
            return results[0]
        return tuple(results)


class _AttributeBaseAct(Command):
    @_fluent
    def get(self, scale: float = None) -> str:
        self._add('get')
        if scale:
            self._add(scale)
        return str(self)

    @_fluent
    def set(self, value: float) -> str:
        self._add('set', value)
        return str(self)


class _AttributeModifierAct(Command):
    @_fluent
    def add(self, uuid: str, name: str, value: float) -> str:
        self._add('add', good_uuid(uuid), f'"{name}"', value)
        return str(self)

    @_fluent
    def remove(self, uuid: str) -> str:
        self._add('remove', good_uuid(uuid))
        return str(self)

    @_fluent
    def value(self, uuid: str, scale: float = None) -> str:
        self._add('value get', good_uuid(uuid))
        if scale:
            self._add(scale)
        return str(self)


class _AttributeAct(Command):
    @_fluent
    def get(self, scale: float = None) -> str:
        self._add('get')
        if scale:
            self._add(scale)
        return str(self)

    @_fluent
    def base(self) -> _AttributeBaseAct:
        self._add('base')
        return self._start(_AttributeBaseAct())

    @_fluent
    def modifier(self) -> _AttributeModifierAct:
        self._add('modifier')
        return self._start(_AttributeModifierAct())


class _BossbarSet(Command):
    @_fluent
    def color(self, color: str) -> str:
        self._add('color', _in_group(BOSSBAR_COLORS, color))
        return str(self)

    @_fluent
    def max(self, value: int) -> str:
        self._add('max', value)
        return str(self)

    @_fluent
    def name(self, name: str) -> str:
        self._add('name', name)
        return str(self)

    @_fluent
    def players(self, *targets: Target) -> str:
        targets = (good_target(x) for x in targets)
        self._add('players', *targets)
        return str(self)

    @_fluent
    def style(self, style: str) -> str:
        self._add('style', _in_group(BOSSBAR_STYLES, style))
        return str(self)

    @_fluent
    def value(self, value: int) -> str:
        self._add('value', value)
        return str(self)

    @_fluent
    def visible(self, visible: bool) -> str:
        self._add('visible', _bool(visible))
        return str(self)


class _BossbarAct(Command):
    @_fluent
    def add(self, id: str, name: str) -> str:
        self._add('add', good_resource(id), _quote(name))
        return str(self)

    @_fluent
    def get(self, id: str, which: str) -> str:
        self._add('get', good_resource(id), _in_group(BOSSBAR_VALUES, which))
        return str(self)

    @_fluent
    def list(self) -> str:
        self._add('list')
        return str(self)

    @_fluent
    def remove(self, id: str) -> str:
        self._add('remove', good_resource(id))
        return str(self)

    @_fluent
    def set(self, id: str, which: str, value: any) -> str:
        if isinstance(value, bool):
            value = _bool(value)
        elif which == NAME:
            value = _quote(value)
        self._add('set', good_resource(id), _in_group(BOSSBAR_VALUES, which), value)
        return str(self)


class _ClearClause(Command):
    @_fluent
    def item(self, item: str, max_count: int = None) -> str:
        self._add(item)
        if max_count:
            self._add(max_count)
        return str(self)


class _CloneClause(Command):
    def _flag(self, flag):
        if flag:
            self._add(_in_group(CLONE_FLAGS, flag))

    @_fluent
    def replace(self, flag: str = None) -> str:
        self._add('replace')
        self._flag(flag)
        return str(self)

    @_fluent
    def masked(self, flag: str = None) -> str:
        self._add('masked')
        self._flag(flag)
        return str(self)

    @_fluent
    def filtered(self, block: BlockDef, flag: str = None) -> str:
        self._add('filtered', good_block(block))
        self._flag(flag)
        return str(self)


class _End(Command):
    pass


class _FromOrValue(Command):
    @_fluent
    def from_(self, data_target: DataTarget, nbt_path: str) -> str:
        self._add('from', data_target_str(data_target), good_resource_path(nbt_path))
        return str(self)

    @_fluent
    def value(self, v: str | float | Nbt | Iterable[str | float | Nbt]) -> str:
        if isinstance(v, float):
            v = _float(v)
        self._add('value', Nbt.to_str(v))
        return str(self)


class _DataModifyClause(Command):
    def _keyword(self, keyword: str) -> _FromOrValue:
        self._add(keyword)
        return self._start(_FromOrValue())

    @_fluent
    def append(self) -> _FromOrValue:
        return self._keyword('append')

    @_fluent
    def insert(self, index: int) -> _FromOrValue:
        self._add('insert', index)
        return self._start(_FromOrValue())

    @_fluent
    def merge(self) -> _FromOrValue:
        return self._keyword('merge')

    @_fluent
    def prepend(self) -> _FromOrValue:
        return self._keyword('prepend')

    @_fluent
    def set(self) -> _FromOrValue:
        return self._keyword('set')


class _DataMod(Command):
    @_fluent
    def get(self, data_target: DataTarget, nbt_path: str = None, scale: float = None, /) -> str:
        self._add('get', data_target_str(data_target))
        if not nbt_path and scale is not None:
            raise ValueError('Must give dir to use scale')
        self._add_opt(nbt_path, scale)
        return str(self)

    @_fluent
    def merge(self, data_target: DataTarget, nbt: NbtDef) -> str:
        self._add('merge', data_target_str(data_target), Nbt.as_nbt(nbt))
        return str(self)

    @_fluent
    def modify(self, data_target: DataTarget, nbt_path: str) -> _DataModifyClause:
        self._add('modify', data_target_str(data_target), nbt_path)
        return self._start(_DataModifyClause())

    @_fluent
    def remove(self, data_target: DataTarget, nbt_path: str) -> str:
        self._add('remove', data_target_str(data_target), nbt_path)
        return str(self)


class _DatapackAction(Command):
    @_fluent
    def disable(self, name: str) -> str:
        self._add('disable', good_name(name))
        return str(self)

    @_fluent
    def enable(self, name, order: str = None, other_datapack: str = None) -> str:
        self._add('enable', name)
        if order:
            order = _in_group(ORDER, order)
            if order in (FIRST, LAST):
                self._add(order)
            else:
                if not other_datapack:
                    raise ValueError(f'"{order}" requires other_datapack value')
                self._add(order, other_datapack)
        return str(self)

    @_fluent
    def list(self) -> str:
        self._add('list')
        return str(self)


class _EffectAction(Command):
    @_fluent
    def give(self, target: Target, effect: Effect | str, seconds: int = None, amplifier: int = None,
             hide_particles: bool = None, /) -> str:
        if amplifier is not None and seconds is None:
            raise ValueError('must give seconds to use amplifier')
        if hide_particles is not None and amplifier is None:
            raise ValueError('must give amplifier to use hide_particles')
        seconds_range = range(0, MAX_EFFECT_SECONDS + 1)
        if seconds is not None and seconds not in seconds_range:
            raise ValueError(f'{seconds:d}: Not in range {seconds_range}')
        self._add('give', good_target(target), Effect(effect))
        self._add_opt(seconds, amplifier, _bool(hide_particles))
        return str(self)

    @_fluent
    def clear(self, target: Target = None, effect: Effect | str = None) -> str:
        if effect is not None and target is None:
            raise ValueError('must give target to use effect')
        self._add('clear')
        if isinstance(effect, str):
            effect = Effect(effect)
        self._add_opt(good_target(target), effect)
        return str(self)


class _ExperienceMod(Command):
    @_fluent
    def add(self, target: Target, amount: int, which: str) -> str:
        self._add('add', good_target(target), amount, _in_group(EXPERIENCE_POINTS, which))
        return str(self)

    @_fluent
    def set(self, target: Target, amount: int, which: str) -> str:
        self._add('set', good_target(target), amount, _in_group(EXPERIENCE_POINTS, which))
        return str(self)

    @_fluent
    def query(self, target: Target, which: str) -> str:
        self._add('query', good_target(target), _in_group(EXPERIENCE_POINTS, which))
        return str(self)


class _FilterClause(Command):
    @_fluent
    def replace(self, filter: str = None) -> str:
        self._add('replace')
        self._add_opt(filter)
        return str(self)

    @_fluent
    def destroy(self) -> str:
        self._add('destroy')
        return str(self)

    @_fluent
    def hollow(self) -> str:
        self._add('hollow')
        return str(self)

    @_fluent
    def keep(self) -> str:
        self._add('keep')
        return str(self)

    @_fluent
    def outline(self) -> str:
        self._add('outline')
        return str(self)


class _ForceloadMod(Command):
    def _to_from(self, action: str, start, end):
        self._add(action, *start)
        if end:
            self._add(*end)
        return str(self)

    @_fluent
    def add(self, start: IntColumnPos, end: IntColumnPos = None) -> str:
        return self._to_from('add', start, end)

    @_fluent
    def remove(self, start: IntColumnPos, end: IntColumnPos = None) -> str:
        return self._to_from('remove', start, end)

    @_fluent
    def remove_all(self) -> str:
        self._add('remove', 'all')
        return str(self)

    @_fluent
    def query(self, pos: IntColumnPos = None) -> str:
        self._add('query')
        if pos:
            self._add(*pos)
        return str(self)


class _ItemTarget(Command):
    def __init__(self, follow: T, allow_modifier=False):
        super().__init__()
        self.follow = follow
        self.allow_modifier = allow_modifier

    @_fluent
    def block(self, pos: Position, slot: str, modifier: str = None) -> T:
        self._add('block', *pos, good_slot(slot))
        self._modifier(modifier)
        return self._start(self.follow)

    @_fluent
    def entity(self, target: Target, slot: str, modifier: str = None) -> T:
        self._add('entity', good_target(target), good_slot(slot))
        self._modifier(modifier)
        return self._start(self.follow)

    def _modifier(self, modifier):
        if modifier and not self.allow_modifier:
            raise ValueError('Modifier not allowed here')
        self._add_opt(modifier)


class _ItemReplace(Command):
    @_fluent
    def with_(self, item: str, count: int = None) -> str:
        self._add('with', item)
        self._add_opt(count)
        return str(self)

    @_fluent
    def from_(self) -> _ItemTarget:
        self._add('from')
        return self._start(_ItemTarget(_End(), True))


class _ItemMod(Command):
    @_fluent
    def modify(self) -> _ItemTarget:
        self._add('modify')
        return self._start(_ItemTarget(_End(), True))

    @_fluent
    def replace(self) -> _ItemTarget:
        self._add('replace')
        return self._start(_ItemTarget(_ItemReplace()))


class _LocateMod(Command):
    @_fluent
    def structure(self, name: str) -> str:
        self._add('structure', name)
        return str(self)

    @_fluent
    def biome(self, name: str) -> str:
        self._add('biome', name)
        return str(self)

    @_fluent
    def poi(self, name: str) -> str:
        self._add('poi', name)
        return str(self)


class _LootSource(Command):
    @_fluent
    def fish(self, loot_table: str, pos: Position, thing: str) -> str:
        # the 'hand' keywords are also valid resource names, so no separate test is meaningful
        self._add('fish', good_resource_path(loot_table), *pos, good_resource(thing))
        return str(self)

    @_fluent
    def loot(self, loot_table: str) -> str:
        self._add('loot', good_resource_path(loot_table))
        return str(self)

    @_fluent
    def kill(self, target: Target) -> str:
        self._add('kill', good_target(target))
        return str(self)

    @_fluent
    def mine(self, pos: Position, thing: str) -> str:
        # the 'hand' keywords are also valid resource names, so no separate test is meaningful
        self._add('mine', *pos, good_resource(thing))
        return str(self)


class _LootReplaceTarget(Command):
    @_fluent
    def block(self, pos: Position, slot: int, count: int = None) -> _LootSource:
        self._add('block', *pos, slot)
        self._add_opt(count)
        return self._start(_LootSource())

    @_fluent
    def entity(self, target: Target, slot: int, count: int = None) -> _LootSource:
        self._add('entity', good_target(target), slot)
        self._add_opt(count)
        return self._start(_LootSource())


class _LootTarget(Command):
    @_fluent
    def give(self, target: Target) -> _LootSource:
        self._add('give', good_target(target))
        return self._start(_LootSource())

    @_fluent
    def insert(self, pos: Position) -> _LootSource:
        self._add('insert', *pos)
        return self._start(_LootSource())

    @_fluent
    def spawn(self, pos: Position) -> _LootSource:
        self._add('spawn', *pos)
        return self._start(_LootSource())

    @_fluent
    def replace(self) -> _LootReplaceTarget:
        self._add('replace')
        return self._start(_LootReplaceTarget())


class _ScoreboardCriteria(Command):
    def __init__(self, criterion: str | ScoreCriteria, *criteria: str | ScoreCriteria):
        super().__init__()
        self._good_criteria(criterion)
        self._add(criterion)
        if criteria:
            self._good_criteria(*criteria)
            self._add('.' + '.'.join(str(x) for x in criteria), space=False)

    @staticmethod
    def _good_criteria(*criteria):
        for c in criteria:
            try:
                ScoreCriteria(c)
            except ValueError:
                good_resource(c)


class _ScoreboardObjectivesMod(Command):
    @_fluent
    def list(self) -> str:
        self._add('list')
        return str(self)

    @_fluent
    def add(self, objective: str, score_criteria: ScoreCriteria | _ScoreboardCriteria | str,
            display_name: str = None) -> str:
        try:
            score_criteria = ScoreCriteria(score_criteria)
        except ValueError:
            score_criteria = _ScoreboardCriteria(score_criteria)
        self._add('add', good_name(objective), score_criteria)
        self._add_opt(good_name(display_name))
        return str(self)

    @_fluent
    def remove(self, objective: str) -> str:
        self._add('remove', good_name(objective))
        return str(self)

    @_fluent
    def setdisplay(self, slot: str, objective: str = None) -> str:
        if not slot.startswith(SIDEBAR_TEAM):
            _in_group(DISPLAY_SLOTS, slot)
        self._add('setdisplay', slot)
        self._add_opt(good_name(objective))
        return str(self)

    @_fluent
    def modify(self, objective: str, which: str, value: str) -> str:
        if which == RENDER_TYPE:
            _in_group(SCOREBOARD_RENDER_TYPES, value)
        self._add('modify', good_name(objective), _in_group(SCOREBOARD_OBJECTIVES_MODIFIABLE, which), value)
        return str(self)


class _ScoreboardPlayersMod(Command):
    # Changes to these methods should be reflected in the Score class

    @_fluent
    def list(self, target: Target = None) -> str:
        self._add('list')
        self._add_opt(good_target(target))
        return str(self)

    @_fluent
    def get(self, score: ScoreName) -> str:
        self._add('get', good_score(score))
        return str(self)

    @_fluent
    def set(self, score: ScoreName, value: int) -> str:
        self._add('set', good_score(score), value)
        return str(self)

    @_fluent
    def add(self, score: ScoreName, value: int) -> str:
        self._add('add', good_score(score), value)
        return str(self)

    @_fluent
    def remove(self, score: ScoreName, value: int) -> str:
        self._add('remove', good_score(score), value)
        return str(self)

    @_fluent
    def reset(self, score: ScoreName | Target | tuple[Target, None]) -> str:
        self._add('reset')
        try:
            score = good_score(score)
            self._add(score)
        except (TypeError, ValueError) as e:
            # if not a valid full score name, it must be just a target
            if isinstance(score, (str, TargetSpec)):
                self._add(good_target(score))
            elif isinstance(score, str):
                self._add(score)
            else:
                if len(score) == 1 or (len(score) == 2 and score[1] is None):
                    self._add(good_target(score[0]))
                else:
                    # An invalid argument to good_score will be most descriptive
                    raise e
        return str(self)

    @_fluent
    def enable(self, score: ScoreName) -> str:
        self._add('enable', good_score(score))
        return str(self)

    @_fluent
    def operation(self, score: ScoreName, op: str, source: ScoreName) -> str:
        _in_group(SCORE_OPERATIONS, op)
        # 'MAX' is used elsewhere, this special-cases it
        if op == MAX:
            op = '>'
        self._add('operation', good_score(score), op, good_score(source))
        return str(self)


class _ScoreboardMod(Command):
    @_fluent
    def objectives(self) -> _ScoreboardObjectivesMod:
        self._add('objectives')
        return self._start(_ScoreboardObjectivesMod())

    @_fluent
    def players(self) -> _ScoreboardPlayersMod:
        self._add('players')
        return self._start(_ScoreboardPlayersMod())


class _PlaceMod(Command):
    @_fluent
    def feature(self, feature: str, pos: Position = None) -> str:
        self._add('feature', good_resource(feature))
        self._add_opt_pos(pos)
        return str(self)

    @_fluent
    def jigsaw(self, pool: str, target_pool: str, max_depth: int, pos: Position = None) -> str:
        self._add('jigsaw', good_resource(pool), good_resource(target_pool), max_depth)
        self._add_opt_pos(pos)
        return str(self)

    @_fluent
    def structure(self, structure: str, /, pos: Position = None) -> str:
        self._add('structure', good_resource(structure))
        self._add_opt_pos(pos)
        return str(self)


class _ScheduleMod(Command):
    @_fluent
    def function(self, path: str, time: Time, action: str) -> str:
        self._add('function', good_resource_path(path), good_time(time), _in_group(SCHEDULE_ACTIONS, action))
        return str(self)

    @_fluent
    def clear(self, path: str) -> str:
        self._add('clear', good_resource_path(path))
        return str(self)


class _TagMod(Command):
    @_fluent
    def add(self, tag: str) -> str:
        self._add('add', good_name(tag))
        return str(self)

    @_fluent
    def list(self) -> str:
        self._add('list')
        return str(self)

    @_fluent
    def remove(self, tag: str) -> str:
        self._add('remove', good_name(tag))
        return str(self)


class _TeamMod(Command):
    @_fluent
    def list(self, team: str = None) -> str:
        self._add('list')
        self._add_opt(good_team(team))
        return str(self)

    @_fluent
    def add(self, team: str, display_name: str = None) -> str:
        self._add('add', good_team(team))
        self._add_opt(good_name(display_name))
        return str(self)

    @_fluent
    def remove(self, team: str) -> str:
        self._add('remove', good_team(team))
        return str(self)

    @_fluent
    def empty(self, team: str) -> str:
        self._add('empty', good_team(team))
        return str(self)

    @_fluent
    def join(self, team: str, target: Target = None) -> str:
        self._add('join', good_team(team))
        self._add_opt(good_target(target))
        return str(self)

    @_fluent
    def leave(self, team: str, target: Target = None) -> str:
        self._add('leave', good_team(team), good_target(target))
        return str(self)

    @_fluent
    def modify(self, team, option: TeamOption | str, value: str | bool) -> str:
        vtype = TeamOption.value_spec(TeamOption(option))
        if vtype == bool:
            value = _bool(value)
        elif vtype != str:
            if value not in vtype:
                raise ValueError(f'{value}: Must be one of {vtype}')
        self._add('modify', good_team(team), option, value)
        return str(self)


class _FacingMod(Command):
    @_fluent
    def facing(self, pos: Position) -> str:
        self._add('facing', *pos)
        return str(self)

    @_fluent
    def facing_entity(self, target: Target) -> str:
        self._add('facing', 'entity', good_target(target))
        return str(self)


class _TeleportMod(Command):
    @_fluent
    def facing(self, facing: Target | Position, anchor: str = None) -> str:
        self._add('facing')
        is_entity = False
        try:
            facing = good_target(facing)
            is_entity = True
            self._add('entity', facing)
            if anchor:
                self._add(_in_group(ENTITY_ANCHOR, anchor))
        except ValueError as e:
            # Check if the error was from the entity or the anchor
            if is_entity:
                raise e
            self._add(*good_position(facing))
            if anchor is not None:
                raise ValueError('anchor not allowed when facing coordinates')
        return str(self)

    @_fluent
    def pos(self, pos: Position, /, target: Target = None,
            rotation: float = None) -> str | _FacingMod:
        if target:
            self._add(good_target(target), *pos)
        else:
            self._add(*pos)
        self._add_opt(rotation)
        if rotation is not None:
            return str(self)
        else:
            return self._start(_FacingMod())


class _TimeMod(Command):
    @_fluent
    def add(self, amount: Time) -> str:
        self._add('add', good_time(amount))
        return str(self)

    @_fluent
    def query(self, which: str) -> str:
        self._add('query', _in_group(TIME_TYPES, which))
        return str(self)

    @_fluent
    def set(self, new_time: Time) -> str:
        try:
            _in_group(TIME_SPEC, new_time)
        except ValueError:
            try:
                good_time(new_time)
            except ValueError:
                raise ValueError(f'{new_time}: Invalid time')
        self._add('set', new_time)
        return str(self)


class _TitleMod(Command):
    @_fluent
    def times(self, fade_in: int, stay: int, fade_out: int) -> str:
        self._add('times', fade_in, stay, fade_out)
        return str(self)


class _TriggerMod(Command):
    @_fluent
    def add(self, value: int) -> str:
        self._add('add', value)
        return str(self)

    @_fluent
    def set(self, value: int) -> str:
        self._add('set', value)
        return str(self)


class _WorldBorderWarningMod(Command):
    @_fluent
    def distance(self, distance: float) -> str:
        self._add('distance', distance)
        return str(self)

    @_fluent
    def time(self, time_sec: int) -> str:
        self._add('time', time_sec)
        return str(self)


class _WorldBorderDamageMod(Command):
    @_fluent
    def amount(self, value: float) -> str:
        self._add('amount', value)
        return str(self)

    @_fluent
    def buffer(self, distance: float) -> str:
        self._add('buffer', distance)
        return str(self)


class _WorldBorderMod(Command):
    @_fluent
    def add(self, distance: float, duration_secs: int = None) -> str:
        self._add('add', distance)
        self._add_opt(duration_secs)
        return str(self)

    @_fluent
    def center(self, pos: ColumnPosition) -> str:
        self._add('center', *pos)
        return str(self)

    @_fluent
    def damage(self) -> _WorldBorderDamageMod:
        self._add('damage')
        return self._start(_WorldBorderDamageMod())

    @_fluent
    def get(self) -> str:
        self._add('get')
        return str(self)

    @_fluent
    def set(self, diameter: float) -> str:
        self._add('set', diameter)
        return str(self)

    @_fluent
    def warning(self) -> _WorldBorderWarningMod:
        self._add('warning')
        return self._start(_WorldBorderWarningMod())


class _BlockMod(Command):
    def __init__(self):
        super().__init__()
        self._nbt = Nbt()
        self._state = {}

    def __str__(self):
        added = ''
        if self._state:
            added = '[' + ','.join(f'{k}={_quote(v)}' for k, v in self._state.items()) + ']'
        if self._nbt:
            added += str(self._nbt)
        return super().__str__() + added

    @_fluent
    def nbt(self, nbt: NbtDef) -> _BlockMod:
        self._nbt = self._nbt.merge(nbt)
        return self

    @_fluent
    def state(self, state: dict) -> _BlockMod:
        self._state.update(state)
        return self


class _ListMod(Command):
    def uuids(self) -> str:
        self._add('uuids')
        return str(self)


def advancement(action: str, target: Selector, behavior: str, advancement: Advancement = None,
                criterion: str = None) -> str:
    action = _to_donate(action, GRANT_REVOKE)
    self = Command()
    self._add('advancement', action, target, _in_group(ADVANCEMENT, behavior))
    if behavior != EVERYTHING:
        self._add(advancement)
        if behavior == ONLY and criterion:
            self._add(criterion)
    return str(self)


def attribute(target: Target, attribute: str) -> _AttributeAct:
    """Queries, adds, removes or sets an entity attribute."""
    self = Command()
    self._add('attribute', good_target(target), good_resource(attribute))
    return self._start(_AttributeAct())


def bossbar() -> _BossbarAct:
    """Creates and modifies bossbars."""
    self = Command()
    self._add('bossbar')
    return self._start(_BossbarAct())


def clear(target: Target, *targets: Target) -> _ClearClause:
    """Clears items from player inventory."""
    self = Command()
    self._add('clear', good_target(target), *targets)
    return self._start(_ClearClause())


def clone(start_pos: Position, end_pos: Position, dest_pos: Position) -> _CloneClause:
    """Copies blocks from one place to another."""
    self = Command()
    self._add('clone', *start_pos, *end_pos, *dest_pos)
    return self._start(_CloneClause())


def data() -> _DataMod:
    """Gets, merges, modifies and removes block entity and entity NBT data."""
    self = Command()
    self._add('data')
    return self._start(_DataMod())


def datapack() -> _DatapackAction:
    """Controls loaded data packs."""
    self = Command()
    self._add('datapack')
    return self._start(_DatapackAction())


def defaultgamemode(gamemode: str) -> str:
    """Sets the default game mode."""
    self = Command()
    self._add('defaultgamemode', _in_group(GAMEMODE, gamemode))
    return str(self)


def deop(*targets: Selector | User) -> str:
    """Revokes operator status from a player."""
    self = Command()
    self._add('deop', *targets)
    return str(self)


def difficulty(difficulty: str) -> str:
    """Sets the difficulty level."""
    self = Command()
    self._add('difficulty', _in_group(DIFFICULTIES, difficulty))
    return str(self)


def effect() -> _EffectAction:
    """Adds or removes status effects."""
    self = Command()
    self._add('effect')
    return self._start(_EffectAction())


def enchant(target: Target, enchantment: Enchantment | str | int, level: int = None) -> str:
    """Adds an enchantment to a player's selected item."""
    self = Command()
    self._add('enchant', good_target(target))
    if isinstance(enchantment, str):
        enchantment = Enchantment(enchantment)
    self._add(enchantment)
    if level is not None:
        if type(enchantment) == Enchantment:
            max_level = Enchantment.max_level(enchantment)
            if level not in range(0, max_level + 1):
                raise ValueError('Level not in range [0..%elem]', max_level)
        self._add_opt(level)
    return str(self)


def execute() -> _ExecuteMod:
    """Executes a command."""
    self = Command()
    self._add('execute')
    return self._start(_ExecuteMod())


def experience() -> _ExperienceMod:
    """Adds or removes player experience."""
    self = Command()
    self._add('experience')
    return self._start(_ExperienceMod())


xp = experience


def fill(start_pos: Position, end_pos: Position, block: BlockDef) -> _FilterClause | str:
    """Fills a region with a specific block."""
    self = Command()
    self._add('fill', *start_pos, *end_pos, good_block(block))
    return self._start(_FilterClause())


def forceload() -> _ForceloadMod:
    """Forces chunks to constantly be loaded or not."""
    self = Command()
    self._add('forceload')
    return self._start(_ForceloadMod())


def function(path: str) -> str:
    """Runs a function."""
    self = Command()
    self._add('function', good_resource_path(path))
    return str(self)


def gamemode(gamemode: str, target: Target = None) -> str:
    """Sets the gamemode for some set of players."""
    self = Command()
    self._add('gamemode', _in_group(GAMEMODE, gamemode))
    self._add_opt(good_target(target))
    return str(self)


def gamerule(rule: GameRule | str, value: bool | int = None) -> str:
    """Sets or queries a game rule value."""
    self = Command()
    rule = GameRule(rule)
    self._add('gamerule', rule)
    if value is not None:
        rule_type = GameRule.rule_type(rule)
        if rule_type == 'int':
            if type(value) != int:
                raise ValueError(f'int value required for rule {rule}')
            self._add(int(value))
        else:
            self._add(_bool(value))
    return str(self)


def give(target: Target, item: EntityDef | BlockDef, count: int = None) -> str:
    """Gives an item to a player."""
    self = Command()
    self._add('give', good_target(target), item)
    self._add_opt(count)
    return str(self)


def help(command: str = None) -> str:
    """Provides help for commands."""
    self = Command()
    self._add('help')
    self._add_opt(command)
    return str(self)


def item() -> _ItemMod:
    """Manipulates items in inventories."""
    self = Command()
    self._add('item')
    return self._start(_ItemMod())


def kill(target: Target = None) -> str:
    """Kills entities (players, mobs, items, etc.)."""
    self = Command()
    self._add('kill')
    self._add_opt(good_target(target))
    return str(self)


def list_() -> _ListMod:
    """Lists players on the server."""
    self = Command()
    self._add('list')
    return self._start(_ListMod())


def locate(what: str, name: str) -> str:
    """Locates closest structure."""
    self = Command()
    self._add('locate', _in_group(LOCATABLE, what), name)
    return str(self)


def loot() -> _LootTarget:
    """Drops items from an inventory slot onto the ground."""
    self = Command()
    self._add('loot')
    return self._start(_LootTarget())


def me(*msg) -> str:
    """Displays a message about the sender."""
    self = Command()
    self._add('me', *msg)
    return str(self)


def op(target: Target) -> str:
    """Grants operator status to a player."""
    self = Command()
    self._add('op', good_target(target))
    return str(self)


def pardon(target: Target) -> str:
    """Removes entries from the banlist."""
    self = Command()
    self._add('pardon', good_target(target))
    return str(self)


def particle(particle: Particle | str, *params) -> str:
    """
    Creates particles. The syntax of the command is too variant and conditional, so nearly no checks are made.
    """
    self = Command()
    self._add('particle', Particle(particle))
    for p in params:
        if not isinstance(p, str) and isinstance(p, Iterable):
            self._add(*p)
        else:
            self._add(p)
    return str(self)


def place() -> _PlaceMod:
    """Used to place a configured feature, jigsaw, or structure at a given location."""
    self = Command()
    self._add('place')
    return self._start(_PlaceMod())


def playsound(sound: str, source: str, target: Target, pos: Position = None, /,
              volume: float = None, pitch: float = None, min_volume: float = None) -> str:
    """Plays a sound."""
    self = Command()
    self._add('playsound', good_resource_path(sound), good_resource_path(source), good_target(target))
    self._add_opt_pos(pos)
    self._add_opt(volume, pitch, min_volume)
    return str(self)


def publish(port: int = None) -> str:
    """Opens single-player dir to local network."""
    self = Command()
    self._add('publish')
    self._add_opt(port)
    return str(self)


def recipe(action: str, target: Target, recipe: str = '*') -> str:
    """Gives or takes player recipes."""
    action = _to_donate(action, GIVE_TAKE)
    if recipe != '*':
        good_resource_path(recipe)
    self = Command()
    self._add('recipe', action, good_target(target), recipe)
    return str(self)


def reload() -> str:
    """Reloads loot tables, advancements, and functions from disk."""
    self = Command()
    self._add('reload')
    return str(self)


def say(*msg: str):
    """Displays a message to multiple players."""
    self = Command()
    self._add('say', *msg)
    return str(self)


def schedule() -> _ScheduleMod:
    """Delays the execution of a dir."""
    self = Command()
    self._add('schedule')
    return self._start(_ScheduleMod())


def scoreboard() -> _ScoreboardMod:
    """Manages scoreboard objectives and players."""
    self = Command()
    self._add('scoreboard')
    return self._start(_ScoreboardMod())


def seed() -> str:
    """Displays the dir seed."""
    self = Command()
    self._add('seed')
    return str(self)


def setblock(pos: Position, block: BlockDef, action: str = None) -> _BlockMod:
    """Changes a block to another block."""
    if isinstance(block, str) and str(block)[0] == '#':
        raise ValueError(f'{block}: Block tag not allowed here')
    block = good_block(block)
    self = Command()
    self._add('setblock', *pos, block)
    if action:
        self._add_opt(_in_group(SETBLOCK_ACTIONS, action))
    return self._start(_BlockMod())


def setworldspawn(pos: Position = None, yaw: Coord = None) -> str:
    """Sets the dir spawn."""
    self = Command()
    self._add('setworldspawn')
    self._add_opt_pos(pos)
    if yaw and str(yaw)[0] == '^':
        raise ValueError(f'{yaw}: Caret notation not allowed')
    self._add_opt(yaw)
    return str(self)


def spawnpoint(target: Target = None, pos: Position = None, yaw: Coord = None) -> str:
    """Sets the spawn point for a player."""
    self = Command()
    self._add('spawnpoint')
    self._add_opt(good_target(target))
    self._add_opt_pos(pos)
    if yaw and str(yaw)[0] == '^':
        raise ValueError(f'{yaw}: Caret notation not allowed')
    self._add_opt(yaw)
    return str(self)


def spectate(target: Target = None, player: Target = None) -> str:
    """Make one player in spectator mode spectate an entity."""
    self = Command()
    self._add('spectate', good_target(target))
    self._add_opt(good_target(player))
    return str(self)


def spreadplayers(pos: Position, distance: float, max_range: float, respect_teams: bool, target: Target,
                  max_height: int = None) -> str:
    """Teleports entities to random locations. This doesn't quite follow the minecraft command syntax because
    that has a weird optional 'under <num>' parameter, which is hard to model and, well, weird. """
    self = Command()
    self._add('spreadplayers', *pos, distance, max_range)
    if max_height is not None:
        self._add_opt('under', max_height)
    self._add(_bool(respect_teams), good_target(target))
    return str(self)


def stopsound(target: Target, /, source: str = None, sound: str = None) -> str:
    """Stops a sound."""
    self = Command()
    self._add('stopsound', good_target(target))
    self._add_opt(good_resource_path(source), good_resource_path(sound))
    return str(self)


def summon(entity: EntityDef, /, pos: Position = None, nbt=None) -> str:
    """Summons an entity."""
    entity = good_entity(entity)
    self = Command()
    self._add('summon', entity.id)
    self._add_opt_pos(pos)
    e_nbt = Nbt(entity.nbt) if entity.nbt else Nbt()
    e_nbt = e_nbt.merge(nbt)
    if len(e_nbt) > 0:
        self._add_opt(e_nbt)
    return str(self)


def tag(target: Target) -> _TagMod:
    """Controls entity tags."""
    self = Command()
    self._add('tag', good_target(target))
    return self._start(_TagMod())


def team() -> _TeamMod:
    """Controls teams."""
    self = Command()
    self._add('team')
    return self._start(_TeamMod())


def teammsg(*msg: str) -> str:
    """An alias of /tm. Specifies the message to send to team."""
    self = Command()
    self._add('teammsg', *msg)
    return str(self)


tm = teammsg


def teleport(who_or_to: Target | Position, to: Target | Position = None,
             rotation: float = None) -> str | _TeleportMod:
    """An alias of /tp. Teleports entities."""
    self = Command()
    self._add('tp')
    try:
        self._add(good_target(who_or_to))
    except ValueError:
        self._add(*good_position(who_or_to))
    if to is None:
        if rotation is not None:
            raise ValueError('Rotation not allowed without two arguments')
    else:
        try:
            self._add(good_target(to))
        except ValueError:
            self._add(*good_position(to))
        if rotation is not None:
            self._add(_float(rotation))
            return str(self)
    return self._start(_TeleportMod())


tp = teleport


def tell(target: Target, *msg: str) -> str:
    """Displays a private message to other players."""
    self = Command()
    self._add('tell', good_target(target), *msg)
    return str(self)


msg = tell
w = tell


def tellraw(target: Target, *msg: JsonDef) -> str:
    """Displays a JSON message to players."""
    self = Command()
    self._add('tellraw', target)
    msg = _to_list(msg)
    if len(msg) > 0:
        for i in range(0, len(msg)):
            if isinstance(msg[i], str):
                msg[i] = JsonText.text(msg[i])
            else:
                msg[i] = JsonText.as_json(msg[i])
        if len(msg) == 1:
            msg = msg[0]
        self._add(msg)
    return str(self)


def time() -> _TimeMod:
    """Changes or queries the dir's game time."""
    self = Command()
    self._add('time')
    return self._start(_TimeMod())


def title(target: Target, /, action: str = None, title: str = None) -> _TitleMod | str:
    """Manages screen titles."""
    self = Command()
    self._add('title', good_target(target))
    if not action:
        return self._start(_TitleMod())
    if action in TITLE_GIVEN and title is None:
        raise ValueError(f'{action}: Requires a title')
    self._add_opt(_in_group(TITLE_ACTIONS, action), title)
    return str(self)


def trigger(objective: str):
    """Sets a trigger to be activated."""
    self = Command()
    self._add('trigger', good_name(objective))
    return self._start(_TriggerMod())


def weather(weather: str, duration: int = None) -> str:
    """Sets the weather."""
    self = Command()
    self._add('weather', weather)
    self._add_opt(duration)
    return str(self)


def worldborder() -> _WorldBorderMod:
    """Manages the dir border."""
    self = Command()
    self._add('worldborder')
    return self._start(_WorldBorderMod())


def comment(text: str, wrap=False):
    """
    Inserts a comment.

    :param text: The text of the comment
    :param wrap: If False, the comment will be the text with each line prepended by a '# '. Otherwise, the text will
     be broken into paragraphs by blank lines, each paragraph will be formatted by textwrap.fill() (to 78 columns),
     and before_cmds each line is prepended by a '# '.
    """
    text = text.strip()
    if wrap:
        orig_paras = re.split(r'\n\s*\n', text)
        new_paras = (textwrap.fill(x, width=78) for x in orig_paras)
        text = '\n\n'.join(new_paras)
    text = text.replace('\n', '\n# ').replace('# \n', '#\n')
    return f'# {text}'


def literal(text: str):
    """Puts the text in without modification or checks."""
    self = Command()
    self._add(text)
    return self


class NbtHolder(Command):
    """This class represents a thing that has NBT values. These include blocks and entities."""

    def __init__(self, id: str = None, name=None):
        """Creates a holder.

        Typically, the ID is an in-game ID, such as 'air' or 'minecraft:smooth_stone', and the name is derived
        from it, such as 'Air' or 'Smooth Stone'. Or the other way around. You could pass 'Smooth Stone' as either the
        ID _or_ the name and get the same result: The ID is checked for being a valid name and if it is not,
        we try to see if we can derive an ID from it, and if so, we use that (id, name) combination.

        The name can incude '|' characters, which are used to split it into a tuple of multiple lines for a sign.
        (Unfortunately it is not possible to calculate where such breaks need to happen.) After those splits, the '|' is
        replaced with ' ' for the actual name.

        The possibly-split version of the name is used to set two fields: `sign_text` is the tuple resulting from the
        split, and `full_text` is that list regularized text for a sign that shows just the name, preferring to
        skip the first line if there are fewer than four lines.

        :param id: The ID of the holder.
        :param name: The name to display to your user, derived from ID if not provided.
        """
        super().__init__()
        if not id and not name == (None, None):
            raise ValueError('Must specify at least one of id or name')
        if id:
            id = id.strip()
        if name:
            name = name.strip()
        if id and not name:
            if _display_name_re.match(id):
                name = id
                id = None
            else:
                name = to_name(id)
        if not id and name:
            id = to_id(name)

        self.id = good_resource(id)
        self.nbt = Nbt()
        self._add(id)
        self.sign_text = tuple(name.split('|'))
        t = self.sign_text
        if len(t) < 4:
            t = ('',) + t
        t = _ensure_size(t, 4, '')
        self.full_text = tuple(t)
        self.name = name.replace('|', ' ')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def sign_nbt(self) -> Nbt:
        """Returns the NBT you would use in a sign, based on `full_text`."""
        nbt = Nbt()
        for i in range(0, 4):
            nbt[f'Text{i + 1:d}'] = self.full_text[i]
        return nbt

    def __str__(self):
        added = ''
        if len(self.nbt) > 0:
            added = str(self.nbt)
        return super().__str__() + added

    def merge_nbt(self, nbt: NbtDef) -> NbtHolder:
        """Merge NBT into our nbt."""
        self.nbt = self.nbt.merge(Nbt.as_nbt(nbt))
        return self


class Entity(NbtHolder):
    """This class supports operations useful for an entity. """

    def __init__(self, id: str, nbt=None, name=None):
        """Creates a new entity object. See `NbtHolder.__init__()` for interpretation of `id` and `name`.

        :param id: The entity ID.
        :param nbt: Any NBT for the entity.s
        :param name: The entity's human-friendly name.
        """
        self._custom_name = False
        self._custom_name_visible = False
        super().__init__(id, name)
        self.merge_nbt(nbt)

    @property
    def name(self):
        """The entity name (same as the NbtHolder's name)."""
        return super().name

    @name.setter
    def name(self, name: str):
        """Set the entity name and, if we're managing it, the custom name."""
        NbtHolder.name.fset(self, name)
        self._update_custom_name()

    def custom_name(self, manage: bool = True) -> Entity:
        """Sets whether to manage the 'CustomName' NBT tag along with the name. Defalut is True. """
        self._custom_name = manage
        self._update_custom_name()
        return self

    def custom_name_visible(self, v: bool) -> Entity:
        """Sets whether the custom name is visible. If so, this implies `custom_name(True)`."""
        self._custom_name_visible = v
        if v:
            self.custom_name(v)
        self._update_custom_name()
        return self

    def _update_custom_name(self):
        if self._custom_name:
            self.merge_nbt({'CustomName': self.name})
            self.merge_nbt({'CustomNameVisible': self._custom_name_visible})
        else:
            self.nbt.pop('CustomName')
            self.nbt.pop('CustomNameVisible')

    def tag(self, *tags: str) -> Entity:
        """Add one or more tags."""
        self.nbt.get_list('Tags').extend(tags)
        return self

    def passenger(self, entity: EntityDef) -> Entity:
        """Add a passenger."""
        passengers = self.nbt.get_list('Passengers')
        e_nbt = entity.nbt
        e_nbt['id'] = entity.id
        passengers.append(e_nbt)
        return self

    def add(self, place: str, item: Nbt) -> Entity:
        """Add for specialized places. `RIGHT` or `LEFT` mean right or left hand,
        while `BOOTS`, LEGGINGS`, `CHESTPLATE`, and `HELMET` refer to armor items. This allows you not to
        remember which index in the respective NBT lists is for each kind of thing."""
        place = _in_group(ENTITY_PLACES, place)
        try:
            index = (RIGHT, LEFT).index(place)
            key = 'HandItems'
            size = 2
        except ValueError:
            index = ENTITY_PLACES.index(place)
            key = 'ArmorItems'
            size = 4
        items = _ensure_size(self.nbt.get_list(key), size, Nbt())
        items[index] = Nbt.as_nbt(item)
        return self

    def summon(self, pos: Position, nbt=None, facing: str = None) -> str:
        """Summon an instance of this entity, optionally with added nbt and a specified facing direction."""
        if facing:
            if not nbt:
                nbt = Nbt()
            else:
                nbt = Nbt.as_nbt(nbt)
            info = good_facing(facing)
            # Item frames use 'facing' instead of rotation, which they use for something else (natch).
            nbt = nbt.merge({'Rotation': info.rotation, 'Facing': info.number})
        return summon(self, pos, nbt)

    def full_id(self):
        """Returns a qualified id, adding 'minecraft:' if none was given at construction."""
        if self.id.find(':') >= 0:
            return self.id
        return 'minecraft:' + self.id


class Block(NbtHolder):
    """This class supports operations useful for a block. """

    def __init__(self, id: str, state=None, nbt=None, name=None):
        """
        Creates a new block object. See `NbtHolder.__init__()` for interpretation of `id` and `name`.

        State is represented as an nbt object.
        """
        super().__init__(id, name)
        if state is None:
            state = {}
        self.merge_nbt(nbt)
        self.state = {}
        self.merge_state(state)

    def __str__(self):
        s: str = super().__str__()
        if self.state:
            at = len(self.id)
            s = s[:at] + self._state_str() + s[at:]
        return s

    @staticmethod
    def _state_value(v):
        if isinstance(v, bool):
            return _bool(v)
        return str(v)

    def _state_str(self):
        comma = ', ' if Nbt.use_spaces else ','
        return '[' + comma.join((k + '=' + self._state_value(v)) for k, v in self.state.items()) + ']'

    def merge_state(self, state: Mapping):
        """Merge state into our state."""
        self.state.update(state)
        return self


class Score(Command):
    _cmd_base = scoreboard().players()

    """This class represents a score, and provides simpler mechanisms for menipulating it."""

    def __init__(self, target: Target, objective: str):
        """Creates a new score.

        :param target: The score's name.
        :param objective: The score's objective name.
        """
        super().__init__()
        if target is None or objective is None:
            raise ValueError('Must give both target and objective')
        self.target = good_target(target)
        self.objective = good_name(objective)
        self._add(target, objective)

    def __eq__(self, other: Score) -> bool:
        return self.target == other.target and self.objective == other.objective

    def __hash__(self):
        return hash(self.target) ^ hash(self.objective)

    def init(self, value: int = 0) -> str:
        """Initiailze the score by ensure the objective exists, and setting it's value to the provided value."""
        return commands(
            scoreboard().objectives().add(self.objective, ScoreCriteria.DUMMY),
            execute().unless().score(self).matches(0).run().scoreboard().players().add(self, value))

    def get(self) -> str:
        """Return a 'get' command for the score."""
        return self._cmd().get(self)

    def set(self, value: int) -> str:
        """Return a 'get' command for the score."""
        return self._cmd().set(self, value)

    def add(self, value: int) -> str:
        """Return an 'add' command for the score."""
        return self._cmd().add(self, value)

    def remove(self, value: int) -> str:
        """Return a 'remove' command for the score."""
        return self._cmd().remove(self, value)

    def reset(self) -> str:
        """Return a 'reset' command for the score."""
        return self._cmd().reset(self)

    def enable(self) -> str:
        """Return an 'enable' command for the score."""
        return self._cmd().enable(self)

    def operation(self, op: str, source: ScoreName) -> str:
        """Return an 'operation' command for the score. The operation must be in `SCORE_OPERATION`."""
        return self._cmd().operation(self, op, source)

    @staticmethod
    def _cmd():
        return Score._cmd_base


class JsonList(UserList, JsonHolder):
    """A list as part of as JSON text structure,"""

    def content(self):
        return tuple(self)


class JsonText(UserDict, JsonHolder):
    """This class represents JSON text.

    You should mostly use the various static factory methods to get a well-formed JSON text component.
    """

    @staticmethod
    def text(txt: str) -> JsonText:
        """Returns a JSON text node."""
        return JsonText({'text': txt})

    @staticmethod
    def html_text(txt: str) -> JsonText:
        """Returns a JSON text node populatd from some HTML."""
        parser = _ToMinecraftText()
        parser.feed(txt)
        parser.close()
        return JsonText({'text': parser.json()})

    @staticmethod
    def translate(translation_id: str, *texts: str) -> JsonText:
        """Returns a JSON text translation node."""
        if not isinstance(texts, list):
            texts = list(texts)
        else:
            texts = texts[:]
        return JsonText({'translate': translation_id, 'with': texts})

    @staticmethod
    def score(score: ScoreName, value=None) -> JsonText:
        """Returns a JSON text score node."""
        score = good_score(score)
        jt = JsonText({'score': {'name': str(score.target), 'objective': score.objective, }})
        if value:
            jt['score']['value'] = value
        return jt

    @staticmethod
    def entity(selector: Selector, sep_color: str = None, sep_text: str = None) -> JsonText:
        """Returns a JSON text entity node."""
        jt = JsonText()
        jt['selector'] = str(selector)
        if sep_color:
            jt.setdefault('separator', {}).update({'color': _in_group(COLORS, sep_color)})
        if sep_text is not None:
            jt.setdefault('separator', {}).update({'text': sep_text})
        return jt

    @staticmethod
    def keybind(keybind_id: str) -> JsonText:
        """Returns a JSON text keybindig node."""
        return JsonText({'keybind': keybind_id})

    @classmethod
    def nbt(cls, resource_path: str, data_target: DataTarget, interpret: bool = None,
            separator: str = None) -> JsonText:
        """Returns a JSON text NBt node."""
        target_key, target_value = data_target_str(data_target).split(' ', 1)
        jt = cls({'nbt': good_resource_path(resource_path), target_key: target_value})
        if interpret is not None:
            jt['interpret'] = interpret
        if separator is not None:
            jt['separator'] = separator
        return jt

    def content(self):
        return dict(self)

    def extra(self, *extras: JsonText | str) -> JsonText:
        """Adds a `extra` field to a JSON node."""
        cur = self.setdefault('extra', [])
        cur.extend(extras)
        return self

    def color(self, color: str) -> JsonText:
        """Adds a `color` field to a JSON node."""
        self['color'] = _in_group(JSON_COLORS, color)
        return self

    def font(self, font: str) -> JsonText:
        """Adds a `font` field to a JSON node."""
        self['font'] = good_resource_path(font)
        return self

    def bold(self) -> JsonText:
        """Adds a `bold` field to a JSON node."""
        self['bold'] = True
        return self

    def italic(self) -> JsonText:
        """Adds a `italic` field to a JSON node."""
        self['italic'] = True
        return self

    def underlined(self, v: bool = True) -> JsonText:
        """Adds an `underline` field to a JSON node."""
        self['underlined'] = v
        return self

    def strikethrough(self) -> JsonText:
        """Adds a `strikethrough` field to a JSON node."""
        self['strikethrough'] = True
        return self

    def obfuscated(self) -> JsonText:
        """Adds an `obfusccated` field to a JSON node."""
        self['obfuscated'] = True
        return self

    def insertion(self, to_insert: str) -> JsonText:
        """Adds an `insertion` field to a JSON node."""
        self['insertion'] = to_insert
        return self

    def click_event(self) -> _JsonTextClickEventAction:
        """Adds a `click_event` field to a JSON node."""
        ev = {}
        self['clickEvent'] = ev
        return _JsonTextClickEventAction(self, ev)

    def hover_event(self) -> _JsonTextHoverAction:
        """Adds a `hover_event` field to a JSON node."""
        ev = {}
        self['hoverEvent'] = ev
        return _JsonTextHoverAction(self, ev)

    @staticmethod
    def as_json(map: Mapping):
        """Returns a JsonText object built from the given mapped values."""
        if map is None or isinstance(map, JsonText):
            return map
        elif isinstance(map, Mapping):
            return JsonText(map)
        else:
            raise ValueError(f'{map}: Not a dictionary')


Range = Union[float, Tuple[Optional[float], Optional[float]]]
Target = Union[str, TargetSpec]
ScoreName = Union[Score, Tuple[Target, str]]
BlockDef = Union[str, Block, Tuple[str, Mapping], Tuple[str, Mapping, Mapping]]
EntityDef = Union[str, Entity, Tuple[str, Mapping]]
JsonDef = Union[JsonText, dict]
SignText = Iterable[Union[str, NbtDef, None]]
SignCommands = Iterable[Union[str, Command, NbtDef, Callable[[Union[JsonText]], JsonText], None]]
Commands = Iterable[Union[Command, str]]
DataTarget = Union[Position, TargetSpec, str]
SomeBlockDefs = Union[BlockDef, Iterable[BlockDef]]
SomeMappings = Union[Mapping, Iterable[Mapping]]


def lines(*orig: any) -> list[str]:
    """Flatten a tree of commands into a one-line-per-command flat list."""
    return _lines([], orig)


def _lines(result: list[str], orig: any) -> list[str]:
    for item in orig:
        if isinstance(item, str):
            if item.find('\n') >= 0:
                result.extend(item.split('\n'))
            else:
                result.append(item)
        elif isinstance(item, Iterable):
            _lines(result, item)
        elif item is not None:
            result.append(str(item))
    return result
