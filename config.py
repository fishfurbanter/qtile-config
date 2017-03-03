from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile import layout, bar, widget
from libqtile.command import lazy
import os
from keys import mod, dgroups_key_binder, keys
from groups import groups
from screens import screens

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='DroidSansMonoForPowerline Nerd',
    fontsize=16,
    padding=3,
    background='#2f343f',
    fontshadow='#676E7D',
    foreground='#f3f4f5',
    low_foreground='#676E7D',
)




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
