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

label ch30_spookystart:
    if time_of_day == "Day":
        n jnb "Scary stories in the day?"
        n jad "No, [player]."
        n jnb "Come back after 7PM but not after 6AM, and I'll tell them to you."
        jump ch30_loop
    $ config.overlay_screens = []
    hide screen hkb_overlay
    n jha "Okay then!"
    n "Spooky it is."
    n "I have 2 tales for you this year."
    n "Which one do you want to start with?"
    menu:
        "[player]'s home":
            call story1
        "No Escape":
            call story2
    jump ch30_loop

label story1:
    n jhb "Nice choice."
    n "Okay..."
    stop music fadeout 2.0
    scene black with dissolve_scene_full
    play music t6
    "Our story begins in a home in Japan."
    scene kitchen with dissolve_scene_full
    "[player] is making food in [persistent.player_pronouns3] kitchen."
    "Natsuki walks out from [persistent.player_pronouns3] bedroom."
    show natsuki 2bk at t11
    n "Hey, [player] did you finish dinner?"
    mc "Natsuki, this takes a while."
    n 1bg "Hey, I'm just hungry."
    mc "Well, I'm almost done."
    n 1bl "Cool, I'll be in your room."
    hide natsuki with dissolve
    "Natsuki walks off."
    "[player] continues to make the cookies."
    if persistent.player_pronouns == "they":
        "As they bake, they hear a strange sound in the house."
    else:
        "As [persistent.player_pronouns] bakes, [persistent.player_pronouns] hears a strange sound in the house."
    mc "Odd..."
    "Another sound rings in [persistent.player_pronouns2] ears, this time below [persistent.player_pronouns2]."
    if persistent.player_pronouns == "they":
        "They squat down on the floor and press their ear to the floorboards."
    else:
        "So, [persistent.player_pronouns] squats down on the floor and presses [persistent.player_pronouns3] ear to the floorboards."
    mc "Nothing... odd..."
    "Getting up, [player] heads to [persistent.player_pronouns3] room."
    scene bedroom with wipeleft_scene
    mc "I'm here Natsuki!"
    show natsuki 3bh at t11
    n "There you are, jeez."
    n "You took forever."
    if persistent.player_gender == "Female":
        n "I thought girls were supposed to be good at cooking."
        mc "..."
        mc "I do not know how to respond to that."
    elif persistent.player_gender == "Male":
        n "Typical, don't trust a boy with cooking."
        mc "..."
        mc "Harsh..."
    else:
        n "I thought you were good at cooking."
        mc "I am, it just takes time..."
    n 1bw "Whatever, let's just watch this movie."
    mc "Right."
    show natsuki at lhide
    hide natsuki
    "[player] heads over to [persistent.player_pronouns3] closet."
    n "Hehe, whatcha got in your closet [player]?"
    mc "No, I don't have any lewd manga or anime, Natsuki."
    n "...I was gonna say bodies."
    n "Weirdo."
    mc "Oh."
    mc "Why would I have bodies in my closet?"
    n "I don't know, I wanted to make a spooky themed joke."
    n "Jeez..."
    "[player] finishes up and grabs some of [persistent.player_pronouns3] old DVDs."
    show natsuki 1ba at t11
    n "What do you wanna watch this year?"
    mc "I don't know..."
    "[player] reaches for the TV when-"
    stop music
    scene black
    n "AAAAAAAAAAAAAAAAAAAAAHHH!!!"
    "The lights went out."
    mc "Natsuki calm down it's just the lights."
    n "I-I'm not scared!"
    n "I-I just... uh..."
    mc "Haha, whatever. I gotta find the breaker, wait here."
    n "Will do."
    play music t6s
    "[player] walks down the stars and into the bottom floor."
    "Feeling around is [persistent.player_pronouns3] only real hope of seeing..."
    "The house is pitch dark, so [player] makes [persistent.player_pronouns3] way to the breaker room."
    "[player] reaches for the switch to turn on power, but nothing happens."
    "A scream rings out in the house..."
    mc "Natsuki!"
    "[player] runs out of the room, crashing into things on [persistent.player_pronouns3] way."
    "Unable to see, [player] trips and falls onto the floor."
    mc "NATSUKI! NATSUKI!! WHERE ARE YOU?!"
    n "Help! [player]! There's someone in here!"
    "[player] tries to stand, but [persistent.player_pronouns3] knee is injured."
    "Falling back to the floor, all [player] can do is listen as footsteps approach for the stairs."
    if persistent.player_gender == "Female":
        "???" "There you are girl."
    elif persistent.player_gender == "Male":
        "???" "There you are boy."
    else:
        "???" "There you are child."
    mc "Who are you?! What did you do to Natsuki?!"
    "???" "Don't worry, you'll see her soon..."
    "[player] feels a sharp pinch in [persistent.player_pronouns3] neck."
    if persistent.player_pronouns == "they":
        "Resistance is futile, and they pass out on the floor..."
    else:
        "Resistance is futile, and [persistent.player_pronouns] passes out on the floor..."
    pause 2.0
    call showroom
    n jha "Pretty scary huh?!"
    n "I have another story, just ask if you want me to tell it."
    return

label story2:
    n jhb "Nice choice."
    n "Okay..."
    stop music fadeout 2.0
    scene residential_night with dissolve_scene_full
    play music t6s
    "The mysterious voice had been following [persistent.player_pronouns2] for the past 3 blocks."
    "[player] was getting terrified now, was something coming for [persistent.player_pronouns2]?"
    "Alas, [persistent.player_pronouns] tried to whistle to herself to defuse the tension."
    "But the steps were behind [persistent.player_pronouns2] now."
    "So, [persistent.player_pronouns] stopped."
    mc "Hello?"
    show yuri 1y1 at t11
    y "Hello."
    mc "Yuri?! From school?"
    y 3u "Yes, it's me."
    mc "What are you doing out here?"
    y 3n "I was... uh... heading home!"
    y 4d "..."
    mc "Oh... alright then..."
    y 4b "May I... accompany you home, [player]?"
    mc "Sure Yuri, since you live close by anyway..."
    y 3y1 "Yes! Thank you!"
    y 3o "Uh! I mean!"
    y 4a "Thank you, [player]..."
    mc "Lets... go then..."
    show yuri 1a at t11
    "[player] and Yuri walked down the road."
    "While Yuri seemed elated to be with [player]."
    "[player] on the other hand was deep in thought."
    "Why would Yuri leave school at such a late hour?"
    "Why would Yuri follow [persistent.player_pronouns2] of all people?"
    "And why was Yuri so excited?"
    play music t10y
    y 1y1 "Aaah... [player]..."
    y "Has anyone ever told you how attractive you are?"
    mc "What?"
    if persistent.player_gender == "Female":
        y "You are so beautiful..."
        y "Your hair is so smooth..."
        y "And your eyes are so gentle..."
        y "And your skin..."
        y "Ahahahaha!"
        y 3y3 "I just want to tear it off and wear it!!"
    elif persistent.player_gender == "Male":
        y "You are so handsome..."
        y "Your so tall, and strong."
        y "And your smell..."
        y "Ehehehehe!"
        y 3y3 "I want to crawl inside you and smell you!"
    else:
        y "You are so gorgeous..."
        y "So mysterious and secretive..."
        y "Yet so alluring..."
        y 3y3 "Why don't you come to my house, and we can share eachother..."
    mc "Yuri what the hell?!"
    y "I love you [player]!"
    y "Don't you love me back?!"
    mc "I-I..."
    "[player] was at a loss for words."
    "What should [persistent.player_pronouns] say?"
    "Yuri seemed unhinged."
    mc "I-I..."
    "Yuri pulls a knife from her bag."
    "It's covered in blood."
    y "Do you like it [player]?"
    y "It has my blood on it."
    y "Now I can add your blood to it."
    y "We'll be bonded forever..."
    mc "No!"
    hide yuri with dissolve
    "[player] made a run for it."
    "Yuri screamed and began chasing [persistent.player_pronouns2]."
    "[player] ran as fast as [persistent.player_pronouns] could down the street."
    "If [persistent.player_pronouns] could make it to [persistent.player_pronouns3] house, she'd be safe."
    if persistent.player_gender == "Female":
        "Yuri caught up to [player] and grabbed the ribbon of [persistent.player_pronouns3] school uniform."
    elif persistent.player_gender == "Male":
        "Yuri caught up to [player] and grabbed the tie of [persistent.player_pronouns3] school uniform."
    else:
        "Yuri caught up to [player] and grabbed the shirt of [persistent.player_pronouns3] school uniform."
    "[player] almost fell, but pushed Yuri off and ran."
    "Yuri screamed again, laughing like a maniac."
    "[player] finally made it to her house, [persistent.player_pronouns] ran in and quickly shut and locked the door."
    scene kitchen with wipeleft_scene
    "In her kitchen, [persistent.player_pronouns] reached for the phone and dialed the police."
    if persistent.player_gender == "Female":
        "Operator" "\"110 What is your emergency ma'am?\""
    elif persistent.player_gender == "Male":
        "Operator" "\"110 What is your emergency sir?\""
    else:
        "Operator" "\"110 What is your emergency?\""
    mc "This girl from my class has gone crazy, she's trying to attack me with a knife!"
    "Operator" "\"Okay... now, can you please tell me where you are?\""
    mc "In my kitchen, at my house on 20221 Cassnide Street."
    "Operator" "\"Alright, please stay on the line. We'll be there soon...\""
    "A knife shot through the door, Yuri was trying to cut her way in!"
    mc "Aaaa!"
    "Operator" "\"Are you still there?\""
    mc "Yes! She's trying to cut her way through my door."
    "Yuri laughed maniacally. As her knife kept cutting the thin material of the door."
    "[player] backed up as far as [persistent.player_pronouns] could."
    "Yuri's laughs kept going, even as sirens rang from far away."
    "[player] closed [persistent.player_pronouns3] eyes, like it was the last time [persistent.player_pronouns]'d ever see the light."
    "Yuri's breath ran down [persistent.player_pronouns3] neck, as the voice of officers came from outside..."
    scene black
    stop music
    pause 2.0
    call showroom
    n jha "Pretty scary huh?!"
    n "I have another story, just ask if you want me to tell it."
    return

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
    if not persistent.seen_3yearintro:
        scene black
        "WARNING: Attempting to play the event without having seen the Anniversary Intro will lead to crashes!"
        "Your game will now close, please re-open it and try again <3"
        $ persistent.playthrough == 3
        $ persistent.autoload = "ch30_autoload"
        $ delete_all_saves()
        $ renpy.quit()
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
    "Flowers are blooming..."
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
    y "Sayori said she was bringing a guest."
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
    "Flowers are blooming..."
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
    