from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile import layout, bar, widget, hook
from libqtile.command import lazy
import os
from keys import mod, dgroups_key_binder, keys
from groups import groups
from screens import screens, widget_defaults
from box import InfoBox
#from libqtile.window import Internal
#from libqtile.drawer import Drawer
#from libqtile.scripts import qtile

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


def main(qtile):
    #pass
    default_infobox = dict(
        x = 500,
        y = 500,
        x_internal = 100,
        y_internal = 100,
        height = 300,
        width = 300,
        height_internal = 100,
        width_internal = 100,
        opacity_internal = 1,
        hide_box = True,
    )
    InfoBox.create_box(qtile, **default_infobox)

