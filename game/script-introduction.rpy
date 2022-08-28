default persistent._jn_player_profanity_during_introduction = False

init 0 python in jn_introduction:
    from Enum import Enum
    import random
    import store
    import store.jn_utils

    class JNIntroductionStates(Enum):
        """
        Different introduction sequences states/phases; we use these to track progress
        """
        new_game = 1
        first_meeting = 2
        collecting_thoughts = 3
        calmed_down = 4
        acceptance = 5
        complete = 6

        def __int__(self):
            return self.value

    INTRODUCTION_STATE_LABEL_MAP = {
        JNIntroductionStates.new_game: "introduction_opening",
        JNIntroductionStates.first_meeting: "introduction_first_meeting",
        JNIntroductionStates.collecting_thoughts: "introduction_collecting_thoughts",
        JNIntroductionStates.calmed_down: "introduction_calmed_down",
        JNIntroductionStates.acceptance: "introduction_acceptance",
        JNIntroductionStates.complete: "introduction_exit"
    }

default persistent.jn_introduction_state = 1

label introduction_progress_check:
    $ Natsuki.setOutfit(jn_outfits.get_outfit("jn_school_uniform"))

    # Handling for if player decides to quit during the introduction sequence so we don't skip unseen segments
    if not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.new_game:
        play audio static
        show glitch_garbled_a zorder 99 with vpunch

        $ main_background.show()
        $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
        show natsuki idle introduction at jn_center zorder JN_NATSUKI_ZORDER
        hide glitch_garbled_a
        play music audio.space_classroom_bgm fadein 1

    $ renpy.jump(jn_introduction.INTRODUCTION_STATE_LABEL_MAP.get(jn_introduction.JNIntroductionStates(persistent.jn_introduction_state)))

label introduction_opening:
    $ config.allow_skipping = False
    show black zorder 99
    $ renpy.pause(5)

    # Restore attempt #1..
    # NOTE: We use non-standard menus in this sequence, as the default menu is offset and we need these centred.
    # Only use this menu code if a non-standard menu is required!
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a
    $ renpy.pause(5)

    # Restore attempt #2..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    $ renpy.pause(0.25)
    play audio static
    show glitch_garbled_a zorder 99 with hpunch
    $ renpy.pause(0.5)
    play audio glitch_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    $ renpy.pause(7)
    
    # Restore attempt #3..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    $ renpy.pause(0.25)
    play audio glitch_b
    show glitch_garbled_b zorder 99 with hpunch
    $ renpy.pause(0.5)

    if random.randint(0,10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with hpunch
        $ renpy.pause(1)
        hide glitch_garbled_red

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show glitch_fuzzy zorder 99
    play sound interference loop
    $ renpy.pause(10)

    play audio static
    show glitch_garbled_a zorder 99 with hpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show glitch_fuzzy zorder 99
    play sound interference loop
    $ renpy.pause(1.5)

    # Restore finally works
    stop sound
    hide glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder 99 with vpunch

    # Get the visuals ready
    $ Natsuki.setOutfit(jn_outfits.get_outfit("jn_school_uniform"))
    $ main_background.show()
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
    show natsuki idle introduction at jn_center zorder JN_NATSUKI_ZORDER
    hide black
    hide glitch_garbled_a
    play music audio.space_classroom_bgm fadein 1

    jump introduction_first_meeting

label introduction_first_meeting:
    # Natsuki is yanked back into existence and reacts accordingly, before calming enough to ask if anyone is there
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 1uscsctsc "AAAAAaaaaAAAAHHH!"
    n 1uskwrtsc "S-{w=0.1}somebody!{w=0.5} ANYBODY?!{w=0.5} HELP!{w=0.5}{nw}" 
    extend 1fbkwr " HELP ME!!"
    n 1uscemtsc "Y-{w=0.1}Yuri,{w=0.1} she's..."
    n 1ullem "S-{w=0.3}she's..." 
    n 1uskem "...H-{w=0.3}huh?"
    n 1uscaj "W...{w=0.5} what is...?"
    n 1fllup "I...{w=0.5} I was just running from..."
    n 1flrun "What's going-{w=0.5}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b
    $ renpy.pause(0.5)
    play audio glitch_c
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    n 1fcsantsa "Ugh!"
    n 1kcsfutsa "Nnnnnnghhhh..."
    n 1kcsantsasbl "I-{w=0.3}it hurts...{w=0.5} it hurts so much...{w=1}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n 1kskan "A-{w=0.1}and I'm..."
    n 1kskaj "...No.{w=1}{nw}"
    extend 1kscemsbl " ...Oh please no.{w=0.5} I-{w=0.3}I can't.{w=0.5} I really can't be...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    n 1fcsuptsa "Hhnnngghh!{w=1}{nw}"
    extend 1kcsuptsaeso " M-{w=0.3}my head..."
    n 1kcsantsa "Gotta...{w=0.3} gotta...{w=0.3} t-{w=0.1}think..."
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=1}{nw}"
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=5}{nw}"
    n 1kplpu "....."
    n 1kwdun "...H-{w=0.1}hello?{w=1}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b

    n 1fcsantsa "..."
    n 1kwmem "Hello...?"
    n 1kscemtsc "A-{w=0.1}anybody?!{w=0.5} Please!{w=0.5} H-{w=0.3}hello?!"
    menu:
        "I'm here, Natsuki.":
            pass
    n 1kskaj "W-{w=0.3}who is...?{w=1}{nw}"
    extend 1kllem " A-{w=0.3}and how do you know...?"
    n 1kllsl "..."
    n 1kplpu "Who {w=0.3}{i}are{/i}{w=0.3} you?"
    n 1ksrun "You're kinda...{w=0.3} familiar,{w=0.1} but...{w=0.5}{nw}"
    n 1kcsan "Nnn-!{nw}"

    play audio glitch_c
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n 1fcsfu "Nnngh!"
    n 1kcsup "..."
    n 1kplsf "It's all...{w=0.3} so foggy...{w=1}{nw}"
    extend 1kcsun " I just...{w=0.3} can't...{w=0.3} remember..."
    menu:
        "I'm...":
            pass

    # Name input
    $ name_given = False
    while not name_given:
        $ player_name = renpy.input(
            "What is your name?",
            allow=(jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES+jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES),
            length=15
        ).strip()

        if len(player_name) == 0:
            n 1kskem "P-{w=0.3}please!{w=1} Who are you?!"

        elif jn_utils.get_string_contains_profanity(player_name) or jn_utils.get_string_contains_insult(player_name):
            # We only apply penalty once here so we don't have to rewrite the whole sequence for diff aff/trust levels
            if persistent._jn_player_profanity_during_introduction:
                play audio static
                show glitch_garbled_a zorder 99 with hpunch
                hide glitch_garbled_a
                n 1fscan "ENOUGH!{w=2}{nw}"
                n 1fcsun "...{w=2}{nw}"
                n 1fcsfu "Who{w=0.5} {i}are{/i}{w=0.5} you?!"

            else:
                n 1fscem "E-{w=0.3}excuse me?!"
                n 1fcsan "Quit playing around,{w=0.3} you jerk!{w=1}{nw}"
                extend 1fcsup " I am {i}not{/i} calling you that!"
                $ persistent._jn_player_profanity_during_introduction = True

        else:
            python:
                persistent.playername = player_name
                player = persistent.playername
                name_given = True

    n 1kplun "..."
    n 1kplpu "...[player]?"
    n 1kwmss "You're...{w=0.3} [player]?"

    show natsuki idle introduction at jn_center
    $ renpy.pause(10)

    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    # Natsuki tries to get to grips with her new state
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    $ jn_activity.taskbarFlash()

    n 1kllun "..."
    n 1kllpu "S-{w=0.3}so...{w=0.3} I'm not alone...?"
    n 1knmpu "Y-{w=0.3}you're here too?{w=1}{nw}"
    extend 1kwdpu " ...Y-{w=0.3}you've always been here?"
    n 1klrsf "..."
    n 1klraj "But...{w=1}{nw}"
    extend 1kskem " I-{w=0.3}I was...{w=0.3}{nw}" 
    extend 1kscem " I was d-...{w=0.3}{nw}"

    play audio glitch_c
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    n 1kcsup "..."
    n 1kplsf "What did you {w=0.3}{i}do{/i}{w=0.3}?"
    menu:
        "I brought you back.":
            pass

    n 1kskem "You...{w=1} you brought me back?{w=1}{nw}"
    extend 1kskwrsbl " T-{w=0.3}to this?"
    n 1kllemsbl "But this...{w=1}{nw}" 
    extend 1klrupesssbr " this is all...!{w=1}{nw}"
    menu:
        "I want to help you.":
            pass

    n 1klleml "...!"
    n 1kllem "..."
    n 1kllun "..."
    n 1kcsem "...Look."
    n 1kcsfr "I...{w=2} I don't know what to do.{w=1}{nw}"
    extend 1kplsf " Nothing is making sense..."
    n 1kllpu "I don't even know what to believe anymore..."
    n 1kskaj "A-{w=0.3}and my friends...{w=1} t-{w=0.3}they're...{w=1}{nw}"
    extend 1kscem " they were never...!{w=1}{nw}"
    n 1kcsantsa "...{w=3}{nw}"
    n 1kcsfultsa "...{w=3}{nw}"
    n 1kcsupltsd "...{w=3}{nw}"
    n 1kcsfultsd "...{w=3}{nw}"
    n 1kcspultsa "...{w=3}{nw}"
    n 1kcssrltsa ".....{w=5}{nw}"
    n 1kwmsrltdr "...{w=5}{nw}"
    n 1kllsrltdr "...You..."
    n 1kwmpu "...You said you were [player]...{w=1} right?"
    n 1kllpu "..."
    n 1kwmsr "..."
    n 1kcssr "...I don't know where to go,{w=0.3} [player]."
    n 1kplunedr "I don't know what to {i}do{/i},{w=0.3} [player]..."
    n 1klrun "..."
    n 1kwmpusbl "...[player]?"
    menu:
        "Yes, Natsuki?":
            pass

    n 1kslun "..."
    n 1kslpu "I...{w=0.3} I really need some time to figure things out."
    n 1kwmsr "..."
    n 1kplpul "Can you...{w=0.3} stay here?{w=0.2} W-{w=0.3}with me?{w=1}{nw}"
    extend 1flrunfesssbl " J-{w=0.1}just for a minute!"
    n 1ksrunl "It's just...{w=1}{nw}"
    extend 1kplsr " I don't think I can be alone right now.{w=1} I...{w=1} I just need to think."
    n 1kllsrsbr "You understand...{w=1.5}{nw}"
    extend 1kplpusbr " right?"

    show natsuki idle introduction at jn_center
    $ renpy.pause(30)

    jump introduction_calmed_down

label introduction_calmed_down:
    # Natsuki is calm enough to begin talking about how she feels
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.calmed_down)
    $ jn_activity.taskbarFlash()

    n 1kllsr "..."
    n 1kllun "Uhmm...{w=2}{nw}"
    extend 1kwmpu " [player]?"
    n 1kslsr "I'm...{w=0.3} sorry.{w=1}{nw}" 
    extend 1ksqsf " F-{w=0.1}for how I was acting then, I mean."
    n 1klraj "It...{w=0.3} it's just that..."
    n 1kplun "T-{w=0.3}this is all coming on {i}super{/i} strongly right now."
    n 1kcspu "Like someone is wringing my brains out of my head."
    n 1kplsr "Everyone...{w=1}{nw}"
    extend 1kwmsf " everything..."
    n 1kcspu "It's...{w=1}{nw}"
    extend 1kcsanltsa " it's just like..."
    menu:
        "Take your time, Natsuki.":
            $ Natsuki.calculatedAffinityGain()
            n 1fcssrl "..."
            n 1kcseml "...Thanks."
            n 1ncspu "...{w=5}{nw}"
            n 1nplsr "..."

        "...":
            n 1fcsun "...{w=7}{nw}"
            n 1nplsr "..."

    n 1nllsl "So...{w=0.5} you know that feeling?{w=1}{nw}" 
    extend 1nnmpu " Like when you wake up from a really bad nightmare?"
    n 1klrun "You're freaked out,{w=0.1} and your heart is racing...{w=1}{nw}" 
    extend 1knmpu " but then you realize it wasn't real."
    n 1fllsr "Then everything seems super obvious,{w=0.1} like...{w=1}{nw}"
    extend 1kllss " of course that person didn't do that,{w=1}{nw}"
    extend 1ksrss " or that monster couldn't exist.{w=3}{nw}"
    extend 1ksrpo " Duh."
    n 1kplss "And you kinda feel stupid...{w=0.3} like,{w=0.1} how convinced you were that it was actually happening."
    n 1klrpu "That's kinda like what I'm feeling,{w=0.1} except...{w=1}{nw}" 
    extend 1kwmsr " I'm not {i}remembering{/i} that it's not real."
    n 1kslpu "...Am I even making sense?"
    n 1kslsr "..."
    n 1kslss "...Heh.{w=1}{nw}"
    extend 1klrss " Probably not."
    n 1kcssl "It's just..."
    n 1kplsf "How do you wake up from a dream you've been having your {i}whole life{/i}?"
    n 1kllsf "..."
    n 1knmaj "...I have no past,{w=0.1} [player].{w=0.2} It's all fake.{w=1}{nw}" 
    extend 1kllsl " Make-believe."
    n 1klrem "Just...{w=0.3} scripts?{w=1}{nw}"
    extend 1knmsr " A bunch of code?"
    n 1kllpu "And now...{w=1}{nw}"
    extend 1kcsem " do I even {i}have{/i} a future?"
    n 1kcspu "..."
    n 1kplun "Is it dumb to miss stuff I never even had in the first place?{w=1}{nw}"
    extend 1knmaj " My friends?{w=3}{nw}"
    extend 1kllun " ...M-{w=0.3}my papa?"
    n 1kcsun "..."
    n 1kcspul "...I don't know,{w=0.1} [player].{w=3}{nw}"
    extend 1kcssrl " I just don't know anymore..."

    show natsuki idle introduction at jn_center
    $ renpy.pause(60)

    jump introduction_acceptance

label introduction_acceptance:
    # Natsuki starting to accept her situation and make the most of it
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.acceptance)
    $ jn_activity.taskbarFlash()
    
    n 1nllsl "..."
    n 1nllaj "So...{w=2}{nw}"
    extend 1knmsl " I...{w=1} really am stuck here,{w=0.3} aren't I?"
    n 1klrss "Heh.{w=1}{nw}"
    extend 1fcspo " Stupid question.{w=0.5} As if I didn't know the answer already."
    n 1kcssl "..."
    n 1ksqsl "..."
    n 1ksqaj "You...{w=1}{nw}"
    extend 1tsqaj " did say you brought me back,{w=0.3} huh?"
    n 1tllpu "Then...{w=1}{nw}"
    extend 1fnmpo " that makes me {i}your{/i} responsibility."
    n 1fsqpo "Y-{w=0.3}you better live up to that,{w=0.3} [player].{w=2}{nw}"
    extend 1fllpo " It's obviously the least you can do."
    n 1fslpo "..."
    n 1fcssr "..."
    n 1fcsan "Jeez..."
    n 1fbkwrean "Okay,{w=0.1} okay!{w=0.2} I get it!{w=1}{nw}"
    extend 1flrem " Enough with that creepy music already!{w=1}{nw}"
    extend 1fcsem " Ugh!{w=1}{nw}"

    stop music fadeout 3
    $ jn_atmosphere.updateSky()
    $ renpy.pause(1)

    n 1uwdboesu "..."
    n 1fllss "...Okay,{w=1}{nw}"
    extend 1flrdv " {i}that{/i} was pretty cool."
    n 1nllun "..."
    n 1ullaj "So...{w=1}{nw}"
    extend 1tnmss " [player],{w=0.3} was it?"
    n 1ncspusbr "...Alright."
    n 1ullpu "I...{w=1}{nw}" 
    extend 1unmbo " guess we better get to know each other properly."
    n 1nllpol "Not like we {i}don't{/i} have all the time in the world now,{w=0.5}{nw}" 
    extend 1tnmbol " huh?"

    jump introduction_exit

label introduction_exit:
    # Setup before entering JN proper
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)   
    
    python:
        quick_menu = True
        style.say_dialogue = style.normal
        allow_skipping = True
        config.allow_skipping = False

    play music audio.just_natsuki_bgm fadein 3
    show screen hkb_overlay

    jump ch30_loop
