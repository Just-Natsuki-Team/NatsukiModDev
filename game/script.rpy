label start:
    python:
        #We'll keep track of the chapter we're on for poem response logic and other stuff
        chapter = 0

        #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
        _dismiss_pause = config.developer

        #Each of the girls' names before the MC learns their name throughout ch0.
        s_name = "Sayori"
        m_name = "Monika"
        n_name = "Natsuki"
        y_name = "Yuri"

        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False

    jump ch30_autoload


label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
