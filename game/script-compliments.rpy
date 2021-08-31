default persistent._compliment_database = dict()

init 0 python in compliments:
    import random
    import store

    COMPLIMENT_MAP = dict()

    # Compliment types
    COMPLIMENT_TYPE_AMAZING = 0
    COMPLIMENT_TYPE_BEAUTIFUL = 1
    COMPLIMENT_TYPE_CONFIDENT = 2
    COMPLIMENT_TYPE_CUTE = 3
    COMPLIMENT_TYPE_HILARIOUS = 4
    COMPLIMENT_TYPE_INSPIRATIONAL = 5
    COMPLIMENT_TYPE_STYLE = 6
    COMPLIMENT_TYPE_THOUGHTFUL = 7

    # The last compliment the player gave to Natsuki
    last_compliment_type = None

    def get_all_compliments():
        """
        Gets all compliment topics which are available

        OUT:
            List<Topic> of compliments which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            COMPLIMENT_MAP.values(),
            affinity=store.jn_globals.current_affinity_state,
            unlocked=True
        )

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        store.persistent._compliment_database.pop("compliment_amazing")
        store.persistent._compliment_database.pop("compliment_beautiful")
        store.persistent._compliment_database.pop("compliment_confident")
        store.persistent._compliment_database.pop("compliment_cute")
        store.persistent._compliment_database.pop("compliment_hilarious")
        store.persistent._compliment_database.pop("compliment_inspirational")
        store.persistent._compliment_database.pop("compliment_style")
        store.persistent._compliment_database.pop("compliment_thoughtful")

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

label player_compliments_start:
    python:
        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in compliments.get_all_compliments()
        ]
        compliment_menu_items.sort()

    call screen scrollable_choice_menu(compliment_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're amazing!",
            label="compliment_amazing",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:

    if last_compliment_type == COMPLIMENT_TYPE_AMAZING:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "[player]...{w=0.3} honestly!{w=0.2} You're making me blush!"
            n "But still...{w=0.3} thanks.{w=0.2} It really means a lot to me."
            n "You're just as amaazing too,{w=0.1} though.{w=0.2} Remember that!"

        else:
            n "Jeez,{w=0.1} [player]...{w=0.3} you're really doling out the compliments today,{w=0.2} aren't you?"
            n "Don't get me wrong{w=0.1} -{w=0.1} I'm not complaining!"
            n "Make sure you don't leave yourself out though,{w=0.1} 'kay?"
            n "Ehehe."

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Y{w=0.1}-you really think so,{w=0.1} [player]?"
            n "..."
            n "I don't like to admit it,{w=0.1} you know."
            n "But...{w=0.3} that honestly means so much to me,{w=0.1} [player]."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n "Really.{w=0.2} Thank you.{w=0.2} You're honestly [chosen_descriptor]."
            n "..."

            if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
                n "Love you,{w=0.1} [player]..."

        else:
            n "O-{w=0.1}oh!{w=0.2} Aha!{w=0.2} I knew you'd admit it eventually!"
            n "Ehehe."
            n "Well,{w=0.1} I'm just glad both of us agree on that."
            n "Thanks,{w=0.1} [player]!"

            if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
                n "But...{w=0.3} don't think that means you don't have something going for you too!"
                n "You're pretty awesome yourself,{w=0.1} [player].{w=0.2} Remember that,{w=0.1} 'kay?"
                n "Ehehe."

    $ last_compliment_type = COMPLIMENT_TYPE_AMAZING
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're beautiful!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    if last_compliment_type == COMPLIMENT_TYPE_BEAUTIFUL:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Oh jeez,{w=0.1} [player]..."
            n "You're really putting me on the spot today,{w=0.1} aren't you?"
            n "I'll take it,{w=0.1} though!{w=0.2} Ehehe."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "Thanks,{w=0.1} [chosen_tease]."

        else:
            n "E-{w=0.1}excuse me?!"
            n "[player]!{w=0.2} What did I tell you?!"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "Seriously...{w=0.3} you're gonna give me a heart attack or something,{w=0.1} [chosen_tease]..."

            if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
                n "Just...{w=0.3} save it until I can be sure you really mean it,{w=0.1} alright?"
                n "Jeez..."

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Oh...{w=0.3} [player]..."
            n "Y-{w=0.1}you really think I'm..."
            n "I-{w=0.3}I'm..."
            n "..."
            n "You're so nice to me,{w=0.1} [player]..."
            n "You do know that,{w=0.1} right?"
            n "T-{w=0.1}thanks,{w=0.1} sweetheart."

            if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
                n "And you wonder why I love you?{w=0.2} Ahaha..."

        else:
            n "W{w=0.1}-w{w=0.1}-what?"
            n "W-{w=0.1}what did you say?!"
            n "Nnnnnnnnnn-!"
            n "Y-{w=0.1}you can't just say things like that so suddenly,{w=0.1} you dummy!"
            n "Sheesh..."

            if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
                n "..."
                n "I mean,{w=0.1} I'm flattered,{w=0.1} but..."
                n "Uuuuuu...{w=0.3} just stop it for now,{w=0.1} okay?"
                n "You're making this all super awkward..."

    $ last_compliment_type = COMPLIMENT_TYPE_BEAUTIFUL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how confident you are!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    if last_compliment_type == COMPLIMENT_TYPE_CONFIDENT:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Ehehe.{w=0.2} I'm glad you still think so,{w=0.1} [player]!"
            n "I'd say you're worth the effort,{w=0.1} [chosen_tease]."

        else:
            n "Ahaha.{w=0.2} I'm glad you still think so, [player]!"
            n "I try my best,{w=0.1} after all."

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Ehehe.{w=0.2} I just radiate confidence,{w=0.1} don't I?"
            n "..."
            n "Well...{w=0.3} to tell you the truth,{w=0.1} [player]."
            n "I...{w=0.3} really...{w=0.3} wish I could say it was {i}all{/i} genuine."
            n "But having you here with me...{w=0.3} it helps,{w=0.1} you know.{w=0.2} A lot."
            n "So...{w=0.3} thanks,{w=0.1} [player].{w=0.2} Really."

        else:
            n "H-{w=0.1}huh?{w=0.2} O-oh!{w=0.2} Well of course you do!"
            n "I have a lot to be confident about,{w=0.1} after all!"
            n "Wouldn't you agree?"

            if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
                n "Oh,{w=0.1} who am I kidding.{w=0.2} Of course you do."
                n "Ahaha!"

    $ last_compliment_type = COMPLIMENT_TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're cute!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    if last_compliment_type == COMPLIMENT_TYPE_CUTE:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""


    $ last_compliment_type = COMPLIMENT_TYPE_CUTE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of humour!",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    if last_compliment_type == COMPLIMENT_TYPE_HILARIOUS:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""


    $ last_compliment_type = COMPLIMENT_TYPE_HILARIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="You're an inspiration to me!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    if last_compliment_type == COMPLIMENT_TYPE_INSPIRATIONAL:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""


    $ last_compliment_type = COMPLIMENT_TYPE_INSPIRATIONAL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of style!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    if last_compliment_type == COMPLIMENT_TYPE_STYLE:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""


    $ last_compliment_type = COMPLIMENT_TYPE_STYLE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how thoughtful you are!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    if last_compliment_type == COMPLIMENT_TYPE_THOUGHTFUL:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

        else:
            n ""


    $ last_compliment_type = COMPLIMENT_TYPE_THOUGHTFUL
    return
