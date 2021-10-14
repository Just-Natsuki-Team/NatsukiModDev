default persistent._apology_database = dict()

init 0 python in apologies:
    import store

    APOLOGY_MAP = dict()

    # Apology types
    APOLOGY_TYPE_BAD_NICKNAME = 0
    APOLOGY_TYPE_CHEATED_GAME = 1
    APOLOGY_TYPE_DEFAULT = 2
    APOLOGY_TYPE_PROLONGED_LEAVE = 3
    APOLOGY_TYPE_RUDE = 4
    APOLOGY_TYPE_SCREENSHOT = 5
    APOLOGY_TYPE_SUDDEN_LEAVE = 6
    APOLOGY_TYPE_UNHEALTHY = 7

    _last_apology_type = None

    def get_all_apologies():
        """
        Gets all apology topics which are available

        OUT:
            List<Topic> of apologies which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            APOLOGY_MAP.values(),
            affinity=store.jn_globals.current_affinity_state,
            unlocked=True
        )

    def get_apology_type_pending(apology_type):
        """
        Checks whether the given apology type is in the list of pending apologies.

        IN:
            Apology type to check.

        OUT:
            True if present, otherwise False.
        """
        if apology_type in store.persistent.jn_player_pending_apologies:
            return True
        else:
            return False

    def add_new_pending_apology(apology_type):
        """
        Adds a new apology possiblity to the list of pending apologies.
        If the apology type is already present in the list, ignore it.

        IN:
            Apology type to add.
        """
        if not apology_type in store.persistent.jn_player_pending_apologies:
            store.persistent.jn_player_pending_apologies.append(apology_type)

init 1 python in apologies:
    import store 
    
    # DEBUG: TODO: Resets - remove these later, once we're done tweaking affinity/trust!
    try:
        store.persistent._apology_database.clear()

        # TODO: Remove these entries
        add_new_pending_apology(APOLOGY_TYPE_BAD_NICKNAME)
        add_new_pending_apology(APOLOGY_TYPE_CHEATED_GAME)
        add_new_pending_apology(APOLOGY_TYPE_PROLONGED_LEAVE)
        add_new_pending_apology(APOLOGY_TYPE_RUDE)
        add_new_pending_apology(APOLOGY_TYPE_SCREENSHOT)
        add_new_pending_apology(APOLOGY_TYPE_SUDDEN_LEAVE)
        add_new_pending_apology(APOLOGY_TYPE_UNHEALTHY)

    except Exception as e:
        store.utils.log(e, store.utils.SEVERITY_ERR)

# Returns all apologies that the player qualifies for, based on wrongdoings
label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in apologies.get_all_apologies()
        ]
        apologies_menu_items.sort()

    call screen scrollable_choice_menu(apologies_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

# Apology for giving Natsuki a bad nickname
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For calling you a hurtful name.",
            label="apology_bad_nickname",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_BAD_NICKNAME)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n "..."
        n "That hurt, [player]. What you did."
        n "That really hurt me."
        n "..."
        n "I'm... glad you've chosen to apologize."
        n "Just please... try to consider my feelings next time, alright?"

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_BAD_NICKNAME)
    return

# Apology for cheating in a minigame
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For cheating during our games.",
            label="apology_cheated_game",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_CHEATED_GAME)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n "Ehehe.{w=0.2} It's fine,{w=0.1} [player]."
        n "We all get a little too competitive sometimes,{w=0.1} right?"
        n "Just remember though."
        n "Two can play at that game!"

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n "Huh?{w=0.2} Oh,{w=0.1} that."
        n "Yeah,{w=0.1} yeah.{w=0.2} It's fine."
        n "Just play fair next time,{w=0.1} 'kay?"

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n "Whatever,{w=0.1} [player]."
        n "But thanks for the apology,{w=0.1} I guess."

    else:
        n "Whatever.{w=0.2} I don't care."
        n "As if I could expect much better from you,{w=0.1} anyway..."

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_CHEATED_GAME)
    return

# Generic apology
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For something.",
            label="apology_default",
            unlocked=True,
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_default:
    if len(persistent.jn_player_pending_apologies) == 0:
        # The player has nothing to be sorry to Natsuki for; prompt them to do better
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Huh?{w=0.2} You're sorry?"
            n "I...{w=0.3} don't get it,{w=0.1} [player].{w=0.2} You haven't done anything to upset me..."
            n "Did you upset someone else or something?"
            n "..."
            n "Well,{w=0.1} there's no point sitting around here feeling sorry for yourself."
            n "You're gonna make things right,{w=0.1} [player]. 'Kay?"
            n "And no -{w=0.1} this isn't up for discussion."
            n "Whatever you did,{w=0.1} you'll fix things up and that's all there is to it."
            $ chosen_tease = random.choice(store.jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "You have my vote of confidence,{w=0.1} [chosen_tease] -{w=0.1} now do your best!"
            n "Ehehe."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n "Eh?{w=0.2} You're sorry?"
            n "What for,{w=0.1} [player]?{w=0.2} I don't remember you getting on my nerves lately..."
            n "Did you do something dumb that I don't know about?"
            n "..."
            n "Well,{w=0.1} whatever it was -{w=0.1} it's not like it's unfixable,{w=0.1} you know?"
            n "Now get out there and put things right,{w=0.1} [player]!{w=0.2} I believe in you!"

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n "...You're sorry,{w=0.1} are you?"
            n "Did you hurt someone besides me,{w=0.1} this time?"
            n "..."
            n "Well,{w=0.1} whatever.{w=0.2} I don't really care right now."
            n "But you better go make things right,{w=0.1} [player]."
            n "You can do that,{w=0.1} at least."

        else:
            n "...Huh.{w=0.2} Wow."
            n "So you do actually feel remorse,{w=0.1} then."
            n "..."
            n "Whatever.{w=0.2} It isn't me you should be apologizing to,{w=0.1} anyway."

    else:
        # The player is avoiding a direct apology to Natsuki; call them out on it
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "...[player].{w=0.2} Come on."
            n "You know what you did wrong."
            n "Just apologize properly,{w=0.1} alright?"
            n "I won't get mad."
            n "I just wanna move on."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n "Come on,{w=0.1} [player]."
            n "You know what you did."
            n "Just apologize properly so we can both move on."
            
        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n "Ugh..."
            n "Really,{w=0.1} [player].{w=0.2} Haven't you screwed with me enough?"
            n "If you're gonna apologize,{w=0.1} have the guts to do it properly."
            n "You owe me that much,{w=0.1} at least."

        else:
            n "...Do you even know how you sound?"
            n "Do you even {i}listen{/i} to yourself?"
            n "Apologize properly or go away."

    return

# Apology for leaving Natsuki for a week or longer unannounced
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For abandoning you.",
            label="apology_prolonged_leave",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n ""

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)
    return

# Apology for generally being rude to Natsuki outside of nicknames
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For being rude to you.",
            label="apology_rude",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_RUDE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n ""

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_RUDE)
    return

# Apology for taking pictures without Natsuki's permission
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For taking pictures of you without permission.",
            label="apology_screenshots",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_SCREENSHOT)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_screenshots:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n ""

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_SCREENSHOT)
    return

# Apology for leaving without saying "Goodbye" properly.
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For leaving without saying 'Goodbye'.",
            label="apology_without_goodbye",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_without_goodbye:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n ""

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)
    return

# Apology for failing to follow Natsuki's advice when she is concerned about the player's health
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For not taking care of myself properly.",
            label="apology_unhealthy",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.APOLOGY_TYPE_UNHEALTHY)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_UNHEALTHY)
    return