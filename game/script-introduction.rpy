init 0 python in jn_introduction:
    from Enum import Enum
    import random
    import store

    class JNIntroductionStates(Enum):
        new_game = 0
        first_meeting = 1
        collecting_thoughts = 2
        complete = 3

        def __int__(self):
            return self.value

default persistent.jn_introduction_state = 0

#TODO: Handling for player quit-out during the introduction sequence

label introduction_opening:
    $ allow_skipping = False
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
    show glitch_garbled_a zorder 99 with vpunch
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
    show glitch_garbled_b zorder 99 with vpunch
    $ renpy.pause(0.5)

    if random.randint(0,10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with vpunch
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
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 1uscsc "AAAAAaaaaAAAAHHH!"
    n 1uskwr "S-{w=0.1}somebody!{w=0.5} ANYBODY?!{w=0.5} HELP!{w=0.5}{nw}" 
    extend 1fbkwr " HELP ME!!"
    n 1uscem "Y-{w=0.1}Yuri,{w=0.1} she's..."
    n 1ullem "S-{w=0.1}she's..." 
    n 1uskem "...H-{w=0.1}huh?"
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
    n 1kcsfu "Nnnnnnnnghhhh..."
    n 1kcsan "I-{w=0.3}it hurts...{w=0.5}{nw}"
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
    n 1kscem "A-anybody?!{w=0.5} Please!{w=0.5} Hello?!"

    #TODO: Ask for name, etc

    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    n "This is where I collect my thoughts..."
    jump introduction_outro

label introduction_outro:
    n "And now we're ready to spend forever together!"
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)
    
    stop music fadeout 3
    play music audio.test_bgm
    $ allow_skipping = True
    show screen hkb_overlay
    jump ch30_loop
