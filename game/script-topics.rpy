default persistent._topic_database = dict()

init python in topics:
    TOPIC_MAP = dict()

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="clubroom_topic_example1",
            unlocked=True,
            location="clubroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
    registerTopic(
        Topic(
            persistent._topic_database,
            label="clubroom_topic_example2",
            unlocked=True,
            location="clubroom"
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


label clubroom_topic_example1:
    n "example1"
    return

label clubroom_topic_example2:
    n "example2"
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
            label="talk_how_are_you",
            unlocked=True,
            prompt="How are you today?",
            player_says=True,
            location="clubroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_cupcakes",
            unlocked=True,
            prompt="Do you like cupcakes?",
            player_says=True,
            location="clubroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_are_you:
    n "Pretty good!"
    return

label talk_cupcakes:
    n "I love them!"
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
    $ persistent._current_location = "beach"
    n "(we are now at the beach)" #TODO:incorporate with location()
    return

label date_go2_room:
    n "Heading back then?"
    n "Alright!"
    $ persistent._current_location = "clubroom"
    n "(we are now in the clubroom)" #TODO:incorporate with location()
    return