default persistent._greeting_database = dict()

init python in greetings:
    import random
    import store

    GREETING_MAP = dict()

    def select_greeting():
        """
        Picks a random greeting, accounting for affinity
        """
        # If the player didn't make an admission that had Natsuki make them leave, pick a random greeting
        # based on the player's affinity
        kwargs = dict()

        kwargs.update(
            {"excludes_categories": ["Admission"]} if not store.persistent.jn_player_admission_type_on_quit else {"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]}
        )

        store.persistent.jn_player_admission_type_on_quit = None

        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.jn_globals.current_affinity_state,
                **kwargs
            )
        ).label

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        store.persistent._greeting_database.pop("greeting_love_plus_today_is_gonna_be_great")
        store.persistent._greeting_database.pop("greeting_love_plus_world_revolves_around_you")
        store.persistent._greeting_database.pop("greeting_love_plus_make_today_amazing")
        store.persistent._greeting_database.pop("greeting_love_plus_always_welcome_here")
        store.persistent._greeting_database.pop("greeting_love_plus_lovestruck")

        store.persistent._greeting_database.pop("greeting_affectionate_enamored_good_to_see_you")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_couldnt_resist")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_just_cant_stay_away")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_have_so_much_fun")
        store.persistent._greeting_database.pop("greeting_affectionate_enamored_everything_is_fine")

        store.persistent._greeting_database.pop("greeting_normal_happy_whats_up")
        store.persistent._greeting_database.pop("greeting_normal_happy_glad_to_see_you")
        store.persistent._greeting_database.pop("greeting_normal_happy_spacing_out")
        store.persistent._greeting_database.pop("greeting_normal_happy_heya")
        store.persistent._greeting_database.pop("greeting_normal_happy_knew_youd_be_back")

        store.persistent._greeting_database.pop("greeting_distressed_upset_oh_its_you")
        store.persistent._greeting_database.pop("greeting_distressed_upset_hi")
        store.persistent._greeting_database.pop("greeting_distressed_upset_welcome_back_i_guess")
        store.persistent._greeting_database.pop("greeting_distressed_upset_better_be_good")
        store.persistent._greeting_database.pop("greeting_distressed_upset_oh_you_came_back")

        store.persistent._greeting_database.pop("greeting_broken_minus_oh_its_you")
        store.persistent._greeting_database.pop("greeting_broken_minus_nothing_to_say")
        store.persistent._greeting_database.pop("greeting_broken_minus_why")
        store.persistent._greeting_database.pop("greeting_broken_minus_enough_on_my_mind")
        store.persistent._greeting_database.pop("greeting_broken_minus_leave_me_be")

        store.persistent._greeting_database.pop("greeting_feeling_better_sick")
        store.persistent._greeting_database.pop("greeting_feeling_better_tired")

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

# LOVE+ greetings
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_today_is_gonna_be_great",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_today_is_gonna_be_great:
    n "[player]!{w=0.2} You're back,{w=0.1} finally!"
    n "Ehehe.{w=0.2} Now I {i}know{/i} today's gonna be great!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_world_revolves_around_you",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_world_revolves_around_you:
    n "[player]!{w=0.1} What took you so long?{w=0.2} Jeez!"
    n "You think my entire world revolves around you or something?"
    n "..."
    n "..."
    n "Ahaha!{w=0.2} Did I get you,{w=0.1} [player]?{w=0.2} Don't lie!"
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "Well, anyway.{w=0.2} You're here now, [chosen_endearment]!{w=0.2} Welcome back!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_make_today_amazing",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_make_today_amazing:
    n "[player]!{w=0.2} [player] [player] [player]!"
    n "I'm so glad to see you again!{w=0.2} Welcome back!"
    n "Let's make today amazing too,{w=0.1} alright?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_always_welcome_here",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_always_welcome_here:
    n "[player],{w=0.1} you're back!"
    n "I was really starting to miss you, you know..."
    n "Don't keep me waiting so long next time,{w=0.2} alright?"
    n "You're always welcome here,{w=0.2} after all..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_lovestruck",
            unlocked=True,
            affinity_range=(jn_aff.LOVE, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_lovestruck:
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
            label="greeting_affectionate_enamored_good_to_see_you",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_good_to_see_you:
    n "[player]!{w=0.2} You're back!"
    n "It's so good to see you again!"
    n "Let's make today amazing as well,{w=0.1} 'kay? Ehehe."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_couldnt_resist",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_couldnt_resist:
    n "Hey,{w=0.1} you!{w=0.2} Back so soon?"
    n "I knew you couldn't resist.{w=0.2} Ehehe."
    n "What do you wanna do today?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_just_cant_stay_away",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_just_cant_stay_away:
    n "Well, well, well.{w=0.2} What do we have here?"
    n "You just can't stay away from me,{w=0.1} can you?{w=0.2} Ahaha!"
    n "Not that I'm complaining too much!"
    n "So...{w=0.3} what do you wanna talk about?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_have_so_much_fun",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_have_so_much_fun:
    n "It's [player],{w=0.1} yay!"
    n "We're gonna have so much fun today!{w=0.2} Ehehe."
    n "So,{w=0.1} what do you wanna talk about?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_everything_is_fine",
            unlocked=True,
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_everything_is_fine:
    n "[player], you're back!"
    n "I've been waiting for you, you know..."
    n "But now that you're here, everything is fine! Ehehe."
    return

# NORMAL/HAPPY greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_up",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_up:
    n "Oh!{w=0.2} Hey,{w=0.1} [player]!"
    n "What's up?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_glad_to_see_you",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_glad_to_see_you:
    n "Hi,{w=0.1} [player]!"
    n "I'm glad to see you again."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_spacing_out",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_spacing_out:
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
            label="greeting_normal_happy_heya",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_heya:
    n "Heya,{w=0.1} [player]!"
    n "Welcome back!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_knew_youd_be_back",
            unlocked=True,
            affinity_range=(jn_aff.NORMAL, jn_aff.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_knew_youd_be_back:
    n "It's [player]!{w=0.2} Hi!"
    n "I-I knew you'd be back,{w=0.1} obviously."
    n "You'd have to have no taste to not visit again! Ahaha!"
    return

# DISTRESSED/UPSET greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_its_you",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_its_you:
    n "Oh.{w=0.2} It's you."
    n "Hello,{w=0.1} [player]."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_hi",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_hi:
    n "[player].{w=0.2} Hi."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_welcome_back_i_guess",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_welcome_back_i_guess:
    n "[player].{w=0.2} Welcome back,{w=0.1} I guess."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_better_be_good",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_better_be_good:
    n "Hi,{w=0.1} [player]."
    n "This better be good."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_you_came_back",
            unlocked=True,
            affinity_range=(jn_aff.DISTRESSED, jn_aff.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_you_came_back:
    n "Oh?{w=0.2} You came back?"
    n "...I wish I could say I was happy about it."
    return

# BROKEN- greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_oh_its_you",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_oh_its_you:
    n "...?"
    n "Oh...{w=0.3} it's you."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_nothing_to_say:
    n "..."
    n "..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_why",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_why:
    n "...Why?"
    n "Why did you come back,{w=0.1} [player]?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_enough_on_my_mind",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_enough_on_my_mind:
    $ player_initial = list(player)[0]
    n "[player_initial]-{w=0.1}[player]...?"
    n "As if I didn't have enough on my mind..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_leave_me_be",
            unlocked=True,
            affinity_range=(None, jn_aff.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_leave_me_be:
    $ player_initial = list(player)[0]
    n "...Why, [player]?{w=0.2} Why do you keep coming back?"
    n "Why can't you just leave me be..."
    return

# Admission-locked greetings; used when Natsuki made the player leave due to tiredness, etc.

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_sick",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "admission_type": admissions.TYPE_SICK,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_sick:
    n "Oh!{w=0.2} [player]!{w=0.2} Hey!"
    n "How're you feeling?{w=0.2} Any better?"
    menu:
        "Much better, thanks!":
            n "Good, good!{w=0.2} I'm glad to hear it!{w=0.2} Nobody likes being ill."
            n "Now that's out of the way,{w=0.1} how about we spend some quality time together?"
            n "You owe me that much!{w=0.2} Ehehe."
            $ persistent.jn_player_admission_type_on_quit = None

        "A little better.":
            n "...I'll admit, that wasn't really what I wanted to hear."
            n "But I'll take 'a little' over not at all,{w=0.1} I guess."
            n "Anyway...{w=0.3} welcome back,{w=0.1} [player]!"
            $ admissions.last_admission_type = admissions.TYPE_SICK

        "Still unwell.":
            n "Still not feeling up to scratch,{w=0.1} [player]?"
            n "I don't mind you being here...{w=0.3} but don't strain yourself,{w=0.1} alright?"
            n "I don't want you making yourself worse for my sake..."
            $ admissions.last_admission_type = admissions.TYPE_SICK

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_tired",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
            additional_properties={
                "admission_type": admissions.TYPE_TIRED,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_tired:
    n "Ah!{w=0.2} [player]!{w=0.2} Hi!"
    n "I hope you got enough sleep.{w=0.2} How're you feeling?"
    menu:
        "Much better, thanks!":
            n "Great!{w=0.2} Nothing like a good night's sleep,{w=0.1} am I right?"
            n "Now then - seeing as you're finally awake and alert..."
            n "What better opportunity to spend some more time with me?{w=0.2} Ehehe."
            $ persistent.jn_player_admission_type_on_quit = None

        "A little tired.":
            n "Oh...{w=0.3} well,{w=0.1} that's not quite what I was hoping to hear."
            n "If you aren't feeling too tired,{w=0.1} perhaps you could grab something to wake up a little?"
            n "A nice glass of water or some bitter coffee should perk you up in no time!"
            $ admissions.last_admission_type = admissions.TYPE_TIRED

        "Still tired.":
            n "Still struggling with your sleep,{w=0.1} [player]?"
            n "I don't mind you being here...{w=0.3} but don't strain yourself,{w=0.1} alright?"
            n "I don't want you face-planting your desk for my sake..."
            $ admissions.last_admission_type = admissions.TYPE_TIRED
    return
