



default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None
default persistent.liked_outfit1 = None

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

label chmall_noskip:
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
    jump chclub_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"
image mangastore = "mod_assets/mangastore.png"
image bakery = "mod_assets/bakery.png"

label chmall_main:
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    $ persistent.autoload = "chmall_main"
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
    $ mall = True
    $ HKBShowButtons()
    scene mall
    play music t6
    n "Okay I got it!"
    show natsuki 1ba zorder 2 at t11
    n 1bz "Oh I miss this outfit!"
    n 1bk "Oh yeah with the other art I couldn't move around."
    show natsuki at t31
    n 1bd "Now I can!"
    show natsuki at t33
    pause 1.0
    show natsuki at t11
    n "That's fun!"
    n "So what's next?"
    $ persistent.autoload = "chmall_autoload"
    jump chmall_loop



label chmall_autoload:
    play music t6
    $ n.display_args["callback"] = slow_nodismiss
    $ n.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    $ mall = True
    $ HKBShowButtons()
    scene mall
    play music t6
    show natsuki 1ba zorder 2 at t11
    $ delete_character("monika")
    $ delete_character("sayori")
    $ delete_character("yuri")
    if renpy.loadable("..natsuki.chr") == False:
        python:
            try: renpy.file(config.basedir + "../(natsuki).chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    play music t6
    window auto
    if persistent.monika_reload <= 4:
        call expression "chmall_reload_" + str(persistent.monika_reload)
    else:
        call chmall_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        n "Now, where was I...?"
        pause 4.0
        call expression "chmall_" + str(persistent.current_monikatopic)
    jump chmall_loop


label chmall_reload_0:
    n "Your back yay!"
    return
label chmall_reload_1:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chmall_reload_2:
    n "Hey [player]!"
    $ allow_dialogue = True
    return
label chmall_reload_3:
    n "Hi again!"
    $ allow_dialogue = True
    return
label chmall_reload_4:
    n "Hi! Welcome back!"
    $ allow_dialogue = True
    return

label chmall_loop:
    show natsuki 1ba zorder 2 at t11
    $ allow_dialogue = True
    $ mall = True
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
            persistent.monikatopics = range(1,7)
        persistent.current_monikatopic = renpy.random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)

    $ allow_dialogue = False

    if persistent.random_talk:
        call expression "chmall_" + str(persistent.current_monikatopic)
    else:
        jump chmall_loop
    jump chmall_loop

label chmall_0:
    n "..."
    return

label chmall_1:
    n 1bk "While I do like to grab manga at the store there are some other things I like."
    n 4bl"Sometimes I go to bakeries to check out what they have."
    n "But I started liking the clothes store."
    n 3bl"It's where I got my swimsuit after all."
    n "I also got this outfit there."
    n "I reccomended it to Monika."
    n 1bk "I wonder if she ever checked it out."
    return

label chmall_2:
    n 2bk "We should check out the manga store."
    n 4bl "Maybe we could find a cool manga and read it together?"
    return

label chmall_3:
    n "I wonder if Yuri would have wanted to be here."
    n "If she were still around I mean."
    n "I feel like she would have made a beeline for the book store."
    n "Yuri is pretty funny sometimes."
    return

label chmall_4:
    n 2bk "I always talk about my friend's outside the literature club."
    n "But I never talk about each of them seperatly."
    n 4bl "Well there's Amy, who likes spiders."
    n "Hanaka, who reminds me a bit of Sayori."
    n "And Yui, she the smartest."
    n 1bm "They don't exist and they don't have charcater files so they can't join us."
    n "I miss them."
    return

label chmall_5:
    n 1bm "Sometimes after school when I don't feel like cooking I come here to look at the scenery and grab something to eat."
    n 3bk "I very rarely get fast food because it's so bad for you!"
    n "I really like getting sushi though."
    return

label chmall_6:
    n 4bl "Ah [player] come stai?"
    menu:
        "What are you saying?":
            pass
        "Fine I guess...?":
            pass
    n "Bene, bene!"
    n "Cosa voui fare?"
    n "I'm kidding!"
    n "I'm practicing italian."
    n 1bz "Eheh!"
    python:
        renpy.error("Stop it.")
    return

label chmall_7:
    n 1bm "Did you ever go to the mall in your reality?"
    if not persistent.natsuki_love:
        menu:
            "Yeah!":
                n "I figured."
            "Nah.":
                n "Odd..."
                n "Malls are so common nowadays."
            "Yeah, but only on dates.":
                n 1bl "Ooh you have a girlfriend?"
                n "What's her name?"
                $ girlfirendinput = renpy.input('',length=30).strip(' \t\n\r')
                $ girlfriend = girlfirendinput.lower()
                n "Ooh [girlfriend]!"
                n 5bf "I'm not jealous~"
                n 5bq "W-ere not even dating!"
    else:
        menu:
            "Yeah!":
                n "I figured."
            "Nah.":
                n "Odd..."
                n "Malls are so common nowadays."
    return

label chmall_videogames:
    n 1bm "Well we never had enough money for games."
    n "My dad used most of it for alchohol and bills."
    n "Sometimes if he was in good mood and had a bit of money he would lend me some."
    n "I really liked playing those dating simulator games."
    n 1bl "Like this one!"
    n "Some of them are a bit weird though..."
    jump chmall_loop

label chmall_clothingstore:
    n "If you want."
    n "It would be cool to pick out a new outfit."
    jump chmall_loop

label chmall_bakery:
    n 1bl "Well for bakeries in THIS mall I recomend Branya's bakery."
    n "They make really good pastires."
    n "But for some reason there is a really pissed off kid who's always on his laptop talking to someone."
    n 1bm "Wonder if it is the owner's kid."
    jump chmall_loop

label chmall_clothingstoreaction:
    scene clothesstore
    with wipeleft_scene
    show natsuki 1ba zorder 2 at t11
    n 4bl "I really love this store!"
    n "I better go look for something."
    show natsuki at lhide
    hide natsuki
    "Natsuki walks off towards the women's aisle."
    window hide
    pause 4.0
    n "Aha!"
    show natsuki 1ck zorder 2 at t11
    n "Hmm..."
    if persistent.natsuki_love:
        n 2cl "What do you think [player]?"
        n "How do I look?"
        menu:
            "You look good!":
                n 2cz "Ehehehe!"
                n "Thanks [player]!"
                n "I'll take this with me to the room."
                n "If you'd like me to wear it, let me know."
                n 1ck "Just for you!"
            "You look sexy!":
                n 1cp "Urk-!"
                n 1cm "Uuuh!! [player] that's lewd!"
                n 1cz "Hahahahaha!"
                n 2ck "Sorry, I couldn't resist."
                n "Hehe."
                show natsuki 1ct at face
                n "Don't worry [player]."
                n "I'll wear it for you whenever you want."
                n 2cz "Ehehehehe!"
                show natsuki 1ck at t11
                n "I'll take this with me."
                n "You can find it in the \"extras\" menu."
            "...":
                n 1cz "What, speechless?"
                n "Hahaha! I guess you like it."
                n "I'll take it with me to the room, it'll be in the \"extras\" menu."
    else:
        n 1cn "I'm not super sure on this one."
        n "I'll{w=0.2}, take this with me back to the room..."
        n "Just in case..."
    show natsuki at lhide
    hide natsuki
    scene mall
    with wipeleft_scene
    jump chmall_loop

label chmall_sayori:
    n 1bn "Well..."
    n "I don't know... She wasn't really the mall type..."
    n 1bl "Probably just get a smoothie."
    jump chmall_loop

label chmall_name:
    n "I don't know..."
    n "All I know is that it's somewhere in Japan."
    jump chmall_loop

label chmall_mangaaction:
    scene mangastore
    with wipeleft_scene
    show natsuki 1bk at t11 zorder 2
    n "Hmm."
    n "It weird that this place is so empty."
    n "I mean the game doesn't have any other characters..."
    n "Kinda lonley, But anyway."
    n 1ba "Let's look for some manga."
    "We walk around the store looking for some manga."
    n 1bl "Aha!"
    n "Wait is this??"
    n "A NEW VOLUME OF PARFAIT GIRLS??!!"
    n "YAYYY!!!!"
    n "I'm so happy!!!"
    n "Hehe!"
    scene mall
    with wipeleft_scene
    jump chmall_loop

label chmall_bakeryaction:
    n "Okay then! Let's go!"
    scene bakery
    with wipeleft_scene
    show natsuki 1bl at t11 zorder 2
    n "This is it!"
    n "I'm not sure about which bakery it is."
    n "But who cares?"
    n "Anyway let's grab some cupcakes!"
    "We walk over the counter and see a man looking rather tired."
    "Baker" "Hey whadda ya want?"
    n "Two cupcakes please!"
    "Baker" "Alright."
    "Thanks!"
    "The baker walks into the back and grabs cupcakes."
    "He hands them to us and walk off."
    n "Thanks I guess?"
    "We eat our cupcakes at the table."
    n "That was great!"
    scene mall
    with wipeleft_scene
    jump chmall_loop

label chmall_rainclouds:
    n 4bk "The heck is Rainclouds?"
    n "Hang on let me google that..."
    hide window
    show natsuki 4bk at lhide zorder 1
    hide natsuki
    call updateconsole("start chrome.exe", "start chrome.exe")
    pause 5.0
    call updateconsole("exit", "exiting")
    pause 0.5
    call hideconsole
    show natsuki 1bm at l11
    n "NOW I'M SAD!!"
    jump chmall_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
