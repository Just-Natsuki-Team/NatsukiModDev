default persistent._event_database = dict()

transform jn_glasses_pre_slide:
    subpixel True
    ypos 0

transform jn_glasses_slide_down:
    subpixel True
    ypos 0
    easeout 5 ypos 20

transform jn_glasses_slide_down_faster:
    subpixel True
    ypos 0
    easeout 3 ypos 20

transform jn_glasses_readjust:
    subpixel True
    ypos 20
    easein 0.75 ypos 0

# Props are displayed on the desk, in front of Natsuki
image prop poetry_attempt = "mod_assets/props/poetry_attempt.png"
image prop parfait_manga_held = "mod_assets/props/parfait_manga_held.png"
image prop renpy_for_dummies_book_held = "mod_assets/props/renpy_for_dummies_book_held.png"
image prop a_la_mode_manga_held = "mod_assets/props/a_la_mode_manga_held.png"
image prop strawberry_milkshake = "mod_assets/props/strawberry_milkshake.png"
image prop step_by_step_manga_held = "mod_assets/props/step_by_step_manga_held.png"
image prop glasses_case = "mod_assets/props/glasses_case.png"

# Overlays are displayed over the top of Natsuki, but behind any props
image overlay slipping_glasses = "mod_assets/overlays/slipping_glasses.png"

init python in jn_events:
    import random
    import store
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity

    JN_EVENT_PROP_ZORDER = 5
    JN_EVENT_OVERLAY_ZORDER = 4

    EVENT_MAP = dict()

    def select_event():
        """
        Picks and returns a random event, or None if no events are left.
        """
        kwargs = dict()
        event_list = store.Topic.filter_topics(
            EVENT_MAP.values(),
            unlocked=True,
            affinity=store.Natsuki._getAffinityState(),
            is_seen=False,
            **kwargs
        )
        return None
        # Events are one-time only, so we sanity check here
        if len(event_list) > 0:
            return random.choice(event_list).label

        else:
            return None

    def display_visuals(natsuki_sprite_code):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
        """
        renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        renpy.pause(0.1)
        renpy.hide("black")
        renpy.show_screen("hkb_overlay")
        renpy.play(filename="mod_assets/bgm/just_natsuki.ogg", channel="music")

        # Reveal
        renpy.hide("black")

# Natsuki is walked in on reading a new volume of Parfait Girls. She isn't impressed.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 2",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_reading_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(2)
    n "W-{w=0.1}wait...{w=0.3} what?!"
    n "M-{w=0.1}Minori!{w=0.5}{nw}"
    extend " You {i}idiot{/i}!"
    n "I seriously can't believe...!"
    n "Ugh...{w=0.5}{nw}"
    extend " {i}this{/i} is what I had to look forward to?"
    n "Come on...{w=0.5}{nw}"
    extend " give me a break..."

    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop parfait_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    n 1uskeml "[player]!{w=0.5}{nw}"
    extend 1fcsan " C-{w=0.1}can you {i}believe{/i} this?"
    n 1fllfu "Parfait Girls got a new editor,{w=0.3}{nw}"
    extend 1fbkwr " and they have no {i}idea{/i} what they're doing!"
    n 1flrwr "I mean,{w=0.1} have you {i}seen{/i} this crap?!{w=0.5}{nw}"
    extend 1fcsfu " Have they even read the series before?!"
    n 1fcsan "As {i}if{/i} Minori would ever stoop so low as to-!"
    n 1unmem "...!"
    n 1fllpol "..."
    n 1fcspo "Actually,{w=0.1} you know what?{w=0.2} It's fine."
    n 1fsrss "I didn't wanna spoil it for you anyway."
    n 1flldv "Ehehe..."
    n 1nllpol "I'll just...{w=0.5}{nw}"
    extend 1nlrss " put this away."

    play audio drawer
    hide prop parfait_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ulraj "So..."
    n 1fchbg "What's new,{w=0.1} [player]?"

    return

# Natsuki is walked in on getting frustrated with her poetry, and gets flustered.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_writing_poetry",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_writing_poetry:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmmm...{w=0.5}{nw}"
    extend " ugh!"

    play audio paper_crumple
    $ renpy.pause(7)

    n "..."
    n "Nnnnnn-!"
    n "I just can't {i}focus{/i}!{w=0.5}{nw}"
    extend " Why is this {i}so{/i} hard now?"

    play audio paper_crumple
    $ renpy.pause(7)

    n "Rrrrr...!"
    n "Oh,{w=0.1} {i}forget it!{/i}"

    play audio paper_crumple
    $ renpy.pause(3)
    play audio paper_throw
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop poetry_attempt zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskuplesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskgsf "[player_initial]-[player]?!{w=0.5}{nw}"
    extend 1fbkwrl " How long have you been there?!"
    n 1fllpol "..."
    n 1uskeml "H-{w=0.1}huh? This?{w=0.5}{nw}"
    extend 1fcswrl " I-{w=0.1}it's nothing!{w=0.5}{nw}"
    extend 1flrpol " Nothing at all!"

    play audio drawer
    hide prop poetry_attempt
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nslpol "..."
    n 1kslss "S-{w=0.1}so...{w=0.5}{nw}"
    extend 1flldv " what's up,{w=0.1} [player]?"

    return

# Natsuki is disillusioned with the relationship, and can't suppress her anger and frustration.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_relationship_doubts",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(None, jn_affinity.DISTRESSED)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_relationship_doubts:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    n "What is even the {i}point{/i} of this..."
    n "Just..."
    n "..."

    if Natsuki.isDistressed(higher=True):
        n "I {w=2}{i}hate{/i}{w=2} this."

    else:
        n "I {w=2}{i}HATE{/i}{w=2} this."

    n "I hate it.{w=1} I hate it.{w=1} I hate it.{w=1} I hate it.{w=1} I {w=2}{i}hate{/i}{w=2} it."
    $ renpy.pause(5)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with vpunch
        n "I {i}HATE{/i} IT!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ renpy.pause(5)

    menu:
        "Enter.":
            pass

    $ jn_events.display_visuals("1fcsupl")
    $ jn_globals.force_quit_enabled = True

    n 1fsqunltsb "..."
    n 1fsqemtsb "...Oh.{w=1}{nw}"
    extend 1fsrsr " {i}You're{/i} here."
    n 1ncsem "{i}Great{/i}..."
    n 1fcsantsa "Yeah, that's {i}just{/i} what I need right now."

    return

# Natsuki tries fiddling with the game, it doesn't go well.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_code_fiddling",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_code_fiddling:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmm..."
    n "Aha!{w=0.5}{nw}"
    extend " I see,{w=0.1} I see."
    n "So,{w=0.3} I think...{w=1}{nw}"
    extend " if I just...{w=1.5}{nw}"
    extend " very...{w=2}{nw}"
    extend " carefully...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n "Ack-!{w=2}{nw}"
    extend " Crap,{w=0.3} that {i}hurt{/i}!"
    n "Ugh..."
    n "How the hell did Monika manage this all the time?"
    extend " This code {i}sucks{/i}!"
    n "..."
    n "..."
    n "But...{w=1} what if I-{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    n "Eek!"
    n "..."
    n "...Yeah,{w=0.3} no.{w=0.5} I think that's enough for now.{w=1}{nw}"
    extend " Yeesh..."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.display_visuals("1fslpo")
    $ jn_globals.force_quit_enabled = True

    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskemlesh "Ack-!"
    n 1fbkwrl "[player_initial]-{w=0.1}[player]!"
    extend 1fcseml " Are you {i}trying{/i} to give me a heart attack or something?"
    n 1fllpol "Jeez..."
    n 1fsrpo "Hello to you too,{w=0.1} dummy..."

    return

# Natsuki isn't quite ready for the day...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_not_ready_yet",
            unlocked=True,
            conditional=(
                "((jn_is_time_block_early_morning() or jn_is_time_block_mid_morning()) and jn_is_weekday())"
                " or (jn_is_time_block_late_morning and not jn_is_weekday())"
            ),
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_not_ready_yet:
    python:
        import random
        jn_globals.force_quit_enabled = False

        # Unlock the starter ahoges
        unlocked_ahoges = [
            jn_outfits.get_wearable("jn_headgear_ahoge_curly"),
            jn_outfits.get_wearable("jn_headgear_ahoge_small"),
            jn_outfits.get_wearable("jn_headgear_ahoge_swoop")
        ]
        for ahoge in unlocked_ahoges:
            ahoge.unlock()

        # Unlock the super-messy hairstyle
        super_messy_hairstyle = jn_outfits.get_wearable("jn_hair_super_messy").unlock()

        # Make note of the loaded outfit, then assign Natsuki a hidden one to show off hair/ahoge
        outfit_to_restore = Natsuki.getOutfitName()
        ahoge_outfit = jn_outfits.get_outfit("jn_ahoge_unlock")
        ahoge_outfit.headgear = random.choice(unlocked_ahoges)
        Natsuki.setOutfit(ahoge_outfit)

    $ renpy.pause(5)
    n "Uuuuuu...{w=2}{nw}"
    extend " man..."
    $ renpy.pause(3)
    n "It's too {i}early{/i} for thiiis!"
    play audio chair_out_in
    $ renpy.pause(5)
    n "Ugh...{w=1}{nw}"
    extend " I gotta get to bed earlier..."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.display_visuals("1uskeml")
    $ jn_globals.force_quit_enabled = True

    n 1uskemlesh "H-{w=0.3}huh?{w=1.5}{nw}"
    extend 1uskwrl " [player]?!{w=1}{nw}"
    extend 1klleml " You're here already?!"
    n 1flrunl "..."
    n 1uskemf "I-{w=0.3}I gotta get ready!"

    play audio clothing_ruffle
    $ Natsuki.setOutfit(jn_outfits.get_outfit(outfit_to_restore))
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    n 1fcsem "Jeez...{w=1.5}{nw}"
    extend 1nslpo  " I really gotta get an alarm clock or something.{w=1}{nw}"
    extend 1nsrss " Heh."
    n 1flldv "So...{w=1}{nw}"
    extend 1fcsbgl " what's up,{w=0.1} [player]?"

    return

# Natsuki is having a hard time understanding Ren'Py (like all of us).
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_renpy_for_dummies",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_renpy_for_dummies:
    $ jn_globals.force_quit_enabled = False

    n "..."

    play audio page_turn
    $ renpy.pause(2)

    n "Labels...{w=1.5}{nw}"
    extend " labels exist as program points to be called or jumped to,{w=1.5}{nw}"
    extend " either from Ren'Py script,{w=0.3} Python functions,{w=0.3} or from screens."
    n "..."
    $ renpy.pause(1)
    n "...What?"
    $ renpy.pause(1)

    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(2)

    n "..."
    n "Labels can be local or global...{w=1.5}{nw}"
    play audio page_turn
    extend " can transfer control to a label using the jump statement..."
    n "..."
    n "I see!{w=1.5}{nw}"
    extend " I see."
    $ renpy.pause(5)

    n "..."
    n "Yep!{w=1.5}{nw}"
    extend " I have no idea what I'm doing!"
    n "Can't believe I thought {i}this{/i} would help me...{w=1.5}{nw}"
    extend " '{i}award winning{/i}',{w=0.1} my butt."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop renpy_for_dummies_book_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1fcspo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "O-{w=0.3}oh!"
    extend 1fllbgl " H-{w=0.3}hey,{w=0.1} [player]!"
    n 1ullss "I was just...{w=1.5}{nw}"
    extend 1nslss " doing...{w=1.5}{nw}"
    n 1fsrun "..."
    n 1fcswr "N-{w=0.1}nevermind that!"
    extend 1fllpo " This book is trash anyway."

    play audio drawer
    hide prop renpy_for_dummies_book_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nllaj "So...{w=1}{nw}"
    extend 1kchbg " what's new,{w=0.1} [player]?"

    return

# Natsuki tries out a new fashion manga.
# Prop courtesy of Almay @ https://twitter.com/art_almay
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_reading_a_la_mode",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_reading_a_la_mode:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(5)

    n "Oh man...{w=1}{nw}"
    extend " this artwork..."
    n "It's so {i}{cps=\7.5}pretty{/cps}{/i}!"
    n "How the hell do they get so good at this?!"

    $ renpy.pause(3)
    play audio page_turn
    $ renpy.pause(5)

    n "Pffffft-!"
    n "The heck is {i}that{/i}?{w=1}{nw}"
    extend " What were you {i}thinking{/i}?!"
    n "This is {i}exactly{/i} why you leave the outfit design to the pros!"

    $ renpy.pause(1)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass
    
    show prop a_la_mode_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1fdwca")
    $ jn_globals.force_quit_enabled = True

    n 1unmgslesu "Oh!{w=1}{nw}"
    extend 1fllbgl " H-{w=0.1}hey,{w=0.1} [player]!"
    n 1nsrss "I was just catching up on some reading time..."
    n 1fspaj "Who'd have guessed slice of life and fashion go so well together?"
    n 1fchbg "I gotta continue this one later!{w=1}{nw}"
    extend 1fchsm " I'm just gonna mark my place real quick,{w=0.1} one sec..."

    play audio drawer
    hide prop a_la_mode_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nchbg "Aaaand we're good to go!{w=1}{nw}"
    extend 1fwlsm " What's new,{w=0.1} [player]?"

    return

# Natsuki treats herself to a strawberry milkshake.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_drinking_strawberry_milkshake",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_drinking_strawberry_milkshake:
    $ jn_globals.force_quit_enabled = False
    n "..."

    play audio straw_sip
    $ renpy.pause(3)

    n "Man...{w=1}{nw}"
    extend " {i}sho good{/i}!"

    play audio straw_sip
    $ renpy.pause(3)

    n "Wow,{w=0.3} I've missed these...{w=1}{nw}"
    extend " why didn't I think of this before?!"

    play audio straw_sip
    $ renpy.pause(2)
    play audio straw_sip
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop strawberry_milkshake zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1nchdr")
    $ jn_globals.force_quit_enabled = True

    n 1nchdr "..."
    play audio straw_sip
    n 1nsqdr "..."
    n 1uskdrlesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fbkwrl "[player_initial]-{w=0.3}[player]!{w=1}{nw}"
    extend 1flleml " I wish you'd stop just {i}appearing{/i} like that..."
    n 1fcseml "Jeez...{w=1}{nw}"
    extend 1fsqpo " you almost made me spill it!"
    n 1flrpo "At least let me finish up here real quick..."

    play audio glass_move
    hide prop strawberry_milkshake
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ncsss "Ah..."
    n 1uchgn "Man,{w=0.1} that hit the spot!"
    n 1fsqbg "And now I'm all refreshed...{w=1}{nw}"
    extend 1tsqsm " what's happening, [player]?{w=1}{nw}"
    extend 1fchsm " Ehehe."

    return

# Natsuki is walked in on reading a manga aimed at/themed around self-help. She *totally* didn't need the self-help, -obviously-.
# Prop courtesy of TheShunBun @ https://twitter.com/TheShunBun
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_step_by_step_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_step_by_step_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(2)
    n "Jeez..."
    n "Who {i}drew{/i} this?!"
    n "I feel like I'm gonna vomit rainbows or something!"
    $ renpy.pause(3)
    play audio page_turn
    $ renpy.pause(2)
    play audio page_turn
    $ renpy.pause(1)
    n "Man..."
    n "A-{w=0.3}alright,{w=0.1} enough drooling over the art!{w=1.5}{nw}"
    extend " You got this thing for a reason,{w=0.1} Natsuki..."
    n "Step by step..."
    n "Improve my daily confidence,{w=0.3} huh?{w=1.5}{nw}"
    extend " Okaaay..."

    $ renpy.pause(1)
    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop step_by_step_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1uskemfesh")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fpawrf "[player_initial]-{w=0.3}[player]!{w=0.2} Again?!{w=1}{nw}"
    extend 1fbkwrf " D-{w=0.3}do you really have to barge in like that {i}every{/i} time?"
    n 1flrunfess "Yeesh...{w=1}{nw}"
    extend 1fsremfess " I swear you're gonna be the death of me one of these days..."
    n 1fslpol "..."
    n 1tsqsll "...Huh?"
    n 1tnmpul "What?{w=0.2} Is something on my face?"
    n 1tllpuleqm "..."
    n 1uskajlesu "O-{w=0.3}oh!{w=0.75}{nw}"
    extend 1fdwbgl " The book!"
    n 1fcsbglsbl "I was just..."
    n 1fllunl "I was..."
    n 1fcsunf "Nnnnnn-!"
    n 1fcswrl "I-{w=0.2}I just like the artwork!{w=1}{nw}"
    extend 1fllemlsbl " That's all it is!"
    n 1fcswrl "I'm {i}super{/i} confident already!"
    n 1fllunlsbl "..."
    n 1fcsemlsbr "A-{w=0.2}and besides,{w=1}{nw}"
    extend 1fllpol " even if I {i}was{/i} reading it for the self-{w=0.1}help stuff..."
    n 1kllsll "..."
    n 1kwmpul "...What'd be wrong with that?"
    n 1fcsbol "It takes real guts to admit to yourself that you can do better.{w=1}{nw}"
    extend 1fnmbol " Can {i}be{/i} better."
    n 1fsrbol "...And only a real jerk would tease someone for trying."
    n 1fcsajl "Never forget that."

    play audio drawer
    hide prop step_by_step_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nllpol "..."
    n 1ulrbol "So..."
    n 1tnmsslsbr "What's new,{w=0.1} [player]?{w=1}{nw}"
    extend 1fllsslsbl " Ahaha..."

    return

# Natsuki finds her glasses in her drawer! They don't fit as well as she remembers...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_eyewear_problems",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 21 and persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_eyewear_problems:
    python:
        import copy
        import random
        
        jn_globals.force_quit_enabled = False

        # Unlock the starter glasses
        unlocked_eyewear = [
            jn_outfits.get_wearable("jn_eyewear_round_glasses_black"),
            jn_outfits.get_wearable("jn_eyewear_round_glasses_red"),
            jn_outfits.get_wearable("jn_eyewear_round_glasses_brown"),
            jn_outfits.get_wearable("jn_eyewear_round_sunglasses"),
            jn_outfits.get_wearable("jn_eyewear_rectangular_glasses_black"),
            jn_outfits.get_wearable("jn_eyewear_rectangular_glasses_red"),
        ]
        for eyewear in unlocked_eyewear:
            eyewear.unlock()

        # Make note of the loaded outfit, then give Natsuki a copy without eyewear so we can show off the new ones!
        outfit_to_restore = Natsuki.getOutfitName()
        eyewear_outfit = copy.copy(jn_outfits.get_outfit(outfit_to_restore))
        eyewear_outfit.eyewear = jn_outfits.get_wearable("jn_none")
        Natsuki.setOutfit(eyewear_outfit)

    n "..."
    play audio drawer
    pause 2 

    n "Oh,{w=0.75}{nw}" 
    extend " come {i}on{/i}!{w=1}{nw}"
    play audio stationary_rustle_c
    extend " I {i}know{/i} I left them here!"
    n "I just know it!"

    pause 3
    play audio drawer
    pause 2.25
    play audio drawer
    pause 1.5
    play audio stationary_rustle_a
    pause 0.5

    n "I just don't get it!{w=1}{nw}"
    extend " It's not like anyone's even {i}here{/i} to mess around with my things any more!"
    n "Ugh...{w=1.25}{nw}"
    extend " I {i}knew{/i} I shouldn't have let Sayori borrow my desk for all the club stuff..."
    n "Reeeeal smooth,{w=0.5} Natsuki..."

    pause 2.5
    play audio paper_crumple
    pause 1

    n "And are these...{w=1} {i}candy wrappers{/i}?!"
    n "That's funny..."
    n "I don't remember ever saying my desk was a{w=0.1}{nw}"
    extend " {b}trash{/b}{w=0.33}{nw}"
    extend " {b}basket!{/b}"

    play audio gift_rustle
    pause 3.5

    n "...Great.{w=0.75} And now my drawer is all sticky."
    n "Gross..."

    play audio paper_crumple
    pause 2.5
    play audio paper_throw
    pause 3

    n "Come on..."

    play audio stationary_rustle_b
    pause 1.5
    play audio stationary_rustle_c
    pause 1.75
    play audio drawer

    n "I can...{w=0.5} just about...{w=0.5} reach the back...!"
    play audio chair_in
    pause 1.5
    n "Nnnnnng-!"

    pause 2
    play audio gift_close
    pause 0.25
    
    n "...!"
    n "T-{w=0.2}they're here?!{w=1}{nw}"
    extend " They're here!"
    n "Man,{w=0.2} that's a relief..."
    n "..."
    play audio glasses_case_open
    n "...I wonder if they still..."
    pause 3.5

    menu:
        "Enter...":
            pass

    show prop glasses_case zorder jn_events.JN_EVENT_PROP_ZORDER
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_pre_slide
    $ jn_events.display_visuals("1fcssmesi")
    $ jn_globals.force_quit_enabled = True

    n 1uskgsesu "...!"
    n 1ullajl "O-{w=0.2}oh!{w=1}{nw}"
    extend 1fllbglsbl " [player]!"
    n 1fcssslsbl "Heh."
    n 1fcsbglsbr "Well,{w=0.5}{nw}" 
    extend 1fsqsglsbr " didn't {i}you{/i} pick a fine time to show up."
    n 1fcssglsbr "..."
    n 1tsqsslsbr "...So,{w=0.3} [player]?{w=1}{nw}"
    extend 1fchgnledzsbr " Notice anything different?"
    n 1tsqsmledz "...Mmm?"
    n 1usqctleme "Oho?{w=1}{nw}"
    extend 1fcsctl " What's that?"
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_slide_down
    n 1tllbgl "Did I do something with my hair?{w=1}{nw}"
    extend 1fcssml " Ehehe."
    n 1nchgnleme "Nope!{w=0.5}{nw}" 
    extend 1fcsbgl " I-{w=0.75}{nw}"
    n 1nsqbol "..."

    show natsuki 1fsqbof at jn_center zorder JN_NATSUKI_ZORDER
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_readjust
    pause 1

    n 1fcspol "..."
    n 1fcsemfsbl "Ahem!"
    n 1fcsbglsbl "N-{w=0.2}nope!{w=0.75}{nw}" 
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_slide_down
    extend 1fchbglsbr " I-{w=0.2}it's not my hair,{w=0.2} [player]!"
    n 1tsqsmlsbr "What else did you-{w=1}{nw}"
    n 1fsranlsbl "..."
    n 1fcsanf "Nnnnn...!"

    show natsuki 1fcsunf at jn_center zorder JN_NATSUKI_ZORDER
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_readjust
    pause 1.15

    n 1fcsemlesi "..."
    n 1fcstrlsbr "So!"
    show overlay slipping_glasses zorder jn_events.JN_EVENT_OVERLAY_ZORDER at jn_glasses_slide_down_faster
    extend 1fsqbglesssbr " What else did you noti-{w=1}{nw}"
    n 1fslanlsbl "Uuuuuuuuu-!"
    
    menu:
        "Natsuki...":
            pass

    n 1fbkwrlesssbl "Alright!{w=0.75}{nw}"
    extend 1flrwrlesssbl" Alright!"
    n 1fcsgslsbr "I know,{w=0.33} okay?!"
    extend 1fsremlsbr " The glasses don't fit properly!"
    n 1fslsrl "They {i}never{/i} have."
    n 1ksrbol "And to think I wasted all that time trying to find them,{w=0.2} too..."
    n 1kcsemlesi "..."

    menu:
        "I think glasses suit you, Natsuki!":
            $ Natsuki.calculatedAffinityGain()
            if Natsuki.isEnamored(higher=True):
                n 1knmsll "..."
                n 1kllpul "...You really think so,{w=0.75}{nw}" 
                extend 1knmpul " [player]?"
                n 1ksrunlsbl "..."
                n 1fcssslsbl "Heh."
                n 1fsldvlsbr "...Then I guess that at least wasn't a {i}total{/i} waste of time."
                n 1fcsajlsbr "Not that I {i}don't{/i} think I look good in them too,{w=0.5}{nw}" 
                extend 1fcssmfsbl " obviously."
            
            elif Natsuki.isAffectionate(higher=True):
                n 1uskemfeshsbl "...!{w=0.5}{nw}"
                n 1fcsgsfsbl "W-{w=0.3}well,{w=0.2} of course they do,{w=0.2} [player]!{w=1}{nw}"
                extend 1flrpolsbl " I {i}did{/i} pick them,{w=0.2} after all."
                n 1ksrsllsbl "..."

            else:
                n 1fcsgslsbl "W-{w=0.2}well,{w=0.5}{nw}"
                extend 1fllgslsbl " duh!"
                n 1fcsbglsbr "Of course they suit me,{w=0.2} [player]!"
                n 1fcsemlsbr "I mean,{w=0.75}{nw}"
                extend 1fllemlsbr " You didn't seriously think I'd pick something that {i}wouldn't{/i} show off my sense of style,{w=0.75}{nw}" 
                extend 1fnmpolsbr " did you?"
                n 1fcsemlsbl "Yeesh..."

        "Yeah, that was a waste of time.":
            $ Natsuki.percentageAffinityLoss(2)
            if Natsuki.isAffectionate(higher=True):
                n 1fskemlesh "H-{w=0.3}hey!{w=1}{nw}"
                extend 1fsqwrl " And listening to you being so rude {i}isn't{/i}?"
                n 1flreml "Yeesh..."
                n 1fsreml "{i}Someone{/i} woke up on the wrong side of the bed..."
                n 1fsrsll "..."

            else:
                n 1fskwrlesh "H-{w=0.2}hey!{w=0.5}{nw}"
                extend 1fnmgsl " What was that for?!"
                n 1fnmwrl "And as if you acting like a jerk {i}isn't{/i}?"
                n 1fsrsllean "..."

        "...":
            n 1fllsll "..."
            n 1knmeml "...What?"
            extend 1fsqemlsbr " The silent act {i}definitely{/i} isn't helping," 
            extend 1fsrpolsbl " you jerk..."

    n 1fcsajl "Well,{w=0.3} whatever.{w=1}{nw}"
    extend 1fllsll " At least I know where they are now,"
    extend 1fslbol " I suppose."
    n 1fcseml "...Wearing them all high up like that was dorky,{w=0.5}{nw}" 
    extend 1fcspol " a-{w=0.2}anyway."

    show black zorder 6 with Dissolve(0.5)
    pause 0.5
    # Hide glasses overlay and restore old outfit
    hide prop
    hide overlay
    $ Natsuki.setOutfit(jn_outfits.get_outfit(outfit_to_restore))
    show natsuki 1fcsbol at jn_center zorder JN_NATSUKI_ZORDER
    play audio glasses_case_close
    pause 0.75
    play audio drawer
    pause 3
    hide black with Dissolve(2)

    n 1nsrcal "..."
    n 1nsrajl "I...{w=0.75}{nw}"
    extend 1nsrsslsbl " guess I should apologize for all of...{w=1.25}{nw}" 
    extend 1nslsllsbl " that."
    n 1nsrpolsbl "Not exactly rolling out the red carpet here,{w=0.2} am I?{w=0.75}{nw}"
    extend 1nslsslsbl " Heh."
    n 1fcsajlsbr "A-{w=0.2}and besides."
    n 1fslsslsbr "I think that's about enough of that{w=0.75}{nw}"
    extend 1fsqbglsbr " {i}spectacle{/i},{w=1}{nw}"
    extend 1nsqbglsbr " huh?"
    n 1nsrsslsbr "So..."
    n 1kchsslesd "W-{w=0.2}what's new,{w=0.2} [player]?"
    
    return
