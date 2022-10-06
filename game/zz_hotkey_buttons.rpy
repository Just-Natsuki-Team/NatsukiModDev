init python:
    def HKBHideButtons():
        """
        Hides hotkeybuttons
        """
        config.overlay_screens.remove("hkb_overlay")
        renpy.hide_screen("hkb_overlay")


    def HKBShowButtons():
        """
        Shows hotkeybuttons
        """
        config.overlay_screens.append("hkb_overlay")

init -1 python in hkb_button:
    enabled = True

# Standard hotkey
define gui.hkb_button_width = 120
define gui.hkb_button_height = None
define gui.hkb_button_tile = False
define gui.hkb_button_borders = Borders(100, 5, 100, 5)
define gui.hkb_button_text_font = gui.default_font
define gui.hkb_button_text_size = gui.button_text_size
define gui.hkb_button_text_xalign = 0.5
define gui.hkb_button_text_idle_color = "#e2d1d1"
define gui.hkb_button_text_hover_color = "#FF8ED0"

# Black hotkey
define gui.hkb_button_black_width = 120
define gui.hkb_button_black_height = None
define gui.hkb_button_black_tile = False
define gui.hkb_button_black_borders = Borders(100, 5, 100, 5)
define gui.hkb_button_black_text_font = gui.default_font
define gui.hkb_button_black_text_size = gui.button_text_size
define gui.hkb_button_black_text_xalign = 0.5
define gui.hkb_button_black_text_idle_color = "#e2d1d1"
define gui.hkb_button_black_text_hover_color = "#FF8ED0"

# Label
define gui.hkb_label_width = 400
define gui.hkb_label_height = None
define gui.hkb_label_tile = False
define gui.hkb_label_borders = Borders(5, 7, 5, 7)
define gui.hkb_label_text_font = gui.default_font
define gui.hkb_label_text_size = 20
define gui.hkb_label_text_xalign = 0.5
define gui.hkb_label_text_color = "#e2d1d1"

# Option hotkey
define gui.hkb_option_width = 200
define gui.hkb_option_height = None
define gui.hkb_option_tile = False
define gui.hkb_option_borders = Borders(5, 5, 5, 5)
define gui.hkb_option_text_font = gui.default_font
define gui.hkb_option_text_size = gui.button_text_size
define gui.hkb_option_text_xalign = 0.5
define gui.hkb_option_text_idle_color = "#e2d1d1"
define gui.hkb_option_text_hover_color = "#FF8ED0"

define gui.talk_button_width = 120
define gui.talk_button_height = None
define gui.talk_button_tile = False
define gui.talk_button_borders = Borders(100, 5, 100, 5)
define gui.talk_button_text_font = gui.default_font
define gui.talk_button_text_size = gui.button_text_size
define gui.talk_button_text_xalign = 0.5
define gui.talk_button_text_idle_color = "#e2d1d1"
define gui.talk_button_text_hover_color = "#FF8ED0"
default allow_boop = False

style hkb_vbox is vbox
style hkb_button is button
style hkb_button_text is button_text

style hkb_vbox_black is vbox
style hkb_button_black is button
style hkb_button_black_text is button_text

style hkb_vbox_label is vbox
style hkb_label is label

style hkb_vbox_option is vbox
style hkb_option is button
style hkb_option_text is button_text

style talk_vbox is vbox
style talk_button is button
style talk_button_text is button_text

style hkb_vbox:
    spacing 0

style hkb_vbox_black:
    spacing 0

style hkb_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/buttons/hkb_idle_background.png"
    hover_background "mod_assets/buttons/hkb_hover_background.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_black is default:
    properties gui.button_properties("hkb_button_black")
    idle_background "mod_assets/buttons/hkb_idle_background_black.png"
    hover_background "mod_assets/buttons/hkb_hover_background_black.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_label is default:
    properties gui.button_properties("hkb_label")
    background "mod_assets/buttons/choice_hover_blank.png"

style hkb_option is default:
    properties gui.button_properties("hkb_option")
    idle_background "mod_assets/buttons/option_hover_blank.png"
    hover_background "mod_assets/buttons/option_hover_fold.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_text is default:
    properties gui.button_text_properties("hkb_button")
    outlines []

style hkb_button_text_black is default:
    properties gui.button_text_properties("hkb_button_black")
    outlines []

style hkb_label_text is default:
    properties gui.button_text_properties("hkb_label")
    outlines []

style hkb_option_text is default:
    properties gui.button_text_properties("hkb_option")
    outlines []

style talk_vbox:
    spacing 0

style talk_button is default:
    properties gui.button_properties("talk_button")
    idle_background "mod_assets/buttons/talk_idle_background.png"
    hover_background "mod_assets/buttons/talk_hover_background.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style talk_button_text is default:
    properties gui.button_text_properties("talk_button")
    outlines []

style hkbd_vbox is hkb_vbox
style hkbd_button is button
style hkbd_button_text is button_text

style hkbd_vbox:
    spacing 0

style hkbd_button is default:
    properties gui.button_properties("hkb_button")
    insensitive_background "mod_assets/buttons/hkb_disabled_background.png"
    idle_background "mod_assets/buttons/hkb_idle_background.png"
    hover_background "mod_assets/buttons/hkb_hover_background.png"
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkbd_button_text is default:
    font gui.default_font
    size gui.button_text_size
    xalign 0.5
    idle_color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines []

style hkbd_button_black is default:
    properties gui.button_properties("hkb_button_black")
    idle_background "mod_assets/buttons/hkb_idle_background.png"
    hover_background "mod_assets/buttons/hkb_idle_background.png"

style hkbd_button_text_black is default:
    font gui.default_font
    size gui.button_text_size
    xalign 0.5
    idle_color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines []

style hkbd_label is default:
    properties gui.button_properties("hkb_label")
    background "mod_assets/buttons/choice_hover_blank.png"

style hkbd_label_text is default:
    font gui.default_font
    size 20
    xalign 0.5
    color "#e2d1d1"
    outlines []

style hkbd_option_text is default:
    font gui.default_font
    size gui.button_text_size
    xalign 0.5
    idle_color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines []

style hkbd_option is default:
    properties gui.button_properties("hkb_option")
    idle_background "mod_assets/buttons/option_hover_blank.png"
    hover_background "mod_assets/buttons/option_hover_fold.png"
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style talkd_vbox is vbox
style talkd_button is button
style talkd_button_text is button_text

style talkd_vbox_black is vbox
style talkd_button_black is button
style talkd_button_text_black is button_text

style talkd_vbox:
    spacing 0

style talkd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/buttons/hkb_disabled_background.png"
    hover_background "mod_assets/buttons/hkb_disabled_background.png"

style talkd_button_text is default:
    font gui.default_font
    size gui.button_text_size
    xalign 0.5
    idle_color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines []

screen hkb_overlay:
    zorder 50

    style_prefix "hkb"

    key "t" action [ Jump("talk_menu"),
                SensitiveIf(not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame) 
            ]

    
    key "m" action [
                Jump("music_menu"),
                SensitiveIf(persistent.jn_custom_music_explanation_given and Natsuki.isHappy(higher=True) not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame)
                ]
    key "e" action [
        Jump("extras_menu"),
        SensitiveIf(not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame)
    ]

    vbox:
        xalign 0.09
        yalign 0.97

        textbutton _("Talk"):
            action [
                Jump("talk_menu"),
                SensitiveIf(not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame)
            ]
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound

            style "hkbd_button"

        if persistent.jn_custom_music_explanation_given and Natsuki.isHappy(higher=True):
            textbutton _("Music"):
                action [
                    Jump("music_menu"),
                    SensitiveIf(not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame)
                ]
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

                style "hkbd_button"

        textbutton _("Extras"):
            action [
                Jump("extras_menu"),
                SensitiveIf(not jn_globals.player_is_in_conversation and not jn_globals.player_is_ingame)
            ]
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound

            style "hkbd_button"
