"""Functionality related to functions."""

from __future__ import annotations

import json
import shutil
from typing import Any

from .base import _ensure_size, _in_group, _to_list
from .commands import *

_function_re = re.compile(r'(\w+:)?(\w+/)?(\w+)$')

BLOCKS = 'blocks'
FLUIDS = 'fluids'
ITEMS = 'items'
ENTITIES = 'entity_types'
EVENTS = 'game_events'
TAG_SETS = [BLOCKS, FLUIDS, ITEMS, ENTITIES, EVENTS]


def text_lines(*orig: any) -> Iterable[str]:
    """Converts a number of commands and lines into a sequence of single lines, each terminated by newlines."""
    result = []
    for cmd in lines(orig):
        text = str(cmd)
        if len(text) > 0 or text[-1] != '\n':
            text += '\n'
        result.append(text)
    return result


def good_function_name(name: str):
    """
    Checks if the name is a valid function name.

    :param name: The (probable) function name.
    :return: the input value.
    """
    m = _function_re.match(name)
    if not m:
        raise ValueError('%s: Invalid function name' % name)
    return name


class Function:
    """A class that represents a function."""

    def __init__(self, name: str, base_name: str = None):
        self.name = good_function_name(name)
        self.base_name = base_name if base_name else name
        self._commands = []
        self.parent = None

    @property
    def full_name(self) -> str:
        if self.parent:
            parent_name = self.parent.full_name
            if parent_name[-1] != ':':
                parent_name += '/'
            return parent_name + self.name
        return self.name

    @property
    def pack(self):
        p = self.parent
        while p is not None and p.pack is None:
            p = p.parent
        if p and p.pack:
            return p.pack
        return None

    def __str__(self):
        return self.name + ':' + str('\n'.join(self.commands()) + '\n')

    def add(self: T, *commands: [Command | str]) -> T:
        """Adds commands to the function.

        You can provide a list of strings or Command objects, or a any un-flat iterables of them. They will be flattend
        into a set of strings for the function's commands.
        """
        commands = lines(commands)
        self._commands.extend(commands[:])
        return self

    def commands(self) -> list[str]:
        """Returns the commands in the function."""
        return self._commands

    def save(self, path: Path | str = None) -> Path:
        """Saves the function to a file.

        If the path is not given, it is derived from this function's full path name, using the Minecraft file layout.
        If the path is a directory, the function is written into a file with the name of the function followed by
        `.mcfunction`. If the path is to a file, it must end in `.mcfunction` or have no suffix, in which case
        `.mcfunction` will be added.

        When saving, if the parent pack has specified an abbreviation, all the text written will be searched for that
        abbreviation as a word, and it will be replaced with the pack name. This allows you to rename the pack without
        having to find everywhere you used the pack name.
        """
        if path is None:
            path = Path(self.name.split(':')[-1])
        path = path if isinstance(path, Path) else Path(path)
        func_suffix = '.mcfunction'
        if path.is_dir():
            path = path / self.name
        if path.suffix:
            if path.suffix != func_suffix:
                raise ValueError("%s: Suffix must be absent or '%s'" % (path.suffix, func_suffix))
        else:
            path = path.with_suffix(func_suffix)
        path.parent.mkdir(exist_ok=True, parents=True)
        count = -1
        pack_name = 'OOPS'
        pattern = 'OOPS'
        if self.parent and self.parent.pack and self.parent.pack.abbreviation:
            count = 0
            pack = self.parent.pack
            pack_name = pack.name
            pattern = r'\b%s\b' % pack.abbreviation
        with open(path, 'w') as out:
            out.writelines(re.sub(pattern, pack_name, x, count) for x in text_lines(self.commands()))
        return path


def _instantiate(items):
    if isinstance(items, (tuple, list)):
        return items
    return [].extend(items)


class Loop(Function):
    """
    A loop function. This does the following:

    * Creates a score that is incremented each time the function is called.
    * Executes a series of commands for each iteration of the loop, only running those for the specific iteration value.
    * Generates a `_cur` function that will execute the code without iteration, which is useful when the commands are
    conditional on something else that may have changed.

    The loop body is provided with the `loop()` function. It is given a function that returns the commands for a given iteration
    of the loop, and then makes those commands run only when the score has that iteration's value. The commands can be
    as similar or dissimilar for each iteration as your loop funciton makes it. The other parameter to `loop()` is the
    list of things that are the values for each step. This could be a simple `range()` command, or a list of names, or
    whatever.

    As an example, you could have the following:

    ```
    Loop('foo', 'funcs').loop(lambda step: say(f'{step.i:d}: {step.elem}, ('Red', 'Green', 'Blue'))
    ```

    The lambda will be invoked three times. The `step` argument defines the data for the specific iteration; `i`
    is the iteration number, and `elem` is the value for from the list for that iteratation. This will produce
    a function that looks something like this:

    ```
    _increment Score('foo', 'funcs') for the loop__
    execute if score foo funcs matches 0 run say 0: Red
    execute if score foo funcs matches 1 run say 0: Green
    execute if score foo funcs matches 2 run say 0: Blue
    ```

    You can have a function that is much more complicated than the lambd, one that might (for example) use `step.i` to
    craft each loop iteration. It's up to you.

    Commands that are added using `add()` will be executed before or after the loop every time the function is invoked,
    depending on whether you call `add()` before or after `loop()`. You can call `loop()` at most once.
    """

    class Step:
        """Data about a specific step in the iteration."""

        def __init__(self, i: int, elem, loop: Loop):
            self.i = i
            self.elem = elem
            self.loop = loop

    class TestControls:
        """Controls that are useful to simplify behavior for testing Loop. You should not otherwise use this code."""

        @staticmethod
        def set_prefix_override(func):
            Loop._prefix_override = func

        @staticmethod
        def set_setup_override(func):
            Loop._setup_override = func

    _prefix_override = None
    _setup_override = None

    @classmethod
    def test_controls(cls):
        return Loop.TestControls()

    def __init__(self, name: str, objective: str = None, /, base_name=None, score=None):
        """
        Creates a Loop function that uses the specified score for its iteration counter.

        :param name: The loop name, which will typically be the 'target' part of the score.
        :param objective: The objective for the score, which can be None if you provide a `score` value.
        :param base_name: The base name for the function. It can be useful to name the function 'foo_main' to run the
        function on the "main" clock, for example. If so, the base name would typically be 'foo'.
        :param score: If given, specifies the score name used for the loop. If not, the score is 'name objective'.
        """
        super().__init__(name, base_name)
        m = _function_re.match(name)
        var_name = base_name if base_name else m.group(3)
        self.looped = False
        self._path_name = m.group(2) + var_name if m.group(2) else var_name
        if objective is None:
            objective = m.group(2)
            if objective:
                if objective.endswith('/'):
                    objective = objective[:-1]
            else:
                objective = m.group(1)
            if not objective:
                raise ValueError('No objective given or derivable from name')
        if score is None:
            score = good_score((var_name, objective))
        self.score = score
        self._to_incr = Score('_to_incr', self.score.objective)
        self.max_score = Score(self.score.target, '%s_max' % self.score.objective)

    def _setup_for(self, max: int):
        if Loop._setup_override:
            return _to_list(Loop._setup_override())
        return [
            execute().unless().score(self.score).matches((0, None)).run(function(
                '%s_init' % self.score.target)),
            execute().if_().score(self._to_incr).matches((1, None)).run(literal(self.score.add(1))),
            self.max_score.set(max),
            self.score.operation(MOD, self.max_score),
        ]

    def _prefix_for(self, i):
        if Loop._prefix_override:
            return Loop._prefix_override(i)
        return execute().if_().score(self.score).matches(i).run('')

    def loop(self, body_func: Callable[[Step], Commands] | Callable[[Step], Command] | None, items: Iterable[Any],
             bounce=False) -> Loop:
        """
        Define the loop.
        :param body_func: The function to call for each iteration of the loop. This returns the same kind of values
        that `add()` will take.
        :param items: The items that will be iterated over. Can be a simple `range` or any other iterable.
        :param bounce: If true, the loop will "bounce" beteween the list values. A loop with range(0, 4) and bounce True
        will go through the values (0, 1, 2, 3, 2, 1) instead of (0, 1, 2, 3).
        :return: the Loop object.
        """
        items = _to_list(items)
        if bounce and len(items) > 2:
            items = items + list(reversed(items[1:-1]))
        assert not self.looped, 'loop() invoked more than once'
        cur_commands = self._commands
        self._commands = self._setup_for(len(items))
        self._commands.extend(cur_commands)
        if body_func:
            for (i, elem) in enumerate(items):
                once = body_func(Loop.Step(i, elem, self))
                prefix = str(self._prefix_for(i)) + ' '
                for line in lines(once):
                    self.add(str(prefix) + line)
        self.looped = True
        return self

    def cur(self) -> Commands:
        """Return the commands for the `_cur` function that will run the function without incrementing the score."""
        return lines(
            self._to_incr.set(0),
            function(self.full_name),
            self._to_incr.set(1),
        )


def _pack_version_rep(spec: str):
    ver_rep = 0
    for p in _ensure_size(spec.split('.'), 3, 0):
        ver_rep = ver_rep * 1000 + int(p)
    return ver_rep


LATEST_PACK_VERSION = 10


class DataPack:
    """
    A datapack. Currently this supports functions and tags, but more things will be added.
    """

    def __init__(self, name: str, path: Path | str, format_version: int = LATEST_PACK_VERSION, /,
                 mcmeta: Mapping = None):
        path = path if isinstance(path, Path) else Path(path)
        self.name = good_name(name)
        datapack_path = path / 'datapacks'
        if datapack_path.exists():
            path = datapack_path / name
            path.mkdir(exist_ok=True)
        self.path = path
        self.function_set = FunctionSet('functions', self)
        self.tag_sets = {}
        self._mcmeta = {'pack': {'pack_format': format_version, 'description': name}}
        self.abbreviation = 'PACK'
        if mcmeta:
            self._mcmeta.update(mcmeta)

    def _data_dir(self):
        return self.path / 'data' / self.name

    def save(self):
        """
        Saves all the files in the datapack. This first removes the path, if it exists, to clean out any old files. It
        then writes all the new files, as well as the `pack.mcmeta` file and a warning `README` file.
        """
        shutil.rmtree(self.path)
        self.function_set.save(self._data_dir())
        self._save_tags()
        with open(self.path / 'pack.mcmeta', 'w') as fp:
            json.dump(self._mcmeta, fp)
        with open(self.path / 'README', 'w') as fp:
            fp.write("Files in this tree were auto-generated using pyker. Hand modifications will be lost!")

    def _save_tags(self):
        for name, tags in self.tag_sets.items():
            dir = self._data_dir() / 'tags' / name
            dir.mkdir(exist_ok=True, parents=True)
            for tag, values in tags.items():
                with open((dir / tag).with_suffix('.json'), 'w') as fp:
                    json.dump(values, fp, indent=2)

    def tags(self, tag_set: str) -> dict:
        """Returns the defined tags. You can add to this dict to add tags to the datapack. """
        return self.tag_sets.setdefault(_in_group(TAG_SETS, tag_set), {})


class FunctionSet:
    """A set of functions. This corresponds to the top-level `functions` directory in the datapack, and any of
    its subdirectories. It enforces this maximum-two-level structure."""

    def __init__(self, name: str, pack_or_parent: DataPack | FunctionSet = None):
        """Creates a function set.

        :param name: The set name. For the top level directory this is notional. For subdirectories it is the directory name.
        The parent can be either a DataPack (for the top-level function directory) or that pack's FunctionSet.
        :param pack_or_parent: The parent of this set.
        """
        self.name = good_name(name)
        if isinstance(pack_or_parent, FunctionSet):
            self.pack = pack_or_parent.pack
            self.parent = pack_or_parent
            self.parent.add_child(self)
            self.full_name = pack_or_parent.full_name + ':' + self.name
            if self.parent.parent:
                raise ValueError('Only two levels of groups (sigh): %s has a parent' % pack_or_parent.name)
        elif isinstance(pack_or_parent, DataPack):
            self.pack = pack_or_parent
            self.full_name = self.pack.name
            self.parent = None
        else:
            self.pack = None
            self.full_name = self.name
            self.parent = None

        self._functions = {}
        self._kids: list[FunctionSet] = []

    def add(self, *functions: Function) -> FunctionSet:
        """Add a function to this set."""
        for f in functions:
            f.parent = self
            if f.name in self._functions:
                raise ValueError('%s: duplicate function in %s' % (f.name, self.name))
            self._functions[f.name] = f
        return self

    def child(self, name: str) -> FunctionSet | None:
        """Returns the named child FunctionSet of this function set."""
        for fs in self._kids:
            if fs.name == name:
                return fs
        return None

    @property
    def functions(self) -> Mapping:
        """The functions in this set"""
        return self._functions

    @property
    def children(self) -> tuple[FunctionSet]:
        """The child FunctionSets of this set. This is read-only"""
        return tuple(self._kids)

    def path(self, dir) -> Path:
        return dir / self._path_for()

    def save(self, dir: Path):
        full_dir = self.path(dir)
        if full_dir.exists():
            shutil.rmtree(full_dir)
        full_dir.mkdir(parents=True, exist_ok=True)
        for func in self.functions.values():
            path = full_dir / func.name
            func.save(path)
        for child in self._kids:
            child.save(dir)

    def _path_for(self) -> Path:
        if self.parent:
            return Path(self.parent.name) / self.name
        return Path(self.name)

    def add_child(self, child: FunctionSet):
        self._kids.append(child)
