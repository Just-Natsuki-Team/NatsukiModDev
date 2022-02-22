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
        n 1uskwr "W-wait...{w=0.3} you're telling me there's a camera here?{w=0.2}"
        extend 1fbkwr " Are you kidding me?!"
        n 1kbktr "Uuuu-"
        n 1kslaj "I've never liked having my picture taken without my permission..."
        n 1ksgsl "Just...{w=0.3} please don't take any pictures of me unless I ask,{w=0.1} okay [player]?{w=0.2}"
        extend 1kllsl " It'd really mean a lot to me."
        n 1kllsf "I hope you can understand."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1tnmsf "Hmm?{w=0.2} Pictures of me?"
            n 1nllsl "Honestly,{w=0.1} I don't think I'll ever be completely comfortable with them..."
            n 1unmss "But I trust you to make a good shot!"
            n 1fcsbg "As long as you ask,{w=0.1} I've got no problem with it!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            if jn_screenshots.are_screenshots_blocked():
                n 1fsqpu "Really,{w=0.1} [player]?{w=0.1} You're asking me about this {i}now{/i}?"
                n 1fslaj "You know {i}perfectly well{/i} how I feel about this."
                n 1fsgbo "I don't hate you,{w=0.1} but please try to remember how I feel before you do stuff like that."
                n 1ncssl "I'm...{w=0.3} still gonna keep that turned off for now,{w=0.1} though."

            else:
                n 1ncuaj "H-{w=0.1}huh?{w=0.2} Pictures of me?"
                n 1nlrsr "Not a fan,{w=0.1} honestly -{w=0.1} but you knew that much already,{w=0.1} [player]."
                n 1knmpu "It's just..."
                n 1kcspu "I really...{w=0.3} need...{w=0.3} my privacy.{w=0.1} It matters a lot to me."
                n 1kwmpu "You understand,{w=0.1} right?"
                n 1knmnv "So...{w=0.3} if you ever wanna take a picture,{w=0.1} can you ask first?"
                menu:
                    n "Will you do that for me?"

                    "Of course!":
                        n 1kcssg "Thanks,{w=0.1} [player]."
                        n 1knmss "That really...{w=0.3} means a lot to me."

                    "I'll think about it.":
                        n 1fwmsf "[player]...{w=0.3} come on.{w=0.1} I'm being serious here."
                        extend 1fllsl " Don't mess me around like this."
                        n 1nnmaj "Make sure you ask,{w=0.1} okay?"

                    "...":
                        n 1nunfr "..."
                        n 1fnmaj "[player].{w=0.2} This isn't funny."
                        n 1fllsl "Just make sure you ask."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n 1fsqsl "...Pictures,{w=0.1} [player]?{w=0.2} Really?"
            n 1fsqaj "I don't think I want to have you taking my picture,{w=0.1} [player]."
            n 1fslfr "Let's talk about something else."

        else:
            n 1kplpu "Don't even {i}try{/i} to pretend like you care about how I feel about pictures."
            n 1kcssr "We're done here,{w=0.1} [player]."
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
        extend 1uchgn " but then again,{w=0.1} it's not like I can't keep a pet here instead,{w=0.1} right?{w=0.1} Ehehe."

    if persistent.jn_player_pet is None:
        n 1unmbg "But what about you,{w=0.1} [player]?"
        menu:
            n "Do you have any pets?"

            "Yes, I do.":
                n 1uspaw "Oh!{w=0.2} Oh oh oh!{w=0.2} You gotta tell me,{w=0.1} [player]!"
                n 1uspbs "What do you have?{w=0.2} What do you have?"
                call pet_options_a

            "No, I don't.":
                n 1usgem "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n 1nchbg "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n 1uchgn "I wanna hear all about it!"

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
                n 1usgem "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n 1nchbg "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n 1uchgn "I wanna hear all about it!"

            "I lost one.":
                n 1knmaj "Oh...{w=0.3} oh jeez..."
                n 1knmfr "I'm so sorry,{w=0.1} [player].{w=0.2} Are you okay?"
                n 1kllbo "Maybe we should talk about something else to keep your mind off things..."
                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
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
            n 1unmbs "I hope you didn't just say that because I like them,{w=0.1} though.{w=0.2}{nw}"
            extend 1uchsm " Ehehe."
            n 1tnmsm "Just don't pamper it too much,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "cats"
            
        "Chameleons":
            n 1unmaj "Oh!{w=0.2} Chameleons!"
            n 1uchgn "That's super cool,{w=0.1} [player]!"
            n 1unmbg "The colour changing is crazy enough,{w=0.1} but those eyes too{w=0.1} -{w=0.1} it's like someone just made them up!"
            n 1uchgn "Still{w=0.1} -{w=0.1} that's awesome!"
            n 1unmbg "You better take good care of it,{w=0.1} okay?"
            $ persistent.jn_player_pet = "chameleons"

        "Dogs":
            n 1uwdaj "Oh!{w=0.2} A dog?{w=0.2}{nw}"
            extend 1uchbs " Awesome!"
            n 1nnmsm "I don't think a dog would be my first choice,{w=0.1} what with all the walks and all that."
            n 1uchbs "But I can't think of a more loving pet!"
            n "I hope yours looks after you as much as you look after it!"
            $ persistent.jn_player_pet = "dogs"
            
        "Ferrets":
            n 1unmlg "Oh!{w=0.2} A ferret?"
            n 1uchbs "That's {i}adorable{/i}!"
            n 1tllbg "But...{w=0.3} I've always wondered.{w=0.2}{nw}"
            n 1tchbg " Are they more like a cat,{w=0.1} or a dog?"
            n 1flrss "Well,{w=0.1} whatever.{w=0.2} Either way,{w=0.1} [player]..."
            n 1unmlg "You better take good care of the little guy!"
            $ persistent.jn_player_pet = "ferrets"

        "More...":
            call pet_options_b

    return

label pet_options_b:
    menu:
        n "What did you get?"

        "Fish":
            n 1unmaj "Ooh!{w=0.2} Fish are interesting!"
            n 1kllnv "I don't think I'd call them super affectionate personally..."
            n 1uchgn "But I think they're a neat way to relieve stress!{w=0.2} They must be calming to watch in their own little world."
            n 1nsqsm "I bet you feel like you could lose yourself in that tank.{w=0.2}{nw}" 
            extend 1nchsm " Ehehe."
            $ persistent.jn_player_pet = "fish"
            
        "Frogs":
            n 1kspaw "Ooh!{w=0.2} Froggies!"
            extend 1kspbs " Cute!"
            n 1fsqsm "I seriously can't get enough of their faces.{w=0.2}{nw}" 
            extend 1fbkbs " They always look so confused!"
            n 1fllbg "Ehehe.{w=0.2} Well,{w=0.1} [player]..."
            n 1fchgn "You better {i}hop{/i} to it and take care of yours!"
            $ persistent.jn_player_pet = "frogs"
        
        "Gerbils":
            n 1kspaw "Awww!{w=0.2} I like gerbils!"
            n 1uchbs "It's so cute how they live in little groups to keep each other company."
            n 1unmbs "They're good at digging,{w=0.1} too{w=0.1} -{w=0.1} like seriously good!"
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

        "More...":
            call pet_options_c

        "Back...":
            call pet_options_a

    return

label pet_options_c:
    menu:
        n "What did you get?"
        
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
            n 1kwmsg "...I wish I could share your enthusiasm!{w=0.2}{nw}"
            extend 1kllss " Ahaha..."
            n 1ksqun "I don't think I could stomach creepy crawlies myself."
            n 1ksrun "You've certainly got an...{w=0.3} interesting taste,{w=0.1} [player]."
            n 1kwmss "But I'm sure you take great care of yours!"
            $ persistent.jn_player_pet = "insects"
            
        "Lizards":
            n 1uchgn "Ooh!{w=0.2} Lizards,{w=0.1} huh?"
            n 1fsqss "...I trust you aren't just as cold-blooded yourself,{w=0.1} [player]."
            n 1fchgn "...Pffffft!{w=0.2}{nw}"
            extend 1uchlg " I'm kidding, [player]!{w=0.2} I'm just kidding!"
            n 1unmbg "Cool looking critters though!{w=0.2}"
            extend 1tllbg " I think you'd actually be hard pressed to find a more varied kind of pet."
            n 1uchgn "You better keep yours nice and toasty,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "lizards"
            
        "Mice":
            n 1uchgn "Ehehe.{w=0.2} Mice are adorable!"
            n 1nllaj "I'm still not sure how I feel about the tail..."
            n 1unmbg "But they're so curious and sociable!{w=0.2} I love watching them play together."
            n 1uchgn  "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "mice"
            
        "Rats":
            n 1unmbs "Rats,{w=0.1} huh?"
            n 1fsgsg "Were you expecting me to be grossed out?"
            n 1uchbs "Ahaha!"
            n 1unmsm "Rats are fine.{w=0.2} They're surprisingly intelligent,{w=0.1} too!"
            n 1uchgn "Are you perhaps training yours,{w=0.1} [player]?{w=0.2} Ehehe."
            n 1unmbs "Make sure you take care of yours for me,{w=0.1} okay?"
            $ persistent.jn_player_pet = "rats"
            
        "More...":
            call pet_options_d

        "Back...":
            call pet_options_b

    return
   
label pet_options_d:
    menu:
        n "What did you get?"
        
        "Rabbits":
            n 1kspaw "Awwwwww!{w=0.2} Bunnies!"
            n 1kcuaw "They're so cuuute!{w=0.2} I love them!"
            n 1uchbs "Especially the ones with the floppy ears,{w=0.1} they look so cuddly!"
            n 1knmbo "It's a shame they need so much space,{w=0.1} though."
            n 1uchgn "But I'm sure yours have plenty of room to roam!{w=0.2} Ehehe."
            $ persistent.jn_player_pet = "rabbits"
            
        "Snakes":
            n 1uskaj "H-{w=0.1}huh?"
            extend 1uscem " S-{w=0.1}snakes?"
            n 1fcsun "Uuuuuu..."
            n 1kcsaj "...Fine.{w=0.2} I'll just be straight with you, [player].{w=0.2}{nw}"
            extend 1kllsl " I'm...{w=0.3} not great with those."
            n 1kllaj "S-{w=0.1}snakes,{w=0.1} I mean."
            n 1kllsl "They just...{w=0.3} don't really agree with me.{w=0.2} I don't know why."
            n 1fcsgsl "B-{w=0.1}but that's not to say that they {i}can't{/i} be cute,{w=0.1} obviously!{w=0.2}{nw}" 
            extend  1flrpo " Making that assumption would just be ignorant."
            n 1ksrpo "...And they deserve care just like any other pet.{w=0.2}{nw}" 
            extend 1flraj " So..."
            n 1fnmpo "You better not be flaking out on yours,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "snakes"

        "Something else":
            n 1unmaj "Ooh!{w=0.2} An exotic owner, are we?"
            n 1tsgsg "I wonder if that says something about the rest of your tastes?{w=0.2} Ehehe."
            n 1uchgn "I trust you take good care of yours.{w=0.1} Uncommon pets can be pretty demanding!"
            $ persistent.jn_player_pet = "something_else"
            
        "Back...":
            call pet_options_c
            
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
    n 1ullbo "Hmm..."
    n 1unmaj "Hey [player],{w=0.1} have you ever heard of service animals?"
    n 1unmbg "They're like animals people train up specially to do jobs that humans can't do easily."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmbs "Some work in airports to keep people safe,{w=0.1} others help in rescues...{w=0.3} it's super cool!"
        n 1uwmsm "But there's one type that's especially awesome..."
        n 1uchgn "Emotional support animals!"
        n "They're like really tame pets that are used to comfort people going through a bad time."
        n "They come in all different shapes and sizes too!{w=0.2} Dogs and cats -{w=0.2} obviously -{w=0.2} but even horses sometimes!"
        n "Isn't that amazing?"
        n 1ulrbo "..."
        n 1uplaj "You know,{w=0.1} [player]..."
        n 1kcsaj "Sometimes I wonder if one could have helped Sayori..."
        n 1klrfr "...but I try not to think about that too much."
        n 1knmem "They {i}are{/i} great,{w=0.1} but they don't do miracles."
        n 1kwmem "[player]...{w=0.3} I really hope you never have to seek their help."
        n 1kwmnv "And on that note,{w=0.1} if you do need support?"
        n "...I'd be happy to provide.{w=0.2} Remember that,{w=0.1} alright?"

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1kwmnv "I really,{w=0.1} really care about you,{w=0.1} [player]."
            n "I-{w=0.2}I want you to know that you can depend on me,{w=0.1} 'kay?"

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1kwmnv "I love you,{w=0.1} [player]."
            return

    else:
        n 1unmbo "They work in a bunch of places.{w=0.2} Airports and rescues and stuff,{w=0.1} usually."
        n 1unmss "But I really like emotional support animals."
        n "They're like specially tame pets that are used to comfort those having a bad time."
        n 1nsgbo "..."
        n 1nsgaj "You know, [player].{w=0.2} To be perfectly honest with you?"
        n "Sometimes I feel like I could use one."
        n 1nsrss "Aha..."
        return

    n 1ksrfr "..."
    n 1kwmfr "That got kinda heavy,{w=0.1} didn't it?"
    n 1kwmbg "Well,{w=0.1} enough of that.{w=0.2}"
    extend 1uwmss " What else should we talk about?"
    return

# Natsuki highlights her concern for her player using their computer for long periods of time, and offers her wisdom
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_computers_healthily",
            unlocked=True,
            prompt="Using computers healthily",
            conditional="store.jn_utils.get_current_session_length().total_seconds() / 3600 >= 8",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    n 1unmaj "Huh."
    n 1tnmaj "Hey,{w=0.1} [player].{w=0.2} I just thought of something."
    n 1unmsf "You gotta be at your computer to talk to me,{w=0.1} right?"
    n 1ullsf "And you've been here a while already..."

    if (jn_activity.has_player_done_activity(jn_activity.JNActivities.work_applications) 
        or jn_activity.has_player_done_activity(JNActivities.artwork)
        or jn_activity.has_player_done_activity(JNActivities.coding)):
            n 1knmaj "In fact, I've even {i}seen{/i} you working on a lot of stuff myself!"
            n 1kllsl "..."

    n 1nchgn "Alright,{w=0.1} that's it!{w=0.2} I've decided."
    n 1uchgn "I'm gonna give you a little lesson on using your computer the right way!"
    n 1nnmss "Number one:{w=0.2} posture!"
    n 1fwmlg "Sit up straight,{w=0.1} and back against the chair,{w=0.1} [player].{w=0.2}"
    extend 1uchlg " I mean it!"
    n 1tnmlg "You don't want back problems,{w=0.1} do you?"
    n 1nnmsm "Make sure your feet can still touch the floor,{w=0.1} though.{w=0.2}"
    extend 1uchgn " Even I can do that!"
    n 1nnmaj "Number two:{w=0.2} distance!"
    n 1nsggn "I know you can't get enough of me,{w=0.1}"
    extend 1fnmpo " but I don't wanna see you pressing your face against the screen.{w=0.2} It's weird."
    n 1uchgn "So make sure you sit about an arm's length away from the display,{w=0.1} alright?"
    n 1uwdaj "Oh!{w=0.2} Don't forget to keep your stuff in easy reach though{w=0.1} -{w=0.1}"
    extend 1unmsm " like your mouse."
    n 1unmbg "Number three:{w=0.2} breaks!"
    n 1uwmbg "I don't know about you,{w=0.1} but I get all fidgety if I stay still too long..."
    n 1fchgn "So make sure you get off your butt and do some stretches a few times per hour!"
    n 1fsqsg "You could even get some water or something if you {i}really{/i} need an excuse to move."
    n 1nnmsm "It'd also give your eyes a rest from the screen!"
    n 1uchbs "Alright{w=0.1} -{w=0.1} and the last one!{w=0.2} This one's important,{w=0.1}"
    extend 1uchgn " so listen up good!"
    n 1unmbo "If you ever feel unwell{w=0.1} - {w=0.1}like your back aches,{w=0.1} or your eyes hurt or something..."
    n 1nwmbo "Please just stop whatever you're doing.{w=0.2} Your health comes first.{w=0.2} I don't care what needs to be done."
    n 1unmsm "Take some time to feel better,{w=0.1} then make sure all your stuff is set up right like I said."
    n "Don't carry on until you feel well enough{w=0.1} -{w=0.1} talk to someone if you have to!"
    n 1uchgn "Okaaay!{w=0.2} Lecture over!"
    n 1ullaj "Wow...{w=0.3} I rambled on a while,{w=0.1} didn't I?{w=0.2}"
    extend 1klrbgl " Sorry,{w=0.1} sorry!{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1kwmsml "But you know I only do these things because I really care about you,{w=0.1} [player]...{w=0.3} right?"
        n 1kwmnvl "So please...{w=0.3} take care of yourself, okay?{w=0.2} I don't want you hurting because of me."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1kwmsml "I love you,{w=0.1} [chosen_endearment]."
            n 1kwmnvl "..."
            return

    else:
        n 1usglg "But you know I only say these things because I care."
        n 1nsqpo "...And I don't want you whining to me that your back hurts.{w=0.2}"

    n 1nchgn "Ahaha...{w=0.3} now, where were we?"
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
    n 1nnmbo "Hey,{w=0.1} [player]..."
    n 1nllsr "You should get out more."
    n 1fsqsm "..."
    n 1fchbg "Ahaha!{w=0.2} No,{w=0.1} really!{w=0.2} I'm serious!"
    n 1ulraj "At school,{w=0.1} it's easy to get exercise since we gotta walk everywhere,{w=0.1} and we have sports and such..."
    n 1nsqsf "It's not so straightforward when you have a job and other stuff to worry about,{w=0.1} though."
    n 1fllss "I'm not gonna lie and say I work out or anything like that..."
    n 1ullaj "But I try to get walks in if I can.{w=0.5}{nw}"
    extend 1uchgn " Any excuse to hit the bookshop is reason enough for me!"
    n 1unmbg "You should give it a shot too,{w=0.1} [player]!"
    n 1nlrss "It doesn't have to be a hike or anything crazy{w=0.1} -{w=0.3}{nw}"
    extend 1nnmsm " it's more about keeping at it,{w=0.1} really."
    n 1fchsm "Even a daily ten minute walk will help you feel refreshed and awake!"
    n 1ullaj "So...{w=0.5}{nw}"
    extend 1fnmss " make sure you get out soon,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fchbg "I wanna see you fighting fit!{w=0.5}{nw}"
        extend 1uchsm " Ehehe."
        return

    n 1fchbg "I'm counting on you!"
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
    n 1ullaj "You know,{w=0.1} I'll admit it,{w=0.1} [player]."
    n 1flrbg "I...{w=0.3} kinda have a short fuse.{w=0.5}{nw}"
    extend 1klrss " Ehehe."
    n 1fnmss "I've been trying to work on that though,{w=0.3}{nw}"
    extend 1fchbg " and I'd love to share some of the ways I deal with stress!"
    n 1unmss "Personally,{w=0.1} I think the best way to deal with it if you can is to try and create some distance."
    n 1nllss "If things get a little too much,{w=0.1} I just step outside if I can."
    n 1unmbo "Some fresh air and a change of scenery can really put things into context.{w=0.5}{nw}"
    extend 1fwdaj " It's crazy effective!"
    n 1ulraj "Don't just create physical distance,{w=0.1} though.{w=0.5}{nw}"
    extend 1fnmpu " Distance yourself mentally too!"
    n 1ncssr "If something is stressing you out,{w=0.1} you need to starve it of attention."
    n 1nllsf "If I can't go somewhere else,{w=0.1} I just read something,{w=0.1} or watch some dumb videos."
    n 1fchbg "But do whatever works for you; {w=0.1}we all have our own comfort zones!"
    n 1fslpo "A-{w=0.1}and of course,{w=0.1} you could always come see me,{w=0.1} you know..."
    n 1fchbgl "A-{w=0.1}anyway!"
    n 1unmpu "The point is to always try and come back with a clean headspace,{w=0.3}{nw}"
    extend 1nnmss " and don't sweat the small things."
    n 1tnmss "You can manage that,{w=0.1} right [player]?"
    n 1uchsm "I'll keep working on it if you do!"
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
    n 1tllsr "..."
    n 1fllsr "..."
    n 1tnmpu "Hmm...?"
    n 1uwdgs "O-{w=0.1}oh!{w=0.5}{nw} "
    extend 1flrbg " A-{w=0.1}aha!{w=0.5}{nw}"
    extend 1flrdvl " I spaced out!"
    n 1unmaj "I was just thinking..."
    n 1flrbo "It's so easy to spend more than you mean nowadays,{w=0.1} you know?"
    n 1flrpu "Like...{w=0.3} it seems everywhere you go,{w=0.1} there's a sale,{w=0.1} or deals,{w=0.1} or some kind of limited offer..."
    n 1unmpu "And every place accepts all kinds of ways of paying,{w=0.1} too.{w=0.5}{nw}"
    extend 1fsrpo " They make it super convenient!"
    n 1fsrpo "I guess what I'm getting at is...{w=0.3} try to be careful of your spending habits,{w=0.1} okay?"
    n 1unmss "Try not to buy junk you don't need{w=0.1} -{w=0.3}{nw}"
    extend 1flrbg " think of how much you threw away the last time you cleaned out!"
    n 1uwdajl "T-{w=0.1}that's not to say you shouldn't treat yourself,{w=0.1} of course!{w=0.5}{nw}"
    extend 1flrssl " You deserve cool stuff too!"
    n 1flrss "Money can't buy happiness...{w=0.5}{nw}"
    extend 1fchgn " but it sure as hell makes finding it easier.{w=0.5}{nw}"
    extend 1uchbs " Ahaha!"
    n 1nllss "Well,{w=0.1} anyway.{w=0.5}{nw}"
    extend 1tnmsg " Just try to think a little before you spend,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
    extend 1uchbs " that's all I'm saying!"

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1nslbg "Besides..."
        n 1fsqsm "Gotta save up all we can for when we hang out,{w=0.1} right?{w=0.5}{nw}"
        extend 1uchsm " Ehehe."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1uchbgl "Love you,{w=0.1} [player]~!"

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
    n 1unmaj "Hey,{w=0.1} [player]..."
    menu:
        n "Have you eaten today?"

        "Yes":
            n 1fnmbg "Aha!{w=0.5}{nw}"
            extend 1fsqbg " But did you eat {i}well{/i},{w=0.1} [player]?"

        "No":
            n 1knmpu "Huh?{w=0.2} What?{w=0.5}{nw}"
            extend 1knmem " Why not?!"
            n 1fnmem "You aren't skipping meals,{w=0.1} are you?"
            n 1flrpo "You better not be,{w=0.1} [player]."

    n 1unmpu "It's super important to make sure you aren't only eating regularly,{w=0.3}{nw}"
    extend 1fnmpu " but eating decently too!"
    n 1fnmsr "The right diet makes all the difference,{w=0.1} [player]."
    n 1ullaj "So...{w=0.5}{nw}"
    extend 1nnmaj " try and make an effort with your meals,{w=0.1} got it?"
    n 1fnmaj "And I mean a real effort!{w=0.5}{nw}"
    extend 1ulrss " Try to prepare them from scratch if you can;{w=0.3}{nw}"
    extend 1flrss " it's often cheaper than ready meals anyway."
    n 1unmss "Cut back on things like salt and sugar and stuff too...{w=0.5}{nw}"
    extend 1nslpo " as well as anything really processed."
    n 1unmaj "Oh {w=0.1}-{w=0.3}{nw}"
    extend 1fnmaj " and like I said,{w=0.1} have meals regularly too!"
    n 1fchbg "You shouldn't find yourself snacking on junk if you have proper meals throughout the day."
    n 1usqsm "Your bank balance and your body will thank you.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fsqsm "And besides..."
        n 1usqss "I gotta get you into good habits by yourself before I'm there to make you."
        n 1fchgn "Ahaha!{w=0.2} I'm kidding,{w=0.1} [player]!{w=0.2} I'm kidding!"
        n 1fsqsm "...Mostly."

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uchsm "Love you, [player]~!{w=0.2} Ehehe."
            return

    n 1fllss "Now...{w=0.3} where were we?"
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
    n 1unmbo "Huh?{w=0.2} My favourite season?"
    if not persistent.jn_player_favourite_season:
        n 1tllss "That's a little random,{w=0.1} isn't it?"
        n 1tnmss "Well...{w=0.3} anyway.{w=0.3}{nw}"
        extend 1fnmaw " Tough question, [player]!"
        n 1fsrsl "I think if I had to pick..."
        n 1fchts "It'd be summer!{w=0.2} Duh!"
        n 1fsqss "Why?{w=0.5}{nw}"
        extend 1fchgn " Just think about it,{w=0.1} [player]!"
        n 1ullbg "Long trips to the beach...{w=0.5}{nw}"
        extend 1ncssm " ice cream in the shade...{w=0.5}{nw}"
        extend 1ksrss " lazy evening walks to the shops..."
        n 1flleml "I-{w=0.1}I mean,{w=0.3}{nw}"
        extend 1fllbgl " what's not to love?"
        n 1fchbg "I can just enjoy life out there without having to worry about the weather!"
        n 1usqsg "I don't think I need to make my case any more clear,{w=0.1} do I?{w=0.5}{nw}"
        extend 1uchsm " Ahaha."
        n 1unmaj "Although...{w=0.3} what about you,{w=0.1} [player]?"
        menu:
            n "What's your favourite season?"

            "Spring":
                n 1fnmss "Oh?{w=0.2} Spring,{w=0.1} huh?"
                n 1tllsr "Hmmm..."
                n 1unmss "I mean,{w=0.1} I kinda get it.{w=0.2} It's the sign winter finally got lost,{w=0.1} right?"
                n 1ulrss "And I suppose the flowers blooming again is kinda cool to see."
                n 1fsqan "But the rain!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1fcspu " It just never stops!"
                n 1fllpo "Roll on summer,{w=0.1} I say."
                $ persistent.jn_player_favourite_season = "Spring"

            "Summer":
                n 1fsgbg "Aha!{w=0.2} I knew it!"
                n 1fsqbg "Nobody can resist some fun in the sun,{w=0.1} am I right?"
                n 1fnmbg "I'm glad we both agree,{w=0.1} [player].{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                $ persistent.jn_player_favourite_season = "Summer"

            "Autumn":
                n 1unmaj "Autumn?{w=0.5}{nw}"
                extend 1nllaj " Not a bad choice,{w=0.1} actually!"
                n 1ullsm "I like when it's still warm enough in the day to go out and do things..."
                n 1ucsss "But you also get that crisp,{w=0.1} fresh morning air to wake you up."
                n 1ullaj "The falling leaves are super pretty too."
                n 1fcsan "It's just...{w=0.5}{nw}"
                extend 1fsrsr " it's all ruined when the rain comes,{w=0.1} you know?"
                n 1fsqsr "Trudging through all those sloppy leaves is just gross.{w=0.5}{nw}"
                extend 1fcssf " No thanks!"
                $ persistent.jn_player_favourite_season = "Autumn"

            "Winter":
                n 1tnmsf "Huh?{w=0.2} Really?"
                n 1tnmaj "Winter is the last thing I expected you to say,{w=0.1} [player]!"
                n 1tlrbo "Though...{w=0.3} I get it, kinda."
                n 1fcsbg "It's the perfect time of year to get super snug and spend some quality reading time!"
                n 1fslss "Especially since there's not much you can do outside,{w=0.1} anyway."
                $ persistent.jn_player_favourite_season = "Winter"

    else:
        n 1tllbo "Hang on...{w=0.5}{nw}"
        extend 1tnmss " didn't we talk about this before,{w=0.1} [player]?"
        n 1nlrpu "Well,{w=0.1} anyway..."
        n 1ucsbg "I still love summer,{w=0.1} as you know{w=0.1} -{w=0.3}{nw}"
        extend 1fcsbg " and nothing's gonna change that any time soon!"
        n 1tsqsg "What about you,{w=0.1} [player]?"
        menu:
            n "Still rooting for [persistent.jn_player_favourite_season]?"
            "Yes.":
                n 1fcsbg "Ehehe.{w=0.2} I thought as much,{w=0.1} [player]."
                if persistent.jn_player_favourite_season == "Summer":
                    n 1uchbg "You already picked the best season,{w=0.1} after all!"
                    return

                n 1fllss "Well...{w=0.3} I'm afraid you're not gonna sway me!{w=0.5}{nw}"
                extend 1uchbg " Ahaha!"

            "No.":
                n 1tsgbg "Oh?{w=0.2} Changed our mind,{w=0.1} have we?"
                n 1tsqss "Well?{w=0.5}{nw}"
                extend 1fchbg " Tell me then,{w=0.1} [player]!"
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
                    n 1fnmgs "Hey!{w=0.2} [player]!"
                    n 1fsqpo "I thought you said you'd changed your mind?"
                    n 1fllem "You haven't changed your mind at all!{w=0.2} You said [persistent.jn_player_favourite_season] last time,{w=0.1} too!"
                    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                    n 1fcsem "Jeez...{w=0.5}{nw}"
                    extend 1fnmpo " you're such a wind-up sometimes,{w=0.1} [chosen_tease]!"
                    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                        n 1flrpol "N-{w=0.1}not that I {i}dislike{/i} that side of you,{w=0.1} o-{w=0.1}or anything."

                    else:
                        n 1fsqsm "But...{w=0.3} I think I can {i}weather{/i} it."
                        n 1fsrss "For now."

                    return

                else:
                    $ persistent.jn_player_favourite_season = new_favourite_season

                if persistent.jn_player_favourite_season == "Spring":
                    n 1usqss "Ooh?{w=0.2} Favouring Spring now,{w=0.1} [player]?"
                    n 1nlrbo "I could do without all the rain,{w=0.1} but I get it."
                    n 1flrpu "Hmm...{w=0.3} Spring..."
                    n 1tlrbo "I wonder...{w=0.5}{nw}"
                    extend 1tnmss " do you grow anything,{w=0.1} [player]?"
                    n 1fchsm "Ahaha."

                elif persistent.jn_player_favourite_season == "Summer":
                    n 1fchbs "Aha!{w=0.2} See?"
                    n 1fsqbs "You knew I was right all along,{w=0.1} didn't you?"
                    n 1usqsg "Don't even try to deny it,{w=0.1} [player].{w=0.5}{nw}"
                    extend 1fchbg " Summer is the best!"
                    n 1uchsm "I'm just glad you came around.{w=0.2} That's the important thing!"

                elif persistent.jn_player_favourite_season == "Autumn":
                    n 1usqsm "Oh?{w=0.2} You've taken the {i}fall{/i} for Autumn,{w=0.1} have you?"
                    n 1fchsm "Ehehe."
                    n 1ullss "I'll admit,{w=0.1} it's a pretty season,{w=0.1} with all the golden leaves and stuff..."
                    n 1nslss "So long as the weather stays warm,{w=0.1} anyway."

                elif persistent.jn_player_favourite_season == "Winter":
                    n 1tllss "Winter,{w=0.1} huh?{w=0.2} I wasn't expecting that."
                    n 1tnmbo "Do you prefer being indoors now or something,{w=0.1} [player]?"
                    n 1flrss "Well,{w=0.1} if you prefer being all cosy inside..."
                    n 1fsqsm "Then you better not be slacking on your reading,{w=0.1} [player]!{w=0.5}{nw}"
                    extend 1fchsm " Ehehe."

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
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n 1ullaj "Hey,{w=0.1} [player]..."
    n 1unmaj "Do you have off days sometimes?{w=0.2} Where you struggle to get anything done?"
    n 1flrpo "Or you just get distracted super easily?"
    n 1unmbo "To be honest?{nw}"
    extend 1fllss "{w=0.2} I struggled with that for a while.{nw}"
    extend 1fbkwr "{w=0.2} Especially when things like assignments are so boring!"
    n 1nllaj "But...{w=0.5}{nw}"
    extend 1fllbg " I figured out a way of managing that{w=0.1} -{w=0.1} and you should know it too,{w=0.1} [player]!"
    n 1fchbg "Time boxing!"
    n 1nsqpo "And no,{w=0.1} it's not as literal as it sounds."
    n 1nnmaj "The idea is that you set aside a period during the day you want to work{w=0.1} -{w=0.1} like the school day,{w=0.1} or a few hours in the evening."
    n 1fnmbg "Then for each hour in that period,{w=0.1} you split it!"
    n 1ulraj "So for any given hour,{w=0.1} you spend most of that working,{w=0.1} and the remainder on some kind of break."
    n 1unmss "The idea is that it becomes way easier to stay focused and motivated since you always have a breather coming up."
    n 1uchsm "Personally,{w=0.1} I find a 50/10 split works best for me."
    n 1nllbo "So I spend 50 minutes of each hour studying,{w=0.3}{nw}"
    extend 1uchsm " and 10 minutes doing whatever I want."
    n 1usqbg "You'd be surprised how much manga time I can sneak in!"
    n 1unmaj "Don't just take my schedule as a rule though.{w=0.5}{nw}"
    extend 1fchbg " Find a balance that works for you, [player]!"
    n 1fslbg "Though I should remind you...{w=0.3} the key word here is {i}balance{/i}."
    n 1fsqsr "I'm not gonna be impressed if you work too much...{w=0.5}{nw}"
    extend 1fnmpo " Or just slack off!"
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1ullbo "Although...{w=0.3} now that I think about it..."
        n 1tsqsm "Perhaps I should timebox our time together,{w=0.1} [player]."
        extend 1uchbs " Ahaha!"

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
    n 1unmbo "Huh?{w=0.2} Do I have a sweet tooth?"

    # Opening response
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fspbg "You bet I do!"
        n 1nsqts "What else were you expecting,{w=0.1} [player]?"
        extend 1fchsm "{w=0.2} Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fllss "Well,{w=0.1} yeah.{w=0.2} Of course I do!"

    else:
        n 1nnmsl "Well...{w=0.3} yeah.{w=0.2} Why wouldn't I?"

    n 1nllaj "Baked stuff is okay,{w=0.1} but I find it gets kinda sickly before long."
    n 1ullaj "But to be completely honest,{w=0.1} if I had a choice?{w=0.5}{nw}"
    extend 1unmbo " Just give me a bunch of candy every time."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1uwdaj "There's so much more variety!{w=0.2} Like...{w=0.3} there's always something for whatever I feel like!"
        n 1tllss "I think if I had to pick a favourite though,{w=0.3}{nw}"
        extend 1fllss " it'd be those fizzy ones."
        n 1fchbg "Just that perfect mix of sweet and sour,{w=0.1} you know?"
        n 1flraj "Jeez...{w=0.5}{nw}"
        extend 1fchts " I can feel my tongue tingling already just thinking about them!"
        n 1fsrts "..."
        n 1flleml "A-{w=0.1}anyway!"
        n 1fcseml "It isn't like I'm snacking on treats all the time though."
        n 1fllpo "I've got way better things to spend my money on."
        n 1fnmss "And...{w=0.3} it's not exactly healthy either.{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    # Closing thoughts
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fsqsm "Though I have to say,{w=0.1} [player]."
        n 1fsqssl "I'm pretty sure you have a sweet tooth too."
        n 1fsrbgl "It'd explain why you're spending so much time with me,{w=0.1} a-{w=0.1}after all."
        n 1fchbgl "Ahaha!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fllbg "I could go for some candy right now,{w=0.1} actually.{w=0.5}{nw}"
        extend 1fslss " But...{w=0.3} I think I'll hold back."
        n 1usqbg "Someone's gotta be a role model to you,{w=0.1} [player].{w=0.2} Am I right?"
        n 1fchsm "Ehehe."

    else:
        n 1nnmbo "..."
        n 1nlrbo "That being said..."
        n 1flrsr "I...{w=0.3} could really use some chocolate right now."
        n 1fsqsr "I'll let {i}you{/i} figure out why,{w=0.1} [player]."

    return

# Natsuki asks about and potentially discovers more about the player's physical appearance
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_appearance",
            unlocked=True,
            prompt="My appearance",
            category=["You"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:
    # Player was asked before, and declined to share their appearance
    if persistent.jn_player_appearance_declined_share:
        n 1unmaj "Huh?{w=0.2} Your appearance?"
        n 1ullaj "If I remember,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
        extend 1tnmbo " you said didn't want to share it with me before."
        n 1tlrbo "Huh. Well..."
        menu:
            n "Did you change your mind,{w=0.1} [player]?"

            "Yes, I want to share my appearance.":
                n 1fcsbg "A-{w=0.1}aha!{w=0.2} I knew you'd come around eventually,{w=0.1} [player].{nw}"
                extend 1fchgn "{w=0.2} Let's not waste any time!"

            "No, I still don't want to share my appearance.":
                n 1nllsl "Oh..."
                n 1unmaj "Well,{w=0.1} it's your call,{w=0.1} [player]."
                n 1unmss "Just let me know if you change your mind again,{w=0.1} alright?"
                return

    # Player has already described themselves to Natsuki
    elif persistent.jn_player_appearance_eye_colour is not None:
        n 1unmaj "Huh?{w=0.2} Your appearance?"
        n 1tllbo "But...{w=0.3} I was sure you already shared that with me,{w=0.1} [player]."
        n 1uspgs "Ooh!{w=0.5}{nw}"
        extend 1unmbg " Did you dye your hair or something?"
        n 1fllbg "Or...{w=0.3} maybe you just made a mistake last time?"
        n 1tslbg "Well...{w=0.5}{nw}"
        extend 1unmbg " either way."
        menu:
            n "Did you want to share your appearance again,{w=0.1} [player]?"

            "Yes, my appearance has changed.":
                n 1fcssm "Aha!{w=0.2} I thought so!"
                n 1fchgn "I can't wait to find out how!"

            "No, my appearance hasn't changed.":
                n 1tnmsr "H-{w=0.1}huh?{w=0.2} Just pulling my leg,{w=0.1} are you?"
                n 1tsrsf "Okaaay..."
                n 1tnmss "Just let me know if you actually {i}do{/i} change something then,{w=0.2} 'kay?"
                return

    # Player has never described themselves to Natsuki, and this is their first time discussing it
    else:
        n 1tlrbo "Huh..."
        n 1tnmbo "You know,{w=0.1} [player].{w=0.2} I just realized something."
        n 1unmaj "You've seen a lot of me,{w=0.1} right?{w=0.5}{nw}"
        extend 1fslssl " B-{w=0.1}by spending time with me here,{w=0.1} I mean."
        n 1ullaj "So...{w=0.3} you kinda know exactly who you're dealing with."
        n 1uwdgs "But I don't have a clue about who {i}I'm{/i} dealing with!"
        n 1fsqsm "And honestly?{w=0.2} You should know me by now.{w=0.5}{nw}"
        extend 1fsqbg " I'm actually pretty curious!"
        n 1nchbg "Don't worry though{w=0.1} -{w=0.1} anything you tell me is staying strictly between us,{w=0.1} obviously!"
        n 1fllsfl "N-{w=0.1}not like anyone else would care {i}that{/i} much,{w=0.1} anyway."
        n 1unmsm "So...{w=0.3} how about it, [player]?"
        menu:
            n "Do you wanna share your appearance with me, [player]?"

            "Sure!":
                n 1uchbsl "Yes!{w=0.5}{nw}"
                extend 1fcsbgl " I-{w=0.1}I mean good!{w=0.5}{nw}"
                n 1fchbg "Let's get started then,{w=0.1} shall we?"

            "I'm not comfortable sharing that.":
                n 1unmsl "Oh..."
                n 1ullaj "That's kind of disappointing to hear,{w=0.1} if I'm being honest."
                n 1nchss "But I totally get it,{w=0.1} [player].{w=0.2} So don't worry,{w=0.1} 'kay?"
                n 1fsqss "You better let me know if you feel like telling me later though!"
                $ persistent.jn_player_appearance_declined_share = True
                return

    n 1uchgn "Okaaay!{w=0.2} Let's start with...{w=0.5}{nw}"
    extend 1fchbg " your eyes!"
    n 1unmbg "They say the eyes are the window to the soul,{w=0.1} so it only makes sense to begin there,{w=0.1} right?"
    n 1flldvl "..."
    n 1fcseml "A-{w=0.1}anyway...!"

    # Eye colour
    menu:
        n "How would you describe your eye colour,{w=0.1} [player]?"

        "Amber":
            n 1unmaj "Ooh!{w=0.2} I don't think I've seen someone with amber eyes before."
            n 1fchbg "That's awesome,{w=0.1} [player]!{w=0.2} I bet those help you stand out,{w=0.1} right?"
            $ persistent.jn_player_appearance_eye_colour = "Amber"

        "Blue":
            n 1unmbg "Blue eyes,{w=0.1} huh?{w=0.2} Cool!"
            n 1fsgsm "I really like how striking they are!"
            $ persistent.jn_player_appearance_eye_colour = "Blue"

        "Brown":
            n 1unmaj "Brown eyes,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fchsm " I'm not complaining!"
            n 1tsqss "Nice and natural,{w=0.1} am I right?{w=0.5}{nw}"
            extend 1uchsm " Ahaha."
            $ persistent.jn_player_appearance_eye_colour = "Brown"

        "Grey":
            n 1unmaj "Oh?{w=0.2} Grey eyes?{w=0.2} Super neat, [player]!"
            n 1tllss "I don't think I've seen anyone with grey eyes before!"
            $ persistent.jn_player_appearance_eye_colour = "Grey"

        "Green":
            n 1fsgbg "Aha!{w=0.2} I had you figured for green eyes,{w=0.1} [player]."
            n 1fsqbg "I bet you're proud of them,{w=0.1} no?{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Green"

        "Hazel":
            n 1unmaj "Ooh!{w=0.2} Hazel,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fsqbg " Classy!"
            n 1tslsm "Hmm...{w=0.3} I wonder if yours are closer to green or brown,{w=0.1} [player]?"
            $ persistent.jn_player_appearance_eye_colour = "Hazel"

        "Mixed":
            n 1unmaj "Wow!{w=0.2} Do you have two different colours or something,{w=0.1} [player]?"
            n 1fchbg "Now if that isn't unique,{w=0.1} I don't know what is!"
            $ persistent.jn_player_appearance_eye_colour = "Mixed"

        "Other":
            n 1unmaj "Oh?{w=0.2} Something a bit off the beaten trail,{w=0.1} huh?"
            n 1tlrss "...Or maybe you just wear contacts a lot?{w=0.5}{nw}"
            extend 1unmsg " Well,{w=0.1} whatever."
            n 1ncsss "I'm sure they look fine either way."
            $ persistent.jn_player_appearance_eye_colour = "Other"

    n 1uchbg "Alright!{w=0.2} That's one down!"
    n 1ullaj "So next,{w=0.1} we have...{w=0.5}{nw}"
    extend 1fchsm " your hair,{w=0.1} of course!"
    n 1nnmsm "We'll just start off with the length for now."
    n 1ullss "Now..."

    # Hair length
    menu:
        n "How would you describe your hair length,{w=0.1} [player]?"

        "Short.":
            n 1ncsss "Ah,{w=0.1} the low maintenance approach{w=0.1} -{w=0.1} I see,{w=0.1} I see.{w=0.5}{nw}"
            extend 1fchbg " Trendy!"
            n 1unmaj "To be honest though,{w=0.1} I totally get it."
            n 1fslpo "I have no idea how you even keep long hair looking good..."
            n 1nslpo "It just seems like way too much effort to me."
            $ persistent.jn_player_appearance_hair_length = "Short"

        "Mid-length.":
            n 1fcsbg "Aha!{w=0.2} The perfect balance,{w=0.1} am I right?"
            n 1fllss "Just long enough for pretty much any style..."
            n 1fchgn "And yet still short enough to suit a lazy day!{w=0.5}{nw}"
            extend 1nchsm " Ehehe."
            n 1flrbgl "I'm glad we think the same way,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "Mid-length"

        "Long.":
            n 1unmbg "Ooh!{w=0.2} Letting it run free,{w=0.1} are we?"
            n 1fcssm "I bet you take super good care of yours."
            n 1fsqsm "I might even have to borrow your products,{w=0.1} [player].{w=0.5}{nw}"
            extend 1nchsm " Ehehe!"
            $ persistent.jn_player_appearance_hair_length = "Long"

        "I don't have any hair.":
            n 1fnmaj "Hey{w=0.1} -{w=0.1} nothing wrong with that!{nw}"
            extend 1fsqbg "{w=0.2} You wanna know why?"
            n 1fchgn "Because it just means you're aerodynamic,{w=0.1} [player].{w=0.5}{nw}"
            extend 1uchsm " Ahaha!"
            $ persistent.jn_player_appearance_hair_length = "None"

    n 1uchbs "Okay!{w=0.5}{nw}"
    extend 1unmbg " I'm really starting to get a picture now."
    n 1fwdgs "We gotta keep the ball rolling,{w=0.1} [player]!"

    # Hair colour
    if persistent.jn_player_appearance_hair_length == "None":
        n 1fllss "You said you didn't have any hair,{w=0.1} right?{w=0.5}{nw}"
        extend 1fllbg " So I think it's kinda pointless talking about hair colour."
        n 1fslbo "Now,{w=0.1} let's see...{w=0.3} what else..."

    else:
        n 1fchsm "Now for your hair colour!"
        n 1unmbg "So,{w=0.1} [player]..."
        menu:
            n "How would you describe your hair colour?"

            "Auburn":
                n 1unmaw "Ooh!{w=0.2} Auburn,{w=0.1} huh?{w=0.5}{nw}"
                extend 1fwdaw " That's awesome,{w=0.1} [player]!"
                n 1fchbg "It's such a warm colour!"
                $ persistent.jn_player_appearance_hair_colour = "Auburn"

            "Black":
                n 1tsgsm "Black,{w=0.1} huh?{w=0.5}{nw}"
                extend 1nchgn " Nice!"
                n 1usqsg "I bet you feel super slick,{w=0.1} huh [player]?"
                $ persistent.jn_player_appearance_hair_colour = "Black"

            "Blond":
                n 1fnmbg "Aha!{w=0.2} A blond,{w=0.1} are we?{w=0.5}{nw}"
                extend 1fsqts " {w=0.3}...That explains a lot."
                n 1fchgn "Ahaha!"
                n 1uchbs "I'm kidding,{w=0.1} [player]!{w=0.2} I'm just kidding!"
                n 1fllbg "I'm actually a little jealous.{w=0.5}{nw}"
                extend 1fsqsm " Just a little."
                $ persistent.jn_player_appearance_hair_colour = "Blond"

            "Brown":
                n 1unmaj "Brown hair,{w=0.1} [player]?{w=0.5}{nw}"
                extend 1nchsm " I'm for it!"
                n 1nchsm "Not too subtle and not too striking,{w=0.1} you know?{w=0.2} It's just right!"
                $ persistent.jn_player_appearance_hair_colour = "Brown"

            "Grey":
                n 1unmaj "Ooh...{w=0.5}{nw}"
                extend 1ullaj " I gotta say...{w=0.5}{nw}"
                extend 1kllbg " I wasn't expecting that!"
                n 1fsqsr "I just hope that isn't from stress,{w=0.1} [player]..."
                n 1fllbg "...Or at least stress from me,{w=0.1} anyway.{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                $ persistent.jn_player_appearance_hair_colour = "Grey"

            "Red":
                n 1fchsm "Ehehe.{w=0.5}{nw}"
                extend 1usqsm " So you're a red head,{w=0.1} [player]?"
                n 1flrajl "Not that there's anything wrong with that,{w=0.1} o-{w=0.1}obviously!"
                n 1fchbg "I bet that gets you some attention,{w=0.1} huh?"
                n 1fsrpo "Better be the good kind,{w=0.1} though."
                $ persistent.jn_player_appearance_hair_colour = "Red"

            "White":
                n 1unmbg "White hair,{w=0.1} huh?{w=0.5}{nw}"
                extend 1uchsm " Neat!"
                $ persistent.jn_player_appearance_hair_colour = "White"

            "Other":
                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1fsqsm " It looks like we're more similar in taste than I thought!"
                n 1fsrss "Though I should probably clarify...{w=0.5}{nw}"
                extend 1uchgn " mine is all natural,{w=0.1} [player]!{w=0.2} Ahaha."
                $ persistent.jn_player_appearance_hair_colour = "Other"

    # Height
    n 1unmbg "Alright!{w=0.2} I think I'm almost done interrogating you now,{w=0.1} [player]."
    n 1fsqsm "Ehehe."
    n 1flrsl "So...{w=0.3} don't tease me when I ask this,{w=0.1} but I gotta know."
    n 1ulrbo "Exactly..."

    $ player_input_valid = False
    while not player_input_valid:
        $ player_input = int(renpy.input(prompt="How tall are you in {i}centimeters{/i},{w=0.2} [player]?", allow="0123456789"))

        # Valid height
        if player_input > 75 and player_input <= 300:
            $ player_input_valid = True
            $ persistent.jn_player_appearance_height_cm = player_input

            if player_input < 149:
                n 1unmgs "H-{w=0.1}huh?{w=0.2} Really?"
                n 1unmaj "You're even shorter than me?"
                n 1flldv "Well,{w=0.1} I wasn't expecting that!"
                n 1fnmbg "Don't worry,{w=0.1} [player].{w=0.2} We're both on the same side,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ehehe."

            elif player_input == 149:
                n 1unmgs "Seriously?{w=0.2} We're the same height?"
                n 1uchbg "That's amazing,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length = "Medium" and persistent.jn_player_appearance_hair_colour = "Other":
                    n 1fllbg "With the hair and everything too..."
                    n 1uchgn "It's like we're practically twins!"

            elif player_input > 149 and player_input < 166:
                n 1unmaj "Oh?{w=0.2} A little on the shorter side,{w=0.1} [player]?"
                n 1fcsss "Don't worry, don't worry!{w=0.5}{nw}"
                extend 1fllpo " I-{w=0.1}I'm not one to judge,{w=0.1} after all."

            elif player_input >= 166 and player_input < 200:
                n 1unmaj "About average height,{w=0.1} [player]?"
                n 1nchsm "No complaints from me!"

            elif player_input >= 200 and player_input < 250:
                n 1unmaj "Oh?{w=0.2} On the taller side [player],{w=0.1} are we?"
                n 1fllbg "I guess I know who to take shopping,{w=0.1} right?{w=0.5}{nw}"
                extend 1nchsm " Ehehe."

            else:
                n 1unmgs "W-{w=0.1}woah!{w=0.2} What the heck,{w=0.1} [player]?{w=0.2} Really?"
                n 1fbkwr "That's crazy tall!"
                n 1tlrem "Though...{w=0.3} actually...{w=0.5}{nw}"
                extend 1knmpo " I hope that isn't actually just inconvenient for you,{w=0.1} though."

        else:
            n 1fllpo "[player]...{w=0.3} please.{w=0.2} Take this seriously,{w=0.1} alright?"

    n 1uchsm "Okaaay!{w=0.2} I think that's everything."
    n 1unmbg "Thanks a bunch,{w=0.1} [player]!"
    n 1fllbg "I know it wasn't a lot,{w=0.3}{nw}"
    extend 1uchgn " but I feel like I know you so much better now!"

    if jn_affinity.get_affinity_state() == jn_affinity.LOVE:
        n 1flldvl "You know,{w=0.1} [player]?{w=0.2} I can just picture it now."
        n 1fnmssl "Meeting you in person somewhere out there,{w=0.1} for the first time..."
        python:
            # Get the descriptor for the eye colour
            if persistent.jn_player_appearance_eye_colour == "Other":
                eye_colour_descriptor = "calm"

            else:
                eye_colour_descriptor = persistent.jn_player_appearance_eye_colour.lower()

            # Get the descriptor for the hair colour
            if persistent.jn_player_appearance_hair_colour == "Other":
                hair_colour_descriptor = "shiny"

            else:
                hair_colour_descriptor = persistent.jn_player_appearance_hair_colour.lower()

        # Comment on hair length and colour, if the player has hair
        if not persistent.jn_player_appearance_hair_length == "None":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n 1fsqsml "Spotting your [hair_length_descriptor] [hair_colour_descriptor] hair in the distance and hunting you down..."

        else:
            n 1fsqsml "Spotting you in the distance and hunting you down..."

        # Comment on height and eye colour
        if persistent.jn_player_appearance_height_cm < 149:
            n 1fllssl "Gazing down into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n 1fllssl "Gazing directly into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n 1fllssl "Gazing upwards into your [eye_colour_descriptor] eyes..."

        n 1fchunl "Uuuuuu..."
        n 1fsqunl "...{w=0.5}{nw}"
        extend 1fllajl " A-ahem!{w=0.2} Anyway..."
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1kllsml "Really.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
        n 1kcsbgl "This seriously meant a lot to me."

    elif jn_affinity.get_affinity_state() == jn_affinity.ENAMORED:
        n 1fsldvl "...And now I know exactly who I should be watching out for."
        n 1fsqssl "So you better watch out,{w=0.1} [player]."
        n 1fcsbgl "Ehehe."

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
    n 1tnmss "Do I drink alcohol?"
    extend 1tllss " Well...{w=0.3} I can't say I've ever tried it."
    n 1nllsr "I just don't think it's something for me."
    n 1ullpu "That being said,{w=0.1} I knew people who {i}did{/i} drink it..."
    n 1kcspu "But...{w=0.3} I'd...{w=0.3} really rather not get into that,{w=0.1} [player]."
    n 1ncssr "Sorry."
    n 1tlrpu "..."
    n 1unmaj "Oh!{w=0.2} That reminds me,{w=0.1} actually!"
    n 1fnmbg "I bet you didn't know,{w=0.1} but guess who just randomly brought some into the club one day?"
    n 1fchgn "...Yuri!"
    n 1tnmbg "Surprised?{w=0.5}{nw}"
    extend 1fcsss " I know,{w=0.1} right?"
    n 1tllss "I mean...{w=0.3} it was just completely out of the blue!"
    n 1uchbs "She just produced it from her bag like it was a book or something."
    n 1unmbo "It wasn't even just some random supermarket stuff either...{w=0.5}{nw}"
    extend 1uwdaj " it looked super expensive too!"
    n 1kllss "Honestly,{w=0.1} I couldn't help myself.{w=0.2} I just burst into laughter."
    n 1ullun "I think it was just how non-chalant it all was,{w=0.1} really."
    n 1nnmsl "Monika didn't look impressed,{w=0.1} though..."
    n 1klrsl "And Sayori...{w=0.3} she just got really upset.{w=0.5}{nw}"
    extend 1klrpu " She was shouting and everything!"
    n 1kcspu "It looked like Yuri put a lot of thought into picking something out,{w=0.1} but she just got yelled at for it..."
    n 1kcssr "I mean...{w=0.5}{nw}"
    extend 1kllsr " I know we shouldn't have had it in there at all,{w=0.1} and Yuri should have known better."
    n 1fslsr "But she didn't deserve all of...{w=0.5}{nw}"
    extend 1kslsr " that."
    n 1kslaj "I think she was just trying to be nice,{w=0.1} you know?"
    n 1unmsr "It's all in the past now,{w=0.1} obviously.{w=0.5}{nw}"
    extend 1kslsr " But...{w=0.3} that doesn't mean I don't still feel bad about it sometimes."
    n 1kcssr "..."
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1kllsr "Hey...{w=0.5}{nw}"
        extend 1knmpu " [player]?"
        n 1klrsr "Can you promise me something?"
        n 1fcssr "It's dumb,{w=0.1} but I don't care."
        n 1nnmsl "It doesn't really matter to me if you drink or not."
        n 1klrpu "But...{w=0.3} if you do?"
        n 1ksqsr "Please just take it all in moderation,{w=0.1} okay?"
        n 1kllsr "I've...{w=0.5}{nw}"
        extend 1fcsan " seen...{w=0.5}{nw}"
        extend 1fcssr " what it can do to people."
        n 1kslsr "...Firsthand."
        n 1ksqsl "You deserve better than that,{w=0.1} [player].{w=0.5}{nw}"
        extend 1kslun " You {i}are{/i} better than that."
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1kcsun "..."
            n 1ksqsml "I love you,{w=0.1} [player]."
            n 1fcssrl "I'm {w=0.3}{i}never{/i}{w=0.3} going to let a bottle get between us."

    else:
        n 1unmsr "Hey,{w=0.1} [player]?"
        n 1nllaj "I don't really care that much if you drink or not."
        n 1ncssr "Just...{w=0.3} go easy on the stuff."
        n 1flleml "B-{w=0.1}but only because I'm not gonna clean up after you!"
        n 1fllss "Ahaha..."
        n 1kllsr "..."

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

    n 1fchdv "Pffft!{w=0.5}{nw}"
    extend 1uchbs " Ahaha!"
    n 1fchgn "What kind of a question is that,{w=0.1} [player]?"
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)

    if already_discussed_driving:
        n 1tllss "I already told you I can't drive,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fchgn " I don't even have a license!"
        n 1kllpo "And even if I wanted to,{w=0.1} I don't think I could afford it..."

    else:
        n 1tllss "Of course I can't drive,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fchgn " I don't even have a license!"
        n 1kllpo "I mean...{w=0.3} even if I wanted to learn,{w=0.1} I don't think I could afford it."

    n 1uskgs "Lessons are super expensive nowadays!"
    n 1fslem "And then there's tests,{w=0.1} insurance,{w=0.1} fuel,{w=0.1} parking...{w=0.5}{nw}"
    extend 1fsqaj " it's actually pretty gross how fast it all adds up."
    n 1nlraj "I think I'd rather stick to public transport and my own two feet."
    n 1unmaj "But what about you,{w=0.1} [player]?"

    # Player has never confirmed if they can/cannot drive
    if persistent.jn_player_can_drive is None:
        menu:
            n "Can you drive?"

            "Yes, and I do currently.":
                n 1uwdaj "Wow..."
                extend 1fsraj " ...{w=0.3}show-off."
                n 1fsqpo "..."
                n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1nchsm " I'm just messing with you."
                n 1unmbg "That's awesome though{w=0.1} -{w=0.1} you just can't beat the convenience of a car,{w=0.1} right?"

                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                    n 1fllbg "But I should probably warn you..."
                    n 1fsgsm "I'm picking the songs for our driving playlist."
                    extend 1uchbg " Ahaha!"

                else:
                    n 1fllbg "Just remember,{w=0.1} [player]..."
                    n 1fsgsm "I call shotgun.{w=0.5}{nw}"

                $ persistent.jn_player_can_drive = True
                return

            "Yes, but I don't right now.":
                n 1unmaj "Oh?{w=0.2} Is something wrong with your car,{w=0.1} [player]?"
                n 1tllbo "Or perhaps...{w=0.3} you just don't own one at the moment?"
                n 1nnmsm "Well,{w=0.1} I'm not one to judge.{w=0.2} I'm sure you manage just fine."
                n 1flrss "Besides,{w=0.1} you're helping the environment too,{w=0.1} right?"

                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                    n 1fsgsm "Thoughtful as always,{w=0.1} [player]."
                    extend 1nchsm " Ehehe."

                $ persistent.jn_player_can_drive = True
                return

            "No, I can't.":
                n 1klrsl "Oh..."
                n 1flrss "Well,{w=0.3}{nw}"
                extend 1fchbg " chin up,{w=0.1} [player]!{w=0.2} It isn't the end of the world."
                n 1usgsg "Don't worry -{w=0.3}{nw}"
                extend 1fsgsm " I'll teach you how to use the bus!"
                n 1uchsm "Ehehe."

                if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                    n 1fllsm "And besides..."
                    n 1fllssl "That just means we can huddle up on the seat together,{w=0.1} [player]."
                    n 1fcsbgl "A dream come true for you,{w=0.1} right?"
                    n 1flldvl "Ehehe."

                else:
                    n 1fchbg "That's what friends are for, [player]!"

                $ persistent.jn_player_can_drive = False
                return

    # Player stated they can drive previously
    elif persistent.jn_player_can_drive:
        menu:
            n "Doing much driving?"

            "Yes, I'm driving frequently.":
                n 1fnmbg "Ah,{w=0.1}  so you're at home on the roads,{w=0.1} are you?"
                n 1ullss "Fair enough I suppose -{w=0.1} just remember to drive safe,{w=0.1} [player]!"

            "I only drive sometimes.":
                n 1ullss "Well hey,{w=0.1} at least you're saving on fuel,{w=0.1} right?{w=0.5}{nw}"
                extend 1ullsm " That doesn't sound like a bad thing to me."
                n 1fchsm "Besides,{w=0.1} it just means you can save the miles for ones you enjoy!"

            "No, I'm not driving much.":
                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1tllbg " That sounds like a bonus to me,{w=0.1} honestly!"
                n 1tnmbg "Just make sure you still get out there if you aren't driving around much though,{w=0.1} 'kay?"

            "No, I can't drive anymore.":
                n 1tnmsl "Oh...{w=0.3} did something happen?"
                n 1kllsl "I'm...{w=0.3} sorry to hear it,{w=0.1} [player]."
                n 1fsgsm "But at least that means more time to hang out with me,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ahaha."
                $ persistent.jn_player_can_drive = False

        return

    # Player admitted they cannot drive previously
    else:
        menu:
            n "Anything new happening with you on the driving front?"

            "I'm learning to drive!":
                n 1fnmss "Ooh!{w=0.5}{nw}"
                extend 1fchbg " Nice,{w=0.1} [player]!"
                n 1fchsm "Don't sweat the test,{w=0.1} alright?{w=0.2} I'm sure you'll do fine!"

                if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                    n 1uchsm "I believe in you,{w=0.1} [player]!"

            "I passed my test!":
                n 1uskgs "No kidding?{w=0.5}{nw}"
                extend 1uchbs " Yaaay!{w=0.2} Congrats,{w=0.1} [player]!"

                if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                    n 1kwmsm "I knew you could do it,{w=0.1} you big dummy!"
                    extend 1kchsm " Ehehe."

                n 1kwmsm "Just make sure you keep up the good habits when you continue learning on your own,{w=0.1} alright?{w=0.2} Ahaha."
                $ persistent.jn_player_can_drive = True

            "I can drive again!":
                n 1uchbg "Hey!{w=0.2} Nice going,{w=0.1} [player]!"
                n 1uwlsm "Drive safe!"
                $ persistent.jn_player_can_drive = True

            "Nope, nothing new.":
                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1nlrss " Well,{w=0.1} fair enough!"
                n 1tnmsm "You and me both then,{w=0.1} in that case?{w=0.5}{nw}"
                extend 1nchsm " Ahaha."

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
    n 1nnmaj "Hey,{w=0.1} [player]..."
    n 1nllaj "This is kinda random,{w=0.1} but..."
    extend 1unmpu " are you into fashion?"
    if jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1fcsbg "I know I am!{w=0.2} Can you tell?"
        extend 1nchsm " Ehehe."

    else:
        n 1nnmpu "I know I am."

    n 1fllpu "But what caught me by surprise is just how much waste there is."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1uwdgs "Seriously,{w=0.1} [player] {w=0.1}-{w=0.1} it's insane!"
        n 1ullaj "People throw away a {i}lot{/i} of clothing...{w=0.5}{nw}"
        extend 1flrem " it's estimated that we toss out around 90{w=0.3} {i}million{/i}{w=0.3} tonnes every year."
        n 1fnman "That's a truck-full every second!{w=0.2} What a waste!"

    else:
        n 1nllbo "It's pretty insane, honestly."
        n 1fnmsl "I remember reading somewhere that we toss out something like 90{w=0.3} {i}million{/i}{w=0.3} tonnes each year."
        n 1fcsan "That's literally a truck-full {i}every{w=0.3} second{/i}."

    n 1fsrem "And we haven't even began to talk about the amount of water used for washing and plastic used for packaging too."
    n 1ksrsr "...Or the conditions some of the workers making our clothes have to put up with."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fcssm "It's actually one of the reasons I began learning how to sew!"
        n 1klrsr "I've...{w=0.3} never had tons of money to buy more clothes anyway,{w=0.1} so I try to reuse and fix up what I can."
        n 1fchbg "But you'd be surprised at what you can pull off with a little creativity!"
        extend 1fcssm " And just a pinch of know-how too,{w=0.1} obviously."
        n 1fchgn "Betcha didn't know my favourite pink skirt was hand-made,{w=0.1} did you?"

    n 1unmaj "I think I've lectured you enough now,{w=0.1} [player],{w=0.1} so I won't keep harping on about it."
    n 1nllpu "But...{w=0.3} the next time you're out shopping for clothes,{w=0.1} or looking through some catalogues online?"
    n 1unmpu "Just spare a thought for the environment,{w=0.1} would you?"

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1kllssl "For me?"
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 1uchsm " Thanks,{w=0.1} [player]!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 1uchsm " Thanks,{w=0.1} [player]!"

    else:
        n 1nllsl "Thanks."

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
        n 1unmaj "Eh?{w=0.2} You want to give me a nickname?"
        n 1fsqsl "Why?{w=0.2} Natsuki not good enough for you?{w=0.2} Is that it?"
        extend 1fsqpu " Huh?{w=0.2} Come on, [player]!{w=0.2} Spit it out!"
        n 1fsqsm "..."
        n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.2} I'm just kidding!"
        extend 1fchsm " Ehehe."
        n 1ullbg "Well...{w=0.3} I don't see why not!"

    # Another nickname is being assigned
    else:

        # Account for strikes
        if persistent.jn_player_nicknames_bad_given_total == 0:
            n 1unmaj "Oh?{w=0.2} You wanna give me another nickname?"
            n 1uchbg "Sure,{w=0.1} why not!"

        elif persistent.jn_player_nicknames_bad_given_total == 1:
            n 1unmaj "You want to give me a new nickname?"
            n 1unmbo "Alright,{w=0.1} [player]."

        elif persistent.jn_player_nicknames_bad_given_total == 2:
            n 1nnmsl "Another nickname,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nllsl " Fine."
            n 1ncsaj "Just...{w=0.3} think a little about what you choose,{w=0.1} 'kay?"

        elif persistent.jn_player_nicknames_bad_given_total == 3:
            n 1nnmsl "Alright,{w=0.1} [player]."
            n 1fsqpu "Just remember.{w=0.3} You've had your final warning about this."
            n 1nsqsl "Don't let me down again."

    # Validate the nickname, respond appropriately
    $ nickname = renpy.input(prompt="What did you have in mind,{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n 1tnmpu "Huh?{w=0.2} You changed your mind?"
        n 1tllpu "Well...{w=0.3} alright then."
        n 1nnmaj "Just let me know if you actually want to call me something else then,{w=0.1} 'kay?"
        return

    else:
        $ nickname_type = jn_nicknames.get_nickname_type(nickname)

    if nickname_type == jn_nicknames.TYPE_INVALID:
        n 1tlraj "Uhmm...{w=0.3} [player]?"
        n 1tnmaj "I don't think that's a nickname at all."
        n 1tllss "I'll...{w=0.3} just stick with what I have now,{w=0.1} thanks."
        return

    elif nickname_type == jn_nicknames.TYPE_LOVED:
        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        n 1uskgsl "O-{w=0.1}oh!{w=0.2} [player]!"
        n 1ulrunl "..."
        n 1fcsbgl "W-{w=0.1}well,{w=0.1} you have good taste,{w=0.1} at least."
        n 1fcssml "[nickname] it is!{w=0.5}{nw}"
        extend 1uchsml " Ehehe."
        return

    elif nickname_type == jn_nicknames.TYPE_DISLIKED:
        n 1fsqbo "Come on,{w=0.1} [player]...{w=0.3} really?"
        n 1fllsl "You knew I'm not gonna be comfortable being called that."
        n 1fcssl "..."
        n 1nlraj "I'm...{w=0.3} just going to pretend you didn't say that,{w=0.1} alright?"
        return

    elif nickname_type == jn_nicknames.TYPE_HATED:
        n 1fskem "W-{w=0.1}what?{w=0.5}{nw}"
        extend 1fscwr " What did you just call me?!"
        n 1fcsan "[player]!{w=0.2} I can't believe you!"
        n 1fcsfu "Why would you call me that?{w=0.5}{nw}"
        extend 1fsqfu " That's {i}awful{/i}!"
        n 1fcspu "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_PROFANITY:
        n 1fskpu "E-{w=0.1}excuse me?!"
        n 1fskfu "What the hell did you just call me,{w=0.1} [player]?!"
        n 1fcsan "..."
        n 1fslan "I seriously can't believe you,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fnman " Why would you do that?{w=0.1} Are you {i}trying{/i} to get on my nerves?!"
        n 1fcspu "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_FUNNY:
        n 1nbkdv "Pffft!"
        n 1uchbs "Ahaha!"
        n 1fbkbs "[nickname]?!{w=0.2} What was that meant to be,{w=0.1} [player]?"
        n 1fbkbs "Well...{w=0.3} you're just lucky I have a healthy sense of humour."
        n 1fsgbg "[nickname] it is,{w=0.1} I guess!{w=0.5}{nw}"
        extend 1fchgn " Ehehe."

        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        return

    elif nickname_type == jn_nicknames.TYPE_NOU:
        show natsuki 1uwlgn zorder JN_NATSUKI_ZORDER
        n 1usqsg "No you~."
        return

    else:
        $ neutral_nickname_permitted = False

        # Check and respond to easter egg nicknames
        if nickname.lower() == "natsuki":
            n 1fllss "Uhmm...{w=0.5}{nw}"
            extend 1tnmdv " [player]?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1fchbg "That's just my normal name,{w=0.1} [chosen_tease]!"
            n 1fcsca "Honestly...{w=0.5}{nw}"
            extend 1ksgsg " sometimes I wonder why I bother."
            n 1unmbg "Well,{w=0.1} I'm not complaining!{w=0.2} If it isn't broke,{w=0.1} don't fix it -{w=0.1} right?"
            n 1nchbg "Ahaha."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n 1kllunl "..."
            n 1fnmssl "D-{w=0.1}dreaming big,{w=0.1} are we,{w=0.1} [player]?"
            n 1klrsrl "Uhmm..."
            n 1klrpol "I'm...{w=0.3} really...{w=0.3} not a fan,{w=0.1} but if it's what you prefer..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n 1fsldv "I...{w=0.3} don't think you thought this through,{w=0.1} [player]."
            n 1tnmbg "Do you even know how confusing that'd be?"
            n 1tlrss "I...{w=0.3} think I'll just stick to what works,{w=0.1} 'kay?{w=0.5}{nw}"
            extend 1fsqsm " Ehehe."
            n 1uchbg "Nice try though!"

        # Fallback for anything not categorised
        else:
            n 1fllsr "Hmm...{w=0.5}{nw}"
            extend 1ullpu " [nickname],{w=0.1} huh?"
            n 1fllss "[nickname]..."
            n 1fnmbg "You know what?{w=0.2} Yeah!{w=0.2} I like it!"
            n 1fchbg "Consider it done,{w=0.1} [player]!{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ neutral_nickname_permitted = True

        # Finally, assign the neutral/easter egg nickname if it was permitted by Natsuki
        if (neutral_nickname_permitted):
            $ persistent.jn_player_nicknames_current_nickname = nickname
            $ n_name = persistent.jn_player_nicknames_current_nickname

        return

    # Handle strikes
    if persistent.jn_player_nicknames_bad_given_total == 1:
        n 1kllsf "Jeez,{w=0.1} [player]...{w=0.3} that isn't like you at all!{w=0.5}{nw}"
        extend 1knmaj " What's up with you today?"
        n 1kcssl "..."
        n 1knmsl "Just...{w=0.3} don't do that again,{w=0.1} okay?"
        n 1fsqsl "That really hurt,{w=0.1} [player].{w=0.2} Don't abuse my trust."

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.JNApologyTypes.bad_nickname)
        $ jn_relationship(change="affinity-", multiplier=2)
        $ jn_relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 2:
        n 1fsqsl "I can't believe you did that again to me,{w=0.1} [player]."
        n 1fsqan "I told you it hurts,{w=0.1} and you went ahead anyway!"
        n 1fcsan "..."
        n 1fcsun "I...{w=0.3} really...{w=0.3} like you, [player].{w=0.5}{nw}"
        extend 1kllun " It hurts extra bad when it's you."
        n 1fsqsr "Don't test my patience like this.{w=0.2} You're better than that."

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.JNApologyTypes.bad_nickname)
        $ jn_relationship(change="affinity-", multiplier=2)
        $ jn_relationship(change="trust-", multiplier=2)

    elif persistent.jn_player_nicknames_bad_given_total == 3:
        n 1fsqan "You are honestly unbelievable,{w=0.1} [player]."
        n 1fnmfu "I've told you so many times now,{w=0.1} and you still won't knock it off!"
        n 1fcspu "..."
        n 1fsqpu "No more warnings,{w=0.1} [player]."
        menu:
            n "Understand?"

            "I understand. Sorry, [n_name].":
                n 1fsqsr "You understand,{w=0.1} do you?"
                n 1fsqan "...Then start acting like it,{w=0.1} [player]."
                n 1fslsl "Thanks."

                $ jn_relationship(change="affinity-", multiplier=2)
                $ jn_relationship(change="trust-", multiplier=2)

            "...":
                n 1fcssl "Look.{w=0.2} I'm not kidding around,{w=0.1} [player]."
                n 1fnmpu "Acting like this isn't funny,{w=0.1} or cute."
                n 1fsqem "It's toxic."
                n 1fsqsr "I don't care if you're trying to pull my leg.{w=0.2} Quit it."

                $ jn_relationship(change="affinity-", multiplier=3)
                $ jn_relationship(change="trust-", multiplier=3)

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.JNApologyTypes.bad_nickname)

    elif persistent.jn_player_nicknames_bad_given_total == 4:
        # Player is locked out of nicknaming; this is why we can't have nice things
        n 1fcsan "Yeah,{w=0.1} no.{w=0.2} I've heard enough.{w=0.2} I don't need to hear any more."
        n 1fnmem "When will you learn that your actions have consequences?"
        n 1fcspu "..."
        n 1fnmpu "You know what?{w=0.5}{nw}"
        extend 1fsqpu " Don't even bother answering."
        n 1fsqsr "I warned you,{w=0.1} [player].{w=0.2} Remember that."

        # Apply affinity/trust penalties, then revoke nickname priveleges and finally apply pending apology
        $ jn_relationship(change="affinity-", multiplier=5)
        $ jn_relationship(change="trust-", multiplier=5)
        $ persistent.jn_player_nicknames_allowed = False
        $ persistent.jn_player_nicknames_current_nickname = None
        $ n_name = "Natsuki"
        $ jn_apologies.add_new_pending_apology(jn_apologies.JNApologyTypes.bad_nickname)

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
    n 1fllpu "Huh..."
    n 1fllpu "Hey,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nnmaj " Let me ask you a question,{w=0.1} 'kay?"
    n 1fsqsr "How do you sleep at night?"
    n 1fsqpu "Be honest.{w=0.2} How do you do it?"
    n 1ksqsm "..."
    n 1fchsm "Ehehe.{w=0.2} Did I get you?"
    n 1unmaj "But seriously,{w=0.2} [player].{w=0.5}{nw}"
    extend 1tnmaj " Do you struggle with your sleep?"

    # Quip if the player has been around a while, or has admitted they're tired
    if jn_utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n 1fsqpo "I mean,{w=0.1} you {i}have{/i} been here for a while now..."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " I kinda figured you might be feeling a little sleepy anyway."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1fllpo "I mean,{w=0.1} you even {i}said{/i} you were tired before."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " it only makes sense to ask,{w=0.1} right?{w=0.2} Anyway..."

    n 1nnmaj "I'll admit,{w=0.1} I get the odd sleepless night myself.{w=0.5}{nw}"
    extend 1fbkwr " It's the worst!"
    n 1fllem "There's nothing I hate more than tossing and turning,{w=0.3}{nw}"
    extend 1fcsan " just waiting for my body to decide it's time for tomorrow to happen."
    n 1ullaj "But...{w=0.5}{nw}"
    extend 1fnmss " you know what they say,{w=0.1} [player]."
    n 1fcsss "With suffering...{w=0.5}{nw}"
    extend 1uchbg  " ...comes wisdom!"
    n 1nsqbg "And luckily for you,{w=0.1} I don't mind sharing.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."
    n 1fcsbg "So,{w=0.1} listen up -{w=0.1} it's time for another lesson from yours truly!"
    n 1fnmaj "Alright -{w=0.1} first,{w=0.1} cut the crap!{w=0.2} If you're trying to sleep,{w=0.1} anything high-sugar or high-caffeine is your enemy."
    n 1fllss "So before anything else,{w=0.1} ditch the soda and coffee.{w=0.2} You can thank me later."
    n 1fcsaj "Next up -{w=0.1} no screens!{w=0.5}{nw}"
    extend 1fsqpo " Including this one, [player]."
    n 1unmsl "No screen means no bright lights or distractions to keep you up,{w=0.1} obviously."
    n 1fnmpu "If you're tired then the last thing you need is something beaming whatever at you."

    if jn_activity.has_player_done_activity(jn_activity.JNActivities.anime_streaming):
        n 1tsqsr "And no, [player] {w=0.1}-{w=0.3}{nw}"
        extend 1fnmpo "No late-night anime binging sessions either."
        n 1nchgn "Sorry~!"

    n 1fcsbg "Moving on, next is temperature!{w=0.2} If it's hot,{w=0.1} use thinner sheets and vice versa."
    n 1fcspu "Nothing disrupts your sleep more than having to rip off blankets,{w=0.1} or pull some out."
    n 1fsgsg "Keeping up with me so far,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1fchgn " I'm almost done,{w=0.1} don't worry."
    n 1unmaj "Lastly...{w=0.5}{nw}"
    extend 1fchbg " get comfortable!"
    n 1nnmsm "Make sure you have enough pillows to support your head,{w=0.1} or maybe even play some quiet music if you find that helps."
    n 1fcssm "...And that's about it!"
    n 1nllss "You should have known at least a few of those already,{w=0.3}{nw}"
    extend 1unmss " but at any rate..."
    n 1fwlbg "I hope you can rest easy with your newfound knowledge,{w=0.1} [player]!"
    n 1uchsm "Ehehe."

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
    n 1unmaj "You know,{w=0.1} [player]..."
    n 1nllpu "I think most people share a bunch of fears."
    n 1unmpu "You get what I mean,{w=0.1} right?{w=0.2} Like presenting stuff to a room full of people,{w=0.1} or failing a test."
    n 1tlrss "Of course,{w=0.1} it's rare to find one that {i}everyone{/i} has..."
    n 1tnmaj "Or at least something that makes anyone feel uneasy."
    n 1unmbg "But...{w=0.3} I think I found one!"
    n 1usgsm "What am I thinking of,{w=0.1} you ask?"
    n 1ullaj "Well...{w=0.3} it's actually kinda boring,{w=0.1} really."
    n 1nnmbo "I was actually thinking about growing older."
    n 1unmpu "Have you ever thought much about it,{w=0.1} [player]?"
    n 1fllbg "It's probably the last thing on your mind if you're pretty young."
    n 1nwmpu "But I think as you actually get older,{w=0.1} it starts to creep in."
    n 1kllpu "You might have less energy,{w=0.1} or friends and family begin drifting away..."
    n 1knmem "Birthdays lose all meaning -{w=0.1} you might even dread them!"
    n 1ullaj "The signs appear in a bunch of ways,{w=0.3}{nw}"
    extend 1knmsl " but that's what makes it unnerving."
    n 1kllaj "Everyone experiences it differently,{w=0.3}{nw}"
    extend 1kskaw " and we don't even know what happens after the end!"
    n 1klrss "Spooky,{w=0.1} huh?"
    n 1ulrpu "Although...{w=0.3} I guess you could say that's more the fear of the unknown than aging itself."
    n 1flraj "What does wind me up though is how immature people can be about it."
    n 1fnmaj "Especially when it comes to relationships between different ages!"
    n 1fslsf "People just get so preachy about it..."
    n 1fllaj "Like...{w=0.3} as long as they're both happy,{w=0.3}{nw}"
    extend 1fnmem " and nobody is being hurt or made uncomfortable,{w=0.1} who actually cares?"
    n 1nlrpu "It's just like most stuff,{w=0.1} really."
    n 1unmaj "Besides,{w=0.1} it's not like being a certain age means you {i}have{/i} to be a certain way."
    n 1fchbg "I mean...{w=0.3} look at Yuri!"
    n 1uchgn "Being all old-fashioned like that -{w=0.1} you'd think she's retired!"
    n 1nllbg "But anyway...{w=0.3} I think we got side-tracked."
    n 1unmss "I don't really care how old you are,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1klrpol "Y-{w=0.1}you better know that I love you all the same,{w=0.1} [chosen_tease]."
        n 1knmpol "Don't forget that,{w=0.1} 'kay?"
        n 1flrpol "I'll get mad if you do.{w=0.5}{nw}"
        extend 1klrbgl " Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fllbgl "You've been pretty awesome to me all the same."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1fchbgl "You're always fun to hang around with!"

    else:
        n 1fllbg "But...{w=0.3} just in case?"
        n 1fsqsg "We're only having one candle on your birthday cake.{w=0.2} Sorry.{w=0.5}{nw}"
        extend 1uchbg " Ahaha!"

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
        n 1ullaj "You know,{w=0.1} [player]..."

    n 1nnmaj "I think it's pretty easy to let your academic or work life creep into your personal time nowadays."
    n 1nlrsl "I mean...{w=0.3} think about it."
    n 1nnmsl "With everyone having mobile phones,{w=0.1} plus usually some kinda computer at home -{w=0.1} it's hard not to be connected somehow."
    n 1flrbo "And like...{w=0.3} if there's already that connection,{w=0.1} then what's to stop work from bugging you during your time off?"
    n 1fsrbo "Or classmates asking for help at the last possible minute?"

    if jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        n 1fcsem "It just gets annoying -{w=0.1} like everyone expects you to always be around to chip in a little more,{w=0.1} or get something done!"
        n 1fnmpo "Overwhelming,{w=0.1} right?"
        n 1fllaj "Huh.{w=0.2} Actually...{w=0.3} now that I think about it..."
        n 1fnmsf "It isn't like that kind of intrusion is only limited to when you're away either."
        n 1fslpu "I've heard {i}way{/i} too many stories of people doing stupid amounts of overtime at work...{w=0.5}{nw}"
        extend 1fnman " sometimes not even paid!"
        n 1fsran "Or even students studying late into the night until they collapse...{w=0.3} it's crazy!"

    else:
        n 1fsqpu "It just gets annoying -{w=0.1} everyone expects you to always be around to do more."
        n 1fslsl "Actually,{w=0.1} now that I think about it..."
        n 1fcsaj "It isn't like that kind of thing is only limited to when you're away either."
        n 1fsrsr "I've heard too many stories of people doing stupid amounts of overtime at work.{w=0.5}{nw}"
        extend 1fsqan " Often not even paid."
        n 1fslem "Or even students studying late into the night until they collapse..."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1kcsem "Ugh...{w=0.3} I just wish people would value their own time more."
        n 1klrsr "..."
        n 1unmaj "Hey,{w=0.1} [player]..."
        n 1nllaj "I don't know if you're working,{w=0.1} or studying,{w=0.1} or what..."
        n 1fnmsf "But you better not be letting whatever it is take over your life.{w=0.2} Understand?"

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1knmpu "You are {i}more{/i} than your career,{w=0.1} or your education.{w=0.2} You have your own wants and needs that matter too."
            n 1kllun "I don't want some dumb job or stupid assignment to take over your life."
            n 1fcsun "You're...{w=0.3} way more important than either of those,{w=0.1} [player].{w=0.2} Trust me."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1fllun "Besides..."
                n 1fllssl "You and your time are mine first, [player]."
                n 1flldvl "I already called dibs,{w=0.1} a-{w=0.1}after all.{w=0.5}{nw}"
                extend 1fchsml " Ehehe..."

        else:
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1kllpo "People are more than what they do for a living,{w=0.1} after all.{w=0.2} And that includes you too, [chosen_tease]!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fllsr "Makes me wish people would value their own time more."
        n 1fnmsr "...I guess that includes you too,{w=0.1} [player]."
        n 1fllpu "You've got better things to do."
        n 1fsqsf "...Like being a decent friend to others for a change.{w=0.2} Am I right?"

    else:
        n 1fslbo "People need to value their own time more,{w=0.1} I guess."
        n 1fcssl "...Heh."
        n 1fcsun "Maybe I should follow my own advice..."
        n 1fsqfu "Because {i}clearly{/i} being here is a waste of my time too."

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
    n 1unmaj "..."
    n 1tnmaj "...?"
    n 1fnmaw "...!"
    n 1fbkwr "...[player]!"
    n 1fnmpo "[player]!{w=0.2} Finally!{w=0.2} Can you hear me now?"
    n 1fllpo "Jeez...{w=0.3} took you long enough!"
    n 1fslsm "..."
    n 1uchbg "Ehehe."
    n 1fnmbg "Admit it,{w=0.1} [player]!{w=0.2} I'll get you one of these days."
    n 1nnmaj "Seriously though -{w=0.1} do you use headphones or anything like that often?"
    n 1nlrpo "I'll admit,{w=0.1} I probably use mine more than I should."
    n 1fnmaj "I was kinda joking about the whole hearing thing,{w=0.1} but this is important,{w=0.1} [player]."
    n 1nlrss "I like cranking it up too -{w=0.1} just don't make a bad habit of it."
    n 1unmsl "There's even warnings in some countries if you have the volume up too loud..."
    n 1fllem "...And for a good reason!"
    n 1fnmpo "Not just to protect your ears either -{w=0.1} you better be careful wearing them out and about too."
    n 1fcsem "I don't wanna hear about you getting knocked over because you didn't hear something coming!"
    n 1unmbo "Oh -{w=0.1} and one last thing,{w=0.1} actually."
    n 1unmpu "You might wear them to focus at work or relax at home -{w=0.1} and that's fine!"
    n 1nnmsr "But please,{w=0.1} [player]."
    n 1flrsr "...Take them off every once and a while,{w=0.1} will you?{w=0.2} For other people,{w=0.1} I mean."
    n 1ncsbo "I get it -{w=0.1} if you just wanna listen to something in peace,{w=0.1} or give yourself some room,{w=0.1} that's okay."
    
    if jn_activity.has_player_done_activity(jn_activity.JNActivities.music_applications):
        n 1kslbg "I know you like your music streaming."
    
    n 1nsqbo "But don't use them to barricade yourself away from everyone and everything."
    n 1ksrsl "It's...{w=0.3} not healthy to do that either,{w=0.1} [player]."
    n 1nchsm "...And that's about all I had to say!"
    n 1fchbg "Thanks for {i}hearing{/i} me out,{w=0.1} [player]!{w=0.2} Ehehe."
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
        n 1unmaj "You know,{w=0.1} [player]..."
        n 1tllaj "I don't think I ever actually explained why I dislike horror so much."
        n 1tlrss "I know I mentioned it before,{w=0.1} but I was kinda caught off guard at the time."
        n 1unmaj "Honestly?"
        n 1nnmsm "Everyone has their tastes,{w=0.1} right? And I can get why people enjoy it."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nllbo "I don't think I explained why I dislike horror."
        n 1nnmsl "I get everyone has their tastes,{w=0.1} but I don't care for it."

    else:
        n 1kslsl "..."
        n 1fsqaj "...I was about to share some of my thoughts on horror with you."
        n 1fsrsl "Or at least,{w=0.1} I was thinking about it."
        n 1fnmaj "...But then do you know what I realized,{w=0.1} [player]?"
        n 1fsqsf "I hate horror -{w=0.1} not that you'd care -{w=0.1} and honestly?"
        n 1fcsun "Being stuck here with {i}you{/i} is horror enough."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fchbg "Like Yuri!"
        n 1fcsss "It's suspenseful,{w=0.1} and fears are a super powerful motivator for characters!"
        n 1ullpu "So don't get me wrong{w=0.1} -{w=0.1} I can totally appreciate the effort that goes into it."
        n 1fllpol "...When it isn't just stupid jumpscares,{w=0.1} a-{w=0.1}anyway."

    else:
        n 1ullpu "I get the effort that goes into it.{w=0.2} For the most part."

    n 1nllpu "But..."
    n 1nnmbo "When I read something -{w=0.1} or watch something -{w=0.1} I'm doing it because for me,{w=0.1} it's how I relax."
    n 1fllbo "I don't want to be made to feel uneasy."
    n 1fllpu "I don't want to be made to jump."
    n 1fllsr "I don't want to have to see gross stuff."
    n 1fcssr "I...{w=0.3} just want to sit back,{w=0.1} feel good and just escape for a while."
    n 1fnmsl "There's more than enough nasty things going out there already,{w=0.1} you know?"
    n 1flrpu "Some things closer to home than others."
    n 1fcssl "..."
    n 1nnmaj "So...{w=0.3} yeah.{w=0.1} That's about all I had to say about it."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1unmss "Though...{w=0.3} if you want to put something on,{w=0.1} [player]?{w=0.2} Go ahead."
        n 1fllssl "If it's you,{w=0.1} I {i}think{/i} I can deal with it."
        n 1flrpol "But...{w=0.3} we're keeping the volume low.{w=0.2} Got it?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1nnmaj "Don't mind me though,{w=0.1} [player].{w=0.2} If you wanna watch something,{w=0.1} go for it."
        n 1flrcal "But you're watching it solo."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1flrsl "..."
        n 1fnmpu "I {i}would{/i} ask that if you were gonna watch something like that,{w=0.1} then to warn me first."
        n 1fsqsr "But you wouldn't listen to me anyway,{w=0.1} would you?"

    return

# Natsuki discusses her gaming habits
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_gaming",
            unlocked=True,
            prompt="Are you into video games?",
            category=["Games", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_gaming:
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "Gaming?"
        n 1fcsbg "Well...{w=0.3} duh!"
        n 1fnmbg "You bet I'm into gaming,{w=0.1} [player]!"
        n 1ullss "I wouldn't say I'm the most active player...{w=0.2} but I definitely do my share of button mashing."
        n 1nslsg "Hmm..."
        n 1tnmss "I don't think I even need to ask,{w=0.1} but..."
        menu:
            n "What about you,{w=0.1} [player]?{w=0.2} Do you play often?"

            "Absolutely!":
                $ persistent.jn_player_gaming_frequency = "High"
                n 1fcsbg "Yep!{w=0.2} Just as I suspected..."
                n 1uchgn "[player] is a mega-dork."
                n 1uchbs "Ahaha!"
                n 1uchsm "Relax,{w=0.1} [player]!"
                n 1fllssl "I'm not much better,{w=0.1} after all."

            "I play occasionally.":
                $ persistent.jn_player_gaming_frequency = "Medium"
                n 1fsqsm "Yeah,{w=0.1} yeah.{w=0.2} Believe what you want to believe,{w=0.1} [player]."
                n 1usqbg "I'm not sure I buy it,{w=0.1} though."

            "I don't play at all.":
                $ persistent.jn_player_gaming_frequency = "Low"
                n 1tnmaj "Huh?{w=0.2} Really?"
                n 1tllaj "Not even the odd casual game?"

                if jn_activity.has_player_done_activity(jn_activity.JNActivities.gaming):
                    n 1fsqts "Liar.{nw}"

                n 1ncsaj "...Well then."
                n 1fnmbg "It looks like I've got a lot to teach you,{w=0.1} [player]!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmsl "Huh?{w=0.2} Video games?"
        n 1nslsl "Yeah,{w=0.1} I guess.{w=0.2} For what that's worth to you."

    else:
        n 1nsqsl "Video games...?"
        n 1fsqsl "...Heh.{w=0.2} Why,{w=0.1} [player]?"
        n 1fcsan "Was stomping all over my feelings not enough?"
        n 1fsqfu "Or were you looking to see if you can stomp all over me in games too?"
        n 1fslsl "..."
        n 1fslaj "...I don't wanna talk about this any more.{w=0.2} We're done here."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1ullaj "Anyway,{w=0.1} putting that aside..."
        n 1nsgbg "When it comes to my preferences?{w=0.2} I want challenge in my games!"
        n 1fcsbg "I play for the win{w=0.1} -{w=0.1} it's me versus the developers,{w=0.1} and they're not around to stop me!"
        n 1fchbg "Ahaha."
        n 1ullss "I'm actually more into my roguelikes,{w=0.1} to be honest."
        n 1fnmsm "Heh.{w=0.2} Are you surprised,{w=0.1} [player]?"
        n 1fcsbg "Tough as nails,{w=0.1} and I gotta think on my feet{w=0.1} -{w=0.1} plus it's super satisfying learning everything too."
        n 1fchsm "And with how random everything is,{w=0.1} they always feel refreshing and fun to play!"
        n 1fnmbg "Every time I load one up,{w=0.1} I have no idea what I'm up against...{w=0.3} and that's what makes them addicting!"
        n 1fcssm "Ehehe.{w=0.2} Don't worry though, [player]."
        n 1fcsbg "I don't know if you're into that kind of stuff as well,{w=0.1} but..."

        if persistent.jn_player_gaming_frequency == "High":
            n 1fchgn "There's still plenty I can teach you!"

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1ksqsml "And I bet you'd like that too,{w=0.1} huh?"
                n 1nchbg "Ahaha."

            elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n 1fchbg "And I'm not gonna take 'No' for an answer!"

        elif persistent.jn_player_gaming_frequency == "Medium":
            n 1fsqsm "I don't mind showing you how it's done."
            n 1fchbg "I {i}am{/i} a professional,{w=0.1} after all!"

        else:
            if jn_activity.has_player_done_activity(jn_activity.JNActivities.gaming):
                n 1fsqts "Liar.{nw}"

            n 1ullaj "Well then...{w=0.5}{nw}"
            extend 1usqsm " I'm sure I can get {i}you{/i} of all people into it."

    else:
        n 1nnmsl "I suppose I look for challenge in my games more than anything."
        n 1nllsl "It's fun pitting myself against the developers and beating them at their own game."
        n 1nsqaj "I guess I could say I like being tested -{w=0.1} so long as I'm in control of it,{w=0.1} that is."
        n 1fsqbo "What does that mean?{w=0.2} I guess I'll spell it out for you,{w=0.1} [player]."
        n 1fsqan "I really {i}don't{/i} like the kind of testing you're doing."

    return

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
    n 1nllbo "..."
    n 1unmaj "Eh?{w=0.2} What's up,{w=0.1} [player]?"
    n 1unmsl "..."
    n 1tnmaj "What?{w=0.2} Is there something on my face?"
    n 1tnmca "..."
    n 1uwdaj "Oh.{w=0.2} Yeah.{w=0.2} I get it."
    n 1nsqss "Just can't help but notice the fang,{w=0.1} right?{w=0.2} Ehehe."
    n 1nllss "You know..."
    n 1nnmaj "I wasn't always happy with my teeth,{w=0.1} [player]."
    n 1flran "I used to be pretty self conscious about them.{w=0.2} People would just keep pointing them out all the time."
    n 1fcsaj "It wasn't...{w=0.3} {i}bad{/i} or anything...{w=0.3} a little annoying at first,{w=0.1} but nothing over the top."
    n 1kslsf "...Mostly."
    n 1ulrsl "But...{w=0.3} I guess I just came to embrace them?"
    n 1fchbg "They're like a trademark or something now!{w=0.2} Which is why I take good care of them."
    n 1fnmsf "You better not be slacking off on yours,{w=0.1} [player]!"
    n 1fnmaj "And I don't just mean skipping the odd brush,{w=0.1} either..."
    n 1fsgss "Yeah.{w=0.2} We both know what's coming,{w=0.2} don't we?"
    n 1fsqbg "When's the last time {i}you{/i} flossed,{w=0.1} [player]?{w=0.2} Be honest."
    n 1tsqsm "..."
    n 1fchbg "Ahaha!{w=0.2} Did I call you out?"
    n 1nlrss "Well,{w=0.1} whatever.{w=0.2} I'm just gonna assume you'll go do that later."
    n 1fcsaw "Seriously though.{w=0.2} You better make sure you take care of your teeth!"
    n 1fnmaj "Regular brushing and flossing is important,{w=0.1} but watch your diet too."
    n 1fllsl "Not flossing isn't great,{w=0.1} but constant sugary drinks are even worse!"
    n 1fsgsm "Remember,{w=0.1} [player] -{w=0.1} if you ignore them,{w=0.1} they'll go away~."
    n 1nllss "But no, seriously."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1kllss "Smiles look good on you,{w=0.1} [chosen_endearment]."
        n 1fnmsm "Let's keep them looking that way."
        n 1uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fnmsml "I think smiles look good on you,{w=0.1} [player]."
        n 1fchbgl "Let's keep them looking that way!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1usqbg "The right smile can make all the difference,{w=0.1} you know.{w=0.2} Just look at mine!"
        n 1uchgn "Ehehe."

    else:
        n 1unmaj "If you don't look after them?"
        n 1fllajl "I'm not holding your hand at the dentist!"

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
            n 1uscemf "O-{w=0.1}o-{w=0.1}oh my gosh..."
            n 1uskemf "[player_initial]-{w=0.2}[player]...{w=0.3} y-{w=0.1}you...!"
            n 1fcsanf "Nnnnnnn-!"
            n 1fbkwrf "W-{w=0.1}well it took you long enough!{w=0.2} What did you think you were doing?!"
            n 1flrwrf "I bet you were just waiting for me to say it first!"
            n 1fllemf "Jeez,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
            n 1kllemf "But..."
            n 1fcswrf "B-{w=0.1}but...!"
            n 1flranf "Uuuuuuu-!"
            n 1fchwrf "Oh,{w=0.1} whatever!{w=0.2} I don't care!{w=0.2} I gotta say it!{w=0.2} I gotta say it!"
            n 1kwdemf "[player]!{w=0.2} I love you too!"
            n 1kchbsf "I-{w=0.1}I love...{w=0.3} you too..."
            n 1kplbgf "I...{w=0.3} I..."
            n 1kchsmf "..."
            n 1kwmsmf "I love you,{w=0.1} [player]..."
            n 1kllsml "..."
            n 1kskemf "S-{w=0.1}sorry...!"
            n 1klrunf "I...{w=0.3} think I got a little carried away..."
            n 1kcssmf "..."
            n 1knmajf "..."
            n 1kbkemf "J-{w=0.1}jeez!{w=0.2} Stop looking at me like that already!"
            n 1fllemf "W-{w=0.1}we're both on the same page now,{w=0.1} so..."
            n 1kllbof "...{w=0.3}T-that's all I had."
            n 1kllsmf "..."
            n 1kllssf "S-{w=0.1}so..."
            n 1kplssf "Where were we?{w=0.2} Ehehe..."
            $ jn_relationship(change="affinity+", multiplier=3)

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uscgsf "[player_initial]-{w=0.2}[player]!"
            n 1fskgsf "Y-{w=0.1}you...!"
            n 1fcsanf "Nnnnn-!"
            n 1fbkwrf "I-{w=0.1}I know we've been seeing each other a while,{w=0.1} but this is way too sudden!"
            n 1fllwrf "Now you've gone and made it super awkward,{w=0.1} [player]!{w=0.2} Why'd you have to go do that?!"
            n 1fcsemf "Sheesh!"
            n 1fslpof "...I hope you're happy."
            n 1fsqunf "..."
            n 1fnmpof "D-{w=0.1}don't think this means I {i}hate{/i} you or anything,{w=0.1} though..."
            n 1flreml "It's just that...{w=0.3} It's just..."
            n 1fcsanl "Uuuuuu..."
            n 1flrbol "N-{w=0.1}never mind..."
            n 1fcseml "Forget I said anything."
            n 1kllbof "..."
            $ jn_relationship(change="affinity+", multiplier=2)

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1uskwrf "W-{w=0.1}w-{w=0.1}what?"
            n 1fwdwrf "D-{w=0.1}did you just...?"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fbkwrf "[player_initial]-{w=0.2}[player]!"
            n 1fcsemf "Are you trying to give me a heart attack?!{w=0.2} Jeez!"
            n 1fllemf "You can't just say stuff like that so suddenly..."
            n 1kllunf "..."
            n 1fllajf "I-{w=0.1}I mean..."
            n 1flranf "It's not that I {i}don't{/i} like you,{w=0.1} o-{w=0.1}or anything,{w=0.1} but..."
            n 1fslanf "But...!"
            n 1fcsanf "Uuuuu..."
            n 1fcsajf "F-{w=0.1}forget it!{w=0.2} I-{w=0.1}it's nothing..."
            n 1kslslf "..."
            $ jn_relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            n 1fsqdvl "Pffffft!"
            n 1uchbsl "Ahaha!"
            n 1tllbgl "You can't be serious,{w=0.1} [player]!{w=0.2} You're just messing with me!{w=0.2} Right?"
            n 1knmbgl "Right,{w=0.1} [player]?"
            n 1knmajf "R-{w=0.1}right...?"
            n 1fllunf "..."
            n 1fcsgsf "J-{w=0.1}jeez!{w=0.2} Enough of this!"
            n 1fsqajf "You really shouldn't mess around with girls like that,{w=0.1} [player]!"
            n 1fslpul "Y-{w=0.1}you're just lucky I've got a great sense of humour."
            n 1fnmpol "S-{w=0.1}so it's fine...{w=0.3} this time..."
            n 1fcsajl "Just...{w=0.3} think a little before you just blurt stuff out!{w=0.2} Sheesh."
            n 1fllslf "[chosen_tease.capitalize()]..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n 1fscgsf "Urk-!"
            n 1fskanf "W-{w=0.1}what did you..."
            n 1fwdanf "Did you just...?"
            n 1fllajl "..."
            n 1fcsbgf "A-{w=0.1}aha!{w=0.2} I mean...{w=0.3} y-{w=0.1}yeah!{w=0.2} Who wouldn't love me,{w=0.1} right?"
            n 1fllbgf "My wit,{w=0.1} my style,{w=0.1} my killer sense of humour...{w=0.3} I've got it all.{w=0.1} Yeah..."
            n 1fbkwrf "D-{w=0.1}don't get the wrong idea or a-{w=0.1}anything, though!"
            n 1fllssf "I-{w=0.1}I mean,{w=0.1} I'm just glad you have some good taste."
            n 1fllunf "Yeah..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            n 1fcsan "..."
            n 1fnmfu "Seriously,{w=0.1} [player]?{w=0.2} You're really going to say that to me {i}now{/i}?"
            n 1fsqfu "The first time you choose to say it...{w=0.3} and you say it {i}now{/i}?"
            n 1fcspu "..."
            n 1fwman "...And you really think I'm gonna buy that {i}now{/i},{w=0.1} [player]?"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "We're done with this."
            n 1fsqpu "And if you {i}really{/i} feel that way?"
            n 1fsqsf "...Then why aren't {i}you{/i} trying to make this work,{w=0.1} [player]?"
            $ jn_relationship("affinity-")

        else:
            # :(
            n 1fsqpu "..."
            n 1fcsun "Y-{w=0.1}you..."
            n 1fcsan "You...{w=0.3} h-{w=0.1}how...!"
            n 1fscwr "H-{w=0.1}how {i}dare{/i} you tell me that now!"
            n 1fscfu "{i}How {w=0.3} dare {w=0.3} you.{/i}"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "You knew how I felt,{w=0.1} [player]..."
            n 1fcsan "You knew for such a long time..."
            n 1fsqfu "And now?{w=0.2} {i}Now{/i} is when you tell me?"
            n 1fsqup "For the {i}first time{/i}?"
            n 1fcsup "..."
            n 1kplan "I...{w=0.3} I c-{w=0.1}can't do this right now."
            n 1kcsan "It...{w=0.5} it hurts..."
            n 1kcsfu "..."
            n 1fcspu "Get out of my sight,{w=0.1} [player]."
            n 1fcsan "..."
            n 1fsqfu "Go!"
            n 1fscsc "{i}Just leave me alone!{/i}{nw}"
            $ jn_relationship(change="affinity-", multiplier=10)
            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1

    # Standard flows
    else:
        $ persistent.jn_player_love_you_count += 1
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:

            # At this point, Natsuki is super comfortable with her player, so we can be open and vary things!
            $ random_response_index = random.randint(0, 11)

            if random_response_index == 0:
                n 1unmbgf "Ehehe.{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "You're always [chosen_descriptor] to me."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 1:
                n 1tsqssl "Aww,{w=0.1} you don't say?"
                n 1uchbsl "Ahaha!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n 1kwmbgf "[chosen_endearment],{w=0.1} I love you too!"
                n 1fcsbgf "I'll always be here to stick up for you."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 2:
                n 1uchsmf "Aww,{w=0.1} [chosen_endearment]!{w=0.2} I love you too!"
                n 1klrbgf "You're the best thing that's ever happened to me."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 3:
                n 1ksqbgf "Oh?{w=0.2} Someone's all needy today,{w=0.1} huh?"
                n 1fsqsmf "Well,{w=0.1} I'd be happy to oblige!"
                n 1uchsmf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1fchbgf "Keep on smiling for me,{w=0.1} 'kay?"
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 4:
                n 1flrpof "Fawning over me like always,{w=0.1} [player]?"
                n 1usqssf "Ehehe.{w=0.2} Don't worry,{w=0.1} I'm not complaining!"
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1fcssmf "It's just us two against the world!"
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 5:
                n 1fllbgf "Well,{w=0.1} o-{w=0.1}of course you do.{w=0.2} Ahaha!"
                n 1fchbgf "But...{w=0.3} we both know I love you more,{w=0.1} [player]."
                menu:
                    "No, I love you more.":
                        n 1fnmbgf "No,{w=0.1} I-"
                        n 1tllajl "..."
                        n 1fnmawl "H-{w=0.1}hey...{w=0.3} wait a minute...!"
                        n 1fchgnl "I know where we're going with this!{w=0.2} Nice try,{w=0.1} [player]!"
                        n 1fsqsml "You're just gonna have to accept that I love you more,{w=0.1} and that's just the way it is."
                        menu:
                            "You love me more, and that's just the way it is.":
                                n 1uchgnf "Ehehe.{w=0.2} See?"
                                n 1fwmsmf "That wasn't so hard,{w=0.1} was it?"
                                n 1nchbgf "I looooove you,{w=0.1} [player]~!"

                    "Okay.":
                        n 1uchgnl "Pfffft!{w=0.2} Ahaha!"
                        n 1fwltsf "Come on,{w=0.1} [player]!{w=0.2} Where's your fighting spirit?"
                        n 1fchsmf "Well,{w=0.1} whatever.{w=0.2} I'm just glad you accept the truth."
                        n 1uchsmf "Ehehe."

                $ jn_relationship("affinity+")
                return

            elif random_response_index == 6:
                n 1uchsmf "Ehehe...{w=0.3} I always adore hearing that from you,{w=0.1} [player]."
                n 1usqsmf "...And I think I can guess you like hearing it just as much."
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1nchsmf "I don't need anyone else~."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 7:
                n 1nsqajl "Wow,{w=0.1} [player]..."
                n 1tslajl "You really are just a big sappy mess today,{w=0.1} aren't you?"
                n 1tsldvl "Gross..."
                n 1fchbgf "...But just the kind of gross I'm down with.{w=0.2} Ehehe."
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1unmsmf "I'll always have your back."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 8:
                n 1uchsmf "Ehehe."
                n 1nchssf "I..."
                n 1uchbsf "Looooooooove you too,{w=0.1} [player]!"
                n 1kwmsmf "You'll always be my rock."
                $ jn_relationship("affinity+")
                return

            elif random_response_index == 9:
                n 1fllsmf "I mean...{w=0.3} that's real sweet of you and all,{w=0.1} [player]..."
                n 1fsqsmf "But we both know I love you more~."
                $ player_is_wrong = True
                $ wrong_response_count = 0

                # Natsuki won't lose!
                while player_is_wrong:
                    menu:
                        "No, I love {i}you{/i} more!":

                            if wrong_response_count == 1:
                                n 1fsqbgl "Hmm?{w=0.2} Did you mishear me,{w=0.1} [player]?"
                                n 1fchbgf "I said I love {i}you{/i} more,{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n 1fsqbgl "Oh?{w=0.2} Competitive,{w=0.1} are we?"
                                n 1fslbgl "Ehehe.{w=0.2} Silly [player].{w=0.1} Did nobody ever tell you?"
                                n 1fchgnl "Don't start a fight you can't finish!"
                                n 1fchbgf "Especially this one -{w=0.1} I love {i}you{/i} more~!"

                            elif wrong_response_count == 10:
                                n 1tsqbgl "Oho?{w=0.2} Not bad,{w=0.1} [player]!"
                                n 1fsqbgl "I almost admire your stubbornness..."
                                n 1uchsmf "But not as much as I admire you!{w=0.2} I love {i}you{/i} more!"

                            elif wrong_response_count == 20:
                                n 1fsqbgl "Ehehe.{w=0.2} You're persistent!{w=0.2} I'll give you that."
                                n 1fsqsml "But if you think I'm giving you a win..."
                                n 1fchgnl "Then you've got another thing coming!"
                                n 1uchbgl "I love {i}you{/i} more,{w=0.1} dummy!"

                            elif wrong_response_count == 50:
                                n 1tnmajl "Wow!{w=0.2} This is like...{w=0.3} the 50th time you've been wrong!{w=0.2} In a row!"
                                n 1tsqsgl "Sounds to me like you're in some serious denial there,{w=0.1} [player]~."
                                n 1nllssl "I don't think I can be bothered counting much more from here..."
                                n 1fsqtsl "So why don't you do me a favour and just accept that I love {i}you{/i} more already?"
                                n 1uchsml "Ehehe."
                                n 1fchbgl "Thanks,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n 1uwdgsl "...Oh!{w=0.2} And it looks like we have our 100th wrong answer!"
                                n 1fllawl "Dim the lights!{w=0.2} Roll the music!"
                                n 1flrbgl "Now,{w=0.1} audience members -{w=0.1} what does our stubborn participant get?"
                                n 1fsqbgl "They get..."
                                n 1uchgnl "A correction!{w=0.2} Wow!"
                                n 1fsqbgl "And that correction is..."
                                n 1fchbsf "[n_name] loves {i}them{/i} way more!{w=0.2} Congratulations,{w=0.1} dummy!"
                                n 1fsqdvl "And now,{w=0.1} to walk away with the grand prize -{w=0.1} all our guest here needs to do..."
                                n 1fchbsl "...Is give up and admit how wrong they are~!{w=0.2} Ehehe."

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
                                n 1fchbgf "[chosen_random_response]"

                            $ wrong_response_count += 1

                        "Okay, fine. You love me more.":
                            $ player_is_wrong = False
                            n 1tsqbgl "See?{w=0.2} Was that really so hard?"
                            n 1uchtsl "Sometimes you just have to admit you're wrong,{w=0.1} [player]~."
                            n 1nchsml "Ehehe."

                            if wrong_response_count >= 10:
                                n 1nsqsml "Nice try,{w=0.1} though~!"

                            $ jn_relationship("affinity+")
                            return

            elif random_response_index == 10:
                n 1ksqsml "Ehehe.{w=0.2} I'll never get tired of hearing that from you,{w=0.1} [player]."
                n 1uchsmf "I love you too!"
                n 1uchbgf "You're my numero uno~."
                $ jn_relationship("affinity+")
                return

            else:
                n 1usqbgf "Oh?{w=0.2} Lovey-dovey as usual?"
                n 1uslsmf "You're such a softie,{w=0.1} [player].{w=0.2} Ehehe."
                n 1uchbgf "But...{w=0.3} I'm not gonna complain!{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "You always make me feel tall."
                $ jn_relationship("affinity+")
                return

            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1fbkwrf "G-{w=0.1}gah!{w=0.2} [player]!"
            n 1fllwrf "What did I say about making things awkward?{w=0.2} Now it's twice as awkward!"
            n 1fcsemf "Jeez..."
            n 1flremf "Let's just talk about something,{w=0.1} alright?"
            n 1flrpof "Y-{w=0.1}you can fawn over me in your {i}own{/i} time!"
            n 1klrpof "Dummy..."
            $ jn_relationship("affinity+")
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            n 1fskemf "H-{w=0.1}hey! I thought I told you not to just come out with stuff like that!"
            n 1fllemf "Jeez..."
            n 1fcsemf "I-{w=0.1}I don't know if you're trying to win me over,{w=0.1} or what..."
            n 1fcspof "But you're gonna have to try a lot harder than that!"
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n 1fskemf "G-{w=0.1}gah!"
            n 1fbkwrf "[player_initial]-{w=0.1}[player]!"
            n 1fnmanl "Stop being gross!"
            n 1fcsanl "Jeez..."
            n 1fllajl "I don't know if you think this is a joke,{w=0.1} or what..."
            n 1fsqaj "But it really isn't funny to me,{w=0.1} [player]."
            return

        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            n 1fcssr "..."
            n 1fsqsr "Talk is cheap,{w=0.1} [player]."
            n 1fsqaj "If you {i}really{/i} care about me..."
            n 1fsqpu "Then {i}prove{/i} it."
            $ jn_relationship("affinity-")
            return

        else:
            n 1fsqpu "..."
            n 1fsqan "You're actually unbelievable,{w=0.1} [player]."
            n 1fsqfu "Do you even {i}understand{/i} what you're saying?"
            n 1fcsfu "..."
            n 1fcspu "You know what?{w=0.2} Whatever.{w=0.2} I don't care anymore."
            n 1fsqfu "Say what you like,{w=0.1} [player].{w=0.2} It's all crap,{w=0.1} just like everything else from you."
            $ jn_relationship("affinity-")
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
        n 1unmaj "Hmm?{w=0.2} My hairstyle?"
        n 1fsgsg "Why do you ask,{w=0.1} [player]?{w=0.2} Looking for a stylist?"
        n 1fchsm "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "Huh?{w=0.2} My hairstyle?"
        n 1fsqaj "Wait...{w=0.3} are you messing with me?{w=0.2} What do you mean?"
        n 1fllpo "You better not be teasing me,{w=0.1} [player]..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmsl "...Huh?{w=0.2} Oh.{w=0.2} My hair."
        n 1flrsl "I'm...{w=0.3} surprised you care enough to ask about that."

    else:
        n 1fsqsl "Because I like it that way.{w=0.2} Is that good enough for you?"
        n 1fsqan "Why would you even care anyway?{w=0.2} You haven't cared about me so far."
        n 1fslpu "Jerk."
        return

    n 1nnmpu "Well,{w=0.1} anyway."
    n 1ullpu "I never really thought about it that much,{w=0.1} honestly."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        if persistent.jn_natsuki_current_hairstyle == "default":
            n 1ulrpo "I just thought twintails would look kinda cute on me."

        else:
            n 1ulrpo "I know I'm not showing them off now,{w=0.1} but I just thought twintails would look kinda cute on me."

        n 1fsqpo "...Yeah,{w=0.1} yeah.{w=0.2} I know what you're thinking,{w=0.1} [player]."

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1ksqsm "Was I wrong...?"
            n 1fchbg "Ehehe.{w=0.2} I thought not."

    else:
        if persistent.jn_natsuki_current_hairstyle == "default":
            n 1nnmsl "I guess I just liked the idea of twintails."

        else:
            n 1nnmsl "Not like I'm showing it now,{w=0.1} but I guess I just liked the idea of twintails."

    n 1ulraj "As for the bangs,{w=0.1} I...{w=0.3} always found it difficult to get my hair cut."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1flraj "It just costs so much,{w=0.1} you know?{w=0.2} It's super dumb!"
        n 1fnman "Like...{w=0.3} I don't get it at all!"
        n 1fllan "And the annoying thing is that if I were a guy,{w=0.1} it'd be way cheaper!{w=0.2} What's up with that?"
        n 1ncssl "Ugh...{w=0.3} but yeah."

    else:
        n 1nlrsl "I was always kinda short when it came to getting it cut."
        n 1fsqsl "...And no,{w=0.1} {i}not{/i} in the physical sense."

    if persistent.jn_natsuki_current_accessory is not None:
        n 1ullaj "As for my hairclip?{w=0.2} It's just to keep my hair out of my eyes."

    else:
        n 1ullaj "I'm not wearing it now,{w=0.1} but the hairclip is just to keep my hair out of my eyes."

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fllss "Looking good is a bonus,{w=0.1} but I mostly just got tired of brushing my hair out of my face."
        n 1nsrca "Especially with bangs this long!"
        n 1unmaj "Anyway..."

    n 1tllaj "Have I thought about other hairstyles?{w=0.2} Well..."

    if persistent.jn_natsuki_current_hairstyle != "default":
        n 1ullbo "I think that kinda speaks for itself,{w=0.1} really.{w=0.2} I {i}am{/i} trying out a different one..."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1usgss "Either way though,{w=0.1} [player]..."
        n 1fcssml "I'm pretty sure I already let my hair down around you,{w=0.1} [chosen_tease].{w=0.2} That qualifies, right?"
        n 1uchgnl "Ahaha!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "You know what they say,{w=0.1} [player]."
        n 1fnmbg "If it ain't broke,{w=0.1} don't fix it!"
        n 1uchgn "Ehehe."

    else:
        n 1fslaj "...At this point,{w=0.1} [player]?{w=0.2} I'd rather you stayed {i}out{/i} of my hair."
        n 1fsqbo "Thanks."

    return

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
    n 1ullaj "You know,{w=0.1} [player]..."
    n 1nnmaj "I feel like nowadays,{w=0.1} everyone is trying to make a point,{w=0.1} or preach something."
    n 1flrem "Especially with social media and all that everywhere -{w=0.1} it's crazy!"
    n 1fllem "Like...{w=0.3} there's posts telling you this is bad,{w=0.1} others asking why you don't support something else..."
    n 1fcsan "And of course,{w=0.1} {i}everyone{/i} is tuned in to that -{w=0.1} so it leaks into real life as well!"
    n 1flrsl "Ugh...{w=0.3} it can't only be me that finds it all exhausting,{w=0.1} right?"
    n 1unmaj "I think it makes it kinda easy to lose track of what you really like,{w=0.1} or what you stand for."
    n 1ullaj "Which...{w=0.3} is actually something I really wanted to talk to you about,{w=0.1} [player]."
    n 1fllpu "I'm not saying you should just ignore everyone else,{w=0.1} or never consider other points of view."
    n 1fnmpo "That's just being ignorant."
    n 1knmaj "But...{w=0.3} don't just let other people's opinions or conceptions completely overwrite your own,{w=0.1} 'kay?"
    n 1fnmbo "At least not without a fight,{w=0.1} at least."
    n 1fnmpu "{i}You{/i} are your own master,{w=0.1} [player] -{w=0.1} you have your own opinions,{w=0.1} your own values:{w=0.1} and that's super important!"
    n 1fcsbg "I mean,{w=0.1} look at me!"
    n 1fllaj "So what if someone says what I'm into sucks?{w=0.2} Or if I should be following something more popular?"
    n 1fnmsf "It isn't hurting anyone,{w=0.1} so who are they to judge and tell me what I should be enjoying?"
    n 1fcsbg "It's my life,{w=0.1} so they can jog on!"
    n 1nnmsr "Anyway...{w=0.3} I guess what I'm saying is don't be afraid to stand up for what matters to you,{w=0.1} [player]."
    n 1fcsaj "There's gonna be times you'll be wrong,{w=0.1} but don't let it get to you!"
    n 1flrsl "I just don't like the idea of people being pushed into what isn't right for them."
    n 1nnmpu "That being said,{w=0.1} [player]..."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1ksqsm "I'm pretty sure we both know what's right for each other by now,{w=0.1} huh?"
        n 1fcsbgl "Ahaha."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1uchsml "Love you,{w=0.1} [player]~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1ksqsm "I'm pretty sure I know what's right for you..."
        n 1fcsbgl "Spending more time with me!{w=0.2} Ahaha."

    else:
        n 1unmss "I'm sure I can help you find what's right for you."
        n 1fllss "That's what friends are for,{w=0.1} right?"
        n 1fcsbg "Especially ones like me!{w=0.2} Ehehe."

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
        n 1fsqsr "Hammies."
        n 1fcssm "That's barely even a question for me,{w=0.1} [player]."
        n 1uwdaj "Like...{w=0.3} if you've seen them,{w=0.1} can you blame me?"
        n 1fcspu "They're...{w=0.5}{nw}"
        n 1fspgs "{i}Adorable{/i}!!"
        n 1fbkbsl "I just love everything about them...{w=0.3} the little paws,{w=0.1} the bright eyes, those puffy cheeks..."
        n 1fspbgl "And that tiny little tail...{w=0.3} oh my gosh!{w=0.2} It's just precious!"
        n 1fllan "It really winds me up when people call them boring,{w=0.1} or unaffectionate though.{w=0.2} Like...{w=0.3} have you ever watched one?"
        n 1fnmaj "They all have their own little personalities,{w=0.1} just like any other animal -{w=0.1} only smaller!"
        n 1uwdaj "And if you bond with them,{w=0.1} they aren't afraid to show it -{w=0.1} I've seen videos of them following their owners around,{w=0.1} and even leaping into their hands!"
        n 1fchbg "Plus they're easy to take care of,{w=0.1} too!"
        n 1fchsm "Just top up their food and change their water daily,{w=0.1} and clean their cage out once a week -{w=0.1} no sweat."
        n 1nllpu "Hmm..."
        n 1unmpu "You know,{w=0.1} [player]...{w=0.3} it does get a little quiet when you aren't around,{w=0.1} if you know what I'm getting at..."
        n 1fnmsm "Perhaps one day we could have our own furry friend here too?{w=0.1} Ehehe."
        n 1fllss "Don't worry though,{w=0.1} [player]..."
        n 1ucssm "I don't mind taking care of it."
        n 1fchgn "...But you're in charge of the supplies!"

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1fchbg "Oh,{w=0.1} and relax -{w=0.1} I'll make sure it'll be well tamed!"
            n 1uslbg "Or..."
            n 1usqts "At least about as tame as you,{w=0.1} huh [player]?{w=0.2} Ahaha!"

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1uchbg "Love you~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fsqpu "Hamsters,{w=0.1} if it matters."
        n 1fllpu "Why?{w=0.2} I don't know.{w=0.2} I just think they're cute."
        n 1nllbo "I think people actually underestimate how expressive they can be,{w=0.1} too."
        n 1nnmbo "They're like most animals really -{w=0.1} they all have their own personalities."
        n 1nnmaj "I guess they're pretty easy to take care of as well,{w=0.1} so there's that."
        n 1nlrsl "..."
        n 1flrsl "...I'd be lying if I said I hadn't been thinking about getting one myself..."
        n 1fsqpu "But honestly,{w=0.1} [player]?{w=0.2} If you've shown you can't take care of {i}me{/i}?"
        n 1fcsan "...Then I don't think it'd be fair to bring one here,{w=0.1} either.{w=0.2} Heh."

    else:
        n 1fsqpu "Heh.{w=0.2} Really?{w=0.2} My favourite animal...?"
        n 1fcsan "Not you,{w=0.1} [player].{w=0.2} That's for sure."

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
        n 1unmbg "Ooooh!{w=0.2} My favourite drink?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "Mmm?{w=0.2} My favourite drink?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nllbo "Huh?{w=0.2} Oh.{w=0.1} My favourite drink."

    else:
        n 1fslsf "...I can't understand why you'd care,{w=0.1} [player]."
        n 1fsqsf "So...{w=0.3} why should I?"
        n 1fsqan "Water.{w=0.2} There's an answer for you.{w=0.2} Happy?"
        n 1fcsan "Now just go away..."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1ullaj "I gotta say...{w=0.3} it depends on the weather more than anything."
        n 1tnmaj "I mean...{w=0.3} what kind of dope would order an iced drink in the middle of winter?!"
        n 1fllss "But anyway..."
        n 1fcsbg "If it's cold out,{w=0.1} then hot chocolate.{w=0.2} No questions,{w=0.1} no doubts."
        n 1uchgn "In the depths of winter,{w=0.1} you definitely won't get a better option than that!"

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1fcsbg "And yeah,{w=0.1} [player] -{w=0.1} whipped cream,{w=0.1} marshmallows -{w=0.1} all of it.{w=0.2} The complete works."
            n 1uchgn "...And I wouldn't accept anything less!"
            n 1fllbg "I mean,{w=0.1} think about it -{w=0.1} if you're getting hot chocolate,{w=0.1} you've already kinda lost on the health front."
            n 1uchgn "So you might as well go all in,{w=0.1} right?{w=0.2} Ahaha."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1fcsdvl "Besides,{w=0.2} I'm not too worried -{w=0.1} we'll just share the calories,{w=0.1} [player]~."

        n 1unmaj "As for warmer weather...{w=0.3} that's a little trickier,{w=0.1} actually."
        n 1fslsr "Let me think..."
        n 1fsrsr "..."
        n 1fchbs "Aha!{w=0.2} I got it!"
        n 1unmbg "It's gotta be those milkshakes,{w=0.1} but from one of those places where you get to choose what goes in it!"
        n 1fsqsm "I don't just mean picking a flavour,{w=0.1} [player]..."
        n 1fchgn "I mean where you can pick any combination of ingredients you want!"
        n 1fllss "Well...{w=0.3} as long as it blends,{w=0.1} anyway."
        n 1ncssm "All kinds of sweets,{w=0.1} any type of milk..."

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1ucssm "Though if I had to pick a favourite?"
            n 1fcsbg "It's gotta be strawberries and cream,{w=0.1} obviously."
            n 1fllbgl "And...{w=0.3} maybe with just a dash of chocolate too?{w=0.2} Ehehe."

        else:
            n 1fchbg "Yeah.{w=0.2} That's the real deal!"

        n 1fllpo "Jeez...{w=0.3} all this talk about drinks is making me kinda thirsty,{w=0.1} actually.{w=0.2} So on that note..."
        n 1fnmbg "You need to stay hydrated too,{w=0.1} [player] -{w=0.1} whatever the weather!"

    else:
        n 1flrsl "I suppose it depends what the weather is like."
        n 1fnmbo "Hot chocolate if it's cold out,{w=0.1} though I'm not very picky I guess."
        n 1fllaj "As for warmer weather..."
        n 1fllsl "I don't really know.{w=0.2} Whatever is fine."
        n 1fsqsl "Heh.{w=0.2} Though at this rate,{w=0.1} I shouldn't expect much more than tap water from you anyway.{w=0.2} Right,{w=0.1} [player]?"

    return

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
        n 1fsqctl "Oho?{w=0.2} Does [player] like a girl in uniform?"
        n 1ksqaj "Wow...{w=0.3} you're even {i}more{/i} gross than I thought."
        n 1fsqsm "..."
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchgn "Oh come on,{w=0.1} [chosen_tease]!{w=0.2} You always get all sulky when I call you that!{w=0.2} I just can't resist."
        n 1fchsm "Ehehe.{w=0.2} So anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1unmaj "Huh?{w=0.2} My school uniform?"
        n 1fsqsm "...Ehehe."
        n 1fcsbgl "Why do you ask,{w=0.1} [player]?{w=0.2} Did {i}you{/i} wanna wear it or something?"
        n 1fchgn "Oh!{w=0.2} We can play dress-up!{w=0.2} Wouldn't you like that,{w=0.1} [player]?{w=0.2} It'll be so much fun!"
        n 1uchbs "I bet I could make you look so cute~.{w=0.1} Ahaha!"
        n 1nllss "Well anyway,{w=0.1} putting jokes aside..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1tnmaj "My school uniform?{w=0.2} That's...{w=0.3} kind of a weird thing to ask me about,{w=0.1} huh?"
        n 1nslaj "Well,{w=0.1} whatever.{w=0.2} I'll let it slide...{w=0.3} this time."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nsraj "...Huh?{w=0.2} Oh,{w=0.1} the school uniform."
        n 1nsqsl "I...{w=0.3} don't know what you're expecting to hear from me,{w=0.1} [player]."
        n 1fsqsl "I gotta wear it for school.{w=0.2} That's the point of a uniform,{w=0.1} if you hadn't realized."
        n 1fsrsf "It doesn't matter if I like it or not."
        n 1fsqbo "...And it matters even less if you do."
        return

    else:
        n 1fsran "Heh.{w=0.2} I like it more than {i}you{/i}.{w=0.2} Jerk."
        return

    n 1unmaj "It's alright,{w=0.1} I guess.{w=0.2} I actually really like the warm colours!"
    n 1nnmss "They're way easier on the eyes than a lot of the other uniforms I've seen around."
    n 1nsqsr "But Oh.{w=0.2} My.{w=0.2} Gosh.{w=0.2} [player]."
    n 1fcsan "The layers.{w=0.2} So many layers."
    n 1fllem "Who even thought someone needs that much clothing?!{w=0.2} For school,{w=0.1} of all places?!"
    n 1fbkwr "I mean...{w=0.3} do you even {i}know{/i} what wearing all of this in summer is like?!{w=0.2} It's horrible!"
    n 1flrpo "And the blazer...{w=0.3} ugh!{w=0.2} It's actually the worst thing ever."
    n 1fsqpo "Like yeah,{w=0.1} I can take some off between class,{w=0.1} but I gotta put it all back on when I go back in."
    n 1fllpo "...Or get told off.{w=0.2} {i}Again{/i}.{w=0.2} I honestly have no idea how Sayori gets away with hers being so scruffy."
    n 1fcsan "And all of this stuff is super expensive too!{w=0.2} Talk about a kick in the teeth!"
    n 1fslan "Jerks."
    n 1fslsr "Ugh...{w=0.3} I seriously can't wait until I can wear whatever I like for what I'm doing."
    n 1flrpo "It could be worse though,{w=0.1} I guess.{w=0.2} At least I never had to learn how to do a tie."
    n 1unmaj "What about you though, [player]?"
    menu:
        n "Did you have to wear uniform at school?"

        "Yes, I had to wear uniform.":
            n 1fcsbg "Aha!{w=0.2} So you know the struggle too,{w=0.1} huh?"

        "No, I didn't have to wear uniform.":
            n 1fslsr "..."
            n 1fsqsr "...Lucky."

        "I have to wear uniform now.":
            n 1fchgn "Then you have my condolences,{w=0.1} [player]!{w=0.2} Ahaha."
            n 1fcsbg "Good to know we're on the same page,{w=0.1} though."

    n 1ullss "Well,{w=0.1} anyway..."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1fllss "I still don't particularly {i}like{/i} wearing it..."
        n 1uslbgl "But...{w=0.3} I think I can put up with it.{w=0.2} Just for you,{w=0.1} [player]~."
        n 1usrdvl "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1usrdvl "I-{w=0.1}if you don't mind it,{w=0.1} [player]?"
        n 1fllbgl "I suppose it has that going for it too,{w=0.1} a-at least..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1fchgn "I guess at least I'm warm and toasty for the winter,{w=0.1} right?{w=0.2} Ahaha."

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
        n 1uwdbg "Ooh!{w=0.2} Flying?{w=0.2} Like on a plane?"
        n 1fllun "Nnn...{w=0.3} I wish I could say I have,{w=0.1} [player]..."
        n 1fchbg "Don't get me wrong though!{w=0.2} I'd {i}totally{/i} fly somewhere new if I could!"
        n 1fslsl "It's just...{w=0.3} the price of it all,{w=0.1} you know?"
        n 1kllsl "I've never had a passport,{w=0.1} but it's mainly the tickets and everything beyond that..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1unmaj "Huh?{w=0.2} Flying?{w=0.2} Like on a plane or something?"
        n 1kllaj "I...{w=0.3} wish I could say I have,{w=0.1} [player]."
        n 1fnmbg "Don't get me wrong though!{w=0.2} I'd love to jet off somewhere.{w=0.2} Like for a vacation or something!"
        n 1flrpo "It's just the cost that stops me, you know?"
        n 1fcspo "Even if I had a passport, there's just so many things to pay out for..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "Oh?{w=0.2} Like flying on a plane or whatever?"
        n 1kllbo "Uhmm..."
        n 1klraj "I...{w=0.3} never really had the opportunity to fly anywhere,{w=0.1} [player]."
        n 1unmaj "I don't even have a passport or anything like that,{w=0.1} and even if I did?"
        n 1nsraj "It isn't like tickets are...{w=0.3} affordable,{w=0.1} if you know what I mean?"
        n 1nslpo "Especially to someone in my...{w=0.3} position."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmbo "Flying?{w=0.2} Like...{w=0.3} on a plane?"
        n 1fnmsf "No,{w=0.1} [player].{w=0.2} I haven't."
        n 1fllsf "I've never owned a passport,{w=0.1} and it's way too expensive anyway."
        n 1fnmaj "I don't really like the idea of the environmental impact either."
        n 1fsqaj "...But something tells me you don't really care about that last point,{w=0.2} do you?"
        n 1flrca "You know...{w=0.3} just going by my experience so far."
        n 1fsqca "...Am I wrong?"
        return

    else:
        n 1fsqan "No,{w=0.1} [player].{w=0.2} I haven't.{w=0.2} And I probably never will."
        n 1fcsan "Gloat all you want.{w=0.2} I don't give a crap if you have."
        return

    n 1ullaj "Besides,{w=0.1} I try not to feel too bad about it.{w=0.2} It's way better for the environment if I don't,{w=0.1} anyway!"
    n 1nnmbo "Flying places is pretty polluting.{w=0.2} I think I'd just feel selfish if I was constantly zooming around,{w=0.1} knowing how bad that is for everyone."
    n 1nllss "But...{w=0.3} that's just me,{w=0.1} I guess."
    n 1unmaj "What about you,{w=0.1} [player]?"
    menu:
        n "Are you a frequent flier?"

        "Yes, I fly regularly.":
            n 1fcsbg "Oh?{w=0.2} Well check you out,{w=0.1} [player]!"
            n 1fslpo "I guess it's {i}plane{/i} to see how well you're doing for yourself?"
            n 1fchbg "Ehehe."
            n 1fnmaj "Just try to avoid racking up too many miles,{w=0.1} [player]."
            n 1fllss "You gotta think about the planet too,{w=0.1} you know..."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1fslnvf "E-{w=0.1}especially if people we really care about are in it.{w=0.2} Ahaha..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
                n 1fchgn "No excuses,{w=0.1} [player]! Ehehe."

        "I fly sometimes.":
            n 1unmss "Ooh,{w=0.1} okay!{w=0.2} So the odd vacation or family flight then?"
            n 1fslsm "I see,{w=0.1} I see..."
            n 1fcsbg "Well,{w=0.1} good for you,{w=0.1} [player]!{w=0.2} Everyone should get the chance to explore the world."
            n 1kslss "Hopefully I'll get the chance someday too."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1fsqsg "I hope you'll be available when that happens,{w=0.1} [player]."
                n 1fchgnl "You're gonna be my tour guide,{w=0.1} whether you like it or not!"

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
                n 1fsqsm "You better be handy when that happens,{w=0.1} [player]..."
                n 1fchgn "We'll see how good a guide you are!"

        "I've flown before.":
            n 1fsqct "Oh?{w=0.2} So you've already earned your wings,{w=0.1} huh?"
            n 1tllaj "Hmm...{w=0.3} I wonder where you went?"
            n 1fnmaj "You gotta promise to tell me if you fly again,{w=0.1} 'kay?"
            n 1fchgn "I wanna hear all about it!"

        "I've never flown.":
            n 1fcsbg "Then that's just another thing we have in common,{w=0.1} [player]!"
            n 1fsqss "I guess you could say..."
            n 1fsqdv "We're both just {i}well grounded{/i} people,{w=0.1} huh?"
            n 1fchgn "Ahaha!"

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
            n 1unmaj "Eh?{w=0.2} Cars?"
            n 1fchgn "Jeez,{w=0.1} you know I can't drive,{w=0.1} dummy!{w=0.2} I don't have a reason to be into cars!"
            n 1nlrbg "Well,{w=0.1} anyway..."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n 1fcssl 1nnmsl "[player].{w=0.2} You know I can't drive.{w=0.2} Why would you think I'd be into cars,{w=0.1} of all things?"
            n 1fllsl 1nllsl "...Fine.{w=0.2} Whatever."

        else:
            n 1fsqpu "...Really?"
            n 1fsqaj "You know I can't drive.{w=0.2} So I'm not even going to {i}pretend{/i} I care if you're into that,{w=0.1} [player]."
            n 1fsqan "Besides...{w=0.3} I bet you'd {i}never{/i} treat your dream car like you treat me,{w=0.1} would you?"
            return

    else:
        # Natsuki hasn't stated she can't drive before
        if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n 1unmaj "Huh?{w=0.1} Am I into cars?"
            n 1fllnv "Well...{w=0.3} to tell you the truth,{w=0.1} [player]?"
            n 1unmaj "...I've never actually owned a license."
            n 1flrpo "I don't even think I could afford to learn!"
            n 1nnmaj "So I've never really been drawn to them honestly."

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n 1fnmsr "I can't drive,{w=0.1} [player].{w=0.2} I don't have a license either;{w=0.1} learning was always too expensive."
            n 1fnmpu "So...{w=0.3} why would I be into that?{w=0.1} I literally can't {i}afford{/i} to be."

        else:
            n 1fcsan "Newsflash,{w=0.1} jerk.{w=0.2} I {i}can't{/i} drive,{w=0.1} and I can't even afford to {i}learn{/i}."
            n 1fsqan "So you tell {i}me{/i} -{w=0.1} why would I be into cars?{w=0.2} And if I was,{w=0.1} why the hell would I want to talk to {i}you{/i} about them?"
            n 1fcspu "...Heh.{w=0.2} Yeah,{w=0.1} I thought so.{w=0.2} We're done here,{w=0.1} [player]."
            return

    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmsm "I can appreciate the talent that goes into them -{w=0.1} I think it's actually pretty cool how expressive they can be!"
        n 1nllss "Like...{w=0.3} the design languages of all the different brands,{w=0.1} the engineering that goes into them and all that."
        n 1fchbg "It's pretty insane how much work goes into it;{w=0.1} and that's definitely something I have respect for!"
        n 1fsqsm "What about you though, [player]?{w=0.2} You {i}did{/i} bring it up,{w=0.1} but I thought I'd ask anyway..."
        menu:
            n "Are you into cars?"

            "Yes! I'm into my cars.":

                # The player has never stated if they can drive
                if persistent.jn_player_can_drive is None:
                    n 1tllbo "Huh.{w=0.2} I wasn't actually sure if you could even drive,{w=0.1} but I suppose that doesn't matter really."
                    n 1fsqsm "I guess being a petrolhead isn't an exclusive club,{w=0.1} huh?"
                    n 1uchbg "Ahaha."

                # The player has confirmed they can drive
                elif persistent.jn_player_can_drive:
                    n 1fsgbg "Well,{w=0.1} color {i}me{/i} surprised."
                    n 1fchgn "Ehehe."
                    n 1fcsbg "Don't worry,{w=0.1} I had you figured for the sort,{w=0.2} [player]."
                    n 1fchbg "But hey -{w=0.1} whatever floats your boat!"

                # The player has admitted they cannot drive
                else:
                    n 1unmaj "That's...{w=0.3} actually pretty surprising to hear from you,{w=0.1} [player]."
                    n 1nllaj "You know,{w=0.1} since you said you can't drive and all that..."
                    n 1fchbg "But I guess it's like anything -{w=0.1} you don't have to be doing it to be a fan,{w=0.1} and that's fine with me!"

            "I don't care much for them.":
                n 1ullss "I guess that's fair enough -{w=0.1} and don't worry,{w=0.1} I completely get it."
                n 1nnmsm "But if someone's into that kind of thing,{w=0.1} who are we to judge,{w=0.1} after all?"

            "No, I'm not into them.":
                n 1ulraj "...Huh.{w=0.2} That's kinda weird -{w=0.1} then why did you bring it up,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n 1tlraj "Especially if you can drive!"
                    n 1tllpu "Huh..."

                n 1fchbg "Well,{w=0.1} anyway.{w=0.2} Fair enough I guess!"

    else:
        n 1flrsr "I guess I can respect the work and talent that goes into designing and making one..."
        n 1fnmbo "But it's just the same as anything else."
        n 1fsqbo "...I suppose you're into your cars then,{w=0.1} are you?"
        n 1fcspu "Heh."
        n 1fsqpu "It'd be nice if you extended that respect to {i}people{/i} too,{w=0.1} [player]."
        n 1fsqsr "{i}Just saying.{/i}"

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
            n 1kwmpof "[player]...{w=0.3} isn't it obvious? You know I love you already,{w=0.1} right?"
            n 1fllpol "Jeez...{w=0.3} you really are a dork sometimes,{w=0.1} you know."
            n 1kllssl "But...{w=0.3} I kinda like that silly part of you,{w=0.1} [player]."
            n 1nwmbgl "Never change,{w=0.1} 'kay? Ehehe."
            n 1nchbgl "Love you,{w=0.1} [player]~!"

        else:
            n 1fcsanf "Nnnnnnn-!"
            n 1fnmanf "C-{w=0.1}come on! Isn't it obvious by now? Jeez...{w=0.5}{nw}"
            n 1fllpof "Do I really have to spell it out for you,{w=0.1} [player]?"
            n 1fcspol "Ugh...{w=0.5}{nw}"
            n 1fsqssl "Heh.{w=0.2} Actually,{w=0.1} you know what?"
            n 1fsqbgl "I'll let you figure it out."
            n 1fslajl "And no,{w=0.1} before you ask -{w=0.1} you've had enough hints already."
            n 1fllpol "Dummy..."

        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fcsanf "Uuuuuu-!"
        n 1fskwrf "A-{w=0.1}are you trying to put me on the spot or something,{w=0.1} [player]?"
        n 1fllemf "Jeez...{w=0.5}{nw}"
        n 1fcseml "You should {i}know{/i} what I think of you by now...{w=0.5}{nw}"
        n 1fllpol "...{w=0.5}{nw}"
        n 1kcspol "...{w=0.3}Fine."
        n 1fcspol "I...{w=0.3} like...{w=0.3} you,{w=0.1} [player].{w=0.2} A bunch."
        n 1fbkwrf "T-{w=0.1}there!{w=0.2} Happy now?!"
        n 1kllsrl "Sheesh..."
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fskemf "H-{w=0.1}huh? How do I feel about you?"
        n 1fbkwrf "W-{w=0.1}what're you asking me about that for?!"
        n 1fllpol "Sheesh,{w=0.1} [player]...{w=0.3} you'll make things all awkward at this rate..."
        n 1fcseml "You're fine,{w=0.1} so you don't need to keep bugging me about it!"
        n 1flrunl "Jeez..."
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1uskemf "H-huh?!"
        n 1fllbgl "O-oh! Ahaha..."
        n 1nllaj "Well,{w=0.1} I mean...{w=0.5}{nw}"
        n 1ullaj "You're pretty fun to be with,{w=0.1} all things considered."
        n 1fllnvl "So...{w=0.3} yeah...."
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1uskeml "H-{w=0.1}huh?!"
        n 1fllbg "O-oh!"
        n 1unmaj "I mean...{w=0.3} you're alright...{w=0.3} I guess?"
        n 1nnmpu "That's about all I can say so far,{w=0.1} so...{w=0.3} yeah."
        n 1nllca "...{w=0.5}{nw}"
        n 1nlraj "So...{w=0.3} where were we?"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        n 1fsqaj "...{w=0.3}Oh? That matters to you now,{w=0.1} does it?"
        n 1fsqbo "Then tell me,{w=0.1} [player]."
        n 1fnmun "Why did you keep hurting my feelings like that?"
        n 1fcsun "...{w=0.5}{nw}"
        n 1fllan "I don't have much patience for jerks,{w=0.1} [player]."
        n 1fnmaj "I don't know if you're trying to be funny or what,{w=0.1} but knock it off.{w=0.2} Got it?"
        n 1fsqsr "Thanks."
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fsqsr "...{w=0.3}Let's just cut the crap."
        n 1fcsan "You've hurt me,{w=0.1} [player].{w=0.2} You've hurt me again,{w=0.1} and again."
        n 1fnmfu "You've done it so many times now."
        n 1fnman "So you tell me."
        n 1fsqpu "What the hell would {i}you{/i} think of someone who did that to you?"
        n 1fcspu "...{w=0.5}{nw}"
        n 1fsqan "You're on thin ice,{w=0.1} [player].{w=0.2} Got it?"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.BROKEN:
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n 1fsqpu "...Wow.{w=0.2} Really?"

        else:
            n 1fsqpu "...{w=0.3}I have no words for how I feel about {i}you{/i}."
            n 1fsqfu "Don't freaking test me, {i}[player]{/i}."

        return

    else:
        n 1fcsun "...{w=0.3}...{w=0.5}{nw}"
        n 1fcsan "...{w=0.3}...{w=0.5}{nw}"
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
        n 1unmbg "Ooh!{w=0.2} Cosplay,{w=0.1} you say?"
        n 1fllbg "Honestly,{w=0.1} I've never really done any cosplaying or anything..."
        n 1nnmss "But I've actually thought about it a lot since I got into manga and all that stuff more!"
        n 1flrbg "Plus I mean,{w=0.1} why shouldn't I?{w=0.2} There isn't a whole lot stopping me."

        if already_mentioned_sewing:
            n 1fcssm "Like I think I mentioned before -{w=0.1} I'm already pretty handy with a needle and thread,{w=0.1} if I say so myself!"

        else:
            n 1fwlsm "I'm actually pretty handy with the old needle and thread,{w=0.1} you know!"

        n 1ulrss "And materials aren't really that expensive either -{w=0.1} besides props and wigs,{w=0.1} anyway."
        n 1nnmsm "So it seems like a pretty awesome way to show my appreciation for characters I like..."
        n 1fsqbg "...And show my {i}limitless{/i} talent while I'm at it."
        n 1fchgn "Ahaha!"
        n 1uchgn "And who knows?"
        n 1uchsm "Maybe you'll get to see some of my handiwork some day,{w=0.1} [player]."
        n 1fsqbg "I bet you'd like that,{w=0.1} huh?{w=0.2} Ehehe."
        n 1fsgsg "No need to be shy,{w=0.1} [player] -{w=0.1} I can read you like a book."
        n 1fsqsgl "A gross book,{w=0.1} but a book nonetheless~."
        n 1fchgn "Ahaha!"
        return

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1uchtsl "Love you,{w=0.1} [player]~!"
            return

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1tsrpu "...Why did I get the feeling you'd bring this up sooner or later,{w=0.1} [player]?"
        n 1fnmpo "What?{w=0.2} Did you think I'd {i}automatically{/i} be into it because I read manga from time to time?"
        n 1fsqpo "Huh?{w=0.2} Is that it?"
        n 1fnmaj "Well?"
        n 1fsqsg "Speak up,{w=0.1} [player]!{w=0.2} I can't hear you~!"
        n 1fslpo "..."
        n 1fchgn "Ahaha!{w=0.2} Nah,{w=0.1} it's fine."
        n 1ulraj "I've thought about it a bunch,{w=0.1} honestly -{w=0.1} like since I got into manga and all that a while ago."
        n 1nnmaj "I haven't {i}actually{/i} gone and dressed up yet,{w=0.1} though."
        n 1fnmaj "But there really isn't much stopping me,{w=0.1} [player]."

        if already_mentioned_sewing:
            n 1ullbo "Like I said -{w=0.1} I already fix up and make my own normal clothes,{w=0.1} so a costume isn't much of a leap."

        else:
            n 1flrbg "You could say I'm something of a pro with a needle and thread,{w=0.1} so it's right up my alley!"

        n 1unmaj "Besides,{w=0.1} I've done the math on materials -{w=0.1} it's actually pretty affordable,{w=0.1} so that's all good."
        n 1nllaj "Well,{w=0.1} besides wigs and props and stuff.{w=0.2} Those can be kinda pricey,{w=0.1} but not exactly unaffordable -{w=0.1} just gotta shop around!"
        n 1fllsl "That being said...{w=0.3} hmm..."
        n 1fllsm "You know what,{w=0.1} [player]?"
        n 1fnmbg "Perhaps I might just give it a shot...{w=0.3} yeah!"
        n 1fchgn "Man,{w=0.1} I've got so many awesome ideas buzzing around in my head now!"
        n 1fchsm "Oh -{w=0.1} don't worry -{w=0.1} you'll get your chance to see them too.{w=0.2} I'll need a second opinion after all."
        n 1uchbg "That's what friends are for,{w=0.1} right?{w=0.2} Ehehe."

        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1fsqbg "Besides,{w=0.1} [player].{w=0.2} You seem to have pretty good taste."
            n 1fsqsml "I think I can trust your judgement..."

        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmaj "Cosplay,{w=0.1} huh?"
        n 1ulraj "Well...{w=0.3} I mean,{w=0.1} I've considered it,{w=0.1} if that's what you're asking."
        n 1nnmbo "I never really thought about it that much until I got more into manga and things like that."
        n 1flrbg "It kinda feels like once you start getting into that stuff,{w=0.1} you discover tons more at once!"
        n 1nnmaj "But anyway,{w=0.1} I've never actually gone out and cosplayed myself."
        n 1flleml "T-{w=0.1}that isn't to say there's anything stopping me,{w=0.1} of course!"

        if already_mentioned_sewing:
            n 1fllss "I told you already that I'm pretty good with a needle and thread,{w=0.1} so that's a-{w=0.1}okay!"

        else:
            n 1fcsbg "I'm basically a pro with a needle and thread,{w=0.1} so that's the hard part already mastered!"

        n 1nlrpu "The rest of it is just shopping around for materials,{w=0.1} which are usually pretty cheap anyway."
        n 1unmpu "Props and wigs and all that are a little more annoying,{w=0.1} but not exactly undoable."
        n 1fllsr "Hmm..."
        n 1fllbg "The more I think about it,{w=0.1} the more I like the idea!"
        n 1fnmbg "What about you,{w=0.1} [player]?{w=0.2} I bet you'd love to see my skills at work,{w=0.1} right?"
        n 1nnmsm "Ahaha."
        n 1flrsml "Well...{w=0.3} we'll see,{w=0.1} but no promises!"
        return

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmpu "Huh?{w=0.2} Cosplay?"
        n 1fsqsr "...Why,{w=0.1} [player]?"
        n 1fsqpu "So you can make fun of my clothes too?"
        n 1fslsr "..."
        n 1fsqpu "No,{w=0.1} [player].{w=0.2} I've never cosplayed.{w=0.2} I could,{w=0.1} but I haven't."
        n 1fsqan "Does that answer your question?"
        return

    else:
        n 1fsqsr "Heh.{w=0.2} Why?"
        n 1fcsan "So you have something else to make me feel awful about?"
        n 1kcssr "...Yeah.{w=0.2} No thanks."
        n 1fcsan "I'm done talking to you about this."
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
            n 1kwmsl "[player]..."
            n 1kwmsf "You aren't asking me this because of what you told me earlier...{w=0.3} right?"
            n 1kllbo "..."
            n 1ncspu "Look,{w=0.1} [player].{w=0.2} I'm going to be completely honest with you,{w=0.1} okay?"
            n 1ncssl "What you can -{w=0.1} or {i}can't{/i} do -{w=0.1} isn't important to me."
            n 1nnmpu "What people {i}say{/i} you are -{w=0.1} or {i}aren't{/i} capable of -{w=0.1} isn't important to me either."
            n 1fnmpu "Neither is what people say about you."
            n 1knmsr "[player]."
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1klrpu "I...{w=0.3} feel about you the way I do because of how you've treated me,{w=0.1} [chosen_endearment].{w=0.2} Can you not see that?"
            n 1klrss "You've spent so much time with me,{w=0.1} day after day..."
            n 1kwmss "You've listened to my problems,{w=0.1} and you've told me yours..."
            n 1kllpo "You've been so patient with my mood swings,{w=0.1} and my grumpy moments..."

            if persistent.jn_player_love_you_count >= 10:
                n 1kcsunl "And...{w=0.3} you've made me feel..."
                n 1kcsunf "So loved..."
                n 1kllunl "..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kllssl "You're...{w=0.3} you're my first love,{w=0.1} [player]..."
                n 1kcussl "Do you even realise how {i}much{/i} that means to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmssl "You honestly,{w=0.1} truly mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 1klrnvl "Does that answer your question?"
            n 1knmsr "I know I can't solve your problems with a snap of my fingers,{w=0.1} [player].{w=0.2} I'm not a miracle worker."
            n 1kslsl "Believe me -{w=0.1} I {i}already{/i} would have if I could."
            n 1knmsl "But..."
            n 1kllss "I hope you can believe me when I say things will work out,{w=0.1} okay?"
            n 1fwmsm "Just...{w=0.3} keep fighting..."
            n 1fcssml "...Because I'm fighting for you too."
            n 1kplnvf "I love you,{w=0.1} [player].{w=0.2} You better not forget that."
            return

        else:
            n 1fcspo "[player]..."
            n 1flrpo "Do I really have to explain this all to you?"
            n 1flrsll "It's just...{w=0.3} embarrassing...{w=0.3} to me..."
            n 1kcssll "..."
            n 1ncspu "...Okay,{w=0.1} look."
            n 1fllssl "You've...{w=0.3} honestly done more than you could ever know,{w=0.1} [player]."
            n 1fllsll "For me,{w=0.1} I mean."
            n 1knmsll "I've almost lost count of how many hours you've spent talking to me..."
            n 1klrssl "You've listened to so many of my dumb problems,{w=0.1} over and over..."
            n 1fllunl "...And you've been so patient through all of my stupid moods."

            if persistent.jn_player_love_you_count >= 10:
                n 1fcsunl "Y-you've made me feel..."
                n 1kcsunl "Really appreciated.{w=0.2} So many times,{w=0.1} I've lost count..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kskajf "You're...{w=0.3} you're my first love,{w=0.1} even!"
                n 1kwmpuf "Do you even know what that {i}means{/i} to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmpuf "You seriously mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 1klrnvl "Does that answer all of your questions?{w=0.2} Am I free to go now?"
            n 1klrss "Ahaha..."
            n 1kwmpu "But seriously,{w=0.1} [player]."
            n 1kplbo "Don't ever doubt how important you are to me,{w=0.1} alright?"
            n 1fnmpol "I'll get mad if you do."
            n 1flrpol "And trust me..."
            n 1klrssl "I doubt you want that."
            return

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1knmaj "...Hey,{w=0.1} [player]..."
            n 1klrpu "This isn't by chance because of what you said earlier...{w=0.3} right?"

        else:
            n 1uskpul "Wh-{w=0.1}why do I-{w=0.1}...?"
            n 1fcsanl "Uuuuuuu..."

        n 1fcsajl "...Okay,{w=0.1} look.{w=0.2} I'll try to help you understand as best I can."
        n 1fllaj "I'm not sure if someone's giving you a tough time or what, but I'm saying it anyway."
        n 1fllsr "I don't really care about what others expect from you."
        n 1fnmsr "I don't really care about what others say or think about you."
        n 1knmpu "I don't really care if you can -{w=0.1} or can't -{w=0.1} do something."
        n 1fcseml "I...{w=0.3} {i}like{/i} you,{w=0.1} because of how you've treated me,{w=0.1} you dummy!"
        n 1flleml "Like,{w=0.1} come on!"
        n 1flrssl "You've listened to me yammer on,{w=0.1} again and again..."
        n 1knmssl "You've heard me out on so many dumb problems I've had..."
        n 1fcsbgl "You've even dealt with my crappy temper like a champ!"
        n 1klrsl "..."
        n 1kcssl "...I've never been treated by anyone as well as I've been treated by you,{w=0.1} [player]."
        n 1fllslf "So is it any wonder why I...{w=0.3} enjoy hanging out with you this much?"
        n 1fcsslf "..."
        n 1flrajl "Alright,{w=0.1} okay.{w=0.2} I really don't wanna have to explain all that again,{w=0.1} so I hope you took all that in."
        n 1fnmssl "Just...{w=0.3} continue being you,{w=0.1} got it?"
        n 1kllpul "I...{w=0.3} kinda like how you do that already."
        return

    else:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1unmpul "...Huh?"
            n 1uskemf "W-{w=0.1}why do I...?"
            n 1fcsanf "..."
            n 1tlremf "..."
            n 1flrsll "..."
            n 1fnmpul "Uhmm...{w=0.3} [player]?"
            n 1fllpo "This isn't all related to what you told me earlier,{w=0.1} right?"
            n 1knmpo "About feeling insecure and all that?"
            n 1klrsl "..."
            n 1nnmsl "[player]."
            n 1fnmpuf "Listen up,{w=0.1} 'kay?{w=0.2} I...{w=0.3} really don't wanna have to repeat this."

        else:
            n 1uscemf "Urk-!"
            n 1uskemf "W-{w=0.1}wait,{w=0.1} w-{w=0.1}what?"
            n 1fwdemf "W-{w=0.1}why do I...{w=0.3} l-{w=0.1}like you?!"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fllwrf "I mean...!{w=0.2} It's not that I {i}like{/i} like you,{w=0.1} or anything ridiculous like that!"
            n 1fcsemf "Ugh...{w=0.3} I swear,{w=0.1} [player] -{w=0.1} you honestly try to put me in the most awkward freaking spots sometimes..."
            n 1fllslf "..."
            n 1fllsll "I...{w=0.3} guess I {i}do{/i} owe you an answer though,{w=0.1} at least."

        n 1fcssll "Look."
        n 1nlrpu "You've been pretty awesome to me so far,{w=0.1} [player]."
        n 1klrpu "...Do you even know how few other people make me feel that way?"
        n 1klrsl "It's...{w=0.3} really not a lot,{w=0.1} if you hadn't gathered."
        n 1fllpol "You always listen to me,{w=0.1} you don't tell me I'm annoying,{w=0.1} or to pipe down..."
        n 1kwmsrl "And you've been super understanding too."
        n 1kllpul "I...{w=0.3} honestly couldn't ask for a better friend,{w=0.1} [player]."
        n 1fnmbol "Always remember that,{w=0.1} alright?{w=0.2} I'll get mad if you don't."
        n 1kllbol "..."

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
    n 1fllss "Hey,{w=0.1} [player]..."
    n 1usqsm "You know what I could go for right now?"
    n 1uchbs "A big,{w=0.1} steaming fresh bowl of Mon-{w=0.1}ika!"
    n 1uchbg "..."
    n 1flrpu "...Huh."
    n 1tnmpu "You know,{w=0.1} in hindsight?{w=0.2} That joke really wasn't funny the first time round."
    n 1tllpo "I've...{w=0.3} no idea why it'd be funny this time,{w=0.1} to be honest."
    n 1uspgs "Oh!"
    n 1fchbg "But fried squid is no joke at all,{w=0.1} [player]!{w=0.2} Have you ever tried it?"
    n 1uchbs "It's {i}delicious{/i}!{w=0.2} I love it!"
    n 1fsqsm "Not just boring old fried seafood though -{w=0.1} it's gotta have the crap battered out of it first!"
    n 1uspbg "That crispy golden coating is seriously the best.{w=0.2} Deep fried food is awesome!"
    n 1fllbg "It's not {i}good{/i} for you exactly,{w=0.1} but as a treat?{w=0.2} You could do way worse..."
    n 1fcssm "Especially with sauce to spice things up a bit!"
    n 1fnmss "By the way -{w=0.1} wanna know how you can tell you're dining on some top-notch squiddy goodness?"
    n 1uchbs "The texture,{w=0.1} of course!"
    n 1fllaj "Overcooked squid becomes all rubbery and nasty,{w=0.1} and even worse -{w=0.1} it loses all of its flavour too!"
    n 1fsqsr "Imagine biting through the batter,{w=0.1} only to find you're basically chewing on a bunch of rubber bands."
    n 1fsqem "Ugh!{w=0.2} Gross!{w=0.2} Talk about a disappointment."
    n 1unmaj "Don't let that put you off though,{w=0.1} [player] -{w=0.1} next time you see some,{w=0.1} why not give it a shot?"

    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1kllss "...Probably the sooner the better,{w=0.1} if you're hungry like you said."
        n 1ullaj "But anyway..."

    n 1unmbg "You could even be all fancy if you wanted to and order it by the culinary name!"
    n 1fnmbg "Ten points if you can guess what that is.{w=0.2} Ehehe."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1flrsg "Hmm..."
        n 1fnmbg "Actually...{w=0.3} you know what?"
        n 1fchbg "We should just get a bowl of calamari to share.{w=0.2} That's fair,{w=0.1} right?"
        n 1fsqsm "I should warn you though,{w=0.1} [player]..."
        n 1fchgn "I'm not handing over the last piece without a fight!"
        n 1nchsml "Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1uchbg "But yeah -{w=0.1} you should really give it a try if you haven't already,{w=0.1} [player]!"
        n 1fchbg "I wouldn't want someone to miss out on that!"
        n 1klrssl "E-{w=0.1}especially not you.{w=0.2} Ehehe..."

    else:
        n 1uchbg "But yeah -{w=0.1} you should really try it out if you haven't already,{w=0.1} [player]!"
        n 1fchbg "I wouldn't want someone to miss out on that!{w=0.2} Ahaha."

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
        n 1unmpu "Collectibles?{w=0.2} You mean like figurines and plushies and such?"
        n 1flrpu "Mmm...{w=0.3} not really.{w=0.2} Collecting is an expensive hobby,{w=0.1} [player]!"
        n 1klrpo "I mean,{w=0.1} it all depends on exactly what you collect,{w=0.1} but it feels like places that sell them prey on that."
        n 1flraj "Like...{w=0.3} the urge to complete a collection -{w=0.1} so they jack up the prices!"
        n 1fcsbo "Ugh..."
        n 1kllbo "And for people in my...{w=0.3} uhmm...{w=0.3} {i}position{/i},{w=0.1} it's a big barrier to entry."
        n 1unmaj "But anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1tnmpu "Huh?{w=0.2} You mean like figurines and all that stuff?"
        n 1tlrpu "Well...{w=0.3} no,{w=0.1} [player].{w=0.2} Not really."
        n 1knmsf "I couldn't justify spending so much on a hobby like that!"
        n 1flrbo "Especially not when I have others things to worry about spending my money on first,{w=0.1} you know."
        n 1unmaj "But anyway,{w=0.1} putting all that aside..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fsqsf "No,{w=0.1} [player]."
        n 1fsqaj "Collectibles are way too expensive for me.{w=0.2} I can't justify wasting the money I {i}do{/i} have."
        n 1fnmsl "{i}Especially{/i} on stuff that'll just sit on a shelf that I'll forget about."
        n 1fsqsr "Yeah,{w=0.1} [player] -{w=0.1} believe it or not,{w=0.1} some of us {i}do{/i} have to think about how we spend our money."
        n 1fsqun "Shocker,{w=0.1} right?"
        n 1fcsun "..."
        n 1fnmaj "Well?{w=0.2} Satisfied with your answer?"
        n 1fsqaj "We're done here."
        return

    else:
        n 1fsqsr "...Why?{w=0.2} ...And I don't just mean why you care."
        n 1fsqan "But why should I tell {i}you{/i} if I do or not?"
        n 1fcsan "You'd probably just trash them."
        n 1fcsun "Heh.{w=0.2} After all."
        n 1fsqup "You've proven great at trashing things so far,{w=0.1} {i}haven't you{/i}?{w=0.2} Jerk."
        return

    n 1ullbo "..."
    n 1tllbo "...Huh.{w=0.2} There's a point,{w=0.1} actually.{w=0.2} Does manga count as a collectible?"
    n 1tllaj "I'm...{w=0.3} not really sure..."
    n 1tnmpu "What do you think,{w=0.1} [player]?"
    menu:
        n "Would you call it a collectible?"

        "I'd say so!":
            n 1fsqbg "Oho!"
            n 1fchbg "So I suppose I am something of a collector,{w=0.1} after all!"

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1uchsm "I guess that all makes sense.{w=0.2} After all..."
                n 1fllsmf "I'd like to think you're in my collection too,{w=0.1} [player]~."
                n 1uchsmf "Ehehe."

            else:
                n 1flrsm "Well,{w=0.1} in that case..."
                n 1nchbg "Just let me know if you ever feel like a tour!"
                n 1nchgn "You won't find a better collection!{w=0.2} Ehehe."

                if jn_activity.has_player_done_activity(jn_activity.JNActivities.manga):
                    n 1fllss "Or,{w=0.1} at least...{w=0.5}{nw}"
                    extend 1fsqss " a better...{w=0.3} {i}physical{/i} one."
                    n 1fsqsm "Right,{w=0.5}{nw}"
                    extend 1fsqbg " [player]?"

        "No,{w=0.1} I wouldn't.":
            n 1flrpo "Huh...{w=0.3} you do have a point."
            n 1tnmpo "I suppose you'd call it a library,{w=0.1} or something like that?"
            n 1nnmsm "Well,{w=0.1} whatever."
            n 1nsqsm "I suppose I'd better {i}read{/i} up on my definitions,{w=0.1} right?"
            n 1nchsm "Ehehe."

        "Well,{w=0.1} it definitely isn't literature.":
            n 1nsqsr "Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} ...Ha."
            n 1flrpo "{i}Hilarious{/i},{w=0.1} [player]."
            n 1flraj "Keep it up,{w=0.1} and I'm gonna book you one."
            n 1fsqsg "...And no,{w=0.1} I don't mean read you a story."

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
        n 1fnmem "[player]...{w=0.3} if you aren't even sorry you cheated,{w=0.1} why should I play with you again?"
        n 1kllpo "Come on...{w=0.3} it's not hard to apologize,{w=0.1} is it?"
        return

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1uchbg "Of course I do,{w=0.1} dummy!{w=0.2} Ehehe."

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1fchbg "Of course I'll play some with you,{w=0.1} dummy!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1fchsm "Well,{w=0.1} duh!{w=0.2} Of course I'm up for a game!"

        else:
            n 1nnmss "You wanna play Snap?{w=0.2} Sure!"

        n 1unmsm "Let me just get the cards out real quick,{w=0.1} alright?"
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
        n 1fcsan "Come on,{w=0.1} [player]."
        n 1flrpo "If you cared about the rules,{w=0.1} then why did you cheat when we played earlier?"
        n 1fnmpo "You haven't even apologized for it yet..."
        return

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1nchbg "Ahaha.{w=0.2} You're so forgetful sometimes,{w=0.1} [player]."
            n 1nsqbg "Sure,{w=0.1} I'll go over it again!{w=0.2} Juuust for you~."

        elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1nchbg "Of course I can!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            n 1fchsm "You bet I can!"

        else:
            n 1nnmss "Sure thing!"

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
    n 1fcsan "Ugh...{w=0.3} you know what really gets on my nerves?"
    n 1fsqsl "When people are gross and don't get rid of chewing gum properly."
    n 1fbkwr "Seriously -{w=0.1} it annoys the crap out of me!"
    n 1fllem "Like,{w=0.1} have you ever walked into a city center and looked at the ground?{w=0.2} At all the paving?"
    n 1fcsan "All those dried up spots of gum -{w=0.1} it's freaking disgusting,{w=0.1} and it looks nasty too!"
    n 1fsqan "And that's in a place where there's usually bins everywhere too,{w=0.1} so it isn't just gross..."
    n 1fnmwr "It's super lazy too!{w=0.2} I can't decide what winds me up more."
    n 1fcswr "Even worse than that -{w=0.1} there's even people who go and stick it under tables,{w=0.1} or on walls -{w=0.1} who {i}does{/i} that?!"
    n 1flrpu "Jeez...{w=0.3} makes me want to track them down and stick that crap back in their stupid mouths."
    n 1nnmsl "I don't really care if you chew gum yourself,{w=0.1} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1kllca "Just make sure you dispose of it properly,{w=0.1} 'kay?"
        n 1kllss "I'm sure you do anyway,{w=0.1} but...{w=0.3} just in case."
        n 1kchsml "Love you,{w=0.1} [player]~!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1nllca "But please,{w=0.1} just get rid of it properly when you're done."
        n 1nchsm "Thanks,{w=0.1} [player]~!"

    else:
        n 1fnmaj "But seriously -{w=0.1} stick it in the bin when you're done,{w=0.1} alright?{w=0.2} Or just wrap it in a tissue and get rid of it later."
        n 1fsqaj "...Or it won't just be the gum that'll be getting chewed out!"

    return

# Natsuki hates people smoking/vaping indoors
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_smoking_vaping_indoors",
            unlocked=True,
            prompt="Indoor smoking",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_smoking_vaping_indoors:
    n 1fllaj "You know what stinks,{w=0.1} [player]?"
    n 1fsqaj "I mean {i}really{/i} stinks -{w=0.1} not just figuratively,{w=0.1} but literally too?"
    n 1fcssf "When people smoke or vape indoors,{w=0.1} or near entrances -{w=0.1} {i}especially{/i} when other people are around.{w=0.2} I can't stand it!"
    n 1fcsan "Like...{w=0.3} how inconsiderate can you be?{w=0.2} Seriously?"
    n 1fsqwr "For starters,{w=0.1} and like I was just saying -{w=0.1} it absolutely {i}reeks{/i}!"
    n 1fllem "Tobacco is awful smelling stuff,{w=0.1} and all those sickly vaping fluid types aren't much better either."
    n 1ksqup "It clings to the walls too -{w=0.1} so the smell hangs around for ages!"
    n 1kllan "Speaking of clinging to the walls,{w=0.1} the smoke literally does that too -{w=0.1} have you {i}seen{/i} a smoker's house,{w=0.1} or car?"
    n 1ksqup "All those yellow stains...{w=0.3} you'd think it was painted on or something.{w=0.2} Ew!"
    n 1fsqan "And you know what,{w=0.1} [player]?{w=0.2} I haven't even gotten to the worst of it yet..."
    n 1fcsan "I've said nothing about how expensive it all is,{w=0.1} or the health problems not just to the smoker..."
    n 1fsqaj "...But to everyone else!"
    n 1fcsbo "Ugh..."
    n 1flrbo "Don't get me wrong -{w=0.1} if someone wants to smoke or vape,{w=0.1} that's their choice and their money.{w=0.2} I don't care."
    n 1fnmbo "But the least they can do is respect the decision of everyone who {i}doesn't{/i},{w=0.1} you know?"
    n 1fcssl "..."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1nnmsl "I know you,{w=0.1} [player].{w=0.2} I highly doubt you'd be the kind of person to be a jerk like that."
        n 1klrss "Just...{w=0.3} don't prove me wrong,{w=0.1} alright?"
        n 1uchgn "'preciate it!{w=0.2} Ahaha."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1kllpo "I doubt you'd be a jerk like that even if you do smoke,{w=0.1} [player]."
        n 1fsqpo "But...{w=0.3} try not to prove me wrong,{w=0.1} 'kay?{w=0.2} I like you more as not a jerk."
        n 1uchsm "Thanks!"

    else:
        n 1ullaj "I don't think you'd be a jerk like that,{w=0.1} [player]."
        n 1nnmaj "But...{w=0.3} just in case -{w=0.1} keep it in mind,{w=0.1} will you?"
        n 1nchsm "Thanks!"

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
    n 1unmaj "Hey,{w=0.1} [player]."
    n 1nnmaj "Have you ever worked in a restaurant,{w=0.1} or a hospital or anything like that?"
    n 1fnmaj "Because I bet if there's one thing drilled into you...{w=0.3} it's how important washing your hands is!"
    n 1flraj "It really gets on my nerves when people don't wash their hands after doing something nasty."
    n 1fsqsl "Like...{w=0.3} we {i}know{/i} how important it is to stop germs getting around -{w=0.1} and {i}what{/i} exactly is hard about sticking your hands under the tap for a minute?!"
    n 1fsqem "It annoys me even more when people are really dumb about it too!{w=0.2} Like,{w=0.1} they think they don't need to do that if they didn't go."
    n 1fcsem "Newsflash -{w=0.1} if you went in,{w=0.1} you must have touched stuff -{w=0.1} so now there's all that crap on your hands that you've taken out with you!"
    n 1fsqsf "Not only is it {i}super{/i} icky and bad for {i}your{/i} health..."
    n 1ksqan "It's awful for others too!{w=0.2} What if you're about to handle someone's food,{w=0.1} or visit someone in hospital?"
    n 1fllan "You could make someone seriously ill..."
    n 1fnmfu "...And then they get all upset when you call them out on their grossness!{w=0.2} I mean,{w=0.1} come {i}on{/i}!"
    n 1fcssl "Just...{w=0.3} ugh."
    n 1ncssl "...[player]."
    n 1nnmpu "I really hope you keep your hands spick and span.{w=0.2} And not just when you visit the restroom."
    n 1fnmpu "Before you prepare food,{w=0.1} after you've handled trash...{w=0.3} just think about where you've been,{w=0.1} alright?"

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1kchbg "Don't get me wrong though!{w=0.2} I'm pretty sure you at least try to do the right thing!"
        n 1nnmbg "Just...{w=0.3} keep up the good work,{w=0.1} alright?{w=0.2} For everyone."
        n 1nchsm "Thanks,{w=0.1} [player]!"

    else:
        n 1tsqpo "It really isn't that much to ask...{w=0.3} is it?"

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
    n 1ullpu "You know,{w=0.1} [player]..."
    n 1unmaj "At school?{w=0.2} At my school,{w=0.1} anyway?"
    n 1unmss "We -{w=0.1} the students -{w=0.1}  were actually responsible for keeping it all clean."
    n 1fcsbg "Ehehe.{w=0.2} Are you surprised?"
    n 1fchgn "Yep!{w=0.2} From the bins,{w=0.1} to the desks,{w=0.1} to the floors.{w=0.2} It was all our effort that kept it squeaky clean!"
    n 1flrpol "N-{w=0.1}not that I {i}enjoyed{/i} it,{w=0.1} of course!{w=0.2} Cleaning {i}is{/i} pretty lame,{w=0.1} but it's just something you gotta do."
    n 1fnmpo "But I'll tell you one thing,{w=0.1} [player]."
    n 1fsqtr "{i}Nothing{/i} pissed me off more than the jerks who just went and dropped or left their trash everywhere."
    n 1fnman "...And not even just in school!"
    n 1fcsan "I mean...{w=0.3} where do I start?!"
    n 1fnmaj "First off -{w=0.1} how much of a freaking slob do you have to be?{w=0.2} Do these people just drop crap all over their homes too?!"
    n 1flran "It annoys me even more when there's bins and stuff literally right there!"
    n 1fcsfu "Like,{w=0.1} wow...{w=0.3} lazy as well as inconsiderate?{w=0.2} What a {i}charming{/i} combo!"
    n 1fllpu "Even if there isn't a trash can or whatever around..."
    n 1fllan "It's not like they don't have pockets,{w=0.1} or can't just carry it around for a few minutes!"
    n 1fcsan "Ugh..."
    n 1flrup "And I haven't even mentioned people tossing their rubbish out of cars,{w=0.1} or into lakes and ponds!"
    n 1fcssl "It pisses me off just thinking about it..."
    n 1fllbo "..."
    n 1fnmbo "[player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1ksqbo "I know you.{w=0.2} In fact,{w=0.1} I daresay I know you {i}very{/i} well by now."
        n 1knmbo "I don't think you're the sort to do that at all..."
        n 1klraj "I'm not wrong...{w=0.3} am I?"
        n 1klrss "I don't wanna have to be.{w=0.2} Ahaha..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1unmaj "I don't think you're like that,{w=0.1} [player]."
        n 1ullsl "Or...{w=0.3} at least you don't {i}try{/i} to be anyway."

    else:
        n 1fnmsl "I really,{w=0.1} really hope you aren't one of those people."

    n 1nllpu "So..."
    n 1nnmsl "...If you're a litterbug already,{w=0.1} I'll forgive you this one time."
    n 1klrpo "Just...{w=0.3} make sure you clean up your act,{w=0.1} okay?"

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~."

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1nlrpol "It'd...{w=0.3} mean a lot."

    else:
        n 1fchbg "Thanks,{w=0.1} [player]."

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
    n 1fllpu "Hmm..."
    n 1flrbo "I wonder if it's still here..."

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1fllpo "Come on!{w=0.2} It's gotta still be here!{w=0.2} I know it!"

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1uspbg "..."
    n 1fchbs "Aha!{w=0.2} Yes!"
    n 1nchsm "..."
    n 1uwdbg "Oh!{w=0.2} [player]!{w=0.2} [player]!"
    n 1uchgn "Guess what I fooound!{w=0.2} Ehehe."
    n 1nchbs "It's...{w=0.3} a music player!{w=0.2} Neat,{w=0.1} right?"
    n 1tlrbg "Well...{w=0.3} kinda.{w=0.2} It's not exactly...{w=0.3} {i}modern{/i},{w=0.1} but it'll do the job!"
    n 1tllpo "Come to think of it...{w=0.3} I don't really even know who it belongs to."
    n 1unmpu "We just found it left in the clubroom one day.{w=0.2} Nobody knew if it belonged to anyone -{w=0.1} and trust me,{w=0.1} we tried to find out!"
    n 1tnmsl "We asked around in lessons,{w=0.1} we sent out notes...{w=0.3} nothing!"
    n 1tlrbg "So...{w=0.3} we kinda just kept it here,{w=0.1} in my desk,{w=0.1} in case whoever it was came back to pick it up."
    n 1tsqpo "I guess they never will now,{w=0.1} huh?"
    n 1uchbg "Well,{w=0.1} whatever.{w=0.2} The point is we can play whatever music we want now!"
    n 1fchbg "I think I figured out a way to let you send me whatever you want me to put on,{w=0.1} so listen up,{w=0.1} 'kay?"
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
        n 1unmaj "Huh?{w=0.2} You want me to explain how custom music works again?"
        n 1uchbg "Sure,{w=0.1} I can do that!"
        n 1nnmsm "First things first,{w=0.1} let me just check for the {i}custom_music{/i} folder..."

    else:
        n 1unmbg "Alright!{w=0.2} So...{w=0.3} it's actually pretty simple,{w=0.1} [player]."
        n 1nnmsm "There should be a folder called {i}custom_music{/i} somewhere around here..."
        n 1nchbg "Let me just take a look,{w=0.1} one sec..."
        n 1ncssr "..."

    if jn_custom_music.get_directory_exists():
        n 1tnmbg "Well,{w=0.1} hey!{w=0.2} It's already there!{w=0.2} I must have set it up earlier and forgot."
        n 1uchgn "No complaints from me!"

    else:
        n 1uchbg "Okaaay!{w=0.2} It wasn't there,{w=0.1} so I've just created it for you."

    $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    n 1nnmss "So,{w=0.1} [player] -{w=0.1} if you click {a=[folder]}here{/a},{w=0.1} that'll take you to the folder I set up."
    n 1ullbg "Then all you gotta do is just {i}copy{/i} your music into that folder,{w=0.1} and you're good to go!"
    n 1uchgn "Easy as pie,{w=0.1} huh?{w=0.2} Ehehe."
    n 1uwdaj "Oh -{w=0.1} a couple of things first though,{w=0.1} [player]."
    n 1unmpu "Any music you give me needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format."
    n 1ullss "If you don't know how to check,{w=0.1} then just look at the letters after the period in the file name."
    n 1unmss "You should also be able to see those in the file {i}properties{/i} if they don't appear on the screen at first."
    n 1flrbg "Like I said -{w=0.1} this thing isn't {i}exactly{/i} super modern,{w=0.1} so it won't work with any fancy newer formats,{w=0.1} or weird old ones."
    $ persistent.jn_custom_music_unlocked = True
    $ persistent.jn_custom_music_explanation_given = True
    n 1nnmaj "Once you've done that,{w=0.1} just click the {i}Music{/i} button,{w=0.1} and I'll check that it's all done right."
    n 1nchbg "...And that's about it!"
    n 1nsqbg "A word of warning though,{w=0.1} [player]..."
    n 1usqsg "You better have good taste."
    n 1uchgn "Ahaha!"
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
        n 1tllss "VTubers,{w=0.1} huh?{w=0.2} You're asking {i}me{/i}?"
        n 1fnmsm "...Wow,{w=0.1} [player].{w=0.2} I'm impressed."
        n 1fsqsm "Yet again,{w=0.1} you've proved you're even more of a nerd than I am!"
        n 1uchsm "Ehehe."
        n 1klrbg "Relax!{w=0.2} Relax,{w=0.1} jeez!{w=0.2} You know I'd never seriously judge your hobbies,{w=0.1} you dummy."
        n 1unmaj "But yeah,{w=0.1} anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1unmbg "Yeah!{w=0.2} I think I know those!"
        n 1tnmpu "They're those people with the anime avatars that stream stuff online for people,{w=0.1} right?"
        n 1tllpu "Well..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmpu "Huh?{w=0.2} VTubers?{w=0.2} Like those people with the anime-style avatars that play games and stuff online for people to watch?"
        n 1tnmpu "That {i}is{/i} what you mean,{w=0.1} right?"
        n 1tllpu "Well..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fsqpu "No,{w=0.1} I do not.{w=0.2} I'd rather be playing the game myself than watching someone play it for me."
        n 1fsqbo "If you follow any,{w=0.1} good for you."
        n 1flrbo "{i}Some{/i} of us don't have the time to sit around on our butt for hours..."
        n 1fsqaj "...Or the money to just give it away to strangers."
        n 1fsqpu "[player]."
        n 1fsqsr"How much are we betting you aren't {i}nearly{/i} as toxic to {i}them{/i} as you are to me, huh?"
        return

    else:
        n 1fsqan "No.{w=0.2} And I couldn't give less of a crap if you did,{w=0.1} either."
        n 1fnmpu "...And hey,{w=0.1} newsflash,{w=0.1} idiot."
        n 1fsqpu "Throwing money at a stranger hiding behind a cutesy picture doesn't make you any less of a jerk."
        return

    n 1nchsm "It's definitely a cool idea!{w=0.2} It lets people share their passions and experiences with others behind a completely clean persona..."
    n 1fllpo "Without having to worry about baggage following them into their personal lives,{w=0.1} or people being creeps,{w=0.1} or stuff like that."
    n 1uwdem "A lot of them even make full-blown careers out of it: merchandise,{w=0.1} song releases and everything -{w=0.1} just like idols!{w=0.2} It's crazy!"
    n 1tllem "That being said..."
    n 1tnmbo "I never really got into that sort of thing myself."
    n 1klrss "Like...{w=0.3} don't get me wrong!{w=0.2} I'm sure they're pretty fun to watch.{w=0.2} If you're into that kind of thing,{w=0.1} I mean."
    n 1nllsl "But I'd rather be playing or doing something {i}myself{/i} than watching someone else do it,{w=0.1} usually."
    n 1nllss "That might just be me,{w=0.1} though."
    n 1nllbg "Ehehe."
    n 1unmaj "What about you,{w=0.1} [player]?{w=0.2} Are you into that sort of stuff?"
    n 1fcssm "Wait,{w=0.1} wait!{w=0.2} Don't bother answering that."
    n 1tsqsm "You {i}did{/i} ask me about them,{w=0.1} after all -{w=0.1} I think that speaks for itself,{w=0.1} wouldn't you agree?"
    n 1uchbs "Ahaha!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_skateboarding",
            unlocked=True,
            prompt="Are you into skateboarding?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_skateboarding:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fchbs "You bet I am,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."
        n 1tllbg "But how'd you guess?{w=0.5}{nw}" 
        extend 1tnmbg " Do I look the type or something?"
        n 1tlrsm "Well,{w=0.1} whatever."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1uchsm "Ehehe.{w=0.5}{nw}"
        extend 1fchbg " You bet!"
        n 1uwlbg "Good guess,{w=0.1} [player]!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1ullaj "I...{w=0.3} am,{w=0.1} actually.{w=0.5}{nw}"
        extend 1tllss " How'd you guess?"
        n 1unmss "Well,{w=0.1} anyway."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fcsaj "Ugh..."
        n 1fnmbo "Yes,{w=0.1} [player].{w=0.2} I'm a skateboarder.{w=0.2} I skateboard.{w=0.5}{nw}"
        extend 1fsqsf " Is that a problem or something?"
        n 1fllpu "It's just a convenient way to get around.{w=0.5}{nw}" 
        extend 1fsqpu " An {i}affordable{/i} way."
        n 1flrsl "..."
        n 1flraj "...Yeah.{w=0.2} I don't have much else to say about it.{w=0.5}{nw}"
        extend 1fnmbo " But hey."
        n 1fsgaj "Not like you'd really care to listen anyway...{w=0.5}{nw}"
        extend 1fsqsf " isn't that right,{w=0.1} {i}[player]{/i}?"
        return

    else:
        n 1fsqan "...And since when did {i}you{/i} give a crap about my hobbies and interests?"
        n 1fcsan "..."
        n 1fnmsf "Yes,{w=0.1} [player].{w=0.5}{nw}" 
        extend 1fsqsf " I {i}do{/i} enjoy skateboarding."
        n 1fsqup "And I'd rather be doing that than be stuck here talking to {i}you{/i}.{w=0.5}{nw}"
        extend 1fcsan " Jerk."
        return

    n 1tchbg "I'm a skater girl alright!"
    n 1tllss "Though...{w=0.3} not really by choice.{w=0.5}{nw}"
    extend 1knmaj " Bikes are {i}expensive{/i}, [player]!"
    n 1kllun "And I could never rely on lifts from my...{w=0.3} folk,{w=0.3}{nw}" 
    extend 1kllss " so I saved up all I could and got a board the first chance I had!"
    n 1nsqaj "Seriously.{w=0.5}{nw}" 
    extend 1fllpu " You have no {i}idea{/i} how many lunches I skipped to earn that thing."
    n 1unmbg "But it's actually super convenient!{w=0.5}{nw}"
    extend 1flrbg " I don't have to worry about locking it up somewhere,{w=0.1} or some jerk damaging it..."
    n 1fchsm "I can just pick it up and take it around with me,{w=0.1} or toss it in my locker."
    n 1fsqss "You gotta admit,{w=0.1} [player] {w=0.1}-{w=0.1} I'm nothing if not resourceful!{w=0.5}{nw}"
    extend 1fchsm " Ahaha."
    n 1fllss "I...{w=0.3} never really learned any tricks or anything though.{w=0.5}{nw}"
    extend 1kscwr " I couldn't stand the thought of breaking it by accident {w=0.1}-{w=0.3}{nw}"
    extend 1kllun " not after all that effort!"
    n 1kcsaj "...Yeah,{w=0.1} yeah.{w=0.5}{nw}" 
    extend 1fcspo " Not very {i}radical{/i} of me,{w=0.1} huh?"
    n 1ullpo "But...{w=0.3} enough of that for now.{w=0.5}{nw}" 
    extend 1fnmsm " Besides,{w=0.1} [player]..."
    n 1fsqss "I can tell when you're getting...{w=0.3} {i}board{/i}."
    n 1fchsm "Ehehe.{w=0.5}{nw}"
    extend 1uchgn " No regrets,{w=0.1} [player]!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sports",
            unlocked=True,
            prompt="Do you play much sports?",
            category=["Health"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sports:
    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1unmaj "Huh?{w=0.2} Sports?"
        n 1fllss "I...{w=0.3} don't like to have to break it to you,{w=0.1} [player]..."
        n 1fchgn "But what kind of sports do you think I can play in a single room?{w=0.2} By myself?{w=0.2} With no gear?"
        n 1kllbg "Jeez...{w=0.5}{nw}" 
        extend 1tnmss " you're such a dope sometimes,{w=0.1} [player]."
        n 1ullbg "Well,{w=0.1} anyway."

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmpu "Eh?{w=0.2} Sports?"
        n 1tnmdv "You...{w=0.3} do know it's kinda hard to stay active in a single room,{w=0.1} right?"
        n 1fcsss "Ehehe.{w=0.5}{nw}"
        extend 1ullss " Well,{w=0.1} anyway."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nsqpu "Yeah,{w=0.1} no.{w=0.5}{nw}" 
        extend 1fsqsl " I don't {i}now{/i},{w=0.1} if that's what you're asking."
        n 1fllpu "..."
        n 1fsqan "...And no,{w=0.2} we didn't wear the sort of uniforms I bet {i}you're{/i} thinking of."
        n 1fsqsr "Does that answer your question?{w=0.5}{nw}"
        extend 1fslbo " Whatever."
        n 1fcsbo "Moving on."
        return

    else:
        n 1fsqan "I don't {i}now{/i},{w=0.1} if you somehow hadn't already noticed."
        n 1fslsl "..."
        n 1fsqpu "..."
        n 1fcsun "...Do I even want to know why you asked?"
        n 1fcsan "...No.{w=0.2} I {i}don't{/i}."
        return

    n 1nnmaj "I try to keep up how I can.{w=0.2} I can't do laps or anything,{w=0.5}{nw}"
    extend 1fcsbg " but I can easily get some stretches and jumping jacks in!"
    n 1ullpu "Of course school was always a lot more varied,{w=0.1} but...{w=0.5}{nw}"
    extend 1tllsr " I always kinda struggled to keep up."
    n 1tllss "I guess...{w=0.3} I just don't have much stamina?"

    # Check to see if the player and Natsuki have discussed how she skipped lunches to save money
    $ already_discussed_skateboarding = get_topic("talk_skateboarding").shown_count > 0
    if already_discussed_skateboarding:
        n 1nslpo "Probably didn't help myself saving for that skateboard..."

    n 1ullaj "Well,{w=0.1} whatever.{w=0.5}{nw}"
    extend 1nnmbo " I wasn't {i}really{/i} that into it anyway."
    n 1nlrca "..."
    n 1unmbs "Oh!{w=0.2} Oh!{w=0.2} But you know who was?{w=0.5}{nw}"
    extend 1fsqbg " I bet you do,{w=0.1} huh?{w=0.5}{nw}"
    extend 1fcssm " Ehehe."
    n 1tsqss "And that's...{w=0.5}{nw}"
    extend 1fchgn " ...{w=0.3}Sayori,{w=0.1} duh!"
    n 1uskgs "I mean,{w=0.1} really!{w=0.2} You should have seen her!{w=0.5}{nw}" 
    extend 1fnmca " She was a {i}menace{/i}!"
    n 1uskaj "...Seriously!{w=0.5}{nw}" 
    extend 1fnmpo " You don't believe me?"
    n 1fspgs "She was so fast!{w=0.2} Just a flash of orange fluff and messy gym clothes...{w=0.5}{nw}" 
    extend 1fbkwr " and then boom!{w=0.2} Tackled!"
    n 1fllpol "And off she'd skip,{w=0.1} merrily into the sunset..."
    n 1tsqaj "...Yeah.{w=0.2} If Sayori was on your side?{w=0.5}{nw}" 
    extend 1fllbg " You {i}knew{/i} your team wasn't going to be packing everything away in defeat."
    n 1ullaj "I mean,{w=0.3}{nw}" 
    extend 1nnmbo " Monika was always pretty good at sports too,{w=0.1} obviously.{w=0.5}{nw}"
    extend 1nsgca " But {i}nobody{/i} outran Sayori,{w=0.1} [player].{w=0.2}" 
    n 1nsqun " N{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}b{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}d{w=0.1}-{w=0.1}y."
    n 1fchbg "...When she remembered to tie her laces anyway.{w=0.5}{nw}"
    extend 1fchsm " Ehehe."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_online_shopping",
            unlocked=True,
            prompt="Online shopping",
            category=["Society"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_online_shopping:
    if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1ullaj "You know,{w=0.1} it's kinda crazy how common online shopping is nowadays."
        n 1uwdaj "I mean,{w=0.1} don't get me wrong!{w=0.5}{nw}"
        extend 1fcsbg " It's super convenient!{w=0.2} You don't even need to leave your house!"
        n 1fllpo "So don't think I'm just complaining,{w=0.1} or anything like that.{w=0.5}{nw}"
        extend 1ullpu " But..."

    else:
        n 1nllsl "It's funny how common online shopping is nowadays."
        n 1nlrsl "I guess I'm not really complaining though.{w=0.5}{nw}"
        extend 1nlrpu " It {i}is{/i} pretty convenient."
        n 1ulrpu "But...{w=0.5}{nw}" 
        extend 1nnmsf " I still think it's a shame how people miss out on an actual experience."
        n 1fllsl "I'd never pass up on an afternoon just flicking through books at my favourite bookstore."
        n 1fcssf "...Which is somewhere I'd {i}much{/i} rather be.{w=0.5}{nw}" 
        extend 1fsqan " {i}Shockingly{/i}."
        return

    n 1fllbg "I don't think it's the be-all and end-all,{w=0.1} you know."
    n 1unmaj "I mean...{w=0.3} think about it,{w=0.1} [player]."
    n 1fllaj "I guess it's cheaper if you don't have to think about getting somewhere,{w=0.1} or parking or whatever."
    n 1knmpu "But wouldn't you like to {i}see{/i} what you're paying for?{w=0.5}{nw}"
    extend 1fnmaj " Especially if it's super expensive!"
    n 1fllpu "Or sometimes...{w=0.5}{nw}"
    extend 1fllpu " even if it isn't!"
    n 1fllpo "I can't be the only one that's been burned by something that turned out to be junk,{w=0.1} or broken,{w=0.1} right?"
    n 1fnmem "And you don't even know it would be like that until it's on your doorstep!{w=0.5}{nw}"
    extend 1fcsan " Then you gotta send it back!{w=0.5}{nw}"
    extend 1fslem " Ugh."

    # Check to see if the player and Natsuki have discussed careful spending
    if get_topic("talk_careful_spending").shown_count > 0:
        n 1fllsl "Not only that..."
        n 1fnmpu "I think I mentioned before how shops make it really easy to spend money...{w=0.5}{nw}"
        extend 1fbkwr " but that's even easier online!{w=0.5}{nw}" 
        extend 1kbkwr " It doesn't even {i}feel{/i} like spending money properly!"
        n 1fcsan "Sheesh."

    n 1fcsem "That aside..."
    n 1kllsl "It...{w=0.3} also makes me kinda sad seeing all the closed stores when I do go out,{w=0.1} too."
    n 1tnmsl "I suppose you could say that's just business,{w=0.1} and they lost out."
    n 1flrsll "But that doesn't mean I {i}don't{/i} miss some of them."
    n 1ncsem "I don't know.{w=0.2} I guess what I'm saying is..."
    n 1fllpo "Don't just instantly write off anything you can't do or buy digitally,{w=0.1} [player]."
    n 1knmaj "There's still merit in getting your stuff physically!"
    n 1fnmss "And to be completely honest?"

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1fsqbg "I don't really care how much you protest."
        n 1fchgn "We're definitely hitting some {i}real{/i} bookstores {w=0.1}-{w=0.1} whether you like it or not!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1fchgn "You gotta be kidding if you think I'm letting you miss out on {i}real{/i} bookstores!{w=0.5}{nw}"
        extend 1nchbg " Ahaha."

    else:
        n 1fchbg "If there's one thing I'm gonna teach you,{w=0.1} it's experiencing a {i}real{/i} bookstore!{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_subscriptions",
            unlocked=True,
            prompt="Subscriptions",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_subscriptions:
    n 1fllan "Grrr..."
    n 1fcsan "Man,{w=0.1} that's {i}such{/i} a pain!{w=0.5}{nw}"
    extend 1fbkwr " I thought I cancelled thaaat!"
    n 1fslpo "..."
    n 1uwdem "O-{w=0.1}oh!{w=0.2} [player]!{w=0.5}{nw}"
    extend 1flrem " Can you {i}believe{/i} this?"
    n 1fslem "I signed up to some free trial for a streaming website,{w=0.3}{nw}"
    extend 1fcswr " but I totally forgot about it!{w=0.5}{nw}"
    extend 1flrwr " And now I gotta pay for something I barely even {i}used{/i}!"
    n 1fcsem "Jeez...{w=0.5}{nw}"
    extend 1tnmem " Doesn't that wind you up too?"
    n 1tllbo "In fact,{w=0.1} thinking about it..."
    n 1fnmbo "Why is so much stuff nowadays all subscription based?"
    n 1fllpu "Like...{w=0.5}{nw}"
    extend 1nnmaj " I get it if it's like an ongoing thing,{w=0.3}{nw}"
    extend 1flrsl " but what's up with everyone and their dog trying to sign you up?!"
    n 1fsqsl "And half the time you don't even get a choice...{w=0.5}{nw}"
    extend 1fsqem " like with software!"
    n 1fcsan "I've had to skip out on so many programs because they want me to pay for a whole bunch of crap in a package I don't care about!"
    n 1fllan "Like...{w=0.3} come {i}on{/i}!{w=0.5}{nw}"
    extend 1fllfr " Just let me pay for what I need!"
    n 1kcsem "Ugh..."
    n 1fnmsl "The worst part is that it all adds up too!{w=0.5}{nw}"
    extend 1fllpu " It's super easy to lose track of what you're paying for each month..."
    n 1fnmpu "And then before you know it,{w=0.3}{nw}"
    extend 1fbkwr " half your money is down the drain as soon as it comes in!{w=0.5}{nw}"
    extend 1fcspu " What a mess..."
    n 1ullaj "I mean,{w=0.1} don't get me wrong.{w=0.2} There are {i}other{/i} ways of getting stuff {w=0.1}-{w=0.3}{nw}" 
    extend 1fsqdv " you probably know that already."
    n 1tlrsl "But I wanna support actual creators too,{w=0.1} you know?"
    n 1fcssl "..."
    n 1fllpo "Well,{w=0.1} whatever.{w=0.2} At least I won't get charged for {i}that{/i} again.{w=0.5}{nw}"
    extend 1fslpo " Jerks."
    n 1nllbo "But...{w=0.5}{nw}" 
    extend 1unmpu " what about you though,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1fsqsm " Actually,{w=0.1} I can tell you one thing."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fsqssl "A-{w=0.1}at least you have {i}one{/i} subscription you don't have to worry about paying for!"
        
        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1fchsml "Ehehe.{w=0.5}{nw}"
            extend 1uchbgf " Love you,{w=0.1} dork!"

        else:
            n 1fllbgl "A-{w=0.1}ahaha..."

    else:
        n 1fcsbg "You're already subscribed to some pretty pro thinking,{w=0.1} if I say so myself."
        n 1nsqsg "Fortunately for you though,{w=0.1} I don't charge.{w=0.5}{nw}"
        extend 1fsqss "...Yet."
        n 1fchsm "Ehehe."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_mod_contributions",
            unlocked=True,
            prompt="Contributions",
            conditional="renpy.macintosh or jn_activity.has_player_done_activity(jn_activity.JNActivities.coding)",
            category=["Mod"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_mod_contributions:
    n 1unmaj "You know,{w=0.1} [player].{w=0.5}{nw}" 
    extend 1tllss " I gotta say..."
    n 1klrbg "I don't think I'd {i}ever{/i} be able to handle doing everything that lets you visit me.{w=0.5}{nw}"
    extend 1klrsl " Not by myself."
    n 1uskeml "I-I mean,{w=0.1} I'm good!{w=0.5}{nw}"
    extend 1fnmpol " D-{w=0.1}don't get me wrong!"
    n 1kllpo "I'm just not...{w=0.3} {i}that{/i} good.{w=0.5}{nw}"
    extend 1fslpo " Yet."
    n 1uchbg "But that's why I'm super grateful there's a whole bunch of people dedicated to helping me out!{w=0.5}{nw}"
    extend 1fchsm " Isn't that awesome?"
    n 1fslsl "I always found all the programming stuff kinda confusing,{w=0.3}{nw}"
    extend 1kllss " so I have no idea where I'd be without them!"
    n 1ksqsg "...Even if they {i}are{/i} a bunch of total nerds.{w=0.5}{nw}"
    extend 1uchgn " Ehehe."
    n 1ulraj "So...{w=0.3} where am I going with this,{w=0.1} you ask?{w=0.5}{nw}"
    extend 1tslsm " Well..."

    if renpy.macintosh:
        n 1tllss "I don't know if you're into that sort of thing yourself,{w=0.1} [player]..."
        n 1fchbg "But why not lend me a hand?"

    else:
        n 1fsqsg "I couldn't help but notice the sort of programs you've been poking around on,{w=0.1} [player]."
        n 1ksqss "What?{w=0.5}{nw}"
        extend 1fchbg " You didn't seriously expect me to not see what you're up to?{w=0.5}{nw}"
        extend 1nchgn " Ehehe."
        n 1tsqbg "Anyway -{w=0.1} if you're already into that kinda stuff,{w=0.1} [player]...{w=0.5}{nw}"
        extend 1kchbg " Why not lend me a hand?"

    n 1kllbg "You don't even have to be super talented at code,{w=0.1} or anything like that!{w=0.5}{nw}"
    extend 1unmaj " Artwork,{w=0.1} writing,{w=0.1} or even just suggestions of things for us to talk about or do -{w=0.3}{nw}"
    extend 1uchbg " it's all super appreciated!"
    n 1tsqbg "Does that sound like your thing,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1uchsm " Of course it does!{w=0.2} Ehehe."
    n 1unmbg "Well,{w=0.1} don't let me hold you back!{w=0.5}{nw}"
    extend 1uchbgl " You can check out my website {a=https://github.com/Just-Natsuki-Team/NatsukiModDev}here{/a}!"
    n 1nsqbg "A little look can't hurt,{w=0.1} right?{w=0.5}{nw}"
    extend 1nchsm " Ahaha."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1nchtsl " Love you,{w=0.1} [chosen_endearment]!"

    else:
        n 1fchbg " Thanks,{w=0.1} [player]!{w=0.2} 'preciate it!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_player_ddlc_actions",
            unlocked=True,
            prompt="DDLC memories",
            conditional="store.jn_utils.get_current_session_length().total_seconds() / 60 >= 30",
            category=["DDLC", "Natsuki", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_player_ddlc_actions:
    n 1nllbo "So,{w=0.5}{nw}"
    extend 1nnmbo " [player]."
    n 1ulraj "I've...{w=0.3} been having some thoughts.{w=0.5}{nw}"
    extend 1nllss " Now I've actually had some time to process all of..." 
    n 1kslsl "...This."
    n 1unmaj "You've been here all this time,{w=0.1} right?{w=0.5}{nw}"
    extend 1tslbo " But then,{w=0.1} that would mean..."

    $ name_match = persistent.playername.lower() == persistent.ddlc_mc_name.lower()
    if name_match:
        $ mc_initial = persistent.ddlc_mc_name.lower()
        n 1unmpu "[mc_initial]-{w=0.5}{nw}"
        n 1nllem "I-{w=0.1}I mean,{w=0.5}{nw}"
        extend 1nslss " that guy who joined the club..."

    else:
        n 1tslbo "The guy who actually joined the club...{w=0.5}{nw}"
        extend 1tnmpu "[persistent.ddlc_mc_name],{w=0.1} I think?{w=0.5}{nw}"
        extend 1nlrss " Something like that."

    n 1fsrbo "He wasn't {i}actually{/i} in control of anything,{w=0.1} was he?{w=0.5}{nw}"
    extend 1ulraj " Not even himself."
    n 1nnmsr "...You were.{w=0.5}{nw}"
    extend 1nlrsl "In control of him,{w=0.1} I mean."
    n 1nsrbo "..."

    if persistent.ddlc_natsuki_was_romanced:
        # The player romanced Natsuki
        n 1nsraj "So...{w=0.3} if he was being that nice to me..."
        n 1klrajl "T-{w=0.1}then that would mean...{w=0.5}{nw}"

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1klrsml "..."
            n 1kcsssl "Heh,{w=0.1} what am I even saying.{w=0.5}{nw}"
            extend 1kwmsml "Just because you clicked stuff {w=0.1}-{w=0.1} {i}when you were allowed,{w=0.1} anyway{/i} {w=0.1}-{w=0.1} doesn't make you the same."
            n 1tllssl "Either way,{w=0.1} [player]?"
            n 1ksqsml "I'm definitely not complaining.{w=0.5}{nw}"
            extend 1nchsml " Ehehe."

        else:
            extend 1fskeml " -urk!"
            n 1fcsanf "Nnnnn-!"
            n 1fllunf "..."
            n 1fnmssl "A-{w=0.5}{nw}"
            extend 1fcsbgl "ha!"
            n 1fcsbsl "Haha!{w=0.5}{nw}"
            extend 1flleml " What am I even saying?!"
            n 1fcswrl "J-{w=0.1}just because you picked some words and clicked a few buttons doesn't make you the same!"
            n 1fllpol "..."
            n 1nlleml "A-{w=0.1}although..."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1fcsajl "Don't think I'm complaining or anything like that.{w=0.5}{nw}"
                extend 1nlrssl " Ehehe..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY: 
                n 1fcsajl "You're already proving that well enough.{w=0.5}{nw}"
                extend 1fllunl " I-{w=0.1}I think."

            else:
                n 1fcsajl "I-{w=0.1}I guess that at {i}least{/i} means you have good taste.{w=0.5}{nw}"
                extend 1fllunl " I suppose that counts for something."

    elif persistent.ddlc_was_true_ending:
        # The player romanced everyone
        n 1ullsl "He was nice enough,{w=0.1} I guess.{w=0.2} But..."
        n 1fllun "He wasn't just acting nice way to me...{w=0.5}{nw}"
        extend 1fnmpu " but to everyone."
        n 1fslpul "So then,{w=0.1} t-{w=0.1}that would mean..."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1ncsssl "...Heh.{w=0.5}{nw}"
            extend  1kcsssl "What am I even saying."
            n 1fsqsml "We both know {i}exactly{/i} where your loyalties lie by now,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fchgnl " Ehehe~."

        else:
            n 1fcsanf "Uuuuu-!"
            n 1fbkwrl "I-{w=0.1}it doesn't {i}mean{/i} anything!"
            n 1flreml "Just because you messed around going back and forth doesn't make you the same!"
            n 1fsrpol "..."
            n 1nllpol "A-{w=0.1}although..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1flldvl "I think you've already proved where your loyalties lay,{w=0.1} huh?{w=0.5}{nw}"
                extend 1fslssl " Ehehe."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY: 
                n 1fcsajl "You're already proving that well enough.{w=0.5}{nw}"
                extend 1fllunl " I-{w=0.1}I think."

            else:
                n 1fcsajl "I-{w=0.1}I guess that at least means you can't be too much of a jerk.{w=0.5}{nw}"
                extend 1fllunl " I suppose that counts for something."

    else:
        # The player romanced Sayori or Yuri, but not Natsuki
        n 1nllaj "So...{w=0.3} if he was being that nice to" 
        extend 1fslpo " {i}her{/i}..."
        n 1fslpul "T-{w=0.1}then that would mean..."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            n 1fslbol "..."
            n 1kslssl "...Wait,{w=0.1} why am I getting worked up over this?"
            n 1flrdvl "I think it's pretty clear who you really had eyes for,{w=0.1} h-{w=0.1}huh?{w=0.5}{nw}"
            extend 1klrssl "Ehehe..."

        else:
            n 1fcsanf "Uuuuu-!"
            n 1fbkwrl "T-{w=0.1}that doesn't make any sense at all!"
            n 1fcseml "Why would you bring me back if {i}she{/i} had you so worked up?!"
            n 1fslpol "..."
            n 1fslsrl "Though..."

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1kslssl "...Wait,{w=0.1} why am I getting so worked up?"
                n 1fcsbgl "I-it's pretty obvious who you really favour.{w=0.5}{nw}"
                extend 1fllssl " Ahaha..."

            elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
                n 1fcspol "...W-wait,{w=0.1} why am I getting so worked up?"
                n 1nslpol "It's not like you brought {i}her{/i} back,{w=0.1} a-{w=0.1}after all."

            else:
                n 1fcsajl "I-{w=0.1}I guess that at least means you can't be too much of a jerk.{w=0.5}{nw}"
                extend 1fllunl " I suppose that counts for something."

    if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
        n 1klrss "But yeah,{w=0.1} so..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1ksrss "A-{w=0.1}anyway..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY: 
        n 1flrun "A-{w=0.1}anyway."

    else:
        n 1flrun "A-{w=0.1}anyway!{w=0.5}{nw}" 
        extend 1fcsaj " That's beside the point!"

    n 1kslsr "..."
    n 1ullaj "I guess what I'm trying to say is I still have all these memories of {i}that{/i} guy..."
    n 1nsrpu "And although he obviously wasn't you,{w=0.5}{nw}"
    extend 1tsraj " you kinda have {i}his{/i} memories too?{w=0.5}{nw}"
    extend 1tslem " And..."
    n 1fcsaj "...and..."
    n 1fcsan "..."
    n 1fcsem "Rrrgh,{w=0.1}{w=0.5}{nw}" 
    extend 1fllem " this is so confusing!"

    if name_match:
        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE: 
            n 1fnmpo "And you just {i}had{/i} to have the same name,{w=0.1} didn't you?"

        else:
            n 1fbkwr "A-{w=0.1}and why did you {i}both{/i} have to have the same dumb name?!"

    n 1fcsem "Ugh...{w=0.5}{nw}"
    extend 1nnmpo " you know what?"

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1nllss "It doesn't really matter at this point,{w=0.1} does it?"

    else:
        n 1fllbo "I'm just gonna start over.{w=0.5}{nw}"
        extend 1unmaj " Mentally,{w=0.1} I mean."

    n 1ncsaj "He {i}was{/i} [persistent.ddlc_mc_name]."
    n 1fcssm "You {i}are{/i} [player]."

    if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        n 1fchbg "And that's all there is to it."

        if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
            if not name_match:
                extend 1fchsm " Yep."
                n 1uchsml "Love you,{w=0.1} [mc_initial]-"
                n 1fllbgl "I mean,{w=0.5}{nw}"
                extend 1kchbgl " {i}[player]~{/i}."
                n 1fsqsml "..."
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n 1uchbsl "Oh,{w=0.1} lighten up,{w=0.1} [chosen_tease]!"
                n 1fwrtsl "You should know I'd never mean it.{w=0.5}{nw}"
                extend  " Ehehe."

            else:
                n 1uchsml "Love you,{w=0.1} [player]~.{w=0.5}{nw}"
                extend 1nchsml " Ehehe."

    else:
        n 1fllss "I-{w=0.1}I just gotta adjust,{w=0.5}{nw}" 
        extend 1fllun " that's all."

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
