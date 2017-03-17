# Libqtile imports
from libqtile import layout

layouts = [
    layout.Max(),
    layout.Tile(name="terminals", border_focus="#000000"),
    layout.Stack(num_stacks=2, border_focus='#383c4a'),
    layout.TreeTab()
]
