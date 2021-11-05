default persistent._greeting_database = dict()

init python in greetings:
    import random
    import store

    GREETING_MAP = dict()

    def select_greeting():
        """
        Picks a random greeting, accounting for affinity and the situation they previously left under
        """
        kwargs = dict()

        # The player either left suddenly, or has been gone a long time
        if store.persistent.jn_player_apology_type_on_quit is not None:
            kwargs.update({"additional_properties": [("apology_type", store.persistent.jn_player_apology_type_on_quit)]})
        
        # The player left or was forced to leave by way of an admission (E.G tired, sick)
        elif store.persistent.jn_player_admission_type_on_quit is not None:
            kwargs.update({"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]})
        
        # Just get a standard greeting from the affinity pool
        else:
            kwargs.update({"excludes_categories": ["Admission", "Apology"]})

        # Finally return an appropriate greeting
        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.jn_affinity.get_affinity_state(),
                conditional=True,
                **kwargs
            )
        ).label

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        persistent._greeting_database.clear()

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
                "admission_type": admissions.ADMISSION_TYPE_SICK,
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
            n "...I'll admit,{w=0.1} that wasn't really what I wanted to hear."
            n "But I'll take 'a little' over not at all,{w=0.1} I guess."
            n "Anyway...{w=0.3} welcome back,{w=0.1} [player]!"
            
            # Add pending apology, reset the admission
            $ store.apologies.add_new_pending_apology(store.apologies.APOLOGY_TYPE_UNHEALTHY)
            $ admissions.last_admission_type = admissions.ADMISSION_TYPE_SICK

        "Still unwell.":
            n "Still not feeling up to scratch,{w=0.1} [player]?"
            n "I don't mind you being here...{w=0.3} but don't strain yourself,{w=0.1} alright?"
            n "I don't want you making yourself worse for my sake..."

            # Add pending apology, reset the admission
            $ store.apologies.add_new_pending_apology(store.apologies.APOLOGY_TYPE_UNHEALTHY)
            $ admissions.last_admission_type = admissions.ADMISSION_TYPE_SICK
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
                "admission_type": admissions.ADMISSION_TYPE_TIRED,
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
            
            # Add pending apology, reset the admission
            $ store.apologies.add_new_pending_apology(store.apologies.APOLOGY_TYPE_UNHEALTHY)
            $ admissions.last_admission_type = admissions.ADMISSION_TYPE_TIRED

        "Still tired.":
            n "Still struggling with your sleep,{w=0.1} [player]?"
            n "I don't mind you being here...{w=0.3} but don't strain yourself,{w=0.1} alright?"
            n "I don't want you face-planting your desk for my sake..."
            
            # Add pending apology, reset the admission
            $ store.apologies.add_new_pending_apology(store.apologies.APOLOGY_TYPE_UNHEALTHY)
            $ admissions.last_admission_type = admissions.ADMISSION_TYPE_TIRED
    return

# Absence-related greetings; used when the player leaves suddenly, or has been gone an extended period

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sudden_leave",
            unlocked=True,
            category=["Apology"],
            affinity_range=(None, jn_aff.LOVE),
            additional_properties={
                "apology_type": apologies.APOLOGY_TYPE_SUDDEN_LEAVE,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sudden_leave:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "..."
        n "[player]."
        n "Come on.{w=0.2} You're better than that."
        n "I don't know if something happened or what,{w=0.1} but please..."
        n "Try to remember to say goodbye properly next time,{w=0.1} 'kay?"
        n "It'd mean a lot to me."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "..."
        n "[player]!{w=0.2} Do you know how scary it is when you just vanish like that?"
        n "Please...{w=0.3} just remember to say goodbye properly when you gotta leave."
        n "It's not much to ask...{w=0.3} is it?"
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)
 
    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "..."
        n "You know I hate that,{w=0.1} [player]."
        n "Knock it off,{w=0.1} will you?"
        n "Thanks."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)

    else:
        n "..."
        n "Heh.{w=0.2} Yeah."
        $ chosen_insult = random.choice(jn_globals.DEFAULT_PLAYER_INSULT_NAMES).capitalize()
        n "Welcome back to you,{w=0.1} too.{w=0.2} [chosen_insult]."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_SUDDEN_LEAVE)

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_prolonged_leave",
            unlocked=True,
            category=["Apology"],
            affinity_range=(None, jn_aff.LOVE),
            additional_properties={
                "apology_type": apologies.APOLOGY_TYPE_PROLONGED_LEAVE,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_prolonged_leave:
    $ player_initial = list(player)[0]

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "[player_initial]-{w=0.1}[player]!"
        n "W-{w=0.1}where were you?!{w=0.2} I was so worried that something had happened!"
        n "..."
        n "I'm...{w=0.3} glad...{w=0.3} you're back,{w=0.1} [player]."
        n "Just...{w=0.3} some warning next time,{w=0.1} please?"
        n "I hate having my heart played with like that..."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "[player_initial]-{w=0.1}[player]!"
        n "What the hell?!{w=0.2} Where have you been?{w=0.2} I was worried sick!"
        n "J-{w=0.1}just as a friend,{w=0.1} but still!"
        n "..."
        n "...Welcome back,{w=0.1} [player]."
        n "Just...{w=0.3} don't leave it so long next time,{w=0.1} alright?{w=0.2} Jeez..."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "[player_initial]-{w=0.1}[player]?"
        n "...You're back."
        n "I...{w=0.3} don't know how I feel about that."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)
        
    else:
        n "...Heh."
        n "So you came back."
        n "{i}Great{/i}."
        $ apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_PROLONGED_LEAVE)

    return

# Time-of-day based greetings

# Early morning

# Natsuki questions why the player is up so early
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_early_morning_why_are_you_here",
            unlocked=True,
            conditional="utils.get_current_hour() in range(3, 4)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_early_morning_why_are_you_here:
    n "H-{w=0.1}huh?{w=0.2} [player]?!"
    n "What the heck are you doing here so early?"
    n "Did you have a nightmare or something?"
    n "Or...{w=0.3} maybe you never slept?{w=0.2} Huh."
    n "Well,{w=0.1} anyway..."
    n "Morning,{w=0.1} I guess!{w=0.2} Ehehe."
    return

# Morning

# The Earth says hello!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_starshine",
            unlocked=True,
            conditional="utils.get_current_hour() in range(5, 11)",
            affinity_range=(jn_aff.ENAMORED, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_starshine:
    n "Good morning,{w=0.1} starshine!"
    n "The Earth says 'Hello!'"
    n "..."
    n "Pfffft-!"
    n "I'm sorry!{w=0.2} It's just such a dumb thing to say...{w=0.3} I can't keep a straight face!"
    n "Ehehe."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n "You really are my starshine though,{w=0.1} [chosen_endearment]."
    n "Welcome back!"
    return

# Natsuki doesn't like to be kept waiting around in the morning
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_waiting_for_you",
            unlocked=True,
            conditional="utils.get_current_hour() in range(5, 11)",
            affinity_range=(jn_aff.AFFECTIONATE, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_waiting_for_you:
    n "Oh! Well look who finally decided to show up!"
    n "You know I don't like being kept waiting...{w=0.3} right?"
    n "Ehehe.{w=0.2} You're just lucky I'm in a good mood."
    n "You better make it up to me,{w=0.1} [player]~!"
    return

# Natsuki doesn't like a lazy player!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_lazy",
            unlocked=True,
            conditional="utils.get_current_hour() in range(10, 11)",
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_lazy:
    n "Oho!{w=0.2} Well look who finally crawled out of bed today!"
    n "Jeez,{w=0.1} [player]...{w=0.3} I swear you're lazier than Sayori sometimes!"
    n "Ehehe."
    n "Well,{w=0.1} you're here now -{w=0.1} and that's all I care about."
    n "Let's make the most of today,{w=0.1} [player]!"
    n "Or...{w=0.3} what's left of it?"
    n "Ahaha."
    return

# Natsuki uses a silly greeting
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_top_of_the_mornin",
            unlocked=True,
            conditional="utils.get_current_hour() in range(8, 11)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_top_of_the_mornin:
    n "Oh!{w=0.2} It's [player]!"
    n "Well -{w=0.1} top of the mornin' to you!"
    n "..."
    n "What?{w=0.2} I'm allowed to say dumb things too,{w=0.1} right?"
    n "Ehehe."
    return

# Afternoon

# Natsuki hopes the player is keeping well
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_keeping_well",
            unlocked=True,
            conditional="utils.get_current_hour() in range(12, 17)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_keeping_well:
    n "Hey!{w=0.2} Afternoon,{w=0.1} [player]!"
    n "Keeping well?"
    return

# Natsuki asks how the player's day is going
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_how_are_you",
            unlocked=True,
            conditional="utils.get_current_hour() in range(12, 17)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_how_are_you:
    n "Oh!{w=0.2} Afternoon,{w=0.1} [player]!"
    n "How're you doing today?"
    return

# Evening

# Natsuki tells the player they can relax now
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_long_day",
            unlocked=True,
            conditional="utils.get_current_hour() in range(18, 21)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_long_day:
    n "Aha!{w=0.2} Evening,{w=0.1} [player]!"
    n "Long day,{w=0.1} huh?{w=0.2} Well,{w=0.1} you've come to the right place!"
    n "Just tell Natsuki all about it!"
    return

# Natsuki teases the player for taking so long
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_took_long_enough",
            unlocked=True,
            conditional="utils.get_current_hour() in range(18, 21)",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_took_long_enough:
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    n "[player]!{w=0.2} There you are,{w=0.1} [chosen_tease]!"
    n "Jeez...{w=0.3} took you long enough!"
    n "Ehehe."
    n "I'm just kidding!{w=0.2} Don't worry about it."
    n "Welcome back!"
    return

# Night

# Natsuki enjoys staying up late too
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_up_late",
            unlocked=True,
            conditional="utils.get_current_hour() >= 22 or utils.get_current_hour() <= 2",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_up_late:
    n "Oh!{w=0.2} Hey,{w=0.1} [player]."
    n "Late night for you too,{w=0.1} huh?"
    n "Well...{w=0.3} I'm not complaining!{w=0.2} Welcome back!"
    return

# Natsuki is also a night owl
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_night_owl",
            unlocked=True,
            conditional="utils.get_current_hour() >= 22 or utils.get_current_hour() <= 2",
            affinity_range=(jn_aff.NORMAL, jn_aff.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_night_owl:
    n "Oh,{w=0.1} [player]!{w=0.2} You're a night owl too,{w=0.1} are you?"
    n "Not that I have a problem with that,{w=0.1} of course - welcome back!"
    return