default persistent._admission_database = dict()

init 0 python in admissions:
    import random
    import store

    ADMISSION_MAP = dict()

    # Admission types
    ADMISSION_TYPE_ANGRY = 0
    ADMISSION_TYPE_ANXIOUS = 1
    ADMISSION_TYPE_ASHAMED = 2
    ADMISSION_TYPE_CONFIDENT = 3
    ADMISSION_TYPE_EXCITED = 4
    ADMISSION_TYPE_HAPPY = 5
    ADMISSION_TYPE_HUNGRY = 6
    ADMISSION_TYPE_INSECURE = 7
    ADMISSION_TYPE_PROUD = 8
    ADMISSION_TYPE_SAD = 9
    ADMISSION_TYPE_SICK = 10
    ADMISSION_TYPE_TIRED = 11

    # The last admission the player gave to Natsuki
    _last_admission_type = None

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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_ANGRY
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_ANXIOUS
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_ASHAMED
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_CONFIDENT
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
    if admissions._last_admission_type == admissions.ADMISSION_TYPE_EXCITED:
        n "Still pumped up,{w=0.1} are we [player]?"
        n "I bet you just can't wait,{w=0.1} huh?{w=0.2} Ehehe."

    else:
        n "Oh?{w=0.2} Did something happen?{w=0.2} Is something {i}gonna{/i} happen?"
        n "Whatever it is,{w=0.1} I'm happy to hear you're looking forward to it!"
        n "It's always awesome to have something you can get excited over, right?"

    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_EXCITED
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
    if admissions._last_admission_type == admissions.ADMISSION_TYPE_HAPPY:
        n "Wow...{w=0.3} it's all sunshine and rainbows for you today,{w=0.1} isn't it?"
        n "Ahaha!"
        n "Keep on smiling,{w=0.1} [player]!"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "Feeling better now,{w=0.1} [player]?"
        n "I'm glad to hear it!{w=0.2} That's...{w=0.3} honestly a relief,{w=0.1} ahaha..."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
            n "..."
            n "So...{w=0.3} where were we?"

        else:
            n "..."
            n "Jeez...{w=0.3} if you're okay,{w=0.1} then let's get back to it already!"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "Feeling better,{w=0.1} [player]?{w=0.2} I'm not surprised!"
        n "You just aren't yourself when you're hungry.{w=0.2} Ehehe."
        n "Trust me...{w=0.3} I would know."

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_SICK:
        n "Feeling better,{w=0.1} [player]?{w=0.2} I'm glad to hear it!"
        n "Nothing makes you appreciate feeling normal more than being sick,{w=0.1} right?"

    else:
        n "Oh?{w=0.1} Someone's in a good mood today!"
        n "Well,{w=0.1} I'm glad to hear it!"
        n "If you're happy,{w=0.1} I'm happy!"

    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_HAPPY
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
    if admissions._last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "What?{w=0.1} You're still hungry?"
        n "Or did you not get something when I told you to earlier?"
        n "Well...{w=0.3} either way,{w=0.1} get off your butt and go get something then!"
        n "Jeez,{w=0.1} [player]...{w=0.3} I'm not your babysitter!"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "As much as you probably wish I was,{w=0.1} right?{w=0.2} Ahaha!"
            n "Now get going already!{w=0.2} Bon appetit,{w=0.1} [player]!"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "[player]...{w=0.3} you told me you were sad earier."
        n "I don't mind if you're hungry,{w=0.1} but try not to comfort-eat,{w=0.1} okay?"
        n "You might feel a little better...{w=0.3} but it won't fix what made you sad."
        n "Try to enjoy your meal,{w=0.1} alright?"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
            n "I'm here for you if you need me,{w=0.1} [player]."

    else:
        n "Huh?{w=0.1} You're hungry?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n "Then what're you telling me for?{w=0.2} Go get something to eat,{w=0.1} [chosen_tease]!"
        n "Honestly...{w=0.3} what am I going to do with you,{w=0.1} [player]?{w=0.2} Ehehe."
        n "Now go make something already!{w=0.2} Just don't fill up on junk food!"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "I want you fighting fit for when we hang out,{w=0.1} 'kay?"
            n "We're gonna have so much to do together,{w=0.1} after all!"

    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_HUNGRY
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_INSECURE
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_PROUD
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_SAD
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
    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_SICK
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
    # TODO - Link in w/ farewells to have Nat force closure
    if admissions._last_admission_type == admissions.ADMISSION_TYPE_TIRED:
        n "Huh?{w=0.2} You're still tired?"
        n "Did you not get any rest,{w=0.1} [player]?"
        n "I don't want you getting all cranky..."
        n "So...{w=0.3} go back to bed, alright?"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_ANGRY or admissions._last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "You said you weren't happy earlier,{w=0.1} [player]..."
        n "If you're already tired,{w=0.1} I think you should sleep on it."
        n "You'll feel better,{w=0.1} alright?{w=0.2} I promise!"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_SICK:
        n "I'm really not surprised if you're already sick,{w=0.1} [player]."
        n "You should really go get some rest."
        n "We can talk later,{w=0.1} alright?"

    elif admissions._last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "I'm not surprised you're feeling tired if you're hungry!"
        n "Stop sitting around and go eat something,{w=0.1} [player]."
        n "Just take it easy getting up,{w=0.1} alright?{w=0.2} I don't want you fainting on me."
        n "And trust me,{w=0.1} I don't think you want that either..."

    else:
        n "Feeling tired,{w=0.1} [player]?"
        n "Perhaps you should think about turning in soon{w=0.1} -{w=0.1} even if it's just a nap!"
        n "Don't worry about me if you need to rest!{w=0.2} I'll be alright."
        n "Just make sure you let me know when you decide to go, [player]."

    $ admissions._last_admission_type = admissions.ADMISSION_TYPE_TIRED
    return
