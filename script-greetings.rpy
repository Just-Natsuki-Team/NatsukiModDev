default persistent._greeting_database = dict()

init python in greetings:
    GREETING_MAP = dict()

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_back",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_back:
    n "You're back, yay!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_hey",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_hey:
    n "Hey [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_hi_again",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_hi_again:
    n "Hi again!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_welcome_back",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_welcome_back:
    n "Hi! Welcome back!"
    return
