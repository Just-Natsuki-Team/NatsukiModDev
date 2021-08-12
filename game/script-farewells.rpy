default persistent._farewell_database = dict()

init python in farewells:
    import random
    import store

    # Natsuki will not ask a player to stay again if they agreed previously
    _player_already_stayed = False

    FAREWELL_MAP = dict()

    def get_farewell_in_affinity_range(farewell):
        """
        Returns true if player's persistent value is within the farewell topic's affinity range

        IN:
            farewell - The farewell topic to check
        """
        if store.persistent.affinity in range(farewell.affinity_range[0], farewell.affinity_range[1]):
            return True
            
        else:
            return False

    def get_farewell_has_no_stay_option(farewell):
        """
        Returns true if the farewell topic given has no has_stay_option attribute set,
        or if has_stay_option is set to False

        IN:
            farewell - The farewell topic to check
        """
        if not farewell.additional_properties["has_stay_option"]:
            return True

        else:
            return False

    def select_farewell():
        """
        Picks a random farewell, accounting for affinity.
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        farewells_in_affinity_range = filter(get_farewell_in_affinity_range, FAREWELL_MAP.values())
        if _player_already_stayed:
            
            return random.choice(filter(get_farewell_no_stay_option, farewells_in_affinity_range)).label

        else:
            return random.choice(farewells_in_affinity_range).label

# Maximum affinity farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_maximum_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_maximum_aff_1:
    n "Aww...{w=0.3} you're leaving now,{w=0.1} [player]?{w=0.2} Well,{w=0.1} okay..."
    n "Y-you know I'll miss you,{w=0.1} right?"
    n "Take care, [player]! You mean the world to me!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_maximum_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_maximum_aff_2:
    n "You know I don't like saying goodbye,{w=0.1} [player]..."
    n "..."
    n "I'll be okay!{w=0.2} Just come back soon,{w=0.1} alright?"
    n "Stay safe,{w=0.1} dummy!{w=0.2} I love you!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_maximum_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_maximum_aff_3:
    n "Uuuu...{w=0.3} I never like saying goodbye to you..."
    n "But I guess it can't be helped,{w=0.1} [player]."
    n "Take care of yourself out there!{w=0.2} I'm counting on you!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_maximum_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_maximum_aff_4:
    n "Oh?{w=0.2} You're heading out now?"
    n "That's fine,{w=0.1} I guess..."
    n "I'll really miss you,{w=0.1} [player]."
    n "Do your best,{w=0.1} sweetheart!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_maximum_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_maximum_aff_5:
    n "Huh?{w=0.2} You're leaving now?"
    n "I always hate it when you have to go somewhere..."
    n "...But I know you'll always be back for me,{w=0.1} [player]."
    n "Well...{w=0.1} I'm rooting for you!"
    n "Make me proud,{w=0.1} [player]! I love you!"
    return

# High affinity farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_high_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 699),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_high_aff_1:
    n "Hmm?{w=0.2} You're leaving now?"
    n "Aww,{w=0.1} man..."
    n "And I was having fun,{w=0.1} too..."
    n "Well,{w=0.1} if you gotta go,{w=0.1} you gotta go!"
    n "Take care,{w=0.1} [player]!{w=0.2} Make me proud!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_high_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 699),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_high_aff_2:
    n "You're going,{w=0.1} [player]?"
    n "Uuuuu...{w=0.3} okay..."
    n "Hurry back if you can,{w=0.1} alright?"
    n "I'll be waiting for you!"
    n "Goodbye,{w=0.1} [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_high_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 699),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_high_aff_3:
    n "Huh?{w=0.2} You're leaving?"
    n "..."
    n "That's fine...{w=0.3} I'll be okay..."
    n "You better come back soon,{w=0.1} alright [player]?"
    n "Goodbye!{w=0.2} I'll miss you!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_high_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 699),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_high_aff_4:
    n "Oh?{w=0.2} Heading off now,{w=0.1} [player]?"
    n "I wish you didn't have to..."
    n "But I know you have things to do."
    n "Come see me later,{w=0.1} promise?"
    n "Don't make me come find you!{w=0.2} Ehehe."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_high_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 699),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_high_aff_5:
    n "Mmm?{w=0.2} You're going now,{w=0.1} [player]?"
    n "I was hoping you'd be around longer..."
    n "Well,{w=0.2} I'll be okay!"
    n "Take care of yourself,{w=0.1} [player]!{w=0.2} For both of us!"
    n "See you later!"
    return

# Medium affinity farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_medium_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 599),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_medium_aff_1:
    n "Going now,{w=0.1} [player]?"
    n "No worries!{w=0.2} I'll see you later!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_medium_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 599),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_medium_aff_2:
    n "Heading off now,{w=0.1} [player]?"
    n "Okay!{w=0.2} Take care!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_medium_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 599),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_medium_aff_3:
    n "Okaaay!{w=0.2} I'll be waiting for you!"
    n "Stay safe,{w=0.1} [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_medium_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 599),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_medium_aff_4:
    n "See you later,{w=0.1} [player]!"
    n "Take care out there!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_medium_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 599),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_medium_aff_5:
    n "Goodbye,{w=0.1} [player]!"
    n "Come see me soon,{w=0.1} alright?"
    return

# Low affinity farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_low_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(0, 299),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_low_aff_1:
    n "See you later, [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_low_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(0, 299),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_low_aff_2:
    n "Later, [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_low_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(0, 299),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_low_aff_3:
    n "Goodbye, [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_low_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(0, 299),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_low_aff_4:
    n "'kay! Bye for now!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_low_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(0, 299),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_low_aff_5:
    n "See ya, [player]."
    return

# Minimum affinity farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_minimum_aff_1",
            unlocked=True,
            conditional=None,
            affinity_range=(-999, -1),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_minimum_aff_1:
    n "Yeah."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_minimum_aff_2",
            unlocked=True,
            conditional=None,
            affinity_range=(-999, -1),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_minimum_aff_2:
    n "Yep."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_minimum_aff_3",
            unlocked=True,
            conditional=None,
            affinity_range=(-999, -1),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_minimum_aff_3:
    n "Uh huh."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_minimum_aff_4",
            unlocked=True,
            conditional=None,
            affinity_range=(-999, -1),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_minimum_aff_4:
    n "..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_minimum_aff_5",
            unlocked=True,
            conditional=None,
            affinity_range=(-999, -1),
            additional_properties={
                "has_stay_option": False
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_minimum_aff_5:
    n "'Kay."
    return

# Farewells that allow the player to choose to stay

# Natsuki calls the player out on how long they've been here, and asks for more time together
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(100, 1000000),
            additional_properties={
                "has_stay_option": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n "What?{w=0.2} You're leaving?{w=0.2} But you've barely been here at all today,{w=0.1} [player]!"
    python:
        # Get the number of minutes the player has been here so far
        minutes_in_session = divmod((datetime.datetime.now() - current_session_start_time).total_seconds(), 60)[0]
        if minutes_in_session <= 1:
            time_in_session_descriptor = "like a minute"

        elif minutes_in_session <= 3:
            time_in_session_descriptor = "a couple of minutes"

        elif minutes_in_session > 3 and minutes_in_session <= 5:
            time_in_session_descriptor = "around five minutes"

        elif minutes_in_session > 5 and minutes_in_session <= 10:
            time_in_session_descriptor = "around ten minutes"

        elif minutes_in_session > 10 and minutes_in_session <= 15:
            time_in_session_descriptor = "around fifteen minutes"

        elif minutes_in_session > 15 and minutes_in_session <= 20:
            time_in_session_descriptor = "around twenty minutes"

        elif minutes_in_session <= 30:
            time_in_session_descriptor = "about half an hour"

    n "In fact, you've only been here for [time_in_session_descriptor]!"
    n "You're sure you can't stay just a little longer?"
    menu:
        "I can stay a little longer.":
            n "Yay{nw}!"
            n "I-I mean...!"
            n "Yeah!{w=0.2} That's what I thought!"
            n "Yeah..."
            n "..."
            n "Stop looking at me like that,{w=0.1} jeez!"
            n "Now,{w=0.1} where were we?"
            $ _player_already_stayed = True

        "Sorry, Natsuki. I really have to leave.":
            if minutes_in_session < 1:
                n "Nnnnnn-!"
                n "Well...{w=0.3} alright."
                n "Don't take too long,{w=0.1} alright?"
                n "See you later!"
            return

    return

# Natsuki tries to confidently ask her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(300, 1000000),
            additional_properties={
                "has_stay_option": True
            }
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n "Huh? You don't really have to leave already, do you?"
    n "It feels like you've barely been here!"
    n "I bet you can hang out with me a little longer! Right, [player]?"
    n "...right?"
    menu:
        "Right!":
            n "A-Aha!{w=0.2} I knew it!"
            n "I totally don't need you here,{w=0.1} or anything dumb like that!"
            n "You'd have to be pretty lonely to be {i}that{/i} dependent on someone else...{w=0.3} ahaha..."
            n "..."
            n "Jeez!{w=0.2} Let's just get back to it already..."
            n "Now,{w=0.1} where were we?"
            $ _player_already_stayed = True

        "Sorry, I really need to go.":
            n "Oh...{w=0.3} aha..."
            n "That's fine,{w=0.1} I guess..."
            n "I'll see you later then,{w=0.1} [player]!"
            n "Don't keep me waiting,{w=0.1} alright?"
            return
    return

# Natuski really doesn't want to be alone today; she pleads for her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(500, 1000000),
            additional_properties={
                "has_stay_option": True
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
            n "T-thanks, [player].{w=0.1} You're awesome,{w=0.1} you know that?"
            n "Really.{w=0.1} Thank you."
            n "N-now,{w=0.1} where were we? Heh..."
            $ _player_already_stayed = True

        "I can't right now.":
            n "Oh..."
            n "Well,{w=0.1} if you gotta go,{w=0.1} it can't be helped,{w=0.1} I guess..."
            n "Come back soon,{w=0.1} alright?"
            n "Or you'll have to make it up to me...{w=0.3} ahaha..."
            n "Stay safe,{w=0.1} [player]!"
            return
    return

# Natsuki gently asks her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional=None,
            affinity_range=(700, 1000000),
            additional_properties={
                "has_stay_option": True
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
            n "Truly.{w=0.1} Thanks..."
            n "..."
            n "Aha...{w=0.3} so what else did you wanna do today?"
            $ _player_already_stayed = True

        "Sorry, I really have to go.":
            n "Oh..."
            n "I'd be lying if I said I wasn't disappointed, but I understand."
            n "Just be careful out there, okay?"
            n "..."
            n "I-I love you,{w=0.1} [player]..."
            n "I'll see you later."
            return
    return