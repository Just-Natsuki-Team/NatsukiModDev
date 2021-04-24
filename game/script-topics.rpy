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
            label="talk_how_are_you",
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
            label="talk_cupcakes",
            unlocked=True,
            prompt="pls increase my affinity <3",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label Affinity_trust_dependant_topic:
    n "you needed specific trust and affinity to show this, and you did it!"
    return

label talk_how_are_you:
    n "I trust you this much: [persistent.trust]"
    $ trust_increase()
    return

label talk_cupcakes:
    n "I like you this much: [persistent.afffinity]"
    $ x = renpy.list_files()
    $ affinity_increase()
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