label start_main:
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    $ delete_character("sayori")
    play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k at t11 zorder 2
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    n 1m "...huh..."
    n "That's gross..."
    n 1l "Don't worry!"
    n "I got it."
    call updateconsole("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    call updateconsole("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")
    n "I'm almost done!"
    n "Let me just grab a cupcake real quick!"
    "Natsuki lifts the foil from her tray and takes a cupcake."
    n "Seriously these are the best!"
    n "I just had to have one since this is the last time I'll be able to."
    n "You know, Before they stop existing and everything."
    n "But anyway... I shoudn't keep stealing Monika's lines anymore."
    n "Gimmie a sec."
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    jump ch30_main
    $ renpy.utter_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc