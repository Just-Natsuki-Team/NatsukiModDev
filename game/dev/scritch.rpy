default persistent.jn_scritches_total_given = 0

init python in jn_scritch:
    import os
    import pygame
    import random

    _SCRITCH_UI_Z_INDEX = 4
    _SCRITCH_POPUP_Z_INDEX = 5

    _FINISHED_START_QUIPS = [
        "...Satisfied?",
        "Happy now,{w=0.1} [player]?",
        "...Y-{w=0.3}you're done now?",
        "A-{w=0.1}all done,{w=0.1} [player]?",
        "I-{w=0.1}is that all,{w=0.1} [player]?"
    ]

    _FINISHED_END_QUIPS = [
        "...Good.",
        "...About time.",
        "Finally...{w=0.3} jeez...",
        "Took you long enough.",
        "Finally..."
    ]

    # Tracking
    _has_been_scritched = False

    # Collision detection
    game_window = pygame.Surface((1280, 720))
    active_scritch_area = pygame.Rect(457, 105, 353, 163)

label scritch_start:
    $ jn_globals.player_is_ingame = True
    n 1kwdajl "H-{w=0.1}huh?!"

    if persistent.jn_scritches_total_given < 5:
        n 1kbkeml "W-{w=0.1}wait...!"

    elif persistent.jn_scritches_total_given < 25:
        n 1kllunl "...Fine." 

    elif persistent.jn_scritches_total_given < 50:
        n 1kllssl "...Okay."

    elif persistent.jn_scritches_total_given < 250:
        n 1kllssl "Sure."

    else:
        n 1kcsssl "...Yes please."
    
    show screen scritch_ui
    jump scritch_loop

label scritch_loop:
    $ current_mouse_position = utils.get_mouse_position()

    if not jn_scritch._has_been_scritched:
        if persistent.jn_scritches_total_given < 5:
            show natsuki scritch nervous

        else:
            show natsuki scritch waiting
            
        $ renpy.pause(2)

    if jn_scritch.active_scritch_area.collidepoint(current_mouse_position[0], current_mouse_position[1]):
        $ jn_scritch._has_been_scritched = True
        $ persistent.jn_scritches_total_given += 1
        play audio scritch
        show scritch_popup zorder jn_scritch._SCRITCH_POPUP_Z_INDEX
        hide scritch_popup with popup_hide_transition
        show natsuki scritch active
        $ renpy.pause(1)

        # Scritch milestones
        if persistent.jn_scritches_total_given == 5:
            jump scritch_milestone_5

        elif persistent.jn_scritches_total_given == 10:
            jump scritch_milestone_10

        elif persistent.jn_scritches_total_given == 25:
            jump scritch_milestone_25

        elif persistent.jn_scritches_total_given == 50:
            jump scritch_milestone_50

        elif persistent.jn_scritches_total_given == 100:
            jump scritch_milestone_100

        elif persistent.jn_scritches_total_given == 250:
            jump scritch_milestone_250

        elif persistent.jn_scritches_total_given == 500:
            jump scritch_milestone_500

        elif persistent.jn_scritches_total_given == 1000:
            jump scritch_milestone_1000

        elif persistent.jn_scritches_total_given % 1000 == 0:
            jump scritch_milestone_1000_plus

    elif jn_scritch._has_been_scritched:
        show natsuki scritch waiting
        $ renpy.pause(2)

    jump scritch_loop

label scritch_milestone_5:
    n 1kwmpol "...Enjoying yourself,{w=0.1} [player]?"
    n 1kllpof "..."
    jump scritch_loop

label scritch_milestone_10:
    n 1knmpul "You're still going,{w=0.1} huh?"
    n 1kllpul "..."
    n 1kllpof "...I never said stop."
    jump scritch_loop

label scritch_milestone_25:
    n 1klrpol "This...{w=0.3} isn't so bad.{w=0.2} I guess."
    n 1klrssf "...You can keep going."
    jump scritch_loop

label scritch_milestone_50:
    n 1kchssl "..."
    n 1knmajl "W-what?"
    n 1klrslf "I didn't say you should stop..."
    jump scritch_loop

label scritch_milestone_100:
    n "...You really enjoy doing this,{w=0.1} huh?"
    n "I'm...{w=0.3} warming up to it."
    jump scritch_loop
    
label scritch_milestone_250:
    n 1kllsml "..."
    n 1knmnvl "...Well?{w=0.2} Keep going,{w=0.1} [player]..."
    jump scritch_loop
    
label scritch_milestone_500:
    n 1knmnvl "..."
    n 1kcssml "..."
    jump scritch_loop

label scritch_milestone_1000:
    n 1kllsml "..."
    n 1kwmssl "...More?"
    jump scritch_loop

label scritch_milestone_1000_plus:
    n 1kcssml "...[player]..."
    jump scritch_loop

label scritch_finished:
    if random.choice(range(4)) == 3:
        n 1kllunf "..."
        n 1knmpuf "Uhmm...{w=0.3} [player]?"
        n 1klrssf "Could you...{w=0.3} you know..."
        n 1klrpof "Keep doing that just a little longer?"

        menu:
            n "J-{w=0.1}just a little."

            "Of course.":
                n 1kwmnvf "...{w=0.3}Thanks,{w=0.1} [player]."
                jump scritch_loop

            "That's it for now.":
                n 1kllajl "...Oh."
                n 1fllpol "W-{w=0.1}well, that's fine!{w=0.2} Not like I was super into it or anything dumb like that anyway."
                n 1kllpol "..."
                pass
    else:
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
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "dev/mod_assets/ui/scritch_b.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "dev/mod_assets/ui/scritch_c.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "dev/mod_assets/ui/scritch_d.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "dev/mod_assets/ui/scritch_e.png"
            ease 0.33 alpha 1.0 yoffset -30
    
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

    text "{0} scritches".format(persistent.jn_scritches_total_given) size 30 xpos 555 ypos 60 style "categorized_menu_button"
    
    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440

        textbutton _("Done"):
            style "hkbd_button"
            action [Function(renpy.jump, "scritch_finished")]
