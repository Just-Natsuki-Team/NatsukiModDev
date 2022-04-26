image deco balloons = "mod_assets/deco/balloons.png"
image prop cake lit = "mod_assets/props/cake_lit.png"
image prop cake unlit = "mod_assets/props/cake_unlit.png"

init python in jn_birthdays:
    import store

    JN_BIRTHDAY_DECO_ZORDER = 2
    JN_BIRTHDAY_PROP_ZORDER = 4

    def display_visuals(natsuki_sprite_code):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
        """
        renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        renpy.show_screen("hkb_overlay")
        renpy.play(filename="mod_assets/sfx/light_switch.ogg", channel="audio")
        renpy.pause(2)
        renpy.hide("black")
        #renpy.play(filename="mod_assets/bgm/birthday.ogg", channel="music")

label player_birthday_intro:
    show deco balloons zorder jn_birthdays.JN_BIRTHDAY_PROP_ZORDER
    show prop cake unlit zorder jn_birthdays.JN_BIRTHDAY_PROP_ZORDER
    $ jn_birthdays.display_visuals("")
    $ jn_globals.force_quit_enabled = True

    n "Happy birthday, [player]!"
    n "Betcha' didn't think I had something planned all along, did you?"
    extend " Ehehe."
    n "Don't lie!"
    extend " I know I got you {i}real{/i} good this time!"
    n "Well, whatever."
    extend " We both know what you're waiting for, huh?"
    n "Yeah, yeah."
    extend " I got you covered, [player]."

    show prop cake lit zorder jn_birthdays.JN_BIRTHDAY_PROP_ZORDER
    play audio necklace_clip

    n "..."
    n "What?!"
    extend " You don't {i}seriously{/i} expect me to sing all by myself?"
    extend " No way!"
    n "..."
    n "But..."

    jump player_birthday_outro

label player_birthday_outro:
    n "Birthday ending~"
    return
