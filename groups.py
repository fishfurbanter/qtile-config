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
    Group("Browser", matches=[Match(wm_class=["Firefox"])]),
    Group("Shell"),
    Group("Media"),
    Group("Files"),
]
