default persistent._admission_database = dict()

init python in admissions:
    import random
    import store

    ADMISSION_MAP = dict()

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        store.persistent._greeting_database.pop("admission_angry")
        store.persistent._greeting_database.pop("admission_anxious")
        store.persistent._greeting_database.pop("admission_ashamed")
        store.persistent._greeting_database.pop("admission_confident")
        store.persistent._greeting_database.pop("admission_excited")
        store.persistent._greeting_database.pop("admission_happy")
        store.persistent._greeting_database.pop("admission_hungry")
        store.persistent._greeting_database.pop("admission_insecure")
        store.persistent._greeting_database.pop("admission_proud")
        store.persistent._greeting_database.pop("admission_sad")
        store.persistent._greeting_database.pop("admission_sick")
        store.persistent._greeting_database.pop("admission_tired")

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_angry",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_angry:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_anxious",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_anxious:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_ashamed",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_ashamed:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_confident",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_confident:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_excited",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_excited:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_happy",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_happy:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_hungry",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_hungry:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_insecure",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_insecure:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_proud",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_proud:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_sad",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sad:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_sick",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sick:
    n ""
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            label="admission_tired",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_tired:
    n ""
    return
