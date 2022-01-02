default persistent.jn_random_music_enabled = False

init python in jn_random_music:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_custom_music as jn_custom_music
    import store.jn_plugins as jn_plugins
    import store.utils as utils

    _NEW_TRACK_QUIPS = [
        "Alright!{w=0.2} About time for a different tune,{w=0.1} I think!",
        "Okay!{w=0.2} Time for another song!",
        "I think I'm about done with this song.",
        "That's about enough of that track,{w=0.1} I think.",
        "New song time!",
        "That's about enough of that song!",
        "I wanna listen to something else...",
        "Time to change things up!"
    ]

    _NEW_TRACK_FOLLOWUPS = [
        "Now, let's see...",
        "Now, what have we got...",
        "Let's see here..."
        "What else have we got...",
        "Aha!{w=0.2} Let's try this one!",
        "Let me see..."
    ]

    def random_music_change_check():
        """
        Determines if Natsuki should pick a new song to play in the background.
        """

        if (store.persistent.jn_custom_music_unlocked
            and store.persistent.jn_random_music_enabled
            and jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE
            and store.preferences.get_volume("music") > 0
            and len(jn_custom_music._get_all_custom_music()) >= 2):
            
            store.push("random_music_change")
            renpy.jump("call_next_topic")

label random_music_change:
    $ track_quip = random.choice(jn_random_music._NEW_TRACK_QUIPS)
    n 1nchbg "[track_quip]{w=2}{nw}"
    $ track_followup = random.choice(jn_random_music._NEW_TRACK_FOLLOWUPS)
    n 1unmbgl "[track_followup]{w=2}{nw}"
    stop music fadeout 3

    python:
        music_title_and_file = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), jn_custom_music._get_all_custom_music()))
        music_title = music_title_and_file[0]
        renpy.play(filename=music_title_and_file[1], channel="music", fadein=3)
        jn_custom_music._now_playing = music_title
        renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop

# Enable random music
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_enable",
            unlocked=True,
            prompt="Can you play random custom music for me?",
            conditional="persistent.jn_custom_music_unlocked and not persistent.jn_random_music_enabled",
            category=["Music"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_enable:
    n 1unmbg "Ooh!{w=0.5}{nw}"
    extend 1fchbg " Yeah,{w=0.1} I can do that!"
    n 1unmss "I'll change it about every fifteen minutes or so then,{w=0.1} 'kay?"
    n 1uwdaj "Oh!{w=0.5}{nw}"
    extend 1fllbg " I almost forgot {w=0.1}-{w=0.1} let me just check there's actually any music for me to play first."
    n 1ncsbo "..."

    if len(jn_custom_music._get_all_custom_music()) >= 2:
        # Proceed if we have at least two tracks
        n 1uchgn "Okaaay!{w=0.2} I think I've got enough to work with here!{w=0.5}{nw}"
        extend 1nchsm " Ehehe."
        n 1nsqsm "Don't worry,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fcsbg " I'll pick good ones!"
        $ persistent.jn_random_music_enabled = True

    elif preferences.get_volume("music") == 0:
        # Cancel if the player has music volume set to zero
        n 1nsqem "Uh...{w=0.5} huh."
        n 1tsqca "And how {i}exactly{/i} do you plan to hear it with music turned off?"
        n 1uchbg "Geez...{w=0.3} you're such a dork sometimes,{w=0.1} [player].{w=0.5}{nw}"
        extend 1nchsm " Ehehe."
        n 1fwlsm "Turn it back up,{w=0.1} and then we'll talk.{w=0.2} 'Kay?"

    else:
        # Cancel if the player doesn't have a selection of custom music
        n 1tllaj "Uhmm...{w=0.3} [player]?{w=0.5}{nw}"
        extend 1tnmca " You haven't exactly given me a lot to work with here."
        n 1unmaj "Can you give me at least a couple of tracks?{w=0.5}{nw}"
        extend 1tnmpo " You {i}do{/i} remember how do to that,{w=0.1} right?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchbg "Just add them to the custom music folder,{w=0.1} [chosen_tease]!"

    jump ch30_loop

# Disable random music
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_disable",
            unlocked=True,
            prompt="Can you stop playing random custom music?",
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_random_music_enabled",
            category=["Music"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_disable:
    n 1unmaj "Huh?{w=0.2} Wow.{w=0.5}{nw}"
    extend 1nsqsf " Are my music choices {i}really{/i} that bad,{w=0.1} [player]?"
    n 1fsrsm "...Ehehe."
    n 1uchbg "I'm just messing with you.{w=0.2} Sure thing!{w=0.5}{nw}"
    extend 1nchsm " I'll just put it back to the regular music."

    stop music fadeout 3
    play music audio.test_bgm fadein 3

    n 1nwlbg "...And there we go!"

    $ persistent.jn_random_music_enabled = False
    jump ch30_loop
