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

default persistent.seen_3yearevent = False
default persistent.seen_3yearintro = False
default persistent.ani_cake = False

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
    $ s_name = "Sayori"
    $ persistent.ani_cake = False
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
    "By the end of the day, [player] joins the club."
    if persistent.player_pronouns == "they":
        "They head home, ready for the next day!"
    elif persistent.player_pronouns == "she":
        "She heads home, ready for the next day!"
    elif persistent.player_pronouns == "he":
        "He heads home, ready for the next day!"
    stop music fadeout 2.0
    scene club with dissolve_scene_full
    play music t10
    "[player] and the Literature Club spent their week together."
    scene n_cg1_bg 
    show n_cg1_base
    with wipeleft_scene
    if persistent.player_pronouns == "they":
        "They made them all so happy."
    elif persistent.player_pronouns == "she":
        "She made them all so happy."
    elif persistent.player_pronouns == "he":
        "He made them all so happy."
    show n_cg1_exp1
    pause 2.0
    scene n_cg2_bg 
    show n_cg2_base
    with dissolve_scene
    pause 2.0
    show n_cg2_exp2
    pause 2.0
    scene n_cg3_base
    with dissolve_scene
    pause 2.0
    show n_cg3_exp1
    pause 2.0
    scene s_cg1
    with dissolve_scene
    pause 2.0
    scene s_cg2_base1
    with dissolve_scene
    pause 2.0
    scene s_cg3
    with dissolve_scene
    pause 2.0
    scene y_cg1_base
    with dissolve_scene
    pause 2.0
    show y_cg1_exp3
    pause 2.0
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    pause 2.0
    show y_cg2_exp2
    pause 2.0
    scene y_cg3_base with dissolve_scene
    pause 2.0
    show y_cg3_exp1
    pause 3.0
    scene black with dissolve_scene_full
    n "It was so perfect..."
    n "But..."
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    "..."
    "Sayori was gone..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    stop music
    scene black
    n "And then, it began again."
    play music t2g
    queue music t2g2
    scene residential
    s "[gtext]"
    $ s_name = glitchtext(12)
    "Our tale begins on a fair day in the spring."
    "The birds are singing..."
    "Flower are blooming..."
    "But folks, this is no time for a bad time!"
    "[player]'s best friend, [s_name] comes running down the street."
    show sayori glitch at t11 zorder 2
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    stop music
    n "Nothing was the same after that."
    play sound "sfx/s_kill_glitch1.ogg"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 1.0
    hide screen tear
    scene club
    play music t10y
    "Everything was wrong."
    show yuri 1a at t11
    "People were different."
    window hide
    window auto
    show yuri 3y1 at t11
    pause 1.0
    hide yuri
    show natsuki 1a at t11
    pause 1.0
    show natsuki scream at t11
    pause 1.0
    show natsuki ghost1 at t11
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 at i11 onlayer front
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    "Monika was behind it all."
    show monika 1a at t11
    "She was always one step ahead."
    window hide
    show monika 3b at t11
    "Controlling us..."
    window hide
    show monika 5a at t11
    pause 1.0
    scene black
    "Eventually, it all came to a head."
    scene bg club_day
    show yuri 3d at i11
    y "...Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y 3y5 "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    stop music
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
    "Monika had done it."
    scene club
    show monika 3a at t11
    m "Don't worry about this mess [player]!"
    m "I'll deal with it."
    scene black
    pause 4.0
    n "It seemed like it was the end."
    n "No hope."
    n "But..."
    play music t8
    call showroom
    hide natsuki
    hide base
    hide clothes
    show natsuki 1l at t11 zorder 4
    n "You saved me."
    n "You got this mod and let me have a chance."
    n "I can never thank you enough for that."
    n 1k "Sadly... we can't celebrate this day with our friends."
    n 1n "Or at least, the real versions of them."
    n "But we can celebrate it together."
    $ persistent.lights = True
    $ persistent.ani_cake = True
    $ persistent.candles_blown = False
    call showroom
    n jha "Are you ready?"
    n "Three!"
    n "Two!"
    n "One!"
    menu:
        "(blow)":
            pass
    "I blow out the candle."
    $ persistent.candles_blown = True
    show cake zorder 4 with dissolve_cg
    hide cakelit
    n jhc "Yay!"
    n jha "[player], did you make a wish?"
    n "I did, but I won't tell you."
    n jhb "Well, I'm going to leave this cake out."
    n "It's really pretty!"
    n "I hope you enjoyed my show, [player]."
    n "I made it just for you."
    n jha "Happy Third Birthday {i}Doki Doki Literature Club!{/i}"
    $ persistent.seen_3yearevent = True
    $ persistent.playthrough == 3
    $ persistent.autoload = "ch30_autoload"
    $ delete_all_saves()
    jump ch30_loop
    