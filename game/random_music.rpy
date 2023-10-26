default persistent.jn_random_music_enabled = False

init python in jn_random_music:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_custom_music as jn_custom_music
    import store.jn_utils as jn_utils

    def getRandomMusicPlayable():
        """
        Returns whether random music is considered playable, ignoring if any custom music is defined.
        Note that at least two tracks must exist for random music to work properly.

        OUT:
            - True if random music should be playable, otherwise False.
        """
        return (
            store.persistent.jn_custom_music_unlocked
            and store.persistent.jn_random_music_enabled
            and store.Natsuki.isAffectionate(higher=True)
            and store.preferences.get_volume("music") > 0
            and not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY)
        )

label random_music_change:
    if not jn_random_music.getRandomMusicPlayable():
        return

    $ available_custom_music = jn_utils.getAllDirectoryFiles(
        path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
        extension_list=jn_utils.getSupportedMusicFileExtensions()
    )

    if len(available_custom_music) < 2:
        return

    $ track_quip = random.choice([
        "Alright!{w=0.2} About time for a different tune,{w=0.1} I think!",
        "Okaaay!{w=0.2} Time for another song!",
        "I think I'm about done with this song.",
        "'Kay, that's enough of that.",
        "New song time!",
        "That's about enough of that number!",
        "I wanna listen to something else...",
        "Time to change things up!"
    ])
    n 3nchbg "[track_quip]{w=2}{nw}"
    show natsuki 4nchsmeme

    $ jn_custom_music.presentMusicPlayer("playing")
    play audio button_tap_c
    show music_player stopped
    stop music fadeout 2
    $ jnPause(2)

    $ track_followup = random.choice([
        "Now,{w=0.1} let's see...",
        "Now,{w=0.1} what have we got...",
        "Let's see here...",
        "What else have we got...",
        "Aha!{w=0.2} Let's try this one!",
        "Let me see..."
    ])
    n 2fcssm "[track_followup]{w=2}{nw}"
    show natsuki 4fcssm

    $ music_title = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))[0]

    play audio button_tap_c
    show music_player playing

    $ jnPause(2)
    $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=music_title, is_custom=True), channel="music", fadein=2)
    $ jn_custom_music._now_playing = music_title
    $ renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing))
    $ track_complete = random.choice([
        "Done~!",
        "All done!",
        "All good!",
        "There we go!",
        "And...{w=0.3} we're good!",
        "Okie-dokie!{w=0.3} Ehehe."
    ])

    n 2uchbgeme "[track_complete]{w=2}{nw}"
    show natsuki 2fcssm

    $ jn_custom_music.hideMusicPlayer()

    return

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
    extend 3fchbg " Yeah,{w=0.1} I can do that!"
    n 3unmss "I'll change it about every fifteen minutes or so then,{w=0.1} 'kay?"
    n 4uwdaj "Oh!{w=0.5}{nw}"
    extend 1fllbg " I almost forgot {w=0.1}-{w=0.1} let me just check there's actually any music for me to play first."
    n 4ncsbo "..."

    if len(jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_utils.getSupportedMusicFileExtensions()
        )) >= 2:
        # Proceed if we have at least two tracks
        n 1uchgn "Okaaay!{w=0.2} I think I've got enough to work with here!{w=0.5}{nw}"
        extend 4nchsm " Ehehe."
        n 2nsqsm "Don't worry,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fcsbg " I'll pick good ones!"

        $ persistent.jn_random_music_enabled = True

    elif preferences.get_volume("music") == 0:
        # Cancel if the player has music volume set to zero
        n 1nsqem "Uh...{w=0.5} huh."
        n 2tsqca "And how {i}exactly{/i} do you plan to hear it with music turned off?"
        n 2uchbg "Geez...{w=0.3} you're such a dork sometimes,{w=0.1} [player].{w=0.5}{nw}"
        extend 4nchsm " Ehehe."
        n 3fwlsm "Turn it back up,{w=0.1} and then we'll talk.{w=0.2} 'Kay?"

    else:
        # Cancel if the player doesn't have a selection of custom music
        n 1tllaj "Uhmm...{w=0.3} [player]?{w=0.5}{nw}"
        extend 4tnmca " You haven't exactly given me a lot to work with here."
        n 2unmaj "Can you give me at least a couple of tracks?{w=0.5}{nw}"
        extend 2tnmpo " You {i}do{/i} remember how do to that,{w=0.1} right?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 3uchbg "Just add them to the custom music folder,{w=0.1} [chosen_tease]!"

    return

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
    extend 2nsqsf " Are my music choices {i}really{/i} that bad,{w=0.1} [player]?"
    n 4fsrsm "...Ehehe."
    n 1uchbg "I'm just messing with you.{w=0.2} Sure thing!{w=0.5}{nw}"
    extend 2nchsm " I'll just put it back to the regular music."

    $ jn_custom_music.presentMusicPlayer("playing")
    play audio button_tap_c
    show music_player stopped
    stop music fadeout 2
    $ jnPause(2)

    play audio button_tap_c
    show music_player playing
    play music audio.just_natsuki_bgm fadein 2
    $ jnPause(2)

    n 2nwlbg "...And there we go!"

    $ jn_custom_music.hideMusicPlayer()

    $ persistent.jn_random_music_enabled = False
    return
