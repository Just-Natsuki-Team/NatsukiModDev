image draw1 = "mod_assets/scribblegame/1.png"
image draw2 = "mod_assets/scribblegame/2.png"
image draw3 = "mod_assets/scribblegame/3.png"

default hp = 20
default n_hp = 25
default hit = None
default n_hit = None
default persistent.first_fight = True
default persistent.first_code = True
default using_aimbot = False
default time_since_aimbot = 0
default using_anivirus = False
default time_since_antivirus = 0
default cleaner_uses = 3
default exiting_fight = False

label scribblegame:
    n jnb"So you want to play a drawing game?"
    n jhb "Okay."
    n "Let me draw something..."
    $ scribble = renpy.random.randint(1, 3)
    if scribble == 1:
        play sound page_turn
        show draw1 with Dissolve(1)
        $ draw1 = "knife"
        $ draw1entry = renpy.input ("What did I just draw?", "")
        if draw1entry == draw1:
             n "That's right! Good job!"
        else:
             n "Nope!"
        hide draw1 Dissolve(1)
    elif scribble == 2:
        play sound page_turn
        show draw2 with Dissolve(1)
        $ draw2 = "book"
        $ draw2entry = renpy.input ("What did I just draw?", "")
        if draw2entry == draw2:
             n "That's right! Good job!"
        else:
             n "Nope!"
        hide draw2 with Dissolve(1)
    elif scribble == 3:
        play sound page_turn
        show draw3 with Dissolve(1)
        $ draw3 = "blood"
        $ draw3entry = renpy.input ("What did I just draw?", "")
        if draw3entry == draw3:
             n "That's right! Good job!"
        else:
             n "Nope!"
        hide draw3 with Dissolve(1)
    n "That was really fun!"
    jump ch30_loop

label startfight:
    n jnb "Y-you want to fight me?"
    n jad "You are going down!"
    if persistent.first_fight:
        call screen dialog("The music for the battle can be changed in \"custom-music\"\nin the Just Natsuki directory.", ok_action=Return)
        $ persistent.first_fight = False
    $ time_since_aimbot == 0
    $ hp = 20
    $ n_hp = 22
    play music battle
    jump fight_loop

label fight_loop:
    $ config.overlay_screens = []
    hide screen hkb_overlay
    show screen fight
    show natsuki jha_idle zorder 2
    if hp <= 1:
        hide screen fight
        n "You loose [player]!"
        n "Ahaha!"
        $ time_since_aimbot == 0
        $ exiting_fight = True
        jump ch30_autoload
    if n_hp <= 1:
        hide screen fight
        n jaa "Ow ow! Stop!"
        n "You win okay!"
        $ time_since_aimbot == 0
        $ exiting_fight = True
        jump ch30_autoload
    if time_since_aimbot != 0:
        $ time_since_aimbot -= 1
    if time_since_antivirus != 0:
        $ time_since_antivirus -= 1
    $ dialog = renpy.random.randint(0, 4)
    if dialog == 0:
        "Natsuki looks at you with confidence!"
    elif dialog == 1:
        "Natsuki smirks."
    elif dialog == 2:
        "You feel like you should roll for initiative."
    elif dialog == 3:
        "Natsuki reaches for a dye."
    elif dialog == 4:
        "Natsuki sticks out her tongue at you."
    window hide
    pause 1000.0
    jump fight_loop

label fight:
    menu:
        "Boop":
            hide screen fight
            "You boop Natsuki!"
            jump attack
        "Yell":
            hide screen fight
            "You yell at Natsuki."
            "Nothing happened."
            jump n_attack

label attack:
    hide screen fight
    if using_aimbot:
        $ hit = 10
    else:
        $ hit = renpy.random.randint(1, 20)
    if hit >= 10:
        if using_aimbot:
            $ dmg = renpy.random.randint(5, 10)
            $ using_aimbot = False
        else:
            $ dmg = renpy.random.randint(2, 4)
        $ n_hp -= dmg
        "You dealt [dmg] damage!"
        "Natsuki is now at [n_hp] HP!"
    elif hit <= 10:
        "You miss!"
        n "Ahaha!"
    if hp <= 1:
        hide screen fight
        n "You loose [player]!"
        n "Ahaha!"
        $ time_since_aimbot == 0
        $ exiting_fight = True
        jump ch30_autoload
    if n_hp <= 1:
        hide screen fight
        n jaa "Ow ow! Stop!"
        n "You win okay!"
        $ exiting_fight = True
        $ time_since_aimbot == 0
        jump ch30_autoload

label n_attack:
    hide screen fight
    n "You are going down!"
    $ hit = renpy.random.randint(1, 20)
    if hit >= 15:
        $ n_dmg = renpy.random.randint(5, 8)
        show natsuki jha zorder 2
        "Natsuki strikes!"
        if using_anivirus:
            "Natsuki's attack is absorbed by the antivirus!"
            $ using_anivirus = False
        else:
            "Natsuki deals [n_dmg] damage!"
            $ hp -= n_dmg
        jump fight_loop
    else:
        "Natsuki misses!"
        n "No!"
        jump fight_loop

label act:
    menu:
        "Check":
            hide screen fight
            "Natsuki 3 ATK 0 DEF\nA feisty tsundere who just wants to read manga."
            n "You bet!"
            jump n_attack
        "Talk":
            hide screen fight
            n "Didn't you say we should fight?!"
            jump n_attack

label codes:
    if persistent.first_code:
        n jnb "Oh!"
        n "[player], this is the new CODEs option!"
        n "These codes can do a variety of things!"
        n "They have a cooldown that lasts multiple turns!"
        n "Some heal you!"
        n "Those are not a free action and will mean you don't get to attack!"
        n "Be careful though."
        n "You can only use it twice!"
        n "Usually you would have to find them but I just added them all here."
        n "You may want to use them as I'm going to start going much harder on you!"
        n "Have fun using them!"
        $ persistent.first_code = False
    menu:
        "Aimbot\n+DAMAGE +ACCURACY\n4 TURN COOLDOWN" if time_since_aimbot == 0:
            $ using_aimbot = True
            "You activate AIMBOT!"
            # This has to be 5 because the game will remove a count for the turn right after making it look like you had a 3 turn cooldown. 
            $ time_since_aimbot = 5
            "Your DAMAGE increased!"
            "Your ACCURACY was maxed out!"
            jump attack
        "Aimbot\n+DAMAGE +ACCURACY\n4 TURN COOLDOWN" if time_since_aimbot != 0:
            "Aimbot is still recharging!"
            if time_since_aimbot == 1:
                "Wait 1 more turn!"
            else:
                "Wait [time_since_aimbot] more turns!"
            jump attack
        "Antivirus\n+DEFENSE\n3 TURN COOLDOWN" if time_since_antivirus == 0:
            $ using_anivirus = True
            "You activate antivirus!"
            $ time_since_antivirus = 4
            "Your DEFENSE was maxed out!"
            jump attack
        "Antivirus\n+DEFENSE\n3 TURN COOLDOWN" if time_since_antivirus != 0:
            "Antivirus is still recharging!"
            if time_since_antivirus == 1:
                "Wait 1 more turn!"
            else:
                "Wait [time_since_antivirus] more turns!"
            jump attack
        "Computer cleaner\n+5 HP\nNO COOLDOWN\n3 USES" if cleaner_uses != 0:
            "You clean you hard drive!"
            $ hp += 5
            $ cleaner_uses -= 1
            if hp == 20:
                "Your HP was maxed out!"
            else:
                "You recovered 5 HP!"
            jump n_attack
    jump n_attack

label mercy:
    hide screen fight
    n jnb "Given up yet?"
    n jhc "Ahaha!"
    n "I win!"
    $ time_since_aimbot == 0
    jump ch30_autoload