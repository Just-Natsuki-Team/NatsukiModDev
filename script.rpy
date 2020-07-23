# This is used for top-level game structure.
# Should not include any actual events or scripting; only logic and calling other labels.

label deleteingname:
    $ persistent.playername = ""
    $ renpy.utter_restart()
label deleteingname2:
    $ persistent.playername = ""
    $ renpy.utter_restart()

label changename:
    $ persistent.playername = "Chris"
    jump start_main

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.playername == "Gaster":
        $ persistent.playername = ""
        $ renpy.utter_restart()
    if persistent.playername == "Natsuki":
        $ persistent.playername = ""
        call screen dialog("You can't steal my name dummy!", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Yuri":
        $ persistent.playername = ""
        call screen dialog("P-please don't do that!", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Sayori":
        $ persistent.playername = ""
        call screen dialog("ERROR: Name is causing errors.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Monika":
        $ persistent.playername = ""
        call screen dialog("There can be only one.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Edgar":
        call screen dialog("I'll allow it!", ok_action=Return)
    if persistent.playername == "Zero":
        call screen dialog("Hello Zero.", ok_action=Return)
    if persistent.playername == "Frisk":
        call screen confirm("This name will make your life hell.\nAre you sure?", yes_action=Return, no_action=Jump("deleteingname"))
    if persistent.playername == "Chara":
        call screen dialog("The true name.", ok_action=Return)
    if persistent.playername == "Ralsei":
        call screen dialog("Trying to compete with Sayori for how much people\nfind you cute? Good luck.", ok_action=Return)
    if persistent.playername == "Cute":
        call screen dialog("No you're not.", ok_action=Jump("deleteingname"))
    if persistent.playername == "MC":
        call screen dialog("That's a little unoriginal, isn't it?", ok_action=Return)
    if persistent.playername == "Kris":
        call screen confirm("Wouldn't it be spelled \"Chris\"?", yes_action=Return, no_action=Jump("start_main"))
        $ persistent.playername = "Chris"
        $ renpy.utter_restart()
    if persistent.playername == "AAAAAAAAAAAA":
        call screen dialog("That's a little unoriginal, isn't it?", ok_action=Return)
    if persistent.playername == "E":
        $ persistent.playername = ""
        call screen dialog("That's not funny.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Fuck":
        $ persistent.playername = ""
        call screen dialog("That's quite rude.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Shit":
        $ persistent.playername = ""
        call screen dialog("That's quite rude.", ok_action=MainMenu(confirm=False))
    if persistent.playername == "Bacon":
        call screen confirm("Really, Bacon?", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Are you sure?", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Natsuki is going to call you this for the rest of the game.", yes_action=Return, no_action=Jump("deleteingname"))
        call screen confirm("Are you sure?!", yes_action=Return, no_action=Jump("deleteingname"))
        call screen dialog("...", ok_action=Return)
        call screen dialog("Alright...", ok_action=Return)
        call screen dialog("Good luck...\n\"Bacon\"...", ok_action=Return)
    if persistent.playername == "Jevil":
        call screen dialog("Why Jevil though?", ok_action=Return)
    if persistent.playername == "Link":
        call screen dialog("The Hero of Time reborn?", ok_action=Return)
    if persistent.playername == "Zelda":
        call screen dialog("Who's the princess here?!", ok_action=Return)
    if persistent.playername == "Ganondorf":
        call screen dialog("The Great King of Evil", ok_action=Return)
    if persistent.playername == "Ganon":
        call screen dialog("The Great King of Evil", ok_action=Return)
    if persistent.playername == "Jevil":
        call screen dialog("Why Jevil though?", ok_action=Return)
    if persistent.playthrough == 0:
        #Call example script
        call start_main from _call_start_main

    elif persistent.playthrough == 3:
        $ chapter = 1
        jump ch30_main
    elif persistent.playthrough == 4:
        jump ch40_main
    elif persistent.playthrough == 5:
        jump ch30_autoload
    elif persistent.playthrough == 6:
        jump ch40_main2
    elif persistent.playthrough == 7:
        jump ch40_main5

    ################################################################
    #This commented block is the original act structure of the game#
    ################################################################
    # if persistent.playthrough == 0:
    #     # Intro
    #     $ chapter = 0
    #     call ch0_main
    #
    #     # Poem minigame 1
    #     call poem
    #
    #     # Day 1
    #     $ chapter = 1
    #     call ch1_main
    #     call poemresponse_start
    #     call ch1_end
    #
    #     # Poem minigame 2
    #     call poem
    #
    #     # Day 2
    #     $ chapter = 2
    #     call ch2_main
    #     call poemresponse_start
    #     call ch2_end
    #
    #     # Poem minigame 3
    #     call poem
    #
    #     # Day 3
    #     $ chapter = 3
    #     call ch3_main
    #     call poemresponse_start
    #     call ch3_end
    #
    #     $ chapter = 4
    #     call ch4_main
    #
    #     python:
    #         try: renpy.file(config.basedir + "/hxppy thxughts.png")
    #         except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    #     $ chapter = 5
    #     call ch5_main
    #
    #     call endgame
    #
    #     return
    #
    # elif persistent.playthrough == 1:
    #     $ chapter = 0
    #     call ch10_main
    #     jump playthrough2
    #
    #
    # elif persistent.playthrough == 2:
    #     # Intro
    #     $ chapter = 0
    #     call ch20_main
    #
    #     label playthrough2:
    #
    #         # Poem minigame 1
    #         call poem
    #         python:
    #             try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
    #             except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
    #
    #         # Day 1
    #         $ chapter = 1
    #         call ch21_main
    #         call poemresponse_start
    #         call ch21_end
    #
    #         # Poem minigame 2
    #         call poem(False)
    #         python:
    #             try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
    #             except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
    #
    #         # Day 2
    #         $ chapter = 2
    #         call ch22_main
    #         call poemresponse_start
    #         call ch22_end
    #
    #         # Poem minigame 3
    #         call poem(False)
    #
    #         # Day 3
    #         $ chapter = 3
    #         call ch23_main
    #         if y_appeal >= 3:
    #             call poemresponse_start2
    #         else:
    #             call poemresponse_start
    #
    #         if persistent.demo:
    #             stop music fadeout 2.0
    #             scene black with dissolve_cg
    #             "End of demo"
    #             return
    #
    #         call ch23_end
    #
    #         return
    #
    # elif persistent.playthrough == 3:
    #     jump ch30_main
    #
    # elif persistent.playthrough == 4:
    #
    #     $ chapter = 0
    #     call ch40_main
    #     jump credits
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
