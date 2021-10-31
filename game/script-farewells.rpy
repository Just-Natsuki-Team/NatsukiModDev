default persistent._farewell_database = dict()

init python in farewells:
    import random
    import store

    FAREWELL_MAP = dict()

    def select_farewell():
        """
        Picks a random farewell, accounting for affinity
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        # Get the farewells the current affinity allows for the player
        #TODO: Generalized filter function
        farewell_pool = store.Topic.filter_topics(
            FAREWELL_MAP.values(),
            affinity=store.jn_globals.current_affinity_state,
            additional_properties=[
                ("is_time_sensitive", store.utils.get_current_session_length().total_seconds() / 60 < 30),
                ("has_stay_option", not store.jn_globals.player_already_stayed_on_farewell and store.jn_globals.current_affinity_state >= 6)
            ],
            excludes_categories=["Failsafe"]
        )

        # If pool isn't empty
        if farewell_pool:
            # Return a random farewell from the remaining pool
            return random.choice(farewell_pool).label

        #else
        # Run filter again, this time without caring for special farewells
        farewell_pool = store.Topic.filter_topics(
            FAREWELL_MAP.values(),
            affinity=store.jn_globals.current_affinity_state,
            additional_properties=[
                ("is_time_sensitive", False),
                ("has_stay_option", False)
            ],
            excludes_categories=["Failsafe"]
        )

        # Again check if pool isn't empy
        if farewell_pool:
            # Return a random farewell from the new pool
            return random.choice(farewell_pool).label

        #else
        # Fallback if both searches fail or if something just Fs up
        return "farewell_fallback_see_you_soon"

    def try_trust_dialogue():
        """
        Coinflip decision on whether to additionally call trust-based dialogue on farewell
        """
        if random.choice([True, False]):
            renpy.call_in_new_context("farewell_extra_trust")

init 1 python:
    # DEBUG: TODO: Resets - remove these later, once we're done tweaking affinity/trust!
    try:
        store.persistent._farewell_database.clear()

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

label farewell_start:
    $ push(farewells.select_farewell())
    jump call_next_topic


# LOVE+ farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_you_mean_the_world_to_me",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_you_mean_the_world_to_me:
    n "Aww...{w=0.3} you're leaving now,{w=0.1} [player]?{w=0.2} Well,{w=0.1} okay..."
    n "Y-{w=0.2}you know I'll miss you,{w=0.1} right?"
    n "Take care,{w=0.1} [player]!{w=0.2} You mean the world to me!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_dont_like_saying_goodbye",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_dont_like_saying_goodbye:
    n "You know I don't like saying goodbye,{w=0.1} [player]..."
    n "..."
    n "I'll be okay!{w=0.2} Just come back soon,{w=0.1} alright?"
    n "Stay safe,{w=0.1} dummy!{w=0.2} I love you!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_counting_on_you",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_counting_on_you:
    n "Uuuu...{w=0.3} I never like saying goodbye to you..."
    n "But I guess it can't be helped,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Take care of yourself out there,{w=0.1} [chosen_endearment]!{w=0.2} I'm counting on you!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_do_your_best",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_do_your_best:
    n "Oh?{w=0.2} You're heading out now?"
    n "That's fine,{w=0.1} I guess..."
    n "I'll really miss you,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Do your best,{w=0.1} [chosen_endearment]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_rooting_for_you",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_rooting_for_you:
    n "Huh?{w=0.2} You're leaving now?"
    n "I always hate it when you have to go somewhere..."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "...But I know you'll always be back for me,{w=0.1} [chosen_endearment]."
    n "Well...{w=0.1} I'm rooting for you!"
    n "Make me proud,{w=0.1} [player]! I love you!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_me_to_deal_with",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_me_to_deal_with:
    n "You're leaving now,{w=0.1} [player]?"
    n "Awww...{w=0.3} well okay."
    n "You take care of yourself,{w=0.1} got it? Or you'll have me to deal with!"
    n "Bye now!{w=0.2} I love you!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_wish_you_could_stay_forever",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_wish_you_could_stay_forever:
    n "Time to go,{w=0.1} [player]?"
    n "Sometimes I wish you could just stay forever...{w=0.3} Ehehe."
    n "But I understand you've got stuff to do."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Goodbye,{w=0.1} [chosen_endearment]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

# AFFECTIONATE/ENAMORED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_was_having_fun",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_was_having_fun:
    n "Hmm?{w=0.2} You're leaving now?"
    n "Aww,{w=0.1} man..."
    n "And I was having fun,{w=0.1} too..."
    n "Well,{w=0.1} if you gotta go,{w=0.1} you gotta go!"
    n "Take care,{w=0.1} [player]!{w=0.2} Make me proud!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_waiting_for_you",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_waiting_for_you:
    n "You're going,{w=0.1} [player]?"
    n "Uuuuu...{w=0.3} okay..."
    n "Hurry back if you can,{w=0.1} alright?"
    n "I'll be waiting for you!"
    n "Goodbye,{w=0.1} [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_ill_be_okay",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_ill_be_okay:
    n "Huh?{w=0.2} You're leaving?"
    n "..."
    n "That's fine...{w=0.3} I'll be okay..."
    n "You better come back soon,{w=0.1} alright [player]?"
    n "Goodbye!{w=0.2} I'll miss you!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_dont_make_me_find_you",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_dont_make_me_find_you:
    n "Oh?{w=0.2} Heading off now,{w=0.1} [player]?"
    n "I wish you didn't have to..."
    n "But I know you have things to do."
    n "Come see me later,{w=0.1} promise?"
    n "Don't make me come find you!{w=0.2} Ehehe."
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_take_care_for_both",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_take_care_for_both:
    n "Mmm?{w=0.2} You're going now,{w=0.1} [player]?"
    n "I was hoping you'd be around longer..."
    n "Well,{w=0.2} I'll be okay!"
    n "Take care of yourself,{w=0.1} [player]!{w=0.2} For both of us!"
    n "See you later!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_enjoy_our_time_together",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_enjoy_our_time_together:
    n "You're leaving now,{w=0.1} [player]?"
    n "Nnnnnn...{w=0.3} alright."
    n "You better be back later,{w=0.1} okay?{w=0.2} I really enjoy our time together."
    n "See you soon,{w=0.1} [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_see_me_soon",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_see_me_soon:
    n "Well,{w=0.1} I guess you had to leave eventually."
    n "Doesn't mean I have to like it,{w=0.1} though..."
    n "Come see me soon,{w=0.1} okay?"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

# HAPPY/AFFECTIONATE farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_going_now",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_going_now:
    n "Going now,{w=0.1} [player]?{w=0.2} I'll see you later!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_heading_off",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_heading_off:
    n "Heading off now,{w=0.1} [player]?"
    n "Okay!{w=0.2} Take care!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_stay_safe",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_stay_safe:
    n "Okaaay!{w=0.2} I'll be waiting for you!"
    n "Stay safe,{w=0.1} [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_take_care",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_take_care:
    n "See you later,{w=0.1} [player]!"
    n "Take care out there!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_see_me_soon",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_see_me_soon:
    n "Goodbye,{w=0.1} [player]!"
    n "Come see me soon,{w=0.1} alright?"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

# NORMAL/HAPPY farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_you_later",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_you_later:
    n "See you later, [player]!"
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_later",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_later:
    n "Later, [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_goodbye",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_goodbye:
    n "Goodbye, [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_kay",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_kay:
    n "'kay! Bye for now!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_ya",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_ya:
    n "See ya, [player]!"
    $ farewells.try_trust_dialogue()
    return { "quit": None }

# UPSET/DISTRESSED farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_bye",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_bye:
    n "Bye, [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_later",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_later:
    n "Later, [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_kay",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_kay:
    n "'kay, [player]. Later."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_goodbye",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_goodbye:
    n "Goodbye, [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_see_you_around",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET),
            additional_properties={
                "has_stay_option": False,
            "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_see_you_around:
    n "See you around."
    return { "quit": None }

# DISTRESSED/BROKEN/RUINED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yeah",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yeah:
    n "Yeah."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yep",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yep:
    n "Yep."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_uh_huh",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_uh_huh:
    n "Uh huh."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_nothing_to_say",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_nothing_to_say:
    n "..."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_kay",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.RUINED, jn_aff.BROKEN),
            additional_properties={
                "has_stay_option": False,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_kay:
    n "'kay."
    return { "quit": None }

# Farewells that allow the player to choose to stay

# Natsuki calls the player out on how long they've been here, and asks for more time together
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n "What?{w=0.2} You're leaving?{w=0.2} But you've barely been here at all today,{w=0.1} [player]!"
    $ time_in_session_descriptor = utils.get_time_in_session_descriptor()
    n "In fact, you've only been here for [time_in_session_descriptor]!"
    n "You're sure you can't stay just a little longer?"
    menu:
        "Sure, I can stay a little longer.":
            n "Yay{nw}!"
            n "I-I mean...!"
            if jn_affinity.get_affinity_state() > jn_affinity.ENAMORED:
                n "Thanks, [player]. It means a lot to me."
                $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                n "Really. Thank you, [chosen_endearment]."
                n "...A-anyway!"

            else:
                n "Yeah!{w=0.2} That's what I thought!"
                n "Yeah..."
                n "..."
                n "Stop looking at me like that,{w=0.1} jeez!"
            n "Now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True

        "If you say so.":
            n "[player]..."
            n "I'm not forcing you to be here.{w=0.1} You know that,{w=0.1} right?"
            n "Are you sure you wanna stay?"
            menu:
                "Yes, I'm sure.":
                    "Well,{w=0.1} if you're sure."
                    "I just want to make sure I don't sound all naggy."
                    if jn_affinity.get_affinity_state() > jn_affinity.ENAMORED:
                        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                        n "Thanks,{w=0.1} [chosen_endearment]. You know it means a lot to me."

                    else:
                        n "Thanks, [player]. It means a lot."

                    $ jn_globals.player_already_stayed_on_farewell = True

                "No, I have to go.":
                    n "Well...{w=0.3} okay,{w=0.1} [player]."
                    n "Take care out there,{w=0.1} alright?"
                    n "See you later!"
                    $ farewells.try_trust_dialogue()
                    return { "quit": None }

        "Sorry, Natsuki. I really have to leave.":
            n "Nnnnnn-!"
            n "..."
            n "Well...{w=0.3} okay."
            n "Don't take too long,{w=0.1} alright?"
            n "See you later, [player]!"
            $ farewells.try_trust_dialogue()
            return { "quit": None }

    return

# Natsuki calls the player out on how long they've been here, and asks for more time together (alt)
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask_alt",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask_alt:
    n "N-{w=0.1}now wait just one second,{w=0.1} [player]!{w=0.2} This isn't fair at all!"
    $ time_in_session_descriptor = utils.get_time_in_session_descriptor()
    n "You've barely been here [time_in_session_descriptor],{w=0.1} and you're already going?"
    n "Come on!{w=0.2} You'll stay a little longer,{w=0.1} won't you?"
    menu:
        "Sure, I can stay a while.":
            n "H-{w=0.1}Ha!{w=0.2} I knew it."
            n "Ehehe.{w=0.1} Looks like I win again,{w=0.1} [player]!"
            n "O-or maybe you just can't bring yourself to leave my side?"
            menu:
                "You got me, Natsuki. I couldn't leave you even if I tried.":
                    $ player_was_snarky = False
                    n "W-{w=0.2}wha...?"
                    n "Nnnnnnn-!"
                    $ player_initial = list(player)[0]
                    n "[player_initial]-{w=0.2}[player]!"
                    n "Don't just come out with stuff like that!"
                    n "Jeez...{w=0.3} you're such a dummy sometimes..."

                "Yeah, yeah.":
                    $ player_was_snarky = True
                    n "Ehehe.{w=0.2} What's wrong,{w=0.1} [player]?"
                    n "A little too close to the truth?"
                    n "Ahaha!"

            n "Well,{w=0.1} either way,{w=0.1} I'm glad you can stay a little longer!"
            if player_was_snarky:
                n "Or...{w=0.3} perhaps you should be thanking {i}me{/i}?{w=0.2} Ehehe."
            n "So...{w=0.3} what else did you wanna do today?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ relationship("affinity+")

        "Fine, I guess.":
            n "You {i}guess{/i}?{w=0.2} What do you mean,{w=0.1} you guess?!"
            n "Jeez...{w=0.3} what's with the attitude today, [player]?"
            n "Well, anyway...{w=0.3} Thanks for staying with me a little longer."
            n "...{i}I guess{/i}."
            n "Ahaha! Oh, lighten up, [player]! I'm just messing with you!"
            n "Now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ relationship("affinity+")

        "Sorry Natsuki, I can't right now.":
            n "Uuuu-"
            n "Well,{w=0.1} I guess that's fine.{w=0.2} It can't be helped,{w=0.1} after all."
            n "But you gotta make it up to me,{w=0.1} alright?"
            n "Stay safe,{w=0.1} [player]!{w=0.2} I'll see you later!"
            $ farewells.try_trust_dialogue()
            return { "quit": None }
    return

# Natsuki tries to confidently ask her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.HAPPY, jn_aff.AFFECTIONATE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n "Huh?{w=0.2} You don't really have to leave already,{w=0.1} do you?"
    n "It feels like you've barely been here!"
    n "I bet you can hang out with me a little longer!{w=0.2} Right,{w=0.1} [player]?"
    n "{w=0.3}...right?"
    menu:
        "Right!":
            n "A-Aha!{w=0.2} I knew it!"
            n "I totally don't need you here,{w=0.1} or anything dumb like that!"
            n "You'd have to be pretty lonely to be {i}that{/i} dependent on someone else...{w=0.3} ahaha..."
            n "..."
            n "Jeez!{w=0.2} Let's just get back to it already..."
            n "Now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ relationship("affinity+")

        "Sorry, I really need to go.":
            n "Oh...{w=0.3} aha..."
            n "That's fine,{w=0.1} I guess..."
            n "I'll see you later then,{w=0.1} [player]!"
            n "Don't keep me waiting,{w=0.1} alright?"
            $ farewells.try_trust_dialogue()
            return { "quit": None }
    return

# Natuski really doesn't want to be alone today; she pleads for her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.ENAMORED, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_pleading_ask:
    n "N-no!{w=0.2} You can't leave yet!"
    n "..."
    n "[player]...{w=0.3} I...{w=0.3} really...{w=0.3} want you here right now."
    n "Just stay with me a little longer...{w=0.3} please?"
    menu:
        "Of course!":
            n "Yes!{nw}"
            n "I-I mean...!"
            n "..."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n "T-thanks, [player].{w=0.1} You're [chosen_descriptor],{w=0.1} you know that?"
            n "Really.{w=0.1} Thank you."
            n "N-now,{w=0.1} where were we? Heh..."
            $ jn_globals.player_already_stayed_on_farewell = True
            $ relationship("affinity+")

        "I can't right now.":
            n "Oh..."
            n "Well,{w=0.1} if you gotta go,{w=0.1} it can't be helped,{w=0.1} I guess..."
            n "Come back soon,{w=0.1} alright?"
            n "Or you'll have to make it up to me...{w=0.3} ahaha..."
            n "Stay safe,{w=0.1} [player]!"
            $ farewells.try_trust_dialogue()
            return { "quit": None }
    return

# Natsuki gently asks her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE),
            additional_properties={
                "has_stay_option": True,
                "is_time_sensitive": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_gentle_ask:
    n "[player]...{w=0.3} do you really have to leave now?"
    n "I know you have stuff to do,{w=0.1} but I...{w=0.3} really...{w=0.3} wanna spend more time with you."
    n "Are you sure you have to go?"
    menu:
        "I can stay a little longer.":
            n "[player]..."
            n "Thank you.{w=0.1} That really means a lot to me right now."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n "Y-You're [chosen_descriptor], [player]."
            n "Truly.{w=0.1} Thanks..."
            n "..."
            n "Aha...{w=0.3} so what else did you wanna do today?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ relationship("affinity+")

        "Sorry, I really have to go.":
            n "Oh..."
            n "I'd be lying if I said I wasn't disappointed, but I understand."
            n "Just be careful out there, okay?"
            n "..."
            n "I-I love you,{w=0.1} [player]..."
            n "I'll see you later."
            $ farewells.try_trust_dialogue()
            return { "quit": None }
    return

# Trust dialogue; chance to call upon farewell completing and prior to the game closing

label farewell_extra_trust:
    # ABSOLUTE+
    if trust.trust_is_between_bounds(
        lower_bound=store.jn_trust.TRUST_ABSOLUTE,
        trust=store.persistent.trust,
        upper_bound=None
    ):
        n "My [player]...{w=0.3} I'll be waiting..."

    # FULL-COMPLETE
    elif trust.trust_is_between_bounds(
        lower_bound=store.jn_trust.TRUST_FULL,
        trust=store.persistent.trust,
        upper_bound=store.jn_trust.TRUST_ABSOLUTE
    ):
        n "I'll be waiting..."

    # NEUTRAL-PARTIAL
    elif trust.trust_is_between_bounds(
        lower_bound=store.jn_trust.TRUST_NEUTRAL,
        trust=store.persistent.trust,
        upper_bound=store.jn_trust.TRUST_PARTIAL
    ):
        n "You'll be back...{w=0.3} right?"

    # SCEPTICAL-NEUTRAL
    elif trust.trust_is_between_bounds(
        lower_bound=store.jn_trust.TRUST_SCEPTICAL,
        trust=store.persistent.trust,
        upper_bound=store.jn_trust.TRUST_NEUTRAL
    ):
        n "I'll be okay...{w=0.3} I'll be okay..."

    # DIMINISHED-SCEPTICAL
    elif trust.trust_is_between_bounds(
        lower_bound=store.jn_trust.TRUST_DIMINISHED,
        trust=store.persistent.trust,
        upper_bound=store.jn_trust.TRUST_SCEPTICAL
    ):
        n "...?"

    # DIMINISHED-
    elif trust.trust_is_between_bounds(
        lower_bound=None,
        trust=store.persistent.trust,
        upper_bound=store.jn_trust.TRUST_DIMINISHED
    ):
        n "..."

    # Debug
    else:
        n "Nnn..."

    return { "quit": None }

# Fallback farewell if selecting a farewell fails

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fallback_see_you_soon",
            unlocked=True,
            category=["Failsafe"]
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fallback_see_you_soon:
    n "Alright, see you soon."
    return { "quit": None }
