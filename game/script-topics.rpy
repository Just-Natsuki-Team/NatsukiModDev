default persistent._topic_database = dict()

init python in topics:
    import store
    TOPIC_MAP = dict()
    store.persistent._topic_database.pop("talk_did_you_have_pets")

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
    if player_screenshots_blocked:
        n "Uh...{w=0.3} no,{w=0.1} I'm not turning the camera back on,{w=0.1} [player]."
        return

    if persistent.affinity >= 700:
        if player_screenshots_permission:
            n "Ahaha!{w=0.2} I already said you could,{w=0.1} dummy!"
            n "I'm ready,{w=0.1} so take one whenever!"

        else:
            n "Eh?{w=0.2} A picture?{w=0.2} Of course!"
            $ player_screenshots_permission = True
        return

    elif persistent.affinity >= 500:
        if player_screenshots_permission:
            n "Huh?{w=0.2} Didn't you ask me that already?"
            n "It's fine,{w=0.1} so go ahead!"

        else:
            n "Oh?{w=0.2} You wanna take a picture?{w=0.2} Alright!"
            $ player_screenshots_permission = True
        return

    elif persistent.affinity >= 300:
        if player_screenshots_permission:
            n "Hmm?{w=0.2} A picture?{w=0.2} Well,{w=0.1} okay."
            $ player_screenshots_permission = True

        else:
            n "Uuuu...{w=0.3} I just said you could,{w=0.1} [player]."
            n "Just take it whenever,{w=0.1} alright?"
        return

    elif persistent.affinity >= 100:
        if player_screenshots_permission:
            n "Eh?{w=0.2} I already said you could,{w=0.1} [player]. Just take it soon,{w=0.1} alright?"
            n "I don't really like being kept on hold like this..."

        else:
            # Indecisive; this lets lower affinity players have a chance at screenshots without upsetting Natsuki
            n "A picture?{w=0.2} I'm not sure...{w=0.3} let me think about it."
            n "..."
            # We take into account the player's behaviour with pictures so far
            $ natsuki_approves = random.randint(1, 100) <= ((100 - bad_screenshot_streak) * 25)
            if natsuki_approves:
                n "Fine,{w=0.1} I guess.{w=0.1} Take it whenever."
                $ player_screenshots_permission = True

            else:
                n "I'm sorry,{w=0.1} [player].{w=0.1} I don't want any pictures taking of me right now."
                $ player_screenshots_permission = False
        return

    elif persistent.affinity >= -50:
        n "No.{w=0.1} I {b}don't{/b} want my picture taken."
        $ player_screenshots_permission = False
        return

    else:
        n "..."
        $ player_screenshots_permission = False

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

    if store.jn_affinity.get_affinity_state() > store.jn_affinity.ENAMORED:
        $ player_or_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)

    else:
        $ player_or_endearment = player

    n "Huh?{w=0.2} Did I ever have any pets?"
    n "You know,{w=0.1} I really wish I had.{w=0.1} But I was never allowed anything!"
    n "It was always about the mess it would make,{w=0.1} or how much it would cost,{w=0.1} or literally anything else they could think of..."
    n "Even when I said {i}I'd{/i} take care of everything!"
    n "Ugh..."
    n "It still annoys me...{w=0.3} but then again,{w=0.1} it's not like I can't keep a pet here instead,{w=0.1} right?{w=0.1} Ehehe."
    n "What about you,{w=0.1} [player]?{w=0.2} Do you have any pets?"
    menu:
        "Yes, I do.":
            n "Oh!{w=0.2} Oh oh oh!{w=0.2} You gotta tell me,{w=0.1} [player]!"
            n "What do you have?{w=0.2} What do you have?"
            menu:
                "Arachnids":
                    n "A-ahh!{w=0.2} G-gross!{nw}"
                    n "..."
                    n "Ahaha...{w=0.3} sorry..."
                    n "Spiders and scorpions and stuff really...{w=0.3} aren't...{w=0.3} my thing."
                    n "But I'm sure you take great care of yours,{w=0.2} [player_or_endearment]!"

                "Birds":
                    n "Oh!{w=0.2} Neat!"
                    n "I don't think I'd keep birds myself,{w=0.1} but they brighten up rooms for sure!"
                    n "It doesn't get too noisy for you,{w=0.1} I hope?"
                    n "I'm sure yours appreciate your company though."

                "Cats":
                    n "Yay!{w=0.2} Cats!"
                    n "I really wish I had one,{w=0.1} I love seeing all the dumb situations they get into!"
                    n "I hope you didn't just say that because I like them,{w=0.1} though.{w=0.1} Ehehe."
                    n "Just don't pamper it too much,{w=0.1} [player_or_endearment]!"

                "Dogs":
                    n "Oh! A dog? Awesome!"
                    n "I don't think a dog would be my first choice,{w=0.1} what with all the walks and all that."
                    n "But I can't think of a more loving pet!"
                    n "I hope yours looks after you as much as you look after it!"

                "Fish":
                    n "Ooh!{w=0.2} Fish are interesting!"
                    n "I don't think I'd call them super affectionate personally..."
                    n "But I think they're a neat way to relieve stress!{w=0.2} They must be calming to watch in their own little world."
                    n "I bet you feel like you could lose yourself in that tank!{w=0.2} Ehehe."

                "Gerbils":
                    call did_you_have_pets_option_gerbil_mice_rat

                "Mice":
                    call did_you_have_pets_option_gerbil_mice_rat

                "Rats:":
                    call did_you_have_pets_option_gerbil_mice_rat

                "Hamsters":
                    n "Oh my gosh!{w=0.2} Hammies!"
                    n "Aaaaaah!{w=0.2} I love them so much!"
                    n "I love their little tails,{w=0.1} and their little paws,{w=0.1} and their little whiskers,{w=0.2} and-"
                    n "And!{w=0.2} And..."
                    n "..."
                    n "A-ahaha!{w=0.2} It would appear I got a little carried away..."
                    n "..."
                    n "You better take good care of yours,{w=0.1} alright?"

                "Insects":
                    n "Uhmm..."
                    n "...I wish I could share your enthusiasm!{w=0.2} Ahaha..."
                    n "I don't think I could stomach creepy crawlies myself."
                    n "You've certainly got an...{w=0.3} interesting taste,{w=0.1} [player_or_endearment]."
                    n "But I'm sure you take great care of yours!"

                "Something else":
                    n "Ooh!{w=0.2} An exotic owner, are we?"
                    n "I wonder if that says something about the rest of your tastes?{w=0.2} Ehehe."
                    n "I trust you take good care of yours.{w=0.1} Uncommon pets can be pretty demanding!"

        "No, I don't.":
            n "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
            n "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player_or_endearment]!"
            n "I wanna hear all about it!"

        "I used to.":
            n "Oh...{w=0.3} oh gosh."
            n "I'm really sorry to hear that,{w=0.1} [player_or_endearment]."
            n "I hope you're managing okay now."
            n "..."
            n "I...{w=0.3} think we should talk about something else, alright?"
            
    return

label did_you_have_pets_option_gerbil_mice_rat:
    n "Aha!{w=0.2} I knew you couldn't resist something small and cute!"
    n "..."
    n "Jeez,{w=0.1} stop looking at me like that!{w=0.2} Anyway..."
    n "Cleaning the cage sounds kinda annoying... especially if you gotta take it apart every time."
    n "But I'm sure you stay on top of it,{w=0.1} [player_or_endearment]!"
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
    n "(service pets)"
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
