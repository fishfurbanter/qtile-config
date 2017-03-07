from libqtile.config import Key, Drag, Click
from libqtile import widget
from libqtile.command import lazy, Client
from libqtile.dgroups import simple_key_binder
from libqtile.widget import KeyboardLayout



c = Client()
mod = "mod4"
mod1 = "mod1"
dgroups_key_binder = simple_key_binder(mod)

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "n",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "d", lazy.spawncmd()),

    # Start applications
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "m", lazy.spawn("pcmanfm")),
    Key(["shift"], "space",
        lazy.widget["keyboardlayout"].next_keyboard()),
]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
                start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
                start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
