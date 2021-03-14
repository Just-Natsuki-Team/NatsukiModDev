default persistent._talk_database = dict()

init python in talk_topics:
    import random
    TALK_MAP = dict()

    def get_unlocked():
        """
        returns all unlocked topics
        """
        unlocked_topics = []
        for topic in TALK_MAP.values():
            if topic.unlocked:
                unlocked_topics.append(topic)

        return unlocked_topics


init 5 python:
    registerTopic(
        Topic(
            persistent._talk_database,
            label="talk_how_are_you",
            unlocked=True,
            prompt = "How are you today?"
        ),
        topic_group=TOPIC_TYPE_TALK
    )

    registerTopic(
        Topic(
            persistent._talk_database,
            label="talk_cupcakes",
            unlocked=True,
            prompt = "Do you like cupcakes?"
        ),
        topic_group=TOPIC_TYPE_TALK
    )

    registerTopic(
        Topic(
            persistent._talk_database,
            label="talk_not_unlocked_test",
            unlocked=False,
            prompt = "This is not unlocked"
        ),
        topic_group=TOPIC_TYPE_TALK
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
