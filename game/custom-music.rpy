default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

image music_player off = "mod_assets/props/music_player/music_player_off.png"
image music_player playing = "mod_assets/props/music_player/music_player_play.png"
image music_player stopped = "mod_assets/props/music_player/music_player_stop.png"
image music_player paused = "mod_assets/props/music_player/music_player_pause.png"

init python in jn_custom_music:
    from Enum import Enum
    import os
    import store
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    class JNMusicOptionTypes(Enum):
        """
        Identifiers for different music option responses.
        """
        bgm = 1
        custom = 2
        random = 3
        no_music = 4
        location = 5

    class JNCustomMusicSelectionOption:
        """
        Represents a custom music option from the custom music menu.
        """
        def __init__(
            self,
            display_prompt,
            option_type,
            file_name
        ):
            """
            Initialises a new instance of JNCustomMusicSelectionOption.

            - display_prompt: The text to display for this option on the list, as well as when playing the track.
            - option_type: The type of the option.
            - file_name: The file name/path of the music associated with this option.
            """
            self.display_prompt = display_prompt
            self.option_type = option_type
            self.file_name = file_name

    # Tracks must be placed here for Natsuki to find them
    CUSTOM_MUSIC_FOLDER = "custom_music/"
    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, CUSTOM_MUSIC_FOLDER).replace("\\", "/")

    _NATSUKI_PICK_MUSIC_DONE_QUIPS = [
        "Done~!",
        "All done!",
        "All good!",
        "There we go!",
        "And...{w=0.3} we're good!",
        "Okie-dokie!{w=0.2} Ehehe."
    ]

    # Tracks what is currently playing to avoid repetition with random music picks
    _now_playing = None
    _last_music_option = None

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

    def getMusicFileRelativePath(file_name, is_custom):
        """
        Returns the relative file path for a music file.
        We do this as renpy.play()'s native path handling isn't great for Linux/Mac.

        IN:
            - file_name - The name of the music file
            - is_custom - Whether the track is custom music or not. If True, then read from the custom music folder. Otherwise, read from the BGM folder.

        OUT:
            - str relative path of file
        """
        return "../{0}{1}".format(CUSTOM_MUSIC_FOLDER, file_name) if is_custom else "../{0}{1}".format("game/mod_assets/bgm/", file_name)

    if store.persistent.jn_custom_music_unlocked:
        jn_utils.createDirectoryIfNotExists(CUSTOM_MUSIC_DIRECTORY)

label music_menu:
    $ Natsuki.setInConversation(True)
    $ music_title = "Unknown track"

    # Attempt to get the music in the custom_music directory to present as menu options
    python:
        success = False

        if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):
            
            # Get the user's music, then sort the options for presentation
            custom_music_options = [jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt=music_file[0].split(".")[0],
                option_type=jn_custom_music.JNMusicOptionTypes.custom,
                file_name=music_file[0]
            ) for music_file in jn_utils.getAllDirectoryFiles(
                path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
                extension_list=jn_utils.getSupportedMusicFileExtensions()            
            )]
            custom_music_options.sort()

            # Add random option if we have more than one potential track for Nat to pick
            if len(custom_music_options) > 1:
                custom_music_options.insert(0, jn_custom_music.JNCustomMusicSelectionOption(
                    display_prompt="You pick!",
                    option_type=jn_custom_music.JNMusicOptionTypes.random,
                    file_name=None
                ))

            # Add the clubroom daytime music
            custom_music_options.insert(1, jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Strawberry daydream",
                option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                file_name="strawberry_daydream.ogg"
            ))

            # Add the clubroom nighttime music
            custom_music_options.insert(2, jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Stars that shimmer",
                option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                file_name="stars_that_shimmer.ogg"
            ))

            # Add the classic music
            custom_music_options.insert(3, jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Just Natsuki",
                option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                file_name="just_natsuki.ogg"
            ))

            # Add the space classroom (Act 3) music
            custom_music_options.insert(4, jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Space classroom",
                option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                file_name="space_classroom.ogg"
            ))

            # Add holiday music if unlocked
            if persistent._jn_event_completed_count > 0 and Natsuki.isNormal(higher=True):
                custom_music_options.insert(4, jn_custom_music.JNCustomMusicSelectionOption(
                    display_prompt="Vacation!",
                    option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                    file_name="vacation.ogg"
                ))

            custom_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Default",
                option_type=jn_custom_music.JNMusicOptionTypes.location,
                file_name=None
            ))
            custom_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="No music",
                option_type=jn_custom_music.JNMusicOptionTypes.no_music,
                file_name=None
            ))

            success = True

    # We failed to get the custom music, prompt player to correct
    if not success:
        show natsuki at jn_center
        
        n 4kllsssbr "Uhmm..."
        n 4klrflsbr "Hey...{w=0.75}{nw}" 
        extend 4knmajsbr " [player]?"
        n 4kslslsbr "Something {i}kinda{/i} went wrong when I was trying look for your music...{w=1}{nw}"
        extend 4kslsssbr " can you just check everything out real quick?"
        n 2tlraj "As a reminder -{w=0.5}{nw}" 
        extend 2tnmsl " anything you want me to play needs to be in the {i}custom_music{/i} folder."
        n 2fcsbgsbl "Just make sure it's all in {i}.mp3,{w=0.1} .ogg or .wav{/i} format!"

        $ Natsuki.resetLastTopicCall()
        $ Natsuki.resetLastIdleCall()
        jump ch30_loop

    elif preferences.get_volume("music") == 0:
        show natsuki at jn_center
        n 1tsqaj "Uh...{w=1}{nw}"
        extend 1tslaj " huh."
        n 2tsgsg "And {i}how{/i} exactly do you plan to hear any music with the volume at zero?"
        n 2fchbg "Jeez,{w=0.2} [player].{w=0.75}{nw}" 
        extend 1uchgn " How do you even get dressed in the morning with memory like that?!"
        n 3ullss "Well,{w=0.2} whatever.{w=0.75}{nw}"
        extend 3unmaj " So..."

        show natsuki option_wait_curious
        menu:
            n "Did you want me to turn the music back up so you can pick something?"

            "Yes.":
                n 1nchsm "Okey-{w=0.1}dokey!{w=0.2} Just a second..."
                $ preferences.set_volume("music", 0.75)
                n 2fcsbg "And there we are!"
                n 2ullss "So...{w=0.5}{nw}"
                extend 2unmaj " what did you wanna listen to?"

                show natsuki option_wait_excited at jn_left

            "No.":
                n 3fcsbg "The sound of silence it is,{w=0.1} then!{w=0.5}{nw}"
                extend 3fchsm " Ehehe."

                $ Natsuki.resetLastTopicCall()
                $ Natsuki.resetLastIdleCall()
                jump ch30_loop

    else:
        $ chosen_quip = renpy.substitute(random.choice([
            "You wanna put something else on?{w=0.2} You got it!",
            "You better play something good,{w=0.2} [player]!",
            "You wanna play something?{w=0.2} Sure!",
            "Some different music?{w=0.2} {i}Now{/i} we're talking!",
            "Another track?{w=0.2} Sure thing!",
            "You wanna play something else?{w=0.2} Go for it!",
            "Huh?{w=0.2} What did you have in mind,{w=0.2} [player]?"
        ]))
        n 3unmbgl "[chosen_quip]"
        show natsuki option_wait_excited at jn_left

    # We have custom music options, present the choices
    call screen custom_music_menu(custom_music_options)
    show natsuki at jn_center

    if not _return:
        $ Natsuki.resetLastTopicCall()
        $ Natsuki.resetLastIdleCall()
        jump ch30_loop

    if _return.option_type == jn_custom_music.JNMusicOptionTypes.no_music:
        $ music_quip = renpy.substitute(random.choice([
            "Just quiet for now,{w=0.2} huh?",
            "Not in the mood,{w=0.2} [player]?{w=0.2} No worries!",
            "'Kay!{w=0.2} I'll just turn that off...",
            "Alright!{w=0.2} Let me get that for you real quick...",
            "Sure thing!{w=0.2} Let me just get that for you...",
            "No worries!{w=0.2} Just give me a sec...",
        ]))
        n 2knmsm "[music_quip]"

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

    elif _return.option_type == jn_custom_music.JNMusicOptionTypes.random:

        $ available_custom_music = jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_utils.getSupportedMusicFileExtensions()
        )

        # Play a random track
        $ chosen_question_quip = renpy.substitute(random.choice([
            "Oho?{w=0.2} You want me to pick?",
            "Huh?{w=0.2} You want me to choose something?",
            "Hmm?{w=0.2} You want me to pick?",
            "Oh?{w=0.2} You want me to choose something to play?",
            "Eh?{w=0.2} Is it my turn to pick?"
        ]))
        n 1unmajl "[chosen_question_quip]"

        $ chosen_answer_quip = renpy.substitute(random.choice([
            "Sure!",
            "Sure,{w=0.2} why not!",
            "Can do!",
            "Heh.{w=0.2} Leave it to me,{w=0.2} [player]!",
            "Ehehe.{w=0.2} About time too,{w=0.2} [player]!",
            "Okie-dokie,{w=0.2} [player]!",
            "Finally!{w=0.2} Ahaha.",
            "{i}Now{/i} we're talking!"
        ]))
        n 4uchbgl "[chosen_answer_quip]"
        show natsuki 1fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        $ chosen_search_quip = renpy.substitute(random.choice([
            "Now,{w=0.2} let's see...",
            "Let me take a look...",
            "Alright,{w=0.2} what have we got...",
            "Oh!{w=0.2} How about this?",
            "Let's see here...",
            "Let's see..."
        ]))
        n 2ullbgl "[chosen_search_quip]{w=2}{nw}"
        show natsuki 4fcspul

        # If we have more than one track, we can make sure the new chosen track isn't the same as the current one
        if len(available_custom_music) > 1:
            $ music_title = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))[0]
            play audio button_tap_c
            show music_player playing
            $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=music_title, is_custom=True), channel="music", fadein=2)
            $ jnPause(2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 1uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 1fcssm

        $ jn_custom_music.hideMusicPlayer()
        $ jn_custom_music._now_playing = music_title
        $ renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing.split(".")[0]))

    elif _return.option_type == jn_custom_music.JNMusicOptionTypes.location:
        $ music_quip = renpy.substitute(random.choice([
            "Whatever works,{w=0.2} huh?",
            "You got it!",
            "Well,{w=0.2} you're the boss!",
            "Just the usual,{w=0.2} huh?{w=0.2} Sure thing!",
            "Sure thing!{w=0.2} Just give me a sec...",
        ]))
        n 2knmsm "[music_quip]"

        show natsuki 2fchsm

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        play audio button_tap_c
        show music_player playing
        $ renpy.play(
            filename=jn_custom_music.getMusicFileRelativePath(
                file_name=main_background.location.getCurrentTheme(),
                is_custom=False),
            channel="music",
            fadein=2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 2uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 2fcssm

        $ jn_custom_music.hideMusicPlayer()

    elif _return is not None:
        n 2fwlbg "You got it!{w=2}{nw}"
        show natsuki 4fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        play audio button_tap_c
        show music_player playing
        $ renpy.play(
            filename=jn_custom_music.getMusicFileRelativePath(
                file_name=_return.file_name,
                is_custom=_return.option_type == jn_custom_music.JNMusicOptionTypes.custom),
            channel="music",
            fadein=2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 2uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 2fcssm

        $ jn_custom_music.hideMusicPlayer()
        $ jn_custom_music._now_playing = _return.display_prompt
        $ renpy.notify("Now playing: {0}".format(_return.display_prompt))

    $ jn_custom_music._last_music_option = _return.display_prompt
    $ Natsuki.resetLastTopicCall()
    $ Natsuki.resetLastIdleCall()
    
    jump ch30_loop

screen custom_music_menu(items):
    $ option_width = 400
    if persistent._jn_display_option_icons:
        add "mod_assets/icons/custom_music.png" anchor(0, 0) pos(1280 - (275 + option_width), 20)
    
    elif not persistent._jn_display_option_icons:
        $ option_width += 175

    fixed:
        area (1280 - (40 + option_width), 40, option_width, 440)
        vbox:
            ypos 0
            yanchor 0

            textbutton "Nevermind":
                style "categorized_menu_button"
                xsize option_width
                action Return(False)
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            null height 20

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    for _value in items:
                        textbutton _value.display_prompt:
                            style "categorized_menu_button"
                            xsize option_width
                            action Return(_value)
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                            if _value.option_type == jn_custom_music.JNMusicOptionTypes.bgm:
                                idle_background Frame("mod_assets/buttons/choice_hover_blank_note.png", gui.frame_hover_borders, tile=gui.frame_tile)

                            elif _value.option_type == jn_custom_music.JNMusicOptionTypes.custom:
                                idle_background Frame("mod_assets/buttons/choice_hover_blank_folder.png", gui.frame_hover_borders, tile=gui.frame_tile)

                        null height 5

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align