from libqtile.config import Screen
from libqtile import bar, widget
import os

bar_textbox = os.environ['USER'].title()
seperator = ' | '

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox(bar_textbox, name="default"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d ' + seperator + '%a %I:%M %p'),
            ],
            30,
        ),
    ),
]
