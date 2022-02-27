default persistent._event_database = dict()

init python in jn_events:
    import random
    import store
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity

    EVENT_MAP = dict()

    def select_event():
        """
        Picks and returns a random event, or None if no events are left.
        """
        kwargs = dict()
        event_list = store.Topic.filter_topics(
            EVENT_MAP.values(),
            unlocked=True,
            affinity=jn_affinity.get_affinity_state(),
            is_seen=False,
            **kwargs
        )

        # Events are one-time only, so we sanity check here
        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None

    def display_visuals(natsuki_sprite_code):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
        """
        # Draw background, with Natsuki using the given sprite code
        store.main_background.appear(natsuki_sprite_code)

        if store.persistent.jn_random_weather and 6 < store.jn_get_current_hour() <= 18:
            jn_atmosphere.show_random_sky()

        elif (
            store.jn_get_current_hour() > 6 and store.jn_get_current_hour() <= 18
            and not jn_atmosphere.is_current_weather_sunny()
        ):
            jn_atmosphere.show_sky(jn_atmosphere.WEATHER_SUNNY)

        # UI, music
        renpy.show_screen("hkb_overlay")
        renpy.play(filename="mod_assets/bgm/just_natsuki.ogg", channel="music")

init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
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
    $ renpy.pause(4)
    play audio page_turn

    menu:
        "Enter...":
            pass

    $ jn_events.display_visuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True
    
    n 1uskem "...!"
    n 1uskeml "[player]!{w=0.5}{nw}"
    extend 1fcsan " C-{w=0.1}can you {i}believe{/i} this?"
    n 1fllfu "Parfait Girls got a new editor,{w=0.3}{nw}"
    extend 1fbkwr " and they have no {i}idea{/i} what they're doing!"
    n 1flrwr "I mean,{w=0.1} have you {i}seen{/i} this crap?!"
    n 1fcsan "As {i}if{/i} Minori would ever stoop so low as to-!"
    n 1unmem "...!"
    n 1fllpol "..."
    n 1fcspo "Actually,{w=0.1} you know what?{w=0.2} It's fine."
    n 1fsrss "I didn't wanna spoil it for you anyway."
    n 1flldv "Ehehe..."
    n 1nllpol "I'll just...{w=0.5}{nw}"
    extend 1nlrss " put this away."

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ulraj "So..."
    n 1fchbg "What's new,{w=0.1} [player]?"

    return
