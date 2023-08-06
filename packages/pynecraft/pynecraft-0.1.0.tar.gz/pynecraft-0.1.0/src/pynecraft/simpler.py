from __future__ import annotations

from typing import Callable, Mapping

from .base import FacingDef, Nbt, NbtDef, Position, _ensure_size, _in_group, _quote, _to_list, good_facing, to_id
from .commands import Block, BlockDef, COLORS, Command, Commands, Entity, JsonList, JsonText, SignCommands, \
    SignText, \
    SomeMappings, fill, good_block, good_color_num, setblock
from .enums import Pattern


class Sign(Block):
    def __init__(self, txt: SignText, /, commands: SignCommands = (), wood='oak', state: Mapping = None,
                 nbt: NbtDef = None):
        wood = to_id(wood)
        super().__init__(self._kind_name(wood), state=state, nbt=nbt)
        self.wood = wood
        txt = _ensure_size(txt, 4)
        commands = _ensure_size(commands, 4)
        lines_nbt = Sign.lines_nbt(txt, commands)
        self.merge_nbt(lines_nbt)
        if nbt:
            self.merge_nbt(nbt)

    @classmethod
    def lines_nbt(cls, text: SignText, commands: SignCommands = ()) -> Nbt:
        text = _to_list(text)
        commands = _to_list(commands)
        max_count = max(len(text), len(commands))
        if max_count > 4:
            raise ValueError('%d: Too many values for text and/or commands' % max_count)
        text = _ensure_size(text, 4)
        commands = _ensure_size(commands, 4)

        nbt = Nbt()
        for i, entry in enumerate(tuple(zip(text, commands))):
            if entry == (None, None):
                continue
            txt, cmd = entry
            if txt is None:
                txt = ''
            key = 'Text%d' % (i + 1)
            if isinstance(txt, str):
                if not cmd:
                    nbt[key] = txt
                    continue
                txt = JsonText.text(txt)
            txt = JsonText.as_json(txt)
            if cmd:
                if isinstance(cmd, Callable):
                    txt = cmd(txt)
                else:
                    txt = txt.click_event().run_command(cmd)
            nbt[key] = txt

        return nbt

    @classmethod
    def text(cls, txt: str) -> str:
        return r'"\"%s\""' % txt.replace('"', r'\\"')

    def _kind_name(self, wood):
        return wood + '_sign'

    def glowing(self, v: bool) -> Sign:
        self.nbt['GlowingText'] = v
        return self

    def color(self, color: str) -> Sign:
        if color is None:
            del self.nbt['Color']
        else:
            self.nbt['Color'] = _in_group(COLORS, color)
        return self

    def place(self, pos: Position, facing: FacingDef, /, water=False, nbt: NbtDef = None) -> Commands:
        self._orientation(facing)
        if water:
            self.merge_state({'waterlogged': True})
        if nbt:
            self.merge_nbt(nbt)
        return (
            setblock(pos, 'water' if water else 'air'),
            setblock(pos, self),
        )

    def _orientation(self, facing):
        self.merge_state({'rotation': good_facing(facing).sign_rotation})


class WallSign(Sign):
    def _kind_name(self, wood):
        return wood + '_wall_sign'

    def _orientation(self, facing):
        self.merge_state({'facing': good_facing(facing).name})


_backslash_map = {'"': '"', '\\': '\\', '\a': 'a', '\b': 'b', '\f': 'f', '\n': 'n', '\r': 'r', '\t': 't', '\v': 'v'}

_fm = {}
for k, v in _backslash_map.items():
    _fm[v] = k


class Book:
    def __init__(self, sign_info: tuple[str, str, str | None] = (None, None, None)):
        _ensure_size(sign_info, 3)
        self.title, self.author, self.display_name = sign_info
        self._pages = []
        self._cur_page = JsonList()

    # Two kinds of books: Written and signed. In theory, they should hold the same kind
    # of text, but the unsigned book cannot have rich text. Hopefully in the future this _will_ be possible, so
    # this method is kept separate instead of being incorporated into the __init__ of a
    # "signed book" class that is separate from the "unsigned book" class. Or some such design.
    def sign_book(self, title: str, author: str, display_name: str = None):
        self.title = title
        self.author = author
        self.display_name = display_name

    def next_page(self):
        self._pages.append(self._cur_page)
        self._cur_page = JsonList()

    def add(self, *txt: JsonText | str):
        if self.title is None:
            raise ValueError("Cannot add Json text to unsigned book")
        for t in txt:
            if isinstance(t, str):
                t = JsonText.text(t)
            self._cur_page.append(t)

    def as_entity(self):
        return Entity('written_book', nbt=self.nbt())

    def as_item(self):
        item = Item.nbt_for('written_book')
        nbt = self.nbt()
        try:
            pages = nbt['pages']
            if pages:
                nbt['pages'] = _quote(pages)
        except KeyError:
            pass

        return Nbt({'Book': item.merge({'tag': nbt})})

    def nbt(self):
        cur_page = self._cur_page
        self.next_page()
        jt = Nbt()
        jt['title'] = self.title
        jt['author'] = self.author
        if self.display_name:
            jt['display_name'] = {'Lore': self.display_name}
        jt['pages'] = list(JsonList(x) for x in self._pages[:])
        self._cur_page = cur_page
        self._pages.pop()
        return jt


class Item(Entity):
    def __init__(self, id: str, count: int = 1, name=None, nbt=None):
        super().__init__(id, name=name)
        self.merge_nbt({'id': id, 'Count': count})
        if nbt:
            self.merge_nbt(nbt)

    @classmethod
    def nbt_for(cls, item: BlockDef, nbt=None) -> Nbt:
        item = good_block(item)
        item_id = item.id
        if item_id.find(':') < 0:
            item_id = 'minecraft:' + item_id
        retval = Nbt({'id': item_id, 'Count': 1})
        # Filled maps are stored directly, not shunted an inner tag
        if item_id:
            if item_id == 'minecraft:filled_map':
                retval = retval.merge(item.nbt)
                if nbt:
                    retval = retval.merge(nbt)
            else:
                retval['tag']['BlockEntityTag'] = item.nbt
        try:
            block_state = item.state
            if block_state:
                retval['tag']['BlockStateTag'] = block_state
        except AttributeError:
            pass
        if nbt:
            return retval.merge(nbt)
        return retval


class Shield(Item):
    def __init__(self, color: int | str):
        super().__init__('shield')
        self.merge_nbt({'tag': {'BlockEntityTag': {'Base': color, 'Patterns': []}}})
        self.color = color

    def add_pattern(self, pattern: str, color: int | str) -> Shield:
        color = good_color_num(color)
        patterns = self.nbt['tag']['BlockEntityTag'].get_list('Patterns')
        patterns.append(Nbt({'Pattern': Pattern(pattern), 'Color': color}))
        return self

    def clear_patterns(self) -> Shield:
        self.nbt['tag']['BlockEntityTag']['Patterns'] = []
        return self


class Volume:
    __slab_states = []
    __stair_states = []
    __door_states = []
    __trapdoor_states = []
    __button_states = []
    __slab_states.append(Nbt({'type': 'double'}))
    __dirs = ("north", "east", "west", "south")
    for __h in ('top', 'bottom'):
        __slab_states.append(Nbt({'type': __h}))
        for __f in __dirs:
            for __s in ('straight', "inner_left", "inner_right", "outer_left", "outer_right"):
                __stair_states.append(Nbt({'half': __h, 'facing': __f, 'shape': __s}))
            for __o in (True, False):
                __trapdoor_states.append(Nbt({'half': __h, 'facing': __f, 'open': __o}))
                for __g in ('left', 'right'):
                    __door_states.append(
                        Nbt({'half': 'upper' if __h == 'top' else 'lower', 'facing': __f, 'open': __o, 'hinge': __g}))
    for __f in __dirs:
        for __t in ('ceiling', 'floor', 'wall'):
            __button_states.append({'facing': __f, 'face': __t})
    slab_states = tuple(__slab_states)
    stair_states = tuple(__stair_states)
    door_states = tuple(__door_states)
    trapdoor_states = tuple(__trapdoor_states)
    button_states = tuple(__button_states)
    facing_states = tuple(Nbt({'facing': x}) for x in __dirs)
    facing_all_states = tuple(Nbt({'facing': x}) for x in __dirs + ('up', 'down'))
    axes_states = tuple(Nbt({'axis': x}) for x in ('x', 'y', 'z'))
    rail_states = tuple(Nbt({'shape': x}) for x in ('east_west', 'north_south') + tuple(
        'ascending_%s' % x for x in ('east', 'west', 'north', 'south')))
    curved_rail_states = tuple(Nbt({'shape': x}) for x in ('north_east', 'north_west', 'south_east', 'south_west'))

    def __init__(self, start: Position, end: Position):
        self.start = start
        self.end = end

    def fill(self, new: BlockDef, replace: BlockDef = None) -> Command:
        f = fill(self.start, self.end, good_block(new))
        if replace:
            f = f.replace(replace)
        yield f

    def replace(self, new: BlockDef, old: BlockDef, states: SomeMappings = None,
                added_states: SomeMappings = None) -> Commands:
        states = _to_list(states) if states else [{}]
        added_states = _to_list(added_states) if added_states else [{}]
        new = good_block(new)
        old = good_block(old)
        if states is None:
            states = ({})
        else:
            states = _to_list(states)

        if not states and not added_states:
            yield from self.fill(new, old)
        else:
            for added in added_states:
                n = new.clone().merge_state(added)
                o = old.clone().merge_state(added)
                for s in states:
                    yield from self.fill(n.clone().merge_state(s), o.clone().merge_state(s))

    def replace_slabs(self, new: BlockDef, old: BlockDef = '#slabs', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.slab_states, added_state)

    def replace_stairs(self, new: BlockDef, old: BlockDef = '#stairs', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.stair_states, added_state)

    def replace_buttons(self, new: BlockDef, old: BlockDef = '#buttons', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.button_states, added_state)

    def replace_doors(self, new: BlockDef, old: BlockDef = '#doors', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.door_states, added_state)

    def replace_trapdoors(self, new: BlockDef, old: BlockDef = '#trapdoors', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.trapdoor_states, added_state)

    def replace_facing(self, new: BlockDef, old: BlockDef, added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.facing_states, added_state)

    def replace_facing_all(self, new: BlockDef, old: BlockDef, added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.facing_all_states, added_state)

    def replace_axes(self, new: BlockDef, old: BlockDef, added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.axes_states, added_state)

    def replace_straight_rails(self, new: BlockDef, old: BlockDef = '#rails', added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.rail_states, added_state)

    def replace_curved_rails(self, new: BlockDef = "rail", old: BlockDef = '#rails',
                             added_state: Mapping = None) -> Commands:
        yield from self.replace(new, old, Volume.curved_rail_states, added_state)


class ItemFrame(Entity):
    def __init__(self, facing: int | str, nbt=None):
        nbt = Nbt.as_nbt(nbt) if nbt else Nbt({})
        nbt = nbt.merge({'Facing': good_facing(facing).number, 'Fixed': True})
        super().__init__('item_frame', nbt=nbt)

    def item(self, item: BlockDef) -> ItemFrame:
        block = good_block(item)
        self.merge_nbt({'Item': Item.nbt_for(block)})
        return self

    def named(self, name: BlockDef = None) -> ItemFrame:
        block = good_block(name)
        if block is None:
            try:
                del self.nbt['Item']['tag']['display']['Name']
            except KeyError:
                pass  # Must not be there already, ignore the error
        else:
            if 'Item' not in self.nbt:
                self.item(block)
            nbt = self.nbt
            nbt['Item']['tag']['display']['Name'] = JsonText.text(block.name)
        return self
