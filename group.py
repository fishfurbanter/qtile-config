from libqtile.config import Group, Match





groups = [
    Group("  ", matches=[Match(wm_class=["Firefox"])]),
    Group("  ", layout="terminals" ,matches=[Match(wm_class=["URxvt"])]),
    Group("  ", matches=[Match(wm_class=["Pcmanfm"])]),
    Group("  "),
]
