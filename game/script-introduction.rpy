init 0 python in jn_introduction:
    from Enum import Enum
    import store

    class JNIntroductionStates(Enum):
        new_game = 0
        first_meeting = 1
        collecting_thoughts = 2
        complete = 3

        def __int__(self):
            return self.value

default persistent.jn_introduction_state = 0

label introduction_opening:
    scene black
    $ renpy.pause(5)

    # Restore attempt #1..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr.", True)], screen="choice_centred")
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a
    $ renpy.pause(5)

    # Restore attempt #2..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr.", True)], screen="choice_centred")
    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    $ renpy.pause(0.5)
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    $ renpy.pause(0.5)
    play audio glitch_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    $ renpy.pause(7)
    
    # Restore attempt #3..
    $ renpy.display_menu(items=[ ("Restore natsuki.chr.", True)], screen="choice_centred")
    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    $ renpy.pause(0.5)
    play audio glitch_b
    show glitch_garbled_b zorder 99 with vpunch
    $ renpy.pause(0.5)
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show glitch_fuzzy zorder 99
    play audio interference loop
    $ renpy.pause(10)

    # Restore finally works
    stop audio
    hide glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a
    jump introduction_first_meeting

label introduction_first_meeting:
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n "AAAAAaaaaAAAAHHH!"
    n "I'm super spooked and confused!"
    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    n "This is where I collect my thoughts..."
    jump introduction_outro

label introduction_outro:
    n "And now we're ready to spend forever together!"
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)
    jump ch30_loop
