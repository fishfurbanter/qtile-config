from libqtile.config import Key, Drag, Click
from libqtile import widget
from libqtile.command import lazy, Client
from libqtile.dgroups import simple_key_binder
from libqtile.widget import KeyboardLayout

MOD = "mod4"
MOD1 = "mod1"
dgroups_key_binder = simple_key_binder(MOD)

keys = [
    # Switch between windows in current stack pane
    Key(
        [MOD], "k",
        lazy.layout.down()
    ),
    Key(
        [MOD], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [MOD, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [MOD, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [MOD], "n",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [MOD, "shift"], "space",
        lazy.layout.rotate()
    ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([MOD], "Return", lazy.spawn("kitty")),
    Key([MOD], "t", lazy.spawn("kitty")),

    Key([MOD, "shift"], "u", lazy.spawn("kitty -e ranger")),

    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout()),
    Key([MOD, "shift"], "w", lazy.window.kill()),

    Key([MOD, "control"], "r", lazy.restart()),
    Key([MOD, "control"], "q", lazy.shutdown()),
    Key([MOD], "d", lazy.spawncmd()),
    Key([MOD, "shift"], "h", lazy.layout.grow_right()),
    Key([MOD, "shift"], "l", lazy.layout.grow_left()),

    # Start applications
    Key([MOD], "f", lazy.spawn("firefox")),
    Key([MOD], "m", lazy.spawn("pcmanfm")),
    Key(["shift"], "space",
        lazy.widget["keyboardlayout"].next_keyboard()),

]


mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
                start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
                start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]
