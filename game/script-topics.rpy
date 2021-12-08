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

# Hobby data
default persistent.jn_player_gaming_frequency = None
default persistent.jn_player_can_drive = None

# Romance data
default persistent.jn_player_love_you_count = 0

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

# Natsuki's thoughts on having her picture taken via the ingame screenshot system
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_having_pictures_taken",
            unlocked=True,
            prompt="How do you feel about having your picture taken?",
            category=["Natsuki", "Photography", "Life"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_having_pictures_taken:

    if not persistent.jn_first_screenshot_taken:
        n 1uskwr "W-wait...{w=0.3} you're telling me there's a camera here?{w=0.2} Are you kidding me?!"
        n 1kbktr "Uuuu-"
        n 1kslaj "I've never liked having my picture taken without my permission..."
        n 1ksgsl "Just...{w=0.3} please don't take any pictures of me unless I ask,{w=0.1} okay [player]?"
        n "It'd really mean a lot to me."
        n 1kllsf "I hope you can understand."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1tnmsf "Hmm?{w=0.2} Pictures of me?"
            n 1nllsl "Honestly,{w=0.1} I don't think I'll ever be completely comfortable with them..."
            n 1unmss "But I trust you to make a good shot!"
            n 1uchlg "As long as you ask,{w=0.1} I've got no problem with it!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            if player_screenshots_blocked:
                n 1fsqpu "Really, [player]?{w=0.1} You're asking me about this {i}now{/i}?"
                n 1fslaj "You know {i}perfectly well{/i} how I feel about this."
                n 1fsgbo "I don't hate you,{w=0.1} but please try to remember how I feel before you do stuff like that."
                n "I'm still gonna keep that turned off for now."

            else:
                n 1ncuaj "H-huh?{w=0.2} Pictures of me?"
                n 1nlrsr "Not a fan,{w=0.1} honestly -{w=0.1} but you knew that much already,{w=0.1} [player]."
                n 1knmpu "It's just..."
                n 1kcspu "I really...{w=0.3} need...{w=0.3} my privacy.{w=0.1} It matters a lot to me."
                n 1kwmpu "You understand,{w=0.1} right?"
                n 1knmnv "So please,{w=0.1} if you ever wanna take a picture,{w=0.1} can you ask me first?"
                menu:
                    n "Will you do that for me?"

                    "Of course!":
                        n 1kcssg "Thanks,{w=0.1} [player]."
                        n 1knmss "That really...{w=0.3} means a lot to me."

                    "I'll think about it.":
                        n 1fwmsf "[player]...{w=0.3} come on.{w=0.1} I'm being serious here."
                        n "Please don't mess me around with this."
                        n 1nnmaj "Make sure you ask,{w=0.1} okay?"

                    "...":
                        n 1nunfr "..."
                        n 1fnmaj "Uh...{w=0.3} [player]?{w=0.1} This isn't very funny."
                        n 1fllsl "Make sure you ask,{w=0.1} okay?{w=0.1} For my sake."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n 1fsqsl "Pictures? Really?"
            n 1fsqaj "I don't think I want to have you taking my picture,{w=0.1} [player]."
            n 1fslfr "Let's talk about something else."

        else:
            n 1kplpu "Please...{w=0.3} don't try to pretend like you care about how I feel about pictures."
            n 1kcssr "I'm done talking about this,{w=0.1} [player]."
    return

# Natsuki discusses her lack of pet with the player, and asks about theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="Did you ever have any pets?",
            category=["Life", "Animals", "Family"],
            player_says=True,
            affinity_range=(jn_aff.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:

    # Check to see if the player and Natsuki have already discussed this
    $ already_discussed_pets = get_topic("talk_did_you_have_pets").shown_count > 0

    if already_discussed_pets:
        n 1tnmsl "Wait...{w=0.3} didn't we talk about this before,{w=0.1} [player]?"
        n 1unmsl "Well anyway,{w=0.1} not much has changed."
        n 1ullsl "I still don't have a pet,{w=0.1} as much as I wish I did."
        n 1nnmsm "Maybe I should get one soon.{w=0.2} Hmm..."

    else:
        n 1tnmsl "Huh?{w=0.2} Did I ever have any pets?"
        n 1fllaj "You know,{w=0.1} I really wish I had.{w=0.1} But I was never allowed anything!"
        n 1fsgpo "It was always about the mess it would make,{w=0.1} or how much it would cost,{w=0.1} or literally anything else they could think of..."
        n 1fnmaj "Even when I said {i}I'd{/i} take care of everything!"
        n 1fslem "Ugh..."
        n 1fslun "It still annoys me...{w=0.3}{nw}" 
        extend 1uchgn "but then again,{w=0.1} it's not like I can't keep a pet here instead,{w=0.1} right?{w=0.1} Ehehe."

    if persistent.jn_player_pet is None:
        menu:
            n "What about you,{w=0.1} [player]? Do you have any pets?"

            "Yes, I do.":
                n 1uspaw "Oh!{w=0.2} Oh oh oh!{w=0.2} You gotta tell me,{w=0.1} [player]!"
                n 1uspbs "What do you have?{w=0.2} What do you have?"
                call pet_options_a

            "No, I don't.":
                n 1usgem "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n 1nchhn "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n "I wanna hear all about it!"

            "I used to.":
                n 1kplaj "Oh...{w=0.3} oh gosh."
                n 1kllbo "I'm really sorry to hear that,{w=0.1} [player]."
                n 1knmbo "I hope you're managing okay now."
                n 1kcsbo "..."
                n 1knmbo "I...{w=0.3} think we should talk about something else, alright?"

    else:
        n 1unmbs "What about you,{w=0.1} [player]?"
        menu:
            n "Did you get another one?"

            "Yes, I did.":
                n 1uspaw "Ooh...{w=0.3} you gotta tell me!{w=0.2} What did you get?"
                call pet_options_a

            "No, I didn't.":
                n 1nnmaj "Oh.{w=0.2} Well,{w=0.1} that's fair."
                n 1nnmsm "You're already giving a home to something,{w=0.1} so I won't complain!"

            "I lost one.":
                n 1knmaj "Oh...{w=0.3} oh jeez..."
                n 1knmfr "I'm so sorry,{w=0.1} [player].{w=0.2} Are you okay?"
                n 1kllbo "Maybe we should talk about something else to keep your mind off things..."
                n 1knmbo "I'm here for you,{w=0.1} [player]."

    return

label pet_options_a:
    menu:
        n "What did you get?"

        "Birds":
            n 1uchgn "Oh!{w=0.2} Neat!"
            n 1nnmsm "I don't think I'd keep birds myself,{w=0.1} but they brighten up rooms for sure!"
            n 1tnmaj "It doesn't get too noisy for you,{w=0.1} I hope?"
            n 1uchsm "I'm sure yours appreciate your company though."
            $ persistent.jn_player_pet = "birds"

        "Cats":
            n 1uchsm "Yay!{w=0.2} Cats!"
            n 1uchgn "I really wish I had one,{w=0.1} I love seeing all the dumb situations they get into!"
            n 1unmbs "I hope you didn't just say that because I like them,{w=0.1} though.{w=0.1}{nw}"
            extend 1uchsm "Ehehe."
            n 1tnmsm "Just don't pamper it too much,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "cats"

        "Dogs":
            n 1uwdaj "Oh!{w=0.2} A dog?{w=0.2}{nw}"
            extend 1uchbs "Awesome!"
            n 1nnmsm "I don't think a dog would be my first choice,{w=0.1} what with all the walks and all that."
            n 1uchbs "But I can't think of a more loving pet!"
            n "I hope yours looks after you as much as you look after it!"
            $ persistent.jn_player_pet = "dogs"
            
        "Ferrets":
            n 1unmlg "Oh!{w=0.2} A ferret?
            n 1uchbs "That's sooo cute!"
            n "They're like cats!{w=0.2} Or pandas!{w=0.2} But long!"
            n 1uchgn "And that's a plus in my book!"
            n 1unmlg "Take good care of it for me, okay?"
            $ persistent.jn_player_pet = "ferret"

        "Fish":
            n 1unmaj "Ooh!{w=0.2} Fish are interesting!"
            n 1kllnv "I don't think I'd call them super affectionate personally..."
            n 1uchgn "But I think they're a neat way to relieve stress!{w=0.2} They must be calming to watch in their own little world."
            n "I bet you feel like you could lose yourself in that tank!{w=0.2} Ehehe."
            $ persistent.jn_player_pet = "fish"

        "More...":
            call pet_options_b

    return

label pet_options_b:
    menu:
        n "What did you get?"
        
        "Gerbils":
            n 1kspaw "Awww!{w=0.2} I like gerbils!"
            n 1uchbs "It's so cute how they live in little groups to keep each other company."
            n 1unmbs "They're good at digging,{w=0.1} too -{w=0.2} like seriously good!"
            n "Take good care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "gerbils"
            
        "Guinea pigs":
            n 1unmaj "Ooh!{w=0.2} I like guinea pigs!"
            n 1uchbs "I don't know much about them,{w=0.1} but I love the little sounds they make."
            n "It's like they're always having a conversation!"
            n 1unmbs "Take good care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "guinea pigs"

        "Hamsters":
            n 1uspbs "Oh my gosh!{w=0.2} Hammies!"
            n 1uchbs "Aaaaaah!{w=0.2} I love them so much!"
            n 1uspbs "I love their little tails,{w=0.1} and their little paws,{w=0.1} and their little whiskers,{w=0.2} and-"
            n "And!{w=0.2} And..."
            n 1uwdbol "..."
            n 1uchbsl "A-{w=0.1}ahaha!{w=0.2} It would appear I got a little carried away..."
            n 1uchgnf "..."
            n 1fllgnf "You better take good care of yours for me,{w=0.1} alright?"
            $ persistent.jn_player_pet = "hamsters"

        "Horses":
            n 1uspaw "W-{w=0.1}wow!{w=0.2} You aren't just messing with me,{w=0.1} right?!"
            n 1uspbs "Horses?!{w=0.2} That's amazing,{w=0.1} [player]!"
            n 1uchbs "You totally gotta teach me how to ride some day!"
            n 1uchbs "Make sure you visit yours often,{w=0.1} alright?"
            n 1unmlg "Oh -{w=0.2} and wear a helmet if you ride!"
            $ persistent.jn_player_pet = "horses"

        "Insects":
            n 1twmsc "Ack-{nw}"
            n 1kslup "Nnnnn..."
            n 1kwmsg "...I wish I could share your enthusiasm!{w=0.2}{nw}
            extend 1kllss "Ahaha..."
            n 1ksqun "I don't think I could stomach creepy crawlies myself."
            n 1ksrun "You've certainly got an...{w=0.3} interesting taste,{w=0.1} [player]."
            n 1kwmss "But I'm sure you take great care of yours!"
            $ persistent.jn_player_pet = "insects"

        "More...":
            call pet_options_c

        "Back...":
            call pet_options_a

    return

label pet_options_c:
    menu:
        n "What did you get?"

        "Mice":
            n "Ehehe.{w=0.2} Mice are adorable!"
            n "I'm still not sure how I feel about the tail..."
            n "But they're so curious and sociable!{w=0.2} I love watching them play together."
            n "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "mice"
            
        "Rats":
            n 1unmbs "Rats,{w=0.1} huh?"
            n "Were you expecting me to be grossed out?"
            n 1uchbs "Ahaha!"
            n "Rats are fine.{w=0.2} They're surprisingly intelligent,{w=0.1} too!"
            n "Are you perhaps training yours,{w=0.1} [player]?{w=0.2} Ehehe."
            n 1unmbs "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "rats"

        "Rabbits":
            n 1kspaw "Awwwwww!{w=0.2} Bunnies!"
            n "They're so cuuute!{w=0.2} I love them!"
            n 1uchbs "Especially the ones with the floppy ears,{w=0.1} they look so cuddly!"
            n "It's a shame they need so much space,{w=0.1} though."
            n "But I'm sure yours have plenty of room to roam!{w=0.2} Ehehe."
            $ persistent.jn_player_pet = "rabbits"

        "Something else":
            n 1unmaj "Ooh!{w=0.2} An exotic owner, are we?"
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
            category=["Animals"],
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

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "I love you,{w=0.1} [player]."
            return

    else:
        n "They work in a bunch of places.{w=0.2} Airports and rescues and stuff,{w=0.1} usually."
        n "But I really like emotional support animals."
        n "They're like specially tame pets that are used to comfort those having a bad time."
        n "..."
        n "You know, [player].{w=0.2} To be perfectly honest with you?"
        n "Sometimes I feel like I could use one."
        n "Aha..."
        return

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
            return

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
        return

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
    n "But do whatever works for you; {w=0.1}we all have our own comfort zones!"
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
            category=["Life", "You", "Health", "Food"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n "Hey,{w=0.1} [player]..."
    menu:
        n "Have you eaten today?"

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
        n "What about you,{w=0.1} [player]?"
        menu:
            n "Still rooting for [persistent.jn_player_favourite_season]?"
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
        n "Perhaps I should timebox our time together,{w=0.1} [player]."
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
            category=["Health", "Food"],
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
            category=["You"],
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
                return

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
                return

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
        n "Now,{w=0.1} let's see...{w=0.3} what else..."
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
            category=["Food", "Health"],
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
            category=["Transport"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:
    # Check to see if the player and Natsuki have already discussed if Nat can drive in this topic, or the "are you into cars?" topic
    $ already_discussed_driving = get_topic("talk_driving").shown_count > 0 or get_topic("talk_are_you_into_cars").shown_count > 0
    
    n "Pffft!"
    n "Ahaha!{w=0.2} What kind of a question is that,{w=0.1} [player]?"
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)

    if already_discussed_driving:
        n "I already told you I can't drive,{w=0.1} [chosen_tease]!{w=0.2} I don't even have a license!"
        n "And even if I wanted to,{w=0.1} I don't think I could afford it..."

    else:
        n "Of course I can't drive,{w=0.1} [chosen_tease]!{w=0.2} I don't even have a license!"
        n "I mean...{w=0.3} even if I wanted to learn,{w=0.1} I don't think I could afford it."

    n "Lessons are super expensive nowadays!"
    n "And then there's tests,{w=0.1} insurance,{w=0.1} fuel,{w=0.1} parking...{w=0.3} it's actually pretty gross how fast it all adds up."
    n "I think I'd rather stick to public transport and my own two feet."
    n "But what about you,{w=0.1} [player]?"

    # Player has never confirmed if they can/cannot drive
    if persistent.jn_player_can_drive is None:
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

                $ persistent.jn_player_can_drive = True
                return

            "Yes, but I don't right now.":
                n "Oh?{w=0.2} Is something wrong with your car,{w=0.1} [player]?"
                n "Or perhaps...{w=0.3} you just don't own one at the moment?"
                n "Well,{w=0.1} I'm not one to judge.{w=0.2} I'm sure you manage just fine."
                n "Besides,{w=0.1} you're helping the environment too,{w=0.1} right?"

                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                    n "Thoughtful as always,{w=0.1} [player]."
                    n "I like that about you."
                    n "Ehehe."

                $ persistent.jn_player_can_drive = True
                return

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

                $ persistent.jn_player_can_drive = False
                return

    # Player stated they can drive previously
    elif persistent.jn_player_can_drive:
        menu:
            n "Doing much driving?"

            "Yes, I'm driving frequently.":
                n "Ah,{w=0.1}  so you're at home on the roads,{w=0.1} are you?"
                n "Fair enough I suppose -{w=0.1} just remember to drive safe,{w=0.1} [player]!"

            "I only drive sometimes.":
                n "Well hey,{w=0.1} at least you're saving on fuel,{w=0.1} right?{w=0.2} That doesn't sound like a bad thing to me."
                n "Besides,{w=0.1} it just means you can save the miles for ones you enjoy!"

            "No, I'm not driving much.":
                n "Oh?{w=0.2} That sounds like a bonus to me,{w=0.1} honestly!"
                n "Just make sure you still get out there if you aren't driving around much though,{w=0.1} 'kay?"

            "No, I can't drive anymore.":
                n "Oh...{w=0.3} did something happen?"
                n "I'm sorry to hear it,{w=0.1} [player]."
                n "But at least that means more time to spend here,{w=0.1} right?{w=0.2} Ahaha..."
                $ persistent.jn_player_can_drive = False

        return

    # Player admitted they cannot drive previously
    else:
        menu:
            n "Anything new happening with you on the driving front?"

            "I'm learning to drive!":
                n "Ooh!{w=0.2} Nice,{w=0.1} [player]!"
                n "Don't sweat the test,{w=0.1} alright?{w=0.2} I'm sure you'll do fine!"

                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                    n "I believe in you,{w=0.1} [player]!"

            "I passed my test!":
                n "No kidding?"
                n "Yaaay!{w=0.2} Congratulations,{w=0.1} [player]!"

                if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                    n "I'm so proud of you!{w=0.2} I knew you could do it,{w=0.1} dummy!"

                n "Just make sure you keep up the good habits when you continue learning on your own,{w=0.1} alright?{w=0.2} Ahaha."
                $ persistent.jn_player_can_drive = True

            "I can drive again!":
                n "Hey!{w=0.2} Nice going,{w=0.1} [player]!"
                n "Drive safe!"
                $ persistent.jn_player_can_drive = True

            "Nope, nothing new.":
                n "Oh?{w=0.2} Well,{w=0.1} fair enough!"
                n "You and me both,{w=0.1} in that case?{w=0.2} Ahaha."

        return
    return

# Natsuki laments her inability to drive and questions the player on if they can
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sustainable_fashion",
            unlocked=True,
            prompt="Sustainable fashion",
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

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
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
        $ nickname_type = jn_nicknames.get_nickname_type(nickname)

    if nickname_type == jn_nicknames.TYPE_INVALID:
        n "Uhmm...{w=0.3} [player]?"
        n "I don't think that's a nickname at all."
        n "I'll...{w=0.3} just stick with what I have now,{w=0.1} thanks."
        return

    elif nickname_type == jn_nicknames.TYPE_LOVED:
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

    elif nickname_type == jn_nicknames.TYPE_DISLIKED:
        n "Come on,{w=0.1} [player]...{w=0.3} really?"
        n "You know I'm really not comfortable being called that."
        n "..."
        n "I'm...{w=0.3} just going to pretend you didn't say that,{w=0.1} alright?"
        return

    elif nickname_type == jn_nicknames.TYPE_HATED:
        n "W-{w=0.1}what?{w=0.2} What did you just call me?!"
        n "[player]!{w=0.2} I can't believe you!"
        n "Why would you call me that?{w=0.2} That's awful!"
        n "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_PROFANITY:
        n "E-{w=0.1}excuse me?!"
        n "What the hell did you just call me,{w=0.1} [player]?!"
        n "..."
        n "I seriously can't believe you,{w=0.1} [player]."
        n "Why would you do that?{w=0.1} Are you trying to upset me?"
        n "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_FUNNY:
        n "Pffft!"
        n "Ahaha!"
        n "[nickname]?{w=0.2} What kind of nickname is that meant to be,{w=0.1} [player]?"
        n "Well...{w=0.3} you're just lucky I have a healthy sense of humour."
        n "[nickname] it is,{w=0.1} I guess!{w=0.2} Ehehe."

        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        return

    elif nickname_type == jn_nicknames.TYPE_NOU:
        show placeholder_natsuki wink zorder jn_placeholders.NATSUKI_Z_INDEX
        n "No you~."
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

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)
        $ relationship(change="affinity-", multiplier=2)
        $ relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 2:
        n "I can't believe you did that again to me,{w=0.1} [player]."
        n "I told you it hurts,{w=0.1} and you went ahead anyway!"
        n "..."
        n "I...{w=0.3} really...{w=0.3} like you, [player].{w=0.2} It hurts extra bad when it's you."
        n "Don't test my patience like this.{w=0.2} You're better than that."

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)
        $ relationship(change="affinity-", multiplier=2)
        $ relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 3:
        n "You are honestly unbelievable,{w=0.1} [player]."
        n "I've told you so many times now,{w=0.1} and you still won't knock it off!"
        n "..."
        n "No more warnings,{w=0.1} [player]."
        menu:
            n "Understand?"

            "I understand. Sorry, [n_name].":
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

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)

    elif persistent.jn_player_nicknames_bad_given_total == 4:
        # Player is locked out of nicknaming; this is why we can't have nice things
        n "Yeah,{w=0.1} no.{w=0.2} I've heard enough.{w=0.2} I don't need to hear any more."
        n "When will you learn that your actions have consequences?"
        n "..."
        n "You know what?{w=0.2} Don't even bother answering."
        n "I warned you,{w=0.1} [player].{w=0.2} Remember that."

        # Apply affinity/trust penalties, then revoke nickname priveleges and finally apply pending apology
        $ relationship(change="affinity-", multiplier=5)
        $ relationship(change="trust-", multiplier=5)
        $ persistent.jn_player_nicknames_allowed = False
        $ persistent.jn_player_nicknames_current_nickname = None
        $ n_name = "Natsuki"
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)

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

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
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
    n "Although...{w=0.3} I guess you could say that's more the fear of the unknown than aging itself."
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
            category=["Life", "Society"],
            nat_says=True,
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
        n "Or even students studying late into the night until they collapse...{w=0.3} it's pretty crazy."

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

# Natsuki warns against the risks of wearing headphones/headsets
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_headphones_carefully",
            unlocked=True,
            prompt="Using headphones carefully",
            category=["Health", "Music", "Technology"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_headphones_carefully:
    n "..."
    n "...?"
    n "...!"
    n "...[player]!"
    n "[player]!{w=0.2} Finally!{w=0.2} Can you hear me now?"
    n "Jeez...{w=0.3} took you long enough!"
    n "..."
    n "Ehehe."
    n "Admit it,{w=0.1} [player]!{w=0.2} I'll get you one of these days."
    n "Seriously though -{w=0.1} do you use headphones or anything like that often?"
    n "I'll admit,{w=0.1} I probably use mine more than I should."
    n "I was kinda joking about the whole hearing thing,{w=0.1} but this is important,{w=0.1} [player]."
    n "I like cranking it up too -{w=0.1} just don't make a bad habit of it."
    n "There's even warnings in some countries if you have the volume up too loud..."
    n "...And for a good reason!"
    n "Not just to protect your ears either -{w=0.1} you better be careful wearing them out and about too."
    n "I don't wanna hear about you getting knocked over because you didn't hear something coming!"
    n "Oh -{w=0.1} and one last thing,{w=0.1} actually."
    n "You might wear them to focus at work or relax at home -{w=0.1} and that's fine!"
    n "But please,{w=0.1} [player]."
    n "...Take them off every once and a while,{w=0.1} will you?{w=0.2} For other people,{w=0.1} I mean."
    n "I get it -{w=0.1} if you just wanna listen to something in peace,{w=0.1} or give yourself some room,{w=0.1} that's okay."
    n "But don't use them to barricade yourself away from everyone and everything."
    n "It's...{w=0.3} not healthy to do that either,{w=0.1} [player]."
    n "...And that's about all I had to say!"
    n "Thanks for hearing me out!{w=0.2} Ehehe."
    return

# Natsuki discusses her dislike of the horror genre
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_horror",
            unlocked=True,
            prompt="Thoughts on horror",
            category=["Media", "Literature"],
            nat_says=True,
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

# Natsuki discusses her gaming habits
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_gaming",
            unlocked=True,
            prompt="Are you into video games?",
            category=["Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_gaming:
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Gaming?"
        n "Well...{w=0.3} duh!"
        n "You bet I'm into gaming,{w=0.1} [player]!"
        n "I wouldn't say I'm the most active player...{w=0.2} but I definitely do my share of button mashing."
        n "Hmm..."
        n "I don't think I even need to ask,{w=0.1} but..."
        menu:
            n "What about you,{w=0.1} [player]?{w=0.2} Do you play often?"

            "Absolutely!":
                $ persistent.jn_player_gaming_frequency = "High"
                n "Yep!{w=0.2} Just as I suspected..."
                n "[player] is a mega-dork."
                n "Ahaha!"
                n "Relax,{w=0.1} [player]!" 
                n "I'm not much better,{w=0.1} after all."

            "I play occasionally.":
                $ persistent.jn_player_gaming_frequency = "Medium"
                n "Yeah,{w=0.1} yeah.{w=0.2} Believe what you want to believe,{w=0.1} [player]."
                n "I'm not sure I buy it,{w=0.1} though."

            "I don't play at all.":
                $ persistent.jn_player_gaming_frequency = "Low"
                n "Huh?{w=0.2} Really?"
                n "Not even the odd casual game?"
                n "It looks like I've got a lot to teach you, [player]!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Huh?{w=0.2} Video games?"
        n "Yeah,{w=0.1} I guess.{w=0.2} For what that's worth to you."

    else:
        n "Video games...?"
        n "...Heh.{w=0.2} Why,{w=0.1} [player]?"
        n "Was stomping all over my feelings not enough? "
        n "Or were you looking to see if you can stomp all over me in games too?"
        n "..."
        n "...I don't wanna talk about this any more.{w=0.2} We're done here."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Anyway,{w=0.1} putting that aside..."
        n "When it comes to my preferences?{w=0.2} I want challenge in my games!"
        n "I play for the win{w=0.1} -{w=0.1} it's me versus the developers,{w=0.1} and they're not around to stop me!"
        n "Ahaha."
        n "I'm actually more into my roguelikes,{w=0.1} to be honest."
        n "Heh.{w=0.2} Are you surprised,{w=0.1} [player]?"
        n "Tough as nails,{w=0.1} and I gotta think on my feet{w=0.1} -{w=0.1} plus it's super satisfying learning everything too."
        n "And with how random everything is,{w=0.1} they always feel refreshing and fun to play!"
        n "Every time I load it up,{w=0.1} I have no idea what I'm up against...{w=0.3} I love it!"
        n "Ehehe.{w=0.2} Don't worry though, [player]."
        n "I don't know if you're into that kind of stuff as well,{w=0.1} but..."

        if persistent.jn_player_gaming_frequency == "High":
            n "There's still plenty I can teach you!"

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "I'd love to help you learn,{w=0.1} [player]."
                n "And I think you'd like that too -{w=0.1} am I right?"
                n "Ehehe."

            elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "And I'd be happy to oblige~."

        elif persistent.jn_player_gaming_frequency == "Medium":
            n "I don't mind showing you how it's done."
            n "I'm a professional,{w=0.1} after all!"

        else:
            n "I don't think I'll have much trouble convincing you."
            n "Ehehe."

    else:
        n "I suppose I look for challenge in my games more than anything."
        n "It's fun pitting myself against the developers and beating them at their own game."
        n "I guess I could say I like being tested -{w=0.1} so long as I'm in control of it,{w=0.1} that is."
        n "...That being said,{w=0.1} [player]."
        n "I don't really like the kind of testing you're doing."

# Natsuki talks about her trademark fang, and checks the player is keeping their own teeth healthy
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_fang",
            unlocked=True,
            prompt="[n_name]'s fang",
            category=["Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_fang:
    n "..."
    n "Eh?{w=0.2} What's up,{w=0.1} [player]?"
    n "..."
    n "What?{w=0.2} Is there something on my face?"
    n "..."
    n "Oh.{w=0.2} Yeah.{w=0.2} I get it."
    n "Just can't help but notice the fang,{w=0.1} right?{w=0.2} Ehehe."
    n "You know..."
    n "I wasn't always happy with my teeth,{w=0.1} [player]."
    n "I used to be pretty self conscious about them.{w=0.2} People would just keep pointing them out all the time."
    n "It wasn't {i}bad{/i} or anything...{w=0.3} a little annoying at first,{w=0.1} but nothing over the top."
    n "I...{w=0.3} guess I just came to embrace them?"
    n "They're like a trademark or something now!{w=0.2} Which is why I take good care of them."
    n "You better not be slacking off on yours,{w=0.1} [player]!"
    n "And I don't just mean skipping the odd brush,{w=0.1} either..."
    n "Yeah.{w=0.2} We both know what's coming,{w=0.2} don't we?"
    n "When's the last time {i}you{/i} flossed,{w=0.1} [player]?{w=0.2} Be honest."
    n "..."
    n "Ahaha!{w=0.2} Did I call you out?"
    n "Well,{w=0.1} whatever.{w=0.2} I'm just gonna assume you'll go do that later."
    n "Seriously though.{w=0.2} You better make sure you take care of your teeth!"
    n "Regular brushing and flossing is important,{w=0.1} but watch your diet too."
    n "Not flossing isn't great,{w=0.1} but constant sugary drinks are even worse!"
    n "Remember,{w=0.1} [player] -{w=0.1} if you ignore them,{w=0.1} they'll go away~."
    n "And besides..."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n "Smiles look good on you,{w=0.1} [chosen_endearment]."
        n "Let's keep them looking that way."
        n "Ehehe.{w=0.2} Love you,{w=0.1} [player]~!"
    
    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "I think smiles look good on you,{w=0.1} [player]."
        n "Let's keep them looking that way!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "The right smile can make all the difference,{w=0.1} you know.{w=0.2} Just look at mine!"
        n "Ehehe."

    else:
        n "If you don't look after them?"
        n "I'm not holding your hand at the dentist!"

    return

# Natsuki responds to the player confessing their love to her
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_i_love_you",
            unlocked=True,
            prompt="I love you, {0}!".format(n_name),
            conditional="jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED",
            category=["Natsuki", "Romance"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_i_love_you:
    # We use these a lot here, so we define them in a higher scope
    $ player_initial = player[0]
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)

    # We account for the situation where a player may have unlocked the topic, but never selected it
    # and therefore may have any affection level
    if persistent.jn_player_love_you_count == 0:

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "O-{w=0.1}o-{w=0.1}oh my gosh..."
            n "[player_initial]-{w=0.2}[player]...{w=0.3} y-{w=0.1}you...!"
            n "Nnnnnnn-!"
            n "W-{w=0.1}well it took you long enough!{w=0.2} What did you think you were doing?!"
            n "I bet you were just waiting for me to say it first!"
            n "Jeez,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
            n "But..."
            n "B-{w=0.1}but...!"
            n "Uuuuuuu-!"
            n "Oh,{w=0.1} whatever!{w=0.2} I don't care!{w=0.2} I gotta say it!{w=0.2} I gotta say it!"
            n "[player]!{w=0.2} I love you too!"
            n "I-{w=0.1}I love...{w=0.3} you too..."
            n "I...{w=0.3} I..."
            n "I love you,{w=0.1} [player]..."
            n "..."
            n "A-{w=0.1}ahaha...{w=0.3} sorry..."
            n "I...{w=0.3} think I got a little carried away..."
            n "..."
            n "J-{w=0.1}jeez!{w=0.2} Stop looking at me like that already!"
            n "W-{w=0.1}we're both on the same page now,{w=0.1} so..."
            n "Where were we?{w=0.2} Ehehe..."
            $ relationship(change="affinity+", multiplier=3)

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "[player_initial]-{w=0.2}[player]!"
            n "Y-{w=0.1}you...!"
            n "Nnnnn-!"
            n "I-{w=0.1}I know we've been seeing each other a while,{w=0.1} but this is way too sudden!"
            n "Gosh...{w=0.3} now you've gone and made it all awkward,{w=0.1} [player]."
            n "I hope you're happy."
            n "..."
            n "D-{w=0.1}don't think this means I {i}hate{/i} you or anything,{w=0.1} though..."
            n "It's just that...{w=0.3} It's just..." 
            n "Uuuuuu..."
            n "N-{w=0.1}never mind...{w=0.3} Ahaha..."
            $ relationship(change="affinity+", multiplier=2)

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "W-{w=0.1}w-{w=0.1}what?"
            n "D-{w=0.1}did you just...?"
            n "Nnnnnnnnn-!"
            n "[player_initial]-{w=0.2}[player]!"
            n "Are you trying to give me a heart attack?!{w=0.2} Jeez..."
            n "You can't just say stuff like that so suddenly,{w=0.1} [chosen_tease]..."
            n "..."
            n "I-{w=0.1}I mean..."
            n "It's not that I {i}don't{/i} like you,{w=0.1} o-{w=0.1}or anything,{w=0.1} but..."
            n "Uuuuu..."
            n "F-{w=0.1}forget it!{w=0.2} I-{w=0.1}it's nothing..."
            n "I guess..."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            n "Pffffft!"
            n "Ahaha!"
            n "You can't be serious,{w=0.1} [player]!{w=0.2} You're just messing with me!{w=0.2} Right?"
            n "R-{w=0.1}right...?{w=0.2} Ahaha..."
            n "..."
            n "J-{w=0.1}jeez!{w=0.2} Enough of this!"
            n "You really shouldn't mess around with girls like that,{w=0.1} [player]..."
            n "Y-{w=0.1}you're just lucky I've got a great sense of humour."
            n "S-{w=0.1}so it's fine...{w=0.3} this time..."
            n "Just...{w=0.3} think a little before you just blurt stuff out, alright?"
            n "[chosen_tease.capitalize()]..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "Urk-!"
            n "W-{w=0.1}what did you..."
            n "Did you just...?"
            n "A-{w=0.1}ahaha!{w=0.2} Y-{w=0.1}yeah!{w=0.2} Who wouldn't love me,{w=0.1} right?"
            n "My wit,{w=0.1} my style,{w=0.1} my killer sense of humour...{w=0.3} I've got it all.{w=0.1} Yeah..."
            n "D-{w=0.1}don't get the wrong idea or a-{w=0.1}anything, though!"
            n "I-{w=0.1}I mean,{w=0.1} I'm just glad you have some good taste."
            n "Ehehe..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET: 
            n "..."
            n "Seriously,{w=0.1} [player]?{w=0.2} You're really going to say that to me {i}now{/i}?"
            n "The first time you choose to say it...{w=0.3} and you say it {i}now{/i}?"
            n "..."
            n "...I don't even know if I can believe you,{w=0.1} [player]."
            n "And you know what?{w=0.2} That makes it so much worse."
            n "..."
            n "We're done with this."
            n "And if you {i}really{/i} feel that way?"
            n "...Then why aren't you trying to make this work,{w=0.1} [player]?"
            $ relationship("affinity-")

        else:
            # :(
            n "..."
            n "Y-{w=0.1}you..."
            n "You...{w=0.3} h-{w=0.1}how...!"
            n "H-{w=0.1}how {i}dare{/i} you tell me that now!"
            n "{i}How {w=0.3} dare {w=0.3} you.{/i}"
            n "..."
            n "You knew how I felt,{w=0.1} [player]..."
            n "You knew for such a long time..."
            n "And now?{w=0.2} {i}Now{/i} is when you tell me?"
            n "For the {i}first time{/i}?"
            n "..."
            n "I...{w=0.3} I c-{w=0.1}can't do this right now."
            n "It...{w=0.5} it hurts..."
            n "..."
            n "Get out of my sight,{w=0.1} [player]."
            n "..."
            n "Go!"
            n "{i}Just leave me alone!{/i}{nw}"
            $ relationship(change="affinity-", multiplier=10)
            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1
    
    # Standard flows
    else:
        $ persistent.jn_player_love_you_count += 1
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:

            # At this point, Natsuki is super comfortable with her player, so we can be open and vary things!
            $ random_response_index = random.randint(0, 11)
            
            if random_response_index == 0:
                n "Ehehe.{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n "You're always [chosen_descriptor] to me."
                $ relationship("affinity+")
                return

            elif random_response_index == 1:
                n "Aww,{w=0.1} you don't say?"
                n "Ahaha!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n "[chosen_endearment],{w=0.1} I love you too!"
                n "I'll always be here to stick up for you."
                $ relationship("affinity+")
                return

            elif random_response_index == 2:
                n "Aww,{w=0.1} [chosen_endearment]!{w=0.2} I love you too!"
                n "You're the best thing that's ever happened to me."
                $ relationship("affinity+")
                return

            elif random_response_index == 3:
                n "Oh?{w=0.2} Someone's all needy today,{w=0.1} huh?"
                n "Well,{w=0.1} I'd be happy to oblige!"
                n "I love you too,{w=0.1} [chosen_endearment]!"
                n "Keep on smiling for me,{w=0.1} 'kay?"
                $ relationship("affinity+")
                return

            elif random_response_index == 4:
                n "Fawning over me like always,{w=0.1} [player]?"
                n "Ehehe.{w=0.2} Don't worry,{w=0.1} I'm not complaining!"
                n "I love you too,{w=0.1} [chosen_endearment]!"
                n "It's just us two against the world!"
                $ relationship("affinity+")
                return

            elif random_response_index == 5:
                n "Well,{w=0.1} o-{w=0.1}of course you do.{w=0.2} Ahaha!"
                n "But...{w=0.3} we both know I love you more,{w=0.1} [player]."
                menu:
                    "No, I love you more.":
                        n "No,{w=0.1} I-"
                        n "..."
                        n "Hey...{w=0.3} wait a minute..."
                        n "I know where we're going with this!{w=0.2} Nice try,{w=0.1} [player]!"
                        n "You're just gonna have to accept that I love you more,{w=0.1} and that's just the way it is."
                        menu:
                            "You love me more, and that's just the way it is.":
                                n "Ehehe.{w=0.2} See?"
                                n "That wasn't so hard,{w=0.1} was it?"
                                n "I looooove you,{w=0.1} [player]~!"

                    "Okay.":
                        n "Pfffft!{w=0.2} Ahaha!"
                        n "Come on,{w=0.1} [player]!{w=0.2} Where's your fighting spirit?"
                        n "Well,{w=0.1} whatever.{w=0.2} I'm just glad you accept the truth."
                        n "Ehehe."

                $ relationship("affinity+")
                return

            elif random_response_index == 6:
                n "Ehehe...{w=0.3} I always adore hearing that from you,{w=0.1} [player]."
                n "...And I think I can guess you like hearing it just as much."
                n "I love you too,{w=0.1} [chosen_endearment]!"
                n "I don't need anyone else~."
                $ relationship("affinity+")
                return

            elif random_response_index == 7:
                n "Wow,{w=0.1} [player]..." 
                n "You really are just a big sappy mess today,{w=0.1} aren't you?"
                n "Gross..." 
                n "...But just the kind of gross I'm down with.{w=0.2} Ehehe."
                n "I love you too,{w=0.1} [chosen_endearment]!"
                n "I'll always have your back."
                $ relationship("affinity+")
                return

            elif random_response_index == 8:
                n "Ehehe."
                n "I..."
                n "Looooooooove you too,{w=0.1} [player]!"
                n "You'll always be my rock."
                $ relationship("affinity+")
                return

            elif random_response_index == 9:
                n "I mean...{w=0.3} that's real sweet of you and all,{w=0.1} [player]..."
                n "But we both know I love you more~."
                $ player_is_wrong = True
                $ wrong_response_count = 0

                # Natsuki won't lose!
                while player_is_wrong:
                    menu:
                        "No, I love {i}you{/i} more!":
                            
                            if wrong_response_count == 1:
                                n "Hmm?{w=0.2} Did you mishear me,{w=0.1} [player]?"
                                n "I said I love {i}you{/i} more,{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n "Oh?{w=0.2} Competitive,{w=0.1} are we?"
                                n "Ehehe.{w=0.2} Silly [player].{w=0.1} Did nobody ever tell you?"
                                n "Don't start a fight you can't finish!"
                                n "Especially this one -{w=0.1} I love {i}you{/i} more~!"

                            elif wrong_response_count == 10:
                                n "Oho?{w=0.2} Not bad,{w=0.1} [player]!"
                                n "I almost admire your stubbornness..."
                                n "But not as much as I admire you!{w=0.2} I love {i}you{/i} more!"

                            elif wrong_response_count == 20:
                                n "Ehehe.{w=0.2} You're persistent!{w=0.2} I'll give you that."
                                n "But if you think I'm giving you a win..."
                                n "Then you've got another thing coming!"
                                n "I love {i}you{/i} more,{w=0.1} dummy!"

                            elif wrong_response_count == 50:
                                n "Wow!{w=0.2} This is like...{w=0.3} the 50th time you've been wrong!{w=0.2} In a row!"
                                n "Sounds to me like you're in some serious denial there,{w=0.1} [player]~."
                                n "I don't think I can be bothered counting much more from here..."
                                n "So why don't you do me a favour and just accept that I love {i}you{/i} more already?"
                                n "Ehehe."
                                n "Thanks,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n "...Oh!{w=0.2} And it looks like we have our 100th wrong answer!"
                                n "Dim the lights!{w=0.2} Roll the music!"
                                n "Now,{w=0.1} audience members -{w=0.1} what does our stubborn participant get?"
                                n "They get..."
                                n "A correction!{w=0.2} Wow!"
                                n "And that correction is..."
                                n "[n_name] loves {i}them{/i} way more!{w=0.2} Congratulations,{w=0.1} dummy!"
                                n "And now,{w=0.1} to walk away with the grand prize -{w=0.1} all our guest here needs to do..."
                                n "Is give up and admit how wrong they are~!{w=0.2} Ehehe."

                            else:
                                $ player_is_wrong_responses = [
                                    "Nope!{w=0.2} I love {i}you{/i} more!",
                                    "Sorry,{w=0.1} bub!{w=0.2} I definitely love {i}you{/i} more!",
                                    "Ehehe.{w=0.2} Nope~!{w=0.2} We both know I love {i}you{/i} more.",
                                    "Hmm...{w=0.3} nah.{w=0.2} Pretty sure I love {i}you{/i} more!",
                                    "Nooooope~!{w=0.2} I love {i}you{/i} more!",
                                    "Silly [player]~.{w=0.2} I love {i}you{/i} more,{w=0.1} remember?",
                                    "Mmmmmmmm...{w=0.3} nope!{w=0.2} I love {i}you{/i} way more,{w=0.1} [player]~!",
                                    "Come come now,{w=0.1} [player].{w=0.2}  Don't be silly!{w=0.2} I definitely love {i}you{/i} more.",
                                    "Wait...{w=0.3} can you hear that?{w=0.2} Oh!{w=0.2} It's how wrong you are -{w=0.1} I love you more,{w=0.1} dummy!"
                                    "You're only wasting your time,{w=0.1} [player]~.{w=0.2} I love {i}you{/i} waaay more!",
                                    "My,{w=0.1} oh my,{w=0.1} [player].{w=0.2} Don't you know that I love {i}you{/i} more by now?{w=0.2} Ehehe.",
                                    "Uh huh...{w=0.3} Nat hears you,{w=0.1} Nat knows you're wrong.{w=0.1} I love {i}you{/i} more,{w=0.1} you goof!",
                                    "You're adorable when you're in denial,{w=0.1} [player].{w=0.2} Ehehe.{w=0.2} I love {i}you{/i} more~!",
                                    "Aww,{w=0.1} come on now,{w=0.1} [player].{w=0.2} If you {i}really{/i} loved me,{w=0.2} you'd admit I love {i}you{/i} more!"
                                ]
                                $ chosen_random_response = renpy.substitute(random.choice(player_is_wrong_responses))
                                n "[chosen_random_response]"

                            $ wrong_response_count += 1

                        "Okay, fine. You love me more.":
                            $ player_is_wrong = False
                            n "See?{w=0.2} Was that really so hard?"
                            n "Sometimes you just have to admit you're wrong,{w=0.1} [player]."
                            n "Ehehe."

                            if wrong_response_count >= 10:
                                n "Nice try,{w=0.1} though~!"

                            $ relationship("affinity+")
                            return

            elif random_response_index == 10:
                n "Ehehe.{w=0.2} I'll never get tired of hearing that from you,{w=0.1} [player]."
                n "I love you too!"
                n "You're my numero uno~."
                $ relationship("affinity+")
                return

            else:
                n "Oh?{w=0.2} Lovey-dovey as usual?"
                n "You're such a softie,{w=0.1} [player].{w=0.2} Ehehe."
                n "But...{w=0.3} I'm not gonna complain!{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n "You always make me feel tall."
                $ relationship("affinity+")
                return

            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "G-{w=0.1}gah!{w=0.2} [player]!"
            n "What did I say about making things awkward?{w=0.2} Now it's twice as awkward!"
            n "Jeez..."
            n "Let's just talk about something,{w=0.1} alright?"
            n "Y-{w=0.1}you can fawn over me in your {i}own{/i} time!"
            n "Dummy..."
            $ relationship("affinity+")
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            n "H-{w=0.1}hey! I thought I told you not to just come out with stuff like that!"
            n "Jeez,{w=0.1} [player]..."
            n "I-{w=0.1}I don't know if you're trying to win me over,{w=0.1} or what..."
            n "But you're gonna have to try harder than that!{w=0.2} Ehehe..."
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "G-{w=0.1}gah!"
            n "[player_initial]-{w=0.1}[player]!"
            n "Stop being gross!{w=0.2} Gosh..."
            n "..."
            n "I don't know if you think this is a joke,{w=0.1} or what..."
            n "But it really isn't funny to me,{w=0.1} [player]."
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            n "..."
            n "Talk is cheap,{w=0.1} [player]."
            n "If you {i}really{/i} care about me like that..."
            n "Then {i}prove{/i} it."
            $ relationship("affinity-")
            return

        else:
            n "..."
            n "You're actually unbelievable,{w=0.1} [player]."
            n "Do you even understand what you're saying?"
            n "..."
            n "You know what?{w=0.2} Whatever.{w=0.2} I don't care anymore."
            n "Say what you like,{w=0.1} [player].{w=0.2} It changes nothing."
            $ relationship("affinity-")
            return

    return

# Natsuki discusses her trademark hairstyle with the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_hairstyle",
            unlocked=True,
            prompt="Why do you style your hair like that?",
            category=["Fashion"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_hairstyle:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "Hmm?{w=0.2} My hairstyle?"
        n "Why do you ask,{w=0.1} [player]?{w=0.2} Looking for a stylist?"
        n "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Huh?{w=0.2} My hairstyle?"
        n "Wait...{w=0.3} are you messing with me?{w=0.2} What do you mean?"
        n "You better not be teasing me,{w=0.1} [player]..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...Huh?{w=0.2} Oh.{w=0.2} My hair."
        n "I'm...{w=0.3} surprised you care enough to ask about that."

    else:
        n "Because I like it that way.{w=0.2} Is that good enough for you?"
        n "Why would you even care anyway?{w=0.2} You haven't cared about me so far."
        n "Jerk."
        return

    n "Well,{w=0.1} anyway."
    n "I never really thought about it that much,{w=0.1} honestly."
    
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "I just thought twintails would look cute on me..."
        n "...Yeah,{w=0.1} yeah.{w=0.2} I know what you're thinking,{w=0.1} [player]."

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Was I wrong...?"
            n "Ehehe.{w=0.2} I thought not."

    else:
        n "I guess I just liked the idea of twintails."

    n "As for the bangs,{w=0.1} I...{w=0.3} always found it difficult to get my hair cut."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "It just costs so much,{w=0.1} you know?{w=0.2} It's super dumb!"
        n "Like...{w=0.3} I don't get it at all!"
        n "And the annoying thing is that if I were a guy,{w=0.1} it'd be way cheaper!{w=0.2} What's up with that?"
        n "Ugh...{w=0.3} anyway."

    else:
        n "I was always kinda short when it came to getting it cut."
        n "...And no,{w=0.1} {i}not{/i} in the physical sense."

    n "As for my hairclip?{w=0.2} It's just to keep my hair out of my eyes."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Looking good is a bonus,{w=0.1} but I mostly just got tired of brushing my hair out of my face."
        n "Especially with bangs this long!"
        n "Anyway..."

    n "Have I thought about other hairstyles?{w=0.2} Well..."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n "I'm pretty sure I already let my hair down around you,{w=0.1} [chosen_tease].{w=0.2} That qualifies, right?"
        n "Ahaha!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "You know what they say,{w=0.1} [player]."
        n "If it ain't broke,{w=0.1} don't fix it!"
        n "Ehehe."

    else:
        n "...At this point,{w=0.1} [player]?{w=0.2} I'd rather you stayed {i}out{/i} of my hair."
        n "Thanks."

# Natsuki provides guidance on how to stay true to yourself and your values
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_integrity",
            unlocked=True,
            prompt="Having integrity",
            category=["Society", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_integrity:
    n "You know,{w=0.1} [player]..."
    n "I feel like nowadays,{w=0.1} everyone is trying to make a point,{w=0.1} or preach something."
    n "Especially with social media and all that everywhere -{w=0.1} it's crazy!"
    n "Like...{w=0.3} there's posts telling you this is bad,{w=0.1} others asking why you don't support something else..."
    n "And of course,{w=0.1} {i}everyone{/i} is tuned in to that -{w=0.1} so it leaks into real life as well!"
    n "Ugh...{w=0.3} it can't only be me that finds it all exhausting,{w=0.1} right?"
    n "I think it makes it kinda easy to lose track of what you really like,{w=0.1} or what you stand for."
    n "Which...{w=0.3} is actually something I really wanted to talk to you about,{w=0.1} [player]."
    n "I'm not saying you should just ignore everyone else,{w=0.1} or never consider other points of view."
    n "That's just being ignorant."
    n "But...{w=0.3} don't just let other people's opinions or conceptions completely overwrite your own,{w=0.1} 'kay?"
    n "At least not without a fight,{w=0.1} at least."
    n "You are your own master,{w=0.1} [player] -{w=0.1} you have your own opinions,{w=0.1} your own values:{w=0.1} and that's super important!"
    n "I mean,{w=0.1} look at me!"
    n "So what if someone says what I'm into sucks?{w=0.2} Or if I should be following something more popular?"
    n "It isn't hurting anyone,{w=0.1} so who are they to judge and tell me what I should be enjoying?"
    n "It's my life,{w=0.1} so they can jog on!"
    n "Anyway...{w=0.3} I guess what I'm saying is don't be afraid to stand up for what matters to you,{w=0.1} [player]."
    n "There's gonna be times you'll be wrong,{w=0.1} but don't let it get to you!"
    n "I just don't like the idea of people being pushed into what isn't right for them."
    n "That being said,{w=0.1} [player]..."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "I'm pretty sure we both know what's right for each other by now,{w=0.1} huh?"
        n "O-{w=0.1}or should I say,{w=0.1} {i}who{/i} is right...?"
        n "Ehehe."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "Love you,{w=0.1} [player]~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "I'm pretty sure I know what's right for you..."
        n "Spending more time with me!{w=0.2} Ahaha."

    else:
        n "I'm sure I can help you find what's right for you."
        n "That's what friends are for,{w=0.1} right?"
        n "Especially ones like me!{w=0.2} Ehehe."
    
    return

# Natsuki discusses her favourite animal
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_animal",
            unlocked=True,
            prompt="What's your favourite animal?",
            category=["Animals", "Nature"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_animal:
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Hammies."
        n "That's barely even a question for me,{w=0.1} [player].{w=0.2} Ehehe."
        n "Like...{w=0.3} if you've seen them,{w=0.1} can you blame me?{w=0.2} They're totally adorable!"
        n "I just love everything about them...{w=0.3} the little paws,{w=0.1} the bright eyes, those puffy cheeks..."
        n "And that tiny litte tail...{w=0.3} oh my gosh!{w=0.2} It's just precious!"
        n "It really winds me up when people call them boring,{w=0.1} or unaffectionate though.{w=0.2} Like...{w=0.3} have you ever watched one?"
        n "They all have their own little personalities,{w=0.1} just like any other animal -{w=0.1} only smaller!"
        n "And if you bond with them,{w=0.1} they aren't afraid to show it -{w=0.1} I've seen videos of them following their owners around,{w=0.1} and even leaping into their hands!"
        n "Plus they're easy to take care of,{w=0.1} too!" 
        n "Just top up their food and change their water daily,{w=0.1} and clean their cage out once a week -{w=0.1} no sweat."
        n "Hmm..."
        n "You know,{w=0.1} [player]...{w=0.3} it does get a little quiet when you aren't around,{w=0.1} if you know what I'm getting at..."
        n "Perhaps one day we could have our own furry friend here too?{w=0.1} Ehehe."
        n "Don't worry though,{w=0.1} [player]..."
        n "I don't mind taking care of it."
        n "...But you're in charge of the supplies!"

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Oh,{w=0.1} and relax -{w=0.1} I'll make sure it'll be well tamed!"
            n "Or..."
            n "At least about as tame as you,{w=0.1} huh [player]?{w=0.2} Ahaha!"

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n "Love you~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Hamsters,{w=0.1} if it matters."
        n "Why?{w=0.2} I don't know.{w=0.2} I just think they're cute."
        n "I think people actually underestimate how expressive they can be,{w=0.1} too."
        n "They're like most animals really -{w=0.1} they all have their own personalities."
        n "I guess they're pretty easy to take care of as well,{w=0.1} so there's that."
        n "..."
        n "...I'd be lying if I said I hadn't been thinking about getting one myself..."
        n "But honestly,{w=0.1} [player]?{w=0.2} If you've shown you can't take care of {i}me{/i}?"
        n "...Then I don't think it'd be fair to bring one here,{w=0.1} either.{w=0.2} Heh."

    else:
        n "Heh.{w=0.2} Really?{w=0.2} My favourite animal...?"
        n "Not you,{w=0.1} [player].{w=0.2} That's for sure."
    
    return

# Natsuki discusses her favourite drink
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_drink",
            unlocked=True,
            prompt="What's your favourite drink?",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_drink:
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Ooooh!{w=0.2} My favourite drink?"
        
    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Mmm?{w=0.2} My favourite drink?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Huh?{w=0.2} Oh.{w=0.1} My favourite drink."

    else:
        n "...I can't understand why you'd care,{w=0.1} [player]."
        n "So...{w=0.3} why should I?"
        n "Water.{w=0.2} There's an answer for you.{w=0.2} Happy?"
        n "Now just go away..."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "I gotta say...{w=0.3} it depends on the weather more than anything."
        n "I mean...{w=0.3} what kind of person would order an iced drink in the middle of winter?!"
        n "But anyway..."
        n "If it's cold out,{w=0.1} then hot chocolate.{w=0.2} No questions,{w=0.1} no doubts."
        n "In the depths of winter,{w=0.1} you definitely won't get a better option than that!"

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "And yeah,{w=0.1} [player] -{w=0.1} whipped cream,{w=0.1} marshmallows -{w=0.1} all of it.{w=0.2} The complete works."
            n "...And I wouldn't accept anything less!"
            n "I mean,{w=0.1} think about it -{w=0.1} if you're getting hot chocolate,{w=0.1} you've already kinda lost on the health front."
            n "So you might as well go all in,{w=0.1} right?{w=0.2} Ahaha."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n "Besides,{w=0.2} I'm not too worried -{w=0.1} we can always share the calories,{w=0.1} [player]~."

        n "As for warmer weather...{w=0.3} that's a little trickier,{w=0.1} actually."
        n "Let me think..."
        n "..."
        n "Aha!{w=0.2} I got it!"
        n "It's gotta be those milkshakes,{w=0.1} but from one of those places where you get to choose what goes in it!"
        n "I don't just mean picking a flavour,{w=0.1} [player]..."
        n "I mean where you can pick any combination of ingredients you want!"
        n "Well...{w=0.3} as long as it blends,{w=0.1} anyway."
        n "All kinds of sweets,{w=0.1} any type of milk..."

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "Though if I had to pick a favourite?"
            n "It's gotta be strawberries and cream,{w=0.1} obviously."
            n "And...{w=0.3} maybe with just a dash of chocolate too?{w=0.2} Ehehe."
        
        else:
            n "Yeah.{w=0.2} That's the real deal!"

        n "Jeez...{w=0.3} all this talk about drinks is making me kinda thirsty,{w=0.1} actually.{w=0.2} So on that note..."
        n "Make sure you stay hydrated too,{w=0.1} [player] -{w=0.1} whatever the weather!"

    else:
        n "I suppose it depends what the weather is like."
        n "Hot chocolate if it's cold out,{w=0.1} though I'm not very picky I guess."
        n "As for warmer weather..."
        n "I don't really know.{w=0.2} Whatever is fine."
        n "Heh.{w=0.2} Though at this rate,{w=0.1} I shouldn't expect much more than tap water from you anyway.{w=0.2} Right,{w=0.1} [player]?"

# Natsuki complains about her school uniform
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_school_uniform",
            unlocked=True,
            prompt="What do you think of your school uniform?",
            category=["Fashion"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_school_uniform:
    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "Oho?{w=0.2} Does [player] like a girl in uniform?"
        n "Wow...{w=0.3} you're even {i}more{/i} gross than I thought."
        n "..."
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n "Oh come on,{w=0.1} [chosen_tease]!{w=0.2} You always get all sulky when I call you that!{w=0.2} I just can't resist."
        n "Ehehe.{w=0.2} So anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Huh?{w=0.2} My school uniform?"
        n "...Ehehe."
        n "Why do you ask,{w=0.1} [player]?{w=0.2} Did {i}you{/i} wanna wear it or something?"
        n "Oh!{w=0.2} We can play dress-up!{w=0.2} Wouldn't you like that,{w=0.1} [player]?{w=0.2} It'll be so much fun!"
        n "I bet I could make you look so cute~.{w=0.1} Ahaha!"
        n "Well anyway,{w=0.1} putting jokes aside..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "My school uniform?{w=0.2} That's...{w=0.3} kind of a weird thing to ask me about,{w=0.1} huh?"
        n "Well,{w=0.1} whatever.{w=0.2} I'll let it slide...{w=0.3} this time."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...Huh?{w=0.2} Oh,{w=0.1} the school uniform."
        n "I...{w=0.3} don't know what you're expecting to hear from me,{w=0.1} [player]."
        n "I gotta wear it for school.{w=0.2} That's the point of a uniform,{w=0.1} if you hadn't realized."
        n "It doesn't matter if I like it or not."
        n "...And it matters even less if you do."
        return

    else:
        n "Heh.{w=0.2} I like it more than {i}you{/i}.{w=0.2} Jerk."
        return

    n "It's alright,{w=0.1} I guess.{w=0.2} I actually really like the warm colours!"
    n "They're way easier on the eyes than a lot of the other uniforms I've seen around."
    n "But Oh.{w=0.2} My.{w=0.2} Gosh.{w=0.2} [player]."
    n "The layers.{w=0.2} So many layers."
    n "Who even thought someone needs this much clothing?!{w=0.2} For school,{w=0.1} of all places?!"
    n "I mean...{w=0.3} do you even {i}know{/i} what wearing all of this in summer is like?!{w=0.2} It's horrible!"
    n "And the blazer...{w=0.3} ugh!{w=0.2} It's actually the worst thing ever."
    n "Like yeah,{w=0.1} I can take some off between class,{w=0.1} but I gotta put it all back on when I go back in."
    n "...Or get told off.{w=0.2} {i}Again{/i}.{w=0.2} I honestly have no idea how Sayori gets away with hers being so scruffy."
    n "And all of this stuff is super expensive too!{w=0.2} Talk about a kick in the teeth!{w=0.2} Jerks."
    n "Ugh...{w=0.3} I seriously can't wait until I can wear whatever I like for what I'm doing."
    n "It could be worse though,{w=0.1} I guess.{w=0.2} At least I never had to learn how to do a tie!"
    n "What about you though, [player]?"
    menu:
        n "Did you have to wear uniform at school?"

        "Yes, I had to wear uniform.":
            n "Aha!{w=0.2} So you know the struggle too,{w=0.1} huh?"

        "No, I didn't have to wear uniform.":
            n "..."
            n "...Lucky."

        "I have to wear uniform now.":
            n "Then you have my condolences,{w=0.1} [player]!{w=0.2} Ahaha."
            n "Good to know we're on the same page,{w=0.1} though."

    n "Well,{w=0.1} anyway..."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "I still don't particularly {i}like{/i} wearing it..."
        n "But I think I can put up with it.{w=0.2} Just for you,{w=0.1} [player]~."
        n "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "I-{w=0.1}if you like it, [player]?"
        n "I suppose it has that going for it too,{w=0.1} right?{w=0.2} Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "I guess at least I'm warm and toasty for the winter,{w=0.1} right?{w=0.2} Ahaha."

    return

# Natsuki laments how she's never travelled abroad by plane
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_flying",
            unlocked=True,
            prompt="Have you ever flown anywhere?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_flying:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "Ooh!{w=0.2} Flying?{w=0.2} Like on a plane?"
        n "Mmm...{w=0.3} I wish I could say I have,{w=0.1} [player]..."
        n "Don't get me wrong though!{w=0.2} I'd {i}totally{/i} fly somewhere new if I could!"
        n "It's just...{w=0.3} the price of it all,{w=0.1} you know?"
        n "I've never had a passport,{w=0.1} but it's mainly the tickets and everything beyond that..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "Huh?{w=0.2} Flying?{w=0.2} Like on a plane or something?"
        n "I...{w=0.3} wish I could say I have,{w=0.1} [player]."
        n "Don't get me wrong though!{w=0.2} I'd love to jet off somewhere.{w=0.2} Like for a vacation or something!"
        n "It's just the cost that stops me, you know?"
        n "Even if I had a passport, there's just so many things to pay out for..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Oh?{w=0.2} Like flying on a plane or whatever?"
        n "Uhmm..." 
        n "I...{w=0.3} never really had the opportunity to fly anywhere,{w=0.1} [player]."
        n "I don't even have a passport or anything like that,{w=0.1} and even if I did?"
        n "It isn't like tickets are...{w=0.3} affordable,{w=0.1} if you know what I mean?"
        n "Especially to someone in my...{w=0.3} position.{w=0.2} Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Flying?{w=0.2} Like...{w=0.3} on a plane?"
        n "No,{w=0.1} [player].{w=0.2} I haven't."
        n "I've never owned a passport,{w=0.1} and it's way too expensive anyway."
        n "I don't really like the idea of the environmental impact either."
        n "...But something tells me you don't really care about that last point,{w=0.2} do you?"
        n "You know...{w=0.3} just going by my experience so far."
        n "...Am I wrong?"
        return

    else:
        n "No,{w=0.1} [player].{w=0.2} I haven't.{w=0.2} And I probably never will."
        n "Gloat all you want.{w=0.2} I don't give a crap if you have."
        return

    n "Besides,{w=0.1} I try not to feel too bad about it.{w=0.2} It's way better for the environment if I don't,{w=0.1} anyway!"
    n "Flying places is pretty polluting.{w=0.2} I think I'd just feel selfish if I was constantly zooming around,{w=0.1} knowing how bad that is for everyone."
    n "But...{w=0.3} that's just me,{w=0.1} I guess.{w=0.2} What about you,{w=0.1} [player]?"
    menu:
        n "Are you a frequent flier?"

        "Yes, I fly regularly.":
            n "Oh?{w=0.2} Well check you out,{w=0.1} [player]!"
            n "I guess it's {i}plane{/i} to see how well you're doing for yourself?{w=0.2} Ehehe."
            n "Just...{w=0.3} try to avoid racking up too many miles,{w=0.1} alright?"
            n "We all gotta do our part for the world,{w=0.1} after all..."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "E-especially if people we really care about are in it. Ehehe..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
                n "Even you, [player]! Ehehe."

        "I fly sometimes.":
            n "Ooh,{w=0.1} okay!{w=0.2} So the odd vacation or family flight then?"
            n "I see,{w=0.1} I see..."
            n "Well,{w=0.1} good for you, [player]! Everyone should get the chance to explore the world."
            n "Hopefully I'll get the chance someday too."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "I hope you'll be available when that happens,{w=0.1} [player]."
                n "I'm gonna need a tour guide,{w=0.1} after all.{w=0.2} Ehehe..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
                n "You better be handy when that happens,{w=0.1} [player]..."
                n "I bet you'd got tons of advice you can share,{w=0.1} right?{w=0.2} Ahaha."

        "I've flown before.":
            n "Ooh!{w=0.2} So you've already earned your wings,{w=0.1} huh?"
            n "Hmm...{w=0.3} I wonder where you went?"
            n "You gotta promise to tell me if you fly again,{w=0.1} 'kay?"
            n "I wanna hear all about it!"

        "I've never flown.":
            n "Then that's just another thing we have in common,{w=0.1} [player]!"
            n "I guess you could say..."
            n "We're both just {i}well grounded{/i} people,{w=0.1} huh?"
            n "Ahaha!"

    return

# Natsuki laments how she's never travelled abroad by plane
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cars",
            unlocked=True,
            prompt="Are you into cars?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cars:
    $ already_discussed_driving = False

    # Check to see if the player and Natsuki have already discussed if Nat can drive in this topic, or the "can you drive" topic
    if get_topic("talk_driving"):
        $ already_discussed_driving = get_topic("talk_driving").shown_count > 0

    elif get_topic("talk_are_you_into_cars"):
        $ already_discussed_driving = get_topic("talk_are_you_into_cars").shown_count > 0

    if already_discussed_driving:
        # Natsuki has already established she can't drive at some point
        if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "Eh?{w=0.2} Cars?" 
            n "You know I can't drive,{w=0.1} dummy!{w=0.2} I don't really think I have much of a reason to be into cars!"
            n "Well,{w=0.1} anyway..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "[player].{w=0.2} You know I can't drive.{w=0.2} Why would you think I'd be into cars,{w=0.1} of all things?"
            n "...Fine.{w=0.2} Whatever."

        else:
            n "...Really?"
            n "You know I can't drive.{w=0.2} So I'm not even going to {i}pretend{/i} I care if you're into that,{w=0.1} [player]."
            n "Besides...{w=0.3} I bet you'd {i}never{/i} treat your dream car like you treat me,{w=0.1} would you?"
            return

    else:
        # Natsuki hasn't stated she can't drive before
        if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "Huh?{w=0.1} Am I into cars?"
            n "Well...{w=0.3} to tell you the truth,{w=0.1} [player]?"
            n "...I've never actually owned a license.{w=0.2} I don't even think I could afford to learn!"
            n "So I've never really been drawn to them honestly."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "I can't drive,{w=0.1} [player].{w=0.2} I don't have a license either;{w=0.1} learning was always too expensive."
            n "So...{w=0.3} why would I be into that?{w=0.1} I literally can't {i}afford{/i} to be."

        else:
            n "Newsflash,{w=0.1} jerk.{w=0.2} I {i}can't{/i} drive,{w=0.1} and I can't even afford to {i}learn{/i}."
            n "So you tell {i}me{/i} -{w=0.1} why would I be into cars?{w=0.2} And if I was,{w=0.1} why the hell would I want to talk to {i}you{/i} about them?"
            n "...Heh.{w=0.2} Yeah,{w=0.1} I thought so.{w=0.2} We're done here,{w=0.1} [player]."
            return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "I can appreciate the talent that goes into them -{w=0.1} I think it's actually pretty cool how expressive they can be!"
        n "Like...{w=0.3} the design languages of all the different brands,{w=0.1} the engineering that goes into them and all that."
        n "It's pretty insane how much work goes into it;{w=0.1} and that's definitely something I have respect for!"
        n "What about your side of the story, [player]?{w=0.2} You {i}did{/i} bring it up,{w=0.1} but I thought I'd ask anyway..."
        menu:
            n "Are you into cars?"

            "Yes! I'm into my cars.":

                # The player has never stated if they can drive
                if persistent.jn_player_can_drive is None:
                    n "Huh.{w=0.2} I wasn't actually sure if you could even drive,{w=0.1} but I guess it doesn't matter really."
                    n "I guess being a petrolhead isn't an exclusive club,{w=0.1} huh?" 
                    n "Ehehe."

                # The player has confirmed they can drive
                elif persistent.jn_player_can_drive:
                    n "Well,{w=0.1} color {i}me{/i} surprised."
                    n "Ehehe."
                    n "Don't worry,{w=0.1} I had you figured for the sort,{w=0.2} [player]."
                    n "But hey -{w=0.1} whatever floats your boat!"

                # The player has admitted they cannot drive
                else:
                    n "That's...{w=0.3} actually pretty surprising to hear from you,{w=0.1} [player]."
                    n "You know,{w=0.1} since you said you can't drive and all that..."
                    n "But I guess it's like anything -{w=0.1} you don't have to be doing it to be a fan,{w=0.1} and that's fine with me!"

            "I don't care much for them.":
                n "I guess that's fair enough -{w=0.1} and don't worry,{w=0.1} I completely get it."
                n "But if someone's into that kind of thing,{w=0.1} who am we to judge,{w=0.1} after all?"
                n "Ahaha."

            "No, I'm not into them.":
                n "...Huh.{w=0.2} That's kinda weird -{w=0.1} then why did you bring it up,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n "Especially if you can drive!"
                    n "Huh..."

                n "Well,{w=0.1} anyway.{w=0.2} Fair enough I guess!"

    else:
        n "I guess I can respect the work and talent that goes into designing and making one..."
        n "But it's just the same as anything else."
        n "I suppose you're into your cars then,{w=0.1} are you?"
        n "Heh.{w=0.2} It'd be nice if you extended that respect to {i}people{/i} too,{w=0.1} [player]."
        n "Just saying."

    return

# Natsuki comments on how she feels about the player, based on affinity
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_do_you_feel_about_me",
            unlocked=True,
            prompt="How do you feel about me?",
            category=["Natsuki", "Romance", "You"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_do_you_feel_about_me:
    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:

        if persistent.jn_player_love_you_count > 0:
            n "[player]...{w=0.3} isn't it obvious? You know I love you already,{w=0.1} right?"
            n "Jeez...{w=0.3} you really are a dork sometimes,{w=0.1} you know."
            n "But...{w=0.3} I really like that silly part of you,{w=0.1} [player]."
            n "Never change,{w=0.1} 'kay? Ehehe."
            n "Love you,{w=0.1} [player]~!"

        else:
            n "Nnnnnnn-!"
            n "C-{w=0.1}come on! Isn't it obvious by now? Jeez...{w=0.3}"
            n "Do I really have to spell it out for you,{w=0.1} [player]?"
            n "Ugh...{w=0.3}"
            n "Heh.{w=0.2} Actually,{w=0.1} you know what?"
            n "I'll let you figure it out."
            n "And no,{w=0.1} before you ask -{w=0.1} you've had enough hints already."
            n "Ehehe...{w=0.3}"

        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "Uuuuuu-!"
        n "A-{w=0.1}are you trying to put me on the spot or something,{w=0.1} [player]?"
        n "Jeez...{w=0.3}"
        n "You should really know how I feel about you by now,{w=0.1} you know...{w=0.3}"
        n "...{w=0.3}"
        n "...{w=0.3}Fine.{w=0.2} I...{w=0.3} really...{w=0.3} like you,{w=0.1} [player]."
        n "I-{w=0.1}is that enough for you? Ahaha...{w=0.3}"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "H-{w=0.1}huh? How do I feel about you?"
        n "W-{w=0.1}what're you worrying about that for,{w=0.1} you dummy?!"
        n "You're a-{w=0.1}okay in my books,{w=0.1} [player]...{w=0.3} so just take it easy!"
        n "Jeez...{w=0.3} you'll make things all awkward at this rate."
        n "Ahaha...{w=0.3}"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "Huh? Well,{w=0.1} I mean...{w=0.3}"
        n "You're pretty fun to be with,{w=0.1} all things considered!"
        n "I guess...{w=0.3} keep up the good work?"
        n "Ehehe...{w=0.3}"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "H-{w=0.1}huh? How do I feel about...{w=0.3} you?"
        n "I-{w=0.1}I mean,{w=0.1} you're alright...{w=0.3} I guess?"
        n "Ahaha...{w=0.3}"
        n "...{w=0.3}"
        n "W-{w=0.1}what?! It's the truth,{w=0.1} so...{w=0.3} yeah."
        n "...{w=0.3}"
        n "Let's just get back to it already!"
        n "Jeez...{w=0.3}"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        n "...{w=0.3}Oh? That matters to you now,{w=0.1} does it?"
        n "Then tell me,{w=0.1} [player]."
        n "Why did you keep hurting my feelings like that?"
        n "...{w=0.3}"
        n "I don't have much patience for jerks,{w=0.1} [player].{w=0.2} You're better than this."
        n "I don't know if you're trying to be funny or what,{w=0.1} but knock it off."
        n "I'd appreciate it.{w=0.2} Thanks."
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...{w=0.3}Let's just cut the crap."
        n "You've hurt me,{w=0.1} [player].{w=0.2} You've hurt me again,{w=0.1} and again."
        n "You've done it so many times now."
        n "So you tell me."
        n "What the hell would {i}you{/i} think of someone who did that to you?"
        n "...{w=0.3}"
        n "You're on thin ice,{w=0.1} [player]."
        n "That's all I'm gonna say...{w=0.3}"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.BROKEN:
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n "...Wow. Really?"

        else:
            n "...{w=0.3}I have no words for how I feel about {i}you{/i}."
            n "Don't even bother asking twice."

        return
        
    else:
        n "...{w=0.3}...{w=0.3}"
        n "...{w=0.3}...{w=0.3}"
        return
        
    return

# Natsuki pitches her thoughts on cosplaying
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cosplay",
            unlocked=True,
            prompt="Are you into cosplay?",
            category=["Fashion", "Media", "Society"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cosplay:

    # Check to see if Natsuki has already revealed she can sew/seamstress in this/previous topic(s)
    $ already_mentioned_sewing = get_topic("talk_sustainable_fashion").shown_count > 0 or get_topic("talk_are_you_into_cosplay").shown_count > 0

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "Ooh!{w=0.2} Cosplay,{w=0.1} you say?"
        n "Honestly,{w=0.1} I've never really done any cosplaying or anything..."
        n "But I've actually thought about it a lot since I got into manga and all that stuff more!"
        n "Plus I mean,{w=0.1} why shouldn't I?{w=0.2} There isn't a whole lot stopping me."

        if already_mentioned_sewing:
            n "Like I think I mentioned before -{w=0.1} I'm already pretty handy with a needle and thread,{w=0.1} if I say so myself!"

        else:
            n "I'm actually pretty handy with the old needle and thread,{w=0.1} you know!"

        n "And materials aren't really that expensive either -{w=0.1} besides props and wigs,{w=0.1} anyway."
        n "So it seems like a pretty awesome way to show my appreciation for characters I like and show my {i}limitless{/i} talent while I'm at it."
        n "Ahaha!"
        n "And who knows?"
        n "Maybe you'll get to see some of my handiwork some day,{w=0.1} [player]."
        n "I bet you'd like that,{w=0.1} huh?{w=0.2} Ehehe."
        n "No need to be shy,{w=0.1} [player] -{w=0.1} I can read you like a book."
        n "A gross book,{w=0.1} but a book nonetheless~."
        n "Ahaha!"
        return

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "Love you,{w=0.1} [player]~!"
            return

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "...Why did I get the feeling you'd bring this up sooner or later,{w=0.1} [player]?"
        n "What?{w=0.2} Did you think I'd {i}automatically{/i} be into it because I read manga from time to time?"
        n "Huh?{w=0.2} Is that it?"
        n "Well?"
        n "Speak up,{w=0.1} [player]!{w=0.2} I can't hear you~!"
        n "..."
        n "Ahaha!{w=0.2} Nah,{w=0.1} it's fine."
        n "I've thought about it a bunch,{w=0.1} honestly -{w=0.1} like since I got into manga and all that a while ago."
        n "I haven't {i}actually{/i} gone and dressed up yet,{w=0.1} though."
        n "But there really isn't much stopping me,{w=0.1} [player]."

        if already_mentioned_sewing:
            n "Like I said -{w=0.1} I already fix up and make my own normal clothes,{w=0.1} so a costume isn't much of a leap."

        else:
            n "You could say I'm something of a pro with a needle and thread,{w=0.1} so it's right up my alley!"

        n "Besides,{w=0.1} I've done the math on materials -{w=0.1} it's actually pretty affordable,{w=0.1} so that's all good."
        n "Well,{w=0.1} besides wigs and props and stuff.{w=0.2} Those can be kinda pricey,{w=0.1} but not exactly unaffordable -{w=0.1} just gotta shop around!"
        n "That being said...{w=0.3} hmm..."
        n "You know what,{w=0.1} [player]?"
        n "Perhaps I might just give it a shot...{w=0.3} yeah!"
        n "Man,{w=0.1} I've got so many awesome ideas buzzing around in my head now!"
        n "Oh -{w=0.1} don't worry -{w=0.1} you'll get your chance to see them too.{w=0.2} I'll need a second opinion after all."
        n "That's what friends are for,{w=0.1} right?{w=0.2} Ehehe."

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "Besides,{w=0.1} [player].{w=0.2} You seem to have pretty good taste."
            n "I think I can trust your judgement.{w=0.2} Ahaha."

        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Cosplay,{w=0.1} huh?"
        n "Well...{w=0.3} I mean,{w=0.1} I've considered it,{w=0.1} if that's what you're asking."
        n "I never really thought about it that much until I got more into manga and things like that."
        n "It kinda feels like once you start getting into that stuff,{w=0.1} you discover tons more at once!"
        n "But anyway,{w=0.1} I've never actually gone out and cosplayed myself."
        n "T-{w=0.1}that isn't to say there's anything stopping me,{w=0.1} of course!"
        
        if already_mentioned_sewing:
            n "I told you already that I'm pretty good with a needle and thread,{w=0.1} so that's a-{w=0.1}okay!"

        else:
            n "I'm basically a pro with a needle and thread,{w=0.1} so that's the hard part already mastered!"

        n "The rest of it is just shopping around for materials,{w=0.1} which are usually pretty cheap anyway."
        n "Props and wigs and all that are a little more annoying,{w=0.1} but not exactly undoable."
        n "Hmm..."
        n "The more I think about it,{w=0.1} the more I like the idea!"
        n "What about you,{w=0.1} [player]?{w=0.2} I bet you'd love to see my skills at work,{w=0.1} right?"
        n "Ahaha."
        n "Well...{w=0.3} we'll see,{w=0.1} but no promises!"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Huh?{w=0.2} Cosplay?"
        n "...Heh.{w=0.2} Why,{w=0.1} [player]?"
        n "So you can make fun of my clothes too?"
        n "..."
        n "No,{w=0.1} [player].{w=0.2} I've never cosplayed.{w=0.2} I could,{w=0.1} but I haven't."
        n "Does that answer your question?"
        return

    else:
        n "Heh.{w=0.2} Why?"
        n "So you have something else to make me feel awful about?"
        n "...Yeah.{w=0.2} No thanks."
        n "I'm done talking to you about this."
        return

    return

# Natsuki describes why she likes the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_why_do_you_like_me",
            unlocked=True,
            prompt="Why do you like me?",
            category=["Natsuki", "Romance", "You"],
            player_says=True,
            affinity_range=(jn_aff.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_why_do_you_like_me:
    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n "[player]..."
            n "You aren't asking me this because of what you told me earlier...{w=0.3} right?"
            n "..."
            n "Look,{w=0.1} [player].{w=0.2} I'm going to be completely honest with you,{w=0.1} okay?"
            n "What you can -{w=0.1} or {i}can't{/i} do -{w=0.1} isn't important to me."
            n "What people {i}say{/i} you are -{w=0.1} or {i}aren't{/i} capable of -{w=0.1} isn't important to me either."
            n "Neither is what people say about you."
            n "[player]."
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n "I...{w=0.3} feel about you the way I do because of how you've treated me,{w=0.1} [chosen_endearment].{w=0.2} Can you not see that?"
            n "You've spent so much time with me,{w=0.1} day after day..."
            n "You've listened to my problems,{w=0.1} and you've told me yours..."
            n "You've been so patient with my mood swings,{w=0.1} and my grumpy moments..."

            if persistent.jn_player_love_you_count >= 10:
                n "And...{w=0.3} you've made me feel..."
                n "So loved..."
                n "..."

            elif persistent.jn_player_love_you_count >= 1:
                n "You're...{w=0.3} you're my first love,{w=0.1} [player]..."
                n "Do you even realise how {i}much{/i} that means to me?"

            elif persistent.jn_player_love_you_count == 0:
                n "You honestly,{w=0.1} truly mean the world to me,{w=0.1} [player]..."

            n "So...{w=0.3} yeah."
            n "Does that answer your question?{w=0.2} Ehehe..."
            n "I know I can't solve your problems with a snap of my fingers,{w=0.1} [player].{w=0.2} I'm not a miracle worker."
            n "Believe me -{w=0.1} I {i}already{/i} would have if I could."
            n "But..."
            n "I hope you can believe me when I say things will work out,{w=0.1} okay?"
            n "Just...{w=0.3} keep fighting..."
            n "...Because I'm fighting for you too."
            n "I love you,{w=0.1} [player].{w=0.2} You better not forget that."
            return

        else:
            n "[player]..."
            n "Do I really need to explain this all to you?"
            n "It's just...{w=0.3} embarrassing...{w=0.3} to me..."
            n "..."
            n "...Okay,{w=0.1} look."
            n "You've...{w=0.3} honestly done more than you could ever know,{w=0.1} [player]."
            n "For me,{w=0.1} I mean."
            n "I've almost lost count of how many hours you've spent talking to me..."
            n "You've listened to so many of my dumb problems,{w=0.1} over and over..."
            n "...And you've been so patient through all of my stupid moods."

            if persistent.jn_player_love_you_count >= 10:
                n "Y-you've made me feel..."
                n "Really appreciated.{w=0.2} So many times,{w=0.1} I've lost count..."

            elif persistent.jn_player_love_you_count >= 1:
                n "You're...{w=0.3} you're my first love,{w=0.1} even!"
                n "Do you even know what that {i}means{/i} to me?"

            elif persistent.jn_player_love_you_count == 0:
                n "You seriously mean the world to me,{w=0.1} [player]..."

            n "So...{w=0.3} yeah."
            n "Does that answer all of your questions?{w=0.2} Am I free to go now?{w=0.2} Ahaha..."
            n "But seriously,{w=0.1} [player]."
            n "Don't ever doubt how important you are to me,{w=0.1} alright?"
            n "I'll get mad if you do."
            n "And trust me..."
            n "You don't want that.{w=0.2} Ehehe."
            return

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n "...Hey,{w=0.1} [player]..."
            n "This isn't by chance because of what you said earlier...{w=0.3} right?"

        else:
            n "Wh-{w=0.1}why do I-{w=0.1}...?"
            n "Uuuuuuu..."

        n "...Okay,{w=0.1} look.{w=0.2} I'll try to help you understand as best I can."
        n "I don't really care about what others expect from you."
        n "I don't really care about what others say or think about you."
        n "I don't really care if you can -{w=0.1} or can't -{w=0.1} do something."
        n "I...{w=0.3} like you,{w=0.1} because of how you've treated me,{w=0.1} you dummy!"
        n "Like,{w=0.1} come on!"
        n "You've listened to me yammer on,{w=0.1} again and again..."
        n "You've heard me out on so many dumb problems I've had..."
        n "You've even dealt with my crappy temper like a champ!"
        n "..."
        n "...I've never been treated by anyone as well as I've been treated by you,{w=0.1} [player]."
        n "So is it any wonder why I...{w=0.3} really like you this much?"
        n "..."
        n "Alright,{w=0.1} okay.{w=0.2} I really don't wanna have to explain all that again,{w=0.1} so I hope you took all that in."
        n "Just...{w=0.3} continue being you,{w=0.1} got it?" 
        n "I...{w=0.3} really couldn't ask for better.{w=0.2} Ahaha..."
        return

    else:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n "W-{w=0.1}why do I...?"
            n "..."
            n "..."
            n "Uhmm...{w=0.3} [player]?"
            n "This isn't all related to what you told me earlier,{w=0.1} right?"
            n "About feeling insecure and all that?"
            n "..."
            n "[player]."
            n "Listen up,{w=0.1} 'kay?{w=0.2} I...{w=0.3} really don't wanna have to repeat this."

        else:
            n "Urk-!"
            n "W-{w=0.1}wait,{w=0.1} w-{w=0.1}what?"
            n "W-{w=0.1}why do I...{w=0.3} l-{w=0.1}like you?!"
            n "Nnnnnnnnn-!"
            n "I mean...!{w=0.2} It's not that I {i}like{/i} like you,{w=0.1} or anything ridiculous like that!"
            n "Ugh...{w=0.3} I swear,{w=0.1} [player] -{w=0.1} you honestly try to put me in the most awkward freaking spots sometimes..."
            n "..."
            n "I...{w=0.3} guess I {i}do{/i} owe you an answer though,{w=0.1} at least."

        n "Look."
        n "You've been awesome to me so far,{w=0.1} [player]."
        n "...Do you even know how few other people make me feel that way?"
        n "It's...{w=0.3} really not a lot,{w=0.1} if you hadn't gathered."
        n "You always listen to me,{w=0.1} you don't tell me I'm annoying,{w=0.1} or to pipe down..."
        n "And you've been super understanding too."
        n "I...{w=0.3} honestly couldn't ask for a better friend,{w=0.1} [player]."
        n "Always remember that,{w=0.1} alright?{w=0.2} I'll get mad if you don't."
        n "And neither of us want that,{w=0.1} do we?"
        n "Ahaha..."

    return

# Natsuki actually likes fried squid!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fried_squid",
            unlocked=True,
            prompt="Fried squid",
            category=["DDLC", "Food"],
            nat_says=True,
            affinity_range=(jn_aff.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fried_squid:
    n "Hey,{w=0.1} [player]..."
    n "You know what I could go for right now?"
    n "A big,{w=0.1} steaming fresh bowl of Mon-{w=0.1}ika!"
    n "..."
    n "...Huh."
    n "You know,{w=0.1} in hindsight?{w=0.2} That joke really wasn't funny the first time round."
    n "I've...{w=0.3} no idea why it'd be funny this time,{w=0.1} to be honest."
    n "Oh!"
    n "But fried squid is no joke at all,{w=0.1} [player]!{w=0.2} Have you ever tried it?"
    n "It's {i}delicious{/i}!{w=0.2} I love it!"
    n "Not just boring old fried seafood though -{w=0.1} it's gotta have the crap battered out of it first!"
    n "That crispy golden coating is seriously the best.{w=0.2} Deep fried food is awesome!"
    n "It's not {i}good{/i} for you exactly,{w=0.1} but as a treat?{w=0.2} You could do way worse..."
    n "Especially with sauce to spice things up a bit!"
    n "By the way -{w=0.1} wanna know how you can tell you're dining on some top-notch squiddy goodness?"
    n "The texture,{w=0.1} of course!" 
    n "Overcooked squid becomes all rubbery and nasty,{w=0.1} and even worse -{w=0.1} it loses all of its flavour too!"
    n "Imagine biting through the batter,{w=0.1} only to find you're basically chewing on a bunch of rubber bands."
    n "Ugh!{w=0.2} Gross!{w=0.2} Talk about a disappointment."
    n "Don't let that put you off though,{w=0.1} [player] -{w=0.1} next time you see some,{w=0.1} why not give it a shot?"

    if jn_admissions.last_admission_type == TYPE_HUNGRY:
        n "...Probably the sooner the better,{w=0.1} if you're hungry like you said."
        n "But anyway..."

    n "You could even be all fancy if you wanted to and order it by the culinary name!"
    n "Ten points if you can guess what that is.{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "Hmm..."
        n "Actually...{w=0.3} you know what?"
        n "We should just get a bowl of calamari to share.{w=0.2} That's fair,{w=0.1} right?"
        n "I should warn you though,{w=0.1} [player]..."
        n "I'm not handing over the last piece without a fight!"
        n "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "But yeah -{w=0.1} you should really give it a try if you haven't already,{w=0.1} [player]!"
        n "I wouldn't want someone to miss out on that!"
        n "Especially not you.{w=0.2} Ehehe..."

    else:
        n "But yeah -{w=0.1} you should really try it out if you haven't already,{w=0.1} [player]!"
        n "I wouldn't want someone to miss out on that!{w=0.2} Ahaha."

    return

# Natsuki talks about collectibles
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_collectibles",
            unlocked=True,
            prompt="Do you have any collectibles?",
            category=["Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_collectibles:
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "Collectibles?{w=0.2} You mean like figurines and plushies and such?"
        n "Mmm...{w=0.3} not really.{w=0.2} Collecting is an expensive hobby,{w=0.1} [player]!"
        n "I mean,{w=0.1} it all depends on exactly what you collect,{w=0.1} but it feels like places that sell them prey on that."
        n "Like...{w=0.3} the urge to complete a collection -{w=0.1} so they jack up the prices!"
        n "Ugh...{w=0.3} and for people in my...{w=0.3} uhmm...{w=0.3} {i}position{/i},{w=0.1} it's a big barrier to entry."
        n "But anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Huh?{w=0.2} You mean like figurines and all that stuff?"
        n "Well...{w=0.3} no,{w=0.1} [player].{w=0.2} Not really."
        n "I couldn't justify spending so much on a hobby like that!"
        n "Especially not when I have others things to worry about spending my money on first,{w=0.1} you know."
        n "But anyway,{w=0.1} putting all that aside..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "No,{w=0.1} [player]."
        n "Collectibles are way too expensive for me.{w=0.2} I can't justify wasting the money I {i}do{/i} have."
        n "{i}Especially{/i} on stuff that'll just sit on a shelf that I'll forget about."
        n "Yeah,{w=0.1} [player] -{w=0.1} believe it or not,{w=0.1} some of us {i}do{/i} have to think about how we spend our money."
        n "Shocker,{w=0.1} right?"
        n "..."
        n "Well?{w=0.2} Satisfied with your answer?"
        n "We're done here."
        return

    else:
        n "...Why?{w=0.2} ...And I don't just mean why you care."
        n "But why should I tell {i}you{/i} if I do or not?"
        n "You'd probably just trash them."
        n "Heh.{w=0.2} After all." 
        n "You've proven great at trashing things so far,{w=0.1} {i}haven't you{/i}?{w=0.2} Jerk."
        return

    n "..."
    n "...Huh.{w=0.2} There's a point,{w=0.1} actually.{w=0.2} Does manga count as a collectible?"
    n "I'm...{w=0.3} not really sure..."
    n "What do you think,{w=0.1} [player]?"
    menu:
        n "Would you call it a collectible?"

        "I'd say so!":
            n "Oho!"
            n "So I suppose I am something of a collector,{w=0.1} after all!"

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:         
                n "I guess that all makes sense.{w=0.2} After all..."
                n "I'd like to think you're in my collection too,{w=0.1} [player]~."
                n "Ehehe."

            else:
                n "Well,{w=0.1} in that case..."
                n "Just let me know if you ever feel like a tour!"
                n "You won't find a better collection,{w=0.1} I bet.{w=0.2} Ehehe."

        "No,{w=0.1} I wouldn't.":
            n "Huh...{w=0.3} you do have a point."
            n "I suppose you'd call it a library,{w=0.1} or something like that?"
            n "Well,{w=0.1} whatever."
            n "I suppose I'd better {i}read{/i} up on my definitions,{w=0.1} right?"
            n "Ehehe."

        "Well,{w=0.1} it definitely isn't literature.":
            n "Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} ...Ha."
            n "{i}Hilarious{/i},{w=0.1} [player]."
            n "Keep it up,{w=0.1} and I'm gonna book you one."
            n "...And no,{w=0.1} I don't mean read you a story."

            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "Sheesh...{w=0.3} you're such a dummy sometimes,{w=0.1} [player]..."

    return

# Prompt Natsuki to play a game of Snap!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_snap",
            unlocked=True,
            prompt="Do you want to play Snap?",
            conditional="persistent.jn_snap_unlocked",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_snap:
    if persistent.jn_snap_player_is_cheater:
        n "[player]...{w=0.3} if you aren't even sorry you cheated,{w=0.1} why should I play with you again?"
        n "Come on...{w=0.3} it's not hard to apologize,{w=0.1} is it?"
        return

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "Of course I do,{w=0.1} dummy!{w=0.2} Ehehe."
            
        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Of course I'll play some with you,{w=0.1} dummy!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "Well,{w=0.1} duh!{w=0.2} Of course I'm up for a game!"

        else:
            n "You wanna play Snap?{w=0.2} Sure!" 
        
        n "Let me just get the cards out real quick,{w=0.1} alright?"
        play audio drawer 
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")
        jump snap_intro

# Natsuki goes over the rules of snap again, for if the player has already heard the explanation pre-game
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_snap_rules",
            unlocked=True,
            prompt="Can you go over the rules of Snap again?",
            conditional="persistent.jn_snap_unlocked and persistent.jn_snap_explanation_given",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_snap_rules:
    if persistent.jn_snap_player_is_cheater:
        n "Come on,{w=0.1} [player]."
        n "If you cared about the rules,{w=0.1} then why did you cheat when we played earlier?"
        n "You haven't even apologized for it yet..."
        return

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n "Ehehe.{w=0.2} You're so forgetful sometimes,{w=0.1} [player]."
            n "Sure,{w=0.1} I'll go over it again.{w=0.2} Juuust for you~."
            
        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Of course I can!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n "You bet I can!"

        else:
            n "Sure thing!"

        jump snap_explanation

# Natsuki hates people being inconsiderate with chewing gum
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_chewing_gum",
            unlocked=True,
            prompt="Chewing gum",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_chewing_gum:
    n "Ugh...{w=0.3} you know what really gets on my nerves?"
    n "When people are gross and don't get rid of chewing gum properly."
    n "Seriously -{w=0.1} it annoys the crap out of me!"
    n "Like,{w=0.1} have you ever walked into a city center and looked at the ground?{w=0.2} At all the paving?"
    n "All those dried up spots of gum -{w=0.1} it's freaking disgusting,{w=0.1} and it looks nasty too!"
    n "And that's in a place where there's usually bins everywhere too,{w=0.1} so it isn't just gross..."
    n "It's super lazy too!{w=0.2} I can't decide what winds me up more."
    n "Even worse than that -{w=0.1} there's even people who go and stick it under tables,{w=0.1} or on walls -{w=0.1} who {i}does{/i} that?!"
    n "Jeez...{w=0.3} makes me want to track them down and stick that crap back in their stupid mouths."
    n "I don't really care if you chew gum yourself,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "Just make sure you dispose of it properly,{w=0.1} 'kay?"
        n "I'm sure you do anyway,{w=0.1} but just in case.{w=0.2} Love you,{w=0.1} [player]~!"

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "But please,{w=0.1} just get rid of it properly when you're done."
        n "Thanks,{w=0.1} [player]~!"

    else:
        n "But seriously -{w=0.1} stick it in the bin when you're done,{w=0.1} alright?{w=0.2} Or just wrap it in a tissue and get rid of it later."
        n "...Or it won't just be the gum that'll be getting chewed out!"

    return

# Natsuki hates people smoking/vaping indoors
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_smoking_vaping_indoors",
            unlocked=True,
            prompt="Smoking and vaping indoors",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_smoking_vaping_indoors:
    n "You know what stinks,{w=0.1} [player]?"
    n "I mean {i}really{/i} stinks -{w=0.1} not just figuratively,{w=0.1} but literally too?"
    n "When people smoke or vape indoors,{w=0.1} or near entrances -{w=0.1} {i}especially{/i} when other people are around.{w=0.2} I can't stand it!"
    n "Like...{w=0.3} how inconsiderate can you be?{w=0.2} Seriously?"
    n "For starters,{w=0.1} and like I was just saying -{w=0.1} it absolutely {i}reeks{/i}!"
    n "Tobacco is awful smelling stuff,{w=0.1} and all those sickly vaping fluid types aren't much better either."
    n "It clings to the walls too -{w=0.1} so the smell hangs around for ages!"
    n "Speaking of clinging to the walls,{w=0.1} the smoke literally does that too -{w=0.1} have you {i}seen{/i} a smoker's house,{w=0.1} or car?"
    n "All those yellow stains...{w=0.3} you'd think it was painted on or something.{w=0.2} Ew!"
    n "And you know what,{w=0.1} [player]?{w=0.2} I haven't even gotten to the worst of it yet..."
    n "I've said nothing about how expensive it all is,{w=0.1} or the health problems not just to the smoker..."
    n "...But to everyone else!"
    n "Ugh..."
    n "Don't get me wrong -{w=0.1} if someone wants to smoke or vape,{w=0.1} that's their choice and their money.{w=0.2} I don't care."
    n "But the least they can do is respect the decision of everyone who {i}doesn't{/i},{w=0.1} you know?"
    n "..."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "I know you,{w=0.1} [player].{w=0.2} I highly doubt you'd be the kind of person to be a jerk like that."
        n "Just don't prove me wrong,{w=0.1} alright?{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "I doubt you'd be a jerk like that even if you do smoke,{w=0.1} [player]."
        n "But...{w=0.3} try not to prove me wrong,{w=0.1} 'kay?{w=0.2} I like you more as not a jerk."
        n "Thanks!"

    else:
        n "I don't think you'd be a jerk like that,{w=0.1} [player]."
        n "But...{w=0.3} just in case -{w=0.1} keep it in mind,{w=0.1} will you?"
        n "Thanks!"

    return

# Natsuki hates people who don't wash their hands after using a restroom
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_unwashed_hands",
            unlocked=True,
            prompt="Handwashing",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_unwashed_hands:
    n "Hey,{w=0.1} [player]."
    n "Have you ever worked in a restaurant,{w=0.1} or a hospital or anything like that?"
    n "Because I bet if there's one thing drilled into you...{w=0.3} it's how important washing your hands is!"
    n "It really gets on my nerves when people don't wash their hands after doing something nasty."
    n "Like...{w=0.3} we {i}know{/i} how important it is to stop germs getting around -{w=0.1} and {i}what{/i} exactly is hard about sticking your hands under the tap for a minute?!"
    n "It annoys me even more when people are really dumb about it too!{w=0.2} Like,{w=0.1} they think they don't need to do that if they didn't go."
    n "Newsflash -{w=0.1} if you went in,{w=0.1} you must have touched stuff -{w=0.1} so now there's all that crap on your hands that you've taken out with you!"
    n "Not only is it {i}super{/i} icky and bad for {i}your{/i} health..."
    n "It's awful for others too!{w=0.2} What if you're about to handle someone's food,{w=0.1} or visit someone in hospital?"
    n "You could make someone seriously ill..."
    n "...And then they get all upset when you call them out on their grossness!{w=0.2} I mean,{w=0.1} come {i}on{/i}!"
    n "Just...{w=0.3} ugh."
    n "...[player]."
    n "I really hope you keep your hands spick and span.{w=0.2} And not just when you visit the restroom."
    n "Before you prepare food,{w=0.1} after you've handled trash...{w=0.3} just think about where you've been,{w=0.1} alright?"

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "Don't get me wrong though!{w=0.2} I trust that you do the right thing!"
        n "Just keep up the good work for me,{w=0.1} alright?{w=0.2} For everyone."
        n "Thanks,{w=0.1} [player]!"

    else:
        n "It really isn't that much to ask...{w=0.3} is it?"

    return

# Natsuki hates people who litter
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_litter",
            unlocked=True,
            prompt="Littering",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_litter:
    n "You know,{w=0.1} [player]..."
    n "At school?{w=0.2} At my school,{w=0.1} anyway?"
    n "We -{w=0.1} the students -{w=0.1}  were actually responsible for keeping it all clean."
    n "Ehehe.{w=0.2} Are you surprised?"
    n "Yep!{w=0.2} From the bins,{w=0.1} to the desks,{w=0.1} to the floors.{w=0.2} It was all our effort that kept it squeaky clean!"
    n "N-{w=0.1}not that I {i}enjoyed{/i} it,{w=0.1} of course!{w=0.2} Cleaning {i}is{/i} pretty lame,{w=0.1} but it's just something you gotta do."
    n "But I'll tell you one thing,{w=0.1} [player]."
    n "{i}Nothing{/i} pissed me off more than the jerks who just went and dropped or left their trash everywhere."
    n "...And not even just in school!"
    n "I mean...{w=0.3} where do I start?!"
    n "First off -{w=0.1} how much of a freaking slob do you have to be?{w=0.2} Do these people just drop crap all over their homes too?!"
    n "It annoys me even more when there's bins and stuff literally right there!"
    n "Like,{w=0.1} wow...{w=0.3} lazy as well as inconsiderate?{w=0.2} What a {i}charming{/i} combo!"
    n "Even if there isn't a trash can or whatever around..."
    n "It's not like they don't have pockets,{w=0.1} or can't just carry it around for a few minutes!"
    n "Ugh..."
    n "And I haven't even mentioned people tossing their rubbish out of cars,{w=0.1} or into lakes and ponds!"
    n "It pisses me off just thinking about it..."
    n "..."
    n "[player]."
    
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "I know you.{w=0.2} In fact,{w=0.1} I daresay I know you {i}very{/i} well by now."
        n "I don't think you're the sort to do that at all..."
        n "I'm not wrong...{w=0.3} am I?"
        n "I don't wanna have to be.{w=0.2} Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "I don't think you're like that,{w=0.1} [player]."
        n "Or...{w=0.3} at least you don't {i}try{/i} to be anyway."

    else:
        n "I really,{w=0.1} really hope you aren't one of those people."

    n "So..."
    n "...If you're a litterbug already,{w=0.1} I'll forgive you this one time."
    n "Just...{w=0.3} make sure you clean up your act,{w=0.1} okay?"

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n "Ehehe.{w=0.2} Love you,{w=0.1} [player]~."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n "It'd...{w=0.3} mean a lot."
        n "Ahaha..."

    else:
        n "Thanks,{w=0.1} [player]."

    return

# Natsuki discovers a music player, leading to the unlocking of custom music! 
# We assign no categories to this so it isn't selectable via menu, making it a one-time conversation
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_introduction",
            unlocked=True,
            prompt="Discovering custom music",
            conditional="not persistent.jn_custom_music_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_introduction:
    n "Hmm..."
    n "I wonder if it's still here..."

    play audio drawer 
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n "Come on!{w=0.2} It's gotta still be here!{w=0.2} I know it!"

    play audio drawer 
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")    

    n "..."
    n "Aha!{w=0.2} Yes!"
    n "..."
    n "Oh!{w=0.2} [player]!{w=0.2} [player]!"
    n "Guess what I fooound!{w=0.2} Ehehe."
    n "It's...{w=0.3} a music player!{w=0.2} Neat,{w=0.1} right?"
    n "Well...{w=0.3} kinda.{w=0.2} It's not exactly...{w=0.3} {i}modern{/i},{w=0.1} but it'll do the job!"
    n "Come to think of it...{w=0.3} I don't really even know who it belongs to."
    n "We just found it left in the clubroom one day.{w=0.2} Nobody knew if it belonged to anyone -{w=0.1} and trust me,{w=0.1} we tried to find out!"
    n "We asked around in lessons,{w=0.1} we sent out notes...{w=0.3} nothing!"
    n "So...{w=0.3} we kinda just kept it here,{w=0.1} in my desk,{w=0.1} in case whoever it was came back to pick it up."
    n "I guess they never will now,{w=0.1} huh?" 
    n "Ahaha..."
    n "Well,{w=0.1} whatever.{w=0.2} The point is we can play whatever music we want now!"
    n "I think I figured out a way to let you send me whatever you want me to put on,{w=0.1} so listen up,{w=0.1} 'kay?"
    jump talk_custom_music_explanation

# Natsuki explains how the custom music functionality works
# Unlocked as a permanent topic once Natsuki has naturally lead into this from talk_custom_music_introduction via random topics
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_explanation",
            unlocked=True,
            prompt="Can you explain custom music for me again?",
            category=["Music"],
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_custom_music_explanation_given",
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_explanation:
    if persistent.jn_custom_music_explanation_given:
        n "Huh?{w=0.2} You want me to explain how custom music works again?"
        n "Sure,{w=0.1} I can do that!"
        n "First things first,{w=0.1} let me just check for the {i}custom_music{/i} folder..."

    else:
        n "Alright!{w=0.2} So...{w=0.3} it's actually pretty simple,{w=0.1} [player]."
        n "There should be a folder called {i}custom_music{/i} somewhere around here..."
        n "Let me just take a look,{w=0.1} one sec..."
        n "..."

    if jn_custom_music.get_directory_exists():
        n "Well,{w=0.1} hey!{w=0.2} It's already there!{w=0.2} I must have set it up earlier and forgot."
        n "No complaints from me!{w=0.2} Ehehe."

    else:
        n "Okaaay!{w=0.2} It wasn't there,{w=0.1} so I've just created it for you."

    $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    n "So,{w=0.1} [player] -{w=0.1} if you click {a=[folder]}here{/a},{w=0.1} that'll take you to the folder I set up."
    n "Then all you gotta do is just {i}copy{/i} your music into that folder,{w=0.1} and you're good to go!"
    n "Easy as pie,{w=0.1} huh?{w=0.2} Ehehe."
    n "Oh -{w=0.1} a couple of things first though,{w=0.1} [player]."
    n "Any music you give me needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format."
    n "If you don't know how to check,{w=0.1} then just look at the letters after the period in the file name."
    n "You should also be able to see those in the file {i}properties{/i} if they don't appear on the screen at first."
    n "Like I said -{w=0.1} this thing isn't {i}exactly{/i} super modern,{w=0.1} so it won't work with any fancy newer formats,{w=0.1} or weird old ones."
    $ persistent.jn_custom_music_unlocked = True
    $ persistent.jn_custom_music_explanation_given = True
    n "Once you've done that,{w=0.1} just click the {i}Music{/i} button,{w=0.1} and I'll check that it's all done right."
    n "...And that's about it!"
    n "A word of warning though,{w=0.1} [player]..."
    n "You better have good taste."
    n "Ahaha!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_vtubers",
            unlocked=True,
            prompt="Do you follow any VTubers?",
            category=["Games", "Media", "Society"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_vtubers:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "VTubers,{w=0.1} huh?{w=0.2} You're asking {i}me{/i}?"
        n "...Wow,{w=0.1} [player].{w=0.2} I'm impressed."
        n "Yet again,{w=0.1} you've proved you're even more of a nerd than I am!"
        n "Ehehe."
        n "Relax!{w=0.2} Relax,{w=0.1} jeez!{w=0.2} You know I'd never seriously judge your hobbies,{w=0.1} you dummy."
        n "But yeah,{w=0.1} anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n "Oh!{w=0.2} Oh!{w=0.2} I think I know those!"
        n "They're those people with the anime avatars that stream stuff online for people,{w=0.1} right?"
        n "Well..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Huh?{w=0.2} VTubers?{w=0.2} Like those people with the anime-style avatars that play games and stuff online for people to watch?"
        n "That {i}is{/i} what you mean,{w=0.1} right?"
        n "Well..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "No,{w=0.1} I do not.{w=0.2} I'd rather be playing the game myself than watching someone play it for me."
        n "If you follow any,{w=0.1} good for you."
        n "{i}Some{/i} of us don't have the time to sit around on our butt for hours..."
        n "...Or the money to just give it away to strangers."
        n "[player]."
        n "How much are we betting you aren't {i}nearly{/i} as toxic to {i}them{/i} as you are to me, huh?"
        return

    else:
        n "No.{w=0.2} And I couldn't give less of a crap if you did,{w=0.1} either."
        n "...And hey,{w=0.1} newsflash,{w=0.1} idiot."
        n "Throwing money at a stranger hiding behind a cutesy picture doesn't make you any less of a jerk.{w=0.2} Heh."
        return

    n "It's definitely a cool idea!{w=0.2} It lets people share their passions and experiences with others behind a completely clean persona..."
    n "Without having to worry about baggage following them into their personal lives,{w=0.1} or people being creeps,{w=0.1} or stuff like that."
    n "A lot of them even make full-blown careers out of it: merchandise,{w=0.1} song releases and everything -{w=0.1} just like idols!{w=0.2} It's crazy!"
    n "That being said..."
    n "I never really got into that sort of thing myself."
    n "Like...{w=0.3} don't get me wrong!{w=0.2} I'm sure they're pretty fun to watch.{w=0.2} If you're into that kind of thing,{w=0.1} I mean."
    n "But I'd rather be playing or doing something {i}myself{/i} than watching someone else do it,{w=0.1} usually."
    n "That might just be me,{w=0.1} though."
    n "...Ehehe."
    n "What about you,{w=0.1} [player]?{w=0.2} Are you into that sort of stuff?"
    n "Wait,{w=0.1} wait!{w=0.2} Don't bother answering that."
    n "You {i}did{/i} ask me about them,{w=0.1} after all -{w=0.1} I think that speaks for itself,{w=0.1} wouldn't you agree?"
    n "Ahaha!"
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
