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

    if persistent.jn_player_nicknames_allowed:
        # The player is still capable of nicknaming Natsuki
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "..."
            n "That hurt,{w=0.1} [player].{w=0.2} What you did."
            n "That really hurt me."
            n "..."
            n "I'm...{w=0.3} glad you've chosen to apologize."
            n "Just please...{w=0.3} try to consider my feelings next time,{w=0.1} alright?"
            $ relationship("affinity+")

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n "..."
            n "...Fine.{w=0.2} I accept your apology, okay?"
            n "Just please knock it off,{w=0.1} [player]."
            n "It isn't funny.{w=0.2} It isn't a joke."
            n "...And I know you're better than that."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n "...Are you sure,{w=0.1} [player]?"
            n "I mean...{w=0.3} if you actually cared about my feelings..."
            n "Why would you even think about doing that in the first place?"
            n "Behaving like that doesn't make you funny,{w=0.1} [player]."
            n "It makes you toxic."
            n "..."
            n "...Thanks,{w=0.1} I guess.{w=0.2} For the apology."
            n "Just quit while you're ahead,{w=0.1} understand?"
            $ relationship("affinity+")

        else:
            n "...I honestly don't know what I find more gross about you,{w=0.1} [player]."
            n "The fact you even did it in the first place..."
            n "...Or that you think a simple apology makes all that a-okay."
            n "..."
            n "Don't think this changes a thing,{w=0.1} [player]."
            n "Because it doesn't."

    else:
        # The player has been barred from nicknaming Natsuki, and even an apology won't change that
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "...[player]."
            n "I warned you."
            n "I warned you so many times."
            n "Did you think apologizing now would change anything?"
            n "..."
            n "...Look,{w=0.1} [player]."
            n "I appreciate your apology,{w=0.1} okay?{w=0.2} I do."
            n "But...{w=0.3} it's just like I said.{w=0.2} Actions have consequences."
            n "I hope you can understand."
            $ relationship("affinity+")

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n "...[player]."
            n "Look.{w=0.2} You're sorry,{w=0.1} I get it.{w=0.2} I'm sure you mean it too."
            n "But...{w=0.3} it's like I said.{w=0.1} Actions have consequences."
            n "I hope you can understand."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n "Ugh...{w=0.3} really,{w=0.1} [player]?"
            n "..."
            n "I {i}said{/i} actions have consequences."
            n "I appreciate the apology.{w=0.2} But that's all you're getting."
            $ relationship("affinity+")

        else:
            n "...Wow.{w=0.2} Just wow."
            n "{i}Now{/i} you choose to apologize?"
            n "..."
            n "Whatever.{w=0.2} I literally don't care."
            n "This changes nothing,{w=0.1} [player]."

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
        $ relationship("affinity+")

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n "Huh?{w=0.2} Oh,{w=0.1} that."
        n "Yeah,{w=0.1} yeah.{w=0.2} It's fine."
        n "Just play fair next time,{w=0.1} 'kay?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n "Whatever,{w=0.1} [player]."
        n "But thanks for the apology,{w=0.1} I guess."
        $ relationship("affinity+")

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
            $ relationship("affinity-")

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n "Come on,{w=0.1} [player]."
            n "You know what you did."
            n "Just apologize properly so we can both move on."
            $ relationship("affinity-")
            
        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n "Ugh..."
            n "Really,{w=0.1} [player].{w=0.2} Haven't you screwed with me enough?"
            n "If you're gonna apologize,{w=0.1} have the guts to do it properly."
            n "You owe me that much,{w=0.1} at least."
            $ relationship("affinity-")

        else:
            n "...Do you even know how you sound?"
            n "Do you even {i}listen{/i} to yourself?"
            n "Apologize properly or don't bother."
            $ relationship("affinity-")

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
        n "...[player]."
        n "We've been together a while now,{w=0.1} haven't we?"
        n "I...{w=0.3} really...{w=0.3} like spending time with you.{w=0.2} Why do you think I'm always here when you drop in?"
        n "So..."
        n "Can you imagine how it makes me feel when you just...{w=0.3} don't turn up?"
        n "..."
        n "I waited for you,{w=0.1} [player]."
        n "I waited a long time."
        n "I was starting to wonder if you were ever going to come back,{w=0.1} or if something happened..."
        n "..."
        n "Thanks,{w=0.1} [player].{w=0.2} I accept your apology."
        n "Just...{w=0.3} some notice would be nice next time,{w=0.1} is all."
        n "That isn't too much to ask...{w=0.3} right?"
        $ relationship("affinity+")

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n "[player]..."
        n "What were you thinking?!{w=0.2} Just disappearing like that!"
        n "I waited so long for you...{w=0.3} I was starting to wonder if something bad happened!"
        n "N-{w=0.1}not that I care {i}that{/i} much,{w=0.1} but still...!"
        n "..."
        n "I'm...{w=0.3} grateful for your apology,{w=0.1} [player]."
        n "Just...{w=0.3} no more vanishing acts,{w=0.1} alright?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n "[player]."
        n "I know we haven't exactly been eye-to-eye lately."
        n "But do you know how {i}scary{/i} it is to me when you just disappear like that?"
        n "In case you haven't already noticed,{w=0.1} I don't exactly have many other people to talk to..."
        n "..."
        n "Thanks for the apology,{w=0.1} I guess."
        n "Try not to do that again,{w=0.1} at least."
        $ relationship("affinity+")

    else:
        n "...Ha...{w=0.3} ah...{w=0.3} haha..."
        n "Y-{w=0.1}you're apologizing to me?{w=0.2} For not being here?"
        n "...Heh..."
        n "You should be apologizing that you {i}came back{/i}."

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
        $ relationship("affinity+")

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""
        $ relationship("affinity+")

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
    # The player has been barred from taking more screenshots
    if store.jn_screenshots.player_screenshots_blocked:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""
            $ relationship("affinity+")

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n ""
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n ""
            $ relationship("affinity+")

        else:
            n ""

    # The player hasn't been barred from taking more screenshots
    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n ""
            $ relationship("affinity+")

        if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            n ""
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            n ""
            $ relationship("affinity+")

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
        $ relationship("affinity+")

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""
        $ relationship("affinity+")

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
        $ relationship("affinity+")

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n ""
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n ""
        $ relationship("affinity+")

    else:
        n ""

    $ persistent.jn_player_pending_apologies.remove(apologies.APOLOGY_TYPE_UNHEALTHY)
    return