init python:
    import subprocess
    import os
    import datetime
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

    def slow_nodismiss(event, interact=True, **kwargs):
        config.allow_skipping = False
        if persistent.monikas_return:
            if not os.path.isfile(basedir + "/characters/monika.chr"):
                renpy.call("ch31_monikareturn")
        if event == "begin":
            config.keymap['dismiss'] = []
            renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
            config.keymap['dismiss'] = dismiss_keys
            renpy.display.behavior.clear_keymap_cache()

define audio.partymusic = "<loop 4.9>mod_assets/bgm/partymusic.mp3"
define audio.drumroll = "mod_assets/sfx/drumroll.mp3"
define audio.applause = "mod_assets/sfx/applause.mp3"

label ch30_3yearautoload:
    $ persistent.playthrough == 0
    $ persistent.anticheat == 0
    python:
        today = datetime.date.today()
        day = datetime.date.today().strftime("%A")
        month = datetime.date.today().strftime("%B")
        date = datetime.date.today().strftime("%d")
        year = datetime.date.today().strftime("%Y")
        now = datetime.datetime.now()
        current_time = datetime.datetime.now().time().hour
    scene black
    show natsuki 4f at t11
    n "Hey, don't quit in the middle of my event!"
    n 4c "I'll... restart it from the top."
    n 2c "Unless you have a {b}save{/b} file. If you do, just load that."
    n "Alright, back to it."
    scene white with dissolve_scene
    jump ch30_3yearevent

label ch30_3yearevent:
    $ config.overlay_screens = []
    hide screen hkb_overlay
    $ persistent.playthrough = 0
    $ persistent.anticheat = 0
    $ persistent.autoload = "ch30_3yearautoload"
    python:
        today = datetime.date.today()
        day = datetime.date.today().strftime("%A")
        month = datetime.date.today().strftime("%B")
        date = datetime.date.today().strftime("%d")
        year = datetime.date.today().strftime("%Y")
        now = datetime.datetime.now()
        current_time = datetime.datetime.now().time().hour
    call showroom
    stop music
    n jha "So... it's been three years since {i}Doki Doki Literature Club{/i} came out."
    n jsa "I didn't have a mod of my own at the time."
    n "It wasn't until May of the next year that this was made for me."
    n jha "I couldn't be happier to be here!"
    n "Now... I have a surprise for you!"
    scene black
    n "And now! Introducing!!"
    pause 2.0
    n "Uh? Introducing!!!"
    pause 1.0
    n "{i}Drum guy! That's your cue!{/i}"
    n "INTRODUCING!!!"
    play audio drumroll
    pause 3.0
    $ renpy.movie_cutscene("partyintro.mpg")
    play music "<from 4.9>mod_assets/bgm/partymusic.mp3"
    scene club with dissolve_scene
    show natsuki 4l at t11
    n "We're so excited to be joined by our lovely stars!"
    n "Sayori!!"
    play audio applause
    show sayori 4m at t41
    s "AAAAAAAAHHH!!!"
    s "What's going on, where am I?"
    n "Yuri!"
    play audio applause
    show yuri 3y1 at t42
    show natsuki 1l at t43
    y "[player]!!! Do you love me??"
    show yuri 3p at h42
    y "Eek!"
    y 4b "[player]!! You're here??"
    if persistent.player_gender == "Female":
        y "A-and you're a woman?!"
        pause 1.0
        show yuri 4e at t42
        pause 1.5
        n 4l "Really gives a new context to your name!"
        n "AM I RIGHT FOLKS?!"
    s "WHAT IS GOING ON?!"
    n "Monika!"
    play audio applause
    show monika 5a at t43
    show natsuki 1l at t44
    m "Huh..."
    m 1b "It appears I am a puppet being brought in by Natsuki to act out a sick game for her."
    m 4b "Fascinating..."
    n 1h "Puppets don't break the fourth wall."
    m 1l "I mean, uh! Yay! Natsuki!"
    n 1l "And of course! You know me! You love me!"
    n "Natsuki!!!"
    play audio applause
    show yuri 2f at t42
    show sayori 1k at t41
    show monika 1a at t43
    pause 2.0
    n "Thank you! Thank you!"
    n "Tonight, we'll be telling the tragic tale..."
    s 1c "A tale of death!"
    y 1s "A tale of corruption."
    m 3a "A tale of love!"
    n "All here on!"
    n "{b}Natsuki's{w=1.0} Literature Club{w=1.0} Celebration!{/b}"
    play sound applause
    pause 3.0
    n 1l "Remember folks, if you at any point need to stop to do anything else, please use our convenient {b}save{/b} feature on your pause menu!"
    m 1l "I... thought you said no fourth wall bre-{nw}"
    n "Let the show begin!"
    stop music fadeout 2.0
    scene black with wipeleft_scene
    call screen dialog("Don't forget to SAVE the game, you don't want to lose all your progress here.", ok_action=Return)
    scene residential with dissolve_scene
    play music t2
    "Our tale begins on a fair day in the spring."
    "The birds are singing..."
    "Flower are blooming..."
    "But folks, this is no time for a bad time!"
    "[player]'s best friend, Sayori comes running down the street."
    show sayori 4p at t11
    s "Uwaaa!! [player] [player]!!!"
    "She cried out, in... dismay...?"
    s "I'm so sorry I was late! I was just oversleeping!"
    menu:
        "Why did you oversleep, Sayori?":
            pass
    s 1l "Because I am the ditzy airhead childhood friend!"
    s "It's my only characterization!"
    "Sayori and [player] walked together to the school."
    "Sayori worrying all the way about [player]!"
    s 1j "You need to get a hobby [player]!"
    s "You can't just spend all day inside!"
    menu:
        "We have to... We're quarantined...":
            pass
    s "That's no excuse to be lazy!"
    "Sayori urges [player] to look into a club."
    if persistent.player_pronouns == "they":
        "They reluctantly agree."
    else:
        "Alas, [persistent.player_pronouns] agrees."
    s 4r "Yayyy!"
    show sayori at lhide
    hide sayori
    "Sayori runs off, leaving [player] to enter the school alone."
    scene class with wipeleft_scene
    if persistent.player_pronouns == "they":
        "[player] spent most of their classes spacing out."
        "As they sit, spacing out, Sayori enters!"
    elif persistent.player_pronouns == "she":
        "[player] spent most of her classes spacing out."
        "As she sits, spacing out, Sayori enters!"
    elif persistent.player_pronouns == "he":
        "[player] spent most of his classes spacing out."
        "As he sits, spacing out, Sayori enters!"
    show sayori 4a at t44
    s "Hey!! [player]!"
    s "Get your goofy butt up!"
    s "I have a club for you to join."
    menu:
        "Do... I have a choice?":
            pass
    s 4r "No!"
    s 1a "Cmon! Let's go!"
    scene corridor with wipeleft_scene
    "Sayori drags [player] through the school all the way to a floor they've never been to before."
    "Sayori opens a door, pushing [player] in."
    scene club
    show natsuki 2m at t31
    show monika 1a at t32
    show yuri 3t at t33
    "[player] stumbles into a room full of girls."
    if persistent.player_pronouns == "they":
        "They look around in awe."
        "[player] can only stare at the beautiful girls in front of then."
    elif persistent.player_pronouns == "she":
        "She looks around in awe."
        "[player] can only stare at the beautiful girls in front of her."
    elif persistent.player_pronouns == "he":
        "He looks around in awe."
        "[player] can only stare at the beautiful girls in front of him."
    if persistent.player_gender == "Male":
        "Man, he's a sad loner."
    elif persistent.player_gender == "Female":
        "Looks like she's a massive lesbian."
    y 3n "A boy?!"
    if persistent.player_gender != "Male":
        "It would seem that Yuri believes that even though [player] is very clearly not a boy."
        "She still thinks that they're a strange boy."
        "She must be a best selling author."
    m 3k "Hello there."
    m "You must be Sayori's friend? [player] right?"
    m "Welcome to the literature club."
    m "Sayori has said many nice things about you."
    hide monika
    hide natsuki
    with dissolve
    show yuri 1a at t11
    y "Hi. I'm Yuri."
    menu:
        "I'm [player].":
            pass
    y 1b "Pleasure to meet you."
    y "Sayori said she was brining a guest."
    show natsuki 4c at t21
    show yuri at t22
    n "That's a good thing too."
    n 1j "I made cupcakes."
    y "Oh yes, I nearly forgot about that."
    y "Why don't we have them now?"
    hide natsuki
    hide yuri
    with wipeleft
    "[player] sits down at the table with the girls."
    "They discuss the club, themselves and other things."
    "Natsuki is very reserved, while Yuri is quiet."
    "Sayori and Monika are chatty though."
    "Bye the end of the day, [player] joins the club."
    if persistent.player_pronouns == "they":
        "They head home, ready for the next day!"
    elif persistent.player_pronouns == "she":
        "She heads home, ready for the next day!"
    elif persistent.player_pronouns == "he":
        "He heads home, ready for the next day!"
    scene black dissolve_scene_full
    "END OF DEMO"
    jump ch30_autoload