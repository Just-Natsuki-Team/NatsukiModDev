



default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass


    dismiss_keys = config.keymap['dismiss']


label chbeachdate_night_noskip:
    show screen fake_skip_indicator
    n "Uh..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    n "No!"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        n "Now, where was I...?"
        pause 4.0
        call expression "chbeach_night_" + str(persistent.current_monikatopic)
    jump chbeach_night_loop
    return

label chbeachdate_night_main:
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chbeachdate_night_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ n_name = "Natsuki"
    $ delete_all_saves()
    $ beach_night = True
    $ HKBShowButtons()
    scene beach_night
    play music t2
    play music tbeach_night
    show natsuki 1ba at t11
    n "We're here!"
    n "It's weird to be here at night."
    n "But it could be pretty peaceful!"
    $ persistent.autoload = "chbeachdate_night_autoload"
    jump chbeach_night_loop



label chbeachdate_night_autoload:
    play music tbeach_night
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ beach_night = True
    $ HKBShowButtons()
    scene beach_night
    play music tbeach_night
    show natsuki 1ba at t11
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    window auto
    if persistent.monika_reload <= 4:
        call expression "chbeach_night_reload_" + str(persistent.monika_reload)
    else:
        call chbeach_night_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    jump chbeach_night_loop


label chbeach_night_reload_0:
    $ allow_dialogue = True
    return
label chbeach_night_reload_1:
    $ allow_dialogue = True
    return
label chbeach_night_reload_2:
    $ allow_dialogue = True
    return
label chbeach_night_reload_3:
    $ allow_dialogue = True
    return
label chbeach_night_reload_4:
    $ allow_dialogue = True
    return

label chbeach_night_loop:
    python:
        current_time = datetime.datetime.now().time().hour
    show natsuki 1ba at t11
    $ allow_dialogue = True
    $ beach_night = True
    $ HKBShowButtons()
    $ allow_boop = False
    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    if not config.developer or True:
        window hide(config.window_hide_transition)
        if persistent.youtuber_mode:
            $ waittime = renpy.random.randint(1, 5)
        else:
            $ waittime = renpy.random.randint(20, 35)
        $ renpy.pause(waittime)
        window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,12)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False
    if current_time >= 6 and current_time < 19:
        $ persistent.autoload = "chbeachdate_autoload"
        $ persistent.date = "beach"
        jump chbeachdate_autoload

    if persistent.random_talk:
        call expression "chbeach_night_" + str(persistent.current_monikatopic)
    else:
        jump chbeach_night_loop
    jump chbeach_night_loop



label chbeach_night_0:
    n "..."

label chbeach_night_1:
    n 1bk "It's so pretty here..."
    n "And pretty calming too..."
    return

label chbeach_night_2:
    n 1bl "I remember going here with my mom!"
    n "When I was a little girl we always came here."
    n 1bm "With my dad too of course."
    n "I miss the old days..."
    return

label chbeach_night_3:
    n 4bl "When I was a kid I HATED sand."
    n "It's itchy and sticky!"
    n "But now I come to love it!"
    return

label chbeach_night_4:
    n "We should build sandcastles!"
    n "If you select \"Action\" we can build sandcastles!"
    return

label chbeach_night_5:
    n "Never knew coming here at night would be so nice."
    n "Even though it is all just a game."
    n "People always love great scenery in games."
    return

label chbeach_night_6:
    n 1bk "Do you like sand more or water more?"
    menu:
        "Sand!":
            pass
        "Water!":
            pass
    n 1bl "Cool!"
    n "I like both the same."
    n "With sand you can make castles."
    n "But you can swim in water."
    return

label chbeach_night_7:
    n 4bf "Two words..."
    n "Seagulls"
    n "SUCK!"
    n "They always steal food!"
    n "It's so annoying!"
    return

label chbeach_night_8:
    n 1bk "It was a good idea to come here at night!"
    n "I'm glad we did!"
    n "It looks so pretty!"
    return

label chbeach_night_9:
    n 1bk "..."
    n "Oh! Sorry I was just staring at the ocean..."
    return

label chbeach_night_10:
    n 1bk "Monika talked about her experience with the beach."
    n "She said she cam fairly often and never really with anyone."
    n "I would feel bad for her."
    n "But I only feel bad that she is suffering in the game's backup chrs folder!"
    return

label chbeach_night_11:
    n 1bl "I always liked the ambiance of the beach at night."
    n "It's calming and soothing."
    n "Do you ever like to sit and listen to the waves?"
    n "Actually you don't need to answer."
    n "I can guess."
    return

label chbeach_night_12:
    n 1bk "You know how most animes have a beach episode?"
    menu:
        "Yes I do!":
            n "Good."
        "Yes, and I hate it.":
            n "I know right!"
        "...no...":
            n "Get with the times bucko."
    n 4bf "Well, it's always like every time they need to fill episode space they have a beach episode for fan service!"
    n "And of COURSE they make the prettiest character get all the..."
    n "{i}...attention...{/i}"
    n 1bk "I almost wonder how the male characters feel."
    n "Probably uncomfortable..."
    return

label chbeach_night_13:
    n 1bm "I've always wanted to come to the beach for my birthday."
    n "It's in the fall though, so we never could."
    n "But hey!"
    n "My next birthday can be at the beach, since I control the game!"
    return

label chbeach_night_14:
    n 4br "Do you know that annoyingly popular song called 'Baby Shark'?"
    n 1bs "You probably have. Sorry."
    n "I think the song is really annoying."
    n "What in the hell about that song is good?"
    n "Ugh."
    return

label chbeach_night_action:
    n 1bk "Don't know..."
    n "Up to you."
    n "Try the actions button down there!"
    jump chbeach_night_loop

label chbeach_night_oceanaction:
    if beach_night:
        $ allow_dialogue = False
        n 1bl "I love taking walks on the beach at night!"
        n "The waves are so nice!"
        window hide
        pause 5.0
        n "I'm really glad we came here!"
        n "It's much better then that stuffy room!"
        n "I know this is just a game. But I dont care!"
        n "Hehe!"
        jump chbeach_night_loop
    else:
        "Don't act dumb."

label chbeach_night_sandcastleaction:
    if beach_night:
        $ allow_dialogue = False
        $ HKBHideButtons()
        play music t5
        "Natsuki sits on the sand."
        n 1bm "Shoot I don't have a shovel!"
        call updateconsole ("os.write(\"characters/shovel.obj\")", "shovel.obj written.")
        if renpy.loadable("..shovel.obj") == False:
            python:
                try: renpy.file(config.basedir + "../(shovel).obj")
                except: open(config.basedir + "/characters/shovel.obj", "wb").write(renpy.file("shovel.obj").read())
        n 1bz "Ehehe!"
        call hideconsole
        menu:
            "That's cheating!":
                pass
        n 1bl "The game does not have shovel what did you want me to do?!"
        menu:
            "Fair point.":
                pass
        n "Seeee~!"
        pause 3.0
        n "Hey [player] can you go get some water for the sand?"
        menu:
            "Yeah.":
                pass
        n "Thanks!"
        scene beach_night with wipeleft_scene
        "I walk down to the water."
        "Seizing a bucket I head down towards the water."
        "I grab some dry sand and place it into the bucket."
        "After that a dip the bucket into the water."
        "Once I have enough I head back up towards Natsuki."
        scene beach_night
        with wipeleft_scene
        "The bucket is really heavy."
        menu:
            "A little help?":
                pass
        show natsuki 1bw at t11
        n "Ugh... you can't do it yourself?"
        menu:
            "No!":
                pass
        n 1bj "Fine!"
        n "There happy?"
        menu:
            "Thanks.":
                pass
        n 4bl "Heh... you're welcome!"
        "We work together to build the ultimate sand castle!"
        n "You know [player] I don't like to do childish things like this..."
        n "Usually people will judge me."
        n "Maybe I'm only comfortable doing because I know it's not real."
        n "Or maybe you are just that special?"
        n "Even if it's not real..."
        n "I'm enjoying it!"
        n "It's done!"
        menu:
            "It's awesome!":
                n "Sure is!"
                pass
            "Could use some work.":
                n "I like it!"
                pass
        $ HKBShowButtons()
        jump chbeach_night_loop
    else:
        "Lol no."
        jump chbeach_night_loop

label chbeach_night_digaction:
    n 4bl "Okay, let's go!"
    if renpy.loadable("..shovel.obj") == False:
        n 1bk "Wait..."
        n "I don't have a shovel!"
        call updateconsole("os.write\(characters/shovel.obj\)", "shovel.obj written sucessfully")
        python:
            try: renpy.file(config.basedir + "../(shovel).obj")
            except: open(config.basedir + "/characters/shovel.obj", "wb").write(renpy.file("shovel.obj").read())
        n "There!"
    n 1bk "Here's a good place!"
    "We begin digging into the sand."
    if renpy.random.randint(5, 10) == 10:
        n 1bk "Woah!"
        menu:
            "What?":
                pass
        n 1bl "I found a really cool gem!"
        n "I'm hanging on to this!"
    else:
        n 1bg "Ah..."
        n "I didn't find anything."
        n "Rats..."
    scene beach_night
    with wipeleft_scene
    show natsuki 1bl at t11
    n 1bl "Well..."
    n "Either way, that was fun!"
    jump chbeach_night_loop

label chbeach_night_episodes:
    n "Does it?"
    n "I mean... I guess?"
    n "Except it's absolutely NOT fan service!"
    n "100 percent!"
    jump chbeach_night_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
