default persistent._greeting_database = dict()

init python in greetings:
    import random
    import store

    GREETING_MAP = dict()

    def select_greeting():
        """
        Picks a random greeting, accounting for affinity
        """
        # Get the farewells the current affinity allows for us
        #TODO: Generalized filter function
        return random.choice(
            filter(lambda x: x.evaluate_affinity_range(), GREETING_MAP.values())
        ).label

init 1 python:
    # DEBUG: TODO: Remove this eventually
    # Kill off old greetings
    try:
        store.persistent._greeting_database.pop("greeting_back")
        store.persistent._greeting_database.pop("greeting_hey")
        store.persistent._greeting_database.pop("greeting_hi_again")
        store.persistent._greeting_database.pop("greeting_welcome_back")

        # Resets - remove these later, once we're done tweaking affinity/trust!
        store.persistent._greeting_database.pop("greeting_love_plus_1")
        store.persistent._greeting_database.pop("greeting_love_plus_2")
        store.persistent._greeting_database.pop("greeting_love_plus_3")
        store.persistent._greeting_database.pop("greeting_love_plus_4")
        store.persistent._greeting_database.pop("greeting_love_plus_5")

        store.persistent._greeting_database.pop("greeting_affectionate_enamored_aff_1")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_aff_2")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_aff_3")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_aff_4")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_aff_5")

        store.persistent._greeting_database.pop("greeting_normal_happy_aff_1")
        store.persistent._greeting_database.pop("greeting_normal_happy_aff_2")
        store.persistent._greeting_database.pop("greeting_normal_happy_aff_3")
        store.persistent._greeting_database.pop("greeting_normal_happy_aff_4")
        store.persistent._greeting_database.pop("greeting_normal_happy_aff_5")

        store.persistent._greeting_database.pop("greeting_distressed_upset_1")
        store.persistent._greeting_database.pop("greeting_distressed_upset_2")
        store.persistent._greeting_database.pop("greeting_distressed_upset_3")
        store.persistent._greeting_database.pop("greeting_distressed_upset_4")
        store.persistent._greeting_database.pop("greeting_distressed_upset_5")

        store.persistent._greeting_database.pop("greeting_broken_minus_1")
        store.persistent._greeting_database.pop("greeting_broken_minus_2")
        store.persistent._greeting_database.pop("greeting_broken_minus_3")
        store.persistent._greeting_database.pop("greeting_broken_minus_4")
        store.persistent._greeting_database.pop("greeting_broken_minus_5")

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

# LOVE+ greetings
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_1",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_1:
    n "[player]!{w=0.2} You're back,{w=0.1} finally!"
    n "Ehehe.{w=0.2} Now I {i}know{/i} today's gonna be great!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_2",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_2:
    n "[player]!{w=0.1} What took you so long?{w=0.2} Jeez!"
    n "You think my entire world revolves around you or something?"
    n "..." # amger when sprites are in, not a dupe!
    n "..." # smug when sprites are in, not a dupe!
    n "Ahaha!{w=0.2} Did I get you,{w=0.1} [player]?{w=0.2} Don't lie!"
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Well, anyway.{w=0.2} You're here now, [chosen_endearment]!{w=0.2} Welcome back!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_3",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_3:
    n "[player]!{w=0.2} [player] [player] [player]!"
    n "I'm so glad to see you again!{w=0.2} Welcome back!"
    n "Let's make today amazing too,{w=0.1} alright?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_4",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_4:
    n "[player],{w=0.1} you're back!"
    n "I was really starting to miss you, you know..."
    n "Don't keep me waiting so long next time,{w=0.2} alright?"
    n "You're always welcome here,{w=0.2} after all..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_5",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_5:
    n "..."
    n "..."
    n "..."
    $ player_initial = list(player)[0]
    n "[player_initial]-[player]!{w=0.2} When did you get here?!"
    n "I-I was...!{w=0.2} I was just...!"
    n "..."
    n "I missed you,{w=0.1} [player].{w=0.2} Ahaha..."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "But I know everything's gonna be okay now you're here,{w=0.1} [chosen_endearment]."
    return

# AFFECTIONATE/ENAMORED greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_aff_1",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_aff_1:
    n "[player]!{w=0.2} You're back!"
    n "It's so good to see you again!"
    n "Let's make today amazing as well,{w=0.1} 'kay? Ehehe."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_aff_2",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_aff_2:
    n "Hey,{w=0.1} you!{w=0.2} Back so soon?"
    n "I knew you couldn't resist.{w=0.2} Ehehe."
    n "What do you wanna do today?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_aff_3",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_aff_3:
    n "Well, well, well.{w=0.2} What do we have here?"
    n "You just can't stay away from me,{w=0.1} can you?{w=0.2} Ahaha!"
    n "Not that I'm complaining too much!"
    n "So...{w=0.3} what do you wanna talk about?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_aff_4",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_aff_4:
    n "It's [player],{w=0.1} yay!"
    n "We're gonna have so much fun today!{w=0.2} Ehehe."
    n "So,{w=0.1} what do you wanna talk about?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_aff_5",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_aff_5:
    n "[player], you're back!"
    n "I've been waiting for you, you know..."
    n "But now that you're here, everything is fine! Ehehe."
    return

# NORMAL/HAPPY greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_aff_1",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_aff_1:
    n "Oh!{w=0.2} Hey,{w=0.1} [player]!"
    n "What's up?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_aff_2",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_aff_2:
    n "Hi,{w=0.1} [player]!"
    n "I'm glad to see you again."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_aff_3",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_aff_3:
    n "..."
    n "Huh?"
    n "Oh!{w=0.2} Hi,{w=0.1} [player]!"
    n "Sorry,{w=0.1} I was spacing out a little.{w=0.2} Ehehe."
    n "So...{w=0.3} what's new?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_aff_4",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_aff_4:
    n "Heya,{w=0.1} [player]!"
    n "Welcome back!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_aff_5",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_aff_5:
    n "It's [player]!{w=0.2} Hi!"
    n "I-I knew you'd be back,{w=0.1} obviously."
    n "You'd have to have no taste to not visit again! Ahaha!"
    return

# DISTRESSED/UPSET greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_1",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_1:
    n "Oh.{w=0.2} It's you."
    n "Hello,{w=0.1} [player]."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_2",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_2:
    n "[player].{w=0.2} Hi."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_3",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_3:
    n "[player].{w=0.2} Welcome back,{w=0.1} I guess."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_4",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_4:
    n "Hi,{w=0.1} [player]."
    n "This better be good."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_5",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_5:
    n "Oh?{w=0.2} You came back?"
    n "...I wish I could say I was happy about it."
    return

# BROKEN- greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_1",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_1:
    n "...?"
    n "Oh...{w=0.3} it's you."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_2",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_2:
    n "..."
    n "..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_3",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_3:
    n "...Why?"
    n "Why did you come back,{w=0.1} [player]?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_4",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_4:
    $ player_initial = list(player)[0]
    n "[player_initial]-{w=0.1}[player]...?"
    n "As if I didn't have enough on my mind..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_5",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_5:
    $ player_initial = list(player)[0]
    n "...Why, [player]?{w=0.2} Why do you keep coming back?"
    n "Why can't you just leave me be..."
    return
