from libqtile.window import Internal
from libqtile.drawer import Drawer

"""
def mybox(qtile):
    name = "mybox"
    height = 300
    width = 300
    win = Internal.create(
    qtile, x=150, y=150, width=width, height=height, opacity=1
        )

    drawer = Drawer(qtile, win.window.wid, width, height)
    drawer.clear("f0f000")

    qtile.windowMap[win.window.wid] = win
    win.place(300, 100, 100, 300, 5, 100)
    win.handle_Expose = lambda e: drawer.draw()
    win.handle_ButtonPress = lambda e: None
    win.unhide()
"""

class InfoBox:
    def __init__(self, qtile, **default_infobox):
        x = self.x
        y = self.y
        x_internal = self.x_internal
        y_internal = self.y_internal
        height_internal = self.height_internal
        width_internal = self.width_internal
        opacity_internal = self.opacity_internal
        height = self.height
        width = self.width
        hide_box = self.hide_box


    def create_box(qtile, x, y, x_internal, y_internal, height_internal, width_internal, opacity_internal, height, width, hide_box):
        win = Internal.create(
            qtile, x = x_internal, y = y_internal, width=width_internal, height=height_internal, opacity=opacity_internal
        )

        drawer = Drawer(qtile, win.window.wid, width, height)
        drawer.clear("f0f000")

        qtile.windowMap[win.window.wid] = win
        win.place(height, width, x, y, 5, 100)
        win.handle_Expose = lambda e: drawer.draw()
        win.handle_ButtonPress = lambda e: button_press()
        win.unhide()
        def button_press():
            if hide_box == True:
                win.hide()
        button_press()
