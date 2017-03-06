from libqtile.config import Screen
from libqtile import bar, widget
import os

login_user = os.environ['USER']
wallpaper_dir = os.environ['WALLPAPER_DIR']


# Widget defaults config

widget_defaults = dict(
    font='Droid Sans Mono Dotted For Powerline',
    fontsize=16,
    padding=10,
    background='#2f343f',
    fontshadow='#2f343f',
    foreground='#f3f4f5',
    markup=True,
)

# KeyboardLayout config
keyboardlayout_c= dict(
    configured_keyboards=['us', 'il'],
    update_interval=1,
)

# Wallpaper config
wallpaper_c = dict(
    directory=wallpaper_dir,
    label='',
)

# GroupBox config
groupbox_c = dict(
    padding=3,
)

# User login name
user_login_textbox_c = dict(
    name="default",
)


# Seperator config
seperator_c = dict(
    linewidth=2,
    size_percent=60,
)

# Clock date config
clock_time_c = dict(
    format='%I:%M %p',
)

# Clock time config
clock_date_c = dict(
    format='%Y-%m-%d %a',
)




################
# Screens start
################

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Wallpaper(**wallpaper_c),
                widget.KeyboardLayout(**keyboardlayout_c),
                widget.GroupBox(**groupbox_c),
                widget.Sep(**seperator_c),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox(login_user.title()),
                widget.Sep(**seperator_c),
                widget.Clock(**clock_time_c),
                widget.Sep(**seperator_c),
                widget.Clock(**clock_date_c),
            ],
            30,
        ),
    ),
]
