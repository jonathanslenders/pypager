from __future__ import unicode_literals
from prompt_toolkit.key_binding.bindings.scroll import scroll_page_up, scroll_page_down, scroll_one_line_down, scroll_one_line_up, scroll_half_page_up, scroll_half_page_down
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.filters import HasFocus
from prompt_toolkit.enums import DEFAULT_BUFFER, SEARCH_BUFFER, IncrementalSearchDirection
from prompt_toolkit.keys import Keys

__all__ = (
    'create_key_bindings',
)

# Key bindings.
manager = KeyBindingManager(
    enable_vi_mode=False,
    enable_search=True,
    enable_extra_page_navigation=True,
    enable_system_bindings=False)
handle = manager.registry.add_binding

default_focus = HasFocus(DEFAULT_BUFFER)


@handle('q', filter=default_focus)
@handle('Q', filter=default_focus)
@handle('Z', 'Z', filter=default_focus)
def _(event):
    " Quit. "
    event.cli.set_return_value(None)


@handle(' ', filter=default_focus)
@handle('f', filter=default_focus)
@handle(Keys.ControlF, filter=default_focus)
@handle(Keys.ControlV, filter=default_focus)
def _(event):
    " Page down."
    scroll_page_down(event)


@handle('b', filter=default_focus)
@handle(Keys.ControlB, filter=default_focus)
@handle(Keys.Escape, 'v', filter=default_focus)
def _(event):
    " Page up."
    scroll_page_up(event)


@handle('d', filter=default_focus)
@handle(Keys.ControlD, filter=default_focus)
def _(event):
    " Half page down."
    scroll_half_page_down(event)


@handle('u', filter=default_focus)
@handle(Keys.ControlU, filter=default_focus)
def _(event):
    " Half page up."
    scroll_half_page_up(event)


@handle('e', filter=default_focus)
@handle('j', filter=default_focus)
@handle(Keys.ControlE, filter=default_focus)
@handle(Keys.ControlN, filter=default_focus)
@handle(Keys.ControlJ, filter=default_focus)
@handle(Keys.ControlM, filter=default_focus)
def _(event):
    " Scoll one line down."
    scroll_one_line_down(event)


@handle('y', filter=default_focus)
@handle('k', filter=default_focus)
@handle(Keys.ControlY, filter=default_focus)
@handle(Keys.ControlK, filter=default_focus)
@handle(Keys.ControlP, filter=default_focus)
def _(event):
    " Scoll one line up."
    scroll_one_line_up(event)


@handle('/', filter=default_focus)
def _(event):
    " Start searching forward. "
    event.cli.search_state.direction = IncrementalSearchDirection.FORWARD
    # get_vi_state(event.cli).input_mode = InputMode.INSERT
    event.cli.push_focus(SEARCH_BUFFER)


@handle('?', filter=default_focus)
def _(event):
    " Start searching backwards. "
    event.cli.search_state.direction = IncrementalSearchDirection.BACKWARD
    # get_vi_state(event.cli).input_mode = InputMode.INSERT
    event.cli.push_focus(SEARCH_BUFFER)


@handle('n', filter=default_focus)
def _(event):
    " Search next. "
    event.current_buffer.apply_search(
        event.cli.search_state, include_current_position=False,
        count=event.arg)


@handle('N', filter=default_focus)
def _(event):
    " Search previous. "
    event.current_buffer.apply_search(
        ~event.cli.search_state, include_current_position=False,
        count=event.arg)


def create_key_bindings():
    return manager
