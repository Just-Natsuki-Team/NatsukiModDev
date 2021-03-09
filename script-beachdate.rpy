default won_water_fight = None
default persistent.seen_bikini = False

image mirage = "mod_assets/locations/beach/mirage.png"
image beach = "mod_assets/locations/beach/beach-day.png"
image beach_night = "mod_assets/locations/beach/beach-night.png"
image beach_eve = "mod_assets/locations/beach/beach-evening.png"
image ocean = "mod_assets/locations/beach/ocean.png"

label beach_showart:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ej at t11 zorder 2
    else:
        show natsuki 1dj at t11 zorder 2
    return

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


label chbeachdate_noskip:
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
        call expression "chbeach_" + str(persistent.current_monikatopic)
    jump chbeach_loop
    return

label chbeachdate_main:
    python:
        today = datetime.date.today()
        day = datetime.date.today().strftime("%A")
        month = datetime.date.today().strftime("%B")
        date = datetime.date.today().strftime("%d")
        year = datetime.date.today().strftime("%Y")
        now = datetime.datetime.now()
        current_time = datetime.datetime.now().time().hour
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chbeachdate_main"
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
    $ beach = True
    $ HKBShowButtons()
    if current_time > 7 and current_time < 18:
        scene beach
    else:
        scene beach_eve
    play music t2
    play music tbeach
    n "H-hang on I'm almost ready!"
    call beach_showart
    if persistent.natsuki_romance >= 100:
        if not persistent.seen_bikini:
            n 1el "Heyyy! [player] do you like my new Bikini?"
            if persistent.natsuki_romance >= 200:
                n "You've been making me feel very comfortable with you recently! So I thought I'd pick out an outfit you'd like!"
                n 2et "I can't see your reaction, but I'm guessing you like it."
                menu:
                    "It looks pretty!":
                        pass
                n 1eq "J-just pretty?"
                menu:
                    "What else would it be?":
                        pass
                n 1es "N-nothing!"
            elif persistent.natsuki_romance >= 100:
                n "I've felt like I can trust you more. So I decided to buy a nice new Bikini!"
                n "I hope you like it!"
                n "It's nice and easy to wear."
                n "It'd be nice to bring it over to your world if I ever cross over."
            $ persistent.seen_bikini = True
        else:
            n "Aah! Nice to be back."
            if persistent.wearing == "Bikini":
                n 4ek "Nice to not have to change, since I was already wearing this back in the room."
            else:
                n 4el "And it's nice to wear this outfit."
            n 4el "It's such a nice day! So let's have some fun!"
    else:
        n 1dl "Here we are, the beach!"
        n "What do you say, what should we do?"
        n 2dk "Hmm, I'll let you pick!"
    $ persistent.autoload = "chbeachdate_autoload"
    jump chbeach_loop



label chbeachdate_autoload:
    play music tbeach
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ beach = True
    $ HKBShowButtons()
    python:
        current_time = datetime.datetime.now().time().hour
    if current_time > 7 and current_time < 18:
        scene beach
    else:
        scene beach_eve
    play music tbeach
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
        call expression "chbeach_reload_" + str(persistent.monika_reload)
    else:
        call chbeach_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    jump chbeach_loop


label chbeach_reload_0:
    return
label chbeach_reload_1:
    $ allow_dialogue = True
    return
label chbeach_reload_2:
    $ allow_dialogue = True
    return
label chbeach_reload_3:
    $ allow_dialogue = True
    return
label chbeach_reload_4:
    $ allow_dialogue = True
    return

label chbeach_loop:
    python:
        current_time = datetime.datetime.now().time().hour
    call beach_showart
    $ allow_dialogue = True
    $ beach = True
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
            persistent.monikatopics = range(1,14)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False
    if current_time >= 19:
        $ persistent.autoload = "chbeachdate_night_autoload"
        if persistent.natsuki_romance >= 100:
            show natsuki 1ek at t11
        else:
            show natsuki 1dk at t11
        n "Oh! It's night!"
        n "Let me change us to night mode, and change my clothes."
        $ persistent.date = "beach_night"
        jump chbeachdate_night_autoload
    elif current_time >= 0 and current_time < 6:
        $ persistent.autoload = "chbeachdate_night_autoload"
        $ beach = False
        if persistent.natsuki_romance >= 100:
            show natsuki 4er at t11
        else:
            show natsuki 2dr at t11
        n "Hey!"
        n "I know you're messing with your clock!"
        n "It can't go from day time to past midnight in an instant you know!"
        $ persistent.date = "beach_night"
        jump chbeachdate_night_autoload

    if current_time > 6 and current_time < 18:
        scene beach
        if persistent.natsuki_romance >= 100:
            show natsuki 1ek at t11
        else:
            show natsuki 1dk at t11
    else:
        scene beach_eve
        if persistent.natsuki_romance >= 100:
            show natsuki 1ek at t11
        else:
            show natsuki 1dk at t11

    if persistent.random_talk:
        call expression "chbeach_" + str(persistent.current_monikatopic)
    else:
        jump chbeach_loop
    jump chbeach_loop



label chbeach_0:
    n "..."

# All this code is very messy and annoying. Will have to find a better way to do this."
label chbeach_1:
    if persistent.natsuki_romance >= 100:
        n 4el "We should go swimming!"
    else:
        show natsuki 2dl at t11
        n "We should go swimming!"
    n "I know the waves are cold but still."
    n "I love swimming!"
    return

label chbeach_2:
    if persistent.natsuki_romance >= 100:
        n 1el "I remember going here with my mom!"
    else:
        show natsuki 1dl at t11
        n "I remember going here with my mom!"
    n "When I was a little girl we always came here."
    if persistent.natsuki_romance >= 100:
        n 1en "With my dad too of course."
    else:
        show natsuki 1dn at t11
        n "With my dad too of course."
    n "I miss the old days..."
    return

label chbeach_3:
    if persistent.natsuki_romance >= 100:
        show natsuki 4ey at t11
    else:
        show natsuki 2dy at t11
        n "When I was a kid I HATED sand."
    n "It's itchy and sticky!"
    if persistent.natsuki_romance >= 100:
        show natsuki 4eh at t11
    else:
        show natsuki 2dh at t11
    n "But I then I...{w=0.5} realized it doesn't stick to you if you aren't wet."
    if persistent.natsuki_romance >= 100:
        show natsuki 1er at t11
    else:
        show natsuki 1dr at t11
    n "Don't laugh...{w=0.5} please."
    return

label chbeach_4:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "We should build some sandcastles!"
    n "There's plenty of sand."
    n "And the water could help keep it stable!"
    n "Well, if you'd like to. It's in the \"action\" menu."
    return

label chbeach_5:
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
    else:
        show natsuki 1dl at t11
    n "I love coming here with friends!"
    n "You can come to the beach for a variety of reasons!"
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "You could bring kids,{w=0.2} if you have any."
    n "You could go just to relax."
    if persistent.natsuki_love and persistent.natsuki_romance >= 150:
        n 1et "You could go for some,{w=0.2} alone time with your partner.{w=0.5} If you know what I mean."
        n "Hee hee."
    elif persistent.natsuki_love and persistent.natsuki_romance <= 150:
        n 2dl "You could come with your girlfriend!"
        n 1dz "Ehehehe!"
    else:
        n "Or just come with a friend!"
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
    else:
        show natsuki 1dl at t11
    n "It's always fun, whatever you do!"
    return

label chbeach_6:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "Do you like sand more or water more?"
    menu:
        "Sand!":
            pass
        "Water!":
            pass
    if persistent.natsuki_romance >= 100:
        show natsuki 4ej at t11
    else:
        show natsuki 2dj at t11
    n "Cool!"
    n "I like both the same."
    n "With sand you can make castles."
    n "But you can swim in water."
    return

label chbeach_7:
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
    else:
        show natsuki 1dl at t11
    n "Two words..."
    if persistent.natsuki_romance >= 100:
        show natsuki 1er at t11
    else:
        show natsuki 1dr at t11
    n "Seagulls"
    if persistent.natsuki_romance >= 100:
        show natsuki 4ee at t11
    else:
        show natsuki 2de at t11
    n "SUCK!"
    n "They always steal food!"
    n "It's so annoying!"
    n "And the sounds they make sometimes!"
    if persistent.natsuki_romance >= 100:
        show natsuki 1ew at t11
    else:
        show natsuki 1dw at t11
    n "Ugh..."
    n "Sorry, for venting [player]."
    n "Just needed to let that out."
    return

label chbeach_8:
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
    else:
        show natsuki 1dl at t11
    n "Have you ever been at the beach at sunset?"
    n "I never do because I always swim and by the time the sun goes down I'm too cold to stay!"
    n "Coming here at sunset is something I would want to do if I entered your reality."
    n "Maybe one day..."
    jump chbeach_loop

label chbeach_9:
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
        n "Hey [player]?"
        n "What do you think?"
        menu:
            "About what?":
                pass
        n "How I look?"
        menu:
            "What?":
                pass
        n 4et "Do you like what you see?"
        menu:
            "Um...?":
                pass
        n 1es "F-forget it..."
    else:
        show natsuki 1dl at t11
        n "I like this outfit!"
        n "It's light and keeps me cool."
        n 2dq "And it's not too revealing."
        n "I...{w=0.2} don't wanna wear something revealing unless we really trust eachother..."
        n 1dy "Sorry to disappoint, hahahha!"
    return

label chbeach_10:
    if persistent.natsuki_romance >= 100:
        show natsuki 4el at t11
    else:
        show natsuki 2dl at t11
    n "Monika talked about her experience with the beach."
    n "She said she came fairly often and never really with anyone."
    $ ten = renpy.random.randint(1, 2)
    if ten == 2:
        menu:
            "That's what she said!":
                pass
        if persistent.natsuki_romance >= 100:
            show natsuki 4ex at t11
        else:
            show natsuki 2dx at t11
        n "Shut up [player]."
        return
    if persistent.natsuki_romance >= 100:
        show natsuki 1eu at t11
    else:
        show natsuki 1du at t11
    n "I would feel bad for her."
    if persistent.natsuki_romance >= 100:
        show natsuki 1ez at t11
    else:
        show natsuki 1dz at t11
    n "But I only feel bad that she is suffering in the game's files!"
    return

label chbeach_11:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ej at t11
    else:
        show natsuki 1dj at t11
    n "I always liked the ambiance of the beach."
    n "It's calming and soothing."
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "Do you ever like to sit and listen to the waves?"
    n "Actually you don't need to answer."
    n "I can guess."
    return

label chbeach_12:
    if persistent.natsuki_romance >= 100:
        show natsuki 1el at t11
    else:
        show natsuki 1dl at t11
    n "I've always wanted to come to the beach for my birthday."
    n "It's in the fall though, so we never could."
    n "But hey!"
    n "My next birthday can be at the beach, since I control the game!"
    return

label chbeach_13:
    if persistent.natsuki_romance >= 100:
        show natsuki 4er at t11
    else:
        show natsuki 2dr at t11
    n "Do you know that annoyingly popular song called 'Baby Shark'?"
    if persistent.natsuki_romance >= 100:
        show natsuki 1es at t11
    else:
        show natsuki 1ds at t11
    n "You probably have. Sorry."
    n "I think the song is really annoying."
    n "What in the hell about that song is good?"
    if persistent.natsuki_romance >= 100:
        show natsuki 1eq at t11
    else:
        show natsuki 1dq at t11
    n "Ugh."
    return

label chbeach_action:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "Don't know..."
    n "Up to you."
    n "Try the actions button down there!"
    if persistent.natsuki_romance >= 200:
        n 4et "I wonder what we'll get up to."
        n "Ehehehe."
        menu:
            "Swimming sounds fun!":
                pass
            "...Sandcastles?":
                pass
            "Ooh! Ooh! We can grab a drink!":
                pass
        show natsuki 1es at s11
        n "Uhh, guh... Yeah sure!"
        show natsuki 2en at t11
        n "Sounds great!"
    elif persistent.natsuki_romance >= 100:
        n 4ed "Try to make it something romantic!"
        n "Since we're a couple and everything."
    elif persistent.natsuki_romance >= 50:
        n 1dl "Sounds like a nice to way to hang out more."
        n 2dk "Or... date more?"
        n "I'm, a bit new to this whole dating thing."
    jump chbeach_loop

label chbeach_oceanaction:
    if beach:
        $ allow_dialogue = False
        scene ocean
        with wipeleft_scene
        call beach_showart
        n "I love taking walks on the beach!"
        n "The waves are so nice!"
        n "Reminds me of the beach episode of..."
        n "You probably don't know that anime."
        window hide
        pause 5.0
        n "I'm really glad we came here!"
        n "It's much better then that stuffy room!"
        n "I know this is just a game. But I dont care!"
        n "Hehe!"
        n "Let's head back to the umbrellas!"
        if current_time >= 6 and current_time < 19:
            scene beach
        else:
            scene beach_eve
        with wipeleft_scene
        jump chbeach_loop
        call beach_showart
    else:
        "Don't act dumb."

label chbeach_sandcastleaction:
    if beach:
        $ allow_dialogue = False
        $ HKBHideButtons()
        play music t5
        "Natsuki sits on the sand."
        n "Shoot I dont have a shovel!"
        call updateconsole ("os.write(\"characters/shovel.obj\")", "shovel.obj written.")
        if renpy.loadable("..shovel.obj") == False:
            python:
                try: renpy.file(config.basedir + "../(shovel).obj")
                except: open(config.basedir + "/characters/shovel.obj", "wb").write(renpy.file("shovel.obj").read())
        n "Ehehe!"
        call hideconsole
        menu:
            "That's cheating!":
                pass
        n "The game does not have shovel what did you want me to do?!"
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
        scene ocean
        with wipeleft_scene
        "I walk down to the water."
        "Seizing a bucket I head down towards the water."
        "I grab some dry sand and place it into the bucket."
        "After that a dip the bucket into the water."
        "Once I have enough I head back up towards Natsuki."
        if current_time >= 6 and current_time < 19:
            scene beach
        else:
            scene beach_eve
        with wipeleft_scene
        "The bucket is really heavy."
        menu:
            "A little help?":
                pass
        call beach_showart
        n "Ugh... you can't do it yourself?"
        menu:
            "No!":
                pass
        n "Fine!"
        n "There happy?"
        menu:
            "Thanks.":
                pass
        n "Heh... you're welcome!"
        "We work together to build the ultimate sandcastle!"
        n "You know [player] I don't like to do childish things like this..."
        n "Usually people will judge me."
        n "Maybe I'm only confortable doing becuase I know it's not real."
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
        jump chbeach_loop
    else:
        "Lol no."
        jump chbeach_loop

label swimsuit:
    if persistent.natsuki_romance >= 100:
        show natsuki 1ek at t11
    else:
        show natsuki 1dk at t11
    n "Oh this?"
    n "If you wanna know who made the art check the {i}credits{/i}."
    if persistent.natsuki_romance >= 100:
        show natsuki 2ek at t11
    else:
        show natsuki 4dk at t11
    n "But you meant where did I get them? Huh?"
    if persistent.natsuki_romance >= 100:
        n 3ek "Well, I really was debating it."
        n 12ea "I'm not super... confident with my figure."
        n "Mostly because, yknow... I'm... small..."
        n "{i}sigh{/i}"
        n 1en "Uh, a-anyway!"
        n 3el "Being with you has made... well... more comfortable?"
        n 1el "So I decided, \"Hey, what the heck?\" and got this outfit."
        n 1en "I... h-hope you like it..."
        n 12eg "..."
        menu:
            "I love it, Natsuki.":
                n "T-thanks..."
                show natsuki 4eq at h11
                n "I-I mean! Yeah of course you should!"
                n "You dummy!"
            "Looks sexy.":
                show natsuki 1ep at h11
                n "Wha?!"
                n "Y-y-you!"
                n 12ed "..."
                n "[player]..."
                n "D-don't tease me like that..."
    else:
        n 1dl "I got the shirt at the mall, on one of my shopping days when my dad gave me money."
        n "I really liked it, and had the money."
        n "I was a bit worried about wearing it here though, because of the writing on it."
        n "I... kinda don't like people thinking I'm a Tsundere, even though... I sorta am."
        n 2di "D-don't tell anyone..."
        n 1dh "Well, I guess you can't..."
        n "You, know what I mean..."
    jump chbeach_loop

label sunburn:
    n "Well yeah, I guess."
    n "I mean the wind and water counter it a bit."
    n "And of course youre not wearing a jacket, so I guess it's not that bad."
    n "Sunburns are a real problem though."
    n "It sucks to have them!"
    n "Sleeping is even painful!"
    n "That's why I don't usually sunbathe."
    n "I swim as much as possible."
    n "Or just sit under an umbrella."
    n "But as long as you wear sunscreen and are careful the beach can be great!"
    n "I guess that Natsuki's protip of the day!"
    jump chbeach_loop

label chbeach_hair:
    n "Don't know."
    n "I didn't make this outfit."
    jump chbeach_loop

label chbeach_others:
    n "Hm..."
    n "I don't know..."
    call updateconsole("renpy.call(\"beachdate\")", "RenPy script called")
    $ config.overlay_screens = []
    hide screen hkb_overlay
    hide nb1
    show mirage
    s "Heeeeyyyyy!"
    call hideconsole
    m "Ah, hi [player]!"
    y "O-oh..."
    y "Hello [player]..."
    "Natsuki tries to speak but is too busy drinking."
    m "Are you ready to go play on the beach?"
    mc "Sure!"
    call updateconsole("renpy.pause(3.0)", "paused...")
    hide mirage
    call beach_showart
    n "Did you like my impression?"
    call hideconsole
    jump chbeach_loop

label chbeach_swimaction:
    scene ocean
    call beach_showart
    n "Ready?"
    menu:
        "Yes.":
            pass
        "Yes.":
            pass
    n "Good! Ehehe!"
    "Natsuki dips her foot in the water and suddenly steps back."
    n "Eek! It's cold!!"
    menu:
        "Haha!":
            pass
    n "H-hey! Shut up!!"
    call updateconsole ("$ persistent.water_temp == 70", "temperature changed")
    menu:
        "You use the console a lot!":
            pass
    n "Sooooo?"
    menu:
        "What would you do without it?":
            pass
    n "Ask you for help."
    n "Since you can control the game."
    n "Anyway lets swim!"
    call hideconsole
    "Natsuki runs into the water and goes pretty far out."
    hide nb1
    n "Heeeeeyyy!!!!"
    n "I'm so far out!"
    "I can barley see her."
    "I decide to run right into the water too."
    "I swim right up to her."
    call beach_showart
    n "Hey [player]~!"
    "She splashes a suprisigly big amount of water at my face."
    play music t7
    menu:
        "It's on Natsuki!!"
        "Splash her back.":
            "I land a huge wave of water in her face."
            n "Ack!!"
            n "Spff!!"
            n "Hey!!"
            $ won_water_fight = True
        "Block her next strike":
            "I stick up my arm to block her strike."
            "But my arm isn't big enough to stop it."
            "It hits me right it the face."
            mc "Ack!!"
            n "Hahaha!"
            menu:
                "No fair!!":
                    pass
            n "It is!!"
            $ won_water_fight = False
    if current_time >= 6 and current_time < 19:
        scene beach
    else:
        scene beach_eve
    with wipeleft_scene
    call beach_showart
    play music t8
    n "That was fun!"
    if won_water_fight:
        n "Nice job beating me!"
    else:
        n "I beat you!"
    n "Hope you had fun!"
    jump chbeach_loop

label chbeach_drinkaction:
    n "A drink?"
    n "Like a smoothie?"
    menu:
        "Yes of course!":
            pass
    n "Good!"
    n "I don't know my age and I don't wanna find out I'm condoning underage drinking!"
    if current_time >= 6 and current_time < 19:
        scene beach
    else:
        scene beach_eve
    with wipeleft_scene
    call beach_showart
    "We walk over to a drink stand."
    if renpy.loadable("..zack.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(zack).obj")
            except: open(config.basedir + "/characters/zack.chr", "wb").write(renpy.file("zack.chr").read())
    if not os.path.isfile(basedir + "/characters/zack.chr"):
        play sound "sfx/s_kill_glitch1.ogg"
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 1.0
        hide screen tear
        n "Come on [player]!"
        n "Not cool."
        jump chbeach_loop
    "Zack" "Hey hey hey!! Get your cool drinks here!!"
    if not os.path.isfile(basedir + "/characters/zack.chr"):
        play sound "sfx/s_kill_glitch1.ogg"
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 1.0
        hide screen tear
        n "Come on [player]!"
        n "Not cool."
        jump chbeach_loop
    n "Ah thanks!"
    if not os.path.isfile(basedir + "/characters/zack.chr"):
        play sound "sfx/s_kill_glitch1.ogg"
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 1.0
        hide screen tear
        n "Come on [player]!"
        n "Not cool."
        jump chbeach_loop
    "Zack" "Good think ya got em now. There on the house for a short time."
    n "Cool!"
    if not os.path.isfile(basedir + "/characters/zack.chr"):
        play sound "sfx/s_kill_glitch1.ogg"
        show screen tear(20, 0.1, 0.1, 0, 40)
        pause 1.0
        hide screen tear
        n "Come on [player]!"
        n "Not cool."
        jump chbeach_loop
    "Zack" "Have a nice day Ms!"
    if persistent.player_gender == "Female":
        "Zack" "And you too ma'am."
    elif persistent.player_gender == "Male":
        "Zack" "And you too sir."
    else:
        "Zack" "And you too..."
        n "They're name is [player]."
        "Zack" "Okay then, have a nice day [player]!"
    n "Don't worry I got something for you [player]"
    menu:
        "Thanks Natsuki.":
            pass
    n "Here!"
    "I take a sip of my drink."
    $ delete_character("zach")
    n "This is really good!"
    menu:
        "Yeah!":
            pass
    n "Hehe!"
    call beach_showart
    n "Well that was good!"
    jump chbeach_loop

label chbeach_digaction:
    n "Okay, let's go!"
    if renpy.loadable("..shovel.obj") == False:
        n "Wait..."
        n "I don't have a shovel!"
        call updateconsole("os.write\(characters/shovel.obj\)", "shovel.obj written sucessfully")
        python:
            try: renpy.file(config.basedir + "../(shovel).obj")
            except: open(config.basedir + "/characters/shovel.obj", "wb").write(renpy.file("shovel.obj").read())
        n "There!"
    n "Here's a good place!"
    "We begin digging into the sand."
    if renpy.random.randint(5, 10) == 10:
        n "Woah!"
        menu:
            "What?":
                pass
        n "I found a really cool gem!"
        n "I'm hanging on to this!"
    else:
        n "Ah..."
        n "I didn't find anything."
        n "Rats..."
    if current_time >= 6 and current_time < 19:
        scene beach
    else:
        scene beach_eve
    with wipeleft_scene
    n "Well..."
    n "Either way that was fun!"
    jump chbeach_loop

label chbeach_episodes:
    n "Does it?"
    n "I mean... I guess?"
    n "Except it's absolutely NOT fan service!"
    n "100 percent!"
    jump chbeach_loop

label chbeach_compliment:
    hide nb1
    #show nb2 --causing issues
    n "Urk..."
    n "..."
    n "T-Thanks [player]..."
    n "I-I guess..."
    jump chbeach_loop

label chbeach_time:
    n "A night version of this background doesn't exist."
    n "If I can get one, I'll add it and we cam come at night."
    jump chbeach_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
