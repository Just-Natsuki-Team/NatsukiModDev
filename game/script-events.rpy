default persistent._event_database = dict()

image prop poetry_attempt = "mod_assets/props/poetry_attempt.png"
image prop parfait_manga_held = "mod_assets/props/parfait_manga_held.png"
image prop renpy_for_dummies_book_held = "mod_assets/props/renpy_for_dummies_book_held.png"
image prop a_la_mode_manga_held = "mod_assets/props/a_la_mode_manga_held.png"
image prop strawberry_milkshake = "mod_assets/props/strawberry_milkshake.png"
image prop step_by_step_manga_held = "mod_assets/props/step_by_step_manga_held.png"

image prop wintendo_twitch_held free = "mod_assets/props/twitch/held/wintendo_twitch_held_free.png"
image prop wintendo_twitch_held charging = "mod_assets/props/twitch/held/wintendo_twitch_held_charging.png"
image prop wintendo_twitch_playing free:
    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1

    choice:
        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat
image prop wintendo_twitch_playing charging:
    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1

    choice:
        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat

image prop wintendo_twitch_battery_low:
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_a.png"
    pause 1
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_b.png"
    pause 1
    repeat

image prop wintendo_twitch_dead:
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_a.png"
    pause 1
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_b.png"
    pause 1
    repeat

init python in jn_events:
    import random
    import store
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity

    JN_EVENT_PROP_ZORDER = 4

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

        # Events are one-time only, so we sanity check here
        if len(event_list) > 0:
            return random.choice(event_list).label

        else:
            return None

    def display_visuals(natsuki_sprite_code=None):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
        """
        if natsuki_sprite_code:
            renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        
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
    $ jnPause(2, hard=True)
    n "W-{w=0.1}wait...{w=0.3} what?!"
    n "M-{w=0.1}Minori!{w=0.5}{nw}"
    extend " You {i}idiot{/i}!"
    n "I seriously can't believe...!"
    n "Ugh...{w=0.5}{nw}"
    extend " {i}this{/i} is what I had to look forward to?"
    n "Come on...{w=0.5}{nw}"
    extend " give me a break..."

    play audio page_turn
    $ jnPause(5, hard=True)
    play audio page_turn
    $ jnPause(7, hard=True)

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
    $ jnPause(7, hard=True)

    n "..."
    n "Nnnnnn-!"
    n "I just can't {i}focus{/i}!{w=0.5}{nw}"
    extend " Why is this {i}so{/i} hard now?"

    play audio paper_crumple
    $ jnPause(7, hard=True)

    n "Rrrrr...!"
    n "Oh,{w=0.1} {i}forget it!{/i}"

    play audio paper_crumple
    $ jnPause(3, hard=True)
    play audio paper_throw
    $ jnPause(7, hard=True)

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
    $ jnPause(5, hard=True)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with vpunch
        n "I {i}HATE{/i} IT!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ jnPause(5, hard=True)

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
    $ jnPause(7, hard=True)

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

    $ jnPause(5, hard=True)
    n "Uuuuuu...{w=2}{nw}"
    extend " man..."
    $ jnPause(3, hard=True)
    n "It's too {i}early{/i} for thiiis!"
    play audio chair_out_in
    $ jnPause(5, hard=True)
    n "Ugh...{w=1}{nw}"
    extend " I gotta get to bed earlier..."
    $ jnPause(7, hard=True)

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
    $ jnPause(2, hard=True)

    n "Labels...{w=1.5}{nw}"
    extend " labels exist as program points to be called or jumped to,{w=1.5}{nw}"
    extend " either from Ren'Py script,{w=0.3} Python functions,{w=0.3} or from screens."
    n "..."
    $ jnPause(1, hard=True)
    n "...What?"
    $ jnPause(1, hard=True)

    play audio page_turn
    $ jnPause(5, hard=True)
    play audio page_turn
    $ jnPause(2, hard=True)

    n "..."
    n "Labels can be local or global...{w=1.5}{nw}"
    play audio page_turn
    extend " can transfer control to a label using the jump statement..."
    n "..."
    n "I see!{w=1.5}{nw}"
    extend " I see."
    $ jnPause(5, hard=True)

    n "..."
    n "Yep!{w=1.5}{nw}"
    extend " I have no idea what I'm doing!"
    n "Can't believe I thought {i}this{/i} would help me...{w=1.5}{nw}"
    extend " '{i}award winning{/i}',{w=0.1} my butt."
    $ jnPause(7, hard=True)

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
    $ jnPause(5, hard=True)

    n "Oh man...{w=1}{nw}"
    extend " this artwork..."
    n "It's so {i}{cps=\7.5}pretty{/cps}{/i}!"
    n "How the hell do they get so good at this?!"

    $ jnPause(3, hard=True)
    play audio page_turn
    $ jnPause(5, hard=True)

    n "Pffffft-!"
    n "The heck is {i}that{/i}?{w=1}{nw}"
    extend " What were you {i}thinking{/i}?!"
    n "This is {i}exactly{/i} why you leave the outfit design to the pros!"

    $ jnPause(1, hard=True)
    play audio page_turn
    $ jnPause(7, hard=True)

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
    $ jnPause(3, hard=True)

    n "Man...{w=1}{nw}"
    extend " {i}sho good{/i}!"

    play audio straw_sip
    $ jnPause(3, hard=True)

    n "Wow,{w=0.3} I've missed these...{w=1}{nw}"
    extend " why didn't I think of this before?!"

    play audio straw_sip
    $ jnPause(2, hard=True)
    play audio straw_sip
    $ jnPause(7, hard=True)

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
    $ jnPause(2, hard=True)
    n "Jeez..."
    n "Who {i}drew{/i} this?!"
    n "I feel like I'm gonna vomit rainbows or something!"
    $ jnPause(3, hard=True)
    play audio page_turn
    $ jnPause(2, hard=True)
    play audio page_turn
    $ jnPause(1, hard=True)
    n "Man..."
    n "A-{w=0.3}alright,{w=0.1} enough drooling over the art!{w=1.5}{nw}"
    extend " You got this thing for a reason,{w=0.1} Natsuki..."
    n "Step by step..."
    n "Improve my daily confidence,{w=0.3} huh?{w=1.5}{nw}"
    extend " Okaaay..."

    $ jnPause(1, hard=True)
    play audio page_turn
    $ jnPause(5, hard=True)
    play audio page_turn
    $ jnPause(7, hard=True)

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

# Natsuki learns why you should always have a charging cable on hand...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_battery_dead",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_battery_dead:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_a
    n "..."
    n "...Ha!"
    play audio button_tap_b
    n "..."

    play audio button_mashing_b
    pause 3
    play audio button_mashing_a

    n "Oh,{w=0.3} come {i}on{/i}!{w=1.25}{nw}"
    extend " As {i}if{/i} that hit me!"
    play audio button_mashing_c

    pause 2
    play audio button_mashing_b

    n "Nnnng-!"
    n "G-{w=0.1}get OFF me!{w=0.5}{nw}"
    extend " Jeez!"
    play audio button_mashing_a
    n "I HATE these enemies!"
    n "Did they {i}have{/i} to add so many?!"

    pause 3
    play audio button_mashing_b

    n "Get out of my way!{w=0.75}{nw}"
    play audio button_tap_b
    extend " It's right there!{w=0.75}{nw}"
    extend " I'm SO {i}close{/i}!"
    play audio button_tap_a
    n "Come on...{w=1}{nw}"
    play audio button_mashing_c
    extend " {i}come on{/i}...!"

    menu:
        "Enter...":
            pass

    show prop wintendo_twitch_playing free zorder jn_events.JN_EVENT_PROP_ZORDER
    show natsuki gaming at jn_center zorder JN_NATSUKI_ZORDER
    $ jn_events.display_visuals()
    $ jn_globals.force_quit_enabled = True
    pause 3

    n 1fdwanl "Nnnnnn...!"
    play audio button_mashing_a 
    n 1fdwpoless "Uuuuuuu-!"
    n 1fdwfo "..."
    play audio button_mashing_c
    n 1fdwfoesssbl "Mmmmmm...!"

    show prop wintendo_twitch_held free zorder jn_events.JN_EVENT_PROP_ZORDER
    
    n 1uchbsedz "YES!{w=1.25}{nw}"
    extend 1uchgnedz " FINALLY!"
    n 1kcsbgesisbl "Haah..."
    n 1fcsbgemesbr "Stick {i}that{/i} in your pipe and smoke it!"

    show prop wintendo_twitch_battery_low zorder jn_events.JN_EVENT_PROP_ZORDER

    n 1kcsssemesbr "..."
    n 1ksqsmsbl "...{w=0.75}{nw}"
    n 1uskemleshsbl "...!"
    n 1fllbglsbl "A-{w=0.2}ah!"
    extend 1fchbglsbr " H-{w=0.2}hey,{w=0.2} [player]!"
    extend 1tchbglsbr " What's up?"
    n 1kcssssbl "Man..."
    n 1fsldvsbl "Sorry,"
    extend 1fcsgssbl " but you have no {i}IDEA{/i} how long I was trying to beat that stage!"
    n 1fnmpol "Seriously!"
    n 1fcsajl "I mean,{w=1}{nw}" 
    extend 1fsrajlsbl " it's not like I was getting {i}upset{/i} or anything..."
    n 1fcsbglsbr "I'm {i}way{/i} past getting vexed over games,{w=0.2} of all things."
    n 1fslbglsbr "T-{w=0.2}they're just lucky I {i}chose{/i} not to go all out.{w=1}{nw}"
    extend 1fcsajlsbr " That's all.{w=1}{nw}"
    extend 1nchgnl " Ehehe."
    n 1nchsmleme "..."
    n 1tnmbo "Eh?"
    extend 1klrbgesssbl " Oh,{w=0.2} right!{w=0.75}{nw}" 
    extend 1fchbgesssbr " Sorry!{w=0.75}{nw}"
    extend 1flrdvlsbr " I'm almost done anyway."
    n 1ucssslsbr "All I gotta do is save,{w=0.5}{nw}"

    show prop wintendo_twitch_dead zorder jn_events.JN_EVENT_PROP_ZORDER

    extend " and I'll be right-{w=1.25}{nw}"
    n 1udwssl "..."
    n 1ndwbo "..."
    n 1fdwem "...But I..."
    n 1fdwwr "I-{w=0.2}I just...{w=0.5}{nw}"
    extend 1fdwun " charged..."
    n 1fdwanl "..."
    n 1fcsful "..."
    n 1fcsunl "..."

    show black zorder 4 with Dissolve(0.5)
    pause 0.5
    hide prop
    play audio chair_out_in
    pause 5
    hide black with Dissolve(2)

    n 1ndtbo "..."
    n 1nslbo "..."
    n 1ndtca "..."
    n 1fdteml "This stays between us."
    n 1fsqfrlsbl "Got it?"
    n 1nsrpolsbl "..."
    n 1nsrajlsbl "...So.{w=1}{nw}"
    extend 1tsqsllsbl " What's new,{w=0.2} [player]?"

    return

# Natsuki jumps at the player entering the room, right as she's about to win a game... uh oh.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_game_over",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 21",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_game_over:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_b
    n "..."
    n "Ehehe..."
    play audio button_mashing_a
    n "Oh yeah.{w=0.5} Uh huh."
    
    play audio button_mashing_b
    pause 2
    play audio button_mashing_a
    pause 2

    n "Ugh!{w=0.5}{nw}"
    play audio button_mashing_c
    extend " Get up!{w=0.75} Get UP!"
    n "Counter,{w=0.2} you idiot!"

    play audio button_mashing_b
    pause 1

    n "Yeah!{w=0.75} Now THAT's what I'm talking about!"
    play audio button_mashing_c
    n "Three hits!{w=0.5}{nw}"
    extend " Four hits!{w=0.3}{nw}"
    extend " Five hits!"
    n "You're on {i}fire{/i},{w=0.2} Natsuki!"

    play audio button_mashing_b
    pause 3
    play audio button_mashing_a

    n "Oh man,{w=0.2} I'm ACING this!"
    play audio button_tap_b
    n "Yeah!{w=0.75}{nw}"
    play audio button_tap_a
    extend " Yeah! Come on!"
    play audio button_mashing_c
    n "Just a few more hits...!"

    menu:
        "Enter...":
            pass

    show prop wintendo_twitch_playing charging zorder jn_events.JN_EVENT_PROP_ZORDER
    show natsuki gaming at jn_center zorder JN_NATSUKI_ZORDER
    $ jn_events.display_visuals()
    $ jn_globals.force_quit_enabled = True
    pause 1.5

    show prop wintendo_twitch_held charging
    n 1unmemesu "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fnmgs "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1fllemlsbr " H-{w=0.2}how many times do I gotta tell y-{w=0.25}{nw}"
    play audio twitch_die
    n 1nskemlsbr "...{w=0.5}{nw}"
    play audio twitch_you_lose
    n 1fdwemsbl "..."
    n 1fcsansbl "..."
    n 1fcsemsbl "Are.{w=0.75}{nw}"
    extend 1fcsfusbr " You.{w=0.75}{nw}"
    extend 1fbkwrleansbr " KIDDING ME?!"
    $ player_final = jn_utils.getPlayerFinal(repeat_times=2)
    n 1kbkwrlsbr "[player][player_final]!{w=1}{nw}"
    extend 1fllgslsbr " Come on!"
    n 1fcswrlsbr "Y-{w=0.2}you totally threw off my groove!{w=0.75}{nw}"
    extend 1fsqpolsbl " You big jerk!"
    n 1kcsemesisbl "..."
    n 1kdwwr "...And now I gotta do {i}that{/i} all over again?{w=1}{nw}"
    extend 1kcspu " Man..."
    n 1fslsl "..."
    n 1flrtr "I guess I'll just do that later."
    n 1fsqcal "{b}Again{/b}."

    show black zorder 4 with Dissolve(0.5)
    pause 0.5
    hide prop
    play audio chair_out_in
    pause 5
    hide black with Dissolve(2)

    n 1nsrcal "..."
    n 1nnmtrl "Well,{w=0.2} [player]."
    n 1nsqtrl "I hope you're buckled up."
    n 1nsrpol "...'Cause now you owe me {i}twice{/i} as much fun today to make up for that."
    n 1nsqbol "..."
    n 1fsqajl "Well?{w=0.5}{nw}"
    extend 1fcspolesi " Get to it then,{w=0.2} [player]!"
    n 1fsqsml " Ehehe."
    
    return
