init python in jn_scritch:
    import os
    import pygame
    import random

    _SCRITCH_UI_Z_INDEX = 4
    _SCRITCH_POPUP_Z_INDEX = 5

    _FINISHED_START_QUIPS = [
        "...Satisfied?",
        "Happy now,{w=0.1} [player]?",
        "...Y-{w=0.3}you're done now?"
    ]

    _FINISHED_END_QUIPS = [
        "...Good.",
        "...About time.",
        "Finally...{w=0.3} jeez..."
    ]

    # Tracking
    _has_been_scritched = False
    _scritch_count = 0

    # Collision detection
    game_window = pygame.Surface((1280, 720))
    active_scritch_area = pygame.Rect(457, 105, 353, 163)

label scritch_start:
    $ jn_globals.player_is_ingame = True
    n 1kwdajl "H-{w=0.1}huh?!"
    n 1kbkeml "W-{w=0.1}wait...!"
    show screen scritch_ui
    jump scritch_loop

label scritch_loop:
    $ current_mouse_position = jn_debug.get_mouse_position()

    if not jn_scritch._has_been_scritched:
        show natsuki scritch nervous
        $ renpy.pause(2)

    if jn_scritch.active_scritch_area.collidepoint(current_mouse_position[0], current_mouse_position[1]):
        $ jn_scritch._has_been_scritched = True
        $ jn_scritch._scritch_count += 1
        play audio scritch
        show scritch_popup zorder jn_scritch._SCRITCH_POPUP_Z_INDEX
        hide scritch_popup with popup_hide_transition
        show natsuki scritch active
        $ renpy.pause(1)

    elif jn_scritch._has_been_scritched:
        show natsuki scritch waiting
        $ renpy.pause(2)

    jump scritch_loop

label scritch_finished:
    $ finished_start_quip = renpy.substitute(random.choice(jn_scritch._FINISHED_START_QUIPS))
    n 1kwmpul "[finished_start_quip]"
    $ finished_end_quip = renpy.substitute(random.choice(jn_scritch._FINISHED_END_QUIPS))
    n 1kllpul "[finished_end_quip]"
    n 1kcsdvf "..."
    hide screen scritch_ui
    $ jn_globals.player_is_ingame = False
    jump ch30_loop

define popup_hide_transition = Dissolve(0.75)
define audio.scritch = "mod_assets/sfx/scritch.mp3"

image scritch_popup:
    block:
        choice:
            "dev/mod_assets/ui/scritch_a.png"
        choice:
            "dev/mod_assets/ui/scritch_b.png"
        choice:
            "dev/mod_assets/ui/scritch_c.png"

image natsuki scritch nervous:
    block:
        choice:
            "natsuki 1kllemf"
        choice:
            "natsuki 1klremf"
        choice:
            "natsuki 1klrunf"
        choice:
            "natsuki 1kllunf"
        choice:
            "natsuki 1fcsunf"

        pause 3
        repeat

image natsuki scritch waiting:
    block:
        choice:
            "natsuki 1knmpul"
        choice:
            "natsuki 1kslbol"
        choice:
            "natsuki 1ksrbol"
        choice:
            "natsuki 1kwmbol"
        choice:
            "natsuki 1kllbol"
        choice:
            "natsuki 1klrbol"
        choice:
            "natsuki 1klrunl"
        choice:
            "natsuki 1kllunl"

        pause 5
        repeat

image natsuki scritch active:
    block:
        choice:
            "natsuki 1kcssmf"
        choice:
            "natsuki 1kchcaf"
        choice:
            "natsuki 1fchcaf"
        choice:
            "natsuki 1kslcaf"
        choice:
            "natsuki 1ksrcaf"
        choice:
            "natsuki 1kcscaf"
        choice:
            "natsuki 1kchpuf"

        pause 2
        repeat

screen scritch_ui:
    zorder jn_scritch._SCRITCH_UI_Z_INDEX

    text "{0} scritches".format(jn_scritch._scritch_count) size 30 xpos 555 ypos 60 style "categorized_menu_button"
    
    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440

        textbutton _("Done"):
            style "hkbd_button"
            action [Function(renpy.jump, "scritch_finished")]
