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
        $ config.allow_skipping = False
        $ n.display_args["callback"] = jnNoDismissDialogue
        $ n.what_args["slow_abortable"] = False
        play audio static
        show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch

        $ main_background.show()
        $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
        show natsuki idle introduction at jn_center zorder JN_NATSUKI_ZORDER
        $ jnPause(0.25)
        hide glitch_garbled_a
        play music audio.space_classroom_bgm fadein 1

    $ renpy.jump(jn_introduction.INTRODUCTION_STATE_LABEL_MAP.get(jn_introduction.JNIntroductionStates(persistent.jn_introduction_state)))

label introduction_opening:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ n.display_args["callback"] = jnNoDismissDialogue
    $ n.what_args["slow_abortable"] = False
    show black zorder JN_BLACK_ZORDER
    $ jnPause(5)

    # Restore attempt #1..
    # NOTE: We use non-standard menus in this sequence, as the default menu is offset and we need these centred.
    # Only use this menu code if a non-standard menu is required!
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a
    $ jnPause(5)

    # Restore attempt #2..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    $ jnPause(0.25)
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    $ jnPause(0.5)
    play audio glitch_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    $ jnPause(7)

    # Restore attempt #3..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    $ jnPause(0.25)
    play audio glitch_b
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    $ jnPause(0.5)

    if random.randint(0,10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder JN_GLITCH_ZORDER with hpunch
        $ jnPause(1)
        hide glitch_garbled_red

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show sky glitch_fuzzy zorder JN_GLITCH_ZORDER
    play sound interference loop
    $ jnPause(10)

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show sky glitch_fuzzy zorder JN_GLITCH_ZORDER
    play sound interference loop
    $ jnPause(1.5)

    # Restore finally works
    stop sound
    hide sky glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch

    # Get the visuals ready
    $ Natsuki.setOutfit(jn_outfits.get_outfit("jn_school_uniform"))
    $ main_background.show()
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
    show natsuki idle introduction at jn_center zorder JN_NATSUKI_ZORDER
    pause 0.25
    hide black
    hide glitch_garbled_a
    play music audio.space_classroom_bgm fadein 1

    jump introduction_first_meeting

label introduction_first_meeting:
    # Natsuki is yanked back into existence and reacts accordingly, before calming enough to ask if anyone is there
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 4uscsctsc "AAAAAaaaaAAAAHHH!"
    n 4uskwrtsc "S-{w=0.1}somebody!{w=0.5} ANYBODY?!{w=0.5} HELP!{w=0.5}{nw}"
    extend 1fbkwr " HELP ME!!"
    n 4uscemtsc "Y-{w=0.1}Yuri,{w=0.1} she's..."
    n 1ullem "S-{w=0.3}she's..."
    n 1uskem "...H-{w=0.3}huh?"
    n 4uscaj "W...{w=0.5} what is...?"
    n 1fllup "I...{w=0.5} I was just running from..."
    n 1flrun "What's going-{w=0.5}{nw}"

    show natsuki 4kskantsc
    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(0.5)
    play audio glitch_c
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 4fcsantsa "Ugh!"
    n 1kcsfutsa "Nnnnnnghhhh..."
    n 1kcsantsasbl "I-{w=0.3}it hurts...{w=0.5} it hurts so much...{w=1}{nw}"

    show natsuki 4fcsantsasbl
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a

    n 1kskan "A-{w=0.1}and I'm..."
    n 4kskaj "...No.{w=1}{nw}"
    extend 4kscemsbl " ...Oh please no.{w=0.5} I-{w=0.3}I can't.{w=0.5} I really can't be...{w=0.5}{nw}"

    show natsuki 4kcsantsc
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 4fcsuptsa "Hhnnngghh!{w=1}{nw}"
    extend 4kcsuptsaeso " M-{w=0.3}my head..."
    n 4kcsantsa "Gotta...{w=0.3} gotta...{w=0.3} t-{w=0.1}think..."
    n 2kcsaj "...{w=1}{nw}"
    n 2kcsem "...{w=1}{nw}"
    n 2kcsaj "...{w=1}{nw}"
    n 2kcsem "...{w=5}{nw}"
    n 2kplpu "....."
    n 4kwdun "...H-{w=0.1}hello?{w=1}{nw}"

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    show natsuki 1kcsantsa

    n 4fcsantsa "..."
    n 1kwmem "Hello...?"
    n 4kscemtsc "A-{w=0.1}anybody?!{w=0.5} Please!{w=0.5} H-{w=0.3}hello?!"
    show natsuki 4kcsuptsa

    menu:
        "I'm here, Natsuki.":
            pass

    n 4kskaj "W-{w=0.3}who is...?{w=1}{nw}"
    extend 4kllem " A-{w=0.3}and how do you know...?"
    n 2kllsl "..."
    n 4kplpu "Who {w=0.3}{i}are{/i}{w=0.3} you?"
    n 4ksrun "You're kinda...{w=0.3} familiar,{w=0.1} but...{w=0.5}{nw}"
    n 1kcsan "Nnn-!{nw}"

    play audio glitch_c
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a

    n 4fcsfu "Nnngh!"
    n 4kcsup "..."
    n 4kplsf "It's all...{w=0.3} so foggy...{w=1}{nw}"
    extend 4kcsun " I just...{w=0.3} can't...{w=0.3} remember..."
    show natsuki 4kcsem
    
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
            n 4kskem "P-{w=0.3}please!{w=1} Who are you?!"

        elif jn_nicknames.getPlayerNicknameType(player_name) != jn_nicknames.NicknameTypes.neutral:            # We only apply penalty once here so we don't have to rewrite the whole sequence for diff aff/trust levels
            if persistent._jn_player_profanity_during_introduction:
                play audio static
                show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
                hide glitch_garbled_a
                n 4fscan "ENOUGH!{w=2}{nw}"
                n 2fcsun "...{w=2}{nw}"
                n 2fcsfu "Who{w=0.5} {i}are{/i}{w=0.5} you?!"

            else:
                n 4fscem "E-{w=0.3}excuse me?!"
                n 4fcsan "Quit playing around,{w=0.3} you jerk!{w=1}{nw}"
                extend 2fcsup " I am {i}not{/i} calling you that!"
                $ persistent._jn_player_profanity_during_introduction = True

        else:
            python:
                persistent.playername = player_name
                player = persistent.playername
                name_given = True

    n 4kplun "..."
    n 4kplpu "...[player]?"
    n 4kwmss "You're...{w=0.3} [player]?"

    show natsuki idle introduction at jn_center
    $ jnPause(10)

    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    # Natsuki tries to get to grips with her new state
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    $ jn_activity.taskbarFlash()

    n 4kllun "..."
    n 4kllpu "S-{w=0.3}so...{w=0.3} I'm not alone...?"
    n 4knmpu "Y-{w=0.3}you're here too?{w=1}{nw}"
    extend 4kwdpu " ...Y-{w=0.3}you've always been here?"
    n 2klrsf "..."
    n 2klraj "But...{w=1}{nw}"
    extend 1kskem " I-{w=0.3}I was...{w=0.3}{nw}"
    extend 4kscem " I was d-...{w=0.3}{nw}"

    show natsuki 1fcsup
    play audio glitch_c
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c

    n 4kcsup "..."
    n 4kplsf "What did you {w=0.3}{i}do{/i}{w=0.3}?"

    menu:
        "I brought you back.":
            pass

    n 1kskem "You...{w=1} you brought me back?{w=1}{nw}"
    extend 4kskwrsbl " T-{w=0.3}to this?"
    n 4kllemsbl "But this...{w=1}{nw}"
    extend 4klrupesssbr " this is all...!{w=1}{nw}"

    menu:
        "I want to help you.":
            pass

    n 4klleml "...!"
    n 4kllem "..."
    n 2kllun "..."
    n 2kcsem "...Look."
    n 1kcsfr "I...{w=2} I don't know what to do.{w=1}{nw}"
    extend 1kplsf " Nothing is making sense..."
    n 4kllpu "I don't even know what to believe anymore..."
    n 4kskaj "A-{w=0.3}and my friends...{w=1} t-{w=0.3}they're...{w=1}{nw}"
    extend 4kscem " they were never...!{w=1}{nw}"
    n 4kcsantsa "...{w=3}{nw}"
    n 4kcsfultsa "...{w=3}{nw}"
    n 4kcsupltsd "...{w=3}{nw}"
    n 4kcsfultsd "...{w=3}{nw}"
    n 4kcspultsa "...{w=3}{nw}"
    n 4kcssrltsa ".....{w=5}{nw}"
    n 4kwmsrltdr "...{w=5}{nw}"
    n 4kllsrltdr "...You..."
    n 1kwmpu "...You said you were [player]...{w=1} right?"
    n 1kllpu "..."
    n 1kwmsr "..."
    n 1kcssr "...I don't know where to go,{w=0.3} [player]."
    n 4kplunedr "I don't know what to {i}do{/i},{w=0.3} [player]..."
    n 4klrun "..."
    n 4kwmpusbl "...[player]?"

    menu:
        "Yes, Natsuki?":
            pass

    n 3kslun "..."
    n 3kslpu "I...{w=0.3} I really need some time to figure things out."
    n 4kwmsr "..."
    n 4kplpul "Can you...{w=0.3} stay here?{w=0.2} W-{w=0.3}with me?{w=1}{nw}"
    extend 2flrunfesssbl " J-{w=0.1}just for a minute!"
    n 2ksrunl "It's just...{w=1}{nw}"
    extend 4kplsr " I don't think I can be alone right now.{w=1} I...{w=1} I just need to think."
    n 4kllsrsbr "You understand...{w=1.5}{nw}"
    extend 4kplpusbr " right?"

    show natsuki idle introduction at jn_center
    $ jnPause(30)

    jump introduction_calmed_down

label introduction_calmed_down:
    # Natsuki is calm enough to begin talking about how she feels
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.calmed_down)
    $ jn_activity.taskbarFlash()

    n 2kllsr "..."
    n 2kllun "Uhmm...{w=2}{nw}"
    extend 4kwmpu " [player]?"
    n 4kslsr "I'm...{w=0.3} sorry.{w=1}{nw}"
    extend 1ksqsf " F-{w=0.1}for how I was acting then, I mean."
    n 1klraj "It...{w=0.3} it's just that..."
    n 1kplun "T-{w=0.3}this is all coming on {i}super{/i} strongly right now."
    n 4kcspu "Like someone is wringing my brains out of my head."
    n 4kplsr "Everyone...{w=1}{nw}"
    extend 4kwmsf " everything..."
    n 4kcspu "It's...{w=1}{nw}"
    extend 4kcsanltsa " it's just like..."

    menu:
        "Take your time, Natsuki.":
            $ Natsuki.calculatedAffinityGain()
            n 4fcssrl "..."
            n 4kcseml "...Thanks."
            n 1ncspu "...{w=5}{nw}"
            n 1nplsr "..."

        "...":
            n 1fcsun "...{w=7}{nw}"
            n 1nplsr "..."

    n 1nllsl "So...{w=0.5} you know that feeling?{w=1}{nw}"
    extend 2nnmpu " Like when you wake up from a really bad nightmare?"
    n 2klrun "You're freaked out,{w=0.1} and your heart is racing...{w=1}{nw}"
    extend 2knmpu " but then you realize it wasn't real."
    n 4fllsr "Then everything seems super obvious,{w=0.1} like...{w=1}{nw}"
    extend 2kllss " of course that person didn't do that,{w=1}{nw}"
    extend 2ksrss " or that monster couldn't exist.{w=3}{nw}"
    extend 2ksrpo " Duh."
    n 2kplss "And you kinda feel stupid...{w=0.3} like,{w=0.1} how convinced you were that it was actually happening."
    n 2klrpu "That's kinda like what I'm feeling,{w=0.1} except...{w=1}{nw}"
    extend 4kwmsr " I'm not {i}remembering{/i} that it's not real."
    n 4kslpu "...Am I even making sense?"
    n 2kslsr "..."
    n 2kslss "...Heh.{w=1}{nw}"
    extend 2klrss " Probably not."
    n 1kcssl "It's just..."
    n 1kplsf "How do you wake up from a dream you've been having your {i}whole life{/i}?"
    n 1kllsf "..."
    n 4knmaj "...I have no past,{w=0.1} [player].{w=0.2} It's all fake.{w=1}{nw}"
    extend 4kllsl " Make-believe."
    n 1klrem "Just...{w=0.3} scripts?{w=1}{nw}"
    extend 4knmsr " A bunch of code?"
    n 1kllpu "And now...{w=1}{nw}"
    extend 1kcsem " do I even {i}have{/i} a future?"
    n 1kcspu "..."
    n 4kplun "Is it dumb to miss stuff I never even had in the first place?{w=1}{nw}"
    extend 4knmaj " My friends?{w=3}{nw}"
    extend 4kllunsbl " ...M-{w=0.3}my papa?"
    n 1kcsun "..."
    n 1kcspul "...I don't know,{w=0.1} [player].{w=3}{nw}"
    extend 2kcssrl " I just don't know anymore..."

    show natsuki idle introduction at jn_center
    $ jnPause(60)

    jump introduction_acceptance

label introduction_acceptance:
    # Natsuki starting to accept her situation and make the most of it
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.acceptance)
    $ jn_activity.taskbarFlash()

    n 2nllsl "..."
    n 2nllaj "So...{w=2}{nw}"
    extend 2knmsl " I...{w=1} really am stuck here,{w=0.3} aren't I?"
    n 2klrss "Heh.{w=1}{nw}"
    extend 2fcspo " Stupid question.{w=0.5} As if I didn't know the answer already."
    n 1kcssl "..."
    n 1ksqsl "..."
    n 4ksqaj "You...{w=1}{nw}"
    extend 4tsqaj " did say you brought me back,{w=0.3} huh?"
    n 2tllpu "Then...{w=1}{nw}"
    extend 2fnmpo " that makes me {i}your{/i} responsibility."
    n 2fsqpo "Y-{w=0.3}you better live up to that,{w=0.3} [player].{w=2}{nw}"
    extend 2fllpo " It's obviously the least you can do."
    n 2fslpo "..."
    n 2fcssr "..."
    n 1fcsan "Jeez..."
    n 4fbkwrean "Okay,{w=0.1} okay!{w=0.2} I get it!{w=1}{nw}"
    extend 3flrem " Enough with that creepy music already!{w=1}{nw}"
    extend 3fcsem " Ugh!{w=1}{nw}"

    stop music fadeout 3
    $ jn_atmosphere.updateSky()
    $ jnPause(1)

    n 3uwdboesu "..."
    n 3fllss "...Okay,{w=1}{nw}"
    extend 4flrdv " {i}that{/i} was pretty cool."
    n 4nllun "..."
    n 1ullaj "So...{w=1}{nw}"
    extend 1tnmss " [player],{w=0.3} was it?"
    n 1ncspusbr "...Alright."
    n 1ullpu "I...{w=1}{nw}"
    extend 2unmbo " guess we better get to know each other properly."
    n 2nllpol "Not like we {i}don't{/i} have all the time in the world now,{w=0.5}{nw}"
    extend 2tnmbol " huh?"

    jump introduction_exit

label introduction_exit:
    # Setup before entering JN proper
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        allow_skipping = True
        config.allow_skipping = False

        global LAST_TOPIC_CALL
        LAST_TOPIC_CALL = datetime.datetime.now()

    play music audio.just_natsuki_bgm fadein 3
    show screen hkb_overlay

    jump ch30_loop
