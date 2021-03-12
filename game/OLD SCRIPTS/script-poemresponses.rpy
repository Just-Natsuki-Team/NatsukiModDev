label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "Whom should I show my poem to first?"
        else:
            $ menutext = "Whom should I show my poem to next?"

        menu:
            "[menutext]"

            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Time to show Natsuki!"
                call poemresponse_natsuki
    return


    $ n_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori:
    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene
    return

label poemresponse_natsuki:
    scene bg club_day
    hide screen hkb_overlay
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse_yuri:
    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene
    return

label poemresponse_monika:
    scene bg club_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene
    return

label ch0_n_end:
    hide screen hkb_overlay
    $ poem = renpy.random.randint(1,4)
    if poem == 1:
        call showpoem (poem_n1, img="natsuki 2s")
    if poem == 2:
        call showpoem (poem_n2, img="natsuki 2s")
    if poem == 3:
        call showpoem (poem_n3, img="natsuki 2s")
    if poem == 4:
        call showpoem (poem_n3b, img="natsuki 2s")
    n "What did you think?"
    menu:
        "Very nice!":
            n 1l "Thanks!"
            n 1z "Ehehe!"
        "It could use some work...":
            n 1k "Hmm..."
    return

label ch0_n_bad:
    hide screen hkb_overlay
    n "It's definitely fancy..."
    n "Very fancy words..."
    n "I think Yuri would like it..."
    n "Anyway..."
    n "Here you can read mine!"
    return

label ch0_n_med:
    hide screen hkb_overlay
    n "Hmmm..."
    n "It's interesting..."
    n "It's cute, and fancy!"
    n "Best of both worlds I guess!"
    $ persistent.natsuki_like += 3
    return

label ch0_n_good:
    hide screen hkb_overlay
    n "Awesome!"
    n "It's very much like my own poems!"
    n "I like it!"
    n "Here take a look at mine!"
    $ persistent.natsuki_like += 5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
