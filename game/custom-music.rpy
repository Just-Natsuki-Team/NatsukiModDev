default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

image music_player off = "mod_assets/props/music_player/music_player_off.png"
image music_player playing = "mod_assets/props/music_player/music_player_play.png"
image music_player stopped = "mod_assets/props/music_player/music_player_stop.png"
image music_player paused = "mod_assets/props/music_player/music_player_pause.png"

init python in jn_custom_music:
    import os
    import store
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    # Tracks must be placed here for Natsuki to find them
    CUSTOM_MUSIC_FOLDER = "custom_music/"
    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, CUSTOM_MUSIC_FOLDER).replace("\\", "/")

    # The file extensions we (Ren'Py) support
    _VALID_FILE_EXTENSIONS = ["mp3", "ogg", "wav"]

    # Variety in dialogue :)
    _CHOOSE_PLAY_MUSIC_QUIPS = [
        "Ooh!{w=0.2} You wanna put something else on?{w=0.2} Okay!",
        "You better play something good,{w=0.1} [player]!{w=0.2} Ahaha.",
        "You wanna play something?{w=0.2} Sure!",
        "Ooh!{w=0.2} Some different music?{w=0.2} Now we're talking!",
        "Eh?{w=0.2} Another track?{w=0.2} Go for it,{w=0.1} [player]!",
        "You wanna play something else?{w=0.2} Go for it!",
        "Ooh,{w=0.1} some different music?{w=0.2} What did you have in mind?"
    ]

    _NATSUKI_PICK_MUSIC_QUESTION_QUIPS = [
        "Oho?{w=0.2} You want me to pick?",
        "Huh?{w=0.2} You want me to choose something?",
        "Hmm?{w=0.2} You want me to pick?",
        "Oh?{w=0.2} You want me to choose something to play?",
        "Mmm?{w=0.2} Is it my turn to pick?"
    ]

    _NATSUKI_PICK_MUSIC_ANSWER_QUIPS = [
        "Ehehe.{w=0.1} Sure!",
        "Sure,{w=0.1} why not!",
        "Can do!",
        "Ehehe.{w=0.2} Leave it to me,{w=0.1} [player]!",
        "I thought you'd never ask,{w=0.1} [player]!",
        "Okie-dokie,{w=0.1} [player]!",
        "Finally!{w=0.2} Ahaha.",
        "Now we're talking!"
    ]

    _NATSUKI_PICK_MUSIC_SEARCH_QUIPS = [
        "Now,{w=0.1} let's see...",
        "Let me take a look...",
        "Alright,{w=0.1} what have we got...",
        "Ooh!{w=0.2} How about this?",
        "Let's see here...",
        "Let's see..."
    ]

    _NATSUKI_PICK_MUSIC_DONE_QUIPS = [
        "Done~!",
        "All done!",
        "All good!",
        "There we go!",
        "And...{w=0.3} we're good!",
        "Okie-dokie!{w=0.3} Ehehe."
    ]

    _NATSUKI_NO_MUSIC_QUIPS = [
        "Just quiet for now?{w=0.2} Sure!",
        "Not in the mood for music,{w=0.1} [player]?{w=0.2} No worries!",
        "Okay!{w=0.2} Let me just turn that off...",
        "Alright!{w=0.2} I'll turn that off for now...",
        "Sure thing!{w=0.2} Let me just get that for you...",
        "No worries!{w=0.2} Just give me a sec...",
    ]

    # Tracks what is currently playing to avoid repetition with random music picks
    _now_playing = None

    def presentMusicPlayer(state="stopped"):
        """
        Shows the music player, in the given state, with some sounds and pauses as appropriate.

        IN:
            - state - str state. Must be an image tag that exists for the player.
        """
        renpy.show(
            name="music_player {0}".format(state),
            at_list=[store.JN_TRANSFORM_FADE_IN],
            zorder=store.JN_PROP_ZORDER
        )
        store.jnPause(0.5)
        renpy.play(filename=store.audio.gift_close, channel="audio")
        store.jnPause(0.5)

    def hideMusicPlayer():
        """
        Hides the music player, with some sounds and pauses as appropriate.
        """
        renpy.show(
            name="music_player",
            at_list=[store.JN_TRANSFORM_FADE_OUT],
            zorder=store.JN_PROP_ZORDER
        )
        store.jnPause(0.5)
        renpy.hide("music_player")
        renpy.play(filename=store.audio.gift_close, channel="audio")
        store.jnPause(0.5)

    def getMusicFileRelativePath(file_name):
        """
        Returns the relative file path for a music file.

        IN:
            - file_name - The name of the music file

        OUT:
            - str relative path of file
        """
        return "../{0}{1}".format(CUSTOM_MUSIC_FOLDER, file_name)

label music_menu:
    $ Natsuki.setInConversation(True)
    $ music_title = "Error, this should have changed"

    # Attempt to get the music in the custom_music directory to present as menu options
    python:
        success = False

        if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):

            # Get the user's music, then sort the options for presentation
            custom_music_options = jn_utils.getAllDirectoryFiles(
                path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
                extension_list=jn_custom_music._VALID_FILE_EXTENSIONS
            )
            custom_music_options.sort()

            # Add random option if we have more than one potential track for Nat to pick
            if len(custom_music_options) > 1:
                custom_music_options.insert(0, ("You pick!", "random"))

            # Add the default music as the first option
            custom_music_options.insert(1, ("Default", "mod_assets/bgm/just_natsuki.ogg"))

            # Add holiday music if unlocked
            if persistent._jn_event_completed_count > 0 and Natsuki.isNormal(higher=True):
                custom_music_options.insert(2, ("Vacation!", "mod_assets/bgm/vacation.ogg"))

            custom_music_options.append(("No music", "no_music"))
            success = True

    # We failed to get the custom music, prompt player to correct
    if not success:
        show natsuki at jn_center
        n 1kllunl "Uhmm..."
        n 4knmunl "Hey...{w=0.3} [player]?"
        n 4klrbgl "Something went wrong when I was trying look for your music..."
        n 1kchbgl "Can you do me a favour and just check everything out real quick?"
        $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
        n 2knmbgl "If you forgot -{w=0.1} anything you want me to play needs to be in the custom_music folder."
        n 2uwdaj "Oh!{w=0.2} Right!{w=0.2} And it also needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format -{w=0.1} just look for the letters after the period in the file name!"
        jump ch30_loop

    elif preferences.get_volume("music") == 0:
        show natsuki at jn_center
        n 1tsqaj "Uh...{w=0.5}{nw}"
        extend 1tslaj " huh."
        n 2tsgsg "And {i}how{/i} exactly do you plan to hear any music with the volume at zero?"
        n 2fchbg "Jeez, [player].{w=0.5}{nw}" 
        extend 1uchgn " How do you even get dressed in the morning with memory like that?!"
        n 3ullss "Well, whatever.{w=0.5}{nw}"
        extend 3unmaj " So..."

        show natsuki 3unmboeqm
        menu:
            n "Did you want me to turn the music back up so you can pick something?"

            "Yes.":
                n 1nchsm "Okey-{w=0.1}dokey!{w=0.2} Just a second..."
                $ preferences.set_volume("music", 0.75)
                n 2fcsbg "And there we are!"
                n 2ullss "So...{w=0.5}{nw}"
                extend 2unmaj " what did you wanna listen to?"

                show natsuki idle at jn_left

            "No.":
                n 3fcsbg "The sound of silence it is,{w=0.1} then!{w=0.5}{nw}"
                extend 3fchsm " Ehehe."

                jump ch30_loop

    else:
        $ chosen_quip = renpy.substitute(random.choice(jn_custom_music._CHOOSE_PLAY_MUSIC_QUIPS))
        n 3unmbgl "[chosen_quip]"
        show natsuki idle at jn_left

    # We have custom music options, present the choices
    call screen scrollable_choice_menu(custom_music_options, ("Nevermind.", False))
    show natsuki idle at jn_center

    if not _return:
        jump ch30_loop

    if _return == "no_music":
        $ chosen_no_music_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_NO_MUSIC_QUIPS))
        n 2knmsm "[chosen_no_music_quip]"

        show natsuki 2fchsm
        $ music_title = "No music"

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        n 2uchsm "There you go, [player]!{w=2}{nw}"
        
        if persistent.jn_random_music_enabled:
            # Stop playing random music, if enabled
            $ persistent.jn_random_music_enabled = False
            n 1unmaj "Oh{w=0.2} -{w=0.50}{nw}" 
            extend 3kchbgsbl " and I'll stop switching around the music too.{w=2}{nw}"

        $ jn_custom_music.hideMusicPlayer()

    elif _return == "random":

        $ available_custom_music = jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_custom_music._VALID_FILE_EXTENSIONS
        )

        # Play a random track
        $ chosen_question_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_QUESTION_QUIPS))
        n 1unmajl "[chosen_question_quip]"

        $ chosen_answer_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_ANSWER_QUIPS))
        n 4uchbgl "[chosen_answer_quip]"
        show natsuki 1fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        $ chosen_search_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_SEARCH_QUIPS))
        n 2ullbgl "[chosen_search_quip]{w=2}{nw}"
        show natsuki 4fcspul

        # If we have more than one track, we can make sure the new chosen track isn't the same as the current one
        if len(available_custom_music) > 1:
            $ music_title_and_file = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))
            $ music_title = music_title_and_file[0]
            play audio button_tap_c
            show music_player playing
            $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(music_title), channel="music", fadein=2)
            $ jnPause(2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 1uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 1fcssm

        $ jn_custom_music.hideMusicPlayer()

    elif _return is not None:
        $ music_title = store.jn_utils.escapeRenpySubstitutionString(_return.split('/')[-1])

        n 2fwlbg "You got it!{w=2}{nw}"
        show natsuki 4fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        play audio button_tap_c
        show music_player playing
        $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(music_title), channel="music", fadein=2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 2uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 2fcssm

        $ jn_custom_music.hideMusicPlayer()

    # Pop a cheeky notify with the Nat for visual confirmation :)
    $ jn_custom_music._now_playing = music_title
    $ renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop
