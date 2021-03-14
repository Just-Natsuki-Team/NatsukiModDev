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