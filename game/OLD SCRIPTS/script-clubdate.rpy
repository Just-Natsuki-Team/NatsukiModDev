image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"



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


label chclub_noskip:
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
        call expression "chclub_" + str(persistent.current_monikatopic)
    jump chclub_loop
    return


label chclub_main:
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chclub_main"
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
    $ club = True
    $ HKBShowButtons()
    scene club
    play music t5
    show natsuki 1a at t11 zorder 2
    n 1l "I've missed this uniform!"
    n "It's good to be back."
    $ persistent.autoload = "chclub_autoload"
    jump chclub_loop



label chclub_autoload:
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ club = True
    $ HKBShowButtons()
    scene club
    play music t5
    show natsuki 1a at t11 zorder 2
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    play music t5
    window auto
    if persistent.monika_reload <= 4:
        call expression "chclub_reload_" + str(persistent.monika_reload)
    else:
        call chclub_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        n "Now, where was I...?"
        pause 4.0
        call expression "chclub_" + str(persistent.current_monikatopic)
    jump chclub_loop


label chclub_reload_0:
    n "Your back yay!"
    return
label chclub_reload_1:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chclub_reload_2:
    n "Hey [player]!"
    $ allow_dialogue = True
    return
label chclub_reload_3:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chclub_reload_4:
    n "Hi! Welcome back!"
    $ allow_dialogue = True
    return

label chclub_loop:
    show natsuki 1a at t11 zorder 2
    $ allow_dialogue = True
    $ club = True
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
            persistent.monikatopics = range(1,6)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False

    if persistent.random_talk:
        call expression "chclub_" + str(persistent.current_monikatopic)
    else:
        jump chclub_loop
    jump chclub_loop



label chclub_0:
    n "..."

label chclub_1:
    n 1k "Hey [player]?"
    n "Why did you want to come here?"
    menu:
        "I was bored.":
            pass
        "Memories, I guess.":
            pass
    n "Yeah I guess."
    return

label chclub_2:
    n 1k "Did YOU like the club [player]?"
    n "I know the MC didn't really."
    n "{cps=15}Actually.{/cps}" 
    n "I won't make you answer."
    n "Nevermind..."
    return

label chclub_3:
    n 1m "I miss when we read manga."
    n "When we sat by the window."
    n 1a "We can do that again, you know."
    return

label chclub_4:
    n 1s "Hey... about what happend by the closet."
    menu:
        "Ah... Yeah, that...":
            pass
    n "I know it was an accident."
    n 1l "So, don't worry!"
    return

label chclub_5:
    n 1k "Hey [player]?"
    n "Are you in any clubs in your world?"
    menu:
        "Yes!":
            n "Which club?"
            n "Type the name of the club. don't add club after it."
            $ clubinput = renpy.input('',length=30).strip(' \t\n\r')
            $ club = clubinput.lower()
            n "So your in the [club] club?"
            n 1l "Cool!"
        "No...":
            n 1l "You should find one you enjoy!"
            n 5h "D-don't do it for me though!"

label chclub_6:
    n "[player]?"
    n "Who's poems did you (honestly) like the most?"
    n "Be honest!"
    menu:
        "Monika's":
            n 1k "Hers were cool..."
            n "They talked a lot about being lost and found..."
            n 1l "Here, I'll show you one of hers!"
            call showpoem(poem_m1)
            n 1k "That one is about the game I think..."
        "Sayori's":
            n 1k "Hers were very unique..."
            n "They weren't deep or cute."
            n "They were actually quite depressing..."
            n 1l "Let's read on of hers!"
            call showpoem(poem_s1)
            n "I think it's about [player]..."
        "Yours":
            n 1l "Really?"
            n "I guess mine were pretty cute..."
            n "Let's read one!"
            call showpoem(poem_n1)
            n "I already explained the complexity of it..."
            n "So I won't repeat myself."
        "Yuri's":
            n 1k "Hers were very complex."
            n "I never understood them honestly."
            n "Why don't you try to read one?"
            call showpoem(poem_y2)
            n "I think is in reference to her \"habits\"..."
    n 1l "Anyway!"
    return

label chclub_7:
    n 1k "Do you remember when [player] joined the club?"
    n "Well, I mean it happened twice, but still."
    n "I actually don't really remember when it happened while Sayori was around."
    n "Since technically the only time it really happened was when you joined after Sayori was deleted."
    n "Now that I have sentience, I can sort of remember it."
    n "I wish I could remember more..."
    return

label chclub_flashback:
    n 1k "Well..."
    n "My memories of the club were good."
    n "So... Yes, but not bad ones."
    jump chclub_loop

label chclub_poem:
    n "I already told you..."
    n "Not really..."
    n "Do you want to write one?"
    menu:
        "Yeah.":
            n "Well go ahead."
            $ persistent.playthrough = 0
            call poem
            scene club
            play music t5
            show natsuki 1a at t11 zorder 2
            $ persistent.playthrough = 3
            n "Hope that was fun."
        "No.":
            n "Okay."
    jump chclub_loop

label chclub_mangaaction:
    n "Here is a good spot!"
    scene n_cg1_bg
    n "So where were we?"
    show n_cg1_base
    with dissolve_cg
    n "This is confortable."
    n "Ah that's right!"
    "We continue to read for about an hour."
    n "We have been at this for a long time."
    show n_cg1_exp1
    n "Ahahah!"
    n "I love this part."
    hide n_cg1_exp1
    n "But anyway..."
    n "We really should be done reading now."
    scene club
    hide n_cg1_base
    show natsuki 1a at t11 zorder 2
    jump chclub_loop

label chclub_grabaction:
    n "Good idea!"
    scene closet
    with wipeleft_scene
    show natsuki 1l at t11 zorder 2
    "Natsuki walks into the closet and grabs some manga."
    n "What should we grab?"
    menu:
        "My Hero Acadamia":
            pass
        "Lovesick: Yandere Tales":
            pass
    n "Okay!"
    n "That's good!"
    scene club
    with wipeleft_scene
    show natsuki 1a at t11 zorder 2
    jump chclub_loop

label chclub_poemaction:
    n "Get writing!"
    $ config.overlay_screens = []
    hide screen hkb_overlay
    $ persistent.playthrough = 0
    call poem
    n "Ready?"
    call poemresponse_start
    $ persistent.playthrough = 3
    n "That was fun!"
    jump chclub_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
