from libqtile.config import Screen
from libqtile import bar, widget
import os


# Collected data
login_user = os.environ['USER'] + " "
wallpaper_dir = os.environ['WALLPAPER_DIR']


# Widget defaults config
widget_defaults = dict(
    font='Droid Sans Mono Dotted For Powerline',
    fontsize=16,
    background='#2f343f',
    padding=10,
    fontshadow='#2f343f',
    foreground='#f3f4f5',
    markup=True,
)

# KeyboardLayout config
keyboardlayout_c = dict(
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

seperator_g = dict(
    linewidth=2,
    size_percent=60,
    padding=15,
)

# Clock date config
clock_time_c = dict(
    format='%I:%M %p',
)

# Clock time config
clock_date_c = dict(
    format='%Y-%m-%d %a',
)

# Volume config
volume_c = dict(
    channel='Master',
    device='default',
    get_volume_command='',
)

# Network statistics
netgraph_c = dict(
    samples=100,
    line_width=3,
    margin_x=1,
    margin_y=1,
    width=100,
)

# Pacman widget config
pacman_c = dict(
    distro='Arch',
    execute='pacman -Qu',
)

# Prompt config
prompt_c = dict(
)

# Padding is added to override
# defaults, when padding > 3
# the object exceeds container
# limits
tasklist_c = dict(
    maxwidth='2000',
    borderwidth=2,
    fontsize=15,
    padding=3,
)


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Wallpaper(**wallpaper_c),
                widget.TextBox(login_user.title()),
                widget.KeyboardLayout(**keyboardlayout_c),
                widget.Sep(**seperator_c),
                widget.Clock(**clock_time_c),
                widget.Sep(**seperator_c),
                widget.GroupBox(**groupbox_c),
                widget.Sep(**seperator_c),
                widget.Prompt(name='prompt',
                              bell_style='visual', prompt='>>>  ',
                              visual_bell_color=widget_defaults['background'],
                              **widget_defaults),
                widget.TaskList(**tasklist_c),
                widget.Sep(**seperator_c),
                widget.Clock(**clock_date_c),
                widget.Sep(**seperator_c),
                widget.TextBox(text='  '),
                widget.CPUGraph(),
                widget.TextBox(text=''),
                widget.TextBox(text='  '),
                widget.NetGraph(),
                widget.TextBox(text=' '),
            ],
            27,
        ),
    ),
]
