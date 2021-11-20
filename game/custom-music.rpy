# General tracking; the player unlocks Snap by admitting boredom to Natsuki at least once
default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

init python in jn_custom_music:
    import os
    import store

    # Tracks must be placed here for Natsuki to find them
    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, "custom_music/").replace("\\", "/")

    # The file extensions we (Ren'Py) support
    _VALID_FILE_EXTENSIONS = [".mp3", ".ogg", ".wav"]

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

    # Tracks what is currently playing to avoid repetition with random music picks
    _now_playing = None

    def get_directory_exists():
        """
        Checks to see if the custom_music directory exists, and creates it if not
        Returns True/False based on whether the directory already existed

        OUT:
            - True/False based on if directory was existing (True) or had to be created (False)
        """
        if not os.path.exists(CUSTOM_MUSIC_DIRECTORY):
            os.makedirs(CUSTOM_MUSIC_DIRECTORY)
            return False

        return True

    def _get_all_custom_music():
        """
        Runs through the files in the custom_music directory, identifying supported music files via extension check
        Returns a tuple representing (file_name, file_path_for_renpy_playback)

        OUT:
            - Tuple representing (file_name, file_path_for_renpy_playback)
        """
        global CUSTOM_MUSIC_DIRECTORY
        return_file_items = []

        for file in os.listdir(CUSTOM_MUSIC_DIRECTORY):
            if any(file_extension in file for file_extension in _VALID_FILE_EXTENSIONS):

                # Valid audio track - return displayed prompt and file name
                return_file_items.append((file, os.path.join(CUSTOM_MUSIC_DIRECTORY, file)))

        return return_file_items

label music_menu:

    $ jn_globals.player_is_in_conversation = True

    # Attempt to get the music in the custom_music directory to present as menu options
    python:
        success = False

        if jn_custom_music.get_directory_exists():

            # Get the user's music, then sort the options for presentation
            custom_music_options = jn_custom_music._get_all_custom_music()
            custom_music_options.sort()

            # Add the default music as the first option
            custom_music_options.insert(0, ("Default", "mod_assets/bgm/background_test_music.ogg"))
            custom_music_options.insert(1, ("You pick!", "random"))
            success = True

    # We failed to get the custom music, prompt player to correct
    if not success:
        n "Uhmm..."
        n "Hey...{w=0.3} [player]?"
        n "Something went wrong when I was trying look for your music..."
        n "Can you do me a favour and just check everything out real quick?"
        $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
        n "If you forgot -{w=0.1} anything you want me to play needs to be in the {a=[folder]}custom_music{/a} folder."
        n "Oh!{w=0.2} Right!{w=0.2} And it also needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format -{w=0.1} just look for the letters after the period in the file name!"
        jump ch30_loop

    else:
        $ chosen_quip = renpy.substitute(random.choice(jn_custom_music._CHOOSE_PLAY_MUSIC_QUIPS))
        n "[chosen_quip]"

    # We have custom music options, present the choices
    call screen scrollable_choice_menu(custom_music_options, ("Nevermind.", None))

    if isinstance(_return, unicode):

        if _return == "random":

            $ available_custom_music = jn_custom_music._get_all_custom_music()

            if (len(available_custom_music) > 0):
                # Play a random track
                $ chosen_question_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_QUESTION_QUIPS))
                n "[chosen_question_quip]"

                show placeholder_natsuki smile zorder jn_placeholders.NATSUKI_Z_INDEX
                
                $ chosen_answer_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_ANSWER_QUIPS))
                n "[chosen_answer_quip]"
                
                $ chosen_search_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_SEARCH_QUIPS))
                n "[chosen_search_quip]"

                # If we have more than one track, we can make sure the new chosen track isn't the same as the current one
                python: 
                    if len(available_custom_music) > 1 and jn_custom_music._now_playing is not None:
                        available_custom_music.remove((jn_custom_music._now_playing, os.path.join(jn_custom_music.CUSTOM_MUSIC_DIRECTORY, jn_custom_music._now_playing)))
                        music_title_and_file = random.choice(available_custom_music)

                    else:
                        music_title_and_file = available_custom_music[0]

                    music_title = music_title_and_file[0]
                    renpy.play(filename=music_title_and_file[1], channel="music")

            else:
                # No tracks to choose from
                n "Uhmm...{w=0.3} [player]?"
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n "I've got no music to pick {i}from{/i},{w=0.1} [chosen_tease]!{w=0.2} Jeez..."
                n "Let me know when you've got some music lined up for me,{w=0.1} 'kay?"
                jump ch30_loop

        else:
            # Play the selected specific track
            $ music_title = _return.split('/')[-1]
            $ renpy.play(filename=_return, channel="music")
        
        # Pop a cheeky notify with the Nat for visual confirmation :)
        $ jn_custom_music._now_playing = music_title 
        $ renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop
