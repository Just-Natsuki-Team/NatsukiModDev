default persistent._topic_database = dict()

init python in topics:
    TOPIC_MAP = dict()

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="topic_example1",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
    registerTopic(
        Topic(
            persistent._topic_database,
            label="topic_example2",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )


label topic_example1:
    n "example1"
    return

label topic_example2:
    n "example2"
    return

#---------------talk_menu_topics--------------------

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_are_you",
            unlocked=True,
            prompt="How are you today?",
            player_says=True
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_cupcakes",
            unlocked=True,
            prompt="Do you like cupcakes?",
            player_says=True
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_not_unlocked_test",
            unlocked=False,
            prompt="This is not unlocked",
            player_says=True
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )



label talk_how_are_you:
    n "Pretty good!"
    return

label talk_cupcakes:
    n "I love them!"
    return

label talk_not_unlocked_test:
    n "this topic isn't unlocked yet"
    return

label menu_nevermind: #TODO: incorporate into _topic_database - not sure how to differentiate it from other talk topics
    n "Okay!"
    jump ch30_loop