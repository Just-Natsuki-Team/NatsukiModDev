default persistent._jn_headpats_total_given = 0

init python in jn_headpats:
    import os
    import pygame
    import random
    import store
    import store.jn_utils as jn_utils
    import store.jn_plugins as jn_plugins

    _PATS_UI_Z_INDEX = 4
    _PATS_POPUP_Z_INDEX = 5

    _FINISHED_START_QUIPS = [
        "...Satisfied?",
        "Happy now,{w=0.2} [player]?",
        "...Y-{w=0.3}you're done now?",
        "A-{w=0.2}all done,{w=0.2} [player]?",
        "I-{w=0.2}is that all,{w=0.2} [player]?"
    ]

    _FINISHED_END_QUIPS = [
        "...Good.",
        "...A-{w=0.2}about time.",
        "Finally...{w=0.5} jeez...",
        "T-{w=0.2}took you long enough.",
        "Finally..."
    ]

    # Tracking
    _has_been_given_pats = False
    _more_pats_requested = False
    _no_pat_count = 0
    _pats_finished = False

    # Collision detection
    _last_mouse_position = None

    _ACTIVE_PAT_AREA = pygame.Rect(457, 105, 353, 163)

    def _getMousePositionChanged():
        """
        Returns whether the current mouse position has changed compared to the last mouse position given as stored under _last_mouse_position.
        """
        if _last_mouse_position is None or _last_mouse_position != jn_utils.getMousePosition():
            return True

        return False

    jn_plugins.registerExtrasOption(
        option_name="Headpats",
        visible_if="store.Natsuki.isLove(higher=True)",
        jump_label="headpats_start"
    )

# Initial dialogue based on scritch count
label headpats_start:
    $ jn_headpats._more_pats_requested = False

    if persistent._jn_headpats_total_given == 0:
        n 1kwdajl "H-{w=0.2}huh?!"
        extend " D-{w=0.1}did you just say...?!"
        n 1kbkeml "[player]!{w=0.5} W-{w=0.2}wait...!"

    elif persistent._jn_headpats_total_given < 10:
        n "T-{w=0.2}this again?!"
        n "[player]..."
        extend " c-{w=0.2}come on..."

    elif persistent._jn_headpats_total_given < 25:
        n "...Again,{w=0.2} [player]?"
        n 1kllajl "Uuuuuuu..."
        n 1kllunl "...Fine." 

    elif persistent._jn_headpats_total_given < 50:
        n 1kwmpul "..." #sigh
        n 1kllssl "Fine..."

    elif persistent._jn_headpats_total_given < 250:
        n 1kllssl "...Fine."

    else:
        n 1kcsssl "...Okay."
    
    show screen headpats_ui
    jump headpats_loop

# Main scritch loop/logic
label headpats_loop:
    $ current_mouse_position = jn_utils.getMousePosition()

    if not jn_headpats._has_been_given_pats:
        if persistent._jn_headpats_total_given < 5:
            show natsuki headpats nervous

        else:
            show natsuki headpats waiting
            
        $ jnPause(1)

    if (jn_headpats._ACTIVE_PAT_AREA.collidepoint(current_mouse_position[0], current_mouse_position[1])
        and jn_headpats._getMousePositionChanged()):

        python:
            global _last_mouse_position
            jn_headpats._has_been_given_pats = True
            persistent._jn_headpats_total_given += 1
            jn_headpats._no_pat_count = 0
            jn_headpats._last_mouse_position = current_mouse_position

        play audio scritch
        show headpats_effect_popup zorder jn_headpats._PATS_POPUP_Z_INDEX
        show natsuki headpats active
        $ jnPause(0.75)
        hide headpats_effect_popup

        python:
            milestone_label = "headpats_milestone_{0}".format(str(persistent._jn_headpats_total_given))
            if (renpy.has_label(milestone_label)):
                renpy.jump(milestone_label)

            elif (
                persistent._jn_headpats_total_given > 1000
                and persistent._jn_headpats_total_given % 1000 == 0
            ):
                renpy.jump(headpats_milestone_1000_plus)

    elif jn_headpats._has_been_given_pats:
        show natsuki headpats waiting
        $ jnPause(2)

    else:
        $ jn_headpats._no_pat_count += 1
        $ jnPause(2)

    # Natsuki picks up on no scritches for extended time
    if (jn_headpats._no_pat_count == 5):
        jump scritch_inactive

    jump headpats_loop

label headpats_inactive:
    if persistent._jn_headpats_total_given >= 750:
        n 1kwmunf "..."

    elif persistent._jn_headpats_total_given >= 50:
        n 1kplunf "...{w=0.3}Why aren't you...{w=0.3} you know?"

    elif persistent._jn_headpats_total_given >= 25:
        n 1kwmpofsbr "...{w=0.3}I said you can keep going,{w=0.2} [player]."

    elif persistent._jn_headpats_total_given >= 10:
        n 1fllpofesssbr "...{w=0.3}I didn't say stop,{w=0.2} you know."

    else:
        n 1kllemfesssbr "...{w=0.3}A-{w=0.2}are you going to do something or what?"

    jump headpats_loop
        
# Dialogue for each scritch milestone

label headpats_milestone_5:
    n 1kwmpolsbl "Nnnnnn..."
    n 1kllpofsbr "..."

    jump headpats_loop

label headpats_milestone_10:
    n 1knmpul "Y-{w=0.2}you're still going?!{w=0.5}{nw}"
    extend 1kllpulsbr " Jeez..."

    jump headpats_loop

label headpats_milestone_25:
    n "Uuuuuuu..."
    n "My hair is gonna be {i}so{/i} tangled later..."

    jump headpats_loop

label headpats_milestone_50:
    n "..."
    n 1klrpol "...E-{w=0.2}enjoying yourself,{w=0.2} [player]?"
    n "..."

    jump headpats_loop

label headpats_milestone_100:
    n 1tdtbol "...You really are enjoying this,{w=0.2} huh?"
    n 1tdtajf "I'm...{w=0.5}{nw}" 
    extend 1fllunfsbl " warming up to it."
    n 1kllssfsbl "I think."

    jump headpats_loop
    
label headpats_milestone_250:
    n 1kllsml "..."
    n 1knmnvl "...Well?{w=0.2} Keep going,{w=0.2} [player]..."

    jump headpats_loop
    
label headpats_milestone_500:
    n 1knmnvl "..."
    n 1kcssml "..."

    jump headpats_loop

label headpats_milestone_750:
    n 1kcsssl "...You know..."
    n 1kllssfsbl "This is...{w=0.75} pretty great after all."

    jump headpats_loop

label headpats_milestone_1000:
    n 1kllsml "..."
    n 1kwmssleaf "...More?"

    jump headpats_loop

label headpats_milestone_1000_plus:
    n 1kcssmleaf "...[player]..."

    jump headpats_loop

label headpats_finished:
    $ jn_headpats._pats_finished = True

    # About a 1/3 chance to ask for more scritches, if not already asked
    if (
        persistent._jn_headpats_total_given >= 100
        and random.randint(1,3) == 1
        and not jn_headpats._more_pats_requested
    ):
        n 1kllunf "..."
        n 1knmpuf "Uhmm...{w=0.3} [player]?"
        n 1klrssf "Could you...{w=0.3} you know..."
        n 1klrpof "Keep doing that just a little longer?"

        menu:
            n "J-{w=0.2}just a little."

            "Of course.":
                n 1kwmnvf "...{w=0.3}Thanks,{w=0.2} [player]."
                $ jn_headpats._more_pats_requested = True
                $ jn_headpats._pats_finished = False
                jump headpats_loop

            "That's it for now.":
                n 1kllajl "...Oh."
                n 1fllpol "W-{w=0.2}well, that's fine!{w=0.2} Not like I was super into it or anything dumb like that anyway."
                n 1kllpol "..."
    else:
        $ finished_start_quip = renpy.substitute(random.choice(jn_headpats._FINISHED_START_QUIPS))
        n 1kwmpul "[finished_start_quip]"
        $ finished_end_quip = renpy.substitute(random.choice(jn_headpats._FINISHED_END_QUIPS))
        n 1kllpul "[finished_end_quip]"
        n 1kcsdvf "..."

    hide screen headpats_ui
    jump ch30_loop

# Definitions
define audio.scritch = "mod_assets/sfx/scritch.ogg"

# Animation for the headpat effect fading out
transform snap_popup_fadeout:
    easeout 0.75 alpha 0

# Appears, floats up and fades away above Natsuki's head for each scritch given
image headpats_effect_popup:
    block:
        choice:
            "mod_assets/extra/headpats/scritch_a.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/scritch_b.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/scritch_c.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/scritch_d.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/scritch_e.png"
            ease 0.33 alpha 1.0 yoffset -30

    snap_popup_fadeout

# Pre-scritch Natsuki sprites
image natsuki headpats nervous:
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

# Natsuki waiting for scritch sprites
image natsuki headpats waiting:
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

# Natsuki during scritch sprites
image natsuki headpats active:
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

screen headpats_ui:
    zorder jn_headpats._PATS_UI_Z_INDEX

    # Scritch counter
    text "{0} headpats given".format(persistent._jn_headpats_total_given) size 30 xpos 555 ypos 40 style "categorized_menu_button"
    
    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440

        textbutton _("Finished"):
            style "hkbd_button"
            action [
                Function(renpy.jump, "headpats_finished"),
                SensitiveIf(not jn_headpats._pats_finished)
            ]
