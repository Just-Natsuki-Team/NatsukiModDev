transform jn_gift_slide_up:
    subpixel True
    ypos 133
    easein 2 ypos 0

init -5 python in jn_gifts:
    import store

    _GIFT_ZORDER = 4

    class JNGift():
        def __init__(self, color, zorder):
            """
            """
            self.color = color
            self.zorder = zorder
            base_tag = "gift {0}".format(color)

            self.closed_tag = "gift_{0} closed".format(self.color)
            self.open_tag = "gift_{0} open".format(self.color)
            self.empty_tag = "gift_{0} empty".format(self.color)

            renpy.image(self.closed_tag, store.Image("mod_assets/props/gifts/{0}/closed.png".format(self.color)))
            renpy.image(self.open_tag, store.Image("mod_assets/props/gifts/{0}/open.png".format(self.color)))
            renpy.image(self.empty_tag, store.Image("mod_assets/props/gifts/{0}/empty.png".format(self.color)))

        def present(self):
            """
            """
            renpy.show(
                name=self.closed_tag,
                at_list=[store.jn_gift_slide_up],
                zorder=self.zorder
            )

        def open(self):
            """
            """
            renpy.show(
                name=self.open_tag,
                at_list=[],
                zorder=self.zorder
            )

        def empty(self):
            """
            """
            renpy.show(
                name=self.empty_tag,
                at_list=[],
                zorder=self.zorder
            )

        def hide(self):
            """
            """
            renpy.hide("gift_{0}".format(self.color))

    GIFT_BLUE = JNGift(
        color="blue",
        zorder=4
    )
    GIFT_GREEN = JNGift(
        color="green",
        zorder=4
    )
    GIFT_PINK = JNGift(
        color="pink",
        zorder=4
    )
    GIFT_PURPLE = JNGift(
        color="purple",
        zorder=4
    )