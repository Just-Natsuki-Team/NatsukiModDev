default persistent._topic_database = dict()

init python in topics:
    import store
    TOPIC_MAP = dict()

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="classroom_topic_example1",
            unlocked=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label classroom_topic_example1:
    n "classroom1"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="classroom_topic_example2",
            unlocked=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label classroom_topic_example2:
    python:
        affinity_index_and_descriptor = {
            1:"RUINED",
            2:"BROKEN",
            3:"DISTRESSED",
            4:"UPSET",
            5:"NORMAL",
            6:"HAPPY",
            7:"AFFECTIONATE",
            8:"ENAMORED",
            9:"LOVE"
        }
        affinity_tier = affinity_index_and_descriptor[store.jn_globals.current_affinity_state]
    n "Your affinity is: [persistent.affinity], and your trust is: [persistent.trust]!"
    n "I'd describe your affinity as [affinity_tier]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example1",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label beach_topic_example1:
    n "beach1"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="beach_topic_example2",
            unlocked=True,
            location="beach"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label beach_topic_example2:
    n "beach2"
    return

# Talk menu topics

# This topic allows us to (temporarily!) set a custom affinity value
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_affinity",
            unlocked=True,
            prompt="Can you change my affinity state?",
            conditional=None,
            category=["Debug"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_affinity:
    n "Okaaay! Just tell me what affinity state you want!"
    menu:
        "LOVE":
            $ store.jn_globals.current_affinity_state = 9
            n "Alright! Your affinity state is now LOVE!" # Yesssssss

        "ENAMORED":
            $ store.jn_globals.current_affinity_state = 8
            n "Alright! Your affinity state is now ENAMORED!"

        "AFFECTIONATE":
            $ store.jn_globals.current_affinity_state = 7
            n "Alright! Your affinity state is now AFFECTIONATE!"

        "HAPPY":
            $ store.jn_globals.current_affinity_state = 6
            n "Alright! Your affinity state is now HAPPY!"

        "NORMAL":
            $ store.jn_globals.current_affinity_state = 5
            n "Alright! Your affinity state is now NORMAL!"

        "UPSET":
            $ store.jn_globals.current_affinity_state = 4
            n "Alright! Your affinity state is now UPSET!"

        "DISTRESSED":
            $ store.jn_globals.current_affinity_state = 3
            n "Alright! Your affinity state is now DISTRESSED!"

        "BROKEN":
            $ store.jn_globals.current_affinity_state = 2
            n "Alright! Your affinity state is now BROKEN!"

        "RUINED":
            $ store.jn_globals.current_affinity_state = 1
            n "Alright! Your affinity state is now RUINED!" # How could you :(

        "Nevermind.":
            n "Oh...{w=0.3} well, alright then."

    return

# This topic allows us to (temporarily!) set a custom trust value
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_trust",
            unlocked=True,
            prompt="Can you change my trust?",
            conditional=None,
            category=["Debug"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_trust:
    n "Sure! Just tell me what trust value you want!"
    python:
        trust_to_set = renpy.input("Enter a trust value (current: {0}):".format(persistent.trust))
        try:
            persistent.trust = float(trust_to_set)
            renpy.say(n, "Alright! Your new trust is [persistent.trust]!")

        except:
            renpy.say(n, "Hmm... sorry, I can't seem to read that. Make sure you enter an integer or decimal value, 'kay?")
    return

# Natsuki's thoughts on having her picture taken via the ingame screenshot system
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_having_pictures_taken",
            unlocked=True,
            prompt="How do you feel about having your picture taken?",
            conditional=None,
            category=["Natsuki", "Photography", "Life"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_having_pictures_taken:

    if not persistent.jn_first_screenshot_taken:
        n "W-wait...{w=0.3} you're telling me there's a camera here?{w=0.2} Are you kidding me?!"
        n "Uuuu-"
        n "I've never liked having my picture taken without my permission..."
        n "Just...{w=0.3} please don't take any pictures of me unless I ask,{w=0.1} okay [player]?"
        n "It'd really mean a lot to me."
        n "I hope you can understand."

    else:
        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Hmm?{w=0.2} Pictures of me?"
            n "Honestly,{w=0.1} I don't think I'll ever be completely comfortable with them..."
            n "But I trust you to make a good shot!"
            n "As long as you ask,{w=0.1} I've got no problem with it!"

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.NORMAL, store.jn_affinity.AFFECTIONATE)
        ):
            if player_screenshots_blocked:
                n "Really, [player]?{w=0.1} You're asking me about this {i}now{/i}?"
                n "You know {i}perfectly well{/i} how I feel about this."
                n "I don't hate you,{w=0.1} but please try to remember how I feel before you do stuff like that."
                n "I'm still gonna keep that turned off for now."

            else:
                n "H-huh?{w=0.2} Pictures of me?"
                n "Not a fan,{w=0.1} honestly -{w=0.1} but you knew that much already,{w=0.1} [player]."
                n "It's just..."
                n "I really...{w=0.3} need...{w=0.3} my privacy.{w=0.1} It matters a lot to me."
                n "You understand,{w=0.1} right?"
                n "So please,{w=0.1} if you ever wanna take a picture,{w=0.1} can you ask me first?"
                menu:
                    "Of course!":
                        n "Thanks,{w=0.1} [player]."
                        n "That really...{w=0.3} means a lot to me."

                    "I'll think about it.":
                        n "[player]...{w=0.3} come on.{w=0.1} I'm being serious here."
                        n "Please don't mess me around with this."
                        n "Make sure you ask,{w=0.1} okay?"

                    "...":
                        n "..."
                        n "Uh...{w=0.3} [player]?{w=0.1} This isn't very funny."
                        n "Make sure you ask,{w=0.1} okay?{w=0.1} For my sake."

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.UPSET, store.jn_affinity.DISTRESSED)
        ):
            n "Pictures? Really?"
            n "I don't think I want to have you taking my picture,{w=0.1} [player]."
            n "Let's talk about something else."

        else:
            n "Please...{w=0.3} don't try to pretend like you care about how I feel about pictures."
            n "I'm done talking about this,{w=0.1} [player]."
    return

# Ask Natsuki for permission to take a picture of her, or have her call out the player if permission already given!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_get_picture_permission",
            unlocked=True,
            prompt="Can I take a picture of you?",
            conditional="persistent._jn_first_screenshot_taken != None",
            category=["You", "Photography"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_get_picture_permission:
    # The player was warned!
    if store.jn_screenshots.player_screenshots_blocked:
        n "Uh...{w=0.3} no,{w=0.1} I'm not turning the camera back on,{w=0.1} [player]."
        return

    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        if store.jn_screenshots.player_screenshots_permission:
            n "Ahaha!{w=0.2} I already said you could,{w=0.1} dummy!"
            n "I'm ready,{w=0.1} so take one whenever!"

        else:
            n "Eh?{w=0.2} A picture?{w=0.2} Of course!"
            $ store.jn_screenshots.player_screenshots_permission = True
        return

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
        if store.jn_screenshots.player_screenshots_permission:
            n "Huh?{w=0.2} Didn't you ask me that already?"
            n "It's fine,{w=0.1} so go ahead!"

        else:
            n "Oh?{w=0.2} You wanna take a picture?{w=0.2} Alright!"
            $ store.jn_screenshots.player_screenshots_permission = True
        return

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.HAPPY:

        if player_screenshots_permission:
            n "Hmm?{w=0.2} A picture?{w=0.2} Well,{w=0.1} okay."
            $ store.jn_screenshots.player_screenshots_permission = True

        else:
            n "Uuuu...{w=0.3} I just said you could,{w=0.1} [player]."
            n "Just take it whenever,{w=0.1} alright?"
        return

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.UPSET:
        if store.jn_screenshots.player_screenshots_permission:
            n "Eh?{w=0.2} I already said you could,{w=0.1} [player]. Just take it soon,{w=0.1} alright?"
            n "I don't really like being kept on hold like this..."

        else:
            # Indecisive; this lets lower affinity players have a chance at screenshots without upsetting Natsuki
            n "A picture?{w=0.2} I'm not sure...{w=0.3} let me think about it."
            n "..."
            # We take into account the player's behaviour with pictures so far
            $ natsuki_approves = random.randint(1, 100) <= (100 - (jn_screenshots.bad_screenshot_streak * 25))
            if natsuki_approves:
                n "Fine,{w=0.1} I guess.{w=0.1} Take it whenever."
                $ store.jn_screenshots.player_screenshots_permission = True

            else:
                n "I'm sorry,{w=0.1} [player].{w=0.1} I don't want any pictures taking of me right now."
                $ store.jn_screenshots.player_screenshots_permission = False
        return

    elif jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
        n "No.{w=0.1} I {b}don't{/b} want my picture taken."
        $ store.jn_screenshots.player_screenshots_permission = False
        return

    else:
        n "..."
        $ store.jn_screenshots.player_screenshots_permission = False

    return

# Natsuki discusses her lack of pet with the player, and asks about theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="Did you ever have any pets?",
            conditional=None,
            category=["Natsuki", "Life", "Animals", "Family"],
            player_says=True,
            affinity_range=(store.jn_aff.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:

    # Check to see if the player and Natsuki have already discussed this
    $ already_discussed_pets = False
    if get_topic("talk_did_you_have_pets"):
        $ already_discussed_pets = get_topic("talk_did_you_have_pets").shown_count > 0

    if already_discussed_pets:
        n "Wait...{w=0.3} didn't we talk about this before,{w=0.1} [player]?"
        n "Well anyway,{w=0.1} not much has changed."
        n "I still don't have a pet,{w=0.1} as much as I wish I did."
        n "Maybe I should get one soon. Hmm..."

    else:
        n "Huh?{w=0.2} Did I ever have any pets?"
        n "You know,{w=0.1} I really wish I had.{w=0.1} But I was never allowed anything!"
        n "It was always about the mess it would make,{w=0.1} or how much it would cost,{w=0.1} or literally anything else they could think of..."
        n "Even when I said {i}I'd{/i} take care of everything!"
        n "Ugh..."
        n "It still annoys me...{w=0.3} but then again,{w=0.1} it's not like I can't keep a pet here instead,{w=0.1} right?{w=0.1} Ehehe."

    if persistent.jn_player_pet is None:
        n "What about you,{w=0.1} [player]?{w=0.2} Do you have any pets?"
        menu:
            "Yes, I do.":
                n "Oh!{w=0.2} Oh oh oh!{w=0.2} You gotta tell me,{w=0.1} [player]!"
                n "What do you have?{w=0.2} What do you have?"
                call pet_options_a

            "No, I don't.":
                n "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n "I wanna hear all about it!"

            "I used to.":
                n "Oh...{w=0.3} oh gosh."
                n "I'm really sorry to hear that,{w=0.1} [player]."
                n "I hope you're managing okay now."
                n "..."
                n "I...{w=0.3} think we should talk about something else, alright?"

    else:
        n "What about you,{w=0.1} [player]?"
        n "Did you get another one?"
        menu:
            "Yes, I did.":
                n "Ooh...{w=0.3} you gotta tell me!{w=0.2} What did you get?"
                call pet_options_a

            "No, I didn't.":
                n "Oh.{w=0.2} Well,{w=0.1} that's fair."
                n "You're already giving a home to something,{w=0.1} so I won't complain!"

            "I lost one.":
                n "Oh...{w=0.3} oh jeez..."
                n "I'm so sorry,{w=0.1} [player].{w=0.2} Are you okay?"
                n "Maybe we should talk about something else to keep your mind off things..."
                n "I'm here for you,{w=0.1} [player]."

    return

label pet_options_a:
    menu:
        "Birds":
            n "Oh!{w=0.2} Neat!"
            n "I don't think I'd keep birds myself,{w=0.1} but they brighten up rooms for sure!"
            n "It doesn't get too noisy for you,{w=0.1} I hope?"
            n "I'm sure yours appreciate your company though."
            $ persistent.jn_player_pet = "birds"

        "Cats":
            n "Yay!{w=0.2} Cats!"
            n "I really wish I had one,{w=0.1} I love seeing all the dumb situations they get into!"
            n "I hope you didn't just say that because I like them,{w=0.1} though.{w=0.1} Ehehe."
            n "Just don't pamper it too much,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "cats"

        "Dogs":
            n "Oh!{w=0.2} A dog?{w=0.2} Awesome!"
            n "I don't think a dog would be my first choice,{w=0.1} what with all the walks and all that."
            n "But I can't think of a more loving pet!"
            n "I hope yours looks after you as much as you look after it!"
            $ persistent.jn_player_pet = "dogs"

        "Fish":
            n "Ooh!{w=0.2} Fish are interesting!"
            n "I don't think I'd call them super affectionate personally..."
            n "But I think they're a neat way to relieve stress!{w=0.2} They must be calming to watch in their own little world."
            n "I bet you feel like you could lose yourself in that tank!{w=0.2} Ehehe."
            $ persistent.jn_player_pet = "fish"

        "Gerbils":
            n "Awww!{w=0.2} I like gerbils!"
            n "It's so cute how they live in little groups to keep each other company."
            n "They're good at digging,{w=0.1} too -{w=0.2} like seriously good!"
            n "Take good care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "gerbils"

        "More...":
            call pet_options_b

    return

label pet_options_b:
    menu:
        "Guinea pigs":
            n "Ooh!{w=0.2} I like guinea pigs!"
            n "I don't know much about them,{w=0.1} but I love the little sounds they make."
            n "It's like they're always having a conversation!"
            n "Take good care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "guinea pigs"

        "Hamsters":
            n "Oh my gosh!{w=0.2} Hammies!"
            n "Aaaaaah!{w=0.2} I love them so much!"
            n "I love their little tails,{w=0.1} and their little paws,{w=0.1} and their little whiskers,{w=0.2} and-"
            n "And!{w=0.2} And..."
            n "..."
            n "A-{w=0.1}ahaha!{w=0.2} It would appear I got a little carried away..."
            n "..."
            n "You better take good care of yours for me,{w=0.1} alright?"
            $ persistent.jn_player_pet = "hamsters"

        "Horses":
            n "W-{w=0.1}wow!{w=0.2} You aren't just messing with me,{w=0.1} right?!"
            n "Horses?!{w=0.2} That's amazing,{w=0.1} [player]!"
            n "You totally gotta teach me how to ride some day!"
            n "Make sure you visit yours often,{w=0.1} alright?"
            n "Oh -{w=0.2} and wear a helmet if you ride!"
            $ persistent.jn_player_pet = "horses"

        "Insects":
            n "Ack-{nw}"
            n "Nnnnn..."
            n "...I wish I could share your enthusiasm!{w=0.2} Ahaha..."
            n "I don't think I could stomach creepy crawlies myself."
            n "You've certainly got an...{w=0.3} interesting taste,{w=0.1} [player]."
            n "But I'm sure you take great care of yours!"
            $ persistent.jn_player_pet = "insects"

        "Mice":
            n "Ehehe.{w=0.2} Mice are adorable!"
            n "I'm still not sure how I feel about the tail..."
            n "But they're so curious and sociable!{w=0.2} I love watching them play together."
            n "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "mice"

        "More...":
            call pet_options_c

        "Back...":
            call pet_options_a

    return

label pet_options_c:
    menu:
        "Rats":
            n "Rats,{w=0.1} huh?"
            n "Were you expecting me to be grossed out?"
            n "Ahaha!"
            n "Rats are fine.{w=0.2} They're surprisingly intelligent,{w=0.1} too!"
            n "Are you perhaps training yours,{w=0.1} [player]?{w=0.2} Ehehe."
            n "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "rats"

        "Rabbits":
            n "Awwwwww!{w=0.2} Bunnies!"
            n "They're so cuuute!{w=0.2} I love them!"
            n "Especially the ones with the floppy ears,{w=0.1} they look so cuddly!"
            n "It's a shame they need so much space,{w=0.1} though."
            n "But I'm sure yours have plenty of room to roam!{w=0.2} Ehehe."
            $ persistent.jn_player_pet = "rabbits"

        "Something else":
            n "Ooh!{w=0.2} An exotic owner, are we?"
            n "I wonder if that says something about the rest of your tastes?{w=0.2} Ehehe."
            n "I trust you take good care of yours.{w=0.1} Uncommon pets can be pretty demanding!"
            $ persistent.jn_player_pet = "something_else"

        "Back...":
            call pet_options_b

    return

# Natsuki discusses service animals with the player, in particular emotional support animals
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_service_animals",
            unlocked=True,
            prompt="Service animals",
            conditional=None,
            category=["Life", "Animals", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_service_animals:
    n "Hmm..."
    n "Hey [player],{w=0.1} have you ever heard of service animals?"
    n "They're like animals people train up specially to do jobs that humans can't do easily."

    if jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
        n "Some work in airports to keep people safe,{w=0.1} others help in rescues...{w=0.3} it's super cool!"
        n "But there's one type that's especially awesome..."
        n "Emotional support animals!"
        n "They're like really tame pets that are used to comfort people going through a bad time."
        n "They come in all different shapes and sizes too!{w=0.2} Dogs and cats -{w=0.2} obviously -{w=0.2} but even horses sometimes!"
        n "Isn't that amazing?"
        n "..."
        n "You know,{w=0.1} [player]..."
        n "Sometimes I wonder if one could have helped Sayori..."
        n "...but I try not to think about that too much."
        n "They {i}are{/i} great,{w=0.1} but they don't do miracles."
        n "[player]...{w=0.3} I really hope you never have to seek their help."
        n "And on that note,{w=0.1} if you do need support?"
        n "...I'd be happy to provide.{w=0.2} Remember that,{w=0.1} alright?"

        if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
            n "I really,{w=0.1} really care about you,{w=0.1} [player]."
            n "I-{w=0.2}I want you to know that you can depend on me,{w=0.1} 'kay?"

        if jn_affinity.get_affinity_state() == store.jn_affinity.LOVE:
            n "I love you,{w=0.1} [player]."

    else:
        n "They work in a bunch of places.{w=0.2} Airports and rescues and stuff,{w=0.1} usually."
        n "But I really like emotional support animals."
        n "They're like specially tame pets that are used to comfort those having a bad time."
        n "..."
        n "You know, [player].{w=0.2} To be perfectly honest with you?"
        n "Sometimes I feel like I could use one."
        n "Aha..."

    n "..."
    n "That got kinda heavy,{w=0.1} didn't it?"
    n "Well,{w=0.1} enough of that.{w=0.2} What else should we talk about?"
    return

# Natsuki highlights her concern for her player using their computer for long periods of time, and offers her wisdom
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_computers_healthily",
            unlocked=True,
            prompt="Using computers healthily",
            conditional="store.utils.get_current_session_length().total_seconds() / 3600 >= 8",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    n "Huh."
    n "Hey,{w=0.1} [player].{w=0.2} I just thought of something."
    n "You gotta be at your computer to talk to me,{w=0.1} right?"
    n "And you've been here a while already..."
    n "Alright,{w=0.1} that's it!{w=0.2} I've decided."
    n "I'm gonna give you a little lesson on using your computer the right way!"
    n "Number one:{w=0.2} posture!"
    n "Sit up straight,{w=0.1} and back against the chair,{w=0.1} [player].{w=0.2} I mean it!"
    n "You don't want back problems,{w=0.1} do you?"
    n "Make sure your feet can still touch the floor,{w=0.1} though.{w=0.2} Even I can do that!"
    n "Number two:{w=0.2} distance!"
    n "I know you can't get enough of me,{w=0.1} but I don't wanna see you pressing your face against the screen.{w=0.2} It's weird."
    n "So make sure you sit about an arm's length away from the display,{w=0.1} alright?"
    n "Oh!{w=0.2} Don't forget to keep your stuff in easy reach though{w=0.1} - {w=0.1}like your mouse."
    n "Number three:{w=0.2} breaks!"
    n "I don't know about you,{w=0.1} but I get all fidgety if I stay still too long..."
    n "So make sure you get off your butt and do some stretches a few times per hour!"
    n "You could even get some water or something if you {i}really{/i} need an excuse to move."
    n "It'd also give your eyes a rest from the screen!"
    n "Alright{w=0.1} -{w=0.1} and the last one!{w=0.2} This one's important,{w=0.1} so listen up good!"
    n "If you ever feel unwell{w=0.1} - {w=0.1}like your back aches,{w=0.1} or your eyes hurt or something..."
    n "Please just stop whatever you're doing.{w=0.2} Your health comes first.{w=0.2} I don't care what needs to be done."
    n "Take some time to feel better,{w=0.1} then make sure all your stuff is set up right like I said."
    n "Don't carry on until you feel well enough{w=0.1} -{w=0.1} talk to someone if you have to!"
    n "Okaaay!{w=0.2} Lecture over!"
    n "Wow...{w=0.3} I rambled on a while,{w=0.1} didn't I?{w=0.2} Sorry,{w=0.1} sorry!{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n "But you know I only do these things because I really care about you,{w=0.1} [player]...{w=0.3} right?"
        n "So please...{w=0.3} take care of yourself, okay?{w=0.2} I don't want you hurting because of me."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n "I love you,{w=0.1} [chosen_endearment]."
            n "..."

    else:
        n "But you know I only say these things because I care."
        n "...And I don't want you whining to me that your back hurts.{w=0.2}"

    n "Ahaha...{w=0.3} now, where were we?"
    return

# Natsuki highlights the importance of staying active and getting exercise
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_active",
            unlocked=True,
            prompt="Staying active",
            conditional="persistent.jn_total_visit_count >= 10",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_active:
    n "Hey,{w=0.1} [player]..."
    n "You should get out more."
    n "..."
    n "Ahaha!{w=0.2} No,{w=0.1} really!{w=0.2} I'm serious!"
    n "At school,{w=0.1} it's easy to get exercise since we gotta walk everywhere,{w=0.1} and we have sports and such..."
    n "I don't think it's so straightforward when you have a job and other stuff to worry about,{w=0.1} though."
    n "I'm not gonna lie and say I work out or anything like that..."
    n "But I try to get walks in if I can.{w=0.2} Any excuse to hit the bookshop is reason enough for me!"
    n "You should give it a shot too,{w=0.1} [player]!"
    n "It doesn't have to be a hike or anything crazy{w=0.1} - {w=0.1}it's more about keeping at it,{w=0.1} really."
    n "Even a daily ten minute walk will help you feel refreshed and awake!"
    n "So make sure you get out soon,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
        n "I wanna see you fighting fit!{w=0.2} Ehehe."

    n "I'm counting on you!"
    return

# Natsuki discusses stress and offers ways she finds useful to deal with it
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_relieving_stress",
            unlocked=True,
            prompt="Relieving stress",
            conditional=None,
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_relieving_stress:
    n "You know,{w=0.1} I'll admit it,{w=0.1} [player]."
    n "I...{w=0.3} kinda have a short fuse.{w=0.2} Ehehe."
    n "I've been trying to work on that though,{w=0.1} and I'd love to share some of the ways I deal with stess!"
    n "Personally,{w=0.1} I think the best way to deal with it if you can is to try and create some distance."
    n "If things get a little too much,{w=0.1} I just step outside if I can."
    n "Some fresh air and a change of scenery can really put things into context.{w=0.2} It's crazy effective!"
    n "Don't just create physical distance,{w=0.1} though.{w=0.2} Distance yourself mentally too!"
    n "If something is stressing you out,{w=0.1} you need to starve it of some attention."
    n "If I can't go somewhere else,{w=0.1} I just read something,{w=0.1} or watch some dumb videos."
    n "But do whatever works for you{w=0.1} - {w=0.1}we all have our own comfort zones!"
    n "And of course,{w=0.1} you could always come see me,{w=0.1} you know..."

    if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
        n "I-{w=0.1}It'd be a welcome surprise.{w=0.2} Ahaha..."

    n "A-{w=0.1}anyway!"
    n "The point is to always try and come back with a clean headspace,{w=0.1} and don't sweat the small things."
    n "Can you do that for me,{w=0.1} [player]?"
    n "I'll keep working on it if you do!"
    return

# Natsuki muses on how easy it is to waste money, and offers some guidance on spending wisely
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_careful_spending",
            unlocked=True,
            prompt="Careful spending",
            conditional=None,
            category=["Life", "You", "Health", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_careful_spending:
    n "..."
    n "..."
    n "Hmm...?"
    n "O-{w=0.1}oh!{w=0.2} Sorry!{w=0.2} I spaced out!"
    n "I was just thinking..."
    n "It's so easy to spend more than you mean nowadays,{w=0.1} you know?"
    n "Like...{w=0.3} it seems everywhere you go,{w=0.1} there's a sale,{w=0.1} or deals,{w=0.1} or some kind of limited offer..."
    n "And everywhere accepts all kinds of ways of paying,{w=0.1} too.{w=0.2} They make it super convenient!"
    n "I guess what I'm getting at is...{w=0.3} try to be careful of your spending habits,{w=0.1} okay?"
    n "Try not to buy junk you don't need{w=0.1} -{w=0.1} think of how much you threw away the last time you cleaned out!"
    n "T-{w=0.1}that's not to say you shouldn't treat yourself,{w=0.1} of course!{w=0.2} You deserve cool stuff too!"
    n "Money can't buy happiness...{w=0.3} but it sure as hell makes finding it easier.{w=0.2} Ahaha!"
    n "Well, anyway.{w=0.2} Just try to think a little before you spend,{w=0.1} [player]{w=0.1} -{w=0.1} that's all I'm saying!"

    if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
        n "Besides..."
        n "Gotta save up all we can for when we hang out,{w=0.1} right?{w=0.2} Ehehe."

    return

# Natsuki discusses the importance of not only eating healthily, but regularly too
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_eating_well",
            unlocked=True,
            prompt="Eating well",
            conditional=None,
            category=["Life", "You", "Health", "Food"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n "Hey,{w=0.1} [player]..."
    n "Have you eaten today?"
    menu:
        "Yes":
            n "Aha!{w=0.2} But did you eat {i}well{/i},{w=0.1} [player]?"

        "No":
            n "Huh?{w=0.2} What?{w=0.2} Why not?!"
            n "You aren't skipping meals,{w=0.1} are you?"
            n "I really hope you aren't,{w=0.1} [player]..."

    n "It's super important to make sure you aren't only eating regularly,{w=0.1} but eating decently too!"
    n "I think the right diet can honestly make all the difference,{w=0.1} [player]."
    n "So...{w=0.3} try and make an effort with your meals,{w=0.1} okay?"
    n "And I mean a real effort!{w=0.2} Try to prepare them from scratch if you can;{w=0.1} it's often cheaper than ready meals anyway!"
    n "Try to cut back on things like salt and sugar and stuff too...{w=0.3} as well as anything really processed."
    n "Oh {w=0.1}-{w=0.1} and like I said,{w=0.1} have meals regularly too!"
    n "You shouldn't find yourself snacking on junk if you have proper meals throughout the day."
    n "Your bank balance and your body will thank you too!{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
        n "And besides..."
        n "I gotta get you into good habits by yourself before I'm there to make you."
        n "Ahaha!{w=0.2} I'm kidding,{w=0.1} [player]!{w=0.2} I'm kidding!"
        n "...Mostly."

        if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Love you, [player]~!{w=0.2} Ehehe."

    n "Now...{w=0.3} where were we?"
    return

# Natsuki brings up the idea of in-game weather, and guides the player through installation
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_weather_setup_part1",
            unlocked=True,
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            category=["one-time", "weather"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_weather_setup_part1:

    # Set flags for how the player replied to Natsuki
    $ player_was_rude = False
    $ player_was_quiet = False

    # Determine if the player already went through any part of the setup here
    $ already_discussed_setup = False
    if get_topic("talk_weather_setup_part1"):
        $ already_discussed_setup = get_topic("talk_weather_setup_part1").shown_count > 0

    if not already_discussed_setup:

        # Introduction
        n "..."
        n "Urgh...{w=0.3} so annoying!"
        n "Why is this so hard to get right...?"
        n "Stupid...{w=0.3} Nnnnnn-!"
        menu:
            "What's the matter, Natsuki?":
                n "Huh?"
                n "Oh!{w=0.2} [player]!"
                n "I'm glad you asked!"

            "What're you complaining about?":
                $ player_was_rude = True
                n "Well,{w=0.1} your attitude,{w=0.1} for one thing!"
                n "Anyway..."

            "...":
                $ player_was_quiet = True
                n "O-{w=0.1}oh!{w=0.2} [player]!"
                n "Sorry,{w=0.1} sorry!{w=0.2} Don't worry{w=0.1} -{w=0.1} it's nothing you did wrong.{w=0.2} I promise!"

        n "So...{w=0.3} I'm not really one to just sit around and admire the view."
        n "But honestly...{w=0.3} it's super boring out there!{w=0.2} Outside the room,{w=0.1} I mean."
        n "Nothing ever changes!"
        n "But...{w=0.3} I've been doing a little tinkering,{w=0.1} and I think I found a way to make things a little more dynamic!"
        n "I just can't quite get it to work..."
        n "It's just...{w=0.3} it's really bugging me.{w=0.2} I hate it when I can't get stuff to go right."

        menu:
            "Perhaps I could help?":
                n "Huh?{w=0.2} Really?!{w=0.2} Thanks, [player]!"
                n "N-{w=0.1}not that I was totally waiting for your help,{w=0.1} obviously!{w=0.2} Ahaha..."

            "What do I have to do?":
                $ player_was_rude = True
                n "Jeez,{w=0.1} [player]...{w=0.3} what's with the attitude today?"
                n "I'm trying to do something nice for us here..."

            "...":
                $ player_was_quiet = True
                n "..."
                n "You know,{w=0.1} [player]..."
                n "If you want to help,{w=0.1} you could just say so."
                n "I'm not scary or anything,{w=0.1} am I?"

        n "Well,{w=0.1} anyway..."
        n "What I'm trying to do is add some atmosphere to this place,{w=0.1} and what better way to do that than..."
        n "Weather!"
        n "I wanna set things up so the weather here matches what it's like where you are,{w=0.1} [player]."
        n "I know{w=0.1} -{w=0.1} awesome,{w=0.1} right?"
        n "But...{w=0.2} I need you to go to this website I found."
        n "Don't worry,{w=0.1} I won't make you go search for it{w=0.1} -{w=0.1} even I'm not that mean!{w=0.2} Ehehe."
        n "It's called OpenWeatherMap,{w=0.1} and it's super cool!{w=0.2} It's just what I need to make this work."
        n "I'll need a little time to get this all set up,{w=0.1} though.{w=0.2} So..."
        n "Are you okay if we get started now,{w=0.1} [player]?"
        menu:
            "Sure.":
                n "Yay!{w=0.2} Thanks a bunch,{w=0.1} [player]!"
                n "This'll all be worth it{w=0.1} -{w=0.1} I promise!"

            "I can't right now.":
                n "Oh...{w=0.3} well, okay..."
                n "Just let me know whenever you have the time,{w=0.1} okay?"
                n "I promise,{w=0.1} it'll be super worth it!"
                return {"lock" : None}

            "I don't want to.":
                n "Huh?{w=0.2} You don't want to?"
                n "..."
                n "Well,{w=0.1} I won't make you do anything you don't want to,{w=0.1} [player]."
                n "I'm a little bummed out,{w=0.1} though..."
                n "..."
                n "Well...{w=0.3} I guess just let me know if you change your mind,{w=0.1} alright?"
                return {"lock" : None}

    else:
        # Natsuki and the player have already discussed this, so we skip the intro

        if not persistent.weather_api_key:
            # We assume the player backed out for whatever reason, as we have no key set
            n "Oh!{w=0.2} Yeah,{w=0.1} I remember!"
            n "Did you want to continue setting everything up for the weather,{w=0.1} [player]?"
            menu:
                "Yes, I want to continue.":
                    n "Awesome!{w=0.2} You won't regret this,{w=0.1} [player]!"
                    n "Now,{w=0.1} where were we..."

                "No, not right now.":
                    n "Huh?{w=0.2} You changed your mind already?"
                    n "Fine,{w=0.1} fine."
                    n "Just let me know when you want to get this set up,{w=0.1} 'kay?"
                    return {"lock" : None}

        else:
            # We assume the player made an oopsie, and wants to give Natsuki another key
            n "Huh?{w=0.2} It looks like you've already got an API key set up,{w=0.1} [player]."
            n "Did you wanna give me a new one?"
            menu:
                "Yes.":
                    n "Alright!{w=0.2} I'll just walk you through it again just in case,{w=0.1} 'kay?"

                "No.":
                    n "Oh...{w=0.3} well,{w=0.1} okay."
                    n "Just let me know if you wanna give me another!"
                    return {"lock" : None}

    # Direct the player to the website

    n "Okaaay!{w=0.2} Let's get started!"
    n "So like I said{w=0.1} -{w=0.1} the website is called OpenWeatherMap.{w=0.2} You can get there from {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_HOME]}here{/a}!"
    n "..."
    n "Did you get there okay, [player]?"

    menu:
        "Yes, I have the website open.":
            n "Awesome!{w=0.2} Step one complete!"

        "No, I couldn't get to the website.":
            n "Huh?{w=0.2} Why not?{w=0.2} Is it down or something?"
            n "Well, anyway...{w=0.3} maybe we can try this again later?"
            n "Just let me know when you're ready,{w=0.1} 'kay?"
            return {"lock" : None}

    # Prompt the player to create an account

    n "'Kay!{w=0.2} Now for step two!"
    n "Basically I need something called an API key,{w=0.1} which will let me use that website to find out what the weather is like over there."
    n "But I can't do that myself...{w=0.3} which is where you come in,{w=0.1} [player]!"
    n "You'll need to make an account before you can get an API key though."
    n "Don't worry{w=0.1} -{w=0.1} it's totally free,{w=0.1} I promise!"
    n "You can create an account {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}here{/a},{w=0.1} or you can sign in using the menu at the top."
    n "Just make sure to go through all the options carefully{w=0.1} -{w=0.1} don't just dash through it!"
    n "Oh{w=0.1} -{w=0.1} and make sure you confirm your email address once you've created it,{w=0.1} 'kay?"
    n "{a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}Here's{/a} that link once more,{w=0.1} just in case!{w=0.2} Just talk to me again when you're done."
    n "..."
    n "Well,{w=0.1} [player]?{w=0.2} All good?"

    menu:
        "Yes, I have an account set up.":
            n "Nice work,{w=0.1} [player]!"
            n "You'll probably want to make sure you save your login details somewhere secure,{w=0.1} just in case."
            n "I hope you didn't forget to confirm your email address too!"

        "I already had an account set up.":
            n "Oh?{w=0.2} I didn't realise you were such a pro at this,{w=0.1} [player]!{w=0.2} Ehehe."

            if already_discussed_setup:
                n "Or maybe we went through this before,{w=0.1} hmm?"

            n "Well, anyway.{w=0.2} The rest of this should be a piece of cake then!"

        "Never mind.":
            n "Huh?{w=0.2} You don't wanna continue?"
            n "That's fine,{w=0.1} I guess."
            n "Just let me know when you're ready,{w=0.1} 'kay?"
            return {"lock" : None}

    # Prompt the player for an API key

    n "Alright!{w=0.2} Now here's the challenging part."
    n "Are you ready,{w=0.1} [player]?"
    n "You need to get your API key and send it to me!"
    n "You can find your keys {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}here{/a},{w=0.1} or you can get there using the menu like before."
    n "You should have one set up already,{w=0.1} but you can create another just for me if you want!{w=0.2} Ehehe."
    n "Oh{w=0.1} -{w=0.1} you'll need to type it all in manually though, so make sure you have it handy!"
    n "{a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}Here's{/a} the link in case you forgot{w=0.1} -{w=0.1} and again,{w=0.1} just talk to me when you have it ready!"
    n "..."
    n "Okaaay!{w=0.2} Take it away,{w=0.1} [player]!"

    $ player_input_valid = False
    $ player_input_count = 0

    # Process the player's input

    while not player_input_valid:

        if player_input_count >= 3:
            # Escape route if we somehow get stuck
            n "I...{w=0.3} don't think we're getting anywhere with this,{w=0.1} [player]."
            n "Maybe we should just try again later?"
            return {"lock" : None}

        else:
            $ player_input = renpy.input("Enter your API key (or type Nevermind to go back):")
            #TODO: This doesn't seem to work; will need to investigate. It's also kind of jarring from a player perspective!
            #$ player_input = txt_input("Enter your API key (or type Nevermind to go back):")

        if not player_input or player_input == "":
            n "Uh...{w=0.3} Did you actually type anything,{w=0.1} [player]?"
            n "I didn't get that...{w=0.3} can you try again for me?"
            $ player_input_count += 1

        elif player_input.replace(" ", "").lower() == "nevermind":
            # Allow the player to back out
            n "Huh?{w=0.2} You don't wanna continue?"
            n "That's fine,{w=0.1} I guess."
            n "Just let me know when you're ready,{w=0.1} 'kay?"
            return {"lock" : None}

        else:
            # Get ready to lead in to the next stage of setup
            $ player_input_valid = True # Kill the loop!
            $ persistent.weather_api_key = player_input
            n "Alright!{w=0.2} I got it!"
            n "Let me just work all of this out...{w=0.3} I might be a few minutes,{w=0.1} just so you know."

            # Final dialogue permutations for that personal touch
            if jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
                $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
                n "But thanks,{w=0.1} [player]!{w=0.2} You're [chosen_descriptor],{w=0.1} you know that?"
            else:
                n "But thanks for all your help, [player]!"

            if player_was_rude:
                n "Even despite your sourness earlier.{w=0.2} Ehehe."

            elif player_was_quiet:
                n "Even if you were a little hesitant at first.{w=0.2} Ehehe."

            if jn_affinity.get_affinity_state() >= store.jn_affinity.LOVE:
                $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                n "Love you,{w=0.1} [chosen_endearment]!"
            # TODO: Perhaps we should decrease this? Seems like a long time to keep the player waiting!
            $ weather.set_next_weather_call_time(7920)
    return {"lock!" : None}

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_weather_setup_part2",
            unlocked=False,
            nat_says=True,
            category=["weather"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_weather_setup_part2:

    # API key isn't valid; we prompt the player for another
    if not weather.is_api_key_valid(persistent.weather_api_key):
        n "Hey...{w=0.3} [player]?"
        n "You know we went through the weather stuff?{w=0.2} With the API key and all that."
        n "Well...{w=0.3} it's been a while,{w=0.1} and it still isn't working!"
        n "Did you wanna try giving me the API key again?"
        menu:
            "Sure.":
                n "Okay!{w=0.2} Let's try and get it working, [player]!"
                n "Do you remember how to find your API keys for that website?"
                n "Fear not!{w=0.2} Natsuki is here to save the day once again!{w=0.2} Ehehe."
                n "You can find yours {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}here{/a}."

            "No, not right now.":
                n "Oh..."
                n "Well...{w=0.3} that's okay, I guess."
                n "Just let me know whenever you're ready,{w=0.1} [player]."
                return {"lock" : None}

        $ player_input_valid = False
        $ player_input_count = 0

        n "..."
        n "All set,{w=0.1} [player]?{w=0.2} Then take it away!"

        while not player_input_valid:

            if player_input_count >= 3:
                # Escape route if we somehow get stuck
                n "This really is going nowhere fast,{w=0.1} huh [player]?"
                n "I think we should just try again later..."
                return {"lock" : None}

            else:
                $ player_input = renpy.input("Enter your API key (or type Nevermind to go back):")

            if not player_input or player_input == "":
                n "Uhmm...{w=0.3} Did you actually type anything,{w=0.1} [player]?"
                n "I didn't get that...{w=0.3} can you try again for me?"
                $ player_input_count += 1

            elif player_input.replace(" ", "").lower() == "nevermind":
                # Allow the player to back out
                n "Huh?{w=0.2} You don't wanna continue?"
                n "That's fine,{w=0.1} I guess."
                n "Just let me know when you're ready,{w=0.1} 'kay?"
                return

            else:
                if weather.is_api_key_valid(player_input):
                    # Save the new API key, since we know it works!
                    n "Ooh!{w=0.2} I can use this one!{w=0.2} Nice work,{w=0.1} [player]!"
                    n "I'll just put this somewhere safe..."
                    $ persistent.weather_api_key = player_input
                    $ player_input_valid = True

                else:
                    n "No dice,{w=0.1} [player]...{w=0.3} that one didn't work either!"

    # API key is valid, now we need the player's location!
    else:
        n "Huh?{w=0.2} For real?"
        n "It looks like we aren't out of the woods yet,{w=0.1} [player]..."
        n "Because I just realized that I have no idea where you actually live!"
        n "Oops!{w=0.2} Ehehe..."
        n "I could {i}probably{/i} find out myself,{w=0.1} but I think that'd be kinda rude."
        n "So...{w=0.3} how about it,{w=0.1} [player]?"
        n "Would you mind if I found out where you are?"
        n "Don't worry! This'll be strictly between you and me. So..."
        menu:
            "How about it?"

            "I don't mind telling you my location.":
                n "Really?{w=0.2} Awesome!{w=0.2}"
                n "Thanks a ton,{w=0.1} [player]!{w=0.2} We're getting so close!"
                n "T-{w=0.1}to this being done,{w=0.1} I mean!"
                n "..."
                n "A-{w=0.1}anyway..."

            "I don't want to tell you my location.":
                n "Aww...{w=0.3} well, okay."
                n "Just let me know if you change your mind,{w=0.1} [player]."
                return

        n "Let's get down to business!"
        n "I'm just gonna look something up real quick..."
        $ ip_latitude_longitude = location.get_coords_by_ip()

        if not ip_latitude_longitude:
            # We couldn't get the coordinates via IP, so we have to prompt them via the player
            n "Huh...{w=0.3} I wasn't actually expecting that."
            n "I was gonna try and find out where you are myself..."
            n "But it looks like we're gonna have to do things the old-fashioned way."
            call weather_setup_manual_coords

        else:
            # Target acquired
            n "Aha!{w=0.2} I think I got it!"
            n "Now...{w=0.3} wanna see something awesome, [player]?{w=0.2} I know you do!"
            n "..."
            $ open_maps(ip_latitude_longitude[0], ip_latitude_longitude[1])
            n "Ta-da!"
            n "Well?{w=0.2} Am I right?{w=0.2} Am I right, [player]?{w=0.2} I bet I am!"
            menu:
                "Yes, you found me.":
                    # Natsuki is clearly a pro at hide and seek
                    n "Yes!{w=0.2} Am I good or what?"
                    n "Ahaha!"
                    n "I'll just note those down real quick..."
                    $ persistent.latitude, persistent.longitude = ip_latitude_longitude

                "No, that's not right.":
                    # We couldn't get the coordinates via IP, so we have to prompt them via the player
                    n "What?{w=0.2} Are you kidding me!?"
                    n "Ugh..."
                    n "And I was so proud of myself for figuring that out,{w=0.1} too..."
                    n "Well,{w=0.1} it looks like we're gonna have to do things the old-fashioned way."
                    call weather_setup_manual_coords

            $ persistent.is_weather_tracking_set_up = True
            n "Okaaay!{w=0.2} It looks like we're finally good to go!"
            n "Thanks again for all your help,{w=0.1} [player]."
            n "I can't wait to see something different out of that window for a change!"
    return

label weather_setup_manual_coords:

    # Determine if the player already went through any part of the setup here

    $ already_discussed_setup = False
    if get_topic("weather_setup_manual_coords"):
        $ already_discussed_setup = get_topic("weather_setup_manual_coords").shown_count > 0

    if not already_discussed_setup:
        n "Well,{w=0.1} fortunately for you,{w=0.1} I happen to have studied Geography so this is right up my alley!"

    # Get the hemispheres

    n "So,{w=0.1} I'm going to need to know a few things to find out where you are."
    n "Let's start off with the basics{w=0.1} -{w=0.1} Hemispheres!"
    n "Do you live in the {b}Northern{/b} or {b}Southern{/b} Hemisphere?"
    n "Just in case you didn't know,{w=0.1} it basically just means if you live {b}North{/b} or {b}South{/b} of the {b}equator{/b}."
    n "So..."
    menu:
        "Which do you live in,{w=0.1} [player]?"

        "The Northern Hemisphere.":
            $ player_in_southern_hemisphere = False
            n "Ooh!{w=0.2} Just like me!"
            n "Looks like we're closer than I thought,{w=0.1} huh?{w=0.2} Ehehe."

        "The Southern Hemisphere.":
            $ player_in_southern_hemisphere = True
            n "Oh?{w=0.2} The Southern Hemisphere?{w=0.2} Neat!"
            n "I bet the weather is a real treat over there,{w=0.1} right?"

    n "Okay,{w=0.1} now time for the other two!"
    n "Do you live in the {b}Eastern{/b} or {b}Western{/b} Hemisphere?"
    n "This one's a little more tricky,{w=0.1} but I find it helps to think of it this way..."
    n "If we took a world map and cut it in half vertically down the middle..."
    menu:
        "Would you live in the Eastern half,{w=0.1} or the Western half?"

        "The Eastern half.":
            $ player_in_western_hemisphere = False
            n "Wow!{w=0.2} Just like me again,{w=0.1} [player]!"
            n "It really is a small world,{w=0.1} huh?{w=0.2} Ehehe."

        "The Western half.":
            $ player_in_western_hemisphere = True
            n "The Western half...{w=0.3} gotcha!"

    # Get the latitude

    n "Now with that out of the way,{w=0.1} I just need your coordinates!"
    n "And by those,{w=0.1} I mean your {b}latitude{/b} and {b}longitude{/b},{w=0.1} of course!"
    n "I always used {a=[store.jn_globals.LINK_LAT_LONG_HOME]}this{/a} website to look mine up for homework,{w=0.1} but you can use your phone or whatever too."
    n "Oh,{w=0.1} and don't worry about making it positive or negative.{w=0.2} I'll take care of that!"
    n "We'll start off with your {b}latitude{/b} first."
    n "So...{w=0.3} hit me,{w=0.1} [player]!"
    $ player_latitude = renpy.input(prompt="Enter your latitude:", allow={"0123456789."})

    # Get the longitude

    n "Thanks,{w=0.1} [player]!{w=0.2} I'll just note that down..."
    n "Alright!{w=0.1} Now finally,{w=0.1} I just need your {b}longitude{/b},{w=0.1} 'kay?"
    n "Just like last time,{w=0.1} I can figure it out without any positive or negative symbols."
    n "Take it away,{w=0.1} [player]!"
    $ player_longitude = renpy.input("Enter your longitude:", allow={"0123456789."})

    # Final checks and prompt

    if player_in_southern_hemisphere:
        $ player_latitude = "-" + player_latitude

    if player_in_western_hemisphere:
        $ player_longitude = "-" + player_longitude

    n "Hey{w=0.1} -{w=0.1} I think we're nearly there now,{w=0.1} [player]!"
    n "Let me just open up a map real quick..."
    n "..."
    $ open_maps(player_latitude, player_longitude)
    n "Ta-da!"
    n "How about it,{w=0.1} [player]?{w=0.2} Close enough,{w=0.1} right?"
    menu:
        "Yes, that's close enough.":
            n "Yay!{w=0.2} Finally!"
            n "I'll just note all that down real quick..."
            $ persistent.latitude = player_latitude
            $ persistent.longitude = player_longitude
            return

        "No, that's not right at all.":
            n "What?{w=0.2} Really?!"
            n "Nnnnnn..."
            n "That's annoying..."
            n "Let's try again,{w=0.1} alright?{w=0.2} I really wanna get this working!"
            jump weather_setup_manual_coords

label menu_nevermind: #TODO: incorporate into _topic_database - not sure how to differentiate it from other talk topics
    n "Okay!"
    jump ch30_loop

#---------------date_menu_topics--------------------

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_beach",
            unlocked=True,
            prompt="Wanna go to the beach?",
            player_says=True,
            category=["date"] #I'm not sure if category is for this..
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_room",
            unlocked=True,
            prompt="Let's return",
            player_says=True,
            category=["date"] #I'm not sure if category is for this..
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_beach:
    n "I love the beach"
    n "Let's go!"
    $ main_background.changeLocation(beach)
    $ main_background.draw(full_redraw=True)
    show Natsuki zorder 3 #replace after sprite rework
    return

label date_go2_room:
    n "Heading back then?"
    n "Alright!"
    $ main_background.changeLocation(classroom)
    $ main_background.draw(dissolve_all=True, full_redraw=True)
    show Natsuki zorder 3 #replace after sprite rework
    return
