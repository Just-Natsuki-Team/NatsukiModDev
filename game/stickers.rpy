default persistent._jn_natsuki_chibi_seen = False

image sticker blank = "mod_assets/sticker/blank.png"
image sticker blank_cheer = "mod_assets/sticker/blank_cheer.png"
image sticker normal = "mod_assets/sticker/normal.png"

transform jn_sticker_peek_up_down:
    subpixel True
    topleft
    xpos 226
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

    _STICKER_TYPE_IMAGE_MAP = {
        StickerTypes.blank : "sticker blank",
        StickerTypes.blank_cheer : "sticker blank_cheer",
        StickerTypes.normal : "sticker normal"
    }

    _WINDOW_STICKER_Z_INDEX = -1

    def stickerWindowPeekUp(sticker_type=StickerTypes.blank):
        """
        Shows Natsuki sticker peeking up and in from the left-side classroom window, before going back down.
        If the player hasn't seen a chibi before, the _jn_natsuki_chibi_seen flag is set to True.

        IN:
            - sticker_type - The StickerTypes sticker to perform the peek for.
        """
        if (sticker_type not in _STICKER_TYPE_IMAGE_MAP):
            raise ValueError("Sticker type {0} is not a valid type, or has no corresponding image".format(sticker_type))

        renpy.hide("sticker")
        renpy.show(
            name=_STICKER_TYPE_IMAGE_MAP.get(sticker_type),
            at_list=[store.jn_sticker_peek_up_down],
            zorder=_WINDOW_STICKER_Z_INDEX)
        store.persistent._jn_natsuki_chibi_seen = True
