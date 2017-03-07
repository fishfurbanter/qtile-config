from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile import layout, bar, widget, hook
from libqtile.command import lazy
import os
from keys import mod, dgroups_key_binder, keys
from groups import groups
from screens import screens, widget_defaults

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2, border_focus='#383c4a'),
    layout.TreeTab()
]


# Drag floating layouts.

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []

# For java UI Toolkit
wmname = "LG3D"

dgroups_app_rules = []

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
