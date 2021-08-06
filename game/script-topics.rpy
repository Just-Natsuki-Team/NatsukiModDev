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
    registerTopic(
        Topic(
            persistent._topic_database,
            label="classroom_topic_example2",
            unlocked=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example1",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example2",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )


label classroom_topic_example1:
    n "classroom1"
    return

label classroom_topic_example2:
    n "This is your affinity :)  :[persistent.affinity]"
    return

label beach_topic_example1:
    n "beach1"
    return

label beach_topic_example2:
    n "beach2"
    return

#---------------talk_menu_topics--------------------

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="Affinity_trust_dependant_topic",
            unlocked=True,
            prompt="test",
            player_says=True,
            affinity_range=(5, 90),
            trust_range=(60, 70),
            location="classroom",
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_trust_increase",
            unlocked=True,
            prompt="pls increase my trust <3",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_affinity_increase",
            unlocked=True,
            prompt="pls increase my affinity <3",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    # Display the screenshot date
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_first_picture",
            unlocked=True,
            prompt="When did I first take a picture of you?",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    # Discuss how Natsuki feels about screenshots
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_screenshots",
            unlocked=False,
            prompt="How do you feel about me taking screenshots?",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    # Discuss how Natsuki feels about screenshots
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_get_screenshot_permission",
            unlocked=False,
            prompt="Would you mind if I took some screenshots?",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label Affinity_trust_dependant_topic:
    n "you needed specific trust and affinity to show this, and you did it!"
    return

label talk_trust_increase:
    n "I trust you this much: [persistent.trust]"
    $ relationship("trust+")
    return

label talk_affinity_increase:
    n "I like you this much: [persistent.affinity]"
    $ relationship("affinity+")
    return

# Screenshot info; not permanent
label talk_first_picture:
    if persistent._jn_first_screenshot_taken == None:
        n "W-wait... you're telling me there's a camera here? Are you kidding me?!"
        n "Uuuu-"
        n "I've never liked having my picture taken without my permission..."
        n "Just... please don't take any pictures of me unless I ask, okay [player]?"
        n "It'd really mean a lot to me."
        n "I hope you can understand."
    else:
        n "Huh? When was my first picture taken? Let me think..."
        python:
            date_prefix = "A prefix"
            first_taken_date = persistent._jn_first_screenshot_taken.strftime(r"%B %d, %Y")
        n "Aha! I had my first picture taken on [first_taken_date]"
        if persistent._jn_screenshot_good_shots_total != None and persistent._jn_screenshot_bad_shots_total != None:
            n "Oooh! Let me check my album too..."
            $ total_pictures = persistent._jn_screenshot_good_shots_total + persistent._jn_screenshot_bad_shots_total
            n "I've got a few pictures, about [total_pictures] in all!"
    return

# Natsuki on screenshots topic; unlocked by taking the first screenshot.
# Should branch further based on metrics under definitions.
# WIP - need to tie this to screenshots.rpy!
label talk_screenshots:
    n "H-huh? Screenshots?"
    n "Not a fan, honestly - but you knew that much already, [player]."
    n "It's just..."
    n "I really... need... my privacy. It means a lot to me."
    n "You understand, right?"
    return

# Ask Natsuki for screenshot permissions for the current session; her response will vary based on the player's relationship state.
label talk_get_screenshot_permission:
    # TODO - Minimum affinity/trust branch

    # TODO - Low affinity/trust branch

    # TODO - Medium affinity/trust branch

    # TODO - High affinity/trust branch

    # TODO - Maximum affinity/trust branch
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