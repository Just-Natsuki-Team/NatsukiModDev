default persistent._jn_natsuki_chibi_seen = False

# Peeks the sticker up from the left classroom window
transform jn_sticker_peek_up_down_left:
    subpixel True
    topleft
    xpos 226
    ypos 400
    easein 3 ypos 337
    pause 1.0
    easeout 2 ypos 400

# Peeks the sticker up from the right classroom window
transform jn_sticker_peek_up_down_right:
    subpixel True
    topleft
    xpos 1022
    ypos 400
    easein 3 ypos 337
    pause 1.0
    easeout 2 ypos 400   

init 0 python in jn_stickers:
    from Enum import Enum
    import store

    class StickerTypes(Enum):
        """
        Identifiers for different weather objects, used for sanity checks when changing weather.
        """
        blank = 1
        blank_cheer = 2
        normal = 3

        def __str__(self):
            return self.name

    def stickerWindowPeekUp(sticker_type=StickerTypes.blank, at_right=False):
        """
        Shows Natsuki sticker peeking up and in from the classroom window (left by default), before going back down.
        If the player hasn't seen a chibi before, the _jn_natsuki_chibi_seen flag is set to True.

        IN:
            - sticker_type - The StickerTypes sticker to perform the peek for.
            - at_right - If True, display the sticker at the right-side window
        """
        renpy.hide("sticker")
        at_list = [store.jn_sticker_peek_up_down_right] if at_right else [store.jn_sticker_peek_up_down_left]
        renpy.show(
            name="sticker {0}".format(sticker_type.__str__()),
            at_list=at_list,
            what=store.Image("mod_assets/sticker/{0}.png".format(sticker_type.__str__())),
            zorder=-1)

        store.persistent._jn_natsuki_chibi_seen = True
