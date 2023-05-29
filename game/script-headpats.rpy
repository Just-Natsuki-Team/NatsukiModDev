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
    _more_pats_requested = False
    _no_pat_count = 0
    _pats_finished = False
    _is_idle = True

    # Collision detection
    _last_mouse_position = None

    _ACTIVE_PAT_AREA = pygame.Rect(519, 100, 239, 152)

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

# Initial dialogue based on headpat count
label headpats_start:
    $ jn_headpats._pats_finished = False
    $ jn_headpats._more_pats_requested = False

    if persistent._jn_headpats_total_given == 0:
        n 1uskemlesh "H-{w=0.2}huh?!{w=0.75}{nw}"
        extend 1uwdemlsbl " D-{w=0.1}did you just say...?!"
        n 2kbkwrlsbl "[player]!{w=0.5} W-{w=0.2}wait...!"

    elif persistent._jn_headpats_total_given < 10:
        n 1knmemlsbl "T-{w=0.2}this again?!"
        n 2kslunlsbr "[player]..."

    elif persistent._jn_headpats_total_given < 25:
        n 1ksqsllsbr "...Again,{w=0.2} [player]?"
        n 2ksrcalsbl "..."

    elif persistent._jn_headpats_total_given < 50:
        n 1kcspulesisbl "..."
        n 2kslcaf "Fine..."

    elif persistent._jn_headpats_total_given < 250:
        n 2kcscaf "...Fine."

    else:
        n 4nsrssf "...Okay."

    show screen headpats_ui
    jump headpats_loop

# Main headpat loop/logic
label headpats_loop:
    $ current_mouse_position = jn_utils.getMousePosition()
    $ config.mouse = (
        {"default": [("mod_assets/extra/headpats/headpats_active_cursor.png", 24, 24)]} if jn_headpats._ACTIVE_PAT_AREA.collidepoint(current_mouse_position[0], current_mouse_position[1])
        else None
    )

    if (
        jn_headpats._ACTIVE_PAT_AREA.collidepoint(current_mouse_position[0], current_mouse_position[1])
        and jn_headpats._getMousePositionChanged()
    ):
        python:
            global _last_mouse_position
            persistent._jn_headpats_total_given += 1
            jn_headpats._no_pat_count = 0
            jn_headpats._last_mouse_position = current_mouse_position
            jn_headpats._is_idle = False

        play audio headpat
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
                renpy.jump("headpats_milestone_1000_plus")

    else:
        $ jn_headpats._no_pat_count += 1

        # Switch to waiting idle
        if not jn_headpats._is_idle and persistent._jn_headpats_total_given < 10:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting min

        elif not jn_headpats._is_idle and persistent._jn_headpats_total_given < 25:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting low

        elif not jn_headpats._is_idle and persistent._jn_headpats_total_given < 100:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting medium

        elif not jn_headpats._is_idle:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting high

        # Natsuki picks up on no headpats for extended time
        if (jn_headpats._no_pat_count == 12):
            jump headpats_inactive

    $ jnPause(1)
    jump headpats_loop

label headpats_inactive:
    if persistent._jn_headpats_total_given == 0:
        n 2fwmeml "A-{w=0.2}are you teasing me or something?"
        show natsuki 2fcspol

    elif persistent._jn_headpats_total_given <= 10:
        n 2fcspolsbr "...Are you gonna do something or what?{w=0.75}{nw}"
        extend 1kslunl " Jeez..."
        show natsuki 1kslsll

    elif persistent._jn_headpats_total_given <= 25:
        n 1kslpul "...Did..."
        n 4knmpulsbr "...D-{w=0.2}did you change your mind or something already?"
        show natsuki 1knmbolsbr

    elif persistent._jn_headpats_total_given <= 50:
        n 4kwmpulsbr "...D-{w=0.2}did you not feel like it anymore or something?"
        show natsuki 4kwmbolsbr

    else:
        n 3kllbolsbr "...Were you done already,{w=0.2} or...?"
        show natsuki 4kwmbolsbr

    jump headpats_loop

# Dialogue for each headpat milestone

label headpats_milestone_5:
    n 2fcsunlsbl "Nnnnnn..."
    n 1ksrunlsbr "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_10:
    n 4kwmpulsbr "Y-{w=0.2}you're still going?{w=0.5}{nw}"
    extend 2ksrunfsbl " Jeez..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_25:
    n 1kslunl "Uuuuuuu..."
    n 3kcsemlesi "My hair is gonna be {i}so{/i} tangled later..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_50:
    n 1ncsemlesi "..."
    n 4fsqcal "...E-{w=0.2}enjoying yourself,{w=0.2} [player]?"
    n 4ksrcaf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_100:
    n 4ksqtrfsbr "...You really are enjoying this,{w=0.2} huh?"
    n 1kslcaf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_250:
    n 1ksqcal "...Still going strong,{w=0.2} huh [player]?{w=0.75}{nw}"
    extend 4ksrfsl " Heh."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_500:
    n 1ucspul "This...{w=0.75}{nw}"
    extend 1nslsml " isn't actually so bad."
    n 3fcscafsbr "O-{w=0.2}once you get used to it."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_750:
    n 4kcsssfesi "...Haah."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_1000:
    n 1kcssmf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_1000_plus:
    n 1kcsssfeaf "...[player]..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_finished:
    $ config.mouse = None
    $ jn_headpats._pats_finished = True

    # About a 1/3 chance to ask for more headpats, if not already asked
    if (
        persistent._jn_headpats_total_given >= 100
        and random.randint(0,3) == 1
        and not jn_headpats._more_pats_requested
    ):
        n 2kslbol "..."
        n 2kslsll "Uhmm...{w=0.75}{nw}"
        extend 4knmsll " [player]?"
        n 1klrpulsbl "Could you...{w=0.75}{nw}"
        extend 2ksrbolsbl " you know..."
        n 4knmbolsbr "Keep doing that just a little longer?"

        show natsuki 1fcscalesssbr at jn_center
        menu:
            n "J-{w=0.2}just a little."

            "Of course.":
                n 1ksrssf "...{w=0.3}Thanks,{w=0.2} [player]."
                $ jn_headpats._more_pats_requested = True
                $ jn_headpats._pats_finished = False
                $ jn_headpats._is_idle = False
                jump headpats_loop

            "That's it for now.":
                n 2nslbol "...Oh."
                n 2fcsemlsbl "W-{w=0.2}well,{w=0.2} that's fine!{w=0.75}{nw}"
                extend 2fcspolsbl " I wasn't really {i}that{/i} into it anyway."
                n 1kslpol "..."
    else:
        $ finished_start_quip = renpy.substitute(random.choice(jn_headpats._FINISHED_START_QUIPS))
        n 1kwmpul "[finished_start_quip]"
        $ finished_end_quip = renpy.substitute(random.choice(jn_headpats._FINISHED_END_QUIPS))
        n 1kllpul "[finished_end_quip]"
        n 1kcsdvf "..."

    hide screen headpats_ui
    jump ch30_loop

# Animation for the headpat effect fading out
transform snap_popup_fadeout:
    easeout 0.75 alpha 0

# Appears, floats up and fades away above Natsuki's head for each headpat given
image headpats_effect_popup:
    block:
        choice:
            "mod_assets/extra/headpats/headpat_poof_a.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_b.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_c.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_d.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_e.png"
            ease 0.33 alpha 1.0 yoffset -30

    snap_popup_fadeout

# Idle for 0+
image natsuki headpats waiting min:
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

        pause 5
        repeat

# Idle for 10+
image natsuki headpats waiting low:
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

# Idle for 25+
image natsuki headpats waiting medium:
    block:
        choice:
            "natsuki 1nnmbol"
        choice:
            "natsuki 1nslbol"
        choice:
            "natsuki 1nsrbol"
        choice:
            "natsuki 1tnmsll"
        choice:
            "natsuki 1tslsll"
        choice:
            "natsuki 1tslsll"
        choice:
            "natsuki 1tsrsll"
        choice:
            "natsuki 1nslpol"
        choice:
            "natsuki 1nsrpol"
        choice:
            "natsuki 1nsqpol"

        pause 5
        repeat

# Idle for 100+
image natsuki headpats waiting high:
    block:
        choice:
            "natsuki 1ksqcal"
        choice:
            "natsuki 1knmcal"
        choice:
            "natsuki 1kwmbol"
        choice:
            "natsuki 1kslfsl"
        choice:
            "natsuki 1ksrfsl"

        pause 5
        repeat

# Natsuki during headpats sprites
image natsuki headpats active:
    block:
        choice:
            "natsuki 4kcssmf"
        choice:
            "natsuki 1kchcaf"
        choice:
            "natsuki 1fchcaf"
        choice:
            "natsuki 2kslcaf"
        choice:
            "natsuki 2ksrcaf"
        choice:
            "natsuki 1kcscaf"
        choice:
            "natsuki 4kchpuf"

        pause 2
        repeat

screen headpats_ui:
    zorder jn_headpats._PATS_UI_Z_INDEX

    # Pat counter
    text "{0} headpats given".format(persistent._jn_headpats_total_given) size 30 xalign 0.5 ypos 40 text_align 0.5 xysize (None, None) outlines [(3, "#000000aa", 0, 0)] style "categorized_menu_button_text"

    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 450

        textbutton _("Finished"):
            style "hkbd_option"
            action [
                Function(renpy.jump, "headpats_finished"),
                SensitiveIf(not jn_headpats._pats_finished)
            ]
