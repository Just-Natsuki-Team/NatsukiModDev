transform jn_gift_slide_up:
    subpixel True
    ypos 133
    easein 2 ypos 0

init -5 python in jn_gifts:
    import os
    import store
    import store.jn_utils as jn_utils

    GIFT_DIRECTORY = os.path.join(renpy.config.basedir, "characters").replace("\\", "/")

    _GIFT_ZORDER = 4

    def getGiftFileExists(gift_name):
        """
        Returns whether the given gift exists in the configured gift directory, with a .nats prefix.

        IN:
            - gift_name - str name of the gift to check for
        OUT:
            - True if the gift exists, otherwise False
        """
        return jn_utils.getFileExists(os.path.join(GIFT_DIRECTORY, "{0}.nats".format(gift_name)).replace("\\", "/"))

    class JNGiftBox():
        def __init__(self, color, zorder):
            """
            Initialises a new instance of JNGiftBox.

            IN:
                - color - The str color of the gift; matching open/closed/empty assets must exist in mod_assets/props/gifts
                - zorder - The int zorder in which to display the gift for its animations
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
            Presents the gift by sliding it slowly up from the bottom of the screen, onto Natsuki's desk.
            """
            renpy.play("mod_assets/sfx/gift_slide.ogg")
            renpy.show(
                name=self.closed_tag,
                at_list=[store.jn_gift_slide_up],
                zorder=self.zorder
            )

        def open(self):
            """
            Shows the gift in an open state, with the lid on one side.
            """
            renpy.play("mod_assets/sfx/gift_open.ogg")
            renpy.show(
                name=self.open_tag,
                at_list=[],
                zorder=self.zorder
            )

        def empty(self):
            """
            Shows the gift in an empty state.
            """
            renpy.show(
                name=self.empty_tag,
                at_list=[],
                zorder=self.zorder
            )

        def close(self):
            """
            Shows the gift with its lid back on.
            """
            renpy.play("mod_assets/sfx/gift_close.ogg")
            renpy.show(
                name=self.closed_tag,
                at_list=[],
                zorder=self.zorder
            )

        def hide(self):
            """
            Hides the gift entirely.
            """
            renpy.hide("gift_{0}".format(self.color))

    GIFT_BLUE = JNGiftBox(
        color="blue",
        zorder=_GIFT_ZORDER
    )
    GIFT_GREEN = JNGiftBox(
        color="green",
        zorder=_GIFT_ZORDER
    )
    GIFT_PINK = JNGiftBox(
        color="pink",
        zorder=_GIFT_ZORDER
    )
    GIFT_PURPLE = JNGiftBox(
        color="purple",
        zorder=_GIFT_ZORDER
    )
