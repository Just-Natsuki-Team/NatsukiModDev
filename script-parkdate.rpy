



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


label chpark_noskip:
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
        call expression "chpark_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"
image park = "mod_assets/park.png"

label chpark_main:
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chpark_main"
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
    $ park = True
    $ HKBShowButtons()
    scene park
    play music t2
    show natsuki 1ba at t11 zorder 2
    n "Here it is!"
    n 1bl "I love parks!"
    $ persistent.autoload = "chpark_autoload"
    jump chpark_loop



label chpark_autoload:
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ park = True
    $ HKBShowButtons()
    $ allow_boop = False
    scene park
    play music t8
    show natsuki 1ba at t11 zorder 2
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    play music t2
    window auto
    if persistent.monika_reload <= 4:
        call expression "chpark_reload_" + str(persistent.monika_reload)
    else:
        call chpark_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        n "Now, where was I...?"
        pause 4.0
        call expression "chpark_" + str(persistent.current_monikatopic)
    jump chpark_loop


label chpark_reload_0:
    n "Your back yay!"
    return
label chpark_reload_1:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chpark_reload_2:
    n "Hey [player]!"
    $ allow_dialogue = True
    return
label chpark_reload_3:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chpark_reload_4:
    n "Hi! Welcome back!"
    $ allow_dialogue = True
    return

label chpark_loop:
    show natsuki 1ba at t11 zorder 2
    $ allow_dialogue = True
    $ park = True
    $ HKBShowButtons()

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
            persistent.monikatopics = range(1,6)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False

    if persistent.random_talk:
        call expression "chpark_" + str(persistent.current_monikatopic)
    else:
        jump chpark_loop
    jump chpark_loop



label chpark_0:
    n "..."

label chpark_1:
    n 1bm "When I went here as a kid my parents never liked it here very much..."
    n "I usually went with friends."
    n "When my Dad started needing my help I stopped going out so much, unless it was really needed."
    return

label chpark_2:
    if seen_park_ask:
        jump chpark_2_repeat
    else:
        pass
    n "Do you like parks [player]?"
    menu:
        "Yeah!":
            n 1bl "Cool!"
        "Meh...":
            n 1ba "Haven't got an opinion?"
        "No.":
            n 1bm "It can be boring sometimes I guess."
    n 1bm "I personally think it's only fun if your with others."
    n 1bl "I like picnics with my friends."
    return

label chpark_2_repeat:
    n 1bl "Do you like pa-"
    n 1bm "Wait I already asked..."
    n "Nevermind..."
    return

label chpark_3:
    n 1bl "Did you know I sang once?"
    n "While here my friends dared me to sing."
    n "And I did it."
    n "Hehe!"
    menu:
        "What did you sing?":
            n "The Pokemon theme!"
            n "Ehehe!"
        "M'kay...":
            n "Ehehe..."
            pass
    return

label chpark_4:
    $ HKBHideButtons()
    $ gtext = glitchtext(96)
    n 1bm "Do you belive in [gtext]{nw}."
    window hide
    $ allow_dialogue = False
    scene black
    $ HKBHideButtons()
    pause 5.0
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    pause 0.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.37
    hide screen tear
    scene park
    stop music
    play music t2
    show natsuki 1bm at t11 zorder 2
    $ HKBShowButtons()
    n "Well I was trying to startle you but it didn't work."
    n "Sorry about that."
    $ allow_dialogue = True
    return

label chpark_5:
    n "You know..."
    n "Are there any parks near you?"
    menu:
        "Yeah.":
            n "Well why not go?"
            n "Come on! Go out a visit the park."
            n "I'll still be here!"
            $ renpy.quit()
        "No.":
            n "Well that sucks."
    return

label chpark_6:
    n 1bk "Do you prefer walking around at the park or just sitting and relaxing."
    n "In my opinion it's better to just sit back and relax."
    n jbl "You get more out of stuff you know."
    n "And it's more time to read manga."

label chpark_location:
    n 1bm "Well I'm not sure."
    n "The game dosen't specify."
    n "I guess it dosent matter so much."
    n "I'd just say someone in Tokyo."
    jump chpark_loop

label chpark_bg:
    n 1bm "I dunno."
    n "It's just a background asset."
    n "Don't look in to it."
    jump chpark_loop

label chpark_fun:
    n 1bl "When me and my family would come here we would usually just have picnics."
    n "My friends and I just played tag."
    n "Did you expect anything more?"
    jump chpark_loop

label chpark_walkaction:
    $ allow_dialogue = False
    n "Okay!"
    "We begin walking down the path."
    "We go over the bridge on the river."
    n 1bl "I love this!"
    n "The birds are so nice to hear."
    n "What do you think?"
    menu:
        "I love it!":
            pass
    n "Awesome!"
    scene park
    with wipeleft_scene
    show natsuki 1bl at t11 zorder 2
    n "That was fun!"
    jump chpark_loop

default persistent.reload_catch = False

label chpark_catchaction:
    $ persistent.playthrough = 2
    $ persistent.anticheat = 0
    "Natsuki runs to far side of the park."
    hide natsuki
    n 1bl "Hang on!"
    call updateconsole ("os.write(\"characters/ball.obj\")", "ball.obj written sucessfully.")
    if renpy.loadable("..ball.obj") == False:
        python:
            try: renpy.file(config.basedir + "../(ball).obj")
            except: open(config.basedir + "/characters/ball.obj", "wb").write(renpy.file("ball.obj").read())
    n "Okay there we go!"
    "Natsuki throws the ball."
    n "Catch!"
    "I reach to catch the ball."
    if persistent.reload_catch:
        menu:
            "Stand and catch it.":
                "I reach my hands out to catch the ball."
                "It lands way too far away from me."
            "Run to catch it.":
                "I run towards the ball."
                "But I trip over something and fall over."
                scene black
                play sound fall
                n "[player]?"
                scene park
                with dissolve_scene
                show natsuki 1bl at t11 zorder 2
                n "Ahaha!"
                n "Get up!"
            "CAREFULLY run to catch it.":
                "Knowing if I don't look where I'm going I'll probably fall I run over to it while looking atthe ground for obstacles."
                "I manage to catch the ball!"
                show natsuki 1bo at t11 zorder 2
                n "Hey you cheated!"
                n "You just reloaded your save file!"
                $ persistent.playthrough = 3
                n "Were done with catch for now!"
                $ persistent.reload_catch = False
                $ persistent.anticheat = renpy.random.randint(100000, 999999)
                $ delete_all_saves()
                $ persistent.natsuki_emotion = "Angry"
                jump chpark_loop
    else:    
        menu:
            "Stand and catch it.":
                "I reach my hands out to catch the ball."
                "It lands way too far away from me."
            "Run to catch it.":
                "I run towards the ball."
                "But I trip over something and fall over."
                scene black
                play sound fall
                n "[player]?"
                scene park
                with dissolve_scene
                show natsuki 1bl at t11 zorder 2
                n "Ahaha!"
                n "Get up!"
    $ persistent.reload_catch = True
    n 1bl "Nice job with \"catching\"! Ehehe!"
    n "Well anyway... That was fun!"
    $ persistent.reload_catch = False
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.playthrough = 3
    $ delete_all_saves()
    jump chpark_loop

label chpark_picnicactions:
    "We sit down and lay a blanket on the grass."
    n 1bl "There we go!"
    n "Let's sit."
    "Natsuki reaches into her basket and grabs a sandwich."
    n "Here you go [player]!"
    menu:
        "Thanks.":
            pass
    n "Don't mention it!"
    "We eat for a pretty long while listening to the birds."
    n "This is really fun!"
    menu:
        "Yeah!":
            pass
    n "I'm all done, you?"
    menu:
        "Yeah!":
            n "Alright!"
        "Not yet.":
            n "Okay, finish up!"
            "I eat for a few more minutes."
            n "Okay, let's go!"
    jump chpark_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
