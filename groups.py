from libqtile.config import Group, Match

#mod = "mod4"

#group_list = [
#    "Browser",
#    "Shell",
#    "Media",
#    "Files",
#    ]
#
#groups = [Group(i) for i in group_list ]

groups = [
    Group("  ", matches=[Match(wm_class=["Firefox"])]),
    Group("  "),
    Group("  "),
    Group("  "),
]
