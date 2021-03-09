image pool = "mod_assets/locations/pool/pool.png"

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


label chpool_noskip:
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
        call expression "chpool_" + str(persistent.current_monikatopic)
    jump chpool_loop
    return


label chpool_main:
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chpool_main"
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
    $ pool = True
    $ HKBShowButtons()
    scene pool
    play music t2
    call beach_showart
    n "This is it!"
    $ persistent.autoload = "chpool_autoload"
    jump chpool_loop



label chpool_autoload:
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ pool = True
    $ HKBShowButtons()
    $ persistent.sunscreen = False
    scene pool
    play music t2
    call beach_showart
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    window auto
    if persistent.monika_reload <= 4:
        call expression "chpool_reload_" + str(persistent.monika_reload)
    else:
        call chpool_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        n "Now, where was I...?"
        pause 4.0
        call expression "chpool_" + str(persistent.current_monikatopic)
    jump chpool_loop


label chpool_reload_0:
    n "Your back yay!"
    return
label chpool_reload_1:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chpool_reload_2:
    n "Hey [player]!"
    $ allow_dialogue = True
    return
label chpool_reload_3:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chpool_reload_4:
    n "Hi! Welcome back!"
    $ allow_dialogue = True
    return

label chpool_loop:
    call beach_showart
    $ allow_dialogue = True
    $ pool = True
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
            persistent.monikatopics = range(1,10)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False

    if persistent.random_talk:
        call expression "chpool_" + str(persistent.current_monikatopic)
    else:
        jump chpool_loop
    jump chpool_loop



label chpool_0:
    n "..."

label chpool_1:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "Hm, it's kinda weird that this pool is so clean..."
    n "I don't think anyone has been here to clean it..."
    n "Yuck..."
    n "I mean, we are in a game I guess..."
    n "So it can't get dirty."
    return

label chpool_2:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "[player] do you like to swim?"
    menu:
        "Yes":
            n "That's cool!"
        "No":
            n "Aw that's okay!"
    if persistent.natsuki_romance >= 100:
        show natsuki 4en at t11
    else:
        show natsuki 2dn at t11
    n "I miss being able to..."
    return

label chpool_3:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "Have you ever taken a swim class?"
    n "I don't personally understand why they exist..."
    n "Well, unless you want to learn how to swim professionally."
    n "Other then that they don't have much purpose..."
    return
label chpool_4:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "I actually found out recently Yuri's family came here a lot."
    n "I think she may have taken swim lessons..."
    n "Random Yuri fact I guess."
    return

label chpool_5:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "It's such a nice day to swim isn't it!?"
    n "I love sunny days!"
    n "Like this one!"
    return

label chpool_6:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "This place is very fancy eh?"
    n "Those chair and umbrellas and even the pool!"
    n "I feel rich!"
    return

label chpool_7:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "Do you prefer hot or cold?"
    n "Or should I say would you rather it be too hot or too cold?"
    n "I prefer too hot to be honest."
    n "Since you can just use cool air and summer clothes and you're fine."
    menu:
        "I prefer too hot.":
            n "I guess we have the same opinion..."
        "I prefer too cold.":
            n "Ah really?"
    return

label chpool_8:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "Do you or your family go to a country club?"
    n "Of course my dad never had enough money."
    n "I think Yuri's family did."
    n "Monika once siad she went to one when she was a kid."
    n "Sayori said [player]'s parents owned one."
    n "I couldn't tell if she was lying but I don't know now."
    return

label chpool_9:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "Etched did a good job on this art."
    n "It looks like Statchely made it for the game."
    n "But no."
    n "What if Etched IS Statchely?"
    return

label chpool_10:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "I wish I could sit on those chairs..."
    menu:
        "You can...":
            pass
    n "Yeah I know!"
    n "I'm just lazy."
    return

label chpool_11:
    if persistent.natsuki_romance >= 100:
        show natsuki 4er at t11
    else:
        show natsuki 2dr at t11
    n "Insects near pool are always such a problem."
    n "I would never go to any pool where bees were a problem."
    n "It just seems like bad upkeep!"
    return

label chpool_sunscreen:
    if persistent.sunscreen:
        if persistent.natsuki_romance >= 100:
            show natsuki 4es at t11
        else:
            show natsuki 2ds at t11
        n "You already told me too!"
    else:
        if persistent.natsuki_romance >= 100:
            show natsuki 4ek at t11
        else:
            show natsuki 2dk at t11
        n "Oh shoot I almost forgot!"
        "Natsuki grabs a bottle of sunscreen and puts in on."
        n "I realize I could always just make it so the sun can't burn me but whatever!"
        $ persistent.sunscreen = True
    jump chpool_loop

label chpool_cute:
    if persistent.natsuki_romance >= 100:
        show natsuki 1eq at h11
    else:
        show natsuki 1dq at h11
    n "Urk!"
    if persistent.natsuki_love:
        n "Thanks, [player]."
        n "I love you."
    else:
        n "I'm not cute!"
    jump chpool_loop

label chpool_preferance:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "I don't know."
    n "The Pool is usually clean and heated."
    n "The Beach has sand and is either too hot or too cold."
    n "I think I like the equally."
    n "Maybe the Beach has more of an edge though."
    jump chpool_loop


label chpool_swimaction:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ek at t11
    else:
        show natsuki 2dk at t11
    n "You want to swim?"
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "Sure!"
    "Natsuki jumps into the water."
    "We swim around in circles for a while."
    "Natsuki swims past me and does underwater flips."
    menu:
        "You're good at that!":
            pass
    n "Thanks!"
    n "Anyway... I'm ready to get out."
    jump chpool_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
