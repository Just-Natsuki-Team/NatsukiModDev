default persistent._topic_database = dict()

init python in topics:
    TOPIC_MAP = dict()

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="classroom_topic_example1",
            unlocked=True,
            location="classroom",
            affinity_range=(0, 50),
            trust_range=(0, 50)
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label classroom_topic_example1:
    n "classroom1"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="classroom_topic_example2",
            unlocked=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label classroom_topic_example2:
    n "Your affinity is: [persistent.affinity], and your trust is: [persistent.trust] <3"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example1",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label beach_topic_example1:
    n "beach1"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example2",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label beach_topic_example2:
    n "beach2"
    return

# Talk menu topics

# This topic allows us to (temporarily!) set a custom affinity value
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_affinity",
            unlocked=True,
            prompt="Can you change my affinity?",
            conditional=None,
            category=["Debug"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_affinity:
    n "Okaaay! Just tell me what affinity value you want!"
    python:
        affinity_to_set = renpy.input("Enter an affinity value (current: {0}):".format(persistent.affinity))
        try:
            persistent.affinity = float(affinity_to_set)
            renpy.say(n, "Done! Your new affinity is [persistent.affinity]!")

        except:
            renpy.say(n, "Huh... sorry, I didn't get that. Make sure you enter an integer or decimal value, alright?")
    return

# This topic allows us to (temporarily!) set a custom trust value
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_trust",
            unlocked=True,
            prompt="Can you change my trust?",
            conditional=None,
            category=["Debug"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_trust:
    n "Sure! Just tell me what trust value you want!"
    python:
        trust_to_set = renpy.input("Enter a trust value (current: {0}):".format(persistent.trust))
        try:
            persistent.trust = float(trust_to_set)
            renpy.say(n, "Alright! Your new trust is [persistent.trust]!")

        except:
            renpy.say(n, "Hmm... sorry, I can't seem to read that. Make sure you enter an integer or decimal value, 'kay?")
    return

# Natsuki's thoughts on having her picture taken via the ingame screenshot system
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_having_pictures_taken",
            unlocked=True,
            prompt="How do you feel about having your picture taken?",
            conditional=None,
            category=["Natsuki", "Photography", "Life"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_having_pictures_taken:
    if not persistent._jn_first_screenshot_taken:
        n "W-wait...{w=0.3} you're telling me there's a camera here?{w=0.2} Are you kidding me?!"
        n "Uuuu-"
        n "I've never liked having my picture taken without my permission..."
        n "Just...{w=0.3} please don't take any pictures of me unless I ask,{w=0.1} okay [player]?"
        n "It'd really mean a lot to me."
        n "I hope you can understand."

    else:
        if persistent.affinity >= 700:
            n "Hmm?{w=0.2} Pictures of me?"
            n "Honestly,{w=0.1} I don't think I'll ever be completely comfortable with them..."
            n "But I trust you to make a good shot!"
            n "As long as you ask,{w=0.1} I've got no problem with it!"

        elif persistent.affinity < 700 and persistent.affinity > 100:
            if player_screenshots_blocked:
                n "Really, [player]?{w=0.1} You're asking me about this {i}now{/i}?"
                n "You know {i}perfectly well{/i} how I feel about this."
                n "I don't hate you,{w=0.1} but please try to remember how I feel before you do stuff like that."
                return

            else:
                n "H-huh?{w=0.2} Pictures of me?"
                n "Not a fan,{w=0.1} honestly -{w=0.1} but you knew that much already,{w=0.1} [player]."
                n "It's just..."
                n "I really...{w=0.3} need...{w=0.3} my privacy.{w=0.1} It matters a lot to me."
                n "You understand,{w=0.1} right?"
                n "So please,{w=0.1} if you ever wanna take a picture,{w=0.1} can you ask me first?"
                menu:
                    "Of course!":
                        n "Thanks,{w=0.1} [player]."
                        n "That really...{w=0.3} means a lot to me."

                    "I'll think about it.":
                        n "[player]...{w=0.3} come on.{w=0.1} I'm being serious here."
                        n "Please don't mess me around with this."
                        n "Make sure you ask,{w=0.1} okay?"

                    "...":
                        n "..."
                        n "Uh...{w=0.3} [player]?{w=0.1} This isn't very funny."
                        n "Make sure you ask,{w=0.1} okay?{w=0.1} For my sake."

        elif persistent.affinity > -50:
            n "Pictures? Really?"
            n "I don't think I want to have you taking my picture,{w=0.1} [player]."
            n "Let's talk about something else."

        else:
            n "Please...{w=0.3} don't try to pretend like you care about how I feel about pictures."
            n "I'm done talking about this,{w=0.1} [player]."
    return

# Ask Natsuki for permission to take a picture of her, or have her call out the player if permission already given!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_get_picture_permission",
            unlocked=True,
            prompt="Can I take a picture of you?",
            conditional="persistent._jn_first_screenshot_taken != None",
            category=["You", "Photography"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_get_picture_permission:
    # The player was warned!
    if player_screenshots_blocked:
        n "Uh...{w=0.3} no,{w=0.1} I'm not turning the camera back on,{w=0.1} [player]."
        return

    if persistent.affinity >= 700:
        if player_screenshots_permission:
            n "Ahaha!{w=0.2} I already said you could,{w=0.1} dummy!"
            n "I'm ready,{w=0.1} so take one whenever!"

        else:
            n "Eh?{w=0.2} A picture?{w=0.2} Of course!"
            $ player_screenshots_permission = True
        return

    elif persistent.affinity >= 500:
        if player_screenshots_permission:
            n "Huh?{w=0.2} Didn't you ask me that already?"
            n "It's fine,{w=0.1} so go ahead!"

        else:
            n "Oh?{w=0.2} You wanna take a picture?{w=0.2} Alright!"
            $ player_screenshots_permission = True
        return

    elif persistent.affinity >= 300:
        if player_screenshots_permission:
            n "Hmm?{w=0.2} A picture?{w=0.2} Well,{w=0.1} okay."
            $ player_screenshots_permission = True

        else:
            n "Uuuu...{w=0.3} I just said you could,{w=0.1} [player]."
            n "Just take it whenever,{w=0.1} alright?"
        return

    elif persistent.affinity >= 100:
        if player_screenshots_permission:
            n "Eh?{w=0.2} I already said you could,{w=0.1} [player]. Just take it soon,{w=0.1} alright?"
            n "I don't really like being kept on hold like this..."

        else:
            # Indecisive; this lets lower affinity players have a chance at screenshots without upsetting Natsuki
            n "A picture?{w=0.2} I'm not sure...{w=0.3} let me think about it."
            n "..."
            # We take into account the player's behaviour with pictures so far
            $ natsuki_approves = random.randint(1, 100) <= ((100 - bad_screenshot_streak) * 25)
            if natsuki_approves:
                n "Fine,{w=0.1} I guess.{w=0.1} Take it whenever."
                $ player_screenshots_permission = True

            else:
                n "I'm sorry,{w=0.1} [player].{w=0.1} I don't want any pictures taking of me right now."
                $ player_screenshots_permission = False
        return

    elif persistent.affinity >= -50:
        n "No.{w=0.1} I {b}don't{/b} want my picture taken."
        $ player_screenshots_permission = False
        return

    else:
        n "..."
        $ player_screenshots_permission = False

    return

label menu_nevermind: #TODO: incorporate into _topic_database - not sure how to differentiate it from other talk topics
    n "Okay!"
    jump ch30_loop

#---------------date_menu_topics--------------------

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_beach",
            unlocked=True,
            prompt="Wanna go to the beach?",
            player_says=True,
            category=["date"] #I'm not sure if category is for this..
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_room",
            unlocked=True,
            prompt="Let's return",
            player_says=True,
            category=["date"] #I'm not sure if category is for this..
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_beach:
    n "I love the beach"
    n "Let's go!"
    $ main_background.changeLocation(beach)
    $ main_background.draw(full_redraw=True)
    show Natsuki zorder 3 #replace after sprite rework
    return

label date_go2_room:
    n "Heading back then?"
    n "Alright!"
    $ main_background.changeLocation(classroom)
    $ main_background.draw(dissolve_all=True, full_redraw=True)
    show Natsuki zorder 3 #replace after sprite rework
    return
