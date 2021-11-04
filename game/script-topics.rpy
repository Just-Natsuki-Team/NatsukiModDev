default persistent._topic_database = dict()

# Pet data
default persistent.jn_player_pet = None

# Seasonal data
default persistent.jn_player_favourite_season = None

# Appearance data
default persistent.jn_player_appearance_declined_share = False
default persistent.jn_player_appearance_eye_colour = None
default persistent.jn_player_appearance_hair_length = None
default persistent.jn_player_appearance_hair_colour = None
default persistent.jn_player_appearance_height_cm = None

init python in topics:
    import store
    TOPIC_MAP = dict()

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        persistent._topic_database.clear()

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

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
            $ jn_globals.current_affinity_state = 9
            n "Alright! Your affinity state is now LOVE!" # Yesssssss

        "ENAMORED":
            $ jn_globals.current_affinity_state = 8
            n "Alright! Your affinity state is now ENAMORED!"

        "AFFECTIONATE":
            $ jn_globals.current_affinity_state = 7
            n "Alright! Your affinity state is now AFFECTIONATE!"

        "HAPPY":
            $ jn_globals.current_affinity_state = 6
            n "Alright! Your affinity state is now HAPPY!"

        "NORMAL":
            $ jn_globals.current_affinity_state = 5
            n "Alright! Your affinity state is now NORMAL!"

        "UPSET":
            $ jn_globals.current_affinity_state = 4
            n "Alright! Your affinity state is now UPSET!"

        "DISTRESSED":
            $ jn_globals.current_affinity_state = 3
            n "Alright! Your affinity state is now DISTRESSED!"

        "BROKEN":
            $ jn_globals.current_affinity_state = 2
            n "Alright! Your affinity state is now BROKEN!"

        "RUINED":
            $ jn_globals.current_affinity_state = 1
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
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Hmm?{w=0.2} Pictures of me?"
            n "Honestly,{w=0.1} I don't think I'll ever be completely comfortable with them..."
            n "But I trust you to make a good shot!"
            n "As long as you ask,{w=0.1} I've got no problem with it!"

        elif jn_affinity.is_state_within_range(
            affinity_state=jn_globals.current_affinity_state,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.AFFECTIONATE)
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

        elif jn_affinity.is_state_within_range(
            affinity_state=jn_globals.current_affinity_state,
            affinity_range=(jn_affinity.UPSET, jn_affinity.DISTRESSED)
        ):
            n "Pictures? Really?"
            n "I don't think I want to have you taking my picture,{w=0.1} [player]."
            n "Let's talk about something else."

        else:
            n "Please...{w=0.3} don't try to pretend like you care about how I feel about pictures."
            n "I'm done talking about this,{w=0.1} [player]."
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
            affinity_range=(jn_aff.NORMAL, None),
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

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
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

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "I really,{w=0.1} really care about you,{w=0.1} [player]."
            n "I-{w=0.2}I want you to know that you can depend on me,{w=0.1} 'kay?"

        if jn_affinity.get_affinity_state() == jn_affinity.LOVE:
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

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "But you know I only do these things because I really care about you,{w=0.1} [player]...{w=0.3} right?"
        n "So please...{w=0.3} take care of yourself, okay?{w=0.2} I don't want you hurting because of me."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
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

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
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

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
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

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
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

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "And besides..."
        n "I gotta get you into good habits by yourself before I'm there to make you."
        n "Ahaha!{w=0.2} I'm kidding,{w=0.1} [player]!{w=0.2} I'm kidding!"
        n "...Mostly."

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Love you, [player]~!{w=0.2} Ehehe."

    n "Now...{w=0.3} where were we?"
    return

# Natsuki discusses her favourite season with the player, and asks the player theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_season",
            unlocked=True,
            prompt="What's your favourite season?",
            conditional=None,
            category=["Weather", "Nature"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_season:
    n "Huh?{w=0.2} My favourite season?"
    if not persistent.jn_player_favourite_season:
        n "That's a little random,{w=0.1} isn't it?"
        n "Well...{w=0.3} anyway.{w=0.1} Tough question, [player]!"
        n "I think if I had to pick..."
        n "It'd be summer!{w=0.2} Duh!"
        n "Why?{w=0.2} Just think about it,{w=0.1} [player]!"
        n "Long trips to the beach...{w=0.3} ice cream in the shade...{w=0.3} lazy evening walks to the shops..."
        n "I mean,{w=0.1} what's not to love?"
        n "I can just enjoy life out there without having to worry about the weather!"
        n "I don't think I need to make my case any more clear,{w=0.1} do I?"
        n "Ahaha."
        n "Although...{w=0.3} what about you,{w=0.1} [player]?"
        menu:
            n "What's your favourite season?"

            "Spring":
                n "Oh?{w=0.2} Spring,{w=0.1} huh?"
                n "Hmmm..."
                n "I mean,{w=0.1} I kinda get it.{w=0.2} It's the sign winter finally got lost,{w=0.1} right?"
                n "And I suppose the flowers blooming again is kinda cool to see."
                n "But the rain!{w=0.2} Jeez!"
                n "It just never stops!"
                n "Roll on summer,{w=0.1} I say."
                $ persistent.jn_player_favourite_season = "Spring"

            "Summer":
                n "Aha!{w=0.2} I knew it!"
                n "Nobody can resist some fun in the sun,{w=0.1} am I right?"
                n "I'm glad we both agree,{w=0.1} [player].{w=0.2} Ehehe."
                $ persistent.jn_player_favourite_season = "Summer"

            "Autumn":
                n "Autumn?{w=0.2} Not a bad choice,{w=0.1} actually!"
                n "I like when it's still warm enough in the day to go out and do things..."
                n "But you also get that crisp,{w=0.1} fresh morning air to wake you up."
                n "The falling leaves are super pretty too!"
                n "It's just...{w=0.3} it's all ruined when the rain comes,{w=0.1} you know?"
                n "Trudging through all those sloppy leaves is just gross.{w=0.2} No thanks!"
                $ persistent.jn_player_favourite_season = "Autumn"

            "Winter":
                n "Huh?{w=0.2} Really?"
                n "Winter is the last thing I expected you to say,{w=0.1} [player]!"
                n "Though...{w=0.3} I get it, kinda."
                n "It's the perfect time of year to get super snug and spend some quality reading time!"
                n "Especially since there's not much you can do outside,{w=0.1} anyway."
                $ persistent.jn_player_favourite_season = "Winter"

    else:
        n "Hang on...{w=0.3} didn't we talk about this before,{w=0.1} [player]?"
        n "Well,{w=0.1} anyway..."
        n "I still love summer,{w=0.1} as you know{w=0.1} -{w=0.1} and nothing's gonna change that any time soon!"
        n "What about you,{w=0.1} [player]?{w=0.2} Still rooting for [persistent.jn_player_favourite_season]?"
        menu:
            "Yes.":
                n "Ehehe.{w=0.2} I thought as much,{w=0.1} [player]."
                if persistent.jn_player_favourite_season == "Summer":
                    n "You already picked the best season,{w=0.1} after all!"
                    return

                n "Well...{w=0.3} I'm afraid you're not gonna sway me!"
                n "Ahaha!"

            "No.":
                n "Oh?{w=0.2} Changed our mind,{w=0.1} have we?"
                n "Well?{w=0.2} Tell me then,{w=0.1} [player]!"
                menu:
                    n "What's your favourite season?"

                    "Spring":
                        $ new_favourite_season = "Spring"

                    "Summer":
                        $ new_favourite_season = "Summer"

                    "Autumn":
                        $ new_favourite_season = "Autumn"

                    "Winter":
                        $ new_favourite_season = "Winter"

                if persistent.jn_player_favourite_season == new_favourite_season:
                    n "Hey!{w=0.2} [player]!"
                    n "I thought you said you'd changed your mind?"
                    n "You haven't changed your mind at all!{w=0.2} You said [persistent.jn_player_favourite_season] last time,{w=0.1} too!"
                    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                    n "Jeez...{w=0.3} you're such a wind-up sometimes,{w=0.1} [chosen_tease]!"
                    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                        n "But...{w=0.3} you know,{w=0.1} [player]."
                        n "It isn't like I {i}dislike{/i} that side of you,{w=0.1} or anything..."
                        n "Ehehe."

                    else:
                        n "But...{w=0.3} I think I can {i}weather{/i} it."
                        n "For now."

                    return

                else:
                    $ persistent.jn_player_favourite_season = new_favourite_season

                if persistent.jn_player_favourite_season == "Spring":
                    n "Ooh?{w=0.2} Favouring Spring now,{w=0.1} [player]?"
                    n "I could do without all the rain,{w=0.1} but I get it."
                    n "Hmm...{w=0.3} Spring..."
                    n "I wonder...{w=0.3} do you grow anything,{w=0.1} [player]?"
                    n "Ahaha."

                elif persistent.jn_player_favourite_season == "Summer":
                    n "Aha!{w=0.2} See?"
                    n "You knew I was right all along,{w=0.1} didn't you?"
                    n "Don't even try to deny it,{w=0.1} [player]."
                    n "Summer is the best!"
                    n "I'm just glad you came around.{w=0.2} That's the important thing!"

                elif persistent.jn_player_favourite_season == "Autumn":
                    n "Oh?{w=0.2} You've taken the {i}fall{/i} for Autumn,{w=0.1} have you?"
                    n "Ehehe."
                    n "I'll admit,{w=0.1} it's a pretty season,{w=0.1} with all the golden leaves and stuff..."
                    n "So long as the weather stays warm,{w=0.1} anyway."

                elif persistent.jn_player_favourite_season == "Winter":
                    n "Winter,{w=0.1} huh?{w=0.2} I wasn't expecting that."
                    n "Do you prefer being indoors now or something,{w=0.1} [player]?"
                    n "Well,{w=0.1} if you prefer being all cosy inside..."
                    n "Then you better not be slacking on your reading,{w=0.1} [player]!"
                    n "Ehehe."

    return

# Natsuki discusses the concept of timeboxing
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_time_management",
            unlocked=True,
            prompt="Time management",
            conditional=None,
            category=["Life"],
            nat_says=True,
            affinity_range=(jn_affinity.UPSET, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n "Hey,{w=0.1} [player]..."
    n "Do you have off days sometimes?{w=0.2} Where you struggle to get anything done?"
    n "Or you just get distracted super easily?"
    n "To be honest,{w=0.1} I struggled with that for a while.{w=0.2} Especially when things like assignments are so boring!"
    n "But...{w=0.3} I figured out a way of managing that{w=0.1} -{w=0.1} and you should know it too,{w=0.1} [player]!"
    n "Time boxing!"
    n "And no,{w=0.1} it's not as literal as it sounds.{w=0.2} Ehehe."
    n "The idea is that you set aside a period during the day you want to work{w=0.1} -{w=0.1} like the school day,{w=0.1} or a few hours in the evening."
    n "Then for each hour in that period,{w=0.1} you split it!"
    n "So for any given hour,{w=0.1} you spend most of that working,{w=0.1} and the remainder on some kind of break."
    n "The idea is that it becomes way easier to stay focused and motivated since you always have a breather coming up."
    n "Personally,{w=0.1} I find a 50/10 split works best for me."
    n "So I spend 50 minutes of each hour studying,{w=0.1} and 10 minutes doing whatever I want."
    n "You'd be surprised how much manga time I can sneak in!"
    n "Don't just take my schedule as a rule though.{w=0.2} Find a balance that works for you, [player]!"
    n "Though I should remind you...{w=0.3} the key word here is {i}balance{/i}."
    n "I'm not gonna be impressed if you work too much..."
    n "Or just slack off!"
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Although...{w=0.3} now that I think about it..."
        n "Perhaps I should timebox our time together, [player]."
        n "Ahaha!"

    return

# Natsuki discusses her sweet tooth with the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sweet_tooth",
            unlocked=True,
            prompt="Do you have a sweet tooth?",
            conditional=None,
            category=["Natsuki", "Health", "Food"],
            player_says=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sweet_tooth:
    n "Huh?{w=0.2} Do I have a sweet tooth?"

    # Opening response
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "You bet I do!"
        n "What were you expecting,{w=0.1} [player]?{w=0.2} Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Well,{w=0.1} yeah.{w=0.2} Of course I do!"

    else:
        n "Well...{w=0.3} yeah.{w=0.2} Why wouldn't I?"

    n "Baked stuff is okay,{w=0.1} but I find it gets kinda sickly before long."
    n "But to be completely honest,{w=0.1} if I had a choice?"
    n "Just give me a bunch of candy every time."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "There's so much more variety!{w=0.2} Like...{w=0.3} there's always something for whatever I feel like!"
        n "I think if I had to pick a favourite though,{w=0.1} it'd be those fizzy ones."
        n "Just that perfect mix of sweet and sour,{w=0.1} you know?"
        n "Jeez...{w=0.3} I can feel my tongue tingling already just thinking about them!"
        n "..."
        n "A-{w=0.1}anyway!"
        n "It isn't like I'm snacking on treats all the time though."
        n "I've got way better things to spend my money on."
        n "And...{w=0.3} it's not exactly healthy either.{w=0.2} Ahaha."

    # Closing thoughts
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Though I have to say,{w=0.1} [player]."
        n "I'm pretty sure you have a sweet tooth too."
        n "It'd explain why you're spending so much time with me,{w=0.1} after all."
        n "Ahaha!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "I could go for some candy right now,{w=0.1} actually."
        n "But...{w=0.3} I think I'll hold back."
        n "Someone's gotta be a role model to you,{w=0.1} [player].{w=0.2} Am I right?"
        n "Ehehe."

    else:
        n "..."
        n "That being said..."
        n "I...{w=0.3} could really use some chocolate right now."
        n "I'll let you figure out why,{w=0.1} [player]."

    return

# Natsuki asks about and potentially discovers more about the player's physical appearance
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_appearance",
            unlocked=True,
            prompt="Your appearance",
            conditional=None,
            category=["Life", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:
    # Player was asked before, and declined to share their appearance
    if persistent.jn_player_appearance_declined_share:
        n "Huh?{w=0.2} Your appearance?"
        n "If I remember,{w=0.1} [player]{w=0.1} -{w=0.1} you said didn't want to share it with me before."
        n "Hmm...{w=0.3} Well..."
        menu:
            n "Did you change your mind,{w=0.1} [player]?"

            "Yes, I want to share my appearance.":
                n "Yay!{w=0.2} I was hoping you'd come around eventually,{w=0.1} [player]."
                n "Let's not waste any time!"

            "No, I still don't want to share my appearance.":
                n "Oh..."
                n "Well,{w=0.1} it's your call,{w=0.1} [player]."
                n "Just let me know if you change your mind again,{w=0.1} alright?"
                return

    # Player has already described themselves to Natsuki
    elif persistent.jn_player_appearance_eye_colour is not None:
        n "Huh?{w=0.2} Your appearance?"
        n "But...{w=0.3} I was sure you already shared that with me,{w=0.1} [player]."
        n "Ooh!{w=0.2} Did you dye your hair or something?"
        n "Or...{w=0.3} maybe you just made a mistake last time?"
        n "Well,{w=0.1} either way..."
        menu:
            n "Did you want to share your appearance again,{w=0.1} [player]?"

            "Yes, my appearance has changed.":
                n "Aha!{w=0.2} I thought so!"
                n "I can't wait to find out how!"

            "No, my appearance hasn't changed.":
                n "Eh?{w=0.2} Just pulling my leg,{w=0.1} are you?"
                n "Okaaay..."
                n "Just let me know if you actually {i}do{/i} change something then,{w=0.2} 'kay?"
                n "Ehehe."

    # Player has never described themselves to Natsuki, and this is their first time discussing it
    else:
        n "Huh..."
        n "You know,{w=0.1} [player].{w=0.2} I just realized something."
        n "You've seen a lot of me,{w=0.1} right?{w=0.2} By spending time with me here,{w=0.1} I mean."
        n "So...{w=0.3} you kinda know exactly who you're dealing with."
        n "But I don't have a clue about how you actually look!"
        n "And honestly?{w=0.2} I'm actually pretty curious!"
        n "Don't worry though{w=0.1} -{w=0.1} anything you tell me is staying strictly between us,{w=0.1} obviously!"
        n "So...{w=0.3} how about it, [player]?"
        menu:
            n "Do you wanna share your appearance with me, [player]?"

            "Sure!":
                n "Yay!{nw}"
                n "I-{w=0.1}I mean good!{w=0.2} Thanks a bunch,{w=0.1} [player]!"
                n "Let's get started then,{w=0.1} shall we?"

            "I'm not comfortable sharing that.":
                n "Oh..."
                n "That's kind of disappointing to hear,{w=0.1} if I'm being honest."
                n "But I totally get it,{w=0.1} [player].{w=0.2} So don't worry,{w=0.1} 'kay?"
                n "Just let me know if you feel like telling me later!"
                $ persistent.jn_player_appearance_declined_share = True

    n "Okaaay!{w=0.2} Let's start with...{w=0.3} your eyes!"
    n "They say the eyes are the window to the soul,{w=0.1} so it only makes sense to begin there,{w=0.1} right?"
    n "Ahaha.{w=0.2} Anyway..."

    # Eye colour
    menu:
        n "How would you describe your eye colour,{w=0.1} [player]?"

        "Amber":
            n "Ooh!{w=0.2} I don't think I've seen someone with amber eyes before."
            n "That's awesome,{w=0.1} [player]!{w=0.2} I bet those help you stand out,{w=0.1} right?"
            $ persistent.jn_player_appearance_eye_colour = "Amber"

        "Blue":
            n "Blue eyes,{w=0.1} huh?{w=0.2} Cool!"
            n "I really like how striking they are!"
            $ persistent.jn_player_appearance_eye_colour = "Blue"

        "Brown":
            n "Brown eyes,{w=0.1} huh?{w=0.2} I'm not complaining!"
            n "Nice and natural,{w=0.1} am I right?{w=0.2} Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Brown"

        "Grey":
            n "Oh?{w=0.2} Grey eyes?{w=0.2} That's super neat, [player]!"
            n "I don't think I've seen anyone with grey eyes before!"
            $ persistent.jn_player_appearance_eye_colour = "Grey"

        "Green":
            n "Aha!{w=0.2} I had you figured for green eyes,{w=0.1} [player]."
            n "I bet you're proud of them,{w=0.1} no?{w=0.2} Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Green"

        "Hazel":
            n "Ooh!{w=0.2} Hazel,{w=0.1} huh?{w=0.2} Classy!"
            n "Hmm...{w=0.3} I wonder if yours are closer to green or brown, [player]?"
            $ persistent.jn_player_appearance_eye_colour = "Hazel"

        "Mixed":
            n "Wow!{w=0.2} Do you have two different colours or something,{w=0.1} [player]?"
            n "Now if that isn't unique,{w=0.1} I don't know what is!"
            $ persistent.jn_player_appearance_eye_colour = "Mixed"

        "Other":
            n "Oh?{w=0.2} Something a bit off the beaten trail,{w=0.1} huh?"
            n "...Or maybe you just wear contacts a lot?{w=0.2} Ahaha."
            n "I'm sure they look great,{w=0.1} either way!"
            $ persistent.jn_player_appearance_eye_colour = "Other"

    n "Alright!{w=0.2} That's one down!{w=0.2} Thanks for sharing that with me,{w=0.1} [player]!"
    n "So next,{w=0.1} we have..."
    n "Your hair,{w=0.1} of course!"
    n "Let's just start off with the length for now,{w=0.1} 'kay?"
    n "Now..."

    # Hair length
    menu:
        n "How would you describe your hair length,{w=0.1} [player]?"

        "Short.":
            n "Ah,{w=0.1} the low maintenance approach{w=0.1} -{w=0.1} I see,{w=0.1} I see.{w=0.2} Trendy!"
            n "To be honest though,{w=0.1} I totally get it."
            n "I have no idea how you even keep long hair looking good..."
            n "It just seems like way too much effort to me."
            $ persistent.jn_player_appearance_hair_length = "Short"

        "Mid-length.":
            n "Aha!{w=0.2} The perfect balance,{w=0.1} am I right?"
            n "Just long enough for pretty much any style..."
            n "And yet still short enough to suit a lazy day!{w=0.2} Ehehe."
            n "I'm glad we think the same way,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "Mid-length"

        "Long.":
            n "Ooh!{w=0.2} Letting it run free,{w=0.1} are we?"
            n "I bet you take super good care of yours!"
            n "I might even have to borrow your products,{w=0.1} [player].{w=0.2} Ehehe!"
            $ persistent.jn_player_appearance_hair_length = "Long"

        "I don't have any hair.":
            n "Hey{w=0.1} -{w=0.1} nothing wrong with that!{w=0.2} You wanna know why?"
            n "Because it just means you're aerodynamic,{w=0.1} [player]."
            n "Ahaha!"
            $ persistent.jn_player_appearance_hair_length = "None"

    n "Okay!{w=0.1} I'm really starting to get a picture now."
    n "Let's keep the ball rolling,{w=0.1} [player]!"

    # Hair colour
    if persistent.jn_player_appearance_hair_length == "None":
        n "You said you didn't have any hair,{w=0.1} so I think it's kinda pointless talking about hair colour."
        n "Now,{w=0.1} let's see... what else..."
        n "Hmm..."

    else:
        n "Now for your hair colour!"
        n "So,{w=0.1} [player]..."
        menu:
            n "How would you describe your hair colour?"

            "Auburn":
                n "Ooh!{w=0.2} Auburn,{w=0.1} huh?{w=0.2} That's awesome,{w=0.1} [player]!"
                n "It's such a warm colour!"
                $ persistent.jn_player_appearance_hair_colour = "Auburn"

            "Black":
                n "Black,{w=0.1} huh?{w=0.2} Nice!"
                n "I bet you look super slick,{w=0.1} [player]!"
                $ persistent.jn_player_appearance_hair_colour = "Black"

            "Blond":
                n "Aha!{w=0.2} A blond,{w=0.1} are we?{w=0.2} That explains a lot."
                n "Ahaha!"
                n "I'm kidding,{w=0.1} [player]!{w=0.2} I'm just kidding!"
                n "I'm actually a little jealous.{w=0.2} Just a little."
                $ persistent.jn_player_appearance_hair_colour = "Blond"

            "Brown":
                n "Brown hair,{w=0.1} [player]?{w=0.2} I'm for it!"
                n "Not too subtle and not too striking,{w=0.1} you know?{w=0.2} It's just right!"
                $ persistent.jn_player_appearance_hair_colour = "Brown"

            "Grey":
                n "Ooh...{w=0.3} I wasn't expecting that!"
                n "I just hope that isn't from stress,{w=0.1} [player]..."
                n "...Or at least stress from me,{w=0.1} anyway.{w=0.2} Ehehe."
                $ persistent.jn_player_appearance_hair_colour = "Grey"

            "Red":
                n "Ehehe.{w=0.2} So you're a red head,{w=0.1} [player]?"
                n "Not that there's anything wrong with that,{w=0.1} o-{w=0.1}obviously!"
                n "I bet you get quite the attention,{w=0.1} huh?"
                $ persistent.jn_player_appearance_hair_colour = "Red"

            "White":
                n "White hair?{w=0.2} Neat!"
                n "I bet it suits you,{w=0.1} [player]!"
                $ persistent.jn_player_appearance_hair_colour = "White"

            "Other":
                n "Oh?{w=0.2} It looks like we're more similar in taste than I thought!"
                n "Though I should probably clarify...{w=0.3} mine is all natural,{w=0.1} [player]!{w=0.2} Ahaha."
                $ persistent.jn_player_appearance_hair_colour = "Other"

    # Height
    n "Alright!{w=0.2} I think I'm almost done interrogating you now,{w=0.1} [player]."
    n "Ehehe."
    n "So...{w=0.3} don't judge me when I ask this,{w=0.1} but I gotta know."
    n "Exactly..."

    $ player_input_valid = False
    while not player_input_valid:
        $ player_input = int(renpy.input(prompt="How tall are you in {i}centimeters{/i},{w=0.2} [player]?", allow="0123456789"))

        # Valid height
        if player_input > 75 and player_input <= 300:
            $ player_input_valid = True
            $ persistent.jn_player_appearance_height_cm = player_input

            if player_input < 149:
                n "H-{w=0.1}huh?{w=0.2} Really?"
                n "You're even shorter than me?"
                n "Well,{w=0.1} I wasn't expecting that!"
                n "Don't worry,{w=0.1} [player].{w=0.2} We're both on the same side,{w=0.1} right?{w=0.2} Ehehe."

            elif player_input == 149:
                n "Seriously?{w=0.2} We're the same height?"
                n "That's amazing,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length = "Medium" and persistent.jn_player_appearance_hair_colour = "Other":
                    n "Well,{w=0.1} no wonder we get along so well..."
                    n "It's like we're practically twins!"

            elif player_input > 149 and player_input < 166:
                n "Oh?{w=0.2} A little on the shorter side,{w=0.1} [player]?"
                n "Don't worry, don't worry!{w=0.2} I'm not one to judge,{w=0.1} after all."

            elif player_input >= 166 and player_input < 200:
                n "About average height,{w=0.1} [player]?"
                n "No complaints from me!{w=0.2} I feel like that's just the way to be,{w=0.1} personally."

            elif player_input >= 200 and player_input < 250:
                n "Oh?{w=0.2} On the taller side [player],{w=0.1} are we?"
                n "I guess I know who to take shopping,{w=0.1} right?{w=0.2} Ehehe."

            else:
                n "W-{w=0.1}woah!{w=0.2} What the heck,{w=0.1} [player]?{w=0.2} Really?"
                n "That's crazy tall!"
                n "Actually...{w=0.3} I hope that isn't actually just inconvenient for you,{w=0.1} though."

        else:
            n "[player]...{w=0.3} please.{w=0.2} Take this seriously,{w=0.1} alright?"

    n "Okaaay!{w=0.2} I think that's everything."
    n "Thanks a bunch,{w=0.1} [player]!"
    n "I know it wasn't a lot,{w=0.1} but I feel like I know you so much better now!"

    if jn_affinity.get_affinity_state() == jn_affinity.ENAMORED:
        n "...And now I know exactly who I should be watching out for."
        n "So you better watch out,{w=0.1} [player]."
        n "Ehehe."

    elif jn_affinity.get_affinity_state() == jn_affinity.LOVE:
        n "You know,{w=0.1} [player]?{w=0.2} I can just picture it now."
        n "Meeting you in person somewhere out there,{w=0.1} for the first time..."
        python:
            # Get the descriptor for the eye colour
            if persistent.jn_player_appearance_eye_colour == "Other":
                eye_colour_descriptor = "sparkling"

            else:
                eye_colour_descriptor = persistent.jn_player_appearance_eye_colour.lower()

            # Get the descriptor for the hair colour
            if persistent.jn_player_appearance_hair_colour == "Other":
                hair_colour_descriptor = "amazing"

            else:
                hair_colour_descriptor = persistent.jn_player_appearance_hair_colour.lower()

        # Comment on hair length and colour, if the player has hair
        if not persistent.jn_player_appearance_hair_length == "None":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n "Spotting your [hair_length_descriptor] [hair_colour_descriptor] hair in the distance and chasing you down..."

        else:
            n "Spotting you in the distance and chasing you down..."

        # Comment on height and eye colour
        if persistent.jn_player_appearance_height_cm < 149:
            n "Gazing down into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n "Gazing directly into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n "Gazing upwards into your [eye_colour_descriptor] eyes..."

        n "Uuuuuu..."
        n "I'm getting a rush just thinking about it!"
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n "But seriously.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
        n "This seriously meant a lot to me."

    return

# Natsuki discusses drinking alcohol
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_drinking_alcohol",
            unlocked=True,
            prompt="Do you drink alcohol?",
            conditional=None,
            category=["Health", "Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_drinking_alcohol:
    n "Do I drink alcohol?"
    n "I can't say I've ever tried it,{w=0.1} [player]."
    n "I just don't really think it's something for me."
    n "That being said,{w=0.1} I knew people who {i}did{/i} drink it..."
    n "But...{w=0.3} I'd...{w=0.3} really rather not get into that,{w=0.1} [player]."
    n "Sorry."
    n "..."
    n "Oh!{w=0.2} That reminds me,{w=0.1} actually!"
    n "I bet you didn't know,{w=0.1} but guess who just randomly brought some into the club one day?"
    n "Yuri!"
    n "Surprised?{w=0.2} I know,{w=0.1} right?"
    n "I mean...{w=0.3} it was just completely out of the blue!"
    n "She just produced it from her bag like it was a book or something."
    n "It wasn't even just some random supermarket stuff either...{w=0.3} it looked super expensive too!"
    n "Honestly,{w=0.1} I couldn't help myself.{w=0.2} I just burst into laughter."
    n "I think it was just how non-chalant it all was,{w=0.1} really."
    n "Monika didn't look impressed,{w=0.1} though..."
    n "And Sayori...{w=0.3} she just got really upset.{w=0.2} She was shouting and everything!"
    n "It looked like she put a lot of thought into picking something out,{w=0.1} but she just got yelled at for it..."
    n "I mean...{w=0.3} I know we shouldn't have had it in there at all,{w=0.1} and Yuri should have known better."
    n "But she didn't deserve all of...{w=0.3} that."
    n "I think she was just trying to build bonds,{w=0.1} you know?"
    n "It's all in the past now,{w=0.1} obviously.{w=0.2} But that doesn't mean I don't still feel bad about it sometimes."
    n "..."
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Hey...{w=0.3} [player]?"
        n "Can you promise me something?"
        n "It's dumb,{w=0.1} but it's personal to me."
        n "I don't care if you drink or not."
        n "But if you do..."
        n "Please...{w=0.3} take it all in moderation,{w=0.1} okay?"
        n "I've...{w=0.3} seen...{w=0.3} what it can do to people."
        n "Firsthand."
        n "You deserve better than that,{w=0.1} [player].{w=0.2} You {i}are{/i} better than that."
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "..."
            n "I love you,{w=0.1} [player]."
            n "I'm never going to let a bottle get between us."

    else:
        n "Hey,{w=0.1} [player]?"
        n "I don't really care if you drink or not."
        n "Just promise you'll go easy on it,{w=0.1} okay?"
        n "I'm not gonna clean up after you!"
        n "Ahaha..."

    return

# Natsuki laments her inability to drive and questions the player on if they can
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_driving",
            unlocked=True,
            prompt="Can you drive?",
            conditional=None,
            category=["Natsuki", "Transport"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:
    n "Pffft!"
    n "Ahaha!{w=0.2} What kind of a question is that,{w=0.1} [player]?"
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    n "Of course I can't drive,{w=0.1} [chosen_tease]!{w=0.2} Why do you think I walk everywhere?"
    n "I mean...{w=0.3} even if I wanted to learn,{w=0.1} I don't think I could afford it."
    n "Lessons are super expensive nowadays!"
    n "And then there's tests,{w=0.1} insurance...{w=0.3} it's actually pretty gross how fast it all adds up."
    n "I think I'd rather stick to public transport and my own two feet."
    n "But what about you,{w=0.1} [player]?"
    menu:
        n "Can you drive?"

        "Yes, and I do currently.":
            n "Wow."
            n "...{w=0.3}Show-off."
            n "..."
            n "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.2} I'm just messing with you."
            n "That's awesome though{w=0.1} -{w=0.1} you just can't beat the convenience of a car,{w=0.1} right?"
            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "But I should probably warn you..."
                n "I'm picking the songs for our driving playlist."
                n "Ahaha!"

            else:
                n "Just remember,{w=0.1} [player]..."
                n "I call shotgun.{w=0.2} Ehehe."

        "Yes, but I don't right now.":
            n "Oh?{w=0.2} Is something wrong with your car,{w=0.1} [player]?"
            n "Or perhaps...{w=0.3} you just don't own one at the moment?"
            n "Well,{w=0.1} I'm not one to judge.{w=0.2} I'm sure you manage just fine."
            n "Besides,{w=0.1} you're helping the environment too,{w=0.1} right?"
            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "Thoughtful as always,{w=0.1} [player]."
                n "I like that about you."
                n "Ehehe."

        "No, I can't.":
            n "Oh..."
            n "Well,{w=0.1} chin up,{w=0.1} [player]!{w=0.2} It isn't the end of the world."
            n "Don't worry {w=0.1}-{w=0.1} I'll teach you how to use the bus!"
            n "Ehehe."
            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "And besides..."
                n "That just means we can snuggle up on the seat together,{w=0.1} [player]."
                n "A dream come true for you,{w=0.1} right?"
                n "Ehehe."

            else:
                n "That's what friends are for, [player]!"

    return

# Natsuki laments her inability to drive and questions the player on if they can
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sustainable_fashion",
            unlocked=True,
            prompt="Sustainable fashion",
            conditional=None,
            category=["Environment", "Fashion"],
            nat_says=True,
            affinity_range=(jn_affinity.UPSET, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sustainable_fashion:
    n "Hey,{w=0.1} [player]..."
    n "This is kinda random,{w=0.1} but are you into fashion?"
    if jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "I know I am!{w=0.2} Can you tell?"
        n "Ehehe."

    else:
        n "I know I am."

    n "But what caught me by surprise is just how much waste there is."
    n "Seriously,{w=0.1} [player] {w=0.1}-{w=0.1} it's insane!"
    n "People throw away a {i}lot{/i} of clothing...{w=0.3} it's estimated that we toss out around 90{w=0.3} {i}million{/i}{w=0.3} tonnes every year."
    n "That's a truck-full every second!{w=0.2} What a waste!"
    n "And we haven't even began to talk about the amount of water used for washing and plastic used for packaging too."
    n "...Or the conditions some of the workers making our clothes have to put up with."
    n "It's actually one of the reasons I began learning how to sew!"
    n "I've never had tons of money to buy more clothes anyway,{w=0.1} so I try to reuse and fix up what I can."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "You'd be surprised at what you can pull off with a little creativity!"
        n "And just a pinch of know-how too,{w=0.1} obviously."
        n "Betcha didn't know my favourite pink skirt was hand-made,{w=0.1} did you?"

    else:
        n "It's neat what you can make with some creativity."

    n "I think I've lectured you enough now,{w=0.1} [player],{w=0.1} so I won't keep harping on about it."
    n "But...{w=0.3} the next time you're out shopping for clothes,{w=0.1} or looking through some catalogues online?"
    n "Just spare a thought for the environment,{w=0.1} would you?"
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "For me?"
        n "I know I can count on you!"

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Ehehe.{w=0.2} Thanks,{w=0.1} [player]!"
        n "I'm counting on you!"

    else:
        n "Thanks, [player]."

    return

# Natsuki gets a nickname from the player, assuming they aren't blocked from doing so
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_give_nickname",
            unlocked=True,
            prompt="Can I give you a nickname?",
            conditional="persistent.jn_player_nicknames_allowed",
            category=["Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_give_nickname:
    # Natsuki hasn't been nicknamed before, or is rocking her normal name
    if persistent.jn_player_nicknames_allowed and persistent.jn_player_nicknames_current_nickname == "Natsuki":
        n "Eh?{w=0.2} You want to give me a nickname?"
        n "Why?{w=0.2} Natsuki not good enough for you?{w=0.2} Is that it?"
        n "Huh?{w=0.2} Come on, [player]!{w=0.2} Spit it out!"
        n "..."
        n "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.2} I'm just kidding!"
        n "Ehehe."
        n "Well...{w=0.3} I don't see why not!"

    # Another nickname is being assigned
    else:

        # Account for strikes
        if persistent.jn_player_nicknames_bad_given_total == 0:
            n "Oh?{w=0.2} You wanna give me another nickname?"
            n "Sure,{w=0.1} why not!"

        elif persistent.jn_player_nicknames_bad_given_total == 1:
            n "You want to give me a new nickname?"
            n "Alright,{w=0.1} [player]."

        elif persistent.jn_player_nicknames_bad_given_total == 2:
            n "Another nickname,{w=0.1} [player]?{w=0.2} Fine."
            n "Just...{w=0.3} think a little about what you choose,{w=0.1} 'kay?"

        elif persistent.jn_player_nicknames_bad_given_total == 3:
            n "Alright,{w=0.1} [player]."
            n "Just remember.{w=0.3} You've had your final warning about this."
            n "Don't let me down again."

    # Validate the nickname, respond appropriately
    $ nickname = renpy.input(prompt="What did you have in mind,{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n "Huh?{w=0.2} You changed your mind?"
        n "Well...{w=0.3} alright then."
        n "Just let me know if you actually want to call me something else then,{w=0.1} 'kay?"
        return

    else:
        $ nickname_type = nicknames.get_nickname_type(nickname)

    if nickname_type == nicknames.NICKNAME_TYPE_INVALID:
        n "Uhmm...{w=0.3} [player]?"
        n "I don't think that's a nickname at all."
        n "I'll...{w=0.3} just stick with what I have now,{w=0.1} thanks."
        return

    elif nickname_type == nicknames.NICKNAME_TYPE_LOVED:
        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        n "O-{w=0.1}oh!{w=0.2} [player]!"
        n "..."
        n "W-{w=0.1}well,{w=0.1} you have good taste,{w=0.1} at least."
        n "..."
        n "Nnnnn...{w=0.3} you made it all awkward,{w=0.1} [player].{w=0.2} I hope you're happy."
        n "But...{w=0.3} I really like this one."
        n "[nickname] it is!{w=0.2} Ehehe."
        return

    elif nickname_type == nicknames.NICKNAME_TYPE_DISLIKED:
        n "Come on,{w=0.1} [player]...{w=0.3} really?"
        n "You know I'm really not comfortable being called that."
        n "..."
        n "I'm...{w=0.3} just going to pretend you didn't say that,{w=0.1} alright?"
        return

    elif nickname_type == nicknames.NICKNAME_TYPE_HATED:
        n "W-{w=0.1}what?{w=0.2} What did you just call me?!"
        n "[player]!{w=0.2} I can't believe you!"
        n "Why would you call me that?{w=0.2} That's awful!"
        n "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == nicknames.NICKNAME_TYPE_PROFANITY:
        n "E-{w=0.1}excuse me?!"
        n "What the hell did you just call me,{w=0.1} [player]?!"
        n "..."
        n "I seriously can't believe you,{w=0.1} [player]."
        n "Why would you do that?{w=0.1} Are you trying to upset me?"
        n "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == nicknames.NICKNAME_TYPE_FUNNY:
        n "Pffft!"
        n "Ahaha!"
        n "[nickname]?{w=0.2} What kind of nickname is that meant to be,{w=0.1} [player]?"
        n "Well...{w=0.3} you're just lucky I have a healthy sense of humour."
        n "[nickname] it is,{w=0.1} I guess!{w=0.2} Ehehe."

        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        return

    else:
        $ neutral_nickname_permitted = False

        # Check and respond to easter egg nicknames
        if nickname.lower() == "natsuki":
            n "Uhmm...{w=0.3} [player]?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "That's just my normal name,{w=0.1} [chosen_tease]!"
            n "Honestly...{w=0.3} sometimes I wonder why I bother."
            n "Well,{w=0.1} I'm not complaining!{w=0.2} If it isn't broke,{w=0.1} don't fix it -{w=0.1} right?"
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n "..."
            n "D-{w=0.1}dreaming big,{w=0.1} are we,{w=0.1} [player]?{w=0.2} Ahaha..."
            n "Uhmm..."
            n "I'm...{w=0.3} really...{w=0.3} not a fan,{w=0.1} but if it's what you prefer..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "qeb" or nickname.lower() == "qeeb":
            n "No you."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n "I...{w=0.3} don't think you thought this through,{w=0.1} [player]."
            n "Do you even know how confusing that'd be?"
            n "I think I'll just stick to what works,{w=0.1} 'kay?"
            n "Ehehe."
            n "Nice try,{w=0.1} though!"

        # Fallback for anything not categorised
        else:
            n "Hmm...{w=0.3} [nickname], huh?"
            n "[nickname]..."
            n "You know what?{w=0.2} Yeah!{w=0.2} I like it!"
            n "Consider it done,{w=0.1} [player]!{w=0.2} Ehehe."
            $ neutral_nickname_permitted = True

        # Finally, assign the neutral/easter egg nickname if it was permitted by Natsuki
        if (neutral_nickname_permitted):
            $ persistent.jn_player_nicknames_current_nickname = nickname
            $ n_name = persistent.jn_player_nicknames_current_nickname

        return

    # Handle strikes
    if persistent.jn_player_nicknames_bad_given_total == 1:
        n "Jeez,{w=0.1} [player]...{w=0.3} that isn't like you at all!"
        n "What's up with you today?"
        n "..."
        n "Just...{w=0.3} don't do that again,{w=0.1} okay?"
        n "That really hurt,{w=0.1} [player].{w=0.2} Don't abuse my trust."

        $ relationship(change="affinity-", multiplier=2)
        $ relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 2:
        n "I can't believe you did that again to me,{w=0.1} [player]."
        n "I told you it hurts,{w=0.1} and you went ahead anyway!"
        n "..."
        n "I...{w=0.3} really...{w=0.3} like you, [player].{w=0.2} It hurts extra bad when it's you."
        n "Don't test my patience like this.{w=0.2} You're better than that."

        $ relationship(change="affinity-", multiplier=2)
        $ relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 3:
        n "You are honestly unbelievable,{w=0.1} [player]."
        n "I've told you so many times now,{w=0.1} and you still won't knock it off!"
        n "..."
        n "No more warnings,{w=0.1} [player]."
        menu:
            n "Understand?"

            "I understand. Sorry, Natsuki.":
                n "You understand,{w=0.1} do you?"
                n "...Then start acting like it,{w=0.1} [player]."
                n "Thanks."

                $ relationship(change="affinity-", multiplier=2)
                $ relationship(change="trust-", multiplier=2)

            "...":
                n "Look.{w=0.2} I'm not kidding around,{w=0.1} [player]."
                n "Acting like this isn't funny,{w=0.1} or cute."
                n "It's toxic."
                n "I don't care if you're trying to pull my leg.{w=0.2} Quit it."

                $ relationship(change="affinity-", multiplier=3)
                $ relationship(change="trust-", multiplier=3)

    elif persistent.jn_player_nicknames_bad_given_total == 4:
        # Player is locked out of nicknaming; this is why we can't have nice things
        n "Yeah,{w=0.1} no.{w=0.2} I've heard enough.{w=0.2} I don't need to hear any more."
        n "When will you learn that your actions have consequences?"
        n "..."
        n "You know what?{w=0.2} Don't even bother answering."
        n "I warned you,{w=0.1} [player].{w=0.2} Remember that."

        $ relationship(change="affinity-", multiplier=5)
        $ relationship(change="trust-", multiplier=5)
        $ persistent.jn_player_nicknames_allowed = False
        $ persistent.jn_player_nicknames_current_nickname = None
        $ n_name = "Natsuki"

    return

# Natsuki advises the player on good sleeping habits
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sleeping_well",
            unlocked=True,
            prompt="Sleeping well",
            conditional="persistent.jn_total_visit_count >= 5",
            category=["Health", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sleeping_well:
    n "Huh..."
    n "Hey,{w=0.1} [player].{w=0.2} Let me ask you a question,{w=0.1} 'kay?"
    n "How do you sleep at night?"
    n "Be honest.{w=0.2} How do you do it?"
    n "..."
    n "Ehehe.{w=0.2} Did I get you?"
    n "But seriously,{w=0.2} [player].{w=0.2} Do you struggle with your sleep?"

    # Quip if the player has been around a while, or has admitted they're tired
    if utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n "I mean,{w=0.1} you {i}have{/i} been here for a while now..."
        n "So I kinda figured you might be feeling a little sleepy anyway."

    elif admissions.last_admission_type == admissions.TYPE_TIRED:
        n "I mean,{w=0.1} you even {i}said{/i} you were tired before."
        n "So...{w=0.3} it only makes sense to ask,{w=0.1} right?{w=0.2} Anyway..."

    n "I'll admit,{w=0.1} I get the odd sleepless night myself.{w=0.2} It's the worst!"
    n "There's nothing I hate more than tossing and turning,{w=0.1} just waiting for my body to decide it's time for tomorrow to happen."
    n "But...{w=0.3} you know what they say,{w=0.1} [player] -{w=0.1} with suffering..."
    n "...Comes wisdom!"
    n "And luckily for you,{w=0.1} I don't mind sharing.{w=0.2} Ehehe."
    n "So,{w=0.1} listen up -{w=0.1} it's time for another lesson from yours truly!"
    n "Alright -{w=0.1} first,{w=0.1} cut the crap!{w=0.2} If you're trying to sleep,{w=0.1} anything high-sugar or high-caffeine is your enemy."
    n "So before anything else,{w=0.1} ditch the soda and coffee.{w=0.2} You can thank me later."
    n "Next up -{w=0.1} no screens!{w=0.2} Including this one, [player]."
    n "No screen means no bright lights or distractions to keep you up,{w=0.1} obviously."
    n "If you're tired then the last thing you need is something beaming whatever at you."
    n "Moving on, next is temperature!{w=0.2} If it's hot,{w=0.1} use thinner sheets and vice versa."
    n "Nothing disrupts your sleep more than having to rip off blankets,{w=0.1} or pull some out."
    n "Keeping up with me so far,{w=0.1} [player]?{w=0.2} I'm almost done,{w=0.1} don't worry."
    n "Lastly...{w=0.3} get comfortable!"
    n "Make sure you have enough pillows to support your head,{w=0.1} or maybe even play some quiet music if you find that helps."
    n "...And that's about it!"
    n "You should have known at least a few of those already,{w=0.1} but at any rate..."
    n "I hope you can rest easy with your newfound knowledge,{w=0.1} [player]!"
    n "Ehehe."

    return

# Natsuki discusses aging, and her carefree attitude towards the age-gap in relationships
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_aging",
            unlocked=True,
            prompt="Aging",
            conditional=None,
            category=["Life"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_aging:
    n "You know,{w=0.1} [player]..."
    n "I think most people share a bunch of fears."
    n "You get what I mean,{w=0.1} right?{w=0.2} Like presenting stuff to a room full of people,{w=0.1} or failing a test."
    n "Of course,{w=0.1} it's rare to find one that {i}everyone{/i} has..."
    n "Or at least something that makes anyone feel uneasy."
    n "But...{w=0.3} I think I found one!"
    n "What am I thinking of,{w=0.1} you ask?"
    n "Well...{w=0.3} it's actually kinda boring,{w=0.1} really."
    n "I was actually thinking about growing older."
    n "Have you ever thought much about it,{w=0.1} [player]?"
    n "It's probably the last thing on your mind if you're pretty young."
    n "But I think as you actually get older,{w=0.1} it starts to creep in."
    n "You might have less energy,{w=0.1} or friends and family begin drifting away..."
    n "Birthdays lose all meaning -{w=0.1} you might even dread them!"
    n "The signs appear in a bunch of ways,{w=0.1} but that's what makes it unnerving."
    n "Everyone experiences it differently,{w=0.1} and we don't even know what happens after the end!"
    n "Spooky,{w=0.1} huh?"
    n "Although... I guess you could say that's more the fear of the unknown than aging itself."
    n "What does wind me up though is how immature people can be about it."
    n "Especially when it comes to relationships between different ages!"
    n "People just get so preachy about it..."
    n "Like...{w=0.3} as long as they're both happy,{w=0.1} and nobody is being hurt or made uncomfortable,{w=0.1} who actually cares?"
    n "It's just like most stuff,{w=0.1} really."
    n "Besides,{w=0.1} it's not like being a certain age means you {i}have{/i} to be a certain way."
    n "I mean...{w=0.3} look at Yuri!"
    n "Being all old-fashioned like that -{w=0.1} you'd think she's retired!"
    n "But anyway...{w=0.3} I think we got side-tracked."
    n "I don't really care how old you are,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n "I love you all the same,{w=0.1} [chosen_tease]."
        n "Don't forget that,{w=0.1} 'kay?"
        n "Or you might make me a little angry.{w=0.2} Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "You've been pretty awesome to me all the same."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "You're always fun to hang around with!"

    else:
        n "But...{w=0.3} just in case?"
        n "We're only having one candle on your birthday cake.{w=0.2} Sorry."
        n "Ahaha!"

    return

# Natsuki discusses the concept of work-life balance, and how it can be difficult to disconnect
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_life_balance",
            unlocked=True,
            prompt="Work-life balance",
            conditional=None,
            category=["Life"],
            nat_says=True,
            affinity_range=(jn_affinity.RUINED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_life_balance:
    if jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        n "You know,{w=0.1} [player]..."

    n "I think it's pretty easy to let your academic or work life creep into your personal time nowadays."
    n "I mean...{w=0.3} think about it."
    n "With everyone having mobile phones,{w=0.1} plus usually some kinda computer at home -{w=0.1} it's hard not to be connected somehow."
    n "And like...{w=0.3} if there's already that connection,{w=0.1} then what's to stop work from bugging you during your time off?"
    n "Or classmates asking for help at the last possible minute?"

    if jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        n "It just gets annoying -{w=0.1} like everyone expects you to always be around to chip in a little more,{w=0.1} or get something done!"
        n "Overwhelming,{w=0.1} right?"
        n "Huh.{w=0.2} Actually...{w=0.3} now that I think about it..."
        n "It isn't like that kind of intrusion is only limited to when you're away either."
        n "I've heard {i}way{/i} too many stories of people doing stupid amounts of overtime at work -{w=0.1} sometimes not even paid!"
        n "Or even students studying late into the night until they collapse... it's pretty crazy."

    else:
        n "It just gets annoying -{w=0.1} everyone expects you to always be around to do more."
        n "Actually,{w=0.1} now that I think about it..."
        n "It isn't like that kind of thing is only limited to when you're away either."
        n "I've heard too many stories of people doing stupid amounts of overtime at work -{w=0.1} often not even paid."
        n "Or even students studying late into the night until they collapse..."
    
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Ugh...{w=0.3} I just wish people would value their own time more."
        n "..."
        n "Hey,{w=0.1} [player]..."
        n "I don't know if you're working,{w=0.1} or studying,{w=0.1} or what..."
        n "But you better not be letting whatever it is take over your life.{w=0.2} Understand?"

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "You are {i}more{/i} than your career,{w=0.1} or your education.{w=0.2} You have your own wants and needs that matter too."
            n "I don't want some dumb job or stupid assignment to take over your life."
            n "You're...{w=0.3} way more important than either of those,{w=0.1} [player].{w=0.2} Trust me."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n "Besides..."
                n "You and your time are mine first, [player]."
                n "I already called dibs,{w=0.1} a-{w=0.1}after all.{w=0.2} Ehehe..."

        else:
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "People are more than what they do for a living,{w=0.1} after all.{w=0.2} And that includes you too, [chosen_tease]!"
        
    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Makes me wish people would value their own time more."
        n "...I guess that includes you too,{w=0.1} [player]."
        n "Try not to let work or studying rule your life.{w=0.2} You've got better things to do."
        n "...Like being a decent friend to others for a change.{w=0.2} Am I right?"

    else:
        n "People need to value their own time more,{w=0.1} I guess."
        n "...Heh."
        n "Maybe I should follow my own advice..."
        n "Because clearly being here is a waste of my time too."

    return

# Natsuki discusses her dislike of the horror genre
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_horror",
            unlocked=True,
            prompt="Thoughts on horror",
            conditional=None,
            category=["Natsuki", "Media", "Literature"],
            nat_says=True,
            affinity_range=(jn_affinity.RUINED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_horror:

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "You know,{w=0.1} [player]..."
        n "I don't think I ever actually explained why I dislike horror so much."
        n "I know I mentioned it before,{w=0.1} but I was kinda caught off guard at the time."
        n "Honestly?"
        n "Everyone has their tastes,{w=0.1} right? And I can get why people enjoy it."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "You know, I don't think I explained why I dislike horror."
        n "I get everyone has their tastes, but it isn't for me."

    else:
        n "...I was about to share some of my thoughts on horror with you."
        n "Or at least,{w=0.1} I was thinking about it."
        n "...But then do you know what I realized,{w=0.1} [player]?"
        n "I hate horror -{w=0.1} not that you'd care -{w=0.1} and honestly?"
        n "...I'm starting to think being here with you is horror enough.{w=0.2} Heh."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Like Yuri!"
        n "It's suspenseful,{w=0.1} and fears are a super powerful motivator for characters!"
        n "So don't get me wrong{w=0.1} -{w=0.1} I can totally appreciate the effort that goes into it."
        n "...When it isn't just stupid jumpscares,{w=0.1} a-{w=0.1}anyway."

    else:
        n "I get the effort that goes into it.{w=0.2} For the most part."

    n "But..."
    n "When I read something -{w=0.1} or watch something -{w=0.1} I'm doing it because for me,{w=0.1} it's how I relax."
    n "I don't want to be made to feel uneasy."
    n "I don't want to be made to jump."
    n "I don't want to have to see gross stuff."
    n "I...{w=0.3} just want to sit back,{w=0.1} feel good and just escape for a while."
    n "There's more than enough nasty things going out there already,{w=0.1} you know?"
    n "Some things closer to home than others."
    n "..."
    n "So...{w=0.3} yeah.{w=0.1} That's about all I had to say about it."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Though...{w=0.3} if you want to put something on,{w=0.1} [player]?{w=0.2} Go ahead."
        n "If it's you,{w=0.1} I think I can put up with it..."
        n "But we're keeping the volume low.{w=0.2} 'Kay?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Don't mind me though,{w=0.1} [player].{w=0.2} If you wanna watch something,{w=0.1} go for it!"
        n "Just don't expect me to sit there with you.{w=0.2} Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "..."
        n "I {i}would{/i} ask that if you were gonna watch something like that,{w=0.1} then to warn me first..."
        n "But you wouldn't listen to me anyway,{w=0.1} would you?"

    return

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
            category=["date"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_beach:
    n "I love the beach"
    n "Let's go!"
    $ main_background.changeLocation(beach)
    $ main_background.draw(full_redraw=True)
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_room",
            unlocked=True,
            prompt="Let's return",
            player_says=True,
            category=["date"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_room:
    n "Heading back then?"
    n "Alright!"
    $ main_background.changeLocation(classroom)
    $ main_background.draw(dissolve_all=True, full_redraw=True)
    return
