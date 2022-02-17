init 0 python in jn_introduction:
    from Enum import Enum
    import random
    import store
    import store.jn_utils

    class JNIntroductionStates(Enum):
        new_game = 0
        first_meeting = 1
        collecting_thoughts = 2
        complete = 3

        def __int__(self):
            return self.value

default persistent.jn_introduction_state = 0

#TODO: Handling for player quit-out during the introduction sequence, so can continue where left off w/ additional dialogue

label introduction_opening:
    $ config.allow_skipping = False
    scene black
    $ renpy.pause(5)

    # Restore attempt #1..
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

    # Restore finally works
    stop sound
    hide glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    # Get the visuals ready
    $ main_background.draw(full_redraw=True)
    if (jn_get_current_hour() > 6 and jn_get_current_hour() <= 18
        and not jn_atmosphere.is_current_weather_sunny()):
        $ jn_atmosphere.show_sky(jn_atmosphere.JNWeatherTypes.sunny)
    show natsuki 1uscaj at jn_center
    play music audio.space_classroom_bgm fadein 1
    jump introduction_first_meeting

label introduction_first_meeting:
    # Natsuki is yanked back into existence and reacts accordingly, before calming enough to ask if anyone is there
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 1uscsc "AAAAAaaaaAAAAHHH!"
    n 1uskwr "S-{w=0.1}somebody!{w=0.5} ANYBODY?!{w=0.5} HELP!{w=0.5}{nw}" 
    extend 1fbkwr " HELP ME!!"
    n 1uscem "Y-{w=0.1}Yuri,{w=0.1} she's..."
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

    n 1fcsan "Ugh!"
    n 1kcsfu "Nnnnnnghhhh..."
    n 1kcsan "I-{w=0.3}it hurts...{w=0.5} it hurts so much...{w=1}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n 1kskan "A-{w=0.1}and I'm..."
    n 1kskaj "...No.{w=1}{nw}"
    extend 1kscem " ...Oh please no.{w=0.5} I-{w=0.3}I can't.{w=0.5} I really can't be...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    n 1fcsup "Hhnnngghh!{w=1}{nw}"
    extend 1kcsup " M-{w=0.3}my head..."
    n 1kcsan "Gotta...{w=0.3} gotta...{w=0.3} t-{w=0.1}think..."
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=1}{nw}"
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=5}{nw}"
    n 1kplpu "....."
    n 1kwdun "...H-{w=0.1}hello?{w=1}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b

    n 1fcsan "..."
    n 1kwmem "Hello...?"
    n 1kscem "A-{w=0.1}anybody?!{w=0.5} Please!{w=0.5} Hello?!"
    $ renpy.display_menu(items=[ ("I'm here, Natsuki.", True)], screen="choice_centred")
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
    python:
        # Name input
        renpy.display_menu(items=[ ("I'm...", True)], screen="choice_centred")
        persistent.playername = renpy.input("What is your name?", allow=(jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES+jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES), length=15)
        global player
        player = persistent.playername

    n 1kplun "..."
    n 1kplpu "...[player]?"
    n 1kwmss "You're...{w=0.3} [player]?"
    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    # Natsuki tries to get to grips with her new state
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
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
    $ renpy.display_menu(items=[ ("I brought you back.",True)], screen="choice_centred")
    n 1kskem "You...{w=1} you brought me back?{w=1}{nw}"
    extend 1kskwr " T-{w=0.3}to this?"
    n 1kllem "But this...{w=1}{nw}" 
    extend 1klrup " this is all...!{w=1}{nw}"
    $ renpy.display_menu(items=[ ("I want to help you.", True)], screen="choice_centred")
    n 1klleml "...!"
    n 1kllem "..."
    n 1kllun "..."
    n 1kcsem "...Look."
    n 1kcsfr "I...{w=2} I don't know what to do.{w=1}{nw}"
    extend 1kplsf " Nothing is making sense..."
    n 1kllpu "I don't even know what to believe anymore..."
    n 1kskaj "A-{w=0.3}and my friends...{w=1} t-{w=0.3}they're...{w=1}{nw}"
    extend 1kscem " they were never...!{w=1}{nw}"
    n 1kcsan "...{w=3}{nw}"
    n 1kcsful "...{w=3}{nw}"
    n 1kcsupl "...{w=3}{nw}"
    n 1kcsful "...{w=3}{nw}"
    n 1kcspul "...{w=3}{nw}"
    n 1kcssrl ".....{w=5}{nw}"
    n 1kwmsrl "...{w=5}{nw}"
    n 1kllsrl "...It..."
    n 1kwmpu "...It was [player]...{w=1} right?"
    n 1kllpu "..."
    n 1kwmsr "..."
    n 1kcssr "...I don't know where to go,{w=0.3} [player]."
    n 1kplun "I don't know what to {i}do{/i},{w=0.3} [player]..."
    n 1klrun "..."
    n 1kwmpu "...[player]?"
    $ renpy.display_menu(items=[ ("Yes, Natsuki?", True)], screen="choice_centred")
    n 1kslun "..."
    n 1kslpu "I...{w=0.3} I really need some time to figure things out."
    n 1kwmsr "..."
    n 1kplpul "Can you...{w=0.3} stay here?{w=0.2} W-{w=0.3}with me?{w=1}{nw}"
    extend 1flrunf " J-{w=0.1}just for a while!"
    n 1ksrunl "It's just...{w=1}{nw}"
    extend 1kplsr " I don't think I can be alone right now."
    n 1kllsr "You understand...{w=1.5}{nw}"
    extend 1kplpu " right?"

    jump introduction_outro

label introduction_outro:
    #TODO: Expand
    n "And now we're ready to spend forever together!"
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)
    
    stop music fadeout 3
    play music audio.just_natsuki_bgm
    $ config.allow_skipping = True
    show screen hkb_overlay
    jump ch30_loop
