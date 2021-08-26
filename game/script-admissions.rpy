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
    last_admission_type = None

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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_ANGRY:
        n ""
        # TODO

    else:
        n ""
        # TODO

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_ANGRY
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_ANXIOUS:
        n "Still feeling anxious, [player]?"
        # TODO

    else:
        n "Feeling anxious, [player]?"
        # TODO

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_ANXIOUS
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_ASHAMED:
        n "[player]...{w=0.3} you're still feeling ashamed of yourself?"
        n "Well,{w=0.1} I'm not going to give up on you {i}that{/i} easily,{w=0.1} you know!"
        n "Just keep trying your best to put things right,{w=0.1} okay?"
        n "You can do it!{w=0.2} I know you can!"

    else:
        n "Huh?{w=0.2} What?"
        n "You're feeling...{w=0.3} ashamed?{w=0.2} Of yourself?"
        n "That's awful to hear,{w=0.2} [player].{w=0.2} Did you do something wrong?"
        n "Well...{w=0.3} whatever you did,{w=0.1} I'm sure you didn't mean it!"
        n "More importantly,{w=0.1} you're going to work hard to put things right.{w=0.2} I just know it!"
        n "So...{w=0.3} don't let me down,{w=0.2} okay?"
        n "And you aren't going to let yourself down either,{w=0.1} right?"
        menu:
            "Right!":
                n "Exactly.{w=0.2} Ehehe."

            "...":
                n "..."
                n "I don't think you get it,{w=0.1} [player]."
                n "Now,{w=0.1} repeat after me:{w=0.2} 'I'm not gonna let myself down!'"
                menu:
                    "I'm not gonna let myself down!":
                        n "See?{w=0.2} I knew you had it in you!{w=0.2} Ehehe."

        n "I believe in you,{w=0.1} [player]!"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_ASHAMED
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_CONFIDENT:
        n "Still full of confidence,{w=0.1} I see?"
        n "Well,{w=0.1} I'm glad to hear it!"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "You've got a lot to be confident of,{w=0.1} [player]."
            n "You better remember that!"

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_INSECURE:
        n "Really?{w=0.2} That's awesome,{w=0.1} [player]!"
        n "I was hoping you'd snap out of those feelings sooner rather than later."
        n "It worries me when you talk like that,{w=0.1} you know..."

        if jn_affinity.get_affinity_state() == store.jn_affinity.AFFECTIONATE:
            n "N-{w=0.1}not that I care {i}that{/i} much, o-{w=0.1}of course!"
            n "But...{w=0.3} I'm glad to know you're okay now,{w=0.1} [player]. That's what matters."

        elif jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "I'm just really glad to know you're better now,{w=0.1} [player]."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n "I love you, [chosen_endearment].{w=0.2} Please don't forget that,{w=0.1} alright?"
            n "I'll get mad if you do.{w=0.2} Ahaha..."

    else:
        n "Ahaha!{w=0.2} I'm glad to hear that,{w=0.1} [player]!"
        n "Being confident in yourself and your abilities can be really difficult sometimes."
        n "Especially if you messed up,{w=0.1} or if you aren't feeling well."
        n "But if you're feeling that way about yourself,{w=0.1} I'm not gonna rob you of it!"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_CONFIDENT
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_EXCITED:
        n "Still pumped up,{w=0.1} are we [player]?"
        n "I bet you just can't wait,{w=0.1} huh?{w=0.2} Ehehe."

    else:
        n "Oh?{w=0.2} Did something happen?{w=0.2} Is something {i}gonna{/i} happen?"
        n "Whatever it is,{w=0.1} I'm happy to hear you're looking forward to it!"
        n "It's always awesome to have something you can get excited over,{w=0.1} right?"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_EXCITED
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_HAPPY:
        n "Wow...{w=0.3} it's all sunshine and rainbows with you today,{w=0.1} isn't it?"
        n "Ahaha!"
        n "Keep on smiling,{w=0.1} [player]!"

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_ANGRY or admissions.last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "Feeling better now,{w=0.1} [player]?"
        n "I'm glad to hear it!{w=0.2} That's...{w=0.3} honestly a relief,{w=0.1} ahaha..."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
            n "..."
            n "So...{w=0.3} where were we?"

        else:
            n "..."
            n "Jeez...{w=0.3} if you're okay,{w=0.1} then let's get back to it already!"

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "Feeling better,{w=0.1} [player]?{w=0.2} I'm not surprised!"
        n "You just aren't yourself when you're hungry.{w=0.2} Ehehe."
        n "Trust me...{w=0.3} I would know."

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_SICK:
        n "Feeling better,{w=0.1} [player]?{w=0.2} I'm glad to hear it!"
        n "Nothing makes you appreciate feeling normal more than being sick,{w=0.1} right?"

    else:
        n "Oh?{w=0.1} Someone's in a good mood today!"
        n "Well,{w=0.1} I'm glad to hear it!"
        n "If you're happy,{w=0.1} I'm happy!"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_HAPPY
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "What?{w=0.1} You're still hungry?"
        n "Or did you not get something when I told you to earlier?"
        n "Well...{w=0.3} either way,{w=0.1} get off your butt and go get something then!"
        n "Jeez,{w=0.1} [player]...{w=0.3} I'm not your babysitter!"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "As much as you probably wish I was,{w=0.1} right?{w=0.2} Ahaha!"
            n "Now get going already!{w=0.2} Bon appetit,{w=0.1} [player]!"

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_SAD:
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
        n "Now go make something already!{w=0.2} Just don't fill yourself up on junk!"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "I want you fighting fit for when we hang out,{w=0.1} 'kay?"
            n "We're gonna have so much to do together,{w=0.1} after all!"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_HUNGRY
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_INSECURE:
        n "You're still feeling insecure about yourself,{w=0.1} [player]?"
        n "You remember what I said though,{w=0.1} right?"
        n "Everybody has their own pace.{w=0.2} I don't care what yours is.{w=0.2} We'll take it together."
        n "...Wow{w=0.1}, that seriously sounded super corny."
        n "But seriously,{w=0.1} [player]...{w=0.3} try not to sweat it,{w=0.1} okay?"
        n "The great Natsuki has your back,{w=0.1} after all!"

    else:
        n "Huh?{w=0.2} You're feeling insecure?{w=0.2} Where did that come from,{w=0.1} [player]?"
        n "..."
        n "I...{w=0.3} can't really comment on what made you feel that way..."
        n "But you better listen,{w=0.1} and listen good,{w=0.1} [player]."
        n "I don't care if people don't like you.{w=0.2} I like you."
        n "I don't care if people think you have no talents.{w=0.2} I know you do."
        n "I don't care if people think you're falling behind.{w=0.2} I know you'll catch up."
        n "Just...{w=0.3} give yourself time and space,{w=0.1} [player]."
        n "These thoughts you're having...{w=0.3} they can lead you to some really bad places.{w=0.2} Trust me."
        n "I won't let that happen without a fight{w=0.1} - {w=0.1}but you gotta fight with me,{w=0.1} [player].{w=0.2} Okay?"
        menu:
            "Okay.":
                n "Good.{w=0.2} Or you'll have me to deal with too.{w=0.2} Ahaha..."
                n "..."
                if jn_affinity.get_affinity_state() <= store.jn_affinity.AFFECTIONATE:
                    n "Message received?{w=0.2} T{w=0.1}-then let's get back to it already!"
                    n "Jeez..."

                else:
                    n "...You know I meant every single word I said,{w=0.1} right?"
                    n "So please...{w=0.3} don't give up.{w=0.2} We both need you to win,{w=0.1} [player]."

                    if jn_affinity.get_affinity_state() == store.jn_affinity.LOVE:
                        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                        n "I really do love you, [chosen_endearment]."

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_INSECURE
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_PROUD:
        n "Really,{w=0.1} [player]?{w=0.1} Still gloating,{w=0.1} are we?"
        n "You {i}do{/i} know what they say about pride,{w=0.1} right?"
        n "..."
        n "I'm just kidding,{w=0.1} [player]!{w=0.2} Jeez!"
        n "You should see your face!{w=0.2} Ehehe."
        n "Well,{w=0.1} I'm glad you're still feeling good about yourself!"

    else:
        n "Oh?{w=0.2} You're feeling proud,{w=0.1} huh?"
        n "You must be pretty pleased with yourself to brag to me about it.{w=0.2} Ahaha!"
        n "I'm sure whatever it is,{w=0.1} it's something I can be proud of you for too."
        n "Good work,{w=0.1} [player]!"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_PROUD
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "Oh...{w=0.3} I'm really sorry to hear you're still feeling upset,{w=0.1} [player]."
        # TODO

    else:
        n "Oh...{w=0.3} I'm really sorry to hear you're upset,{w=0.1} [player]."
        # TODO

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_SAD
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_SICK:
        n "[player]...{w=0.3} you're still feeling sick?"
        n "How long have you felt like this now?"
        menu:
            "A few hours.":
                n "That's...{w=0.3} not great to hear,{w=0.1} [player]."
                n "Perhaps you should get some rest soon{w=0.1} -{w=0.1} hopefully you'll feel better."
                n "Let me know if it keeps up,{w=0.1} okay?"

            "A few days.":
                n "You're starting to worry me,{w=0.1}  [player]."
                n "Make sure you see someone soon."
                n "Especially if you start to hurt anywhere,{w=0.1}  or if you've been sick,{w=0.1}  or anything like that..."
                n "Make sure you get some extra rest too,{w=0.1} okay?"

            "A week or so.":
                n "[player]..."
                n "Have you seen anybody about this yet?"

                menu:
                    "Yes, I have.":
                        n "Well...{w=0.3} okay."
                        n "I really,{w=0.1} really hope they were able to help you,{w=0.1} [player]."
                        n "Make sure you get some extra rest,{w=0.1} okay?"

                    "No, I haven't.":
                        n "[player]...{w=0.3} that's no good."
                        n "I trust you know your own limits...{w=0.3} but please,{w=0.1} take care of yourself."
                        n "Your health...{w=0.3} really matters to me."

            "Longer.":
                n "..."
                n "I...{w=0.3} don't really know what to say to you,{w=0.1} [player]."
                n "I just hope you feel better soon."
                n "Take it easy,{w=0.1} alright?"

                if jn_affinity.get_affinity_state() == store.jn_affinity.AFFECTIONATE:
                    n "I hate seeing you unwell like this..."

                elif jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
                    n "It really hurts me seeing you unwell like this..."

                if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
                    n "I love you,{w=0.1} [player].{w=0.2} Please get well soon."

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "You know,{w=0.1} you can start to feel unwell if you haven't eaten for a while,{w=0.1} [player]."
        n "Have you eaten something today?{w=0.2} Like a proper meal?"
        menu:
            "Yes, I have.":
                n "Hmmm...{w=0.3} maybe it was something you ate that's making you feel sick?"
                n "Take a lie down if you need to,{w=0.1} [player].{w=0.2} Alright?"

            "No, I haven't.":
                n "Hmmm...{w=0.3} maybe you should have something now,{w=0.1} [player]."
                n "Even something small like some candy.{w=0.2} Just to get your energy level up."
                n "Can you do that for me,{w=0.1} [player]?"
                n "I'm counting on you!"

    else:
        n "Feeling under the weather,{w=0.1} [player]?"
        n "I wish there was something I could do to help..."
        n "You aren't straining yourself by being here,{w=0.1} are you?"
        n "I don't wanna get in the way of you feeling better."
        n "Your health has to come first over our time together."
        n "So...{w=0.3} promise me you'll leave and rest if you have to,{w=0.1} okay?"

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_SICK
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
    if admissions.last_admission_type == admissions.ADMISSION_TYPE_TIRED:
        n "Huh?{w=0.2} You're still tired?"
        n "Did you not get any rest,{w=0.1} [player]?"
        n "I don't want you getting all cranky..."
        n "So...{w=0.3} go back to bed, alright?"
        n "I'll see you later,{w=0.1} [player]!"

        $ persistent.jn_player_admission_type_on_quit = admissions.ADMISSION_TYPE_TIRED
        return { "quit": None }

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_ANGRY or admissions.last_admission_type == admissions.ADMISSION_TYPE_SAD:
        n "You said you weren't happy earlier,{w=0.1} [player]..."
        n "If you're already tired,{w=0.1} I think you should sleep on it."
        n "Are you gonna turn in,{w=0.1} [player]?"
        menu:
            "Yes, I will.":
                n "Good...{w=0.3} you'll feel better soon,{w=0.1} okay?{w=0.2} I promise."
                n "Sleep well,{w=0.1} [player]!"
                $ persistent.jn_player_admission_type_on_quit = admissions.ADMISSION_TYPE_TIRED
                return { "quit": None }

            "No, not yet.":
                n "Well...{w=0.3} if you're sure,{w=0.1} [player]."
                n "Let's see if I can't improve your mood,{w=0.1} shall we?"

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_SICK:
        n "I'm really not surprised if you're already sick,{w=0.1} [player]."
        n "You should really go get some rest."
        n "We can talk later,{w=0.1} alright?"
        n "Take it easy,{w=0.1} [player]!"

        $ persistent.jn_player_admission_type_on_quit = admissions.ADMISSION_TYPE_SICK
        return { "quit": None }

    elif admissions.last_admission_type == admissions.ADMISSION_TYPE_HUNGRY:
        n "I'm not surprised you're feeling tired if you're hungry!"
        n "Stop sitting around and go eat something,{w=0.1} [player]."
        n "Just take it easy getting up,{w=0.1} alright?{w=0.2} I don't want you fainting on me."
        n "And trust me,{w=0.1} I don't think you want that either..."

    else:
        n "Feeling tired,{w=0.1} [player]?"
        n "Perhaps you should think about turning in soon{w=0.1} -{w=0.1} even if it's just a nap!"
        n "Don't worry about me if you need to rest!{w=0.2} I'll be alright."
        n "Just make sure you let me know when you decide to go,{w=0.1} [player]."

    $ admissions.last_admission_type = admissions.ADMISSION_TYPE_TIRED
    return
