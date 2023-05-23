## This splash screen is the first thing that Renpy will show the player
##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    #Check for each archive needed
    for archive in ['audio','images','fonts']:  # Exclude scripts.rpa
        if archive not in config.archives:
            #If one is missing, throw an error and close
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

## First, a disclaimer declaring this is a mod is shown, then there is a
## check for the original DDLC assets in the install folder. If those are
## not found, the player is directed to the developer's site to download.
##
init python:
    config.rollback_enabled = False
    menu_trans_time = 1
    #The default splash message, originally shown in Act 1 and Act 4
    splash_message = _("This game is an unofficial fan work, unaffiliated with Team Salvato.")

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

##Here's where you can change the logo file to whatever you want
image menu_logo:
    "mod_assets/jnlogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

#Removed rendering below of other char imgs in main menu

image menu_bg:
    topleft
    "mod_assets/backgrounds/menu/backdrop.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "mod_assets/backgrounds/menu/backdrop.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_nav:
    "mod_assets/backgrounds/menu/background.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset 0 yoffset -160
        repeat

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset 0 yoffset -160
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos_a = "mod_assets/backgrounds/menu/tos_a.png"
image tos_b = "mod_assets/backgrounds/menu/tos_b.png"

label splashscreen:
    #If this is the first time the game has been run, show a disclaimer
    default persistent.has_launched_before = False
    $ persistent.tried_skip = False
    if not persistent.has_launched_before:
        scene white
        $ quick_menu = False
        pause 0.5
        scene tos_a
        with Dissolve(1.0)
        pause 1.0
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: http://ddlc.moe"
        $ narrator(
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within.",
            interact=False
        )
        $ renpy.display_menu(items=[ ("I agree.", True)], screen="choice_centred")
        scene tos_b
        with Dissolve(1)
        pause 1.0

        scene black
        with Dissolve(1)

        ##Optional, load a copy of DDLC save data
        #if not persistent.has_merged:
        #    call import_ddlc_persistent

        $ persistent.has_launched_before = True

    #Check for game updates before loading the game or the splash screen

    # Set the first visited date, if not already on record
    if not persistent.jn_first_visited_date:
        $ persistent.jn_first_visited_date = datetime.datetime.now()

    jump autoload

label after_load:
    $ config.allow_skipping = False
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ style.say_dialogue = style.normal
    return

label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen

        if "_old_history" in globals():
            _history = _old_history
            del _old_history

        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # Prevent the player's menu hotkey from defaulting to Save/Load
    $ store._game_menu_screen  = "preferences"

    # Explicity remove keymaps we dont want
    $ config.keymap["debug_voicing"] = list()
    $ config.keymap["choose_renderer"] = list()

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()

    # Load the appropriate introduction sequence stage, or go straight to ch30 if already completed introduction
    if not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete:
        jump introduction_progress_check

    else:
        jump ch30_autoload

label before_main_menu:
    if persistent.playername != "":
        $ renpy.jump_out_of_context("start")

    # Prevent the player's menu hotkey from defaulting to Save/Load
    $ store._game_menu_screen  = "preferences"

    return

label quit:
    python:
        # Save game data
        jn_utils.save_game()

        # Finally quit
        renpy.quit()
