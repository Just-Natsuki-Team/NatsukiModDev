#Finally the first DLC!

default persistent.seen_kitchenintro = False
default persistent.has_supplies = False

label chkitchen_start:
    if persistent.seen_kitchenintro == False:
        n jnb "So you want to go to the kitchen?"
        n "Alright then!"
        hide n2
        hide shade
        hide red
        hide blonde
        hide lime
        hide skyblue
        show natsuki 1l at t11 zorder 5
        n "It's just over here!"
        show natsuki at lhide
        hide natsuki
        show kitchenoverlay zorder 3
        show natsuki 1l at t11 zorder 5
        n "Here we are!"
        n "Let me just change into something more comfortable!"
        window hide
        pause 0.5
        show natsuki 3bl at t11
        pause 0.5
        n "Alright!"
        play music t6
        n "Now, I'd better explain how all this works eh?"
        n "Alright, So here we can cook different foods!"
        n "Maybe a cupcake?"
        n "Or whatever you want."
        n "You could mix your own ingredients to make some unique foods!"
        n "Not sure how good they'll taste..."
        n "Also, if you have to close the game, I'll set everything back up the way we had it."
        n "Alright, let's get to it!"
    else:
        n jnb "Wanna go and cook then?"
        n jha "Alright, let's go!"
        hide n2
        hide shade
        hide red
        hide blonde
        hide lime
        hide skyblue
        show kitchenoverlay zorder 3
        show natsuki 1ba at t11 zorder 5
        n "Here we are!"
    $ persistent.autoload = "chkitchen_autoload"

label chkitchen_loop:
    pause 30.0
    jump chkitchen_loop

label chkitchen_autoload:
    python:
        today = datetime.date.today()      
        day = datetime.date.today().strftime("%A")
        month = datetime.date.today().strftime("%B")
        date = datetime.date.today().strftime("%d")
        year = datetime.date.today().strftime("%Y")
        now = datetime.datetime.now()
        current_time = datetime.datetime.now().time().hour
    call showroom
    n jnb "Oh, you're here!"
    n "One second..."
    hide n2
    hide shade
    hide red
    hide blonde
    hide lime
    hide skyblue
    show kitchenoverlay zorder 3
    show natsuki 1ba at t11 zorder 5
    n 1bl "There!"
    jump chkitchen_loop

label kitchentalkmenu:
    $ allow_dialogue = False
    n 1bk "What's up?"
    menu:
        "Let's go back to the room.":
            n "Alright."
            $ persistent.autoload = "ch30_autoload"
            $ exiting_fight = True
            jump ch30_autoload
    