# All topics list
default persistent._topic_database = dict()

# Generic
default persistent._jn_out_of_topics_warning_given = False

# Pet data
default persistent._jn_player_pet = None

# Seasonal data
default persistent.jn_player_favourite_season = None

# Personal data
default persistent.jn_player_appearance_declined_share = False
default persistent.jn_player_appearance_eye_colour = None
default persistent.jn_player_appearance_hair_length = None
default persistent.jn_player_appearance_hair_colour = None
default persistent.jn_player_appearance_height_cm = None
default persistent._jn_player_birthday_day_month = None # Format (day, month)
default persistent._jn_player_birthday_is_leap_day = False # True if player gave birthday as 29th
default persistent._jn_player_is_multilingual = None
default persistent._jn_player_had_work_placement = None

# Hobby data
default persistent.jn_player_gaming_frequency = None
default persistent.jn_player_can_drive = None
default persistent._jn_player_has_flown = None

# Romance data
default persistent.jn_player_love_you_count = 0

# Preferences data
default persistent.jn_player_tea_coffee_preference = None

init python in topics:
    import store
    TOPIC_MAP = dict()

# Special dialogue for when out of random topics
label talk_out_of_topics:
    if Natsuki.isNormal(higher=True):
        n 3kllpo "Uhmm..."
        n 1knmaj "Hey...{w=0.5}{nw}"
        extend 4knmss " [player]?"
        n 1fslss "I'm...{w=0.3} kinda struggling to think of more stuff I wanna talk about."
        n 1ulraj "So...{w=0.5}{nw}"
        extend 1nsrss " I don't think I'm gonna talk much until I think of something else."
        n 3nsrpo "..."
        n 4tnmem "What?{w=0.5}{nw}"
        extend 3fllpol " I don't just talk because I like the sound of my own voice,{w=0.1} you know!"
        n 1tllpu "But...{w=0.5}{nw}"
        extend 1unmbo " I guess I {i}could{/i} just tell you about whatever comes to mind."
        n 1nchbg "So...{w=0.3} how about it?"

        show natsuki 2nsrsssbl
        menu:
            n "Do you mind if I repeat some stuff,{w=0.2} or...?"

            "Sure, I don't mind listening.":
                $ persistent.jn_natsuki_repeat_topics = True

                n 4uchgn "Okaaay!{w=0.5}{nw}"
                extend 1tcsaj " Now,{w=0.2} let me think..."

            "I don't mind listening, but don't remind me next time.":
                $ persistent.jn_natsuki_repeat_topics = True
                $ persistent._jn_natsuki_out_of_topics_remind = False

                n 2tnmboeqm "Huh?{w=0.75}{nw}"
                extend 2unmfl " Oh.{w=0.75}{nw}"
                extend 2nslsssbl " Right.{w=0.5} Sure."
                n 2cslsl "Now,{w=0.2} let me think..."

            "I'd rather wait.":
                n 2tllaj "Well...{w=0.5}{nw}"
                extend 2tnmbo " if you're sure."

                if Natsuki.isAffectionate(higher=True):
                    n 2kwmpol "I'll try to come up with something soon,{w=0.5}{nw}"
                    extend 4klrssl " 'kay?"

                else:
                    n 1flrpol "J-{w=0.2}just don't make the silence all awkward,{w=0.2} got it?!"

            "I'd rather wait, but don't remind me next time.":
                $ persistent._jn_natsuki_out_of_topics_remind = False
                
                n 2tsqpueqm "Huh?{w=0.75}{nw}"
                extend 2unmfl " Oh.{w=0.75}{nw}"
                extend 2csrsssbl " Heh."
                n 2clrsl "Well...{w=1}{nw}"
                extend 2tnmca " if you're sure,{w=0.2} [player]."

                if Natsuki.isAffectionate(higher=True):
                    n 4cllss "I'll...{w=1}{nw}"
                    extend 1cslbosbr " try to think of something soon."

    elif Natsuki.isDistressed(higher=True):
        n 1nllsf "..."
        n 1fllaj "Yeah,{w=0.1} so.{w=0.5}{nw}"
        extend 1fnmsl " I haven't got anything else to say."
        n 2fsqpu "...Or stuff I want to tell {i}you{/i},{w=0.1} anyway."
        n 2fslsr "So I'm just gonna shut up."
        n 1fcsun "Heh.{w=0.5}{nw}"
        extend 1fsqun " Not like that's a {i}problem{/i} for you,{w=0.1} huh?"

    else:
        n 2fslun "...{w=2}{nw}"
        extend 1fsqem " What?"
        n 2fcsan "You're the {i}last{/i} person I wanna think of more stuff to talk about with.{w=1}{nw}"
        extend 1fsrem " Jerk."

    $ persistent._jn_out_of_topics_warning_given = True
    return

# Talk menu topics

# Natsuki discusses her lack of pet with the player, and asks about theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="Did you ever have any pets?",
            category=["Animals", "Family"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:
    if get_topic("talk_did_you_have_pets").shown_count > 0:
        n 4unmaj "Huh?{w=0.75}{nw}" 
        extend 4tnmpu " Pets?"
        n 3ccspu "Hang on...{w=1}{nw}"
        extend 7tnmbo " didn't we talk about this already,{w=0.2} [player]?{w=1}{nw}"
        extend 7clrpu " Huh."
        n 2ulraj "Well,{w=0.2} anyway.{w=0.75}{nw}"
        extend 2tnmsl " I'm pretty sure you didn't need me to tell you {i}that{/i} hasn't changed.{w=1}{nw}"
        extend 2cslca " As you can see."

        if jn_desk_items.getDeskItem("jn_sanjo").unlocked:
            n 2csrss "It's not like Sanjo really counts as a pet either,{w=0.5}{nw}"
            extend 2csrbo " before you say anything."

        n 4ccsfl "...And actually,{w=0.5}{nw}"
        extend 7csrfl " now that I think about it..."
        n 7tnmfl "Where would I even {i}get{/i} one now anyway?{w=0.75}{nw}"
        extend 4clremsbl " L-{w=0.2}let alone all the stuff I'd need to actually keep it here!"
        n 2nsqem "You didn't seriously think I'd just have all that gear chilling out in my desk or something,{w=0.2} did you?"
        n 4cslflsbr "...And somehow I doubt the closet was left stocked up with pet food and kitty litter,{w=0.75}{nw}" 
        extend 4cllbosbr " of all things."
        n 2unmfl "I mean,{w=0.5}{nw}"
        extend 2ccsgs " don't get me wrong!{w=0.5}{nw}"
        extend 2clrfll " It's not like I {i}wouldn't{/i} like the company."

        if Natsuki.isEnamored(higher=True):
            n 2ccsbolsbr "A-{w=0.2}as much as having you here helps.{w=0.75}{nw}"

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsajlsbr "B-{w=0.2}between your visits,{w=0.2} I mean.{w=0.75}{nw}"

        else:
            n 2fcsemlsbr "O-{w=0.2}of course I would!{w=0.75}{nw}"

        extend 4clrsll " But..."
        n 4tnmpu "Keeping something {i}else{/i} here?{w=0.75}{nw}"
        extend 5cllpu " That's..."

        if Natsuki.isAffectionate(higher=True):
            n 5kslslsbl "..."
            n 7cllslsbl "I guess it just wouldn't feel fair...{w=1}{nw}"
            extend 7knmbosbrl " you know?{w=0.75}{nw}"
            extend 4klrbolsbr " Like..."
            n 2ccsfl "I-{w=0.2}I know I'm already stuck here.{w=0.75}{nw}"
            extend 2clrfl " Do I {i}really{/i} wanna force that on something else too?{w=0.75}{nw}"
            extend 2ksrpusbr " Just for my own sake?"

            if Natsuki.isEnamored(higher=True):
                n 7ksrslsbr "..."
                n 7kcsflsbr "I don't know,{w=0.2} [player].{w=0.75}{nw}"
                n 4kllflsbr "It just..."
                n 4kslcasbr "..."
                n 2ccsfll "It just doesn't sit right with me.{w=0.75}{nw}"
                extend 2csrsll " A-{w=0.2}at least right {i}now{/i}."
                n 2nsrbol "..."

            else:
                n 1cslsllsbr "..."
                n 4ccsfllsbr "N-{w=0.2}nevermind.{w=0.75}{nw}"
                extend 3ccsajsbl " It just wouldn't be fair on whatever it was.{w=0.75}{nw}" 
                extend 3ccscasbl " That's all I'm saying."

            n 4ccsemsbl "A-{w=0.2}anyway.{w=0.75}{nw}"
            extend 4ullaj " I think I've gone on for long enough.{w=0.75}{nw}"
            extend 3cllbo " But..."

            if Natsuki.isAffectionate(higher=True):
                n 3tnmbo "Why all the talk about pets all of a sudden,{w=0.2} [player]?{w=0.75}{nw}"
                extend 3fsqss " Is there something you're not telling me?"
                n 3fsqsm "..."
                n 3fcsbg "Well?{w=0.75}{nw}"
                $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
                extend 4fchgn " Spit it out already,{w=0.2} [chosen_descriptor]!"

                show natsuki option_wait_smug

            else:
                n 7tnmaj "Why all the talk about pets all of a sudden,{w=0.2} [player]?"
                
                show natsuki option_wait_curious

        else:
            n 1cslsllsbr "..."
            n 4ccsfllsbr "N-{w=0.2}nevermind.{w=0.75}{nw}"
            extend 3ccsajsbl " It just wouldn't be fair on whatever it was.{w=0.75}{nw}" 
            extend 3ccscasbl " That's all I'm saying."
            n 3tlraj "But...{w=1}{nw}"
            extend 7tnmbo " why all the talk about pets all of a sudden,{w=0.2} [player]?"

            show natsuki option_wait_curious

    else:
        n 3tnmboeqm "Huh?{w=0.75}{nw}" 
        extend 3tsqfl " Did I ever have any pets?"
        n 1fcssl "Heh.{w=0.75}{nw}"
        extend 4fllfl " I wish.{w=0.75}{nw}"
        extend 4fcswr " As if that was ever gonna happen with {i}my{/i} parents!"

        if jn_desk_items.getDeskItem("jn_sanjo").unlocked:
            n 4ccsem "...And no,{w=0.5}{nw}"
            extend 4csrsl " Sanjo doesn't count."
            n 4fnmem "But seriously -{w=0.5}{nw}"

        else:
            n 4fnmem "Seriously -{w=0.5}{nw}"
        
        extend 2flrwr " I was never allowed anything!{w=0.75}{nw}"
        extend 2fcsan " There was always some {i}convenient{/i} reason it couldn't possibly happen!"
        n 1fcsgs "And just to top it off..."
        n 3fllwr "It wasn't like the excuses even made any {i}sense{/i} either!{w=0.75}{nw}"
        extend 3fcsanean " Every single time I tried to bring it up!"
        n 6flrgs "It was always just about the mess it would make,{w=0.5}{nw}"
        extend 6fllem " or how we'd pay for it,{w=0.5}{nw}"
        extend 3fsrem " or literally anything else they could come up with..."
        n 4fcsan "...Even when I already {i}said{/i} I'd take care of all that stuff myself!"
        n 2fcsemesi "Ugh..."
        n 2fsrsll "Talk about {i}pet peeves{/i}.{w=1}{nw}"
        extend 2csrfl " But I guess it's not like any of that matters now,{w=0.2} anyway.{w=1}{nw}"
        extend 2cllbosbr " Being stuck here and all."
        n 2cslbosbr "..."
        n 2ullaj "Though...{w=1}{nw}"
        extend 7tnmbo " what about you,{w=0.2} [player]?"

        show natsuki option_wait_curious

    $ player_has_pet = persistent._jn_player_pet is not None
    $ prompt = "Do you have any pets,{w=0.2} or...?" if not player_has_pet else "Did you just get another pet,{w=0.2} or...?"
    $ response_yes = "Yes, I do." if not player_has_pet else "Yes, I did."
    $ response_no = "No, I don't." if not player_has_pet else "No, I didn't."
    $ response_gone = "I used to." if not player_has_pet else "I lost one."

    menu:
        n "[prompt]"

        "[response_yes]":
            n 1uspgs "Oh!{w=0.5}{nw}" 
            extend 4fchbs " Oh{w=0.2} oh{w=0.2} oh!" 
            n 4unmbs "Come on!{w=0.75}{nw}" 
            extend 3unmbg " You gotta tell me,{w=0.2} [player]!{w=0.75}{nw}"

            if player_has_pet:
                extend 3uchgnedz " What did you get?{w=0.2} What did you get?"

            else:
                extend 3uchgnedz " What is it?{w=0.2} What is it?"

            show natsuki option_wait_excited at jn_left

            $ pet_options = [
                ("Birds", "birds"),
                ("Cats", "cats"),
                ("Chameleons", "chameleons"),
                ("Dogs", "dogs"),
                ("Ferrets", "ferrets"),
                ("Fish", "fish"),
                ("Frogs", "frogs"),
                ("Geckos", "geckos"),
                ("Gerbils", "gerbils"),
                ("Guinea pigs", "guinea_pigs"),
                ("Hamsters", "hamsters"),
                ("Horses", "horses"),
                ("Insects", "insects"),
                ("Lizards", "lizards"),
                ("Mice", "mice"),
                ("Rats", "rats"),
                ("Rabbits", "rabbits"),
                ("Snakes", "snakes"),
                ("Something else", "something_else")
            ]
            $ pet_options.sort()
            call screen scrollable_choice_menu(items=pet_options)
            $ persistent._jn_player_pet = _return
            show natsuki at jn_center

        "[response_no]":
            n 4cllfl "Man...{w=1}{nw}"
            extend 4tsqfl " really?"
            n 2nsrsl "..."
            n 2nsraj "Well...{w=1}{nw}" 
            extend 1nlrbo " I gotta admit.{w=0.75}{nw}"
            extend 3nsrfl " I'd be lying if I said I wasn't at least {i}kinda{/i} disappointed."

            if player_has_pet:
                n 3cslss "Even if you {i}did{/i} say you had [persistent._jn_player_pet] already."
                n 3cslbosbr "..."

            if Natsuki.isAffectionate(higher=True):
                n 3ullaj "Well,{w=0.2} whatever.{w=0.75}{nw}"
                extend 1ccsss " It's not like people get pets regularly or anything,{w=0.2} after all."
                n 4fsqss "Don't start thinking that means you're off the hook though,{w=0.2} [player].{w=0.75}{nw}"
                extend 4fsqsm " Ehehe."
                n 3fchbg "Nope!{w=0.75}{nw}"
                
                if Natsuki.isEnamored(higher=True):
                    extend 3fcsbg " As if I'd miss out on that kind of news.{w=0.75}{nw}"
                    extend 3flrss " And besides..."
                    n 6fcsbgeme "Something tells me you'd just {i}have{/i} to share it with me,{w=0.2} anyway."
                    n 4fsqsm "...Isn't that right?{w=0.75}{nw}"
                    extend 1fchsm " Ahaha."

                else:
                    extend 3fcsbg " As if I'd miss out on that kind of news.{w=0.75}{nw}"
                    extend 7nchgn " You better tell me all about it!"

            else:
                n 7ulraj "Well...{w=1}{nw}"
                extend 7tnmbo " just let me know when that changes,{w=0.2} I guess.{w=0.75}{nw}"
                extend 3fcssmesm " I still wanna hear all about it!"

            return

        "[response_gone]":
            if Natsuki.isAffectionate(higher=True):
                n 4klrbo "..."
                n 4klrpusbr "I...{w=1}{nw}"
                extend 5ksrpusbr " don't really know what to say,{w=0.2} [player]."
                n 4ccsflsbr "Just..."
                n 1kslslsbl "..."
                n 4ccsslsbl "...Just don't keep it bottled up if you don't have to.{w=0.75}{nw}"
                extend 4cnmflsbl " Got it?"
                n 5csrsllsbl "Y-{w=0.2}you should know you have people around you who'd listen by now."

                if Natsuki.isEnamored(higher=True):
                    n 4ksrsllsbl "..."
                    n 4knmflsbr "...And [player]?"
                    n 5kllbosbr "..."
                    n 5ccspulsbr "I...{w=1.25}{nw}"
                    extend 4clrpulsbr " know I said never I had a pet or anything like that.{w=0.75}{nw}"
                    extend 1csrpulsbr " Not even close.{w=1}{nw}"
                    extend 1ksrsll " But..."
                    n 2ksrbol "..."
                    n 2ksrajl "...You know I've lost friends too.{w=0.75}{nw}"
                    extend 2ksqcal " Right?"
                    n 2ccsfllsbl "I-{w=0.2}I'm not saying I {i}know{/i} how you feel.{w=0.75}{nw}"
                    extend 2cllfllsbl " Of course not!{w=0.75}{nw}"
                    extend 2cllbolsbl " Only you know that,{w=0.2} [player].{w=1.5}{nw}"
                    extend 4kslbolsbl " But..."
                    n 1ccsbolesisbl "..."
                    n 1kslsll "...I understand.{w=0.75}{nw}" 
                    extend 4ksqsll " Okay?"
                    n 4knmcal "Really."
                    
                    if Natsuki.isLove(higher=True):
                        n 5ksrbol "...I get it.{w=1.25}{nw}"
                        extend 1ccsfllsbl " I just wanted you to know that too."
                        n 4ksrcal "..."
                        n 4ksqbol "...And [player]?"
                        n 5kslsllsbl "..."

                        show natsuki 4ccssllsbr at jn_center
                        play audio chair_out
                        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                        $ jnPause(2)
                        play audio clothing_ruffle
                        show natsuki 1ccscalsbr at jn_center
                        $ jnPause(3)
                        play audio chair_in
                        $ jnPause(3)
                        hide black with Dissolve(1.25)

                    else:
                        n 5ksrbol "...I get it.{w=0.75}{nw}"
                        extend 1ccsfllsbl " I just wanted you to know that too.{w=1.25}{nw}"
                        extend 1cllpulsbl " But..."
                        n 4cslbolsbl "..."
                        n 4kslbolsbl "...Yeah."

                n 5kslcal "..."
                n 4nslajl "So..."
                n 4tnmsllsbr "Did you wanna talk about something else instead,{w=0.2} or...?"

            else:
                n 4ccsemsbr "W-{w=0.2}wait.{w=0.75}{nw}"
                extend 4knmemsbr " You..."
                n 1ksrpusbr "...Oh.{w=1}{nw}" 
                extend 4ksrflsbr " Jeez."
                n 5kslbosbr "..."
                n 4ccsflsbl "I'm...{w=1.25}{nw}"
                extend 2cllslsbl " really sorry to hear that,{w=0.2} [player].{w=1}{nw}"
                extend 2kslbolsbl " T-{w=0.2}truly."
                n 4kslcalsbr "..."
                n 4ccsemlsbr "...Maybe we should just talk about something else for now.{w=0.75}{nw}"
                extend 2cnmemlsbr " I-{w=0.2}if you wanted to,{w=0.5}{nw}" 
                extend 2nsrbolsbr " I mean."
                n 4ksrcalsbr "..."

            return

    if persistent._jn_player_pet == "birds":
        n 1unmaj "Oh?{w=0.75}{nw}"
        extend 2tnmss " Birds,{w=0.2} huh?{w=0.75}{nw}"
        extend 2fchsm " Neat!"
        n 1flrss "I bet you got into a total{w=0.5}{nw}"
        extend 4fsqbg " {i}flap{/i}{w=0.75}{nw}"
        extend 4usqbg " when you saw yours for the first time,{w=0.2} huh?"

        if Natsuki.isLove(higher=True):
            n 3fcssmeme "Ehehe.{w=0.75}{nw}"
            extend 3fwlbgl " Love you,{w=0.2} [player]~!"

        else:
            n 3fchsmeme "Ehehe."

    elif persistent._jn_player_pet == "cats":
        n 4unmbg "Kitties?{w=0.75}{nw}"
        extend 4uchgn " {i}Now{/i} we're talking,{w=0.2} [player]!"

        if Natsuki.isAffectionate(higher=True):
            n 4clraj "Well..."
            n 3ccsbglsbl "Unless you just said that hoping {i}I{/i} like them too,{w=0.2} anyway."

        else:
            n 2nllaj "Though...{w=1}{nw}" 
            extend 2fllss " I've gotta ask."
            n 4fcsbg "...Just how many videos have you made {i}yours{/i} the star of,{w=0.5}{nw}" 
            extend 4fsqbg " [player]?"

        n 3usqsm "..."
        n 3fcssm "Oh?{w=0.75}{nw}"
        extend 7fcsbg " What's wrong,{w=0.2} [player]?"
        extend 7fchgn " Did I call you out?"
        n 4ulraj "Well,{w=0.2} anyway.{w=0.75}{nw}"
        extend 3fcsaj " You better be taking care of yours,{w=0.2} [player]!"
        n 3fcspo "...Or I really will give you {i}paws{/i} for thought.{w=0.75}{nw}"
        
        if Natsuki.isLove(higher=True):
            extend 3fchsmeme " Ehehe."
            n 3fchbll "Love you too,{w=0.2} [player]~!"

        else:
            extend 3fchsmeme " Ehehe."

    elif persistent._jn_player_pet == "chameleons":
        n 4tnmfl "Chameleons?{w=0.75}{nw}"
        extend 7unmbo " Like with the swivelly eyes and all that?{w=0.75}{nw}"
        extend 7clrbo " Huh."
        n 7clrfl "I...{w=1}{nw}" 
        extend 3tnmbo " didn't even know people kept those,{w=0.2} honestly.{w=0.75}{nw}"
        extend 3tllss " Neat."
        n 1fcssm "...Heh."
        n 4flrss "Well...{w=1}{nw}"
        extend 3fcsbg " {i}color{/i} me surprised!"
        extend 3fchsm " Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 4nchgn "No regrets,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "dogs":
        n 7unmaj "Dogs,{w=0.2} huh?{w=0.75}{nw}"
        extend 4fchsm " Cool!"
        n 4csrss "...Not that I can see myself ever owning one,{w=0.2} though.{w=0.75}{nw}"
        extend 2csrpo " With the walks every single day and all that."

        if get_topic("talk_skateboarding").shown_count > 0:
            n 2fcsaj "Nope!{w=0.75}{nw}"
            extend 2fcsbg " The skateboard is more than enough for me!"

        else:
            n 2fcsaj "Nope!{w=0.75}{nw}"
            extend 2fcsgs " I'll take my walks when {i}I{/i} want them,{w=0.5}{nw}"
            extend 2fcspo " thank you very much."
            n 2fsqsm "Ehehe."

        n 4ullaj "Well,{w=0.2} anyway -{w=0.5}{nw}"
        extend 4ccstr " better make sure you're taking care of yours,{w=0.2} [player]..."
        n 2csqpo "Or I really {i}will{/i} have a bone to pick with you."

    elif persistent._jn_player_pet == "ferrets":
        n 7clrpu "You know...{w=1}{nw}"
        extend 7cnmbo " I've always wondered about ferrets.{w=0.75}{nw}"
        extend 7tslpu " Is it more like having a cat or a dog?"
        n 7cslbo "Huh."
        n 4ullaj "Well anyway...{w=1}{nw}" 
        extend 4fcstr " whatever they're like.{w=0.75}{nw}"
        extend 2fcssmesm " You better be taking care of the little guy!"

        if Natsuki.isLove(higher=True):
            n 5flrssl "At least as much as you take care of me,{w=0.2} anyway."
            n 7tlrajl "Well...{w=1}{nw}"
            extend 3fsqssl " {i}almost{/i} as much.{w=0.75}{nw}"
            extend 3fchsml " Ehehe."

    elif persistent._jn_player_pet == "fish":
        n 3tllpu "Fish,{w=0.5}{nw}"
        extend 3tnmbo " huh?"
        n 7tlrbo "..."
        n 7tlrss "Well...{w=1}{nw}"
        extend 5csrss " I wouldn't call them {i}super{/i} affectionate or anything...{w=1}{nw}"
        extend 7ulrca " but I suppose I can see the reasons to keep them around.{w=0.75}{nw}"
        extend 7unmbg " Like for stress!"
        n 4fcsss "Heh."
        n 3fcssm "I bet you feel like you could lose yourself in that tank,{w=0.5}{nw}" 
        extend 3fsqsm " huh?{w=0.75}{nw}"
        extend 3fchsm " Ehehe."

    elif persistent._jn_player_pet == "frogs":
        n 3unmaj "Ooh!{w=0.2} Froggies!{w=0.75}{nw}"
        extend 3fchbg " Cute!"
        n 4fllss "I seriously can't get enough of their faces.{w=0.75}{nw}"
        extend 3uchgn " They always look so {i}confused{/i}!{w=0.75}{nw}"
        extend 3nchgn " Ahaha."
        n 1ulrss "Well,{w=0.2} anyway...{w=1}{nw}"
        extend 4tnmss " I guess I shouldn't keep you waiting,{w=0.2} [player]."
        n 4fsqss "You know."
        n 6fcsbg "...Just in case you gotta {i}hop to it{/i} and take care of yours!"

        if Natsuki.isLove(higher=True):
            n 3fchsmleme "Ehehe.{w=0.75}{nw}"
            extend 3fchbll " Love you,{w=0.2} [player]~!"

        else:
            n 3fchsmeme "Ehehe."

    elif persistent._jn_player_pet == "geckos":
        n 1unmbg "Geckies!{w=0.75}{nw}"
        extend 4fchbg " Yeah!{w=0.75}{nw}"
        extend 4fchsm " I've heard about those!"
        n 1flrss "Man...{w=1}{nw}"
        extend 3fchgn " I just can't get over how goofy they look!{w=0.75}{nw}"
        extend 3cslbosbr " Even if you do have to feed them bugs."
        n 1ccstr "Just a warning though,{w=0.2} [player]..."
        n 2csqpo "I better not hear about any tails falling off on your watch."

    elif persistent._jn_player_pet == "gerbils":
        n 3ulraj "Gerbils,{w=0.5}{nw}"
        extend 3tnmbo " huh?"
        n 4fsqaj "...And why's that,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2fnmfl " Hamsters not good enough for you?{w=0.75}{nw}"
        extend 2fnmaj " Is that it?"
        n 2fsqpo "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 4ulrss " Nah,{w=0.2} I guess I can see it.{w=0.75}{nw}"
        extend 7tnmbo " You keep gerbils together,{w=0.2} right?{w=0.75}{nw}"
        extend 3fchsm " Cute!"
        n 3fcsaj "You better be taking care of yours though,{w=0.2} [player]..."
        n 4fsqss "...Or you really {i}will{/i} need them to dig you out of it.{w=0.75}{nw}"
        extend 4fcssm " Ehehe."

        if Natsuki.isLove(higher=True):
            n 2fchsmleaf "Love you,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "guinea_pigs":
        n 4uwdaj "Ooh!{w=0.75}{nw}"
        extend 3uchbg " Yeah!{w=0.2} I've seen those!"
        n 3clrbgsbl "I don't exactly know {i}tons{/i} about them,{w=0.5}{nw}" 
        extend 3fchgn " but I love the little sounds they make!{w=0.75}"
        extend 4fchbg " Especially when you have a bunch of them together!"
        n 2fcssm "I bet yours are a total bunch of chatterboxes too,{w=0.2} huh?{w=0.75}{nw}"
        extend 2fchsm " Ehehe."

    elif persistent._jn_player_pet == "hamsters":
        n 1fcsaj "W-{w=0.2}wait.{w=0.75}{nw}"
        extend 4unmfl " Hammies?{w=0.75}{nw}"
        extend 4fnmfl " For real?"
        n 2fcsun "..."
        n 2fcsem "Are...{w=1}{nw}"
        extend 1fcsaj " you...{w=1}{nw}"
        extend 4fspgs " freaking KIDDNG ME?!{w=0.75}{nw}"
        extend 4uchbs " I {b}love{/b} hammies!"
        n 3fcsbgl "Those stubby little tails,{w=0.5}{nw}"
        extend 3flrbgl " those tiny paws...{w=1}{nw}"
        extend 3fchgnl " those chubby cheeks?"
        n 1fcssml "Ehehe.{w=0.75}{nw}"
        extend 4fcsbs " Yep!{w=0.75}{nw}"
        extend 4fllbg " When it comes to a {i}professional{/i} display of cuteness,{w=0.5}{nw}"
        extend 3fcsbg " I'm afraid I've gotta say it."
        n 3nchgn "You just can't beat hamsters!"
        n 3nllsssbr "Though...{w=1}{nw}"
        extend 3nslss " that being said."
        n 1csqtr "You better be taking {i}real{/i} good care of yours,{w=0.2} [player]..."

        if Natsuki.isAffectionate(higher=True):
            n 4nsrpo "...Or you really will find out how much I ham it up.{w=0.75}{nw}"
            extend 4fsqsm " Ehehe."
            
            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "Love you too,{w=0.2} [player]~!"

        else:
            n 4fcspo "...Or you really {i}will{/i} find out how much I ham it up."

    elif persistent._jn_player_pet == "horses":
        n 1unmemesu "H-{w=0.2}huh?{w=0.75}{nw}"
        extend 4unmgssbl " Horses?{w=0.75}{nw}"
        extend 4tnmflsbl " Seriously?!"
        n 2clremsbr "Jeez...{w=1}{nw}"
        extend 2csqposbr " you aren't just messing with me,{w=0.2} are you?{w=0.75}{nw}"
        extend 2cllemsbr " How do you even {i}afford{/i} something like that,{w=0.2} [player]?"
        
        if get_topic("talk_careful_spending").shown_count > 0:
            n 4tllsl "..."
            n 7tllpu "...Huh.{w=0.75}{nw}"
            extend 7cslsssbr " Maybe that whole conversation about being careful with your money {i}was{/i} needed after all."

        else:
            n 5csrsssbr "...Even if it {i}is{/i} pretty cool."
        
        n 2csrsssbr "W-{w=0.2}well,{w=0.2} anyway.{w=0.75}{nw}"

        if Natsuki.isAffectionate(higher=True):
            extend 2fcsbg " I hope you're all saddled up,{w=0.2} [player]..."
            n 2nchgnelg "'Cause there's no way you're wiggling out of some free riding lessons!{w=0.75}{nw}"
            extend 2nchgn " Ehehe."

        else:
            extend 4nsqpo " You better hope I don't catch you riding without a helmet,{w=0.2} [player]."
            n 2ccspoesi "'Cause you getting saddled up with a bunch of dumb hospital bills is the last thing I wanna hear about."

    elif persistent._jn_player_pet == "insects":
        n 2tsqan "Ack-{w=0.75}{nw}"
        n 2cllunlsbr "..."
        n 2ccssslsbr "B-{w=0.2}bugs,{w=0.5}{nw}"
        extend 4clrsslsbl " huh?"
        n 4csrunlsbl "..."
        n 1ccsajlsbl "I-{w=0.2}I mean,{w=0.75}{nw}"
        extend 2cllsssbl " don't get me wrong!{w=0.75}{nw}"
        extend 2cllbosbl " Someone's gotta take care of all the creepy crawlies."
        n 5cslemsbl "...I'm just glad it's not me.{w=0.75}{nw}"
        extend 1ccsemsbl " Yeesh."
        n 4csrbosbl "..."
        n 4ccssssbl "W-{w=0.2}well..."
        n 2fllbg "I guess I'll just try not to let it{w=0.5}{nw}"
        extend 2fsqsm " {i}bug me{/i}{w=0.75}{nw}"
        extend 4fwlbg " then!{w=0.75}{nw}"
        extend 4fcssmeme " Ehehe."

        if Natsuki.isLove(higher=True):
            n 3fchblleaf "Love you too,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "lizards":
        n 1tnmfl "Oh?{w=0.75}{nw}"
        extend 2tllfl " Really,{w=0.2} [player]?{w=1.25}{nw}"
        extend 2tsqem " Lizards?"
        n 4ccsss "Heh.{w=0.75}{nw}"
        extend 7ulraj " I gotta say,{w=0.2} [player] -{w=0.5}{nw}" 
        extend 7unmbo " I'm impressed."
        n 6fchbg "...You {i}finally{/i} managed to find a pet just as cold-blooded as you!"
        n 1fsqdv "..."
        n 4fchdvesi "Pfffft!{w=0.75}{nw}"
        extend 3fchbg " I'm kidding,{w=0.2} [player]!{w=0.5} I'm just kidding!{w=0.75}{nw}"
        extend 3kllbg " Jeez..."
        n 3cnmss "..."
        n 1fsqbo "..."
        n 4fnmem "Hey!{w=0.75}{nw}"
        extend 4flrfl " Come on,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fcspo " Don't give me that look.{w=0.75}{nw}"
        extend 3fchgn " It was a good one this time!"
        n 6fcsbg "And besides -{w=0.5}{nw}"
        extend 6unmaj " think about it!"
        n 4fnmsg "Shouldn't you of all people know how to{w=0.5}{nw}" 
        extend 3fsqbg " {i}shed{/i}{w=0.75}{nw}" 
        extend 3fchbg " things off?{w=0.75}{nw}"
        extend 3nchgn " Ahaha."

        if Natsuki.isLove(higher=True):
            n 4fwlbgl "Love you too,{w=0.2} [player]~!"

        else:
            n 4fwlbg "I'm here all week,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "mice":
        n 7tlrbo "Mice,{w=0.2} eh?{w=0.75}{nw}"
        extend 7tsqfl " Are you sure,{w=0.2} [player]?"
        n 4fsqss "Not hamsters?{w=1}{nw}"
        extend 4fnmbg " Gerbils?"
        n 3fsqbg "...Or do I smell a rat?"
        n 3fsqsm "..."
        n 3fchsm "Ehehe.{w=0.75}{nw}"
        extend 4ullss " Nah,{w=0.2} I guess I can see the appeal.{w=0.75}{nw}"
        extend 7unmaj " They're social animals,{w=0.2} right?"
        n 3fcssmesm "You better be giving yours plenty of company too,{w=0.2} [player]!"

    elif persistent._jn_player_pet == "rats":
        n 7tnmbo "Rats,{w=0.2} huh?{w=0.75}{nw}"
        extend 7ullaj " That's pretty cool."
        n 2ullsl "..."
        n 2fsqsm "..."
        n 2fcsbg "Oh?{w=0.75}{nw}"
        extend 4fnmbg " What's the matter,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4fnmsm " Were you {i}expecting{/i} me to be grossed out or what?"
        n 1fcssm "Ehehe.{w=0.75}{nw}"
        extend 3tllss " Nah,{w=0.2} rats are fine.{w=1}{nw}"
        extend 3unmaj " They're super smart too!{w=0.75}{nw}"
        extend 3nlrsssbl " But I bet you already knew that by now anyway."
        n 1fcsss "Heh.{w=0.75}{nw}"
        extend 4fcsbg " In fact..."
        n 2fsqbg "I bet you probably have plenty of {i}tails{/i} to tell by now,{w=0.5}{nw}"
        extend 2nchgn " right?"

        if Natsuki.isLove(higher=True):
            n 1nchsml "Ahaha.{w=0.75}{nw}"
            extend 3fchbll " Love you too,{w=0.2} [player]~!"

    elif persistent._jn_player_pet == "rabbits":
        n 4unmbg "Bunnies!{w=0.75}{nw}"
        extend 4uchgnl " Yes!{w=0.75}{nw}"
        extend 3ccsssl " Man..."
        n 3cllbolsbr "..."
        n 4ccsfllsbr "I-{w=0.2}I mean,{w=0.5}{nw}"
        extend 2fcsajlsbr " how could anyone {i}not{/i} love those little fuzzballs?{w=0.75}{nw}"
        extend 2fllsslsbr " Are you kidding me?!"
        n 4fcsbgl "Especially those ones with the floppy ears!{w=0.75}{nw}" 
        extend 4nchgnl " They look so cuddly!"
        n 1fllbg "And then just to top if off,{w=0.5}{nw}" 
        extend 3fspaj " they come in all those different colors too!{w=0.75}{nw}"
        extend 3fchbg " Talk about variety!"
        n 6ullaj "Just make sure you keep that cage spick and span though,{w=0.2} [player] -{w=0.5}{nw}"
        extend 2csqpo " I'm not putting up with any {i}dust{/i} bunnies on my watch."

    elif persistent._jn_player_pet == "snakes":
        n 1unmemesh "H-{w=0.2}huh?{w=0.75}{nw}"
        extend 4ccsemlsbl " N-{w=0.2}now just hold on a second,{w=0.2} [player].{w=0.75}{nw}"
        extend 4clremlsbl " {i}Snakes{/i}?"
        n 1csrunlsbr "..."
        n 4fcsunsbr "Uuuuuu..."
        n 2kcsaj "...Fine.{w=0.75}{nw}" 
        extend 2cslbosbr " I guess I'll just be straight with you,{w=0.2} [player]."
        n 1ccsfllsbr "I'm...{w=1}{nw}"
        extend 4ksrsllsbr " not {i}amazing{/i} with those."
        n 2fcsfllsbr "S-{w=0.2}snakes,{w=0.2} I mean."
        n 2fllfll "They just...{w=1}{nw}" 
        extend 2cslcal " don't really agree with me.{w=0.75}{nw}" 
        extend 4cslsll " I don't know why."
        n 6fcsgsl "B-{w=0.2}but that's not to say that they {i}can't{/i} be cute,{w=0.1} obviously!{w=0.75}{nw}"
        extend 3flrpo " Making that kind of assumption is just being ignorant."
        n 3ksrpo "...And they deserve care just like any other pet."

        if Natsuki.isAffectionate(higher=True):
            n 1fcsaj "Besides,{w=0.2} [player] -{w=0.5}{nw}" 
            extend 4ccsca " you know what you signed up for."
            n 3fchgn "You can't {i}shed{/i} your responsibilities that easily!{w=0.75}{nw}"
            extend 3nchgn " Ehehe."

            if Natsuki.isLove(higher=True):
                n 3fchbll "Love you too,{w=0.2} [player]~!"

        else:
            n 4flraj "So!{w=0.75}{nw}"
            extend 3fcsposbr " You better not be flaking out on yours,{w=0.2} [player]!"
            n 3fcscaesmsbr "That's all I'm saying!"

    elif persistent._jn_player_pet == "something_else":
        n 4tsqbg "Oho?{w=0.75}{nw}"
        extend 3tnmbg " An exotic owner,{w=0.2} are we?"
        n 3fcsbg "...And why's that,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqss " Regular pets just aren't {i}special{/i} enough for you?{w=0.75}{nw}"
        extend 3fupfl " You just {i}had{/i} to stand out?"
        n 3fsqsm "..."
        n 4fnmsm "Well?{w=0.75}{nw}"
        extend 2fcsbs " Spit it out!"
        n 2fsqcs "..."
        n 2nchgn "Ahaha.{w=0.75}{nw}"
        extend 2cllss " Nah,{w=0.2} I guess that's fine.{w=0.75}{nw}"
        extend 2tnmaj " In all seriousness though,{w=0.2} [player]?"
        n 2clrca "..."
        n 4ccstr "Just...{w=1}{nw}"
        extend 4csqsl " make sure you know what you're doing.{w=0.75}{nw}"
        extend 4csqaj " Capiche?"

        if Natsuki.isAffectionate(higher=True):
            n 1unmemlsbl "I-{w=0.2}it's not that I think you're automatically a bad owner or anything!{w=0.75}{nw}"
            extend 2fcsemlsbl "\nOf course not!"
            n 2fcspol "Only a {i}real{/i} dummy just jumps to those kinds of assumptions.{w=1}{nw}"
            extend 4csrbol " But..."
            n 3ccsajl "I {i}have{/i} heard about how demanding they can be.{w=0.75}{nw}"
            extend 3csqbo " And trust me."
            n 4fcssslsbl "You really don't want {i}my{/i} demands on top of that too.{w=0.75}{nw}"
            extend 4fsqsml " Ehehe."

            if Natsuki.isLove(higher=True):
                n 3fchbll "Love you too,{w=0.2} [player]~!"

            else:
                n 6fwlbgl "Enjoy,{w=0.2} [player]!"

        else:
            n 6ccsajlsbr "Y-{w=0.2}you owe the animal {i}that{/i} much,{w=0.2} after all.{w=0.75}{nw}"
            extend 3fcscalesm " Remember that."

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
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_service_animals:
    if get_topic("talk_service_animals").shown_count > 0:
        if Natsuki.isNormal(higher=True):
            n 4ncsss "Heh.{w=0.75}{nw}"
            extend 3nslss " Man..."
            n 7ntlaj "I'm pretty sure I talked about it before,{w=0.75}{nw}"
            extend 7unmbo " but I still can't get my mind off that school visit we had."
            n 4fsrsssbl "N-{w=0.2}not the careers advice or anything like that.{w=0.75}{nw}"
            extend 4unmaj " But that visit we had from the charity for service and therapy animals!"
            n 3fchbg "Talk about making an impression,{w=0.2} huh?"
            n 3ulraj "Seriously though -{w=0.5}{nw}"
            extend 4unmfl " it's crazy how much work they do!{w=0.75}{nw}"
            extend 4tllfl " Like I was saying before..."

        else:
            n 1ncssl "Heh.{w=0.75}{nw}"
            extend 2nlraj " I'm pretty sure I talked about it before -{w=0.5}{nw}"
            extend 2csqsl " if you were even {i}listening{/i} -{w=0.5}{nw}"
            extend 2clrpu " but I still keep thinking back about that school visit we had."
            n 1fsqfl "...And no,{w=0.5}{nw}"
            extend 4ccsfl " none of the career ones or anything like that."
            n 4cdlbo "I was actually thinking about that charity with the service and therapy animals.{w=0.75}{nw}"
            extend 2cllaj " It's still pretty crazy to me how much work they actually do."

    else:
        if Natsuki.isNormal(higher=True):
            n 7cdlbo "You know,{w=0.2} [player]..."
            n 7tdlaj "I don't think I ever mentioned it before,{w=0.75}{nw}"
            extend 7unmbo " but we did actually used to get visitors at school sometimes."
            n 3ccsss "Heh.{w=0.75}{nw}"
            extend 3csqss " Are you surprised?{w=0.75}{nw}"
            extend 1fdrsl " We were {i}basically{/i} a captive audience,{w=0.2} after all."
            n 1csrfl "Not like we were given the option to leave."
            n 3cllaj "Usually it was just someone trying to sell us on some kinda career after school,{w=0.75}{nw}"
            extend 3csrbo " or like a visit from the local police or some other snooze-fest."
            n 7utrpu "But...{w=0.75}{nw}"
            extend 7clrbg " there was {i}one{/i} visit I actually did like."
            n 4fcsbg "Betcha' can't guess what it was,{w=0.2} [player]."
            n 3fsqsm "Ehehe."
            n 3ullaj "It was actually a bunch of volunteers from a charity...{w=1}{nw}"
            extend 4unmfl " but for service and therapy animals!"
            n 1ccsgs "And oh.{w=0.5}{nw}"
            extend 1ccsfl " My.{w=0.5}{nw}"
            extend 1csqaj " God.{w=0.5}{nw}"
            extend 4csqca " [player]."
            n 4ccstr "They're...{w=1}{nw}"
            extend 4fspgsedz " {b}awesome{/b}!{w=0.75}{nw}"
            extend 3uchgn " I love them!"

        else:
            n 1cllpu "You know..."
            n 2fslpu "Not that I expect you to care or anything,{w=0.75}{nw}"
            extend 2cnmsl " but we did actually get random visitors at school sometimes."
            n 2clrsl "..."
            n 2ccsfl "Yeah.{w=0.75}{nw}"
            extend 4csqsl " Don't look too surprised."
            n 4fllem "Hard to find a better captive audience than a bunch of students.{w=0.75}{nw}"
            extend 2fslem " Obviously."
            n 2cslpu "I mean...{w=1}{nw}"
            extend 2clrsl " most of them were just a {i}total{/i} snooze-fest.{w=0.75}{nw}"
            extend 2clraj " Career talks,{w=0.5}{nw}"
            extend 2csrfl " that sort of stuff."
            n 7csrsl "But there was one I {i}did{/i} actually like."
            n 3cllpu "It was some kinda charity,{w=0.5}{nw}"
            extend 3nllaj " but all their work was around training up service and therapy animals -{w=0.5}{nw}" 
            extend 3cllca " then getting them to people who needed them."

    if Natsuki.isNormal(higher=True):
        n 7ulrss "They're like animals trained up specially to help people who struggle to do certain things for themselves -{w=0.5}{nw}"
        extend 7unmfl " or stuff they can't do at all!"
        n 2ccsss "Everybody knows about guide dogs.{w=0.75}{nw}"
        extend 2unmbo " But there's actually a {i}ton{/i} of roles people never even think about."
        n 4unmaj "Seriously!"
        n 4ccsss "There's ones that are meant to help more with mobility,{w=0.5}{nw}"
        extend 3cllsssbr " some that listen out for stuff if their owner has sucky hearing..."
        n 3unmaj "Even helping out with managing medical conditions or avoiding allergies!"
        n 7ccsss "Heh.{w=0.75}{nw}"
        extend 7fcssmesm " Talk about sniffing things out."
        n 7tllaj "But...{w=1}{nw}"
        extend 7tnmbo " personally?"
        n 4unmbg "The ones I really liked were the therapy animals!"
        n 2clrss "The visitors didn't go into that much detail about them,{w=0.5}{nw}"
        extend 4csrss " and they aren't {i}exactly{/i} in the same group as service types..."
        n 4unmbo "But they're sorta like extra-tame pets for people going through rough times of some kind."
        n 2ullaj "You know,{w=0.5}{nw}" 
        extend 2unmbo " like emotionally or mentally."
        n 4nchgn "...And they come in a ton of shapes and sizes too!"
        n 3clrbg "You have cats and dogs -{w=0.5}{nw}"
        extend 3fcsbg " {i}obviously{/i} -{w=0.5}{nw}"
        extend 3fchsm " but even animals like those miniature horses can be trained up to help!"
        n 6fcsbg "You don't just find them hanging around the home either,{w=0.2} [player] -{w=0.5}{nw}"
        extend 6unmbg " they said that offices,{w=0.2} hospices and even hospitals can arrange visits with them too!"
        
        if Natsuki.isAffectionate(higher=True):
            n 3nchgn "Pretty awesome,{w=0.2} right?{w=0.75}{nw}"
            extend 3clrsm " Ehehe..."
            n 4clrslsbl "..."
            n 5ksrbosbl "..."
            n 1kcsflesi "..."
            n 4kllbo "It...{w=1}{nw}" 
            extend 4kslbo " just sucks sometimes,{w=0.2} thinking about it now.{w=0.75}{nw}"
            extend 4knmbol " You know?"
            n 5cslcal "...W-{w=0.2}with Sayori and all."
            n 5cslfll "She...{w=1}{nw}" 
            extend 4cdlbol " wasn't around that day we had the visit.{w=0.75}{nw}"
            extend 4cslbol " Doesn't exactly take a genius to figure out why."
            n 2ccsfllsbl "I-{w=0.2}it's just that..."

            if Natsuki.isEnamored(higher=True):
                n 2ksrbolsbl "..."
                n 2ksrfllsbr "I can't help but think if just having one around could have {i}done{/i} something for her.{w=0.75}{nw}"
                extend 5knmbolsbr " One of those support animals."
                n 4ccsemlsbr "I...{w=1}{nw}" 
                extend 4ccsfllsbr " know...{w=1}{nw}" 
                extend 4cdlbolsbr " they can't work miracles.{w=0.75}{nw}"
                extend 2ccssrlsbr " I-{w=0.2}I'm not {i}naive{/i}."
                n 4kslpulsbr "But..."
                n 4kslfllsbr "It would have been something...{w=1}{nw}"
                extend 5knmbolsbr " right?"
                n 5ksrbolsbr "...Maybe just that one thing could have made {i}some{/i} sort of difference."
                n 7ksrsllsbl "..."
                n 3ccsfllsbl "...A-{w=0.2}anyway."

            else:
                n 4cslunlsbl "..."
                n 4ccsemlsbl "...N-{w=0.2}nevermind.{w=0.75}{nw}"
                extend 2cllfllsbl " It's..."
                n 2cdlsllsbr "...Not really something I wanna think about right now."
                n 2nslbolsbr "S-{w=0.2}sorry."
                n 2nslbol "..."
                n 4ccsajl "A-{w=0.2}anyway."

        else:
            n 3nchgn "Pretty awesome,{w=0.2} right?{w=0.75}{nw}"
            extend 3fchsm " Ehehe."
            n 4ulrss "Well,{w=0.2} anyhow..."

        n 3ulrbo "It wasn't a super big visit or anything,{w=0.5}{nw}"
        extend 3csrss " so the volunteers didn't stick around for {i}that{/i} long..."
        n 4uchgn "But they did let us go up and meet the animals they brought in with them!"
        n 3fcssmesm "No surprises who got picked to go up first.{w=0.75}{nw}"
        extend 3fsqsm " Ehehe."
        n 4fcsbg "Yep!"
        n 2ullbg "When it comes to those kinds of animals,{w=0.2} it's gotta be said.{w=0.75}{nw}"
        extend 6fchbg "\nNothing beats a real hands-on experience!"
        n 2fchsm "Ahaha.{w=0.75}{nw}"
        extend 2tllss " Well,{w=0.2} anyway."
        n 4ullaj "I think I've gone on for way too long already,{w=0.5}{nw}"
        extend 6fcssmesm " but I hope you learned something,{w=0.2} [player]!"
        n 3fsqbg "And if not?"
        n 4fcsss "Heh.{w=0.75}{nw}"
        extend 4tllss " Well..."
        n 7tsqss "You're an animal too,{w=0.2} right?{w=0.75}{nw}"
        extend 7fcssm " Don't sweat it too much,{w=0.2} [player]..."
        n 3fchgnelg "Pretty sure I can train {i}you{/i} up just as well!"

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "Love you too,{w=0.2} [chosen_tease]~!"

        else:
            n 3fwlbg "You're welcome,{w=0.2} [player]!"

    else:
        n 7tllbo "They're like animals specially trained to help people with stuff they couldn't do normally -{w=0.5}{nw}"
        extend 7cllpu " or at all."
        n 2csqsl "Yeah,{w=0.2} no kidding.{w=0.75}{nw}"
        extend 2clrfl " Everyone's heard of guide dogs.{w=1}{nw}"
        extend 2fcsca " But people forget all the other stuff trained up animals can help out with."
        n 4clltr "Mobility,{w=0.2} hearing issues...{w=1}{nw}"
        extend 4cllca " medical conditions and allergies too,{w=0.2} actually."
        n 2cslaj "I suppose that kind of animal help is cool and all.{w=0.75}{nw}"
        extend 2cnmsl " But what really stuck out to me were the therapy and emotional support animals.{w=0.75}{nw}"
        extend 2csrfl " Even if they {i}didn't{/i} get as much focus."
        n 7clrfl "I guess they're kinda like super-tame pets people have to help them get through a rough time."
        n 2fcssl "Heh.{w=0.75}{nw}"
        extend 2fsqfr " Ring any bells,{w=0.2} {i}[player]{/i}?"
        n 2cllfl "You get dogs and cats -{w=0.5}{nw}"
        extend 2cslfl " obviously -{w=0.5}{nw}"
        extend 4nlraj " but you can get miniature horses and all sorts too nowadays."
        n 1ulrfl "You can even get visits arranged to hospitals and hospices now,{w=0.2} so..."
        n 2cdrbo "Yeah.{w=0.75}{nw}"
        extend 2cdrsl " That's about all I had to say about it."

        if Natsuki.isUpset(higher=True):
            n 1fcssl "Heh.{w=0.75}{nw}"
            extend 1fllpu " And besides."
            n 4fslfl "Not like you listen to much else I say anyway.{w=0.75}{nw}"
            extend 4fsqsl " {i}Right{/i}?"

        else:
            n 1fcsem "Heh.{w=0.75}{nw}"
            extend 1fsrem " And besides..."
            n 4fslsr "I can think of at least {i}one{/i} animal that could use some extra training right now...{w=0.75}{nw}"
            extend 4fsqan " {i}[player].{/i}"

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
            category=["Health", "Technology"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    if get_topic("talk_using_computers_healthily").shown_count > 0:
        n 3tllsl "..."
        n 7tslbo "..."
        n 7tslfl "Say...{w=1}{nw}"
        extend 7tnmfl " [player]?{w=0.75}{nw}"
        extend 3unmaj " You got a minute?{w=0.75}{nw}"
        extend 3tnmbo " I gotta ask you a question."
        n 7tslsl "..."
        n 7tslaj "So...{w=1}{nw}"
        extend 7unmaj " you've been visiting me for a while already,{w=0.2} huh?{w=0.75}{nw}"
        extend 3ulrbo " You know,{w=0.2} using your computer and everything."
        n 4csrss "And I'm pretty sure I went through how to make sure you aren't just setting yourself up for some major hurt down the line already."
        n 4tlraj "But...{w=1}{nw}"
        extend 7tnmaj " I gotta ask."
        n 3fnmbg "Just how much of that exactly do you{w=0.3}{nw}"
        extend 3fsqbg " {i}actually{/i}{w=0.3}{nw}"
        extend 3fnmbg " remember,{w=0.75}{nw}"
        extend 3fsqsm " [player]?"
        n 4fnmbg "Huh?"
        n 4tsqsm "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 2fcsbg " Yep,{w=0.2} just as I thought.{w=0.75}{nw}"
        extend 2nchgn " Total silence!"
        n 4fllbg "Well [player],{w=0.2} have no fear."
        n 6fcssmedz "'Cause it's time for a little refresher on how {i}not{/i} to ruin your spine from yours truly!"

    else:
        n 7tslsl "..."
        n 7cslpu "...Huh."
        n 7tnmaj "You know,{w=0.2} [player]...{w=1}{nw}"
        extend 3tlraj " I just thought of something.{w=0.75}{nw}"
        extend 3unmbo " About how you actually visit me and all."
        n 7ulraj "So...{w=1}{nw}"
        extend 2tlrfl " you gotta be at your desk to actually talk to me,{w=0.5}{nw}"
        extend 2tnmca " right?{w=0.75}{nw}"
        extend 4cslss " Or using some kind of computer at least."
        n 7tslpu "And you've been here for a bunch of time already too,{w=0.2} now that I think about it."

        if Natsuki.isEnamored(higher=True):
            n 3unmfll "N-{w=0.2}not that I'm saying I don't appreciate it or anything like that!\n{w=0.75}{nw}"
            extend 3ccsajlsbr "O-{w=0.2}of course I do!"
            $ chosen_tease = jn_utils.getRandomTease()
            n 5csrbolsbr "I shouldn't even have to remind you by now,{w=0.2} [chosen_tease]."

        elif Natsuki.isAffectionate(higher=True):
            n 3unmeml "N-{w=0.2}not that it's a problem,{w=0.5}{nw}" 
            extend 3clremlsbl " or anything like that!{w=0.75}{nw}"
            extend 3ccspolsbl " Y-{w=0.2}you should know it isn't by now anyway,{w=0.2} [player]."

        else:
            n 3unmeml "N-{w=0.2}not that I'm saying it's some kind of problem or anything like that,\n{w=0.5}{nw}" 
            extend 4ccsgslsbl "{i}obviously{/i}!"
            n 2csrbolsbl "..."

        n 4clrpu "Though..."
        n 7tnmflsbr "Doesn't that mean you're spending a whole bunch of extra time sat around with your computer every day?{w=0.75}{nw}"
        extend 3tsqslsbr " Just for my sake?"
        
        if (
            Natsuki.isAffectionate(higher=True) 
            and (jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork) 
            or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding) 
            or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.work_applications))
        ):
            $ activity_options = []
            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
                $ activity_options.append("drawing")

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding):
                $ activity_options.append("coding")

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.work_applications):
                $ activity_options.append("working")

            if len(activity_options) > 0:
                $ activity_mention = random.choice(activity_options)
                n 2ccsfl "I mean...{w=1}{nw}"
                extend 2ulraj " I know you use your computer already for a bunch of stuff.\n{w=0.75}{nw}"
                extend 4fchbg "Like [activity_mention]!"

        else:
            n 2ccsfl "I mean...{w=1}{nw}"
            extend 2tllsl " I guess you probably still use your computer for other stuff already."

        n 1ccsflsbl "But that still doesn't change the fact you're gonna be racking up a load of extra screen time thanks to me."
        
        if Natsuki.isEnamored(higher=True):
            n 2clrfllsbl "And the last thing I wanna hear about is you getting yourself all cramped up because you were slouched over like a potato for hours."
            n 2cllsl "..."

        else:
            n 2ccsaj "And the last thing I wanna hear is you complaining your back hurts because nobody had the brains to tell you not to slouch like a potato for hours."
            n 2ccspol "I-{w=0.2}I'm not having {i}that{/i} on my conscience."

        n 1ccsss "Heh.{w=0.75}{nw}"
        extend 4fsrss " In fact..."
        n 2fnmbg "You know what,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2fsqsm " I hope you're sitting."
        n 6fcsbg "'Cause I'm gonna make sure you're using your computer the {i}right{/i} way,{w=0.5}{nw}"
        extend 3fchgn " whether you like it or not!"

    n 1fcsbg "Alright,{w=0.75}{nw}"
    extend 6fcsaj " so number one:{w=1}{nw}" 
    extend 3unmbg " posture!"
    n 1ccsflsbl "...And no,{w=0.2} [player].{w=0.75}{nw}"
    extend 4csqtr " I mean {i}actual{/i} posture.{w=0.75}{nw}"
    extend 4ccspo " The sitting kind."
    n 3fnmfl "Now sit up straight,{w=0.2} and keep that back of yours against the chair,{w=0.2} [player].{w=0.75}{nw}"
    extend 3fcsgs " I mean it!"
    n 4cllfl "Seriously -{w=0.5}{nw}"
    extend 4tsqem " unless you feel like making friends with your nearest chiropractor,{w=0.5}{nw}"
    extend 4cslem " trust me when I say you {i}really{/i} don't wanna spend all your time slouching."
    n 2csqss "...Or hunched up on your chair like some kind of weird computer gremlin."
    n 6unmaj "If you're doing it right,{w=0.5}{nw}"
    extend 3ullaj " then you should have your arms and thighs parallel to the ground,{w=0.5}{nw}"
    extend 3fcssm " with your eyes roughly at the top of your screen.{w=0.75}{nw}"
    extend 3fcsbg " Easy peasy!"
    n 4unmfl "Oh,{w=0.2} right -{w=0.5}{nw}"
    extend 2clrsssbl " make sure your feet can still touch the floor,{w=0.2} though.\n{w=0.75}{nw}"
    extend 2fcscasbr "Even {i}I{/i} can do that,{w=0.2} [player]."
    n 1fnmaj "Number two:{w=0.75}{nw}"
    extend 2fcsbg " distance!"
    n 2clrbg "It's pretty easy to forget,{w=0.5}{nw}"
    extend 4tnmbo " but if you wanna avoid sore eyes then you've gotta make sure you're actually a decent distance from the screen too."
    n 2fcsca "Not right up close or so far away you need binoculars!"

    if Natsuki.isEnamored(higher=True):
        n 2fcsbglsbr "I-{w=0.2}I know you just can't get enough of me,{w=0.2} [player].{w=0.75}{nw}"
        extend 4cslfllsbr " But really."
        n 4ccspol "Even I don't wanna see you practically pressing your face against the screen either."

    elif Natsuki.isAffectionate(higher=True):
        n 2fsrsslsbr "I-{w=0.2}I know I {i}am{/i} pretty awesome,{w=0.5}{nw}"
        extend 4csqflsbr " but the last thing I wanna be greeted by is your face right up against the screen either."

    else:
        n 2ccsflsbr "A-{w=0.2}and besides,{w=0.5}{nw}"
        extend 2cslflsbr " the last thing I wanna see is your face all smushed up against the screen,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccsposbr " I didn't ask for {i}that{/i}."

    n 2ulraj "So...{w=1}{nw}"
    extend 4tsgbg " just make sure you're sitting about an arm's length away from the screen.{w=0.75}{nw}"
    extend 4ccsbg " That's all I'm saying!"
    n 3unmpu "Don't forget to keep all your stuff in easy reach though -{w=0.5}{nw}"
    extend 3ccsbg " unless you're a psychic,{w=0.5}{nw}"
    extend 6csqsm " you aren't getting far if you can barely hit the keyboard."

    if get_topic("talk_using_computers_healthily").shown_count > 0:
        n 7ullaj "And remember,{w=0.2} there's plenty of stuff to see beyond the screen -{w=0.5}{nw}"
        extend 3fcsbg " so you better be giving your eyes a break too!"

    else:
        n 7ullfl "And while you're at it?{w=0.75}{nw}"
        extend 7ullaj " Spend some time looking at something {i}other{/i} than the screen too,{w=0.5}{nw}"
        extend 7unmbo " for that matter."
        n 3fcsbg "You've got windows there,{w=0.2} right?{w=0.75}{nw}"
        extend 3fsqbg " So you better be using them!"

    n 7ccsbg "Now,{w=0.2} number three:{w=0.75}{nw}"
    extend 3fchbg " breaks!"
    n 3tllfl "I don't know about you [player],{w=0.5}{nw}"
    extend 7tnmbo " but personally?{w=0.75}{nw}"
    extend 7csrem " I can't stand being sat staring at a screen for hours at a time."
    n 3cnmem "Seriously -{w=0.5}{nw}"
    extend 4cllan " I keep getting distracted if I'm stuck in front of my laptop for too long.{w=1}{nw}"
    extend 4fcsem " It's the worst!"
    n 2fslem "Plus on top of that,{w=0.5}{nw}"
    extend 2csqsl " you're {i}really{/i} not doing your circulation a favor either."
    n 6fcsbg "...So get off your butt and do some stretches or something!{w=0.75}{nw}"
    extend 3clraj " Or even go get some water if you {i}really{/i} need an excuse to get moving."
    n 3tnmbo "Really,{w=0.2} it doesn't matter what you do.{w=0.75}{nw}"
    extend 4ccsca " It's all about getting off your rear,{w=0.2} back on your feet,{w=0.2} and giving your eyes a break.{w=0.75}{nw}"
    extend 6ccsbg " Simple enough!"
    n 3fsqsm "..."
    n 3fsqss "Well?{w=0.75}{nw}"
    extend 7fcsbg " Still following me,{w=0.2} [player]?"
    n 3flraj "You better be.{w=0.75}{nw}"
    extend 3fnmfl " This one's easily the most important,{w=0.2} so listen up!"
    n 4tllfl "Don't get the wrong idea,{w=0.2} [player] -{w=0.5}{nw}"
    extend 4tsqfl " obviously you're gonna know your limits better than I do."
    n 2tlrpu "But...{w=1}{nw}" 
    extend 2tnmbo " if you start feeling kinda weird or sick,{w=0.2} or your eyes start hurting or something while you're around?"
    n 2cllaj "Just..."
    n 1cdlsll "..."
    n 4ccsfllsbl "...Just don't be a total dummy about it.{w=0.75}{nw}"
    extend 4csqfllsbl " Alright?"
    n 2clrflsbr "I'm being serious here."
    n 2cnmslsbr "Call it quits on whatever you were doing and just come back to it later.{w=0.75}{nw}"
    extend 1csqbosbr " Got it?"
    n 3ccstr "Work or some dusty old assignment can wait if you're just gonna make yourself even worse trying to impress someone."
    n 3csqbo "No,{w=0.2} your boss or professor isn't going to drop dead if that stinky report isn't done today."
    n 1ccsss "Heh.{w=0.75}{nw}"
    extend 4clrss " Anyway,{w=0.2} think about it."
    n 3tnmbo "It isn't like you're going to pull some kind of miracle if you try and push through it all."
    n 3ccsaj "All you're gonna achieve is make yourself feel like crap for even longer.{w=0.75}{nw}"
    extend 3fcsca " It's totally pointless."
    
    if Natsuki.isEnamored(higher=True):
        n 2cllca "...And besides,{w=0.2} [player]."
        n 2cllpulsbl "You know I'm not going to get mad or anything if you have to take a rain check on our time together..."
        n 4knmbolsbl "Right?"
        n 4klrbolsbl "..."
        n 2ccsfllesisbl "..."
        n 2cnmsll "...Look."
        n 1fcspul "I...{w=1}{nw}"
        
        if Natsuki.isLove(higher=True):
            extend 1ncspul " really...{w=1}{nw}"
        
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 4csrbol " care about you,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"
        extend 5cnmbol " You should seriously know that by now."
        n 3ccsajl "...Just like you should know you I'm {i}not{/i} gonna be impressed by some weird macho display of toughing it out."
        n 3cnmpol "Capiche?"
        n 3cslbol "..."

    elif Natsuki.isAffectionate(higher=True):
        n 2cllflsbr "A-{w=0.2}and besides,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccssllsbl " I'm not {i}that{/i} selfish."
        n 4csrajlsbl "You {i}do{/i} know I won't get mad or anything if you really have to go for a while..."
        n 4cnmsllsbl "Right?"
        n 1cslbolsbl "..."

    else:
        n 2fcstr "A-{w=0.2}and besides,{w=0.2} [player]."
        n 2clrajsbl "It's not like I'm gonna get mad at you or anything like that either if you gotta duck out.{w=0.75}{nw}"
        extend 2clrsll " Even I'm not that much of a jerk."
        n 1clrbol "..."

    n 4ccsflsbr "A-{w=0.2}anyway."
    n 4ullaj "I've gone on way long enough already,{w=0.5}{nw}"
    extend 2cnmca " so I'm just gonna say this,{w=0.2} [player]."
    n 7fcsaj "You might end up with a crappy back or nasty eyes if you aren't careful..."
    n 3fcspo "...But that's gonna be nothing compared to the grade-A earache you're getting if you come crying to me later!"
    n 3fsqsm "Ehehe."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fchbll "Love you too,{w=0.2} [chosen_tease]!"

    else:
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 4fchgnedz "You're welcome,{w=0.2} [chosen_descriptor]!"

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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_active:
    n 1nnmbo "Hey,{w=0.1} [player]..."
    n 3nllsr "You should get out more."
    n 1fsqsm "..."
    n 4fchbg "Ahaha!{w=0.2} No,{w=0.1} really!{w=0.2} I'm serious!"
    n 1ulraj "At school,{w=0.1} it was super easy to get exercise since we had to walk everywhere,{w=0.1} and we had sports and such..."
    n 1nsqsf "It's not so straightforward when you have a job and other stuff to worry about,{w=0.1} though."
    n 2fllss "I'm not gonna lie and say I worked out or anything like that..."
    n 1ullaj "But I tried to get some walks in when I could.{w=0.5}{nw}"
    extend 4uchgn " Any excuse to hit the bookshop is reason enough for me!"
    n 2kslsl "...Or {i}was{/i} reason enough, anyway."
    n 1fllaj "But still {w=0.1}-{w=0.5}{nw}"
    extend 1unmbg " you should give it a shot too,{w=0.1} [player]!"
    n 1nlrss "It doesn't have to be a hike or anything crazy{w=0.1} -{w=0.3}{nw}"
    extend 1nnmsm " it's more about keeping at it,{w=0.1} really."
    n 1fchsm "Even a daily ten minute walk will help you feel refreshed and awake!"
    n 4ullaj "So...{w=0.5}{nw}"
    extend 4fnmss " make sure you get out soon,{w=0.1} [player]."

    if Natsuki.isEnamored(higher=True):
        n 3fchbg "I wanna see you fighting fit!{w=0.5}{nw}"
        extend 3uchsm " Ehehe."
        return

    n 1fchbl "It's the least you can do!"
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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_relieving_stress:
    n 1ullaj "You know,{w=0.1} I'll admit it,{w=0.1} [player]."
    n 2flrbgsbl "I...{w=0.3} kinda have a short fuse.{w=0.5}{nw}"
    extend 1klrsssbl " Ehehe."
    n 1fnmss "I've been trying to work on that though,{w=0.3}{nw}"
    extend 1fchbg " and I'd love to share some of the ways I deal with stress!"
    n 1unmss "Personally,{w=0.1} I think the best way to deal with it if you can is to try and create some distance."
    n 2nslss "Back before all of...{w=0.3} this,{w=0.5}{nw}"
    extend 2nllss " if things got a little too much,{w=0.1} I just stepped outside if I could."
    n 1unmbo "Some fresh air and a change of scenery can really put things into context.{w=0.5}{nw}"
    extend 4fwdaj " It's crazy effective!"
    n 4ulraj "But don't just create physical distance,{w=0.1} though.{w=0.5}{nw}"
    extend 1fnmpu " Distance yourself mentally too!"
    n 3ncssr "If something is stressing you out,{w=0.1} you need to starve it of attention."
    n 3fslpo "I can't really go outside now,{w=0.5}{nw}"
    extend 1nllsf " so I just read something,{w=0.1} or watch some dumb videos."
    n 1fchbg "But do whatever works for you; {w=0.1}we all have our own comfort zones!"
    n 2fslpo "A-{w=0.1}and of course,{w=0.1} you could always come see me,{w=0.1} you know..."
    n 1fchbgl "A-{w=0.1}anyway!"
    n 1unmpu "The point is to always try and come back with a clean headspace,{w=0.3}{nw}"
    extend 1nnmss " and don't sweat the small things."
    n 4tnmss "You can manage that,{w=0.1} right [player]?"
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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_careful_spending:
    n 1tllsr "..."
    n 1fllsr "..."
    n 1tnmpu "Hmm...?"
    n 4uwdgsesu "O-{w=0.1}oh!{w=0.5}{nw}"
    extend 1flrbg " A-{w=0.1}aha!{w=0.5}{nw}"
    extend 4fsrdvl " I spaced out!"
    n 1unmaj "I was just thinking..."
    n 1flrbo "It's so easy to spend more than you mean nowadays,{w=0.1} you know?"
    n 2flrpu "Like...{w=0.3} it seems everywhere you look,{w=0.1} there's a sale,{w=0.1} or deals,{w=0.1} or some kind of special offer..."
    n 1unmpu "And every place accepts all kinds of ways of paying,{w=0.1} too.{w=0.5}{nw}"
    extend 3fsrpo " They make it super convenient!"
    n 3fnmun "I guess what I'm getting at is...{w=0.3} try to be careful of your spending habits,{w=0.1} okay?"
    n 1uslss "Try not to buy junk you don't need{w=0.1} -{w=0.3}{nw}"
    extend 1flrbg " think of how much you threw away the last time you cleaned out!"
    n 4uwdajl "T-{w=0.1}that's not to say you shouldn't treat yourself,{w=0.1} of course!{w=0.5}{nw}"
    extend 4flrssl " You deserve cool stuff too!"
    n 1fcsss "Money can't buy happiness...{w=0.5}{nw}"
    extend 1fchgn " but it sure as hell makes finding it easier.{w=0.5}{nw}"
    extend 1uchbselg " Ahaha!"
    n 4nllss "Well,{w=0.1} anyway.{w=0.5}{nw}"
    extend 1tnmsg " Just try to think a little before you spend,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
    extend 1uchbs " that's all I'm saying!"

    if Natsuki.isAffectionate(higher=True):
        n 3nslbg "Besides..."
        n 1fsqsm "Gotta save up all we can for when we can hang out,{w=0.1} right?{w=0.5}{nw}"
        extend 1uchsm " Ehehe."

        if Natsuki.isLove(higher=True):
            n 4uchbgl "Love you,{w=0.1} [player]~!"

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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n 4unmaj "Hey,{w=0.1} [player]..."
    menu:
        n "Have you eaten today?"

        "Yes":
            n 1fnmbg "Aha!{w=0.5}{nw}"
            extend 3fsqbg " But did you eat {i}well{/i},{w=0.1} [player]?"

        "No":
            n 1knmpu "Huh?{w=0.2} What?{w=0.5}{nw}"
            extend 2knmem " Why not?!"
            n 1fnmpu "You aren't skipping meals,{w=0.1} are you?"
            n 3flrpo "You better not be,{w=0.1} [player]."

    n 1unmpu "It's super important to make sure you aren't only eating regularly,{w=0.3}{nw}"
    extend 1fnmpu " but eating decently too!"
    n 1fnmsr "The right diet makes all the difference,{w=0.1} [player]."
    n 4ullaj "So...{w=0.5}{nw}"
    extend 1nsgaj " try and make an effort with your meals,{w=0.1} got it?"
    n 1fnmaj "And I mean a real effort!{w=0.5}{nw}"
    extend 1ulrss " Try to prepare them from scratch if you can;{w=0.3}{nw}"
    extend 2fsrss " it's often cheaper than ready meals anyway."
    n 1unmss "Cut back on things like salt and sugar and stuff too...{w=0.5}{nw}"
    extend 3nslpo " as well as anything really processed."
    n 1unmaj "Oh {w=0.1}-{w=0.3}{nw}"
    extend 4fnmaj " and like I said,{w=0.1} have meals regularly too!"
    n 1fchbg "You shouldn't find yourself snacking on junk if you have proper meals throughout the day."
    n 1usqsm "Your bank balance and your body will thank you.{w=0.5}{nw}"
    extend 4nchsm " Ehehe."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "And besides..."
        n 3usqss "I gotta get you into good habits by yourself before I'm there to make you."
        n 1fchgnelg "Ahaha!{w=0.2} I'm kidding,{w=0.1} [player]!{w=0.2} I'm kidding!"
        n 4fsqsm "...Mostly."

        if Natsuki.isLove(higher=True):
            n 4uchsm "Love you, [player]~!{w=0.2} Ehehe."
            return

    n 1fllss "Now...{w=0.3} where were we?"
    return

# Natsuki brings up the idea of in-game weather, and guides the player through installation
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_weather_setup_main",
            unlocked=True,
            prompt="Setting up the weather",
            category=["Setup", "Weather"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_weather_setup_main:
    if persistent._jn_weather_api_key:
        $ persistent._jn_weather_setup_started = True

    if persistent._jn_weather_setup_started:
        # Player has already done at least some of the setup process, so offer range of options
        n 4unmajesu "Oh!{w=1}{nw}"
        extend 1fcsbg " Yeah,{w=0.1} I remember!"
        n 1ulraj "So..."
        show natsuki 1unmbg at jn_center

        menu:
            n "Where did you wanna start from,{w=0.1} [player]?"

            "I want to give you an API key.":
                # API key
                n 4unmaj "You wanna give me an API key?{w=1}{nw}"
                extend 1fchbg " Sure!"
                n 3nchbg "I'll just walk you through it just in case,{w=0.1} 'kay?"

                # Reset configuration state
                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_api_key

            "I want to give you my location." if persistent._jn_weather_api_key:
                # Location
                n 4unmaj "You wanna go through your location?{w=1}{nw}"
                extend 1fchbg " Sure!"
                n 3nchbg "I'll just walk you through it just in case,{w=0.1} 'kay?"

                # Reset configuration state
                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_location

            "Can you try testing everything I've told you again?" if persistent._jn_weather_api_key and persistent._jn_player_latitude_longitude:
                # Retry verification
                n 4unmaj "You just want me to try testing it all again?{w=0.75}{nw}"
                extend 1fchbgeme " Right-o!"

                # Reset configuration state
                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_verify

            "Nevermind.":
                # Cancel
                n 1tsqpu "Uh...{w=0.5}{nw}"
                extend 2tsrpu " huh."
                n 1fchbg "Well,{w=0.1} your loss,{w=0.3} [player]!"
                extend 4fchsm " Ehehe."

                return

    else:
        # Introduction
        n 3fslbo "..."
        n 3fcsem "Urgh...{w=1.5}{nw}"
        extend 4fsrem " so annoying!"
        n 1fbkwr "Why is this so hard to get right...?!"
        n 2fllpo "Stupid...{w=0.5}{nw}"
        extend 2fcsan " Nnnnnn-!"

        menu:
            "What's the matter, Natsuki?":
                n 4uwdpueqm "Huh?{w=0.5}{nw}"
                extend 4uwdajesu " Oh!{w=0.5} [player]!{w=1}{nw}"
                extend 1fllbgsbr " I'm glad you asked!"

            "What're you complaining about?":
                n 1fwdemesh "...!{w=0.5}{nw}"
                n 2fcsgs "Well,{w=0.1} your attitude,{w=0.1} for one thing!{w=1}{nw}"
                extend 2fslca " Anyway..."

        n 1ullaj "So...{w=0.5}{nw}"
        extend 1flrss " I'm not really one to just sit around and admire the view."
        n 4nsqbo "But seriously,{w=0.1} [player]...{w=1}{nw}"
        extend 2fllpo " it's super boring out there!"
        n 2nsqpo "Outside the room,{w=0.1} I mean.{w=1}{nw}"
        extend 1fbkwr " Nothing ever changes!"
        n 1ulraj "But...{w=1}{nw}"
        extend 1fchbg " I've been doing a little tinkering,{w=0.1} and I think I found a way to make things a little more dynamic!"
        n 3fslsr "I just can't get it all to work properly..."
        n 1fcsem "It's just...{w=1}{nw}"
        extend 1fcssr " it's really bugging me.{w=1}{nw}"
        extend 2fslan " I hate it when I can't get stuff to go right!"

        menu:
            "Perhaps I could help?":
                n 1uwdpu "Huh?{w=0.5}{nw}"
                extend 1unmbg " Really?!{w=0.5}{nw}"
                extend 4nchbs " Thanks,{w=0.1} [player]!"
                n 4fllssl "N-{w=0.3}not that I was {i}waiting{/i} for help,{w=0.1} {i}obviously{/i}!"

            "What do I have to do?":
                n 2fcsem "Jeez,{w=0.1} [player]...{w=0.3}"
                extend 2fsqpo " what's with the attitude today?"
                n 4kslpo "I'm {i}trying{/i} to do something nice here..."

        n 1ullaj "Well,{w=0.1} anyway..."
        n 4fslss "What I'm {i}trying{/i} to do is add some atmosphere to this place,{w=1}{nw}"
        extend 1fsqsm " and what better way to do that than..."
        n 1fchbg "Some actual weather!"
        n 1nsqsl "And not {i}just{/i} some randomly changing thing..."
        n 2ulraj "I wanna set things up so the weather here matches what it's like where you are,{w=0.1} [player]."
        n 1fcsbg "I know{w=0.1} -{w=0.5}{nw}"
        extend 4fwlbg " awesome,{w=0.1} right?"
        n 1ullaj "But...{w=1}{nw}"
        extend 4nnmbo " I need you to go to this website I found."
        n 1kchbg "Don't worry,{w=0.1} I won't make you go search for it.{w=1}{nw}"
        extend 1kchbgess " I'm not {i}that{/i} mean!"
        n 1unmss "It's called OpenWeatherMap,{w=0.5}{nw}"
        extend 1uchbg " and it's {i}super{/i} cool!{w=1}{nw}"
        extend 3fcssm " It's just what I need to make this work."
        n 1fllss "I'll need a little time to get this all set up,{w=0.1} though.{w=1}{nw}"
        extend 4ulraj " So..."

        menu:
            n "Are you okay if we get started now,{w=0.1} [player]?"

            "Sure.":
                n 1uchbg "Alright!"
                $ persistent._jn_weather_setup_started = True
                jump talk_weather_setup_api_key

            "I can't right now.":
                n 1nnmbo "Oh.{w=1.5}{nw}"
                extend 4nllsssbl " Well..."
                n 1nsldv "Just let me know when you have the time,{w=0.1} 'kay?"
                n 3fcsbg "It'll be {i}super{/i} worth it!"
                return

label talk_weather_setup_api_key:
    # Direct the player to the website
    n 1nnmss "Okaaay!{w=1}{nw}"
    extend 3fchbg " Let's get started!"
    n 1ullaj "So like I said{w=0.1} -{w=0.3}{nw}"
    extend 1unmaj " the website is called OpenWeatherMap.{w=1}{nw}"
    extend 4nnmsm " You can get there from {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_HOME]}here{/a}!"
    n 1ulraj "So..."

    menu:
        n "Do you have the website open,{w=0.1} [player]?"

        "Yes, I have the website open.":
            n 1nchbs "Awesome!{w=0.5}{nw}"
            extend 4nwlbg " Step one complete!"

        "No, I couldn't get to the website.":
            n 4tnmaj "Huh?{w=1} Why not?{w=1}{nw}"
            extend 1tnmsr " Is it down or something?"
            n 2tslaj "Well...{w=1}{nw}"
            extend 2tnmss " Maybe we can try this again later?"
            n 1fllsssbr "Just let me know when you're ready!"

            jump ch30_loop

    # Prompt the player to create an account
    n 1nchbg "'Kay!{w=0.5}{nw}"
    extend 3fcssm " Now for step two!"
    n 1nllaj "Basically I need something called an API key,{w=1}{nw}"
    extend 1nnmbo " which will let me use that website to find out what the weather is like over there."
    n 3fslbo "But I can't do that myself...{w=1.5}{nw}"
    extend 1fchsm " which is where you come in,{w=0.1} [player]!"
    n 1nlrss "You'll need to make an account before you can get an API key."
    extend 1kchbgess " It's totally free though!"
    n 1ullaj "You can create an account {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}here{/a},{w=1}{nw}"
    extend 1nnmsm " or you can sign in using the menu at the top."
    n 3fcsaj "Just make sure to go through all the options carefully{w=0.1} -{w=0.5}{nw}"
    extend 3nsqpo " don't just dash through it!"
    n 1unmaj "Oh{w=0.1} -{w=0.5}{nw}"
    extend 1flrss " and make sure you confirm your email address once you've created it,{w=0.1} 'kay?"
    n 4nchbg "{a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}Here's{/a} that link once more,{w=0.1} just in case!"
    n 1fnmsm "Now..."

    menu:
        n "Did you get an account sorted,{w=0.1} [player]?"

        "Yes, I have an account set up.":
            n 1fchsm "Awesome!"
            n 3tllss "You'll probably want to make sure you save your login details somewhere secure,{w=0.5}{nw}"
            extend 4fchsm " juuuust in case."
            n 1fchts "Don't forget to confirm your email address too!"
            n 1fsqsm "Now,{w=0.1} here comes the challenging part..."

        "I already had an account set up.":
            n 1fchsm "Awesome!{w=0.5}{nw}"
            extend 3fwlbg " The rest of this should be a piece of cake!"

    # API Key

    # Prompt the player for an API key
    n 1usqsm "Are you ready,{w=0.1} [player]?"
    n 1fchsm "You need to get your API key and send it to me!"
    n 4ullss "You can find your keys {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}here{/a},{w=1}{nw}"
    extend 1unmaj " or you can get there using the menu like before."
    n 3tsqsm "You got all that?"
    n 3fsqsm "Ehehe.{w=0.5}{nw}"
    extend 4fchbg " Then take it away,{w=0.1} [player]!"

    $ player_input_valid = False

    # Process the player's input
    while not player_input_valid:

        $ player_input = renpy.input("Enter your API key (or type Nevermind to go back):")

        if not player_input or player_input == "":
            n 3tsqsm "I {i}thought{/i} I asked for an {i}API key{/i},{w=0.1} [player]?"
            extend 4fchbl " Try again!"

        elif player_input.replace(" ", "").lower() == "nevermind":
            # Allow the player to back out
            n 4tnmaj "Huh?{w=0.2} You don't wanna continue?"
            n 1tllbo "That's fine,{w=0.1} I guess."
            n 1fcsbg "Just let me know when you're ready,{w=0.1} 'kay?"

            jump ch30_loop

        else:
            # Get ready to lead in to the next stage of setup
            $ player_input_valid = True
            $ persistent._jn_weather_api_key = player_input
            n 1uchbg "Alright!{w=0.2} I got it!"

            jump talk_weather_setup_location

label talk_weather_setup_location:
    n 1fsqbg "Now for the final piece of the puzzle..."
    n 4uchss "...Your location,{w=0.1} obviously!"
    n 1ullaj "There's a couple ways to do this,{w=1}{nw}"
    extend 1nnmsm " but I thought it'd be best to just ask."
    n 4ulraj "So..."

    menu:
        n "How do you wanna tell me, [player]?"

        "Can you try locating me through the Internet?":
            n 1fchsm "Sure, I can give it a shot!{w=1}{nw}"
            extend 1fcssm " Just give me a second here...{w=1}{nw}"

            $ ip_latitude_longitude = jn_atmosphere.getLatitudeLongitudeByIpAddress()
            if not ip_latitude_longitude:
                # We couldn't get the coordinates via IP, so we have to prompt them via the player
                n 2fslpu "...Huh."
                n 2knmpo "I {i}tried{/i} to look you up, but I couldn't find anything!"
                n 2flrpo "..."
                n 1tlraj "Well..."
                extend 1tllbgsbl " looks like we're gonna have to do things the old-fashioned way,{w=0.1} [player]."

                jump talk_weather_setup_manual_coords

            else:
                # Success, confirm with player
                n 4fsgss "Aha!{w=0.5}{nw}"
                extend 1uchbg " I think I got it!"
                n 3nwlbg "Now...{w=0.3} wanna see something awesome, [player]?{w=1}{nw}"
                extend 3fsqsm " I know you do."
                n 1ncsbo "...{w=1}{nw}"

                python:
                    # Try to show the map, and come back with the result to drive dialogue
                    show_map_success = False
                    try:
                        jn_open_google_maps(ip_latitude_longitude[0], ip_latitude_longitude[1])
                        show_map_success = True

                    except Exception as exception:
                        store.jn_utils.log(exception.message, jn_utils.SEVERITY_ERR)

                if show_map_success:
                    n 1fchbg "Ta-da!{w=0.5} Found you!"
                    n 1fsqsm  "..."
                    n 3tsqsm "Well?{w=1}{nw}"
                    extend 3tsqss " Am I right or what, [player]?"
                    menu:
                        "Yes, you found me.":
                            n 4fcsbg "Like a pro!"
                            extend 1fcssm " Ehehe."
                            n 1fllss "I'll just note those down real quick..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify

                        "No, that's not right.":
                            n 2fnmgs "What?{w=0.2} Are you kidding me!?"
                            n 2flrsl "Ugh..."
                            n 4nlrpu "And I was so proud of myself for figuring that out,{w=0.1} too..."
                            n 1nnmss "Well,{w=0.1} it looks like we're gonna have to do things the old-fashioned way."

                            jump talk_weather_setup_manual_coords

                else:
                    n 4fnmaj "Eh?{w=0.2} What the...?"
                    n 1nnmpu "Huh.{w=0.2} Weird."
                    n 1nlrss "Well,{w=0.1} I {i}was{/i} gonna show you something neat,{w=0.5}{nw}"
                    extend 3nslpo " but it looks like something messed up."
                    n 4nlrss "Hey,{w=0.1} [player]...{w=0.3}"
                    extend 1flrbg " could you look these coordinates up and tell me if I got it right?"
                    n 4tslbo "I'm {i}pretty{/i} sure your latitude is [ip_latitude_longitude[0]],{w=0.1} and your longitude is [ip_latitude_longitude[1]]."
                    n 1nllbo "..."
                    n 4tnmss "Well,{w=0.3} [player]?"
                    menu:
                        n "How're we looking?"

                        "Yes, that looks good to me.":
                            n 1kchbg "Phew!"
                            extend 2nsldv " I was kinda worried I'd have to get a little more creative..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify

                        "No, that's not right.":
                            n 4fcsan "Uuuuuuu..."
                            n 2nslpo "Fine.{w=1}{nw}"
                            extend 2usqpo " It looks like we're gonna have to do things the old-fashioned way."

                            jump talk_weather_setup_manual_coords

        "I want to tell you where I am myself.":
            n 1uchgn "Well, you're the boss!"

            jump talk_weather_setup_manual_coords

        "Nevermind.":
            n 2fllpo "Well...{w=1}{nw}"
            extend 4nslpo " fine."
            n 1fchbg "Just let me know when you wanna go through all this again,{w=0.1} 'kay?"

            jump ch30_loop

label talk_weather_setup_manual_coords:
    n 1ulraj "So,{w=0.3}{nw}"
    extend 1nnmbo " I'm going to need to know a few things to find out where you are."
    n 1flrss "Let's start off with the basics{w=0.1} -{w=0.5}{nw}"
    extend 4fchsm " Hemispheres!"
    n 1unmaj "Do you live in the {b}Northern{/b} or {b}Southern{/b} Hemisphere?"
    n 3nllss "Just in case you didn't know,{w=0.1} it basically just means if you live {b}North{/b} or {b}South{/b} of the {b}equator{/b}."
    n 1nllaj "So..."
    show natsuki 1tsqsm at jn_center
    menu:
        n "Which do you live in,{w=0.1} [player]?"

        "The Northern Hemisphere.":
            $ player_in_southern_hemisphere = False
            $ persistent.hemisphere_north_south = "North"

            n 1unmaj "The Northern Hemisphere?{w=1}{nw}"
            extend 1flrbg " Well hey!{w=1}{nw}"
            extend 4fchbg " Just like me!"

        "The Southern Hemisphere.":
            $ player_in_southern_hemisphere = True
            $ persistent.hemisphere_north_south = "South"

            n 1unmaj "The Southern Hemisphere?{w=1}{nw}"
            extend 4fchbg " Gotcha!"

    n 1uchbg "Okay,{w=0.1} now time for the other two!"
    n 1tnmss "Do you live in the {b}Eastern{/b} or {b}Western{/b} Hemisphere?"
    n 1ulraj "This one's a little more tricky,{w=0.1} but I find it helps to think of it this way:"
    n 4nnmbo "If we took a world map and cut it in half {b}vertically{/b} down the middle..."
    show natsuki 1unmaj at jn_center
    menu:
        n "Would you live in the {b}Eastern half{/b},{w=0.1} or the {b}Western half{/b}?"

        "The Eastern half.":
            $ player_in_western_hemisphere = False
            $ persistent._jn_hemisphere_east_west = "East"

            if not player_in_southern_hemisphere:
                n 1unmbg "Wow!{w=1}{nw}"
                extend 1fchbg " Just like me again,{w=0.1} [player]!"
                n 2tslss "It really is a small world,{w=0.1} huh?"

            else:
                n 1fchbg "Well hey!{w=0.5} Just like me!"

        "The Western half.":
            $ player_in_western_hemisphere = True
            $ persistent._jn_hemisphere_east_west = "West"

            n 1fchbg "The Western half.{w=0.5} Gotcha!"

    # Get the latitude
    n 4fllss "Now with that out of the way,{w=0.1} I just need your coordinates!"
    n 3fsqsm "And by those,{w=0.5}{nw}"
    extend 1fchsm " I mean your {b}latitude{/b} and {b}longitude{/b}!"
    n 1ullaj "I always used {a=[store.jn_globals.LINK_LAT_LONG_HOME]}this{/a} website to look mine up for homework,{w=0.1} but you can use your phone or whatever too."
    n 4unmaj "Oh,{w=0.3}{nw}"
    extend 1fnmbo " and don't worry about making it positive or negative.{w=1}{nw}"
    extend 3fcssm " I'll take care of that!"
    n 1ullss "We'll start off with your {b}latitude{/b} first."
    n 1fchsm "So...{w=0.3} take it away!"
    $ player_latitude = renpy.input(prompt="Enter your {b}latitude{/b}:", allow="0123456789.")

    # Get the longitude
    n 1fchbg "Alright!{w=0.5}{nw}"
    extend 1nchsm " Now finally,{w=0.1} I just need your {b}longitude{/b}!"
    n 3fcssm "Just like last time,{w=0.1} I can figure it out without any positive or negative symbols."
    n 1fchsm "Take it away,{w=0.1} [player]!"
    $ player_longitude = renpy.input("Enter your {b}longitude{/b}:", allow="0123456789.")

    # Final checks and prompt
    python:
        if player_in_southern_hemisphere:
            player_latitude = "-" + player_latitude

        if player_in_western_hemisphere:
            player_longitude = "-" + player_longitude

        player_latitude = float(player_latitude)
        player_longitude = float(player_longitude)

    n 3fcssm "'Kay!"
    extend 1fchsm " I think we're nearly there now,{w=0.1} [player]!"
    extend 1fcsbg " Let me just open up a map real quick...{w=1}{nw}"

    python:
        # Try to show the map, and come back with the result to drive dialogue
        show_map_success = False
        try:
            jn_open_google_maps(player_latitude, player_longitude)
            show_map_success = True

        except Exception as exception:
            store.jn_utils.log(exception.message, store.jn_utils.SEVERITY_ERR)

    if show_map_success:
        n 1uchgn "Ta-da!"
        n 4fnmbg "How about it,{w=0.1} [player]?{w=1}{nw}"

        menu:
            n "Close enough,{w=0.1} right?"

            "Yes, that's close enough.":
                n 1fchbg "Finally!{w=1}{nw}"
                extend 4nchsm " I'll just note all that down real quick..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify

            "No, that's not right at all.":
                n 1tnmem "What?{w=0.2} Really?!"
                n 3fcsem "Ugh..."
                n 4fcsaj "Let's...{w=0.5} try again,{w=0.1} alright?{w=1}{nw}"
                extend 2fnmpo " I really wanna get this working!"

                jump talk_weather_setup_manual_coords

    else:
        n 1fllaj "Urgh...{w=0.3} really?{w=0.2} This is {i}such{/i} a pain!"
        n 1nlrsl "I can't seem to show you where I think you are on a map,{w=0.1} so I'll just ask to make sure."
        n 1nnmss "I've done some checks to work out the coordinates,{w=0.1} and from what you said..."
        n 4nnmaj "Your overall latitude would be [player_latitude],{w=0.1} and your overall longitude would be [player_longitude]."
        menu:
            n "Is [player_latitude], [player_longitude] correct?"

            "Yes, that's right.":
                n 3fcsem "Finally!{w=1}{nw}"
                extend 3kslpo " Jeez..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify

            "No, that's still not right.":
                n 3tnmem "What?{w=0.2} Really?!"
                n 3fcsem "Ugh..."
                n 1fcsaj "Let's...{0.5} try again,{w=0.1} alright?{w=1}{nw}"
                extend 4fnmpo " I really wanna get this working!"

                jump talk_weather_setup_manual_coords

            "Nevermind.":
                n 3fllpo "Jeez...{w=1}{nw}"
                extend 1tlrss " what a mess,{w=0.1} huh?"
                n 1fcspo "..."
                n 1nllaj "Well,{w=0.1} thanks anyway.{w=1}{nw}"
                extend 1nnmaj " We can always try again later,{w=0.5}{nw}"
                extend 4tnmss " right?"

                jump ch30_loop

label talk_weather_setup_verify:
    n 1nchbg "Okaaay!{w=1}{nw}"
    extend 4fnmsm " I think we're almost done now,{w=0.1} [player]!"
    n 1ncsbo "Let me just check everything is in order here...{w=1.5}{nw}"

    if jn_atmosphere.getWeatherFromApi():
        n 1fchbg "Yes!"
        extend 1uchbs " It's working,{w=0.5} it's working!{w=1}{nw}"
        extend 4nchsml " Ehehe."
        n 1nchbgl "Thanks a bunch,{w=0.1} [player]!{w=1}{nw}"
        extend 3uchgnledz " This is gonna be {i}super{/i} awesome!"
        $ Natsuki.calculatedAffinityGain()

        python:
            persistent._jn_weather_api_configured = True
            persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.real_time)
            jn_atmosphere.updateSky()

    else:
        n 1fcsaj "Oh,{w=0.5}{nw}"
        extend 2fllan " come {i}on!{/i}"
        n 1fcsem "Ugh..."
        n 3fslem "And I was so stoked about it,{w=0.1} too..."
        n 1fcsem "I'm sorry,{w=0.1} [player].{w=1}{nw}"
        extend 4knmemsbl " I can't get it all to work!"
        n 2fsrem "Talk about a disappointment..."
        n 2nsrposbl "..."
        n 1unmgsesu "Ah!{w=0.5}{nw}"
        extend 1fnmgs " I just thought of something!"
        n 4tnmpueqm "Did you have to make a new account for OpenWeatherMap,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4tslbo " Or like,{w=0.2} did you make a new API key?"
        n 1tnmss "I...{w=1}{nw}"
        extend 4fsrdvsbr " kinda spaced out a little when you told me before.{w=0.75}{nw}"
        extend 1nlrajsbr " So..."
        show natsuki 2tnmslsbr at jn_center

        menu:
            n "Do you remember?{w=0.3} Like,{w=0.2} at all?"

            "I created a new account.":
                $ new_account_or_key = True

            "I created a new API key.":
                $ new_account_or_key = True

            "I already had an account, and used an existing API key.":
                $ new_account_or_key = False
                n 2tslpusbr "...Huh."
                n 1tslsr "I'm...{w=0.75}{nw}"
                extend 1kcsemesisbl " kinda stumped then,{w=0.2} actually."
                n 3tsrsl "I mean..."
                n 4tnmpueqm "Maybe you just gave me the wrong key...?"
                extend 1fchbgsbl " Or your internet just isn't feeling it today?"
                n 1nslsssbl "I don't know."
                n 1fllsssbl "Just...{w=0.5}{nw}"
                extend 4knmsssbr " let me know when if you wanna try again,{w=0.2} 'kay?"
                n 1knmcaesssbr "It'll be awesome!{w=0.5}{nw}"
                extend 2knmpolesssbr " I-{w=0.3}I promise!"

        if new_account_or_key:
            n 1tslbo "So you did,{w=0.2} huh..."
            n 4fslpuesp "..."
            n 1unmgsesu "Oh!{w=0.5}{nw}"
            extend 1fsrdvsbl " Right!"
            n 2fsrsssbl "I forgot to say..."
            n 2fsldvsbr "It might take a day or so for your API key to actually {i}activate{/i} so I can use it..."
            n 1kchsssbr "Ehehe.{w=0.5}{nw}"
            extend 1fchblsbl " Oops!"
            n 1fllsssbl "Just...{w=0.5}{nw}"
            extend 4knmsssbr " let me know when you wanna try again,{w=0.2} 'kay?"
            n 4fnmcasbr "I really wanna get this all working!"
            n 1fcstr "Because when I do,{w=0.2} you bet it's gonna be{w=0.3}{nw}"
            extend 4fspgsledz " {i}awesome{/i}!"

    jump ch30_loop

# Natsuki discusses her favourite season with the player, and asks the player theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_season",
            unlocked=True,
            prompt="What's your favorite season?",
            category=["Weather", "Nature"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
label talk_favourite_season:
    n 1unmbo "Huh?{w=0.2} My favorite season?"

    # Player hasn't given their favourite season before
    if not persistent.jn_player_favourite_season:
        n 4tllss "That's a little random,{w=0.1} isn't it?"
        n 1tnmss "Well...{w=0.3} anyway.{w=0.3}{nw}"
        extend 4fnmaw " Tough question, [player]!"
        n 3fsrsl "I think if I had to pick..."
        n 1fchts "It'd be summer!{w=0.2} Duh!"
        n 3fsqss "Why?{w=0.5}{nw}"
        extend 1fchgn " Just think about it,{w=0.1} [player]!"
        n 4ullbg "Long trips to the beach...{w=0.5}{nw}"
        extend 4ncssm " ice cream in the shade...{w=0.5}{nw}"
        extend 4ksrss " lazy evening walks to the shops..."
        n 1flleml "I-{w=0.1}I mean,{w=0.3}{nw}"
        extend 1fllbgl " what's not to love?"
        n 1fchbg "I can just enjoy life out there without having to worry about the weather!"
        n 1usqsg "I don't think I need to make my case any more clear,{w=0.1} do I?{w=0.5}{nw}"
        extend 4uchsm " Ahaha."
        n 1unmaj "Although...{w=0.3} what about you,{w=0.1} [player]?"
        menu:
            n "What's your favorite season?"

            "Spring":
                n 1fnmss "Oh?{w=0.2} Spring,{w=0.1} huh?"
                n 3tllsr "Hmmm..."
                n 1unmss "I mean,{w=0.1} I kinda get it.{w=0.2} It's the sign winter finally got lost,{w=0.1} right?"
                n 1ulrss "And I suppose the flowers blooming again is kinda cool to see."
                n 3fsqan "But the rain!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1fcspu " It just never stops!"
                n 3fllpo "Roll on summer,{w=0.1} I say."

                $ persistent.jn_player_favourite_season = "Spring"

            "Summer":
                n 1fsgbg "Aha!{w=0.2} I knew it!"
                n 4fsqbg "Nobody can resist some fun in the sun,{w=0.1} am I right?"
                n 1fnmbg "I'm glad we both agree,{w=0.1} [player].{w=0.5}{nw}"
                extend 3fchsm " Ehehe."

                $ persistent.jn_player_favourite_season = "Summer"

            "Autumn":
                n 1unmaj "Autumn?{w=0.5}{nw}"
                extend 4nllaj " Not a bad choice,{w=0.1} actually!"
                n 1ullsm "I like when it's still warm enough in the day to go out and do things..."
                n 4ucsss "But you also get that crisp,{w=0.1} fresh morning air to wake you up."
                n 1ullaj "The falling leaves are super pretty too."
                n 2fcsan "It's just...{w=0.5}{nw}"
                extend 4fsrsr " it's all ruined when the rain comes,{w=0.1} you know?"
                n 2fsqsr "Trudging through all those sloppy leaves is just gross.{w=0.5}{nw}"
                extend 1fcssf " No thanks!"

                $ persistent.jn_player_favourite_season = "Autumn"

            "Winter":
                n 1tnmsf "Huh?{w=0.2} Really?"
                n 1tnmaj "Winter is the last thing I expected you to say,{w=0.1} [player]!"
                n 4tlrbo "Though...{w=0.3} I get it, kinda."
                n 1fcsbg "It's the perfect time of year to get super snug and spend some quality reading time!"
                n 2fslss "Especially since there's not much you can do outside,{w=0.1} anyway."

                $ persistent.jn_player_favourite_season = "Winter"

    # Player has already shared their favourite season
    else:
        n 1tllbo "Hang on...{w=0.5}{nw}"
        extend 4tnmss " didn't we talk about this before,{w=0.1} [player]?"
        n 1nlrpu "Well,{w=0.1} anyway..."
        n 1ucsbg "I still love summer,{w=0.1} as you know{w=0.1} -{w=0.3}{nw}"
        extend 3fcsbg " and nothing's gonna change that any time soon!"
        n 4tsqsg "What about you,{w=0.1} [player]?"
        menu:
            n "Still rooting for [persistent.jn_player_favourite_season]?"
            "Yes.":
                n 1fcsbg "Ehehe.{w=0.2} I thought as much,{w=0.1} [player]."

                if persistent.jn_player_favourite_season == "Summer":
                    n 1uchbg "You already picked the best season,{w=0.1} after all!"

                else:
                    n 4fllss "Well...{w=0.3} I'm afraid you're not gonna sway me!{w=0.5}{nw}"
                    extend 1uchbg " Ahaha!"

            "No.":
                n 3tsgbg "Oh?{w=0.2} Changed our mind,{w=0.1} have we?"
                n 3tsqss "Well?{w=0.5}{nw}"
                extend 1fchbg " Tell me then,{w=0.1} [player]!"
                menu:
                    n "What's your favorite season?"

                    "Spring":
                        $ new_favourite_season = "Spring"

                    "Summer":
                        $ new_favourite_season = "Summer"

                    "Autumn":
                        $ new_favourite_season = "Autumn"

                    "Winter":
                        $ new_favourite_season = "Winter"

                $ season_preference_changed = False
                if persistent.jn_player_favourite_season == new_favourite_season:
                    n 1fnmgs "Hey!{w=0.2} [player]!"
                    n 3fsqpo "I thought you said you'd changed your mind?"
                    n 3fllem "You haven't changed your mind at all!{w=0.2} You said [persistent.jn_player_favourite_season] last time,{w=0.1} too!"
                    $ chosen_tease = jn_utils.getRandomTease()
                    n 1fcsem "Jeez...{w=0.5}{nw}"
                    extend 2fnmpo " you're such a wind-up sometimes,{w=0.1} [chosen_tease]!"

                    if Natsuki.isAffectionate(higher=True):
                        n 2flrpol "N-{w=0.1}not that I {i}dislike{/i} that side of you,{w=0.1} o-{w=0.1}or anything."

                    else:
                        n 1fsqsm "But...{w=0.3} I think I can {i}weather{/i} it."
                        n 4fsrss "For now."

                else:
                    $ persistent.jn_player_favourite_season = new_favourite_season
                    $ season_preference_changed = True

                if season_preference_changed and persistent.jn_player_favourite_season == "Spring":
                    n 1usqss "Ooh?{w=0.2} Favoring Spring now,{w=0.1} [player]?"
                    n 1nlrbo "I could do without all the rain,{w=0.1} but I get it."
                    n 3flrpu "Hmm...{w=0.3} Spring..."
                    n 1tlrbo "I wonder...{w=0.5}{nw}"
                    extend 4tnmss " do you grow anything,{w=0.1} [player]?"
                    n 1fchsm "Ahaha."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Summer":
                    n 1fchbs "Aha!{w=0.2} See?"
                    n 4fsqbs "You knew I was right all along,{w=0.1} didn't you?"
                    n 3usqsg "Don't even try to deny it,{w=0.1} [player].{w=0.5}{nw}"
                    extend 1fchbg " Summer is the best!"
                    n 1uchsm "I'm just glad you came around.{w=0.2} That's the important thing!"

                elif season_preference_changed and persistent.jn_player_favourite_season == "Autumn":
                    n 4usqsm "Oh?{w=0.2} You've taken the {i}fall{/i} for Autumn,{w=0.1} have you?"
                    n 1fchsm "Ehehe."
                    n 1ullss "I'll admit,{w=0.1} it's a pretty season,{w=0.1} with all the golden leaves and stuff..."
                    n 2nslss "So long as the weather stays warm,{w=0.1} anyway."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Winter":
                    n 1tllss "Winter,{w=0.1} huh?{w=0.2} I wasn't expecting that."
                    n 3tnmbo "Do you prefer being indoors now or something,{w=0.1} [player]?"
                    n 4flrss "Well,{w=0.1} if you prefer being all cosy inside..."
                    n 1fsqsm "Then you better not be slacking on your reading,{w=0.1} [player]!{w=0.5}{nw}"
                    extend 1fchsm " Ehehe."

    # Unlock the seasonal off-shoulder sweaters, if all not already unlocked and custom outfits unlocked.
    # Some special dialogue based off the chosen season.

    python:
        spring_sweater = jn_outfits.getWearable("jn_clothes_bee_off_shoulder_sweater")
        summer_sweater = jn_outfits.getWearable("jn_clothes_creamsicle_off_shoulder_sweater")
        autumn_sweater = jn_outfits.getWearable("jn_clothes_autumn_off_shoulder_sweater")
        winter_sweater = jn_outfits.getWearable("jn_clothes_nightbloom_off_shoulder_sweater")

    if (
        (
            not spring_sweater.unlocked
            or not summer_sweater.unlocked
            or not autumn_sweater.unlocked
            or not winter_sweater.unlocked
        )
        and Natsuki.isHappy(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):
        n 1flrpu "..."
        n 1ulraj "Actually,{w=0.3}{nw}"
        extend 3fnmss " you know what?"
        n 1fcsss "Give me a sec here.{w=0.75}{nw}"
        extend 3uchgnl " I've got {i}just{/i} the thing!{w=1}{nw}"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio zipper
        $ jnPause(2)

        python:
            import copy

            spring_sweater.unlock()
            summer_sweater.unlock()
            autumn_sweater.unlock()
            winter_sweater.unlock()
            temporary_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))

            if persistent.jn_player_favourite_season == "Spring":
                temporary_outfit.clothes = spring_sweater

            elif persistent.jn_player_favourite_season == "Summer":
                temporary_outfit.clothes = summer_sweater

            elif persistent.jn_player_favourite_season == "Autumn":
                temporary_outfit.clothes = autumn_sweater

            else:
                temporary_outfit.clothes = winter_sweater

            jn_outfits.saveTemporaryOutfit(temporary_outfit)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio zipper
        $ jnPause(1)
        show natsuki 1fsqsm at jn_center
        hide black with Dissolve(1.25)

        n 1fsqsm "..."
        n 1tsqssl "...Well,{w=0.2} [player]?{w=1}{nw}"
        extend 1tcsssl " You gotta admit..."
        n 3fsqss "Whatever your preference?"
        n 4fcsbgedz "My fashion is {i}always{/i} in-season."
        n 1fchsml "Ehehe."

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
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n 1ullaj "Hey,{w=0.1} [player]..."
    n 1unmaj "Do you have off days sometimes?{w=0.2} Where you struggle to get anything done?"
    n 3flrpo "Or you just get distracted super easily?"
    n 4unmbo "To be honest?{nw}"
    extend 3fllss "{w=0.2} I struggled with that for a while.{nw}"
    extend 3fbkwr "{w=0.2} Especially when things like assignments are so boring!"
    n 1nllaj "But...{w=0.5}{nw}"
    extend 1fllbg " I figured out a way of managing that{w=0.1} -{w=0.1} and you should know it too,{w=0.1} [player]!"
    n 1fchbg "Time boxing!"
    n 3nsqpo "And no,{w=0.1} it's not as literal as it sounds."
    n 1nnmaj "The idea is that you set aside a period during the day you want to work{w=0.1} -{w=0.1} like the school day,{w=0.1} or a few hours in the evening."
    n 4fnmbg "Then for each hour in that period,{w=0.1} you split it!"
    n 1ulraj "So for any given hour,{w=0.1} you spend most of that working,{w=0.1} and the remainder on some kind of break."
    n 1unmss "The idea is that it becomes way easier to stay focused and motivated since you always have a breather coming up."
    n 1uchsm "Personally,{w=0.1} I find a 50/10 split works best for me."
    n 2nllbo "So I spend 50 minutes of each hour studying,{w=0.3}{nw}"
    extend 1uchsm " and 10 minutes doing whatever I want."
    n 4usqbg "You'd be surprised how much manga time I can sneak in!"
    n 1unmaj "Don't just take my schedule as a rule though.{w=0.5}{nw}"
    extend 1fchbg " Find a balance that works for you, [player]!"
    n 3fslbg "Though I should remind you...{w=0.3} the key word here is {i}balance{/i}."
    n 1fsqsr "I'm not gonna be impressed if you work too much...{w=0.5}{nw}"
    extend 4fnmpo " Or just slack off!"
    if Natsuki.isAffectionate(higher=True):
        n 1ullbo "Although...{w=0.3} now that I think about it..."
        n 3tsqsm "Perhaps I should timebox our time together,{w=0.1} [player]."
        extend 1uchbselg " Ahaha!"

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
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sweet_tooth:
    n 4unmbo "Huh?{w=0.2} Do I have a sweet tooth?"

    # Opening response
    if Natsuki.isAffectionate(higher=True):
        n 3fspbg "You bet I do!"
        n 4nsqts "What else were you expecting,{w=0.1} [player]?"
        extend 1fchsm "{w=0.2} Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 3fllss "Well,{w=0.1} yeah.{w=0.2} Of course I do!"

    else:
        n 1nnmsl "Well...{w=0.3} yeah.{w=0.2} Why wouldn't I?"

    n 1nllaj "Baked stuff is okay,{w=0.1} but I find it gets kinda sickly before long."
    n 1ullaj "But to be completely honest,{w=0.1} if I had a choice?{w=0.5}{nw}"
    extend 2unmbo " Just give me a bunch of candy every time."

    if Natsuki.isNormal(higher=True):
        n 1uwdaj "There's so much more variety!{w=0.2} Like...{w=0.3} there's always something for whatever I feel like!"
        n 2tllss "I think if I had to pick a favorite though,{w=0.3}{nw}"
        extend 1fllss " it'd be those fizzy ones."
        n 1fchbg "Just that perfect mix of sweet and sour,{w=0.1} you know?"
        n 3flraj "Jeez...{w=0.5}{nw}"
        extend 1fchts " I can feel my tongue tingling already just thinking about them!"
        n 1fsrts "..."
        n 3flleml "A-{w=0.1}anyway!"
        n 1fcseml "It isn't like I'm snacking on treats all the time though."
        n 2fllpo "I've got way better things to spend my money on."
        n 1fnmss "And...{w=0.3} it's not exactly healthy either.{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    # Closing thoughts
    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Though I have to say,{w=0.1} [player]."
        n 1fsqssl "I'm pretty sure you have a sweet tooth too."
        n 2fsrbgl "It'd explain why you're spending so much time with me,{w=0.1} a-{w=0.1}after all."
        n 1fchbgl "Ahaha!"

    elif Natsuki.isNormal(higher=True):
        n 1fllbg "I could go for some candy right now,{w=0.1} actually.{w=0.5}{nw}"
        extend 1fslss " But...{w=0.3} I think I'll hold back."
        n 4usqbg "Someone's gotta be a role model to you,{w=0.1} [player].{w=0.2} Am I right?"
        n 1fchsm "Ehehe."

    else:
        n 1nnmbo "..."
        n 1nlrbo "That being said..."
        n 2flrsr "I...{w=0.3} could really use some chocolate right now."
        n 2fsqsr "I'll let {i}you{/i} figure out why,{w=0.1} [player]."

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
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:
    # Player was asked before, and declined to share their appearance
    if persistent.jn_player_appearance_declined_share:
        n 4unmaj "Huh?{w=0.2} Your appearance?"
        n 1ullaj "If I remember,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
        extend 2tnmbo " you said didn't want to share it with me before."
        n 1tlrbo "Huh. Well..."
        menu:
            n "Did you change your mind,{w=0.1} [player]?"

            "Yes, I want to share my appearance.":
                n 3fcsbg "A-{w=0.1}aha!{w=0.2} I knew you'd come around eventually,{w=0.1} [player].{nw}"
                extend 3fchgn "{w=0.2} Let's not waste any time!"

            "No, I still don't want to share my appearance.":
                n 1nllsl "Oh..."
                n 4unmaj "Well,{w=0.1} it's your call,{w=0.1} [player]."
                n 1unmss "Just let me know if you change your mind again,{w=0.1} alright?"
                return

    # Player has already described themselves to Natsuki
    elif persistent.jn_player_appearance_eye_colour is not None:
        n 1unmaj "Huh?{w=0.2} Your appearance?"
        n 2tllbo "But...{w=0.3} I was sure you already shared that with me,{w=0.1} [player]."
        n 4uspgs "Ooh!{w=0.5}{nw}"
        extend 1unmbg " Did you dye your hair or something?"
        n 2fllbg "Or...{w=0.3} maybe you just made a mistake last time?"
        n 2tslbg "Well...{w=0.5}{nw}"
        extend 1unmbg " either way."
        menu:
            n "Did you want to share your appearance again,{w=0.1} [player]?"

            "Yes, my appearance has changed.":
                n 1fcssm "Aha!{w=0.2} I thought so!"
                n 2fchgn "I can't wait to find out how!"

            "No, my appearance hasn't changed.":
                n 1tnmsr "H-{w=0.1}huh?{w=0.2} Just pulling my leg,{w=0.1} are you?"
                n 2tsrsf "Okaaay..."
                n 1tnmss "Just let me know if you actually {i}do{/i} change something then,{w=0.2} 'kay?"
                return

    # Player has never described themselves to Natsuki, and this is their first time discussing it
    else:
        n 1tlrbo "Huh..."
        n 1tnmbo "You know,{w=0.1} [player].{w=0.2} I just realized something."
        n 4unmaj "You've seen a lot of me,{w=0.1} right?{w=0.5}{nw}"
        extend 2fslssl " B-{w=0.1}by spending time with me here,{w=0.1} I mean."
        n 1ullaj "So...{w=0.3} you kinda know exactly who you're dealing with."
        n 4uwdgs "But I don't have a clue about who {i}I'm{/i} dealing with!"
        n 3fsqsm "And honestly?{w=0.2} You should know me by now.{w=0.5}{nw}"
        extend 3fsqbg " I'm actually pretty curious!"
        n 1nchbg "Don't worry though{w=0.1} -{w=0.1} anything you tell me is staying strictly between us,{w=0.1} obviously!"
        n 1fllsfl "N-{w=0.1}not like anyone else would care {i}that{/i} much,{w=0.1} anyway."
        n 4unmsm "So...{w=0.3} how about it, [player]?"
        menu:
            n "Do you wanna share your appearance with me, [player]?"

            "Sure!":
                n 1uchbsl "Yes!{w=0.5}{nw}"
                extend 2fcsbgl " I-{w=0.1}I mean good!{w=0.5}{nw}"
                n 1fchbg "Let's get started then,{w=0.1} shall we?"

            "I'm not comfortable sharing that.":
                n 1unmsl "Oh..."
                n 1ullaj "That's kind of disappointing to hear,{w=0.1} if I'm being honest."
                n 2nchss "But I totally get it,{w=0.1} [player].{w=0.2} So don't worry,{w=0.1} 'kay?"
                n 2fsqss "You better let me know if you feel like telling me later though!"
                $ persistent.jn_player_appearance_declined_share = True
                return

    n 1uchgn "Okaaay!{w=0.2} Let's start with...{w=0.5}{nw}"
    extend 1fchbg " your eyes!"
    n 4unmbg "They say the eyes are the window to the soul,{w=0.1} so it only makes sense to begin there,{w=0.1} right?"
    n 4flldvl "..."
    n 1fcseml "A-{w=0.1}anyway...!"

    # Eye colour
    menu:
        n "How would you describe your eye color,{w=0.1} [player]?"

        "Amber":
            n 4unmaj "Ooh!{w=0.2} I don't think I've seen someone with amber eyes before."
            n 1fchbg "That's awesome,{w=0.1} [player]!{w=0.2} I bet those help you stand out,{w=0.1} right?"
            $ persistent.jn_player_appearance_eye_colour = "Amber"

        "Blue":
            n 4unmbg "Blue eyes,{w=0.1} huh?{w=0.2} Cool!"
            n 1fsgsm "I really like how striking they are!"
            $ persistent.jn_player_appearance_eye_colour = "Blue"

        "Brown":
            n 4unmaj "Brown eyes,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fchsm " I'm not complaining!"
            n 3tsqss "Nice and natural,{w=0.1} am I right?{w=0.5}{nw}"
            extend 1uchsm " Ahaha."
            $ persistent.jn_player_appearance_eye_colour = "Brown"

        "Grey":
            n 4unmaj "Oh?{w=0.2} Grey eyes?{w=0.2} Super neat, [player]!"
            n 1tllss "I don't think I've seen anyone with grey eyes before!"
            $ persistent.jn_player_appearance_eye_colour = "Grey"

        "Green":
            n 4fsgbg "Aha!{w=0.2} I had you figured for green eyes,{w=0.1} [player]."
            n 1fsqbg "I bet you're proud of them,{w=0.1} no?{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Green"

        "Hazel":
            n 4unmaj "Ooh!{w=0.2} Hazel,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fsqbg " Classy!"
            n 1tslsm "Hmm...{w=0.3} I wonder if yours are closer to green or brown,{w=0.1} [player]?"
            $ persistent.jn_player_appearance_eye_colour = "Hazel"

        "Mixed":
            n 4unmaj "Wow!{w=0.2} Do you have two different colors or something,{w=0.1} [player]?"
            n 1fchbg "Now if that isn't unique,{w=0.1} I don't know what is!"
            $ persistent.jn_player_appearance_eye_colour = "Mixed"

        "Other":
            n 4unmaj "Oh?{w=0.2} Something a bit off the beaten trail,{w=0.1} huh?"
            n 1tlrss "...Or maybe you just wear contacts a lot?{w=0.5}{nw}"
            extend 1unmsg " Well,{w=0.1} whatever."
            n 1ncsss "I'm sure they look fine either way."
            $ persistent.jn_player_appearance_eye_colour = "Other"

    n 1uchbg "Alright!{w=0.2} That's one down!"
    n 3ullaj "So next,{w=0.1} we have...{w=0.5}{nw}"
    extend 1fchsm " your hair,{w=0.1} of course!"
    n 1nnmsm "We'll just start off with the length for now."
    n 4ullss "Now..."

    # Hair length
    menu:
        n "How would you describe your hair length,{w=0.1} [player]?"

        "Short.":
            n 4ncsss "Ah,{w=0.1} the low maintenance approach{w=0.1} -{w=0.1} I see,{w=0.1} I see.{w=0.5}{nw}"
            extend 1fchbg " Trendy!"
            n 1unmaj "To be honest though,{w=0.1} I totally get it."
            n 3fslpo "I have no idea how you even keep long hair looking good..."
            n 3nslpo "It just seems like way too much effort to me."
            $ persistent.jn_player_appearance_hair_length = "Short"

        "Mid-length.":
            n 4fcsbg "Aha!{w=0.2} The perfect balance,{w=0.1} am I right?"
            n 1fllss "Just long enough for pretty much any style..."
            n 1fchgn "And yet still short enough to suit a lazy day!{w=0.5}{nw}"
            extend 1nchsm " Ehehe."
            n 3flrbgl "I'm glad we think the same way,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "Mid-length"

        "Long.":
            n 4unmbg "Ooh!{w=0.2} Letting it run free,{w=0.1} are we?"
            n 1fcssm "I bet you take super good care of yours."
            n 3fsqsm "I might even have to borrow your products,{w=0.1} [player].{w=0.5}{nw}"
            extend 1nchsm " Ehehe!"
            $ persistent.jn_player_appearance_hair_length = "Long"

        "I don't have any hair.":
            n 4fnmaj "Hey{w=0.1} -{w=0.1} nothing wrong with that!{nw}"
            extend 1fsqbg "{w=0.2} You wanna know why?"
            n 3fchgn "Because it just means you're aerodynamic,{w=0.1} [player].{w=0.5}{nw}"
            extend 3uchsmelg " Ahaha!"
            $ persistent.jn_player_appearance_hair_length = "None"

    n 1uchbs "Okay!{w=0.5}{nw}"
    extend 1unmbg " I'm really starting to get a picture now."
    n 4fwdgs "We gotta keep the ball rolling,{w=0.1} [player]!"

    # Hair colour
    if persistent.jn_player_appearance_hair_length == "None":
        n 1fllss "You said you didn't have any hair,{w=0.1} right?{w=0.5}{nw}"
        extend 4fllbg " So I think it's kinda pointless talking about hair color."
        n 3fslbo "Now,{w=0.1} let's see...{w=0.3} what else..."

    else:
        n 1fchsm "Now for your hair color!"
        n 4unmbg "So,{w=0.1} [player]..."
        menu:
            n "How would you describe your hair color?"

            "Auburn":
                n 4unmaw "Ooh!{w=0.2} Auburn,{w=0.1} huh?{w=0.5}{nw}"
                extend 1fwdaw " That's awesome,{w=0.1} [player]!"
                n 1fchbg "It's such a warm color!"
                $ persistent.jn_player_appearance_hair_colour = "Auburn"

            "Black":
                n 4tsgsm "Black,{w=0.1} huh?{w=0.5}{nw}"
                extend 1nchgn " Nice!"
                n 1usqsg "I bet you feel super slick,{w=0.1} huh [player]?"
                $ persistent.jn_player_appearance_hair_colour = "Black"

            "Blond":
                n 4fnmbg "Aha!{w=0.2} A blond,{w=0.1} are we?{w=0.5}{nw}"
                extend 3fsqts " {w=0.3}...That explains a lot."
                n 1fchgnelg "Ahaha!"
                n 1uchbs "I'm kidding,{w=0.1} [player]!{w=0.2} I'm just kidding!"
                n 3fllbg "I'm actually a little jealous.{w=0.5}{nw}"
                extend 4fsqsm " Just a little."
                $ persistent.jn_player_appearance_hair_colour = "Blond"

            "Brown":
                n 4unmaj "Brown hair,{w=0.1} [player]?{w=0.5}{nw}"
                extend 1nchsm " I'm for it!"
                n 4nsgss "Not too subtle and not too striking,{w=0.1} you know?{w=0.2} It's just right!"
                $ persistent.jn_player_appearance_hair_colour = "Brown"

            "Grey":
                n 4unmaj "Ooh...{w=0.5}{nw}"
                extend 1ullaj " I gotta say...{w=0.5}{nw}"
                extend 1kllbg " I wasn't expecting that!"
                n 2fsqsr "I just hope that isn't from stress,{w=0.1} [player]..."
                n 2fllbg "...Or at least stress from me,{w=0.1} anyway.{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                $ persistent.jn_player_appearance_hair_colour = "Grey"

            "Red":
                n 4fchsm "Ehehe.{w=0.5}{nw}"
                extend 1usqsm " So you're a red head,{w=0.1} [player]?"
                n 3flrajl "Not that there's anything wrong with that,{w=0.1} o-{w=0.1}obviously!"
                n 1fchbg "I bet that gets you some attention,{w=0.1} huh?"
                n 3fsrpo "Better be the good kind,{w=0.1} though."
                $ persistent.jn_player_appearance_hair_colour = "Red"

            "White":
                n 4unmbg "White hair,{w=0.1} huh?{w=0.5}{nw}"
                extend 1uchsm " Neat!"
                $ persistent.jn_player_appearance_hair_colour = "White"

            "Other":
                n 4unmaj "Oh?{w=0.5}{nw}"
                extend 1fsqsm " It looks like we're more similar in taste than I thought!"
                n 4fsrss "Though I should probably clarify...{w=0.5}{nw}"
                extend 1uchgn " mine is all natural,{w=0.1} [player]!{w=0.2} Ahaha."
                $ persistent.jn_player_appearance_hair_colour = "Other"

    # Height
    n 1unmbg "Alright!{w=0.2} I think I'm almost done interrogating you now,{w=0.1} [player]."
    n 4fsqsm "Ehehe."
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
                n 4unmgs "H-{w=0.1}huh?{w=0.2} Really?"
                n 1unmaj "You're even shorter than me?"
                n 3flldv "Well,{w=0.1} I wasn't expecting that!"
                n 1fnmbg "Don't worry,{w=0.1} [player].{w=0.2} We're both on the same side,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ehehe."

            elif player_input == 149:
                n 4unmgs "Seriously?{w=0.2} We're the same height?"
                n 1uchbg "That's amazing,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length = "Medium" and persistent.jn_player_appearance_hair_colour = "Other":
                    n 2fllbg "With the hair and everything too..."
                    n 1uchgn "It's like we're practically twins!"

            elif player_input > 149 and player_input < 166:
                n 4unmaj "Oh?{w=0.2} A little on the shorter side,{w=0.1} [player]?"
                n 1fcsss "Don't worry, don't worry!{w=0.5}{nw}"
                extend 2fllpo " I-{w=0.1}I'm not one to judge,{w=0.1} after all."

            elif player_input >= 166 and player_input < 200:
                n 4unmaj "About average height,{w=0.1} [player]?"
                n 1nchsm "No complaints from me!"

            elif player_input >= 200 and player_input < 250:
                n 4unmaj "Oh?{w=0.2} On the taller side [player],{w=0.1} are we?"
                n 1fllbg "I guess I know who to take shopping,{w=0.1} right?{w=0.5}{nw}"
                extend 1nchsm " Ehehe."

            else:
                n 4unmgs "W-{w=0.1}woah!{w=0.2} What the heck,{w=0.1} [player]?{w=0.2} Really?"
                n 1fbkwr "That's crazy tall!"
                n 3tlrem "Though...{w=0.3} actually...{w=0.5}{nw}"
                extend 3knmpo " I hope that isn't actually just inconvenient for you,{w=0.1} though."

        else:
            n 3fllpo "[player]...{w=0.3} please.{w=0.2} Take this seriously,{w=0.1} alright?"

    n 1uchsm "Okaaay!{w=0.2} I think that's everything."
    n 1unmbg "Thanks a bunch,{w=0.1} [player]!"
    n 4fllbg "I know it wasn't a lot,{w=0.3}{nw}"
    extend 1uchgn " but I feel like I know you so much better now!"

    if Natsuki.isLove(higher=True):
        n 4flldvl "You know,{w=0.1} [player]?{w=0.2} I can just picture it now."
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
        if persistent.jn_player_appearance_hair_length != "None":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n 4fsqsml "Spotting your [hair_length_descriptor] [hair_colour_descriptor] hair in the distance and hunting you down..."

        else:
            n 4fsqsml "Spotting you in the distance and hunting you down..."

        # Comment on height and eye colour
        if persistent.jn_player_appearance_height_cm < 149:
            n 2fllssl "Gazing down into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n 2fllssl "Gazing directly into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n 2fllssl "Gazing upwards into your [eye_colour_descriptor] eyes..."

        n 1fchunl "Uuuuuu..."
        n 1fsqunl "...{w=0.5}{nw}"
        extend 2fllajl " A-ahem!{w=0.2} Anyway..."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllsml "Really.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
        n 1kcsbgl "This seriously meant a lot to me."

    elif Natsuki.isEnamored():
        n 4fsldvl "...And now I know exactly who I should be watching out for."
        n 4fsqssl "So you better watch out,{w=0.1} [player]."
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
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_drinking_alcohol:
    n 1tnmss "Do I drink alcohol?"
    extend 1tllss " Well...{w=0.3} I can't say I've ever tried it."
    n 2nllsr "I just don't think it's something for me."
    n 1ullpu "That being said,{w=0.1} I knew people who {i}did{/i} drink it..."
    n 1kcspu "But...{w=0.3} I'd...{w=0.3} really rather not get into that,{w=0.1} [player]."
    n 1ncssr "Sorry."
    n 2tlrpu "..."
    n 4uwdajesu "Oh!{w=0.5}{nw}"
    extend 4fllss " That reminds me,{w=0.1} actually!"
    n 1fnmbg "I bet you didn't know,{w=0.1} but guess who just randomly brought some into the club one day?"
    n 1fchgn "...Yuri!"
    n 4tnmbg "Surprised?{w=0.5}{nw}"
    extend 1fcsss " I know,{w=0.1} right?"
    n 3tllss "I mean...{w=0.3} it was just completely out of the blue!"
    n 1uchbs "She just slipped it out from her bag like it was a book or something."
    n 4unmbo "It wasn't even just some random supermarket stuff either...{w=0.5}{nw}"
    extend 1uwdaj " it looked super expensive too!"
    n 3kllss "Honestly,{w=0.1} I couldn't help myself.{w=0.2} I just burst into laughter."
    n 1ullun "I think it was just how all casual she was being about it all,{w=0.1} really."
    n 4nnmsl "Monika didn't look impressed,{w=0.1} though..."
    n 1klrsl "And Sayori...{w=0.3} she just got really upset.{w=0.5}{nw}"
    extend 2klrpu " She was shouting and everything!"
    n 1kcspu "It looked like Yuri put a lot of thought into picking something out,{w=0.1} but she was just given a hard time over for it..."
    n 1kcssr "I mean...{w=0.5}{nw}"
    extend 1kllsr " I know we shouldn't have had it in there at all,{w=0.1} and Yuri should have known better."
    n 2fslsr "But she didn't deserve all of...{w=0.5}{nw}"
    extend 2kslsr " that."
    n 1kslaj "I think she was just trying to be nice,{w=0.1} you know?"
    n 4unmsr "It's all in the past now,{w=0.1} obviously.{w=0.5}{nw}"
    extend 2kslsr " But...{w=0.3} that doesn't mean I don't still feel bad about it sometimes."
    n 1kcssr "..."

    if Natsuki.isAffectionate(higher=True):
        n 1kllsr "Hey...{w=0.5}{nw}"
        extend 4knmpu " [player]?"
        n 1klrsr "Can you promise me something?"
        n 2fcssr "It's dumb,{w=0.1} but I don't care."
        n 1nnmsl "It doesn't really matter to me if you drink or not."
        n 2klrpu "But...{w=0.3} if you do?"
        n 4ksqsr "Please just take it all in moderation,{w=0.1} okay?"
        n 2kllsr "I've...{w=0.5}{nw}"
        extend 2fcsan " seen...{w=0.5}{nw}"
        extend 1fcssr " what it can do to people."
        n 1kslsr "...Firsthand."
        n 4ksqsl "You deserve better than that,{w=0.1} [player].{w=0.5}{nw}"
        extend 4kslun " You {i}are{/i} better than that."

        if Natsuki.isLove(higher=True):
            n 1kcsun "..."
            n 1ksqsml "I love you,{w=0.1} [player]."
            n 3fcssrl "I'm {w=0.3}{i}never{/i}{w=0.3} going to let a bottle get between us."

    else:
        n 4unmsr "Hey,{w=0.1} [player]?"
        n 1nllaj "I don't really care that much if you drink or not."
        n 2ncssr "Just...{w=0.3} go easy on the stuff."
        n 2flleml "B-{w=0.1}but only because I'm not gonna clean up after you!"
        n 2fllss "Ahaha..."
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
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:
    # Check to see if the player and Natsuki have already discussed if Nat can drive in this topic, or the "are you into cars?" topic
    $ already_discussed_driving = get_topic("talk_driving").shown_count > 0 or get_topic("talk_are_you_into_cars").shown_count > 0
    $ chosen_tease = jn_utils.getRandomTease()

    if already_discussed_driving:
        n 4tnmboeqm "...Huh?{w=0.75}{nw}"
        extend 1tllsssbr " I already told you I can't drive,{w=0.2} [chosen_tease]!"
        n 1fchgnelg "I still don't have a license,{w=0.2} remember?"
        n 3tllaj "And even if I wanted to,{w=0.5}{nw}"
        extend 3nslposbl " I don't think I could afford it..."

    else:
        n 1fchdvesm "Pffft!{w=0.5}{nw}"
        extend 1uchbselg " Ahaha!"
        n 3fchgn "What kind of a question is that,{w=0.1} [player]?"
        n 1tllss "Of course I can't drive,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 4fchgn " I don't even have a license!"
        n 2kllpo "I mean...{w=0.3} even if I wanted to learn,{w=0.1} I don't think I could afford it."

    n 1uskgs "Lessons are super expensive nowadays!"
    n 3fslem "And then there's tests,{w=0.1} insurance,{w=0.1} fuel,{w=0.1} parking...{w=0.5}{nw}"
    extend 1fsqaj " it's actually pretty gross how fast it all adds up."
    n 1nlraj "I think I'd rather stick to public transport and my own two feet."
    n 4unmaj "But what about you,{w=0.1} [player]?"
    show natsuki 1tnmss at jn_center

    # Player has never confirmed if they can/cannot drive
    if persistent.jn_player_can_drive is None:
        menu:
            n "Can you drive?"

            "Yes, and I do currently.":
                n 1uwdaj "Wow..."
                extend 3fsraj " ...{w=0.3}show-off."
                n 1fsqpo "..."
                n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1nchsm " I'm just messing with you."
                n 4unmbg "That's awesome though{w=0.1} -{w=0.1} you just can't beat the convenience of a car,{w=0.1} right?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fllbg "But I should probably warn you..."
                    n 3fsgsm "I'm picking the songs for our driving playlist."
                    extend 3uchbgelg " Ahaha!"

                else:
                    n 2fllbg "Just remember,{w=0.1} [player]..."
                    n 4fsgsm "I call shotgun.{w=0.5}{nw}"

                $ persistent.jn_player_can_drive = True
                return

            "Yes, but I don't right now.":
                n 4unmaj "Oh?{w=0.2} Is something wrong with your car,{w=0.1} [player]?"
                n 2tllbo "Or perhaps...{w=0.3} you just don't own one at the moment?"
                n 1nnmsm "Well,{w=0.1} I'm not one to judge.{w=0.2} I'm sure you manage just fine."
                n 2flrss "Besides,{w=0.1} you're helping the environment too,{w=0.1} right?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fsgsm "Thoughtful as always,{w=0.1} [player]."
                    extend 4nchsm " Ehehe."

                $ persistent.jn_player_can_drive = True
                return

            "No, I can't.":
                n 2klrsl "Oh..."
                n 1flrss "Well,{w=0.3}{nw}"
                extend 1fchbg " chin up,{w=0.1} [player]!{w=0.2} It isn't the end of the world."
                n 1usgsg "Don't worry -{w=0.3}{nw}"
                extend 1fsgsm " I'll teach you how to use the bus!"
                n 4uchsm "Ehehe."

                if Natsuki.isEnamored(higher=True):
                    n 1fllsm "And besides..."
                    n 3fllssl "That just means we can huddle up on the seat together,{w=0.1} [player]."
                    n 1fcsbgl "A dream come true for you,{w=0.1} right?"
                    n 4flldvl "Ehehe."

                else:
                    n 4fchbg "That's what friends are for, [player]!"

                $ persistent.jn_player_can_drive = False
                return

    # Player stated they can drive previously
    elif persistent.jn_player_can_drive:
        menu:
            n "Doing much driving?"

            "Yes, I'm driving frequently.":
                n 1fnmbg "Ah,{w=0.1}  so you're at home on the roads,{w=0.1} are you?"
                n 4ullss "Fair enough I suppose -{w=0.1} just remember to drive safe,{w=0.1} [player]!"

            "I only drive sometimes.":
                n 4ullss "Well hey,{w=0.1} at least you're saving on fuel,{w=0.1} right?{w=0.5}{nw}"
                extend 1ullsm " That doesn't sound like a bad thing to me."
                n 1fchsm "Besides,{w=0.1} it just means you can save the miles for ones you enjoy!"

            "No, I'm not driving much.":
                n 4unmaj "Oh?{w=0.5}{nw}"
                extend 1tllbg " That sounds like a bonus to me,{w=0.1} honestly!"
                n 1tnmbg "Just make sure you still get out there if you aren't driving around much though,{w=0.1} 'kay?"

            "No, I can't drive anymore.":
                n 4tnmsl "Oh...{w=0.3} did something happen?"
                n 3kllsl "I'm...{w=0.3} sorry to hear it,{w=0.1} [player]."
                n 1fsgsm "But at least that means more time to hang out with me,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ahaha."
                $ persistent.jn_player_can_drive = False

        return

    # Player admitted they cannot drive previously
    else:
        menu:
            n "Anything new happening with you on the driving front?"

            "I'm learning to drive!":
                n 4fnmss "Ooh!{w=0.5}{nw}"
                extend 1fchbg " Nice,{w=0.1} [player]!"
                n 1fchsm "Don't sweat the test,{w=0.1} alright?{w=0.2} I'm sure you'll do fine!"

                if Natsuki.isAffectionate(higher=True):
                    n 4uchsm "I believe in you,{w=0.1} [player]!"

            "I passed my test!":
                n 4uskgs "No kidding?{w=0.5}{nw}"
                extend 3uchbs " Yaaay!{w=0.2} Congrats,{w=0.1} [player]!"

                if Natsuki.isLove(higher=True):
                    n 4kwmsm "I knew you could do it,{w=0.1} you big dummy!"
                    extend 4kchsm " Ehehe."

                n 3kwmsm "Just make sure you keep up the good habits when you continue learning on your own,{w=0.1} alright?{w=0.2} Ahaha."
                $ persistent.jn_player_can_drive = True

            "I can drive again!":
                n 3uchbgedz "Hey!{w=0.2} Nice going,{w=0.1} [player]!"
                n 1fchbl "Drive safe!"
                $ persistent.jn_player_can_drive = True

            "Nope, nothing new.":
                n 4unmaj "Oh?{w=0.5}{nw}"
                extend 1nlrss " Well,{w=0.1} fair enough!"
                n 2tnmsm "You and me both then,{w=0.1} in that case?{w=0.5}{nw}"
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
            affinity_range=(jn_affinity.UPSET, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sustainable_fashion:
    n 1nnmaj "Hey,{w=0.1} [player]..."
    n 3nllaj "This is kinda random,{w=0.1} but..."
    extend 4unmpu " are you into fashion?"
    if Natsuki.isHappy(higher=True):
        n 1fcsbg "I know I am!{w=0.2} Can you tell?"
        extend 1nchsm " Ehehe."

    else:
        n 1nnmpu "I know I am."

    n 3fllpu "But what caught me by surprise is just how much waste there is."

    if Natsuki.isNormal(higher=True):
        n 1uwdgs "Seriously,{w=0.1} [player] {w=0.1}-{w=0.1} it's insane!"
        n 1ullaj "People throw away a {i}lot{/i} of clothing...{w=0.5}{nw}"
        extend 3flrem " it's estimated that we toss out around 90{w=0.3} {i}million{/i}{w=0.3} tonnes every year."
        n 1fnman "That's a truck-full every second!{w=0.2} What a waste!"

    else:
        n 1nllbo "It's pretty insane, honestly."
        n 2fnmsl "I remember reading somewhere that we toss out something like 90{w=0.3} {i}million{/i}{w=0.3} tonnes each year."
        n 1fcsan "That's literally a truck-full {i}every{w=0.3} second{/i}."

    n 2fsrem "And we haven't even began to talk about the amount of water used for washing and plastic used for packaging too."
    n 1ksrsr "...Or the conditions some of the workers making our clothes have to put up with."

    if Natsuki.isNormal(higher=True):
        n 1fcssm "It's actually one of the reasons I began learning how to sew!"
        n 2klrsr "I've...{w=0.3} never had tons of money to buy more clothes anyway,{w=0.1} so I try to reuse and fix up what I can."
        n 1fchbg "But you'd be surprised at what you can pull off with a little creativity!"
        extend 1fcssm " And just a pinch of know-how too,{w=0.1} obviously."
        n 4fchgn "Betcha' didn't know my favorite pink skirt was hand-made,{w=0.1} did you?"

    n 1unmaj "I think I've lectured you enough now,{w=0.1} [player],{w=0.1} so I won't keep harping on about it."
    n 3nllpu "But...{w=0.3} the next time you're out shopping for clothes,{w=0.1} or looking through some catalogues online?"
    n 3unmpu "Just spare a thought for the environment,{w=0.1} would you?"

    if Natsuki.isAffectionate(higher=True):
        n 1kllssl "For me?"
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 4uchsm " Thanks,{w=0.1} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 4uchsm " Thanks,{w=0.1} [player]!"

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
            conditional="persistent._jn_nicknames_natsuki_allowed",
            category=["Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_give_nickname:
    # Natsuki hasn't been nicknamed before, or is rocking her normal name
    if persistent._jn_nicknames_natsuki_allowed and persistent._jn_nicknames_natsuki_current_nickname == "Natsuki":
        n 1unmaj "Eh?{w=0.2} You want to give me a nickname?"
        n 2fsqsl "Why?{w=0.2} Natsuki not good enough for you?{w=0.2} Is that it?"
        extend 4fsqpu " Huh?{w=0.2} Come on, [player]!{w=0.2} Spit it out!"
        n 1fsqsm "..."
        n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.2} I'm just kidding!"
        extend 1fchsm " Ehehe."
        n 3ullbg "Well...{w=0.3} I don't see why not!"

    # Another nickname is being assigned
    else:

        # Account for strikes
        if persistent._jn_nicknames_natsuki_bad_given_total == 0:
            n 4unmaj "Oh?{w=0.2} You wanna give me another nickname?"
            n 1uchbg "Sure,{w=0.1} why not!"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 1:
            n 4unmaj "You want to give me a new nickname?"
            n 1unmbo "Alright,{w=0.1} [player]."

        elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
            n 1nnmsl "Another nickname,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nllsl " Fine."
            n 2ncsaj "Just...{w=0.3} think a little about what you choose,{w=0.1} 'kay?"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
            n 1nnmsl "Alright,{w=0.1} [player]."
            n 2fsqpu "Just remember.{w=0.3} You've had your final warning about this."
            n 1nsqsl "Don't let me down again."

    # Validate the nickname, respond appropriately
    $ nickname = renpy.input(prompt="What did you have in mind,{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n 4tnmpu "Huh?{w=0.2} You changed your mind?"
        n 4tllpu "Well...{w=0.3} alright then."
        n 1nnmaj "Just let me know if you actually want to call me something else then,{w=0.1} 'kay?"
        return

    else:
        $ nickname_type = jn_nicknames.getNatsukiNicknameType(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 2tlraj "Uhmm...{w=0.3} [player]?"
        n 1tnmaj "I don't think that's a nickname at all."
        n 1tllss "I'll...{w=0.3} just stick with what I have now,{w=0.1} thanks."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.loved:
        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        n 1uskgsl "O-{w=0.1}oh!{w=0.2} [player]!"
        n 1ulrunl "..."
        n 1fcsbgl "W-{w=0.1}well,{w=0.1} you have good taste,{w=0.1} at least."
        n 1fcssml "[nickname] it is!{w=0.5}{nw}"
        extend 1uchsml " Ehehe."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 2fsqbo "Come on,{w=0.1} [player]...{w=0.3} really?"
        n 2fllsl "You knew I'm not gonna be comfortable being called that."
        n 1fcssl "..."
        n 1nlraj "I'm...{w=0.3} just going to pretend you didn't say that,{w=0.1} alright?"
        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 2fskem "W-{w=0.1}what?{w=0.5}{nw}"
        extend 1fscwr " What did you just call me?!"
        n 2fcsan "[player]!{w=0.2} I can't believe you!"
        n 2fcsfu "Why would you call me that?{w=0.5}{nw}"
        extend 1fsqfu " That's {i}awful{/i}!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 4fskpu "E-{w=0.1}excuse me?!"
        n 2fskfu "What the hell did you just call me,{w=0.1} [player]?!"
        n 1fcsan "..."
        n 1fslan "I seriously can't believe you,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fnman " Why would you do that?{w=0.1} Are you {i}trying{/i} to get on my nerves?!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 4nbkdvesm "Pffft!"
        n 1uchbselg "Ahaha!"
        n 1fbkbs "[nickname]?!{w=0.2} What was that meant to be,{w=0.1} [player]?"
        n 4fchbg "Well...{w=0.3} you're just lucky I have a healthy sense of humor."
        n 4fsgbg "[nickname] it is,{w=0.1} I guess!{w=0.5}{nw}"
        extend 1fchgn " Ehehe."

        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        return

    elif nickname_type == jn_nicknames.NicknameTypes.nou:
        n 2usqsg "No you~."
        return

    else:
        $ neutral_nickname_permitted = False

        # Check and respond to easter egg nicknames
        if nickname.lower() == "natsuki":
            n 1fllss "Uhmm...{w=0.5}{nw}"
            extend 4tnmdv " [player]?"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbg "That's just my normal name,{w=0.1} [chosen_tease]!"
            n 3fcsca "Honestly...{w=0.5}{nw}"
            extend 3ksgsg " sometimes I wonder why I bother."
            n 1unmbg "Well,{w=0.1} I'm not complaining!{w=0.2} If it isn't broke,{w=0.1} don't fix it -{w=0.1} right?"
            n 1nchbg "Ahaha."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n 3kllunl "..."
            n 3fnmssl "D-{w=0.1}dreaming big,{w=0.1} are we,{w=0.1} [player]?"
            n 1klrsrl "Uhmm..."
            n 4klrpol "I'm...{w=0.3} really...{w=0.3} not a fan,{w=0.1} but if it's what you prefer..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n 4fsldv "I...{w=0.3} don't think you thought this through,{w=0.1} [player]."
            n 1tnmbg "Do you even know how confusing that'd be?"
            n 1tlrss "I...{w=0.3} think I'll just stick to what works,{w=0.1} 'kay?{w=0.5}{nw}"
            extend 4fsqsm " Ehehe."
            n 1uchbg "Nice try though!"

        # Fallback for anything not categorised
        else:
            n 1fllsr "Hmm...{w=0.5}{nw}"
            extend 1ullpu " [nickname],{w=0.1} huh?"
            n 4fllss "[nickname]..."
            n 1fnmbg "You know what?{w=0.2} Yeah!{w=0.2} I like it!"
            n 3fchbg "Consider it done,{w=0.1} [player]!{w=0.5}{nw}"
            extend 3uchsm " Ehehe."
            $ neutral_nickname_permitted = True

        # Finally, assign the neutral/easter egg nickname if it was permitted by Natsuki
        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_natsuki_current_nickname = nickname
            $ n_name = persistent._jn_nicknames_natsuki_current_nickname

        return

    # Handle strikes
    if persistent._jn_nicknames_natsuki_bad_given_total == 1:
        n 2kllsf "Jeez,{w=0.1} [player]...{w=0.3} that isn't like you at all!{w=0.5}{nw}"
        extend 1knmaj " What's up with you today?"
        n 1kcssl "..."
        n 1knmsl "Just...{w=0.3} don't do that again,{w=0.1} okay?"
        n 2fsqsl "That really hurt,{w=0.1} [player].{w=0.2} Don't abuse my trust."

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
        n 1fsqsl "I can't believe you did that again to me,{w=0.1} [player]."
        n 2fsqan "I told you it hurts,{w=0.1} and you went ahead anyway!"
        n 1fcsan "..."
        n 1fcsun "I...{w=0.3} really...{w=0.3} like you, [player].{w=0.5}{nw}"
        extend 4kllun " It hurts extra bad when it's you."
        n 2fsqsr "Don't test my patience like this.{w=0.2} You're better than that."

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
        n 1fsqan "You are honestly unbelievable,{w=0.1} [player]."
        n 2fnmfu "I've told you so many times now,{w=0.1} and you still won't knock it off!"
        n 1fcspu "..."
        n 2fsqpu "No more warnings,{w=0.1} [player]."
        menu:
            n "Understand?"

            "I understand.":
                n 1fsqsr "You understand,{w=0.1} do you?"
                n 2fsqan "...Then start acting like it,{w=0.1} [player]."
                n 1fslsl "Thanks."

                $ Natsuki.percentageAffinityLoss(3)

            "...":
                n 1fcssl "Look.{w=0.2} I'm not kidding around,{w=0.1} [player]."
                n 1fnmpu "Acting like this isn't funny,{w=0.1} or cute."
                n 2fsqem "It's toxic."
                n 1fsqsr "I don't care if you're trying to pull my leg.{w=0.2} Quit it."

                $ Natsuki.percentageAffinityLoss(5)

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 4:
        # Player is locked out of nicknaming; this is why we can't have nice things
        n 2fcsan "Yeah,{w=0.1} no.{w=0.2} I've heard enough.{w=0.2} I don't need to hear any more."
        n 1fnmem "When will you learn that your actions have consequences?"
        n 1fcspu "..."
        n 1fnmpu "You know what?{w=0.5}{nw}"
        extend 2fsqpu " Don't even bother answering."
        n 1fsqsr "I warned you,{w=0.1} [player].{w=0.2} Remember that."

        # Apply affinity/trust penalties, then revoke nickname priveleges and finally apply pending apology
        python:
            get_topic("talk_give_nickname").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_natsuki_allowed = False
            persistent._jn_nicknames_natsuki_current_nickname = None
            n_name = "Natsuki"
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)


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
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sleeping_well:
    n 1fllpu "Huh..."
    n 4uwdaj "Hey,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nnmaj " Let me ask you a question,{w=0.1} 'kay?"
    n 2fsqsr "How do you sleep at night?"
    n 1fsqpu "Be honest.{w=0.2} How do you do it?"
    n 1ksqsm "..."
    n 3fchsm "Ehehe.{w=0.2} Did I get you?"
    n 1unmaj "But seriously,{w=0.2} [player].{w=0.5}{nw}"
    extend 4tnmaj " Do you struggle with your sleep?"

    # Quip if the player has been around a while, or has admitted they're tired
    if jn_utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n 2fsqpo "I mean,{w=0.1} you {i}have{/i} been here for a while now..."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " I kinda figured you might be feeling a little sleepy anyway."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 2fllpo "I mean,{w=0.1} you even {i}said{/i} you were tired before."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " it only makes sense to ask,{w=0.1} right?{w=0.2} Anyway..."

    n 2fslpu "I'll admit,{w=0.1} I get the odd sleepless night myself.{w=0.5}{nw}"
    extend 4fbkwr " It's the worst!"
    n 1fllem "There's nothing I hate more than tossing and turning,{w=0.3}{nw}"
    extend 2fcsan " just waiting for my body to decide it's time for tomorrow to happen."
    n 1ullaj "But...{w=0.5}{nw}"
    extend 4fnmss " you know what they say,{w=0.1} [player]."
    n 3fcsss "With suffering...{w=0.5}{nw}"
    extend 3uchbg  " ...comes wisdom!"
    n 1nsqbg "And luckily for you,{w=0.1} I don't mind sharing.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."
    n 1fcsbg "So,{w=0.1} listen up -{w=0.1} it's time for another lesson from yours truly!"
    n 1fnmaj "Alright -{w=0.1} first,{w=0.1} cut the crap!{w=0.2} If you're trying to sleep,{w=0.1} anything high-sugar or high-caffeine is your enemy."
    n 3fllss "So before anything else,{w=0.1} ditch the soda and coffee.{w=0.2} You can thank me later."
    n 1fcsaj "Next up -{w=0.1} no screens!{w=0.5}{nw}"
    extend 4fsqpo " Including this one, [player]."
    n 1unmsl "No screen means no bright lights or distractions to keep you up,{w=0.1} obviously."
    n 1fnmpu "If you're tired then the last thing you need is something beaming whatever at you."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.anime_streaming):
        n 3tsqsr "And no, [player] {w=0.1}-{w=0.3}{nw}"
        extend 3fnmpo " No late-night anime binging sessions either."
        n 1nchgn "Sorry~!"

    n 1fcsbg "Moving on, next is temperature!{w=0.2} If it's hot,{w=0.1} use thinner sheets and vice versa."
    n 1fcspu "Nothing disrupts your sleep more than having to rip off blankets,{w=0.1} or pull some out."
    n 3fsgsg "Keeping up with me so far,{w=0.1} [player]?{w=0.5}{nw}"
    extend 4fchgn " I'm almost done,{w=0.1} don't worry."
    n 1unmaj "Lastly...{w=0.5}{nw}"
    extend 1fchbg " get comfortable!"
    n 1nnmsm "Make sure you have enough pillows to support your head,{w=0.1} or maybe even play some quiet music if you find that helps."
    n 1fcssm "...And that's about it!"
    n 1nllss "You should have known at least a few of those already,{w=0.3}{nw}"
    extend 4unmss " but at any rate..."
    n 3fwlbg "I hope you can rest easy with your newfound knowledge,{w=0.1} [player]!"
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
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_aging:
    n 1unmaj "You know,{w=0.1} [player]..."
    n 1nllpu "I think most people share a bunch of fears."
    n 1unmpu "You get what I mean,{w=0.1} right?{w=0.2} Like presenting stuff to a room full of people,{w=0.1} or failing a test."
    n 3tlrss "Of course,{w=0.1} it's rare to find one that {i}everyone{/i} has..."
    n 1tnmaj "Or at least something that makes anyone feel uneasy."
    n 1unmbg "But...{w=0.3} I think I found one!"
    n 4usgsm "What am I thinking of,{w=0.1} you ask?"
    n 1ullaj "Well...{w=0.3} it's actually kinda boring,{w=0.1} really."
    n 1nnmbo "I was actually thinking about growing older."
    n 3unmpu "Have you ever thought much about it,{w=0.1} [player]?"
    n 4fllbg "It's probably the last thing on your mind if you're pretty young."
    n 1nwmpu "But I think as you actually get older,{w=0.1} it starts to creep in."
    n 1kllpu "You might have less energy,{w=0.1} or friends and family begin drifting away..."
    n 2knmem "Birthdays lose all meaning -{w=0.1} you might even dread them!"
    n 1ullaj "The signs appear in a bunch of ways,{w=0.3}{nw}"
    extend 1knmsl " but that's what makes it unnerving."
    n 1kllaj "Everyone experiences it differently,{w=0.3}{nw}"
    extend 2ksksl " and we don't even know what happens after the end!"
    n 1klrss "Spooky,{w=0.1} huh?"
    n 1ulrpu "Although...{w=0.3} I guess you could say that's more the fear of the unknown than aging itself."
    n 2flraj "What does wind me up though is how immature people can be about it."
    n 1fnmaj "Especially when it comes to relationships between different ages!"
    n 2fslsf "People just get so preachy about it..."
    n 1fllaj "Like...{w=0.3} as long as they're both happy,{w=0.2} it's all legal,{w=0.3}{nw}"
    extend 4fnmem " and nobody is being hurt or made uncomfortable,{w=0.1} who {i}actually{/i} cares?"
    n 2nlrpu "It's just like most stuff,{w=0.1} really."
    n 1unmaj "Besides,{w=0.1} it's not like being a certain age means you {i}have{/i} to be a certain way."
    n 1fchbg "I mean...{w=0.3} look at Yuri!"
    n 1uchgn "Being all old-fashioned like that -{w=0.1} you'd think she's retired!"
    n 4nllbg "But anyway...{w=0.3} I think we got side-tracked."
    n 1unmss "I don't really care how old you are,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3klrpol "Y-{w=0.1}you better know that I love you all the same,{w=0.1} [chosen_tease]."
        n 3knmpol "Don't forget that,{w=0.1} 'kay?"
        n 4flrpol "I'll get mad if you do.{w=0.5}{nw}"
        extend 1klrbgl " Ahaha..."

    elif Natsuki.isEnamored(higher=True):
        n 2fllbgl "You've been pretty awesome to me all the same."

    elif Natsuki.isHappy(higher=True):
        n 4fchbgl "You're always fun to hang around with!"

    else:
        n 1fllbg "But...{w=0.3} just in case?"
        n 2fsqsg "We're only having one candle on your birthday cake.{w=0.2} Sorry.{w=0.5}{nw}"
        extend 1uchbgelg " Ahaha!"

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
    if Natsuki.isUpset(higher=True):
        n 4ullaj "You know,{w=0.1} [player]..."

    n 1nnmaj "I think it's pretty easy to let your academic or work life creep into your personal time nowadays."
    n 2nlrsl "I mean...{w=0.3} think about it."
    n 1nnmsl "With everyone having mobile phones,{w=0.1} plus usually some kinda computer at home -{w=0.1} it's hard not to be connected somehow."
    n 2flrbo "And like...{w=0.3} if there's already that connection,{w=0.1} then what's to stop work from bugging you during your time off?"
    n 2fsrun "Or classmates asking for help at the last possible minute?"

    if Natsuki.isUpset(higher=True):
        n 1fcsem "It just gets annoying -{w=0.1} like everyone expects you to always be around to chip in a little more,{w=0.1} or get something done!"
        n 2fnmpo "Overwhelming,{w=0.1} right?"
        n 1fllaj "Huh.{w=0.2} Actually...{w=0.3} now that I think about it..."
        n 4fnmsf "It isn't like that kind of intrusion is only limited to when you're away either."
        n 1fslpu "I've heard {i}way{/i} too many stories of people doing stupid amounts of overtime at work...{w=0.5}{nw}"
        extend 3fnman " sometimes not even paid!"
        n 1fsran "Or even students studying late into the night until they collapse...{w=0.3} it's crazy!"

    else:
        n 1fsqpu "It just gets annoying -{w=0.1} everyone expects you to always be around to do more."
        n 2fslsl "Actually,{w=0.1} now that I think about it..."
        n 1fcsaj "It isn't like that kind of thing is only limited to when you're away either."
        n 1fsrsr "I've heard too many stories of people doing stupid amounts of overtime at work.{w=0.5}{nw}"
        extend 3fsqan " Often not even paid."
        n 1fslem "Or even students studying late into the night until they collapse..."

    if Natsuki.isNormal(higher=True):
        n 1kcsemesi "Ugh...{w=1} I just wish people would value their own time more."
        n 1klrsr "..."
        n 4unmaj "Hey,{w=0.1} [player]..."
        n 1nllaj "I don't know if you're working,{w=0.1} or studying,{w=0.1} or what..."
        n 3fnmsf "But you better not be letting whatever it is take over your life.{w=0.2} Understand?"

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "You are {i}more{/i} than your career,{w=0.1} or your education.{w=0.2} You have your own wants and needs that matter too."
            n 3kllun "I don't want some dumb job or stupid assignment to take over your life."
            n 1fcsun "You're...{w=0.3} way more important than either of those,{w=0.1} [player].{w=0.2} Trust me."

            if Natsuki.isLove(higher=True):
                n 4fllun "Besides..."
                n 1fllssl "You and your time are mine first, [player]."
                n 3flldvl "I already called dibs,{w=0.1} a-{w=0.1}after all.{w=0.5}{nw}"
                extend 3fchsml " Ehehe..."

        else:
            $ chosen_tease = jn_utils.getRandomTease()
            n 3kllpo "People are more than what they do for a living,{w=0.1} after all.{w=0.2} And that includes you too, [chosen_tease]!"

    elif Natsuki.isDistressed(higher=True):
        n 3fllsr "Makes me wish people would value their own time more."
        n 1fnmsr "...I guess that includes you too,{w=0.1} [player]."
        n 1fllpu "You've got better things to do."
        n 2fsqsf "...Like being a decent friend to others for a change.{w=0.2} Am I right?"

    else:
        n 1fslbo "People need to value their own time more,{w=0.1} I guess."
        n 1fcssl "...Heh."
        n 3fcsunl "Maybe I should follow my own advice..."
        n 1fsqanltsb "Because {i}clearly{/i} being here is a waste of my time too."

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
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_headphones_carefully:
    n 1unmaj "..."
    n 4tnmaj "...?"
    n 2fnmaw "...!"
    n 1fbkwr "...[player]!"
    n 3fnmpo "[player]!{w=0.2} Finally!{w=0.2} Can you hear me now?"
    n 3fllpo "Jeez...{w=0.3} took you long enough!"
    n 1fslsm "..."
    n 1uchbg "Ehehe."
    n 4fnmbg "Admit it,{w=0.1} [player]!{w=0.2} I'll get you one of these days."
    n 1nnmaj "Seriously though -{w=0.1} do you use headphones or anything like that often?"
    n 3nlrpo "I'll admit,{w=0.1} I probably use mine more than I should."
    n 1fnmaj "I was kinda joking about the whole hearing thing,{w=0.1} but this is important,{w=0.1} [player]."
    n 1nlrss "I like cranking it up too -{w=0.1} just don't make a bad habit of it."
    n 4unmsl "There's even warnings in some countries if you have the volume up too loud..."
    n 1fllem "...And for a good reason!"
    n 2fnmpo "Not just to protect your ears either -{w=0.1} you better be careful wearing them out and about too."
    n 1fcsem "I don't wanna hear about you getting knocked over because you didn't hear something coming!"
    n 4unmbo "Oh -{w=0.1} and one last thing,{w=0.1} actually."
    n 1unmpu "You might wear them to focus at work or relax at home -{w=0.1} and that's fine!"
    n 2nnmsr "But please,{w=0.1} [player]."
    n 4flrsr "...Take them off every once and a while,{w=0.1} will you?{w=0.2} For other people,{w=0.1} I mean."
    n 1ncsbo "I get it -{w=0.1} if you just wanna listen to something in peace,{w=0.1} or give yourself some room,{w=0.1} that's okay."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.music_applications):
        n 1kslbg "I know you like your music streaming."

    n 1nsqbo "But don't use them to barricade yourself away from everyone and everything."
    n 2ksrsl "It's...{w=0.3} not healthy to do that either,{w=0.1} [player]."
    n 1nchsm "...And that's about all I had to say!"
    n 4fchbg "Thanks for {i}hearing{/i} me out,{w=0.1} [player]!{w=0.2} Ehehe."
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

    if Natsuki.isNormal(higher=True):
        n 4unmaj "You know,{w=0.1} [player]..."
        n 1tllaj "I don't think I ever actually explained why I dislike horror so much."
        n 1tlrss "I know I mentioned it before,{w=0.1} but I was kinda caught off guard at the time."
        n 3unmaj "Honestly?"
        n 1nnmsm "Everyone has their tastes,{w=0.1} right? And I can get why people enjoy it."

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "I don't think I explained why I dislike horror."
        n 2nnmsl "I get everyone has their tastes,{w=0.1} but I don't care for it."

    else:
        n 1kslsl "..."
        n 2fsqun "...I was about to share some of my thoughts on horror with you.{w=1}{nw}"
        extend 1fsrsl " Or at least,{w=0.1} I was thinking about it."
        n 2fsqem "...But then do you know what I realized,{w=0.1} [player]?"
        n 1fsqan "I hate horror -{w=0.5}{nw}"
        extend 1fllem " not that you'd care -{w=0.3}{nw}"
        extend 4fnmful " and honestly?"
        n 1fcsanltsa "Being stuck here with {i}you{/i} is horror enough."
        return

    if Natsuki.isNormal(higher=True):
        n 1fchbg "Like Yuri!"
        n 1fcsss "It's suspenseful,{w=0.1} and fears are a super powerful motivator for characters!"
        n 4ullpu "So don't get me wrong{w=0.1} -{w=0.1} I can totally appreciate the effort that goes into it."
        n 2fllpol "...When it isn't just stupid jumpscares,{w=0.1} a-{w=0.1}anyway."

    else:
        n 2uslbo "I get the effort that goes into it.{w=0.2} For the most part."

    n 1nllpu "But..."
    n 1nnmbo "When I read something -{w=0.1} or watch something -{w=0.1} I'm doing it because for me,{w=0.1} it's how I relax."
    n 1fllbo "I don't want to be made to feel uneasy."
    n 2fllpu "I don't want to be made to jump."
    n 2fllsr "I don't want to have to see gross stuff."
    n 1fcssr "I...{w=0.3} just want to sit back,{w=0.1} feel good and just escape for a while."
    n 4fnmsl "There's more than enough nasty things going out there already,{w=0.1} you know?"
    n 1flrpu "Some things closer to home than others."
    n 1fcssl "..."
    n 1nnmaj "So...{w=0.3} yeah.{w=0.1} That's about all I had to say about it."

    if Natsuki.isAffectionate(higher=True):
        n 1unmss "Though...{w=0.3} if you want to put something on,{w=0.1} [player]?{w=0.2} Go ahead."
        n 2fllssl "If it's you,{w=0.1} I {i}think{/i} I can deal with it."
        n 2flrpol "But...{w=0.3} we're keeping the volume low.{w=0.2} Got it?"

    elif Natsuki.isNormal(higher=True):
        n 1nnmaj "Don't mind me though,{w=0.1} [player].{w=0.2} If you wanna watch something,{w=0.1} go for it."
        n 2flrcal "But you're watching it solo."

    elif Natsuki.isDistressed(higher=True):
        n 1flrsl "..."
        n 1fnmpu "I {i}would{/i} ask that if you were gonna watch something like that,{w=0.1} then to warn me first."
        n 2fsqsrtsb "But you wouldn't listen to me anyway,{w=0.1} would you?"

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
    if Natsuki.isNormal(higher=True):
        n 4unmaj "Gaming?"
        n 1fcsbg "Well...{w=0.3} duh!"
        n 1fnmbg "You bet I'm into gaming,{w=0.1} [player]!"
        n 3ullss "I wouldn't say I'm the most active player...{w=0.2} but I definitely do my share of button mashing."
        n 1nslsg "Hmm..."
        n 4tnmss "I don't think I even need to ask,{w=0.1} but..."
        menu:
            n "What about you,{w=0.1} [player]?{w=0.2} Do you play often?"

            "Absolutely!":
                $ persistent.jn_player_gaming_frequency = "High"
                n 3fcsbg "Yep!{w=0.2} Just as I suspected..."
                n 1uchgn "[player] is a mega-dork."
                n 4uchbselg "Ahaha!"
                n 1uchsm "Relax,{w=0.1} [player]!"
                n 3fllssl "I'm not much better,{w=0.1} after all."

            "I play occasionally.":
                $ persistent.jn_player_gaming_frequency = "Medium"
                n 1fsqsm "Yeah,{w=0.1} yeah.{w=0.2} Believe what you want to believe,{w=0.1} [player]."
                n 3usqbg "I'm not sure I buy it,{w=0.1} though."

            "I don't play at all.":
                $ persistent.jn_player_gaming_frequency = "Low"
                n 4tnmaj "Huh?{w=0.2} Really?"
                n 1tllaj "Not even the odd casual game?"

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                    n 4fsqts "Liar.{nw}"

                n 1ncsaj "...Well then."
                n 3fnmbg "It looks like I've got a lot to teach you,{w=0.1} [player]!"

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "Huh?{w=0.2} Video games?"
        n 2nslsl "Yeah,{w=0.1} I guess.{w=0.2} For what that's worth to you."

    else:
        n 1nsqsl "Video games...?"
        n 2fsqsltsb "...Heh.{w=0.2} Why,{w=0.3} [player]?{w=1}{nw}"
        extend 1fcsantsa " Was stomping all over my feelings not enough?"
        n 4fsqfultsb "Or were you looking to see if you can stomp all over me in games too?"
        n 1fcsfrltsa "..."
        n 1fcsupl "...I don't wanna talk about this any more.{w=0.2} We're {i}done{/i} here."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "Anyway,{w=0.1} putting that aside..."
        n 4nsgbg "When it comes to my preferences?{w=0.2} I want challenge in my games!"
        n 3fcsbg "I play for the win{w=0.1} -{w=0.1} it's me versus the developers,{w=0.1} and they're not around to stop me!"
        n 3fchbg "Ahaha."
        n 1ullss "I'm actually more into my roguelikes,{w=0.1} to be honest."
        n 4fnmsm "Heh.{w=0.2} Are you surprised,{w=0.1} [player]?"
        n 3fcsbg "Tough as nails,{w=0.1} and I gotta think on my feet{w=0.1} -{w=0.1} plus it's super satisfying learning everything too."
        n 1fchsm "And with how random everything is,{w=0.1} they always feel refreshing and fun to play!"
        n 1fnmbg "Every time I load one up,{w=0.1} I have no idea what I'm up against...{w=0.3} and that's what makes them addicting!"
        n 1fcssm "Ehehe.{w=0.2} Don't worry though, [player]."
        n 4fcsbg "I don't know if you're into that kind of stuff as well,{w=0.1} but..."

        if persistent.jn_player_gaming_frequency == "High":
            n 1fchgn "There's still plenty I can teach you!"

            if Natsuki.isEnamored(higher=True):
                n 3ksqsml "And I bet you'd like that too,{w=0.1} huh?"
                n 1nchbg "Ahaha."

            elif Natsuki.isAffectionate(higher=True):
                n 1fchbg "And I'm not gonna take 'No' for an answer!"

        elif persistent.jn_player_gaming_frequency == "Medium":
            n 1fsqsm "I don't mind showing you how it's done."
            n 3fchbg "I {i}am{/i} a professional,{w=0.1} after all!"

        else:
            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                n 3fsqts "Liar.{nw}"

            n 1ullaj "Well then...{w=0.5}{nw}"
            extend 4usqsm " I'm sure I can get {i}you{/i} of all people into it."

    else:
        n 1nnmsl "I suppose I look for challenge in my games more than anything."
        n 2nllsl "It's fun pitting myself against the developers and beating them at their own game."
        n 1nsqaj "I guess I could say I like being tested -{w=0.1} so long as I'm in control of it,{w=0.1} that is."
        n 2fsqbo "What does that mean?{w=0.2} I guess I'll spell it out for you,{w=0.1} [player]."
        n 4fsqan "I really {i}don't{/i} like the kind of testing you're doing."

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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_fang:
    n 1nllbo "..."
    n 4unmaj "Eh?{w=0.2} What's up,{w=0.1} [player]?"
    n 1unmsl "..."
    n 1tnmaj "What?{w=0.2} Is there something on my face?"
    n 1tnmca "..."
    n 4uwdaj "Oh.{w=0.2} Yeah.{w=0.2} I get it."
    n 3nsqss "Just can't help but notice the fang,{w=0.1} right?{w=0.2} Ehehe."
    n 1nllss "You know..."
    n 1nnmaj "I wasn't always happy with my teeth,{w=0.1} [player]."
    n 3flran "I used to be pretty self conscious about them.{w=0.2} People would just keep pointing them out all the time."
    n 1fcsaj "It wasn't...{w=0.3} {i}bad{/i} or anything...{w=0.3} a little annoying at first,{w=0.1} but nothing over the top."
    n 4kslsf "...Mostly."
    n 1ulrsl "But...{w=0.3} I guess I just came to embrace them?"
    n 3fchbg "They're like a trademark or something now!{w=0.2} Which is why I take good care of them."
    n 1fnmsf "You better not be slacking off on yours,{w=0.1} [player]!"
    n 3fnmaj "And I don't just mean skipping the odd brush,{w=0.1} either..."
    n 3fsgss "Yeah.{w=0.2} We both know what's coming,{w=0.2} don't we?"
    n 4fsqbg "When's the last time {i}you{/i} flossed,{w=0.1} [player]?{w=0.2} Be honest."
    n 1tsqsm "..."
    n 1fchbgelg "Ahaha!{w=0.2} Did I call you out?"
    n 1nlrss "Well,{w=0.1} whatever.{w=0.2} I'm just gonna assume you'll go do that later."
    n 4fcsaw "Seriously though.{w=0.2} You better make sure you take care of your teeth!"
    n 1fnmaj "Regular brushing and flossing is important,{w=0.1} but watch your diet too."
    n 3fllsl "Not flossing isn't great,{w=0.1} but constant sugary drinks are even worse!"
    n 1fsgsm "Remember,{w=0.1} [player] -{w=0.1} if you ignore them,{w=0.1} they'll go away~."
    n 1nllss "But no, seriously."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllss "Smiles look good on you,{w=0.1} [chosen_endearment]."
        n 4fnmsm "Let's keep them looking that way."
        n 4uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fnmsml "I think smiles look good on you,{w=0.1} [player]."
        n 4fchbgl "Let's keep them looking that way!"

    elif Natsuki.isAffectionate(higher=True):
        n 1usqbg "The right smile can make all the difference,{w=0.1} you know.{w=0.2} Just look at mine!"
        n 3uchgn "Ehehe."

    else:
        n 1unmaj "If you don't look after them?"
        n 3fllajl "I'm not holding your hand at the dentist!"

    return

# Natsuki responds to the player confessing their love to her
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_i_love_you",
            unlocked=True,
            prompt="I love you, {0}!".format(n_name),
            category=["Natsuki", "Romance"],
            player_says=True,
            location="classroom",
            affinity_range=(jn_affinity.ENAMORED, None)
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_i_love_you:
    # We use these a lot here, so we define them in a higher scope
    $ player_initial = jn_utils.getPlayerInitial()
    $ chosen_tease = jn_utils.getRandomTease()
    $ chosen_endearment = jn_utils.getRandomEndearment()
    $ chosen_descriptor = jn_utils.getRandomDescriptor()

    # De facto confession
    if (
        persistent.affinity >= (jn_affinity.AFF_THRESHOLD_LOVE -1)
        and not persistent._jn_player_confession_accepted
    ):
        n 1uscemf "O-{w=0.1}o-{w=0.1}oh my gosh..."
        n 4uskemf "[player_initial]-{w=0.2}[player]...{w=0.3} y-{w=0.1}you...!"
        n 2fcsanf "Nnnnnnn-!"
        n 1fbkwrf "W-{w=0.1}well it took you long enough!{w=0.2} What did you think you were doing?!"
        n 4flrwrf "I bet you were just waiting for me to say it first!"
        n 4fllemf "Jeez,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
        n 1kllemf "But..."
        n 2fcswrf "B-{w=0.1}but...!"
        n 1flranf "Uuuuuuu-!"
        n 1fchwrf "Oh,{w=0.1} whatever!{w=0.2} I don't care!{w=0.2} I gotta say it!{w=0.2} I gotta say it!"
        n 4kwdemf "[player]!{w=0.2} I love you too!"
        n 4kchbsf "I-{w=0.1}I love...{w=0.3} you too..."
        n 4kplbgf "I...{w=0.3} I..."
        n 1fcsunfsbl "..."

        show natsuki 1kcspuf at jn_center zorder JN_NATSUKI_ZORDER
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5)
        play audio kiss
        show natsuki 1ksrsmfsbr at jn_center zorder JN_NATSUKI_ZORDER
        $ jnPause(1.5)
        hide black with Dissolve(1.25)

        n 1kchsmf "..."
        n 3kwmsmf "I love you,{w=0.3} [player]..."
        n 3kllsml "..."
        n 1kskemf "S-{w=0.1}sorry...!"
        n 4klrunf "I...{w=0.3} think I got a little carried away..."
        n 1kcssmf "..."
        n 1knmajf "..."
        n 2kbkemf "J-{w=0.1}jeez!{w=0.2} Stop looking at me like that already!"
        n 4fllemf "W-{w=0.1}we're both on the same page now,{w=0.1} so..."
        n 4kllbof "...{w=0.3}T-that's all I had."
        n 1kllsmf "..."
        n 1kllssf "S-{w=0.1}so..."
        n 3kplssf "Where were we?{w=0.2} Ehehe..."

        python:
            import datetime

            persistent._jn_player_confession_accepted = True
            persistent._jn_player_confession_day_month = (
                datetime.date.today().day,
                datetime.date.today().month
            )
            persistent.jn_player_love_you_count += 1
            Natsuki.percentageAffinityGain(10)
        return

    # Player has not confessed, and this is the first time they're telling Natsuki this
    elif persistent.jn_player_love_you_count == 0 and not persistent._jn_player_confession_accepted:
        if Natsuki.isEnamored():
            n 1uscgsf "[player_initial]-{w=0.2}[player]!"
            n 2fskgsf "Y-{w=0.1}you...!"
            n 1fcsanf "Nnnnn-!"
            n 1fbkwrf "I-{w=0.1}I know we've been seeing each other a while,{w=0.1} but this is way too sudden!"
            n 3fllwrf "Now you've gone and made it super awkward,{w=0.1} [player]!{w=0.2} Why'd you have to go do that?!"
            n 1fcsemf "Sheesh!"
            n 2fslpof "...I hope you're happy."
            n 1fsqunf "..."
            n 4fnmpof "D-{w=0.1}don't think this means I {i}hate{/i} you or anything,{w=0.1} though..."
            n 2flreml "It's just that...{w=0.3} It's just..."
            n 1fcsanl "Uuuuuu..."
            n 1flrbol "N-{w=0.1}never mind..."
            n 4fcseml "Forget I said anything."
            n 1kllbof "..."
            $ Natsuki.calculatedAffinityGain(base=2, bypass=True)

        elif Natsuki.isAffectionate(higher=True):
            n 1uskwrf "W-{w=0.1}w-{w=0.1}what?"
            n 4fwdwrf "D-{w=0.1}did you just...?"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fbkwrf "[player_initial]-{w=0.2}[player]!"
            n 3fcsemf "Are you trying to give me a heart attack?!{w=0.2} Jeez!"
            n 3fllemf "You can't just say stuff like that so suddenly..."
            n 1kllunf "..."
            n 4fllajf "I-{w=0.1}I mean..."
            n 1flranf "It's not that I {i}don't{/i} like you,{w=0.1} o-{w=0.1}or anything,{w=0.1} but..."
            n 3fslanf "But...!"
            n 1fcsanf "Uuuuu..."
            n 1fcsajf "F-{w=0.1}forget it!{w=0.2} I-{w=0.1}it's nothing..."
            n 1kslslf "..."
            $ Natsuki.calculatedAffinityGain(bypass=True)

        elif Natsuki.isHappy(higher=True):
            n 4fsqdvlesm "Pffffft!"
            n 1uchbslelg "Ahaha!"
            n 1tllbgl "You can't be serious,{w=0.1} [player]!{w=0.2} You're just messing with me!{w=0.2} Right?"
            n 3knmbgl "Right,{w=0.1} [player]?"
            n 4knmajf "R-{w=0.1}right...?"
            n 1fllunf "..."
            n 1fcsgsf "J-{w=0.1}jeez!{w=0.2} Enough of this!"
            n 3fsqajf "You really shouldn't mess around with girls like that,{w=0.1} [player]!"
            n 3fslpul "Y-{w=0.1}you're just lucky I've got a great sense of humor."
            n 4fnmpol "S-{w=0.1}so it's fine...{w=0.3} this time..."
            n 1fcsajl "Just...{w=0.3} think a little before you just blurt stuff out!{w=0.2} Sheesh."
            $ capitalized_tease = chosen_tease.capitalize()
            n 1fllslf "[capitalized_tease]..."

        elif Natsuki.isNormal(higher=True):
            n 1fscgsf "Urk-!"
            n 4fskanf "W-{w=0.1}what did you..."
            n 1fwdanf "Did you just...?"
            n 1fllajl "..."
            n 3fcsbgf "A-{w=0.1}aha!{w=0.2} I mean...{w=0.3} y-{w=0.1}yeah!{w=0.2} Who wouldn't love me,{w=0.1} right?"
            n 3fllbgf "My wit,{w=0.1} my style,{w=0.1} my killer sense of humor...{w=0.3} I've got it all.{w=0.1} Yeah..."
            n 1fbkwrf "D-{w=0.1}don't get the wrong idea or a-{w=0.1}anything, though!"
            n 1fllssf "I-{w=0.1}I mean,{w=0.1} I'm just glad you have some good taste."
            n 2fllunf "Yeah..."

        elif Natsuki.isUpset(higher=True):
            n 1fcsan "..."
            n 4fnmfu "Seriously,{w=0.1} [player]?{w=0.2} You're really going to say that to me {i}now{/i}?"
            n 1fsqfutsb "The first time you choose to say it...{w=0.3} and you say it {i}now{/i}?"
            n 1fcspu "..."
            n 1fwman "...And you really think I'm gonna buy that {i}now{/i},{w=0.1} [player]?"
            n 4fcsfu "..."
            n 1fcssr "..."
            n 2fsqsr "We're done with this."
            n 1fsqpu "And if you {i}really{/i} feel that way?"
            n 2fsqsftsb "...Then why aren't {i}you{/i} trying to make this work,{w=0.1} [player]?"
            $ Natsuki.percentageAffinityLoss(10)

        else:
            # :(
            n 1fsqputsb "..."
            n 2fcsuntsa "Y-{w=0.1}you..."
            n 1fcsantsa "You...{w=0.3} h-{w=0.1}how...!"
            n 4fscwr "H-{w=0.1}how {i}dare{/i} you tell me that now!"
            n 1fscfu "{i}How {w=0.3} dare {w=0.3} you.{/i}"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "You knew how I felt,{w=0.1} [player]..."
            n 2fcsan "You knew for such a long time..."
            n 1fsqfutsb "And now?{w=0.2} {i}Now{/i} is when you tell me?"
            n 4fsquptse "For the {i}first time{/i}?"
            n 1fcsuptsa "..."
            n 1kplan "I...{w=0.3} I c-{w=0.1}can't do this right now."
            n 2kcsantsd "It...{w=0.5} it hurts..."
            n 1kcsfutsd "..."
            n 4fcsputsd "Get out of my sight,{w=0.1} [player]."
            n 1fcsantsd "..."
            n 1fsqfutse "Go!"
            n 4fscsctdc "{i}JUST LEAVE ME ALONE!{/i}{nw}"
            
            $ Natsuki.percentageAffinityLoss(25)
            $ Natsuki.setForceQuitAttempt(False)
            $ persistent.jn_player_love_you_count += 1

            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1

    # Player may or may not have confessed, and Natsuki has been told this before
    else:
        $ persistent.jn_player_love_you_count += 1
        if Natsuki.isLove(higher=True):

            # At this point, Natsuki is super comfortable with her player, so we can be open and vary things!
            $ random_response_index = random.randint(0, 11)

            if random_response_index == 0:
                n 4unmbgf "Ehehe.{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 3uchsmf "You're always [chosen_descriptor] to me."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 1:
                n 1tsqssl "Aww,{w=0.1} you don't say?"
                n 3uchbslelg "Ahaha!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n 1kwmbgf "[chosen_endearment],{w=0.1} I love you too!"
                n 4fcsbgf "I'll always be here to stick up for you."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 2:
                n 1uchsmf "Aww,{w=0.1} [chosen_endearment]!{w=0.2} I love you too!"
                n 4klrbgf "You're the best thing that's ever happened to me."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 3:
                n 1ksqbgf "Oh?{w=0.2} Someone's all needy today,{w=0.1} huh?"
                n 4fsqsmf "Well,{w=0.1} I'd be happy to oblige!"
                n 1uchsmf "I love you too,{w=0.1} [chosen_endearment]!"
                n 3fchbgf "Keep on smiling for me,{w=0.1} 'kay?"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 4:
                n 3flrpof "Fawning over me like always,{w=0.1} [player]?"
                n 1usqssf "Ehehe.{w=0.2} Don't worry,{w=0.1} I'm not complaining!"
                n 4uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 3fcssmf "It's just us two against the world!"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 5:
                n 1fllbgf "Well,{w=0.1} o-{w=0.1}of course you do.{w=0.2} Ahaha!"
                n 4fchbgf "But...{w=0.3} we both know I love you more,{w=0.1} [player]."
                menu:
                    "No, I love you more.":
                        n 1fnmbgf "No,{w=0.1} I-"
                        n 1tllajl "..."
                        n 4fnmawl "H-{w=0.1}hey...{w=0.3} wait a minute...!"
                        n 1fchgnl "I know where we're going with this!{w=0.2} Nice try,{w=0.1} [player]!"
                        n 1fsqsml "You're just gonna have to accept that I love you more,{w=0.1} and that's just the way it is."
                        menu:
                            "You love me more, and that's just the way it is.":
                                n 1uchgnf "Ehehe.{w=0.2} See?"
                                n 3fwmsmf "That wasn't so hard,{w=0.1} was it?"
                                n 1nchbgf "I looooove you,{w=0.1} [player]~!"

                    "Okay.":
                        n 1uchgnlesm "Pfffft!{w=0.2} Ahaha!"
                        n 3fwltsf "Come on,{w=0.1} [player]!{w=0.2} Where's your fighting spirit?"
                        n 1fchsmf "Well,{w=0.1} whatever.{w=0.2} I'm just glad you accept the truth."
                        n 4uchsmf "Ehehe."

                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 6:
                n 1uchsmf "Ehehe...{w=0.3} I always adore hearing that from you,{w=0.1} [player]."
                n 1usqsmf "...And I think I can guess you like hearing it just as much."
                n 3uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 4nchsmf "I don't need anyone else~."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 7:
                n 1nsqajl "Wow,{w=0.1} [player]..."
                n 3tslajl "You really are just a big sappy mess today,{w=0.1} aren't you?"
                n 3tsldvl "Gross..."
                n 1fchbgf "...But just the kind of gross I'm down with.{w=0.2} Ehehe."
                n 4uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1unmsmf "I'll always have your back."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 8:
                n 1uchsmf "Ehehe."
                n 1nchssf "I..."
                n 3uchbsf "Looooooooove you too,{w=0.1} [player]!"
                n 4kwmsmf "You'll always be my rock."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 9:
                n 1fllsmf "I mean...{w=0.3} that's real sweet of you and all,{w=0.1} [player]..."
                n 4fsqsmf "But we both know I love you more~."
                $ player_is_wrong = True
                $ wrong_response_count = 0

                # Natsuki won't lose!
                while player_is_wrong:
                    menu:
                        "No, I love {i}you{/i} more!":

                            if wrong_response_count == 1:
                                n 1fsqbgl "Hmm?{w=0.2} Did you mishear me,{w=0.1} [player]?"
                                n 4fchbgf "I said I love {i}you{/i} more,{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n 1fsqbgl "Oh?{w=0.2} Competitive,{w=0.1} are we?"
                                n 3fslbgl "Ehehe.{w=0.2} Silly [player].{w=0.1} Did nobody ever tell you?"
                                n 3fchgnl "Don't start a fight you can't finish!"
                                n 1fchbgf "Especially this one -{w=0.1} I love {i}you{/i} more~!"

                            elif wrong_response_count == 10:
                                n 3tsqcsl "Oho?{w=0.2} Not bad,{w=0.1} [player]!"
                                n 1fsqbgl "I almost admire your stubbornness..."
                                n 4uchsmf "But not as much as I admire you!{w=0.2} I love {i}you{/i} more!"

                            elif wrong_response_count == 20:
                                n 3fsqbgl "Ehehe.{w=0.2} You're persistent!{w=0.2} I'll give you that."
                                n 1fsqsml "But if you think I'm giving you a win..."
                                n 1fchgnl "Then you've got another thing coming!"
                                n 4uchbgl "I love {i}you{/i} more,{w=0.1} dummy!"

                            elif wrong_response_count == 50:
                                n 1tnmajl "Wow!{w=0.2} This is like...{w=0.3} the 50th time you've been wrong!{w=0.2} In a row!"
                                n 3tsqsgl "Sounds to me like you're in some serious denial there,{w=0.1} [player]~."
                                n 1nllssl "I don't think I can be bothered counting much more from here..."
                                n 3fsqtsl "So why don't you do me a favor and just accept that I love {i}you{/i} more already?"
                                n 1uchsml "Ehehe."
                                n 4fchbgl "Thanks,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n 4uwdgsl "...Oh!{w=0.2} And it looks like we have our 100th wrong answer!"
                                n 3fllawl "Dim the lights!{w=0.2} Roll the music!"
                                n 1flrbgl "Now,{w=0.1} audience members -{w=0.1} what does our stubborn participant get?"
                                n 1fsqbgl "They get..."
                                n 3uchgnl "A correction!{w=0.2} Wow!"
                                n 4fsqbgl "And that correction is..."
                                n 1fchbsf "[n_name] loves {i}them{/i} way more!{w=0.2} Congratulations,{w=0.1} dummy!"
                                n 3fsqdvl "And now,{w=0.1} to walk away with the grand prize -{w=0.1} all our guest here needs to do..."
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
                                    "Wait...{w=0.3} can you hear that?{w=0.2} Oh!{w=0.2} It's how wrong you are -{w=0.1} I love you more,{w=0.1} dummy!",
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
                            n 3tsqbgl "See?{w=0.2} Was that really so hard?"
                            n 1uchtsl "Sometimes you just have to admit you're wrong,{w=0.1} [player]~."
                            n 4nchsml "Ehehe."

                            if wrong_response_count >= 10:
                                n 3nsqsml "Nice try,{w=0.1} though~!"

                            $ Natsuki.calculatedAffinityGain()
                            return

            elif random_response_index == 10:
                n 1ksqsml "Ehehe.{w=0.2} I'll never get tired of hearing that from you,{w=0.1} [player]."
                n 1uchsmf "I love you too!"
                n 3uchbgf "You're my numero uno~."
                $ Natsuki.calculatedAffinityGain()
                return

            else:
                n 4usqbgf "Oh?{w=0.2} Lovey-dovey as usual?"
                n 1uslsmf "You're such a softie,{w=0.1} [player].{w=0.2} Ehehe."
                n 3uchbgf "But...{w=0.3} I'm not gonna complain!{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "You always make me feel tall."
                $ Natsuki.calculatedAffinityGain()
                return

            return

        elif Natsuki.isEnamored(higher=True):
            n 1fbkwrf "G-{w=0.1}gah!{w=0.2} [player]!"
            n 3fllwrf "What did I say about making things awkward?{w=0.2} Now it's twice as awkward!"
            n 1fcsemf "Jeez..."
            n 1flremf "Let's just talk about something,{w=0.1} alright?"
            n 4flrpof "Y-{w=0.1}you can fawn over me in your {i}own{/i} time!"
            n 4klrpof "Dummy..."
            $ Natsuki.calculatedAffinityGain()
            return

        elif Natsuki.isHappy(higher=True):
            n 1fskemf "H-{w=0.1}hey! I thought I told you not to just come out with stuff like that!"
            n 2fllemf "Jeez..."
            n 1fcsemf "I-{w=0.1}I don't know if you're trying to win me over,{w=0.1} or what..."
            n 2fcspof "But you're gonna have to try a lot harder than that!"
            return

        elif Natsuki.isNormal(higher=True):
            n 1fskemf "G-{w=0.1}gah!"
            n 4fbkwrf "[player_initial]-{w=0.1}[player]!"
            n 1fnmanl "Stop being gross!"
            n 2fcsanl "Jeez..."
            n 1fllajl "I don't know if you think this is a joke,{w=0.1} or what..."
            n 2fsqaj "But it really isn't funny to me,{w=0.1} [player]."
            return

        elif Natsuki.isUpset(higher=True):
            n 1fcssr "..."
            n 1fsqsr "Talk is cheap,{w=0.1} [player]."
            n 1fsqaj "If you {i}really{/i} care about me..."
            n 2fsqpu "Then {i}prove{/i} it."
            $ Natsuki.percentageAffinityLoss(2.5)
            return

        else:
            n 1fsqpu "..."
            n 1fsqan "You're actually unbelievable,{w=0.1} [player]."
            n 2fsqfu "Do you even {i}understand{/i} what you're saying?"
            n 1fcsfu "..."
            n 1fcspu "You know what?{w=0.2} Whatever.{w=0.2} I don't care anymore."
            n 4fsqfu "Say what you like,{w=0.1} [player].{w=0.2} It's all crap,{w=0.1} just like everything else from you."
            $ Natsuki.percentageAffinityLoss(2)
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
    if Natsuki.isEnamored(higher=True):
        n 4tnmaj "Hmm?{w=0.2} My hairstyle?"
        n 3fsqss "Why do you ask,{w=0.1} [player]?{w=0.5}{nw}"
        extend 3fsgsg " Looking for a stylist?"
        n 1fchsm "Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 4tnmpu "Huh?{w=0.2} My hairstyle?"
        n 1fsqaj "Wait...{w=0.75}{nw}"
        extend 4fnmeml " a-{w=0.1}are you messing with me?{w=0.2} What do you mean?"
        n 3fslpo "You better not be teasing me,{w=0.1} [player]..."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "...Huh?{w=0.2} Oh.{w=0.2} My hair."
        n 2flrsl "I'm...{w=0.3} surprised you care enough to ask about that."

    else:
        n 1fsqfu "Because I {i}like{/i} it that way.{w=0.75}{nw}"
        extend 2fnman " That good enough for you,{w=0.3} {i}[player]{/i}?"
        n 1fsqantsb "And why would you even {i}care{/i} anyway?{w=1}{nw}"
        extend 4fsqupltsb " You haven't cared about me so far."
        n 2fcsanltsa "Jerk."
        return

    n 1nnmpu "Well,{w=0.1} anyway."
    n 4ullpu "I never really thought about it that much,{w=0.1} honestly."

    if Natsuki.isNormal(higher=True):
        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 2ulrpo "I just thought twintails would look kinda cute on me."

        else:
            n 2ulrpo "I think this hairstyle looks kinda cute on me."

        n 4fsqpo "...Yeah,{w=0.1} yeah.{w=0.2} I know what you're thinking,{w=0.1} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1ksqsm "Was I wrong...?"
            n 1fchbg "Ehehe.{w=0.2} I thought not."

        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 1ullaj "Besides,{w=0.1} I had a whole bunch of ribbon lying around from my craft stuff {w=0.1}-{w=0.5}{nw}"
            extend 3fcsbg " so it isn't like I had to go {i}buy{/i} anything new to try twintails out."

    else:
        if Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_long") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
            n 1nnmsl "I guess I just liked the idea of twintails."
            n 1nlrpu "Besides,{w=0.1} I had some spare ribbons lying around anyways.{w=0.5}{nw}"
            extend 4nsrsr " Not like I had to {i}buy{/i} anything to try doing twintails."

        else:
            n 1nnmsl "I guess I just like this hairstyle."

    n 1ulraj "As for the bangs,{w=0.1} I...{w=0.3} always found it difficult to get my hair cut."

    if Natsuki.isNormal(higher=True):
        n 4flraj "It just costs so much,{w=0.1} you know?{w=0.2} It's super dumb!"
        n 1fnman "Like...{w=0.3} I don't get it at all!"
        n 3fllan "And the annoying thing is that if I were a guy,{w=0.1} it'd be {i}way{/i} cheaper!{w=0.5}{nw}"
        extend 1fbkwrean " What's up with that?!"
        n 1fcspuesi "Ugh...{w=1}{nw}"
        extend 2nsrpo " but yeah."

    else:
        n 1nlrsl "I was always kinda short when it came to getting it cut."
        n 1fsqsl "...And no,{w=0.1} {i}not{/i} in the physical sense."

    if Natsuki.isWearingAccessory(jn_outfits.getWearable("jn_accessory_hairband_red")):
        n 4ullaj "As for my hairband?{w=0.2} It's just to keep my hair out of my eyes."

    else:
        n 4ullaj "I'm not wearing it now,{w=0.1} but my old hairband was just to keep my hair out of my eyes."

    if Natsuki.isNormal(higher=True):
        n 3fllss "Looking good is a bonus,{w=0.1} but I mostly just got tired of brushing my hair out of my face."
        n 1nsrca "Especially with those bangs!"
        n 1unmaj "Anyway..."

    n 4tllaj "Have I thought about other hairstyles?{w=0.2} Well..."

    if not Natsuki.isWearingHairstyle("jn_hair_twintails") or Natsuki.isWearingHairstyle("jn_hair_twintails_white_ribbons"):
        if Natsuki.isEnamored(higher=True):
            n 1tsqsml "Is that not what I'm doing right now?"
            extend 1fchsml " Ehehe."

        elif Natsuki.isNormal(higher=True):
            n 1ullbo "I think that kinda speaks for itself,{w=0.1} really.{w=0.2} I {i}am{/i} trying out a different one..."

        else:
            n 2nsqsl "...Go figure,{w=0.1} [player]."

    else:
        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcssml "I'm pretty sure I already let my hair down around you,{w=0.1} [chosen_tease].{w=0.2} That qualifies, right?"
            n 3uchgnlelg "Ahaha!"

        elif Natsuki.isNormal(higher=True):
            n 1unmaj "You know what they say,{w=0.1} [player]."
            n 3fnmbg "If it ain't broke,{w=0.1} don't fix it!"
            n 1uchgn "Ehehe."

        else:
            n 2fslaj "...At this point,{w=0.1} [player]?{w=0.2} I'd rather you stayed {i}out{/i} of my hair."
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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_integrity:
    n 4ullaj "You know,{w=0.1} [player]..."
    n 1nnmaj "I feel like nowadays,{w=0.1} everyone is trying to make a point,{w=0.1} or preach something."
    n 2flrem "Especially with social media and all that everywhere -{w=0.1} it's crazy!"
    n 2fllem "Like...{w=0.3} there's posts telling you this is bad,{w=0.1} others asking why you don't support something else..."
    n 1fcsan "And of course,{w=0.1} {i}everyone{/i} is tuned in to that -{w=0.1} so it leaks into real life as well!"
    n 1flrsl "Ugh...{w=0.3} it can't only be me that finds it all exhausting,{w=0.1} right?"
    n 1unmaj "I think it makes it kinda easy to lose track of what you really like,{w=0.1} or what you stand for."
    n 4ullaj "Which...{w=0.3} is actually something I really wanted to talk to you about,{w=0.1} [player]."
    n 1fllpu "I'm not saying you should just ignore everyone else,{w=0.1} or never consider other points of view."
    n 3fnmpo "That's just being ignorant."
    n 1knmaj "But...{w=0.3} don't just let other people's opinions or conceptions completely overwrite your own,{w=0.1} 'kay?"
    n 4fnmbo "At least not without a fight,{w=0.1} at least."
    n 1fnmpu "{i}You{/i} are your own master,{w=0.1} [player] -{w=0.1} you have your own opinions,{w=0.1} your own values:{w=0.1} and that's super important!"
    n 1fcsbg "I mean,{w=0.1} look at me!"
    n 1fllaj "So what if someone says what I'm into sucks?{w=0.2} Or if I should be following something more popular?"
    n 1fnmsf "It isn't hurting anyone,{w=0.1} so who are they to judge and tell me what I should be enjoying?"
    n 3fcsbg "It's my life,{w=0.1} so they can jog on!"
    n 1nnmsr "Anyway...{w=0.3} I guess what I'm saying is don't be afraid to stand up for what matters to you,{w=0.1} [player]."
    n 1fcsaj "There's gonna be times you'll be wrong,{w=0.1} but don't let it get to you!"
    n 1flrsl "I just don't like the idea of people being pushed into what isn't right for them."
    n 4nnmpu "That being said,{w=0.1} [player]..."

    if Natsuki.isEnamored(higher=True):
        n 1ksqsm "I'm pretty sure we both know what's right for each other by now,{w=0.1} huh?"
        n 3fcsbglesssbl "Ahaha."

        if Natsuki.isLove(higher=True):
            n 4uchsml "Love you,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1ksqsm "I'm pretty sure I know what's right for you..."
        n 3fcsbgledz "Spending more time with me!"
        extend 4nchgnedz " Ehehe."

    else:
        n 1unmss "I'm sure I can help you find what's right for you."
        n 1fllss "That's what friends are for,{w=0.1} right?"
        n 3fcsbg "{i}Especially{/i} ones like me!{w=0.5}{nw}"
        extend 4nchgnedz " Ehehe."

    return

# Natsuki discusses her favourite animal
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_animal",
            unlocked=True,
            prompt="What's your favorite animal?",
            category=["Animals", "Nature"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_animal:
    if Natsuki.isNormal(higher=True):
        n 1fsqsr "Hammies."
        n 3fcssm "That's barely even a question for me,{w=0.1} [player]."
        n 1uwdaj "Like...{w=0.3} if you've seen them,{w=0.1} can you blame me?"
        n 1fcspu "They're...{w=0.5}{nw}"
        n 4fspgsedz "{i}Adorable{/i}!!"
        n 1fbkbsl "I just love everything about them...{w=0.3} the little paws,{w=0.1} the bright eyes, those puffy cheeks..."
        n 4fspbgl "And that tiny little tail...{w=0.3} oh my gosh!{w=0.2} It's just precious!"
        n 2fllan "It really winds me up when people call them boring,{w=0.1} or unaffectionate though.{w=0.2} Like...{w=0.3} have you ever watched one?"
        n 1fnmaj "They all have their own little personalities,{w=0.1} just like any other animal -{w=0.1} only smaller!"
        n 1uwdaj "And if you bond with them,{w=0.1} they aren't afraid to show it -{w=0.1} I've seen videos of them following their owners around,{w=0.1} and even leaping into their hands!"
        n 4fchbg "Plus they're easy to take care of,{w=0.1} too!"
        n 1fchsm "Just top up their food and change their water daily,{w=0.1} and clean their cage out once a week -{w=0.1} no sweat."
        n 4nllpu "Hmm..."
        n 1unmpu "You know,{w=0.1} [player]...{w=0.3} it does get a little quiet when you aren't around,{w=0.1} if you know what I'm getting at..."
        n 3fnmsm "Perhaps one day we could have our own furry friend here too?{w=0.1} Ehehe."
        n 1fllss "Don't worry though,{w=0.1} [player]..."
        n 1ucssm "I don't mind taking care of it."
        n 3fchgn "...But you're in charge of the supplies!"

        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Oh,{w=0.1} and relax -{w=0.1} I'll make sure it'll be well tamed!"
            n 1uslbg "Or..."
            n 3usqts "At least about as tame as you,{w=0.1} huh [player]?{w=0.2} Ahaha!"

            if Natsuki.isLove(higher=True):
                n 4uchbg "Love you~!"

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "Hamsters,{w=0.1} if it matters."
        n 2fllpu "Why?{w=0.2} I don't know.{w=0.2} I just think they're cute."
        n 1nllbo "I think people actually underestimate how expressive they can be,{w=0.1} too."
        n 1nnmbo "They're like most animals really -{w=0.1} they all have their own personalities."
        n 1nnmaj "I guess they're pretty easy to take care of as well,{w=0.1} so there's that."
        n 1nlrsl "..."
        n 2flrsl "...I'd be lying if I said I hadn't been thinking about getting one myself..."
        n 1fsqpu "But honestly,{w=0.1} [player]?{w=0.2} If you've shown you can't take care of {i}me{/i}?"
        n 2fcsan "...Then I don't think it'd be fair to bring one here,{w=0.1} either.{w=0.2} Heh."

    else:
        n 1fsqpu "Heh.{w=0.2} Really?{w=0.2} My favorite animal...?"
        n 2fcsantsa "Not you,{w=0.1} [player].{w=0.2} That's for sure."

    return

# Natsuki discusses her favourite drink
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_drink",
            unlocked=True,
            prompt="What's your favorite drink?",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_drink:
    if Natsuki.isAffectionate(higher=True):
        n 1unmbg "Ooooh!{w=0.2} My favorite drink?"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Mmm?{w=0.2} My favorite drink?"

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "Huh?{w=0.2} Oh.{w=0.1} My favorite drink."

    else:
        n 2fslsf "...I can't understand why you'd care,{w=0.1} [player]."
        n 1fsqsf "So...{w=0.3} why should I?"
        n 2fsqan "Water.{w=0.2} There's an answer for you.{w=0.2} Happy?"
        n 2fcsanltsa "Now just go away..."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "I gotta say...{w=0.3} it depends on the weather more than anything."
        n 3tnmaj "I mean...{w=0.3} what kind of dope would order an iced drink in the middle of winter?!"
        n 1fllss "But anyway..."
        n 1fcsbg "If it's cold out,{w=0.1} then hot chocolate.{w=0.2} No questions,{w=0.1} no doubts."
        n 4uchgn "In the depths of winter,{w=0.1} you definitely won't get a better option than that!"

        if Natsuki.isAffectionate(higher=True):
            n 1fcsbg "And yeah,{w=0.1} [player] -{w=0.1} whipped cream,{w=0.1} marshmallows -{w=0.1} all of it.{w=0.2} The complete works."
            n 1uchgn "...And I wouldn't accept anything less!"
            n 3fllbg "I mean,{w=0.1} think about it -{w=0.1} if you're getting hot chocolate,{w=0.1} you've already kinda lost on the health front."
            n 3uchgn "So you might as well go all in,{w=0.1} right?{w=0.2} Ahaha."

            if Natsuki.isLove(higher=True):
                n 4fcsdvl "Besides,{w=0.2} I'm not too worried -{w=0.1} we'll just share the calories,{w=0.1} [player]~."

        n 1unmaj "As for warmer weather...{w=0.3} that's a little trickier,{w=0.1} actually."
        n 3fslsr "Let me think..."
        n 3fsrsr "..."
        n 1fchbs "Aha!{w=0.2} I got it!"
        n 1unmbg "It's gotta be those milkshakes,{w=0.1} but from one of those places where you get to choose what goes in it!"
        n 1fsqsm "I don't just mean picking a flavor,{w=0.1} [player]..."
        n 4fchgn "I mean where you can pick any combination of ingredients you want!"
        n 1fllss "Well...{w=0.3} as long as it blends,{w=0.1} anyway."
        n 1ncssm "All kinds of sweets,{w=0.1} any type of milk..."

        if Natsuki.isAffectionate(higher=True):
            n 1ucssm "Though if I had to pick a favorite?"
            n 3fcsbg "It's gotta be strawberries and cream,{w=0.1} obviously."
            n 3fllbgl "And...{w=0.3} maybe with just a dash of chocolate too?{w=0.2} Ehehe."

        else:
            n 1fchbg "Yeah.{w=0.2} That's the real deal!"

        n 3fllpo "Jeez...{w=0.3} all this talk about drinks is making me kinda thirsty,{w=0.1} actually.{w=0.2} So on that note..."
        n 1fnmbg "You need to stay hydrated too,{w=0.1} [player] -{w=0.1} whatever the weather!"

    else:
        n 1flrsl "I suppose it depends what the weather is like."
        n 2fnmbo "Hot chocolate if it's cold out,{w=0.1} though I'm not very picky I guess."
        n 1fllaj "As for warmer weather..."
        n 1fllsl "I don't really know.{w=0.2} Whatever is fine."
        n 2fsqsl "Heh.{w=0.2} Though at this rate,{w=0.1} I shouldn't expect much more than tap water from you anyway.{w=0.2} Right,{w=0.1} [player]?"

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
    if Natsuki.isLove(higher=True):
        n 4fsqcsl "Oho?{w=0.2} Does [player] like a girl in uniform?"
        n 1ksqaj "Wow...{w=0.3} you're even {i}more{/i} gross than I thought."
        n 1fsqsm "..."
        $ chosen_tease = jn_utils.getRandomTease()
        n 3uchgn "Oh come on,{w=0.1} [chosen_tease]!{w=0.2} You always get all sulky when I call you that!{w=0.2} I just can't resist."
        n 1fchsm "Ehehe.{w=0.2} So anyway..."

    elif Natsuki.isAffectionate(higher=True):
        n 4unmaj "Huh?{w=0.2} My school uniform?"
        n 1fsqsm "...Ehehe."
        n 3fcsbgl "Why do you ask,{w=0.1} [player]?{w=0.2} Did {i}you{/i} wanna wear it or something?"
        n 1fchgn "Oh!{w=0.2} We can play dress-up!{w=0.2} Wouldn't you like that,{w=0.1} [player]?{w=0.2} It'll be so much fun!"
        n 4uchbselg "I bet I could make you look so cute~.{w=0.1} Ahaha!"
        n 1nllss "Well anyway,{w=0.1} putting jokes aside..."

    elif Natsuki.isNormal(higher=True):
        n 4tnmaj "My school uniform?{w=0.2} That's...{w=0.3} kind of a weird thing to ask me about,{w=0.1} huh?"
        n 1nslaj "Well,{w=0.1} whatever.{w=0.2} I'll let it slide...{w=0.3} this time."

    elif Natsuki.isDistressed(higher=True):
        n 2nsraj "...Huh?{w=0.2} Oh,{w=0.1} the school uniform."
        n 1nsqsl "I...{w=0.3} don't know what you're expecting to hear from me,{w=0.1} [player]."
        n 1fsqsl "I had to wear it for school.{w=0.2} That's the point of a uniform,{w=0.1} if you hadn't realized."
        n 2fsrsf "It doesn't matter if I like it or not."
        n 4fsqbo "...And it matters even less if you do."
        return

    else:
        n 2fsran "Heh.{w=0.2} I like it more than {i}you{/i}.{w=0.2} Jerk."
        return

    n 1unmaj "It's alright,{w=0.1} I guess.{w=0.2} I actually really like the warm colors!"
    n 1nnmss "They're way easier on the eyes than a lot of the other uniforms I've seen around."
    n 2nsqsr "But Oh.{w=0.2} My.{w=0.2} Gosh.{w=0.2} [player]."
    n 1fcsan "The layers.{w=0.2} So many layers."
    n 4fllem "Who even thought someone needs that much clothing?!{w=0.2} For school,{w=0.1} of all places?!"
    n 1fbkwr "I mean...{w=0.3} do you even {i}know{/i} what wearing all that clothing in summer is like?!{w=0.2} It's {i}horrible{/i}!"
    n 2flrpo "And the blazer...{w=0.3} ugh!{w=0.2} It's actually the worst thing ever."
    n 2fsqpo "Like yeah,{w=0.1} I could take some off between class,{w=0.1} but I had to put it all back on when I went in."
    n 2fllpo "...Or get told off.{w=0.2} {i}Again{/i}.{w=0.2} I honestly have no idea how Sayori got away with hers being so scruffy."
    n 1fcsan "And all of the uniform stuff is super expensive too!{w=0.2} Talk about a kick in the teeth!"
    n 4fslan "Jerks."
    n 1fslsr "Ugh...{w=0.3} I seriously wish uniforms were banned or something."
    n 3flrpo "I guess it could be worse.{w=0.5}{nw}"
    extend 1ksrsl  " At least it kept me warm when it mattered."

    if not Natsuki.isWearingClothes("jn_clothes_school_uniform"):
        n 1nchgn "...And I'm not wearing it now,{w=0.1} at least!{w=1}{nw}"
        extend 3fcsbg " Always a plus."
        n 1ullaj "That being said...{w=0.75}{nw}"

    else:
        n 1ulraj "But...{w=0.75}{nw}"

    extend 4unmbo " what about you,{w=0.1} [player]?"
    show natsuki 1tnmpu at jn_center

    menu:
        n "Did you have to wear any uniform at school?"

        "Yes, I had to wear uniform.":
            n 3fcsbg "Aha!{w=0.2} So you know the struggle too,{w=0.1} huh?"

        "No, I didn't have to wear uniform.":
            n 1fslsr "..."
            n 3fsqsr "...Lucky."

        "I have to wear uniform now.":
            n 1fchgn "Then you have my condolences,{w=0.1} [player]!{w=0.2} Ahaha."
            n 4fcsbg "Good to know we're on the same page,{w=0.1} though."

        "I don't have to wear uniform now.":
            n 1fslsr "..."
            n 3fsqsr "...Lucky."

    n 1ullss "Well,{w=0.1} anyway..."

    if Natsuki.isLove(higher=True):
        n 1fllss "I still don't particularly {i}like{/i} wearing it..."
        n 3uslbgl "But...{w=0.3} I think I can put up with it.{w=0.2} Just for you,{w=0.1} [player]~."
        n 1usrdvl "Ehehe."

    elif Natsuki.isAffectionate(higher=True):
        n 4usrdvl "I-{w=0.1}if you don't mind it,{w=0.1} [player]?"
        n 1fllbgl "I suppose it has that going for it too,{w=0.1} a-{w=0.1}at least..."

    elif Natsuki.isNormal(higher=True):
        n 1fcsbg "I guess at least I never had to learn how to do a tie!"
        extend 1nchgn " Ehehe."

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
    if Natsuki.isEnamored(higher=True):
        n 4uwdaj "Ooh!{w=0.2} Flying?{w=0.2} Like on a plane?"
        n 3fllun "Nnn...{w=0.3} I wish I could say I have,{w=0.1} [player]..."
        n 1fchbg "Don't get me wrong though!{w=0.2} I'd {i}totally{/i} fly somewhere new if I could!"
        n 4fslsl "It's just...{w=0.3} the price of it all,{w=0.1} you know?"
        n 4kllsl "I've never had a passport,{w=0.1} but it's mainly the tickets and everything beyond that..."

    elif Natsuki.isHappy(higher=True):
        n 4unmaj "Huh?{w=0.2} Flying?{w=0.2} Like on a plane or something?"
        n 1kllaj "I...{w=0.3} wish I could say I have,{w=0.1} [player]."
        n 1fnmbg "Don't get me wrong though!{w=0.2} I'd love to jet off somewhere.{w=0.2} Like for a vacation or something!"
        n 2flrpo "It's just the cost that stops me, you know?"
        n 2fcspo "Even if I had a passport, there's just so many things to pay out for..."

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Oh?{w=0.2} Like flying on a plane or whatever?"
        n 1kllbo "Uhmm..."
        n 2klraj "I...{w=0.3} never really had the opportunity to fly anywhere,{w=0.1} [player]."
        n 1unmaj "I don't even have a passport or anything like that,{w=0.1} and even if I did?"
        n 2nsraj "It isn't like tickets are...{w=0.3} affordable,{w=0.1} if you know what I mean?"
        n 2nslpo "Especially to someone in my...{w=0.3} position."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmbo "Flying?{w=0.2} Like...{w=0.3} on a plane?"
        n 2fnmsf "No,{w=0.1} [player].{w=0.2} I haven't."
        n 1fllsf "I've never owned a passport,{w=0.1} and it's way too expensive anyway."
        n 1fnmaj "I don't really like the idea of the environmental impact either."
        n 2fsqaj "...But something tells me you don't really care about that last point,{w=0.2} do you?"
        n 1flrca "You know...{w=0.3} just going by my experience so far."
        n 2fsqca "...Am I {i}wrong{/i}?"
        return

    else:
        n 2fsqanean "No,{w=0.1} [player].{w=0.2} I haven't.{w=0.2} And I probably never will."
        n 1fcsanltsa "Gloat all you want.{w=0.2} I don't give a crap if you have."
        return

    n 1ullaj "Besides,{w=0.1} I try not to feel too bad about it.{w=0.2} It's way better for the environment if I don't,{w=0.1} anyway!"
    n 1nnmbo "Flying places is pretty polluting.{w=0.2} I think I'd just feel selfish if I was constantly zooming around,{w=0.1} knowing how bad that is for everyone."
    n 1nllss "But...{w=0.3} that's just me,{w=0.1} I guess."
    n 4unmaj "What about you,{w=0.1} [player]?"
    menu:
        n "Are you a frequent flier?"

        "Yes, I fly regularly.":
            n 1fcsbg "Oh?{w=0.2} Well check you out,{w=0.1} [player]!"
            n 3fslpo "I guess it's {i}plane{/i} to see how well you're doing for yourself?"
            n 1fchbg "Ehehe."
            n 1fnmaj "Just try to avoid racking up too many miles,{w=0.1} [player]."
            n 4fllss "You gotta think about the planet too,{w=0.1} you know..."

            if Natsuki.isEnamored(higher=True):
                n 4fslnvf "E-{w=0.1}especially if people we really care about are in it.{w=0.2} Ahaha..."

            elif Natsuki.isHappy(higher=True):
                n 1fchgn "No excuses,{w=0.1} [player]! Ehehe."

            $ persistent._jn_player_has_flown = True

        "I fly sometimes.":
            n 1unmss "Ooh,{w=0.1} okay!{w=0.2} So the odd vacation or family flight then?"
            n 2fslsm "I see,{w=0.1} I see..."
            n 1fcsbg "Well,{w=0.1} good for you,{w=0.1} [player]!{w=0.2} Everyone should get the chance to explore the world."
            n 4kslss "Hopefully I'll get the chance someday too."

            if Natsuki.isEnamored(higher=True):
                n 1fsqsg "I hope you'll be available when that happens,{w=0.1} [player]."
                n 3fchgnl "You're gonna be my tour guide,{w=0.1} whether you like it or not!"

            elif Natsuki.isHappy(higher=True):
                n 1fsqsm "You better be handy when that happens,{w=0.1} [player]..."
                n 4fchgn "We'll see how good a guide you are!"

            $ persistent._jn_player_has_flown = True

        "I've flown before.":
            n 4fsqct "Oh?{w=0.2} So you've already earned your wings,{w=0.1} huh?"
            n 1tllaj "Hmm...{w=0.3} I wonder where you went?"
            n 1fnmaj "You gotta promise to tell me if you fly again,{w=0.1} 'kay?"
            n 3fchgn "I wanna hear all about it!"

            $ persistent._jn_player_has_flown = True

        "I've never flown.":
            n 1fcsbg "Then that's just another thing we have in common,{w=0.1} [player]!"
            n 1fsqss "I guess you could say..."
            n 4fsqdv "We're both just {i}well grounded{/i} people,{w=0.1} huh?"
            n 3fchgnelg "Ahaha!"

            $ persistent._jn_player_has_flown = False

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
        if Natsuki.isNormal(higher=True):
            n 4unmaj "Eh?{w=0.2} Cars?"
            n 1fchgn "Jeez,{w=0.1} you know I can't drive,{w=0.1} dummy!{w=0.2} I don't have a reason to be into cars!"
            n 3nlrbg "Well,{w=0.1} anyway..."

        elif Natsuki.isDistressed(higher=True):
            n 1fcssl "[player].{w=0.2} You know I can't drive.{w=0.2} Why would you think I'd be into cars,{w=0.1} of all things?"
            n 2fllsl "...Fine.{w=0.2} Whatever."

        else:
            n 1fsqpu "...Really?"
            n 2fsqan "You know I can't drive.{w=0.2} So I'm not even going to {i}pretend{/i} I care if you're into that,{w=0.1} [player]."
            n 1fnmfultsc "Besides...{w=0.3} I bet you'd {i}never{/i} treat your {i}precious{/i} car like you treat me,{w=0.1} huh?"
            return

    else:
        # Natsuki hasn't stated she can't drive before
        if Natsuki.isNormal(higher=True):
            n 4unmaj "Huh?{w=0.1} Am I into cars?"
            n 2fllnv "Well...{w=0.3} to tell you the truth,{w=0.1} [player]?"
            n 1unmaj "...I've never actually owned a license."
            n 3flrpo "I don't even think I could afford to learn!"
            n 1nnmaj "So I've never really been drawn to them honestly."

        elif Natsuki.isDistressed(higher=True):
            n 1fnmsr "I can't drive,{w=0.1} [player].{w=0.2} I don't have a license either;{w=0.1} learning was always too expensive."
            n 2fnmpu "So...{w=0.3} why would I be into that?{w=0.1} I literally can't {i}afford{/i} to be."

        else:
            n 1fcsan "Newsflash,{w=0.1} jerk.{w=0.2} I {i}can't{/i} drive,{w=0.1} and I can't even afford to {i}learn{/i}."
            n 2fsqan "So you tell {i}me{/i} -{w=0.1} why would I be into cars?{w=0.2} And if I was,{w=0.1} why the hell would I want to talk to {i}you{/i} about them?"
            n 1fcspu "...Heh.{w=0.2} Yeah,{w=0.1} I thought so.{w=0.2} We're done here,{w=0.1} [player]."
            return

    if Natsuki.isNormal(higher=True):
        n 1unmsm "I can appreciate the talent that goes into them -{w=0.1} I think it's actually pretty cool how expressive they can be!"
        n 1nllss "Like...{w=0.3} the design languages of all the different brands,{w=0.1} the engineering that goes into them and all that."
        n 1fchbg "It's pretty insane how much work goes into it;{w=0.1} and that's definitely something I have respect for!"
        n 2fsqsm "What about you though, [player]?{w=0.2} You {i}did{/i} bring it up,{w=0.1} but I thought I'd ask anyway..."
        menu:
            n "Are you into cars?"

            "Yes! I'm into my cars.":

                # The player has never stated if they can drive
                if persistent.jn_player_can_drive is None:
                    n 1tllbo "Huh.{w=0.2} I wasn't actually sure if you could even drive,{w=0.1} but I suppose that doesn't matter really."
                    n 3fsqsm "I guess being a petrolhead isn't an exclusive club,{w=0.1} huh?"
                    n 1uchbg "Ahaha."

                # The player has confirmed they can drive
                elif persistent.jn_player_can_drive:
                    n 4fsgbg "Well,{w=0.1} color {i}me{/i} surprised."
                    n 1fchgn "Ehehe."
                    n 1fcsbg "Don't worry,{w=0.1} I had you figured for the sort,{w=0.2} [player]."
                    n 3fchbg "But hey -{w=0.1} whatever floats your boat!"

                # The player has admitted they cannot drive
                else:
                    n 1unmaj "That's...{w=0.3} actually pretty surprising to hear from you,{w=0.1} [player]."
                    n 1nllaj "You know,{w=0.1} since you said you can't drive and all that..."
                    n 3fchbg "But I guess it's like anything -{w=0.1} you don't have to be doing it to be a fan,{w=0.1} and that's fine with me!"

            "I don't care much for them.":
                n 1ullss "I guess that's fair enough -{w=0.1} and don't worry,{w=0.1} I completely get it."
                n 4nnmsm "But if someone's into that kind of thing,{w=0.1} who are we to judge,{w=0.1} after all?"

            "No, I'm not into them.":
                n 1ulraj "...Huh.{w=0.2} That's kinda weird -{w=0.1} then why did you bring it up,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n 4tlraj "Especially if you can drive!"
                    n 1tllpu "Huh..."

                n 3fchbg "Well,{w=0.1} anyway.{w=0.2} Fair enough I guess!"

    else:
        n 2flrsr "I guess I can respect the work and talent that goes into designing and making one..."
        n 1fnmbo "But it's just the same as anything else."
        n 1fsqbo "...I suppose you're into your cars then,{w=0.1} are you?"
        n 1fcspu "Heh."
        n 2fsqpu "It'd be nice if you extended that respect to {i}people{/i} too,{w=0.1} [player]."
        n 4fsqsr "{i}Just saying.{/i}"

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
    if Natsuki.isLove(higher=True):

        if persistent.jn_player_love_you_count > 0:
            n 3kwmpof "[player]...{w=0.3} isn't it obvious? You know I love you already,{w=0.1} right?"
            n 3fllpol "Jeez...{w=0.3} you really are a dork sometimes,{w=0.1} you know."
            n 1kllssl "But...{w=0.3} I kinda like that silly part of you,{w=0.1} [player]."
            n 1nwmbgl "Never change,{w=0.1} 'kay? Ehehe."
            n 4nchbgl "Love you,{w=0.1} [player]~!"

        else:
            n 1fcsanf "Nnnnnnn-!"
            n 4fnmanf "C-{w=0.1}come on! Isn't it obvious by now? Jeez...{w=0.5}{nw}"
            n 2fllpof "Do I really have to spell it out for you,{w=0.1} [player]?"
            n 1fcspolesi "Ugh...{w=0.5}{nw}"
            n 1fsqssl "Heh.{w=0.2} Actually,{w=0.1} you know what?"
            n 4fsqbgl "I'll let you figure it out."
            n 1fslajl "And no,{w=0.1} before you ask -{w=0.1} you've had enough hints already."
            n 2fllpol "Dummy..."

        return

    elif Natsuki.isEnamored(higher=True):
        n 1fcsanf "Uuuuuu-!"
        n 4fskwrf "A-{w=0.1}are you trying to put me on the spot or something,{w=0.1} [player]?"
        n 2fllemf "Jeez...{w=0.5}{nw}"
        n 1fcseml "You should {i}know{/i} what I think of you by now...{w=0.5}{nw}"
        n 2fllpol "...{w=0.5}{nw}"
        n 2kcspol "...{w=0.3}Fine."
        n 4fcspol "I...{w=0.3} like...{w=0.3} you,{w=0.1} [player].{w=0.2} A bunch."
        n 1fbkwrf "T-{w=0.1}there!{w=0.2} Happy now?!"
        n 4kllsrl "Sheesh..."
        return

    elif Natsuki.isAffectionate(higher=True):
        n 1fskemf "H-{w=0.1}huh? How do I feel about you?"
        n 4fbkwrf "W-{w=0.1}what're you asking me about that for?!"
        n 2fllpol "Sheesh,{w=0.1} [player]...{w=0.3} you'll make things all awkward at this rate..."
        n 1fcseml "You're fine,{w=0.1} so you don't need to keep bugging me about it!"
        n 4flrunl "Jeez..."
        return

    elif Natsuki.isHappy(higher=True):
        n 1uskemf "H-huh?!"
        n 2fllbgl "O-oh! Ahaha..."
        n 1nllaj "Well,{w=0.1} I mean...{w=0.5}{nw}"
        n 1ullaj "You're pretty fun to be with,{w=0.1} all things considered."
        n 4fllnvl "So...{w=0.3} yeah...."
        return

    elif Natsuki.isNormal(higher=True):
        n 1uskeml "H-{w=0.1}huh?!"
        n 1fllbg "O-oh!"
        n 4unmaj "I mean...{w=0.3} you're alright...{w=0.3} I guess?"

        if not persistent.jn_player_first_farewell_response:
            n 1flleml "W-{w=0.1}what did you expect?{w=0.5}{nw}"
            extend 2fnmpol " We've {i}literally{/i} just met!"

        n 1nnmpu "That's about all I can say so far,{w=0.1} so...{w=0.3} yeah."
        n 1nllca "...{w=0.5}{nw}"
        n 4nlraj "So...{w=0.3} where were we?"
        return

    elif Natsuki.isUpset(higher=True):
        n 2fsqaj "...{w=0.3}Oh? That matters to you now,{w=0.1} does it?"
        n 1fsqbo "Then tell me,{w=0.1} [player]."
        n 1fnmun "Why did you keep hurting my feelings like that?"
        n 1fcsun "...{w=0.5}{nw}"
        n 2fllan "I don't have much patience for jerks,{w=0.1} [player]."
        n 1fnmaj "I don't know if you're trying to be funny or what,{w=0.1} but knock it off.{w=0.2} Got it?"
        n 1fsqsr "Thanks."
        return

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsr "...{w=0.3}Let's just cut the crap."
        n 4fcsan "You've hurt me,{w=0.1} [player].{w=0.2} You've hurt me again,{w=0.1} and again."
        n 2fnmfu "You've done it so many times now."
        n 2fnman "So you tell me."
        n 1fsqpu "What the hell would {i}you{/i} think of someone who did that to you?"
        n 1fcspu "...{w=0.5}{nw}"
        n 2fsqan "You're on thin ice,{w=0.1} [player].{w=0.2} Got it?"
        return

    elif Natsuki.isBroken():
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n 2fsqpultse "...Wow.{w=0.2} Really?"

        else:
            n 1fsqputsb "...{w=0.3}I have no words for how I feel about {i}you{/i}."
            n 2fsqfultseean "Don't freaking test me, {i}[player]{/i}."

        return

    else:
        n 1fsqunltse "...{w=1}...{w=1}{nw}"
        n 1fcsanltda "...{w=1}..."
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
    $ already_unlocked_cosplay_outfits = jn_outfits.getOutfit("jn_trainer_cosplay").unlocked and jn_outfits.getOutfit("jn_sango_cosplay").unlocked

    if Natsuki.isEnamored(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tnmpu "Eh?{w=0.5}{nw}"
            extend 2tsqsf " Cosplay {i}again{/i}, [player]?"
            n 2fllpo "Yeesh..."

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 4fsqpol "As if having me {i}wearing{/i} cosplay wasn't already enough for you..."
                n 1fnmeml "It's all you wanna {i}talk{/i} about too!"
                n 1fcseml "I'm not your own personal dress-up doll,{w=0.75}{nw}"
                extend 2fsrpol " you know..."

            else:
                n 1nslaj "You know,{w=0.75}{nw}"
                extend 1fsqajl " if you wanted me wearing it {i}that{/i} badly..."
                n 4fsqsslsbl "You do realize you could have just {i}asked{/i},{w=0.2} right?"

            n 1fchsml "Ahaha."
            n 1ullss "Well,{w=0.2} anyway.{w=0.5}{nw}"
            extend 4unmbo " In all seriousness?"
            n 1ulrsl "I can't say too much has changed,{w=0.2} honestly."
            n 1unmpu "Don't get me wrong!"
            n 1fchbg "I totally wanna get into cosplaying more!{w=0.75}{nw}"
            extend 3fcssmeme " Any excuse to show off my talent {i}and{/i} needlework."
            n 1ullaj "Plus I mean,{w=0.75}{nw}"
            extend 4unmgs " have you {i}seen{/i} what kinds of outfits people can pull off,{w=0.5}{nw}"
            extend 4fnmgs " all in the name of the stuff they love?"
            n 3fcsem "All that talent,{w=0.3} all that passion...{w=1}{nw}"
            n 1fcspu "It's{w=0.75}{nw}"
            extend 4fspgsedz " {i}awesome{/i}!{w=1}{nw}"
            extend 1fchgnedz " There's no way I {i}don't{/i} wanna be a part of that!"
            n 1kllpu "But..."
            n 2nslsl "Well."
            n 2ksrca "Ignoring how conventions are pretty much completely out of reach for me..."
            n 1ksqtr "I don't suppose {i}you've{/i} seen any crafts shops around here,{w=0.2} have you?{w=0.75}{nw}"
            extend 1ksqca " Or any of my sewing stuff?"
            n 1ksqsl "..."
            n 4ncsss "Heh.{w=1}{nw}"
            extend 4nsrsl " Yeah,{w=0.2} I thought not."
            n 1nsrajsbl "I really gotta figure something out for that,{w=0.75}{nw}"
            extend 1tsqsssbl " huh?"
            n 1tslslsbl "..."
            n 3fcsbgsbl "W-{w=0.2}well,{w=0.2} if there's one thing I'm not short of here,{w=0.75}{nw}"
            extend 1fchbgedz " it's ideas!{w=0.5}{nw}"
            extend 1fsqsm " So don't you worry about a thing,{w=0.2} [player]..."
            n 1fwrbg "'Cause there's no shortage of that {i}material{/i}!{w=0.75}{nw}"
            extend 4nchgnl " Ehehe."

            return

        else:
            n 4usqct "Oho?{w=0.5}{nw}"
            extend 3fcsbg " Cosplay,{w=0.2} you say?"
            n 1fllbo "..."
            n 1ullpu "Honestly?{w=0.75}{nw}"
            extend 2nslsssbl " I've never really done any {i}serious{/i} cosplaying or anything..."
            n 1unmaj "But I've actually thought about it a lot more since I got into manga and all that stuff a bunch!"
            n 1fcsbg "Plus I mean,{w=0.1} why shouldn't I?{w=0.75}{nw}"
            extend 4fspgsedz " I {w=0.2}{i}love{/i}{w=0.2} thinking up new ideas for outfits!"
            n 1fcsbg "Besides,{w=0.2} I know my way around a needle and thread!{w=0.75}{nw}"
            extend 3nsrsssbr " I've had to use them often enough before."
            n 1fcsajlsbr "B-{w=0.2}but I think it seems like a pretty awesome way to show my appreciation for characters I like..."
            n 1fsqbg "...And show my {i}limitless{/i} talent while I'm at it."
            n 1usqsm "Anyway,{w=0.2} who knows?"
            n 4fsqsm "Maybe you'll get to see some of my handiwork some day,{w=0.2} [player]."
            n 1fsqbg "I bet you'd like that,{w=0.2} huh?{w=0.5}{nw}"
            extend 1fchsml " Ehehe."

            # Continue to unlock dialogue

    elif Natsuki.isAffectionate(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tsqpu "Huh?{w=0.5}{nw}"
            extend 1tsqsf " Cosplay {i}again{/i}, [player]?"

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 2fsqsflsbl "...Was {i}wearing{/i} it seriously not enough already?"
                n 4fsqsslsbl "Or did I somehow awaken some kind of hidden nerdiness in you?"
                n 4fslsslsbr "Ehehe..."
                n 1fcsemlsbr "A-{w=0.3}anyway!{w=0.5}{nw}"

            else:
                n 1tlraj "I gotta say,{w=0.2} I'm actually kinda impressed."
                n 1fslsslsbr "Sucking up to my interest in manga,{w=0.75}{nw}"
                extend 4fsqsslsbr " bugging me about cosplay..."
                n 1tsqsm "You're absorbing my sense of taste pretty fast,{w=0.2} huh?{w=0.75}{nw}"
                extend 3uchgn " Like a little dorky sponge!"
                n 1fchsm "Ehehe."
                n 1fchss "Anyway!{w=0.75}{nw}"

            extend 4nllss " Putting all that aside..."
            n 1unmaj "I actually wouldn't be {i}against{/i} doing a little more cosplay at all."
            n 1ulrpu "I mean,{w=0.75}{nw}"
            extend 3flrss " I've already got most of what I need."
            n 1fsqss "{i}Amazing{/i} ideas?{w=0.75}{nw}"
            extend 3fcsbg " Check!{w=0.75}{nw}"
            extend 4tsqsm " Tons of experience?{w=0.75}{nw}"
            extend 3fchbg " Check!"
            n 4usqgn "{i}Unmatched{/i} handiwork with a needle and thread?{w=1}{nw}"
            extend 3fcsbg " Oh,{w=0.2} you bet."
            n 1fllpu "It's just..."
            n 2kslsl "..."
            n 1tsrsf "I don't exactly have much {i}material{/i} to work with here,{w=0.75}{nw}"
            extend 4tnmsf " you know?"
            n 2kslbo "...Or even my sewing stuff,{w=0.2} for that matter."
            n 1kslsl "..."
            n 1fcswrlsbl "W-{w=0.2}well,{w=0.2} I'll figure something out!{w=0.75}{nw}"
            extend 2fcspolsbl " I always do,{w=0.2} a-{w=0.2}anyway."
            n 1fsqcal "So you better look forward to it,{w=0.2} [player]..."
            n 1fcsbglsbr "'Cause you ain't seen nothing yet!{w=0.75}{nw}"
            extend 3fcssmlsbr " Ehehe."

            return

        else:
            n 1tsrpu "Why...{w=1}{nw}"
            extend 1nsqbo " did I get the feeling you'd bring this up sooner or later,{w=0.2} [player]?"
            n 1fsqsl "..."
            n 3fnmpo "What?{w=0.75}{nw}"
            extend 3fsqgs " Did you think I'd {i}automatically{/i} be into it because I read manga from time to time?"
            n 4fsqpo "Huh?{w=0.75}{nw}"
            extend 4fnmgs " Is that it?"
            n 1fsqaj "Well?"
            n 1fsqdv "..."
            n 4fchdvesm "Pfffft!"
            n 3fchsm "Ehehe.{w=0.5}{nw}"
            extend 1ullss " Nah,{w=0.2} it's fine."
            n 1ulraj "I've thought about it a bunch,{w=0.2} honestly -{w=0.3}{nw}"
            extend 4unmbo " like since I got into manga and all that a while ago."
            n 2nslsssbr "I haven't {i}actually{/i} gone dressed up to a convention or anything yet..."
            n 2fcswrlsbl "B-{w=0.2}but that doesn't mean I haven't tried cosplaying at all!"
            n 4fcsbgsbl "I {i}am{/i} something of a pro with a needle and thread,{w=0.75}{nw}"
            extend 1fcssmeme " so it's right up my alley!"
            n 1tslsl "..."
            n 2tslss "Actually...{w=1}{nw}"
            extend 1fsqbg " you know what,{w=0.2} [player]?"
            n 1fsrsm "Perhaps I {i}might{/i} just give it another shot...{w=0.5}{nw}"
            extend 3fchbg " yeah!"
            n 1fcsss "Man,{w=0.5}{nw}"
            extend 4fchgnedz " I've got so many awesome ideas buzzing around in my head now!"
            n 1fsqss "You better be prepared,{w=0.2} [player]..."
            n 1fchbg "'Cause I'm gonna need some second opinions when I do!"
            n 3fwlbll "That's what friends are for,{w=0.2} right?"

            # Continue to unlock dialogue

    elif Natsuki.isNormal(higher=True):
        n 1unmbo "Cosplay,{w=0.2} huh?"
        n 1ulraj "Well...{w=0.5}{nw}"
        extend 3tnmbo " I mean,{w=0.2} I've played around with it,{w=0.2} if that's what you're asking."
        n 1tllpu "I never really thought about it that much until I got more into manga and things like that."
        n 3flrbg "It kinda feels like once you start getting into that stuff,{w=0.2} you discover tons more at once!"
        n 4nslsssbr "I've never really gone out and cosplayed myself though..."
        n 3fcsgslsbr "B-{w=0.2}but that doesn't mean I couldn't try it out more!"
        n 3fcspolesi "I'm basically a pro with a needle and thread,{w=0.5}{nw}"
        extend 1fchsml " so I've already got the hardest part done!"
        n 1fcsaj "The rest of it is just finding materials,{w=0.2} which are usually pretty easy to come by anyway."
        n 2fslcasbl "Props and wigs and all that are a little more annoying,{w=0.2} but not exactly {i}undoable{/i}.{w=1}{nw}"
        extend 1fcssmeme " Especially with a little ingenuity."
        n 1tcssl "..."
        n 3tupbo "Mmmm..."
        n 1tllpu "You know,{w=0.75}{nw}"
        extend 1fllss " the more I think about it...{w=1}{nw}"
        extend 3nchgnedz " the more I like the idea of giving it another run!"
        n 1fnmbg "What about you,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1usqbg " I bet you'd love to see my skills at work,{w=0.2} right?"
        n 3fsrbgl "Well...{w=1}{nw}"
        extend 1fsqsm " we'll see."
        n 2fcsgssbl "B-{w=0.2}but no promises!"

        return

    elif Natsuki.isDistressed(higher=True):
        n 1nnmpu "Huh?{w=0.2} Cosplay?"
        n 1fsqsr "...Why,{w=0.2} [player]?"
        n 2fsqpu "So you can make fun of my clothes too?"
        n 1fslsr "..."
        n 2fsqpu "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fcssr " That's for me to know,{w=0.75}{nw}"
        extend 4fsqan " and for you {i}not{/i} to find out."
        n 2fsqgs "Does {i}that{/i} answer your question?"

        return

    else:
        n 1fsqsr "Heh.{w=0.5} Why?"
        n 2fcsantsa "So you have something else to make me feel awful about?"
        n 1fcssrltsa "...Yeah.{w=0.75} No thanks."
        n 2fcsanltsd "I'm done talking to you about this."

        return

    # Show Natsuki in cosplay and unlock cosplay outfits, if custom outfits unlocked
    if (
        Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
        and not already_unlocked_cosplay_outfits
    ):
        n 1tllbo "..."
        n 1tslpu "...Actually,{w=0.5}{nw}"
        extend 2tslaj " now that I think about it..."
        n 1tlrsl "I wonder..."
        n 1fcssl "..."
        n 3nnmaj "You know what?{w=0.75}{nw}"
        extend 1nllaj " Just...{w=0.75}{nw}"
        extend 4nslunl " give me a sec here...{w=1}{nw}"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(2)
        play audio gift_open
        $ jnPause(3)
        n "...!"
        play audio clothing_ruffle
        $ jnPause(1)
        play audio zipper
        $ jnPause(5)

        $ outfit_to_restore = Natsuki.getOutfit()
        $ jn_outfits.getOutfit("jn_trainer_cosplay").unlock()
        $ jn_outfits.getOutfit("jn_sango_cosplay").unlock()
        $ Natsuki.setOutfit(jn_outfits.getOutfit(random.choice(["jn_trainer_cosplay", "jn_sango_cosplay"])))

        play audio chair_in
        $ jnPause(3)
        show natsuki 1fsldvlesssbr at jn_center
        hide black with Dissolve(1.25)

        n 2fchsslesssbr "T-{w=0.5}ta-da!{w=0.5}{nw}"
        extend 1fchsml " Ehehe..."
        n 1fsqsll "..."
        n 2fslunl "..."
        n 4fcsemlsbl "W-{w=0.2}well?"
        n 2fcsbglsbl "What do you think,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fchsmlsbr " I made it all myself,{w=0.2} too!"
        n 2fsqsrlsbr "..."
        n 4fnmemlsbr "What?"
        n 3fcsgslsbl "I {i}did{/i} say I was good with a needle and thread!"
        n 3fllsslsbl "S-{w=0.3}so of course I {i}had{/i} to prove it!"
        extend 1fcsajlsbl " And..."
        n 1nslsslsbl "...And..."
        n 4nslsllsbl "..."
        n 1kslsll "..."
        n 1kcspul "This...{w=1}{nw}"
        extend 2ksrsfl " wasn't actually {i}meant{/i} for me,{w=0.2} you know."
        n 1kcspulesi "..."
        n 4ksqbol "...I made it for Sayori."
        n 1fcseml "I-{w=0.2}it was meant to be for some kind of party after the festival she insisted on,{w=0.2} but...{w=1}{nw}"
        extend 2kcssll " yeah."
        n 1kslslltsb "..."
        n 2fcsunltsb "I'm...{w=1.25}{nw}"
        extend 4ksrsrl " just gonna go put this away now."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(4)
        play audio gift_close
        $ jnPause(3)

        play audio chair_in
        $ jnPause(3)
        $ Natsuki.setOutfit(outfit_to_restore)
        show natsuki 1ncspul at jn_center
        hide black with Dissolve(1.25)

        n 1kslsll "..."
        n 2kslpul "...I know I can't just throw that outfit away.{w=1.25}{nw}"
        extend 1kcsajl " It just...{w=0.5} wouldn't be right."
        n 1kslbol "..."
        n 4kcspul "I'll...{w=0.5} keep it around."
        n 2knmsll "The best thing I could do is to make some {i}happy{/i} memories with it myself instead."
        n 2ksrajl "...It's what she would have done, a-{w=0.2}after all."
        n 1ksrsll "..."
        n 4ksqbol "...Right?"

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
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_why_do_you_like_me:
    if Natsuki.isLove(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 4kwmsl "[player]..."
            n 1kwmsf "You aren't asking me this because of what you told me earlier...{w=0.3} right?"
            n 1kllbo "..."
            n 1ncspu "Look,{w=0.1} [player].{w=0.2} I'm going to be completely honest with you,{w=0.1} okay?"
            n 1ncssl "What you can -{w=0.1} or {i}can't{/i} do -{w=0.1} isn't important to me."
            n 1nnmpu "What people {i}say{/i} you are -{w=0.1} or {i}aren't{/i} capable of -{w=0.1} isn't important to me either."
            n 4fnmpu "Neither is what people say about you."
            n 2knmsr "[player]."
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1klrpu "I...{w=0.3} feel about you the way I do because of how you've treated me,{w=0.1} [chosen_endearment].{w=0.2} Can you not see that?"
            n 2klrss "You've spent so much time with me,{w=0.1} day after day..."
            n 4kwmss "You've listened to my problems,{w=0.1} and you've told me yours..."
            n 2kllpo "You've been so patient with my mood swings,{w=0.1} and my grumpy moments..."

            if persistent.jn_player_love_you_count >= 10:
                n 1kcsunl "And...{w=0.3} you've made me feel..."
                n 4kcsunf "So loved..."
                n 1kllunl "..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kllssl "You're...{w=0.3} you're my first love,{w=0.1} [player]..."
                n 4kcussl "Do you even realize how {i}much{/i} that means to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 2kwmssl "You honestly,{w=0.1} truly mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 4klrnvl "Does that answer your question?"
            n 1knmsr "I know I can't solve your problems with a snap of my fingers,{w=0.1} [player].{w=0.2} I'm not a miracle worker."
            n 2kslsl "Believe me -{w=0.1} I {i}already{/i} would have if I could."
            n 1knmsl "But..."
            n 1kllss "I hope you can believe me when I say things will work out,{w=0.1} okay?"
            n 4fwmsm "Just...{w=0.3} keep fighting..."
            n 1fcssml "...Because I'm fighting for you too."
            n 3kplnvf "I love you,{w=0.1} [player].{w=0.2} You better not forget that."
            return

        else:
            n 3fcspo "[player]..."
            n 3flrpo "Do I really have to explain this all to you?"
            n 1flrsll "It's just...{w=0.3} embarrassing...{w=0.3} to me..."
            n 1kcssll "..."
            n 4ncspu "...Okay,{w=0.1} look."
            n 1fllssl "You've...{w=0.3} honestly done more than you could ever know,{w=0.1} [player]."
            n 2fllsll "For me,{w=0.1} I mean."
            n 1knmsll "I've almost lost count of how many hours you've spent talking to me..."
            n 3klrssl "You've listened to so many of my dumb problems,{w=0.1} over and over..."
            n 4fllunl "...And you've been so patient through all of my stupid moods."

            if persistent.jn_player_love_you_count >= 10:
                n 1fcsunl "Y-you've made me feel..."
                n 4kcsunl "Really appreciated.{w=0.2} So many times,{w=0.1} I've lost count..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kskajf "You're...{w=0.3} you're my first love,{w=0.1} even!"
                n 3kwmpuf "Do you even know what that {i}means{/i} to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 3kwmpuf "You seriously mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 4klrnvl "Does that answer all of your questions?{w=0.2} Am I free to go now?"
            n 1klrss "Ahaha..."
            n 2kwmpu "But seriously,{w=0.1} [player]."
            n 1kplbo "Don't ever doubt how important you are to me,{w=0.1} alright?"
            n 2fnmpol "I'll get mad if you do."
            n 2flrpol "And trust me..."
            n 4klrssl "I doubt you want that."
            return

    elif Natsuki.isEnamored(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1knmaj "...Hey,{w=0.1} [player]..."
            n 2klrpu "This isn't by chance because of what you said earlier...{w=0.3} right?"

        else:
            n 1uskpul "Wh-{w=0.1}why do I-{w=0.1}...?"
            n 2fcsanl "Uuuuuuu..."

        n 1fcsajl "...Okay,{w=0.1} look.{w=0.2} I'll try to help you understand as best I can."
        n 3fllaj "I'm not sure if someone's giving you a tough time or what, but I'm saying it anyway."
        n 1fllsr "I don't really care about what others expect from you."
        n 4fnmsr "I don't really care about what others say or think about you."
        n 4knmpu "I don't really care if you can -{w=0.1} or can't -{w=0.1} do something."
        n 1fcseml "I...{w=0.3} {i}like{/i} you,{w=0.1} because of how you've treated me,{w=0.1} you dummy!"
        n 3flleml "Like,{w=0.1} come on!"
        n 4flrssl "You've listened to me yammer on,{w=0.1} again and again..."
        n 1knmssl "You've heard me out on so many dumb problems I've had..."
        n 3fcsbgl "You've even dealt with my crappy temper like a champ!"
        n 1klrsl "..."
        n 1kcssl "...I've never been treated by anyone as well as I've been treated by you,{w=0.1} [player]."
        n 3fllslf "So is it any wonder why I...{w=0.3} enjoy hanging out with you this much?"
        n 1fcsslf "..."
        n 1flrajl "Alright,{w=0.1} okay.{w=0.2} I really don't wanna have to explain all that again,{w=0.1} so I hope you took all that in."
        n 4fnmssl "Just...{w=0.3} continue being you,{w=0.1} got it?"
        n 3kllpul "I...{w=0.3} kinda like how you do that already."
        return

    else:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1unmpul "...Huh?"
            n 4uskemf "W-{w=0.1}why do I...?"
            n 2fcsanf "..."
            n 1tlremf "..."
            n 1flrsll "..."
            n 4fnmpul "Uhmm...{w=0.3} [player]?"
            n 2fllpo "This isn't all related to what you told me earlier,{w=0.1} right?"
            n 4knmpo "About feeling insecure and all that?"
            n 1klrsl "..."
            n 4nnmsl "[player]."
            n 3fnmpuf "Listen up,{w=0.1} 'kay?{w=0.2} I...{w=0.3} really don't wanna have to repeat this."

        else:
            n 4uscemf "Urk-!"
            n 1uskemf "W-{w=0.1}wait,{w=0.1} w-{w=0.1}what?"
            n 3fwdemf "W-{w=0.1}why do I...{w=0.3} l-{w=0.1}like you?!"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fllwrf "I mean...!{w=0.2} It's not that I {i}like{/i} like you,{w=0.1} or anything ridiculous like that!"
            n 3fcsemf "Ugh...{w=0.3} I swear,{w=0.1} [player] -{w=0.1} you honestly try to put me in the most awkward freaking spots sometimes..."
            n 1fllslf "..."
            n 4fllsll "I...{w=0.3} guess I {i}do{/i} owe you an answer though,{w=0.1} at least."

        n 1fcssll "Look."
        n 1nlrpu "You've been pretty awesome to me so far,{w=0.1} [player]."
        n 4klrpu "...Do you even know how few other people make me feel that way?"
        n 1klrsl "It's...{w=0.3} really not a lot,{w=0.1} if you hadn't gathered."
        n 2fllpol "You always listen to me,{w=0.1} you don't tell me I'm annoying,{w=0.1} or to pipe down..."
        n 1kwmsrl "And you've been super understanding too."
        n 1kllpul "I...{w=0.3} honestly couldn't ask for a better friend,{w=0.1} [player]."
        n 3fnmbol "Always remember that,{w=0.1} alright?{w=0.2} I'll get mad if you don't."
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
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fried_squid:
    n 1fllss "Hey,{w=0.1} [player]..."
    n 4usqsm "You know what I could go for right now?"
    n 1uchbs "A big,{w=0.1} steaming fresh bowl of Mon-{w=0.1}ika!"
    n 1uchbg "..."
    n 2flrpu "...Huh."
    n 1tnmpu "You know,{w=0.1} in hindsight?{w=0.2} That joke really wasn't funny the first time round."
    n 3tllpo "I've...{w=0.3} no idea why it'd be funny this time,{w=0.1} to be honest."
    n 4uspgsesu "Oh!"
    n 1fchbg "But fried squid is no joke at all,{w=0.1} [player]!{w=0.2} Have you ever tried it?"
    n 1uchbs "It's {i}delicious{/i}!{w=0.2} I love it!"
    n 3fsqsm "Not just boring old fried seafood though -{w=0.1} it's gotta have the crap battered out of it first!"
    n 4uspbg "That crispy golden coating is seriously the best.{w=0.2} Deep fried food is awesome!"
    n 1fllbg "It's not {i}good{/i} for you exactly,{w=0.1} but as a treat?{w=0.2} You could do way worse..."
    n 4fcsts "Especially with sauce to spice things up a bit!"
    n 1fnmss "By the way -{w=0.1} wanna know how you can tell you're dining on some top-notch squiddy goodness?"
    n 3uchbs "The texture,{w=0.1} of course!"
    n 3fllaj "Overcooked squid becomes all rubbery and nasty,{w=0.1} and even worse -{w=0.1} it loses all of its flavor too!"
    n 1fsqsr "Imagine biting through the batter,{w=0.1} only to find you're basically chewing on a bunch of rubber bands."
    n 2fsqem "Ugh!{w=0.2} Gross!{w=0.2} Talk about a disappointment."
    n 1unmaj "Don't let that put you off though,{w=0.1} [player] -{w=0.1} next time you see some,{w=0.1} why not give it a shot?"

    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1kllss "...Probably the sooner the better,{w=0.1} if you're hungry like you said."
        n 4ullaj "But anyway..."

    n 1unmbg "You could even be all fancy if you wanted to and order it by the culinary name!"
    n 3fnmbg "Ten points if you can guess what that is.{w=0.2} Ehehe."

    if Natsuki.isLove(higher=True):
        n 3flrsg "Hmm..."
        n 1fnmbg "Actually...{w=0.3} you know what?"
        n 1fchbg "We should just get a bowl of calamari to share.{w=0.2} That's fair,{w=0.1} right?"
        n 4fsqsm "I should warn you though,{w=0.1} [player]..."
        n 3fchgn "I'm not handing over the last piece without a fight!"
        n 1nchsml "Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1uchbg "But yeah -{w=0.1} you should really give it a try if you haven't already,{w=0.1} [player]!"
        n 4fchbg "I wouldn't want someone to miss out on that!"
        n 2klrssl "E-{w=0.1}especially not you.{w=0.2} Ehehe..."

    else:
        n 1uchbg "But yeah {w=0.1}-{w=0.1} you should really try it out if you haven't already,{w=0.1} [player]!"
        n 4fchbg "I wouldn't want someone to miss out on that!{w=0.2} Ahaha."

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
    if Natsuki.isAffectionate(higher=True):
        n 4unmpueqm "Collectibles?{w=0.2} You mean like figurines and plushies and such?"
        n 4flrpu "Mmm...{w=0.3} not really.{w=0.2} Collecting is an expensive hobby,{w=0.1} [player]!"
        n 3klrpo "I mean,{w=0.1} it all depends on exactly what you collect,{w=0.1} but it feels like places that sell them prey on that."
        n 1flraj "Like...{w=0.3} the urge to complete a collection -{w=0.1} so they jack up the prices!"
        n 1fcsboesi "Ugh..."
        n 3kllbosbl "And for people in my...{w=0.3} uhmm...{w=0.3} {i}position{/i},{w=0.1} it's a big barrier to entry."
        n 1unmaj "But anyway..."

    elif Natsuki.isNormal(higher=True):
        n 4tnmpueqm "Huh?{w=0.2} You mean like figurines and all that stuff?"
        n 1tlrpu "Well...{w=0.3} no,{w=0.1} [player].{w=0.2} Not really."
        n 2knmsf "I couldn't justify spending so much just on hobbies like that!"
        n 2flrbo "...Especially not when I had {i}other{/i} things to worry about spending my money on first."
        n 1unmaj "B-{w=0.2}but anyway,{w=0.1} putting all that aside..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsfsbl "No,{w=0.1} [player]."
        n 2fsqaj "Collectibles were way too expensive for me.{w=0.2} I couldn't justify wasting the money I {i}do{/i} have."
        n 1fnmsl "{i}Especially{/i} on stuff that'll just sit on a shelf that I'll forget about."
        n 4fsqsr "Yeah,{w=0.1} [player] -{w=0.1} believe it or not,{w=0.1} some of us {i}do{/i} have to think about how we spend our money."
        n 2fsqun "Shocker,{w=0.1} right?"
        n 1fcsun "..."
        n 1fnmaj "Well?{w=0.2} Satisfied with your answer?"
        n 2fsqsl "We're done here."
        return

    else:
        n 1fsqsr "...Why?{w=0.2} ...And I don't just mean why you care."
        n 2fsqan "But why should I tell {i}you{/i} if I do or not?"
        n 1fcsan "You'd probably just trash them."
        n 2fcsun "Heh.{w=0.2} After all."
        n 4fsqupltsa "You've proven great at trashing things so far,{w=0.1} {i}haven't you{/i}?{w=0.2} Jerk."
        return

    n 1ullbo "..."
    n 2tllbo "...Huh.{w=0.2} There's a point,{w=0.1} actually.{w=0.2} Does manga count as a collectible?"
    n 1tllaj "I'm...{w=0.3} not really sure..."
    n 1tnmpu "What do you think,{w=0.1} [player]?"
    menu:
        n "Would you call it a collectible?"

        "I'd say so!":
            n 4fsqct "Oho!"
            n 3fchbg "So I suppose I am something of a collector,{w=0.1} after all!"

            if Natsuki.isLove(higher=True):
                n 1uchsm "I guess that all makes sense.{w=0.2} After all..."
                n 3fllsmf "I'd like to think you're in my collection too,{w=0.1} [player]~."
                n 1uchsmf "Ehehe."

            else:
                n 1flrsm "Well,{w=0.1} in that case..."
                n 4nchbg "Just let me know if you ever feel like a tour!"
                n 3nchgn "You won't find a better collection!{w=0.2} Ehehe."

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.manga):
                    n 1fllss "Or,{w=0.1} at least...{w=0.5}{nw}"
                    extend 3fsqss " a better...{w=0.3} {i}physical{/i} one."
                    n 1fsqsm "Right,{w=0.5}{nw}"
                    extend 4fsqbg " [player]?"

        "No,{w=0.1} I wouldn't.":
            n 3flrpo "Huh...{w=0.3} you do have a point."
            n 3tnmpo "I suppose you'd call it a library,{w=0.1} or something like that?"
            n 1nnmsm "Well,{w=0.1} whatever."
            n 4nsqsm "I suppose I'd better {i}read{/i} up on my definitions,{w=0.1} right?"
            n 1nchsm "Ehehe."

        "Well,{w=0.1} it definitely isn't literature.":
            n 1nsqsr "Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} ...Ha."
            n 2flrpo "{i}Hilarious{/i},{w=0.1} [player]."
            n 1flraj "Keep it up,{w=0.1} and I'm gonna book you one."
            n 4fsqsg "...And no,{w=0.1} I don't mean read you a story."

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
        # Unlock Snap if the player somehow is labelled as a cheater with no option to apologize
        if not int(jn_apologies.ApologyTypes.cheated_game) in persistent._jn_player_pending_apologies:
            $ persistent.jn_snap_player_is_cheater = False

        else:
            n 1ccsem "[player]..." 
            n 2cllfl "If you aren't even sorry you cheated,{w=0.5}{nw}" 
            extend 2csqfl " why {i}should{/i} I play with you again?"
            n 4fcssl "Come on...{w=1}{nw}" 
            extend 2csrca " it's not hard to apologize,{w=0.75}{nw}" 
            extend 2csqca " is it?"

            return

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3fchbg "Of course I do,{w=0.2} [chosen_tease]!{w=0.5}{nw}"
        extend 3fchsmeme " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 4unmss "Snap?{w=0.75}{nw}"
        extend 4fchbg " Sure thing,{w=0.2} [player]!"

    elif Natsuki.isAffectionate(higher=True):
        n 1fcsbg "Well,{w=0.2} duh!{w=0.75}" 
        extend 2fchbg " Say no more,{w=0.2} [player]!"

    else:
        n 1unmaj "You wanna play Snap?{w=0.75}{nw}" 
        extend 4fchsm " Sure!"

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_card_pack":
        n 7csqbg "Good thing I never put the cards away,{w=0.2} huh?"

    else:
        n 4fcsss "Let me just get the cards out real quick..."

        show natsuki 4fcssm
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1.5)
        play audio drawer
        $ jnPause(1)
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
        show natsuki 4fchsm
        hide black with Dissolve(1)

    $ get_topic("talk_play_snap").shown_count += 1 # Have to increment here manually thanks to jump
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
        n 2fcsan "Come on,{w=0.1} [player]."
        n 2flrpo "If you cared about the rules,{w=0.1} then why did you cheat when we played earlier?"
        n 4fnmpo "You haven't even apologized for it yet..."

        $ get_topic("talk_remind_snap_rules").shown_count += 1 # Have to increment manually here thanks to jump
        return

    else:
        if Natsuki.isLove(higher=True):
            n 1nchbg "Ahaha.{w=0.2} You're so forgetful sometimes,{w=0.1} [player]."
            n 3nsqbg "Sure,{w=0.1} I'll go over it again!{w=0.2} Juuust for you~."

        elif Natsuki.isEnamored(higher=True):
            n 4nchbg "Of course I can!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fchsm "You bet I can!"

        else:
            n 1nnmss "Sure thing!"

        $ get_topic("talk_remind_snap_rules").shown_count += 1 # Have to increment manually here thanks to jump
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
    n 2fcsan "Ugh...{w=0.3} you know what really gets on my nerves?"
    n 1fsqsl "When people are gross and don't get rid of chewing gum properly."
    n 1fbkwr "Seriously -{w=0.1} it annoys the crap out of me!"
    n 3fllem "Like,{w=0.1} have you ever walked into a city center and looked at the ground?{w=0.2} At all the paving?"
    n 1fcsan "All those dried up spots of gum -{w=0.1} it's freaking disgusting,{w=0.1} and it looks nasty too!"
    n 4fsqan "And that's in a place where there's usually bins everywhere too,{w=0.1} so it isn't just gross..."
    n 3fnmwr "It's super lazy too!{w=0.2} I can't decide what winds me up more."
    n 3fcsup "Even worse than that -{w=0.1} there's even people who go and stick it under tables,{w=0.1} or on walls -{w=0.1} who {i}does{/i} that?!"
    n 1flrpu "Jeez...{w=0.3} makes me want to track them down and stick that crap back in their stupid mouths."
    n 1nnmsl "I don't really care if you chew gum yourself,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        n 2kllca "Just make sure you dispose of it properly,{w=0.1} 'kay?"
        n 1kllss "I'm sure you do anyway,{w=0.1} but...{w=0.3} just in case."
        n 4kchsml "Love you,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1nllca "But please,{w=0.1} just get rid of it properly when you're done."
        n 4nchsm "Thanks,{w=0.1} [player]~!"

    else:
        n 3fnmaj "But seriously -{w=0.1} stick it in the bin when you're done,{w=0.1} alright?{w=0.2} Or just wrap it in a tissue and get rid of it later."
        n 3fsqaj "...Or it won't just be the gum that'll be getting chewed out!"

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
    n 3fsqaj "I mean {i}really{/i} stinks -{w=0.1} not just figuratively,{w=0.1} but literally too?"
    n 1fcssf "When people smoke or vape indoors,{w=0.1} or near entrances -{w=0.1} {i}especially{/i} when other people are around.{w=0.2} I can't stand it!"
    n 4fcsan "Like...{w=0.3} how inconsiderate can you be?{w=0.2} Seriously?"
    n 3fsqwr "For starters,{w=0.1} and like I was just saying -{w=0.1} it absolutely {i}reeks{/i}!"
    n 3fllem "Tobacco is awful smelling stuff,{w=0.1} and all those sickly vaping fluid types aren't much better either."
    n 4ksqup "It clings to the walls too -{w=0.1} so the smell hangs around for ages!"
    n 1kllan "Speaking of clinging to the walls,{w=0.1} the smoke literally does that too -{w=0.1} have you {i}seen{/i} a smoker's house,{w=0.1} or car?"
    n 3ksqup "All those yellow stains...{w=0.3} you'd think it was painted on or something.{w=0.2} Ew!"
    n 1fsqan "And you know what,{w=0.1} [player]?{w=0.2} I haven't even gotten to the worst of it yet..."
    n 3fcsan "I've said nothing about how expensive it all is,{w=0.1} or the health problems not just to the smoker..."
    n 4fsqaj "...But to everyone else!"
    n 1fcsbo "Ugh..."
    n 3flrbo "Don't get me wrong -{w=0.1} if someone wants to smoke or vape,{w=0.1} that's their choice and their money.{w=0.2} I don't care."
    n 1fnmbo "But the least they can do is respect the decision of everyone who {i}doesn't{/i},{w=0.1} you know?"
    n 1fcssl "..."

    if Natsuki.isLove(higher=True):
        n 1nnmsl "I know you,{w=0.1} [player].{w=0.2} I highly doubt you'd be the kind of person to be a jerk like that."
        n 4klrss "Just...{w=0.3} don't prove me wrong,{w=0.1} alright?"
        n 2uchgn "'preciate it!{w=0.2} Ahaha."

    elif Natsuki.isAffectionate(higher=True):
        n 3kllpo "I doubt you'd be a jerk like that even if you do smoke,{w=0.1} [player]."
        n 3fsqpo "But...{w=0.3} try not to prove me wrong,{w=0.1} 'kay?{w=0.2} I like you more as not a jerk."
        n 1uchsm "Thanks!"

    else:
        n 1ullaj "I don't think you'd be a jerk like that,{w=0.1} [player]."
        n 4nnmaj "But...{w=0.3} just in case -{w=0.1} keep it in mind,{w=0.1} will you?"
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
    n 4unmaj "Hey,{w=0.1} [player]."
    n 3nsqsl "Have you ever worked in a restaurant,{w=0.1} or a hospital or anything like that?"
    n 1fnmaj "Because I bet if there's one thing drilled into you...{w=0.3} it's how important washing your hands is!"
    n 3flrun "It really gets on my nerves when people don't wash their hands after doing something nasty."
    n 3fsqsl "Like...{w=0.3} we {i}know{/i} how important it is to stop germs getting around -{w=0.1} and {i}what{/i} exactly is hard about sticking your hands under the tap for a minute?!"
    n 1fslem "It annoys me even more when people are really dumb about it too!{w=0.2} Like,{w=0.1} they think they don't need to do that if they didn't go."
    n 1fcsan "Newsflash -{w=0.1} if you went in,{w=0.1} you must have touched stuff -{w=0.1} so now there's all that crap on your hands that you've taken out with you!"
    n 4fsqsf "Not only is it {i}super{/i} icky and bad for {i}your{/i} health..."
    n 2ksqan "It's awful for others too!{w=0.2} What if you're about to handle someone's food,{w=0.1} or visit someone in hospital?"
    n 1fllem "You could make someone seriously ill..."
    n 3fnmfu "...And then they get all upset when you call them out on their grossness!{w=0.2} I mean,{w=0.1} come {i}on{/i}!"
    n 1fcssl "Just...{w=0.3} ugh."
    n 1ncssl "...[player]."
    n 4nnmpu "I really hope you keep your hands spick and span.{w=0.2} And not just when you visit the restroom."
    n 3fsgaj "Before you prepare food,{w=0.1} after you've handled trash...{w=0.3} just think about where you've been,{w=0.1} alright?"

    if Natsuki.isLove(higher=True):
        n 1kchbg "Don't get me wrong though!{w=0.2} I'm pretty sure you at least try to do the right thing!"
        n 3nnmss "Just...{w=0.3} keep up the good work,{w=0.1} alright?{w=0.2} For everyone."
        n 4nchsm "Thanks,{w=0.1} [player]!"

    else:
        n 3tsqpo "It really isn't that much to ask...{w=0.3} is it?"

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
    n 3fcsbg "Ehehe.{w=0.2} Are you surprised?"
    n 3fchgn "Yep!{w=0.2} From the bins,{w=0.1} to the desks,{w=0.1} to the floors.{w=0.2} It was all our effort that kept it squeaky clean!"
    n 3flrpol "N-{w=0.1}not that I {i}enjoyed{/i} it,{w=0.1} of course!{w=0.2} Cleaning {i}is{/i} pretty lame,{w=0.1} but it's just something you gotta do."
    n 4fnmpo "But I'll tell you one thing,{w=0.1} [player]."
    n 2fsqtr "{i}Nothing{/i} pissed me off more than the jerks who just went and dropped or left their trash everywhere."
    n 1fnman "...And not even just in school!"
    n 1fcsan "I mean...{w=0.3} where do I start?!"
    n 3fnmaj "First off -{w=0.1} how much of a freaking slob do you have to be?{w=0.2} Do these people just drop crap all over their homes too?!"
    n 1flran "It annoys me even more when there's bins and stuff literally right there!"
    n 4fcsfu "Like,{w=0.1} wow...{w=0.3} lazy as well as inconsiderate?{w=0.2} What a {i}charming{/i} combo!"
    n 1fllpu "Even if there isn't a trash can or whatever around..."
    n 3fllan "It's not like they don't have pockets,{w=0.1} or can't just carry it around for a few minutes!"
    n 1fcswr "Ugh..."
    n 3flrup "And I haven't even mentioned people tossing their rubbish out of cars,{w=0.1} or into lakes and ponds!"
    n 1fcssl "It pisses me off just thinking about it..."
    n 1fllbo "..."
    n 4fnmbo "[player]."

    if Natsuki.isEnamored(higher=True):
        n 2ksqbo "I know you.{w=0.2} In fact,{w=0.1} I daresay I know you {i}very{/i} well by now."
        n 1knmbo "I don't think you're the sort to do that at all..."
        n 2ksraj "I'm not wrong...{w=0.3} am I?"
        n 1klrss "I don't wanna have to be.{w=0.2} Ahaha..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "I don't think you're like that,{w=0.1} [player]."
        n 2ullsl "Or...{w=0.3} at least you don't {i}try{/i} to be anyway."

    else:
        n 2fnmsl "I really,{w=0.1} really hope you aren't one of those people."

    n 1nllpu "So..."
    n 1nnmsl "...If you're a litterbug already,{w=0.1} I'll forgive you this one time."
    n 3klrpo "Just...{w=0.3} make sure you clean up your act,{w=0.1} okay?"

    if Natsuki.isLove(higher=True):
        n 4uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~."

    elif Natsuki.isAffectionate(higher=True):
        n 3nlrpol "It'd...{w=0.3} mean a lot."

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
            prompt="Music player",
            conditional="not persistent.jn_custom_music_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_introduction:
    n 1tllboeqm "..."
    n 1fllpu "...Huh."
    n 1flrbo "I wonder if it's still here..."
    n 2fsrpoesp "..."
    n 1flraj "You know what?{w=0.75}{nw}"
    extend 4fnmsseid " Just give me a second here,{w=0.2} [player]."
    n 1fcsbg "You're gonna {i}love{/i} this!"
    show natsuki 1fcssm

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio chair_out
    $ jnPause(3)
    play audio drawer
    $ jnPause(2)

    n "Come on!{w=0.75} It's gotta still be here somewhere!{w=0.75} I know it!"

    play audio drawer
    $ jnPause(2.5)
    play audio gift_slide
    $ jnPause(0.5)

    n "...!"
    n "Aha!{w=0.5} Yes!{w=0.75} Found you~!"
    play audio gift_close
    $ jnPause(3)
    n "...Ah.{w=0.75} Just gotta...{w=0.75}{nw}"
    play audio blow
    $ jnPause(0.3)
    n "A-{w=0.2}ack!{w=0.75} I didn't think it was {i}that{/i} dusty..."
    n "...Ew."

    play audio headpat
    $ jnPause(3)
    play audio gift_close
    show music_player off zorder JN_PROP_ZORDER
    show natsuki 1fchsm
    $ jnPause(1.5)
    play audio chair_in
    $ jnPause(2)
    hide black with Dissolve(2)

    n 1nchsm "..."
    n 1unmajesu "Oh!{w=0.5}{nw}"
    extend 2fchbgsbl " [player]!"
    n 1fcsbg "Guess what I fooound!{w=0.75}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsbg "It's...{w=1.25}{nw}"
    play audio button_tap_c
    show music_player stopped
    $ jnPause(1)
    n 2uchgn "...Our old music player!{w=1}{nw}"
    extend 1fwlbg " Neat,{w=0.2} right?"
    n 4fchbgsbl "Ehehe..."
    n 1tlrss "Well...{w=1}{nw}"
    extend 1nsrsssbl " kinda."
    n 2nllsssbl "It's not exactly...{w=0.5}{nw}"
    extend 2nslsssbl " well...{w=1}{nw}"
    extend 2fslposbl " {i}modern{/i},{w=0.75}{nw}"
    extend 1fcsbgsbr " but it'll do the job!"
    n 1tslbo "..."
    n 1tslaj "Actually...{w=0.75}{nw}"
    extend 1tllsl " come to think of it..."
    n 4tnmpo "I don't really even know who it belongs to."
    n 1tllca "We just found it left in the clubroom one day.{w=0.75}{nw}"
    extend 1tnmpu " Nobody knew if it belonged to anyone -{w=0.5}{nw}"
    extend 1unmaj " and trust me,{w=0.2} we {i}tried{/i} to find out!"
    n 2tlrsl "We asked around in lessons,{w=0.5}{nw}"
    extend 2tllaj " Monika sent out notes...{w=1}{nw}"
    extend 1unmaw " nothing!"
    n 4ulraj "So...{w=0.75}{nw}"
    extend 1tnmsl " we kinda just kept it here,{w=0.2} by the teacher's desk,{w=0.2} in case whoever it was came back to pick it up."
    n 2nslss "And,{w=0.2} well..."
    n 2tsqposbr "I guess they never will now,{w=0.2} huh?"
    n 1kslbo "..."
    n 1fcssslsbl "W-{w=0.2}well,{w=0.2} whatever.{w=0.75}{nw}"
    extend 4fchbgsbl " The point is we can play whatever music we want now!"
    n 1fchsmeme "I think I figured out a way to let you send me whatever you want me to put on,{w=0.75}{nw}"
    extend 2fwlbg " so listen up,{w=0.2} 'kay?"

    $ get_topic("talk_custom_music_introduction").lock()
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
    # Unlock early in case of crash/quit
    $ persistent.jn_custom_music_unlocked = True
    $ hide_music_player = False

    if persistent.jn_custom_music_explanation_given:
        $ persistent.jn_custom_music_explanation_given = True
        n 1unmaj "Huh?{w=0.2} You want me to explain how custom music works again?"
        n 1uchbg "Sure,{w=0.1} I can do that!"
        n 2nnmsm "First things first,{w=0.1} let me just check for the {i}custom_music{/i} folder..."

    else:
        $ hide_music_player = True
        $ persistent.jn_custom_music_explanation_given = True
        n 1unmbg "Alright!{w=0.2} So...{w=0.3} it's actually pretty simple,{w=0.1} [player]."
        n 1nsgsm "There should be a folder called {i}custom_music{/i} somewhere around here..."
        n 1nchbg "Let me just take a look,{w=0.1} one sec..."
        n 2ncssr "..."

    if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):
        n 2tnmbg "Well,{w=0.1} hey!{w=0.2} It's already there!{w=0.2} I must have set it up earlier and forgot."
        n 2uchgn "No complaints from me!"

    else:
        n 1uchbg "Okaaay!{w=0.2} It wasn't there,{w=0.1} so I've just created it for you."

    $ custom_music_link_path = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    if renpy.windows:
        n 1unmaj "So,{w=0.1} [player] -{w=0.3}{nw}" 
        extend 1ullaj " if you click {a=[custom_music_link_path]}here{/a},{w=0.2}{nw}" 
        extend 1fcsss " that'll take you to the folder I set up."
        n 1fchbg "Then all you gotta do is just {i}copy{/i} your music into that folder,{w=0.2} and you're good to go!"

    else:
        n 1unmaj "So,{w=0.1} [player] -{w=0.3}{nw}" 
        extend 1ullaj " you should be able to find the folder I set up at {i}[custom_music_link_path]{/i}." 
        n 1fchbg "All you gotta do is just {i}copy{/i} your music into that folder,{w=0.2} and you're good to go!"

    n 2uchgn "Easy as pie,{w=0.1} huh?{w=0.5}{nw}" 
    extend 2fchsm " Ehehe."
    n 4uwdaj "Oh -{w=0.1} a couple of things first though,{w=0.1} [player]."
    n 1unmpu "Any music you give me needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format."
    n 1ullss "If you don't know how to check,{w=0.1} then just look at the letters after the period in the file name."
    n 1unmss "You should also be able to see those in the file {i}properties{/i} if they don't appear on the screen at first."
    n 2flrbg "Like I said -{w=0.1} this thing isn't {i}exactly{/i} super modern,{w=0.1} so it won't work with any fancy newer formats,{w=0.1} or weird old ones."
    n 4uwdaj "Oh,{w=0.75}{nw}"
    extend 1nlrpu " and if you gotta convert it first,{w=1}{nw}"
    extend 2nsqpo " don't just rename it."
    n 1fcsbg "Use a proper converter!{w=1}{nw}"
    extend 2fsrbg " Unless you {i}enjoy{/i} hearing your music being all warped and nasty,{w=0.3} anyway."
    n 1nnmaj "Once you've done that,{w=0.1} just click the {i}Music{/i} button,{w=0.1} and I'll check that it's all done right."
    n 4nchbg "...And that's about it!"
    n 4nsqbg "A word of warning though,{w=0.1} [player]..."
    n 1usqsg "You better have good taste."
    n 2uchgnelg "Ahaha!"

    if hide_music_player:
        $ jn_custom_music.hideMusicPlayer()

    return

# Natsuki's thoughts on VTubers
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
    if Natsuki.isEnamored(higher=True):
        n 1tllss "VTubers,{w=0.1} huh?{w=0.2} You're asking {i}me{/i}?"
        n 4fnmsm "...Wow,{w=0.1} [player].{w=0.2} I'm impressed."
        n 4fsqsm "Yet again,{w=0.1} you've proved you're even more of a nerd than I am!"
        n 1uchsm "Ehehe."
        n 3klrbg "Relax!{w=0.2} Relax,{w=0.1} jeez!{w=0.2} You know I'd never seriously judge your hobbies,{w=0.1} you dummy."
        n 1unmaj "But yeah,{w=0.1} anyway..."

    elif Natsuki.isHappy(higher=True):
        n 1unmbg "Yeah!{w=0.2} I think I know those!"
        n 4tnmpu "They're those people with the anime avatars that stream stuff online for people,{w=0.1} right?"
        n 2tllpu "Well..."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "Huh?{w=0.2} VTubers?{w=0.2} Like those people with the anime-style avatars that play games and stuff online for people to watch?"
        n 4tnmpu "That {i}is{/i} what you mean,{w=0.1} right?"
        n 2tllpu "Well..."

    elif Natsuki.isDistressed(higher=True):
        n 2fsqpu "No,{w=0.1} I do not.{w=0.2} I'd rather be playing the game myself than watching someone play it for me."
        n 1fsqbo "If you follow any,{w=0.1} good for you."
        n 4flrbo "{i}Some{/i} of us don't have the time to sit around on our butt for hours..."
        n 1fsqaj "...Or the money to just give it away to strangers."
        n 2fsqpu "[player]."
        n 1fsqsrtsb "How much are we betting you aren't {i}nearly{/i} as toxic to {i}them{/i} as you are to me, huh?"
        return

    else:
        n 2fsqantsb "No.{w=0.2} And I couldn't give less of a crap if you did,{w=0.1} either."
        n 2fnmpultsf "...And hey,{w=0.1} newsflash,{w=0.1} idiot."
        n 1fsqupltse "Throwing money at a stranger hiding behind a cutesy picture doesn't make you any less of a {b}jerk{/b}."
        return

    n 1nchsm "It's definitely a cool idea!{w=0.2} It lets people share their passions and experiences with others behind a new persona..."
    n 3fllpo "Without having to worry about baggage following them into their personal lives,{w=0.1} or people being creeps,{w=0.1} or stuff like that."
    n 1uwdem "A lot of them even make full-blown careers out of it: merchandise,{w=0.1} song releases and everything -{w=0.1} just like idols!{w=0.2} It's crazy!"
    n 4tllem "That being said..."
    n 1tnmbo "I never really got into that sort of thing myself."
    n 2klrss "Like...{w=0.3} don't get me wrong!{w=0.2} I'm sure they're pretty fun to watch.{w=0.2} If you're into that kind of thing,{w=0.1} I mean."
    n 1nllsl "But I'd rather be playing or doing something {i}myself{/i} than watching someone else do it,{w=0.1} usually."
    n 1nllss "That might just be me,{w=0.1} though."
    n 4nllbg "Ehehe."
    n 4unmaj "What about you,{w=0.1} [player]?{w=0.2} Are you into that sort of stuff?"
    n 1fcssm "Wait,{w=0.1} wait!{w=0.2} Don't bother answering that."
    n 3tsqsm "You {i}did{/i} ask me about them,{w=0.1} after all -{w=0.1} I think that speaks for itself,{w=0.1} wouldn't you agree?"
    n 3uchbselg "Ahaha!"
    return

# Natsuki discusses her skateboarding past, and why she used to use one
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
    if Natsuki.isEnamored(higher=True):
        n 1fchbs "You bet I am,{w=0.2} [player]!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."
        n 3tllbg "But how'd you guess?{w=0.5}{nw}"
        extend 3tnmbg " Do I look the type or something?"
        n 1tlrsm "Well,{w=0.2} whatever."

    elif Natsuki.isHappy(higher=True):
        n 1uchsm "Ehehe.{w=0.5}{nw}"
        extend 4fchbg " You bet!"
        n 3uwlbg "Good guess,{w=0.2} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1ullaj "I...{w=0.3} am,{w=0.2} actually.{w=0.5}{nw}"
        extend 3tllss " How'd you guess?"
        n 4unmss "Well,{w=0.2} anyway."

    elif Natsuki.isDistressed(higher=True):
        n 3fupemesi "Ugh..."
        n 1fnmbo "Yes,{w=0.2} [player].{w=0.2} I'm a skateboarder.{w=0.2} I skateboard.{w=0.5}{nw}"
        extend 2fsqsf " Is that a problem or something?"
        n 1fllpu "It's just a convenient way to get around.{w=0.5}{nw}"
        extend 2fsqpu " An {i}affordable{/i} way."
        n 1flrsl "..."
        n 1flraj "...Yeah.{w=0.2} I don't have much else to say about it.{w=0.5}{nw}"
        extend 1fnmbo " But hey."
        n 2fsgaj "Not like you'd really care to listen anyway...{w=0.5}{nw}"
        extend 2fsqsftsa " isn't that right,{w=0.2} {i}[player]{/i}?"
        return

    else:
        n 2fsqanean "...And since when did {i}you{/i} give a crap about my hobbies and interests?"
        n 1fcsan "..."
        n 1fnmsf "Yes,{w=0.2} [player].{w=0.5}{nw}"
        extend 2fsqsftsb " I {i}do{/i} enjoy skateboarding."
        n 1fsqupltsb "And I'd rather be doing that than be stuck here talking to {i}you{/i}.{w=0.5}{nw}"
        extend 2fcsanltsa " Jerk."
        return

    n 1tchbg "I'm a skater girl alright!{w=0.5}{nw}"
    extend 2tslbo " Or...{w=0.3} was?"
    n 1tllss "Though...{w=0.3} not really by choice.{w=0.5}{nw}"
    extend 4knmaj " Bikes are {i}expensive{/i},{w=0.2} [player]!"
    n 2kllun "And I could never rely on lifts from my...{w=0.3} folk,{w=0.3}{nw}"
    extend 1kllss " so I saved up all I could,{w=0.3}{nw}"
    extend 1fcsbg " and got a board the first chance I had!"
    n 4nsqaj "Seriously.{w=0.75}{nw}"
    extend 2fllpusbr " You have no {i}idea{/i} how many lunches I skipped to earn that thing."
    n 1unmbg "But it was actually super convenient!{w=0.5}{nw}"
    extend 3flrbg " I didn't have to worry about locking it up somewhere,{w=0.2} or some jerk damaging it..."
    n 1fchsm "I could just pick it up and take it around with me,{w=0.2} or toss it in my locker."
    n 2nslsssbl "I mean...{w=0.3} I don't need it so much {i}now{/i},{w=0.2} but..."
    n 4fsqss "You gotta admit,{w=0.2} [player] {w=0.2}-{w=0.2} I'm nothing if not resourceful!{w=0.5}{nw}"
    extend 1fchsm " Ahaha."

    n 2fllss "I...{w=0.75}{nw}"
    extend 2nslsl " never really got super into tricks or anything though."
    n 1fwdgsesh "D-{w=0.2}don't get me wrong!{w=1}{nw}"
    extend 3fcsgsl " It isn't like I couldn't ace them!"
    n 1fcstrlesi "I totally could!{w=1}{nw}"
    extend 2kslcal " But..."
    n 1knmemsbl "I don't think I could {i}stand{/i} the thought of breaking it by accident."
    n 4kslunsbr "Not after all that effort."

    n 1kcsaj "...Yeah,{w=0.2} yeah.{w=0.5}{nw}"
    extend 2fcspo " Not very {i}radical{/i} of me,{w=0.2} huh?"

    if (
        not jn_outfits.getOutfit("jn_skater_outfit").unlocked
        and Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):
        # Unlock skater outfit, if custom outfits unlocked
        n 1tslsl "..."
        n 4uwdajesu "Oh!{w=0.5}{nw}"
        extend 1fsqbs " But you know what {i}totally{/i} was,{w=0.2} [player]?{w=1}{nw}"
        extend 3fllbgsbl " Radical,{w=0.2} I mean."
        n 1uchgn "...My favorite skateboarding outfit,{w=0.2} of course!"
        n 3tllss "In fact,{w=0.75}{nw}"
        extend 1fchbg " I probably still have it around here somewhere too!{w=0.75}{nw}"
        extend 1ullaj " I usually brought it around with me anyways."
        n 3fcsajsbl "O-{w=0.2}only for going back and forth from school though!{w=0.75}{nw}"
        extend 3nslsssbl " It isn't exactly following the dress code..."
        n 1nslbosbl "But...{w=0.75}{nw}"
        extend 1tsqem " I wasn't exactly gonna make my uniform all sweaty for rest of the day either."
        n 2fsrpu "...Ew."
        n 1ulrpu "Well,{w=0.2} anyway.{w=1}{nw}"
        extend 1unmaj " I'm not gonna go look for it now though,{w=0.75}{nw}"
        extend 1nnmpu " but I think we can both agree."
        n 3fcsss "If you're gonna skateboard..."
        n 3uchgn "You gotta follow {w=0.2}{i}all{/i}{w=0.2} the rules of cool!{w=0.75}{nw}"
        extend 1fchsmeme " Ehehe."

        $ jn_outfits.getOutfit("jn_skater_outfit").unlock()

    else:
        n 2ullpo "But...{w=0.5} enough of that for now.{w=0.5}{nw}"
        extend 1fnmsm " Besides,{w=0.2} [player]..."
        n 4fsqss "I can tell when you're getting...{w=0.3} {i}board{/i}."
        n 1fchsm "Ehehe.{w=0.5}{nw}"
        extend 1uchgn " No regrets,{w=0.2} [player]!"

    return

# Natsuki describes her experiences with sports at school
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
    if Natsuki.isAffectionate(higher=True):
        n 4unmaj "Huh?{w=0.2} Sports?"
        n 1fllss "I...{w=0.3} don't like to have to break it to you,{w=0.1} [player]..."
        n 3fchgn "But what kind of sports do you think I can play in a single room?{w=0.2} By myself?{w=0.2} With no gear?"
        n 1kllbg "Jeez...{w=0.5}{nw}"
        extend 1tnmss " you're such a dope sometimes,{w=0.1} [player]."
        n 1ullbg "Well,{w=0.1} anyway."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "Eh?{w=0.2} Sports?"
        n 3tnmdv "You...{w=0.3} do know it's kinda hard to stay active in a single room,{w=0.1} right?"
        n 1fcsss "Ehehe.{w=0.5}{nw}"
        extend 1ullss " Well,{w=0.1} anyway."

    elif Natsuki.isDistressed(higher=True):
        n 1nsqpu "Yeah,{w=0.1} no.{w=0.5}{nw}"
        extend 2fsqsl " I don't {i}now{/i},{w=0.1} if that's what you're asking."
        n 1fllpu "..."
        n 1fsqan "...And no,{w=0.2} we didn't wear the sort of uniforms I bet {i}you're{/i} thinking of."
        n 1fsqsr "Does that answer your question?{w=0.5}{nw}"
        extend 2fslbo " Whatever."
        n 1fcsbo "Moving on."
        return

    else:
        n 1fsqan "I don't {i}now{/i},{w=0.1} if you {i}somehow{/i} hadn't already noticed."
        n 1fslsl "..."
        n 1fsqpu "..."
        n 2fcsemtsa "...Do I even want to know why you asked?"
        n 2fcsanltsd "...No.{w=0.75} I {i}don't{/i}."
        return

    n 1nnmaj "I try to keep up how I can.{w=0.2} I can't do laps or anything,{w=0.5}{nw}"
    extend 3fcsbg " but I can easily get some stretches and jumping jacks in!"
    n 1ullpu "Of course school was always a lot more varied with activities,{w=0.2} but...{w=0.5}{nw}"
    n 4tllsr "I always kinda struggled to keep up,{w=0.2} I guess."
    n 2nslsssbr "...Maybe I just don't have much stamina."

    # Check to see if the player and Natsuki have discussed how she skipped lunches to save money
    $ already_discussed_skateboarding = get_topic("talk_skateboarding").shown_count > 0
    if already_discussed_skateboarding:
        n 2nslpo "Probably didn't help myself saving for that skateboard..."

    n 1ullaj "Well,{w=0.1} whatever.{w=0.5}{nw}"
    extend 1nnmbo " I wasn't {i}really{/i} that into sports anyway."
    n 1nlrca "..."
    n 4unmbs "Oh!{w=0.2} Oh!{w=0.2} But you know who was?{w=0.5}{nw}"
    extend 4fsqbg " I bet you do,{w=0.1} huh?{w=0.5}{nw}"
    extend 4fcssm " Ehehe."
    n 1tsqss "And that's...{w=0.5}{nw}"
    extend 3fchgn " ...{w=0.3}Sayori,{w=0.1} duh!"
    n 1uskgs "I mean,{w=0.1} really!{w=0.2} You should have seen her!{w=0.5}{nw}"
    extend 1fnmca " She was a {i}menace{/i}!"
    n 4uskaj "...Seriously!{w=0.5}{nw}"
    extend 3fnmpo " You don't believe me?"
    n 3fspgs "She was so fast!{w=0.2} Just a flash of orange fluff and messy gym clothes...{w=0.5}{nw}"
    extend 1fbkwr " and then boom!{w=0.2} Tackled!"
    n 3fllpol "And off she'd skip,{w=0.1} merrily into the sunset..."
    n 1tsqaj "...Yeah.{w=0.2} If Sayori was on your side?{w=0.5}{nw}"
    extend 1fllbg " You {i}knew{/i} your team wasn't going to be packing everything away in defeat."
    n 1ullaj "I mean,{w=0.3}{nw}"
    extend 1nnmbo " Monika was always pretty good at sports too,{w=0.1} obviously.{w=0.5}{nw}"
    extend 3nsgca " But {i}nobody{/i} outran Sayori,{w=0.1} [player].{w=0.2}"
    n 1nsqun " N{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}b{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}d{w=0.1}-{w=0.1}y."
    n 4fchbg "...When she remembered to tie her laces anyway.{w=0.5}{nw}"
    extend 4fchsm " Ehehe."
    return

# Natsuki laments her frustrations with online shopping, and the disappearance of physical stores
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
    if Natsuki.isNormal(higher=True):
        n 1ullaj "You know,{w=0.1} it's kinda crazy how common online shopping is nowadays."
        n 4uwdaj "I mean,{w=0.1} don't get me wrong!{w=0.5}{nw}"
        extend 1fcsbg " It's super convenient!{w=0.2} You don't even need to leave your house!"
        n 3fllpo "So don't think I'm just complaining,{w=0.1} or anything like that.{w=0.5}{nw}"
        extend 1ullpu " But..."

    else:
        n 1nllsl "It's funny how common online shopping is nowadays."
        n 1nlrsl "I guess I'm not really complaining though.{w=0.5}{nw}"
        extend 1nlrpu " It {i}is{/i} pretty convenient."
        n 2ulrpu "But...{w=0.5}{nw}"
        extend 1nnmsf " I still think it's a shame how people miss out on an actual experience."
        n 2fllsl "I'd never pass up on an afternoon just flicking through books at my favorite bookstore."
        n 1fcssf "...Which is somewhere I'd {i}much{/i} rather be.{w=0.5}{nw}"
        extend 4fsqan " {i}Shockingly{/i}."
        return

    n 1fllbg "I don't think it's the be-all and end-all,{w=0.1} you know."
    n 4unmaj "I mean...{w=0.3} think about it,{w=0.1} [player]."
    n 3fllaj "I guess it's cheaper if you don't have to think about getting somewhere,{w=0.1} or parking or whatever."
    n 1knmpu "But wouldn't you like to {i}see{/i} what you're paying for?{w=0.5}{nw}"
    extend 1fnmaj " Especially if it's super expensive!"
    n 1fllpu "Or sometimes...{w=0.5}{nw}"
    extend 3fslbo " even if it isn't!"
    n 3fllpo "I can't be the only one that's been burned by something that turned out to be junk,{w=0.1} or broken,{w=0.1} right?"
    n 1fnmem "And you don't even know it would be like that until it's on your doorstep!{w=0.5}{nw}"
    extend 1fcsan " Then you gotta send it back!{w=0.5}{nw}"
    extend 2fslem " Ugh."

    # Check to see if the player and Natsuki have discussed careful spending
    if get_topic("talk_careful_spending").shown_count > 0:
        n 1fllsl "Not only that..."
        n 1fnmpu "I think I mentioned before how shops make it really easy to spend money...{w=0.5}{nw}"
        extend 4fbkwr " but that's even easier online!{w=0.5}{nw}"
        extend 4kbkgs " It doesn't even {i}feel{/i} like spending money properly!"
        n 1fcsan "Sheesh."

    n 1fcsem "That aside..."
    n 2kllsl "It...{w=0.3} also made me kinda sad seeing all the closed stores when I went out,{w=0.1} too."
    n 1tnmsl "I suppose you could say that's just business,{w=0.1} and they lost out."
    n 4flrsll "But that doesn't mean I {i}didn't{/i} miss some of them."
    n 1ncsem "I don't know.{w=0.2} I guess what I'm saying is..."
    n 3fllpo "Don't just instantly write off anything you can't do or buy digitally,{w=0.1} [player]."
    n 1knmaj "There's still merit in getting your stuff physically!"
    n 4fnmss "And to be completely honest?"

    if Natsuki.isEnamored(higher=True):
        n 1fsqbg "I don't really care how much you protest."
        n 3fchgn "We're definitely hitting some {i}real{/i} bookstores eventually {w=0.1}-{w=0.1} whether you like it or not!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 3fchgn "You gotta be kidding if you think I'm letting you miss out on {i}real{/i} bookstores!{w=0.5}{nw}"
        extend 1nchbg " Ahaha."

    else:
        n 3fchbg "If there's one thing I'm gonna teach you eventually,{w=0.1} it's experiencing a {i}real{/i} bookstore!{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    return

# Natsuki hates forced subscription services, and accidentally paying for trial periods
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
    n 3fcsan "Man,{w=0.1} that's {i}such{/i} a pain!{w=0.5}{nw}"
    extend 1fbkwr " I thought I cancelled thaaat!"
    n 3fslpo "..."
    n 4uwdemesu "O-{w=0.1}oh!{w=0.2} [player]!{w=0.5}{nw}"
    extend 2flremsbl " Can you {i}believe{/i} this?"
    n 1fslem "I signed up to some free trial for a streaming website,{w=0.3}{nw}"
    extend 1fcsup " but I totally forgot about it!{w=0.5}{nw}"
    extend 2flrwr " And now I gotta pay for something I barely even {i}used{/i}!"
    n 1fcsem "Jeez...{w=0.5}{nw}"
    extend 1tnmem " doesn't that wind you up too?"
    n 1tllbo "In fact,{w=0.1} thinking about it..."
    n 2fnmbo "Why is so much stuff nowadays all subscription based?"
    n 1fllpu "Like...{w=0.5}{nw}"
    extend 1nnmaj " I get it if it's like an ongoing thing,{w=0.3}{nw}"
    extend 2flrsl " but what's up with everyone and their {i}dog{/i} trying to sign you up?!"
    n 1fsqsl "And half the time you don't even get a choice...{w=0.5}{nw}"
    extend 1fsqem " like with software!"
    n 1fcsan "I've had to skip out on so many programs because they want me to pay for a whole bunch of crap in a package I don't care about!"
    n 3fllan "Like...{w=0.3} come {i}on{/i}!{w=0.5}{nw}"
    extend 3fslfrean " Just let me pay for what I need!"
    n 1kcsemesi "Ugh..."
    n 1fnmsl "The worst part is that it all adds up too!{w=0.5}{nw}"
    extend 1fllpu " It's super easy to lose track of what you're paying for each month..."
    n 1fnmpu "And then before you know it,{w=0.3}{nw}"
    extend 3fbkwr " half your money is down the drain as soon as it comes in!{w=1.25}{nw}"
    extend 3ncspuesd " What a mess..."
    n 1ullaj "I mean,{w=0.1} don't get me wrong.{w=0.2} There are {i}other{/i} ways of getting stuff {w=0.1}-{w=0.3}{nw}"
    extend 4fsqdv " you probably know that already."
    n 2tlrsl "But I wanna support {i}actual{/i} creators too,{w=0.1} you know?"
    n 1fcssl "..."
    n 3fllpo "Well,{w=0.1} whatever.{w=0.2} At least I won't get charged for {i}that{/i} again.{w=1.25}{nw}"
    extend 3fslpo " Jerks."
    n 1nllbo "But...{w=0.5}{nw}"
    extend 4unmpu " what about you though,{w=0.1} [player]?{w=0.5}{nw}"
    extend 4fsqsm " Actually,{w=0.1} I can tell you one thing."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqssl "A-{w=0.1}at least you have {i}one{/i} subscription you don't have to worry about paying for!"

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=0.5}{nw}"
            extend 4uchbgf " Love you,{w=0.1} dork!"

        else:
            n 2fllbgl "A-{w=0.1}ahaha..."

    else:
        n 3fcsbg "You're already subscribed to some pretty pro thinking,{w=0.1} if I say so myself."
        n 1nsqsg "Fortunately for you though,{w=0.1} I don't charge.{w=0.5}{nw}"
        extend 4fsqss "...Yet."
        n 1fchsm "Ehehe."

    return

# Natsuki discusses the possibility of the player contributing to JN (and praises the JN team)
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_mod_contributions",
            unlocked=True,
            prompt="Contributions",
            conditional=(
                "not jn_activity.ACTIVITY_SYSTEM_ENABLED "
                "or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
            ),
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
    n 2klrbg "I don't think I'd {i}ever{/i} be able to handle doing everything that lets you visit me.{w=0.5}{nw}"
    extend 1klrsl " Not by myself."
    n 4uskeml "I-I mean,{w=0.1} I'm good!{w=0.5}{nw}"
    extend 2fnmpol " D-{w=0.1}don't get me wrong!"
    n 2kllpo "I'm just not...{w=0.3} {i}that{/i} good.{w=0.5}{nw}"
    extend 2fslpo " Yet."
    n 1uchbg "But that's why I'm super grateful there's a whole bunch of people dedicated to helping me out!{w=0.5}{nw}"
    extend 1fchsm " Isn't that awesome?"
    n 4fslsl "I always found all the programming stuff kinda confusing,{w=0.3}{nw}"
    extend 1kllss " so I have no idea where I'd be without them!"
    n 3ksqsg "...Even if they {i}are{/i} a bunch of total nerds.{w=0.5}{nw}"
    extend 3uchgn " Ehehe."
    n 1ulraj "So...{w=0.3} where am I going with this,{w=0.1} you ask?{w=0.5}{nw}"
    extend 4tslsm " Well..."

    if not jn_activity.ACTIVITY_SYSTEM_ENABLED:
        n 1tllss "I don't know if you're into that sort of thing yourself,{w=0.1} [player]..."
        n 1fchbg "But why not lend me a hand?"

    else:
        n 2fsqsg "I couldn't help but notice the sort of programs you've been poking around on,{w=0.1} [player]."
        n 1ksqss "What?{w=0.5}{nw}"
        extend 1fchbg " You didn't seriously expect me to not see what you're up to?{w=0.5}{nw}"
        extend 1nchgn " Ehehe."
        n 3tsqbg "Anyway -{w=0.1} if you're already into that kinda stuff,{w=0.1} [player]...{w=0.5}{nw}"
        extend 3kchbg " why not lend me a hand?"

    n 1kllbg "You don't even have to be super talented at code,{w=0.1} or anything like that!{w=0.5}{nw}"
    extend 4unmaj " Artwork,{w=0.1} writing,{w=0.1} or even just suggestions of things for us to talk about or do -{w=0.3}{nw}"
    extend 3uchbg " it's all super appreciated!"
    n 1tsqbg "Does that sound like your thing,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1uchsm " Of course it does!{w=0.2} Ehehe."
    n 1unmbg "Well,{w=0.1} don't let me hold you back!{w=0.5}{nw}"
    extend 4uchbgl " You can check out my website {a=[jn_globals.LINK_JN_GITHUB]}here{/a}!"
    n 3nsqbg "A little look can't hurt,{w=0.1} right?{w=0.5}{nw}"
    extend 3nchsm " Ahaha."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1nchtsl "Love you,{w=0.1} [chosen_endearment]!"

    else:
        n 1fchbg "Thanks,{w=0.1} [player]!{w=0.2} 'preciate it!"

    return

# Natsuki ponders her new understanding of the separation between the player and MC as entities
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_player_ddlc_actions",
            unlocked=True,
            prompt="DDLC memories",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 60 >= 30",
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
    n 2kslsl "...This."
    n 1unmaj "You've been here all this time,{w=0.1} right?{w=0.5}{nw}"
    extend 2tslbo " But then,{w=0.1} that would mean..."
    n 4tsqfr "The guy who actually joined the club...{w=0.5}{nw}"
    extend 1nlrss " whatever his name was."
    n 2fsrbo "He wasn't {i}actually{/i} in control of anything,{w=0.1} was he?{w=0.5}{nw}"
    extend 1ulraj " Not even himself."
    n 1nnmsr "...You were.{w=0.5}{nw}"
    extend 4nlrsl " In control of him,{w=0.1} I mean."
    n 1nsrbo "..."

    # We assume the player romanced Natsuki, until we get import scripts
    n 1nsraj "So...{w=0.3} if he was being that nice to me..."
    n 2klrajl "T-{w=0.1}then that would mean...{w=0.5}{nw}"

    if Natsuki.isLove(higher=True):
        n 2klrsml "..."
        n 1kcsssl "Heh,{w=0.1} what am I even saying.{w=0.5}{nw}"
        extend 1kwmsml " Just because you clicked stuff {w=0.1}-{w=0.1} {i}when you were allowed,{w=0.1} anyway{/i} {w=0.1}-{w=0.1} doesn't make you the same."
        n 1tllssl "Either way,{w=0.1} [player]?"
        n 4ksqsml "I'm definitely not complaining.{w=0.5}{nw}"
        extend 4nchsml " Ehehe."

    else:
        extend 1fskeml " -urk!"
        n 2fcsanf "Nnnnn-!"
        n 1fllunf "..."
        n 2fnmssl "A-{w=0.5}{nw}"
        extend 2fcsbgl "ha!"
        n 4fcsbsl "Haha!{w=2}{nw}"
        extend 1flleml " What am I even saying?!"
        n 2fcswrl "J-{w=0.1}just because you picked some words and clicked a few buttons doesn't make you the same!"
        n 2fllpol "..."
        n 1nlleml "A-{w=0.1}although..."

        if Natsuki.isEnamored(higher=True):
            n 3fcsajl "Don't think I'm complaining or anything like that.{w=0.5}{nw}"
            extend 3nlrssl " Ehehe..."

        elif Natsuki.isHappy(higher=True):
            n 1fcsajl "You're already proving that well enough.{w=0.5}{nw}"
            extend 2fllunl " I-{w=0.1}I think."

        else:
            n 1fcsajl "I-{w=0.1}I guess that at {i}least{/i} means you have good taste.{w=0.5}{nw}"
            extend 2fllunl " I suppose that counts for something."

    if Natsuki.isLove(higher=True):
        n 1klrss "But yeah,{w=0.1} so..."

    elif Natsuki.isEnamored(higher=True):
        n 4ksrss "A-{w=0.1}anyway..."

    elif Natsuki.isHappy(higher=True):
        n 2flrun "A-{w=0.1}anyway."

    else:
        n 2flrun "A-{w=0.1}anyway!{w=0.5}{nw}"
        extend 1fcsaj " That's beside the point!"

    n 1kslsr "..."
    n 1ullaj "I guess what I'm trying to say is I still have all these memories of {i}that{/i} guy..."
    n 2nsrpu "And although he obviously wasn't you,{w=0.5}{nw}"
    extend 4tsraj " you kinda have {i}his{/i} memories too?{w=0.5}{nw}"
    extend 1tslem " And..."
    n 1fcsaj "...and..."
    n 2fcsan "..."
    n 1fcsem "Rrrgh,{w=0.1}{w=0.5}{nw}"
    extend 4fllem " this is so confusing!"
    n 2fcsemesi "Ugh...{w=0.5}{nw}"
    extend 2nnmpo " you know what?"

    if Natsuki.isAffectionate(higher=True):
        n 1nllss "It doesn't really matter at this point,{w=0.1} does it?"

    else:
        n 1fllbo "I'm just gonna start over.{w=0.5}{nw}"
        extend 1unmaj " Mentally,{w=0.1} I mean."

    n 1ncsaj "He was here {i}then{/i}."
    n 3fcssm "You are here {i}now{/i}."

    if Natsuki.isAffectionate(higher=True):
        n 1fchbg "And that's all there is to it."

        if Natsuki.isLove(higher=True):
            extend 1fchsm " Yep."
            n 1uchsml "Love you,{w=0.1} generic protag-{w=0.3}{nw}"
            n 3fllbgl "I mean,{w=0.5}{nw}"
            extend 3kchbgl " {i}[player]~{/i}."
            n 1fsqsml "..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 4uchbsl "Oh,{w=0.1} lighten up,{w=0.1} [chosen_tease]!"
            n 1fwrtsl "You should know I'd never mean it.{w=0.5}{nw}"
            extend 1fchctleme " Ehehe."

    else:
        n 1fllss "I-{w=0.1}I just gotta adjust,{w=0.5}{nw}"
        extend 2fllun " that's all."

    return

# Natsuki ponders the fates of the other girls, and her understanding of Monika's actions
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_other_girls",
            unlocked=True,
            prompt="Monika and the other girls",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0"
            ),
            category=["DDLC", "Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_other_girls:
    n 2kllun "..."
    n 1klrbo "Uhmm..."
    n 4knmaj "Hey...{w=0.3} [player]?"
    n 1knmsf "I've...{w=0.3} been thinking again.{w=0.5}{nw}"
    extend 1kllsf " About before."
    n 2kslss "I guess I really was onto something when I said Monika was acting weird."
    n 1kskem "D-{w=0.1}don't get me wrong!{w=0.5}{nw}"
    extend 1kllsf " I'm not happy about being right or anything.{w=0.5}{nw}"
    extend 4kwmsr " ...At all."
    n 1kcssr "In fact..."
    n 2klrpu "I really wish that I was wrong."
    n 1knmaj "I-"
    n 1kcsunl "..."
    n 2kplun "I honestly just thought it was all the school work and the festival stuff getting to her,{w=0.5}{nw}"
    extend 1kslpu " or something."
    n 1tslpu "But...{w=0.5}{nw}"
    extend 4kplsr " in hindsight?"
    n 1klrun "..."
    n 1kcsaj "...I think I actually got off {i}lightly{/i}."
    n 3knmsl "I mean...{w=0.3} she messed with all of us.{w=0.5}{nw}"
    extend 3klrsf " In some way or another."
    n 1klraj "But...{w=0.5}{nw}"
    extend 2fcsupl " I just didn't know how much she {i}hurt{/i} everyone else..."
    n 1fcsunl "..."
    n 4kplunl "Sayori was the happiest person I thought I knew,{w=0.1} [player]."
    n 1kskunl "A-{w=0.1}and Yuri...{w=0.5}{nw}"
    extend 2kllupl " I don't..."
    n 1kcsupl "..."
    n 1fcsunl "..."
    n 1kcsaj "...Sorry."
    n 1kcssr "..."
    n 2kllpu "I...{w=2}{nw}"
    extend 2knmsr " we never saw eye-to-eye.{w=0.2} I always knew she had her insecurities."
    n 1kslbo "...So did I."
    n 1kcsanl "But...{w=0.3} {i}that{/i}..."
    n 1kcsunl "..."
    n 1kcspu "..."
    n 2fcsanl "I...{w=1} don't...{w=1} hate...{w=0.5} Monika."
    n 1fcsun "I...{w=0.3} understand how she felt.{w=0.2} I {i}know{/i} how she felt."
    n 4fsqsr "It's {i}terrifying{/i},{w=0.1} [player]."
    n 1kcsanl "But I'll never understand why she felt she had to do {i}that{/i}.{w=1}{nw}"
    extend 4kplpu " Surely...{w=0.3} there was another way?"
    n 1kllsl "..."
    n 2kcspu "...I don't know.{w=0.5}{nw}"
    extend 2kslsssbl " I guess I should just be glad she deleted me before..."
    n 1kskuni "B-{w=0.5}before..."
    n 1kcsun "..."
    n 2kslun "Uhmm..."
    n 1kcspu "...Sorry.{w=0.2} I really don't wanna talk about all this any more,{w=0.1} [player]."
    n 4kllsrl "But...{w=0.3} thanks.{w=0.5}{nw}"
    extend 4flrpol " F-{w=0.1}for listening,{w=0.1} I mean."

    if Natsuki.isAffectionate(higher=True):
        n 2klrpol "..."
        n 1kcspul "...And for rescuing me too."

        if Natsuki.isLove(higher=True):
            n 4kwmsml "I'll never,{w=0.1} ever forget that,{w=0.1} [player]."

    else:
        n 1ncspu "..."

    return

# Natsuki muses over the possibility of leaving the space classroom, and the risks involved
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_space_classroom",
            unlocked=True,
            prompt="Leaving the space classroom",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0 "
                "and get_topic('talk_realizations_other_girls').shown_count > 0"
            ),
            category=["DDLC", "Natsuki", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_space_classroom:
    n 1kllsr "Uhmm..."
    n 1klrpu "So,{w=0.1} this room..."
    n 2nsrss "I...{w=0.3} still haven't actually left it.{w=0.5}{nw}"
    extend 2tnmsl " Since you brought me back and all."
    n 1fllssl "I-{w=0.1}I mean,{w=0.5}{nw}"
    extend 4fcseml " it's not like I can't!"
    extend 4unmbo " I'm actually pretty sure I could."
    n 1kllsf "It's just...{w=0.5}{nw}"
    extend 1knmaj " I have no idea what would happen!"
    n 2tllaj "Would I like...{w=0.3} break?{w=0.5}{nw}"
    extend 2tnmun " Or just stop existing?"
    extend 4kskem " Could I even {i}come{/i} back?!"
    n 1klrun "..."
    n 1kcspu "I miss my bed,{w=0.1} [player].{w=1}{nw}"
    extend 2knmem " I miss having blankets and pillows!{w=1}{nw}"
    extend 2ksrsr " And all my stuff."
    n 1kcssr "Even if it doesn't exist anymore.{w=0.5}{nw}"
    extend 2tslaj " Never existed at all?{w=0.5}{nw}"
    extend 1kcsem " Whatever."
    n 1kllsr "But..."
    n 4ksqun "I really don't feel like taking a chance and finding out what would happen if I left.{w=0.5}{nw}"
    extend 2flrsl " Not yet."
    n 1kcssf "..."
    n 1kcspu "Just...{w=0.5}{nw}"
    extend 3fcsaj " give me some time,{w=0.1} alright?{w=0.5}{nw}"
    extend 1fnmbo " I'll try and think of something soon."
    n 3kllpo "I don't exactly wanna be stuck here either,{w=0.1} after all..."

    return

# Natsuki discusses how she feels about lightning
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_lightning",
            unlocked=True,
            prompt="Are you afraid of lightning?",
            category=["Fears", "Weather"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_lightning:
    if Natsuki.isAffectionate(higher=True):
        n 2fllpol "..."
        n 1fllajl "...So?"
        n 2fcseml "I-{w=0.1}I mean,{w=0.5}{nw}"
        extend 2flreml " I'm {i}obviously{/i} not,{w=0.5}{nw}"
        extend 2knmpol " but so what even if I was?"

    elif Natsuki.isNormal(higher=True):
        n 1fllwrl "N-{w=0.1}no!{w=0.5}{nw}"
        extend 2fcspol " Where'd you get that idea from?"
        n 2kslpol "I'm not afraid of lightning..."
        n 1fsrbo "..."
        n 1tsrpu "And come to think of it...{w=0.5}{nw}"
        extend 4tnmpo " why would you even {i}ask{/i} that?"

        if get_topic("talk_favourite_season").shown_count > 0:
            n 1tllss "I gotta say,{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
            extend 3tsqss " you've got a weird knack for asking me random stuff,{w=0.1} huh?"

        else:
            n 1tllss "It's a pretty random thing to ask,{w=0.1} I gotta say."

        n 1nlraj "But I mean,{w=0.1} putting all that aside..."

    elif Natsuki.isDistressed(higher=True):
        n 1fllpu "...And even if I {i}was{/i},{w=0.5}{nw}"
        extend 2fsqsr " do you {i}really{/i} think I'd want to share that with {i}you{/i} right now?"
        n 2fsqem "Like,{w=0.1} {i}seriously{/i} [player]?{w=0.5}{nw}"
        extend 2fcsem " Cut me a break."
        n 1fcssr "..."
        n 1fcsem "Besides,{w=0.5}{nw}"
        extend 2fllsr " I've seen the numbers from when I studied."
        n 4fsqpu "You'd have to be an idiot {i}not{/i} to at least wary of it."

        return

    else:
        n 1fcsan "Oh,{w=1.5}{nw}"
        extend 2fcsfultsaean " {i}{cps=\7.5}get lost{/cps}{/i},{w=0.3} [player]."
        n 1fsqanltseean "As if I'd want to talk about anything uncomfortable with the likes of {b}you{/b}!"

        return

    n 4uwdem "Lightning is no joke,{w=0.1} [player]!"
    n 1fllun "..."
    n 1knmem "...What?{w=1}{nw}"
    extend 2fllpo " I'm serious!"
    n 1knmun "Have you {i}seen{/i} the numbers on lightning?"
    n 1nnmaj "A typical strike is like 300 {i}million{/i} volts!{w=0.5}{nw}"
    extend 4uwdaj " With about 30 thousand amps!{w=1.5}{nw}"
    extend 2nllan " Yeesh!"
    n 1nsqun "...And for perspective?{w=0.5}{nw}"
    extend 1tsqpu " The current in your home?"
    n 2nsrss "Around 120-{w=0.1}230 volts.{w=1.5}{nw}"
    extend 1nsqun " ...15-{w=0.1}30 amps."
    n 4fspgs "That's one {i}hell{/i} of a lotta juice!"
    n 1klrpu "A-{w=0.1}and it just falls out of the sky!{w=0.5}{nw}"
    extend 2knmaj " Constantly!"
    n 2fsqaj "And I mean {i}constantly{/i},{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
    extend 2nllan " 44 strikes every {i}second{/i}!"
    n 1fsqun "Then there's the sound,{w=0.1} too!{w=0.5}{nw}"
    extend 4kslun " Especially if its close!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 2fllsr "I mean,{w=0.1} I'm pretty sure I told you before that I hate cheap jumpscares."
        n 1fbkwrl "So how do you think I feel about {i}nature{/i} trying to pull that crap?!"

    else:
        n 1fbkwrl "It's such a cheap fright!"

    n 2fcsaj "Jeez..."
    n 1fllss "But yeah,{w=0.1} a-{w=0.1}anyway."
    n 4unmaj "I'll spare you a lecture on staying safe in lightning storms.{w=0.5}{nw}"
    extend 4fsrss " You should {i}really{/i} know all that by now anyway."
    n 1ulraj "But..."
    n 3fsqsg "I just have one question for you,{w=0.1} [player]."

    if preferences.get_volume("sfx") == 0:
        # Player has sound disabled, so we skip the prank
        n 3fsqss "Are {i}you{/i} scared of lightning?"
        n 1tsqsm "..."
        n 1fsqbg "What?"
        n 4usqsg "I'm allowed to ask too,{w=0.1} aren't I?{w=0.5}{nw}"
        extend 4nchgn " Ehehe."

    else:
        # We store the current sfx preference so we don't mess up the player's settings with the prank
        $ previous_sfx_setting = preferences.get_volume("sfx")
        $ preferences.set_volume("sfx", 1)

        n 1fsqsm "Ehehe."
        n 1fsqbg "Are {i}you{/i} scared of light{nw}"

        play audio smack
        with Fade(.1, 0.25, .1, color="#fff")
        $ preferences.set_volume("sfx", previous_sfx_setting)

        n 3uchgnelg "..."
        n 3kchbg "Sorry,{w=0.1} sorry!{w=0.5}{nw}"
        extend 1fchsm " I had to!{w=0.5}{nw}"
        extend 1kchbg " I just {i}had{/i} to!"
        n 4nsqsm "Ehehe."
        n 1tsqss "Well,{w=0.5}{nw}"
        extend 3fchtsl " they don't call it a thunder-{w=0.5}{i}clap{/i}{w=0.5} for nothing!~"

    return

# Natsuki almost falls asleep, jolts awake and then discusses how to combat drowsiness
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fighting_drowsiness",
            unlocked=True,
            prompt="Drowsiness",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12",
            category=["Health"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fighting_drowsiness:
    n 1nllpu "...{w=2}{nw}"
    n 1nslpu "...{w=3}{nw}"
    n 1ncsbo "...{w=4}{nw}"
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    $ jnPause(4)
    n 1fcsbo "..."
    n 1nsqpu "Mmmmm...{w=0.5}{nw}"
    extend 1tsqsr " mmmnn?"
    n 4uskemesh "...!{w=0.5}{nw}"
    n 2ullwrl "W-{w=0.1}woah!{w=0.5}{nw}"
    extend 2flrss " Ahaha..."
    n 1nsrss "I...{w=0.3} haven't been getting much sleep here,{w=0.1} as you can guess."
    n 1kcsun "Uuuuuu...{w=0.5}{nw}"
    extend 1kslpu " I gotta wake up..."
    n 1kcssr "..."
    n 4unmbo "You know what?{w=0.5}{nw}"
    extend 1ullss " I'll just...{w=1}{nw}"
    extend 2nslss " be right back...{w=1}{nw}"

    play audio chair_out_in
    with Fade(out_time=0.25,hold_time=5,in_time=0.25, color="#000000")

    n 1nchbg "Okaaay!{w=0.5}{nw}"
    extend 1fchsm " We're back in business!"
    n 1nnmaj "I'll tell you,{w=0.1} [player].{w=0.5}{nw}"
    extend 3fchbg " If there's one thing I know,{w=0.1} it's how to shake off the drowsiness!"
    n 1fsqsm "..."
    n 1fsqcs "Oho?{w=0.5}{nw}"
    extend 3tsqaj " And what's that I hear?{w=0.5}{nw}"
    extend 3tllss " How do I do it,{w=0.1} you ask?"
    n 1fsqsg "Ehehe.{w=0.5}{nw}"
    extend 3usqsg " Well aren't {i}you{/i} in luck,{w=0.1} [player].{w=0.5} 'Cause..."
    n 1uchgn "It's time for a Natsuki pro-tip!"
    n 4fnmaj "So!{w=0.2} First order of business...{w=0.5}{nw}"
    extend 1fcsbg " hydration,{w=0.1} obviously!"
    n 1ullaj "It's actually pretty easy to forget how much fluid you need per day...{w=0.5}{nw}"
    extend 1unmbo " and how {i}often{/i} you should be drinking!"
    n 2tlrss "You should be taking in something like six to eight glasses of water a day,{w=0.3}{nw}"
    extend 1fcsaj " but not all at once!"
    n 1ullaj "It isn't hard to space it out through the whole day {w=0.1}-{w=0.1} just start early and keep at it.{w=0.5}{nw}"
    extend 3fchsm " Easy peasy!"
    n 4fnmaj "Next up: exercise!"
    n 1tsqsm "Yeah,{w=0.1} yeah.{w=0.2} I know,{w=0.1} I know.{w=0.5}{nw}"
    extend 2fslss " We all just {i}love it{/i},{w=0.1} don't we?"
    n 1unmaj "Don't think you have to go crazy or anything though -{w=0.5}{nw}"
    extend 2flrbg " I sure don't!"
    n 1unmbo "People {i}say{/i} an hour a day is good,{w=0.5}{nw}"
    extend 4fnmca " but honestly even a lap around the house trumps sitting on your butt,{w=0.1} [player]."
    n 3fcsss "It's just about moving around and giving your muscles a stretch,{w=0.1} that's all."
    n 1ulrpu "Lastly,{w=0.5}{nw}"
    extend 4fsqsm " and I {i}know{/i} you'll like this one,{w=0.1} [player]..."
    n 3fchgn "...Food!"
    n 1fllem "Of course you're gonna feel like crap if you aren't eating enough!"
    n 2kllsr "...And trust me on this one.{w=0.5}{nw}"
    extend 2ksrpu " I would know."
    n 1ksrun "..."
    n 3fcsajl "A-{w=0.1}anyway!"
    n 4fnmca "You wouldn't expect a car to run without fuel {w=0.1}-{w=0.1} and you're no different,{w=0.1} [player]."
    n 1ullaj "Don't go crazy though.{w=0.5}{nw}"
    extend 1nlrpu " Just grab an apple or something.{w=0.5}{nw}"
    extend 3fsqpo " Don't cheap out on your body with processed crap all the time."
    n 3tsqpo "...Or you'll feel like that too."
    n 1fchbg "But...{w=0.3} yeah!{w=0.5}{nw}"
    extend 1fchsm " That just about covers it!"
    n 1unmbg "So,{w=0.1} I-{w=0.5}{nw}"
    n 1nnmss "I...{w=1}{nw}"
    n 2nsqsr "...{w=2}{nw}"
    n 4fsqaj "[player]."
    n 3fsqpo "Were you actually listening?{w=0.5}{nw}"
    extend 1fnmem " You {i}better{/i} not be dozing off on me!"
    n 2fllpo "..."
    n 4fsqss "...Or I really {i}will{/i} put you to sleep.{w=0.5}{nw}"
    extend 3fchgn " Ehehe."

    if Natsuki.isLove(higher=True):
        n 3uchtsl "Love you too,{w=0.1} [player]!~"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchss "You're welcome,{w=0.1} [player]!~"

    return

# Natsuki doesn't hate spiders, contrary to her poem in DDLC
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_spiders",
            unlocked=True,
            prompt="Are you afraid of spiders?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24",
            category=["Animals", "Fears"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_spiders:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "Huh?{w=0.5} Spiders?"
        n 2tslss "I mean...{w=0.5}{nw}"
        extend 2tnmss " not...{w=1} really?"
        n 1nchgnesm "Pffff-!"
        n 1fchbg "What?"
        n 3ullaj "You thought that because I wrote a poem about them being nasty and gross,{w=0.5}{nw}"
        extend 3tnmaj " that I'd {i}actually{/i} think that?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fslpo "I even {w=0.3}{i}said{/i}{w=0.3} the spider thing was a metaphor,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 4fsqts " Remember?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 2fcssr "No,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fsqsr " I am not afraid of spiders."
        n 1fsqem "...And might I ask {i}why{/i} you feel entitled to know about my fears?"
        n 2fcsan "Why the hell would I give you {i}more{/i} ammo to get on my nerves?"
        n 1fsrem "Ugh..."
        n 1fcssf "Yeah.{w=0.5}{nw}"
        extend 2fsqpu " We're done talking here,{w=0.1} {i}[player]{/i}."

        return

    else:
        n 2fcsan "...Are {i}you{/i} afraid of asking me dumb questions,{w=0.1} since you're the {i}last{/i} person I'd want to answer them for?!"
        n 1fsqun "..."
        n 2fslem "Yeah.{w=2}{nw}"
        extend 2fsqemtsb " Apparently not,{w=0.1} huh?"
        n 4fslanltsb "Jerk."

        return

    if get_topic("talk_fear_of_lightning").shown_count > 0:
        n 1tslpu "And actually...{w=0.3} come to think of it..."
        n 2tnmbo "This isn't the {i}first{/i} time you've randomly asked me if I'm scared of stuff."
        n 1tsqsl "...Are you planning some dumb prank or something?"

    n 1fsqsm "Ehehe.{w=1.5}{nw}"
    extend 1nllss " Well,{w=0.1} whatever."
    n 1ullaj "I mean,{w=0.5}{nw}"
    extend 3fnmaj " don't get me wrong!"
    n 4ksrem "I wouldn't want them like...{w=0.3} {i}crawling{/i} over me or anything.{w=0.5}{nw}"
    extend 2fcsfu " Ew!"
    n 2fslun " I don't even want to {i}imagine{/i} that."
    n 1unmss "But spiders are awesome little guys!{w=1.5}{nw}"
    extend 4nsrss " ...Mostly."
    n 1unmbo "They get rid of the really annoying sorts of bugs,{w=0.1} like ones that bite or fly around constantly."
    n 1nnmaj "And some of them -{w=0.5}{nw}"
    extend 2nslss " as weird as it feels to say -{w=0.5}{nw}"
    extend 1ncspu " are{w=1} freaking{w=1.5}{nw}"
    extend 4fspgsedz " {i}adorable{/i}!"
    n 4uwdaj "Seriously!{w=1.5}{nw}"
    extend 3uchbg " Jumping spiders are cuuuute!"
    n 1tnmss "So...{w=0.3} overall?{w=0.5}{nw}"
    extend 1ncssm " I'd call that a win for the spiders!"
    n 2nslss "...Yeah,{w=0.1} yeah,{w=0.1} [player].{w=0.2} I know.{w=0.5}{nw}"
    extend 2flrpo " I'm not naive!"
    n 1nllun "I know some places have some really nasty types.{w=0.5}{nw}"
    extend 4uskem " And I {i}wish{/i} I was kidding!"
    n 2klrpu "Spiders are already sneaky,{w=0.1} so imagine living with ones that hide in your shoes,{w=0.1} or under your desk..."
    n 1kskgs "That can put you in {i}hospital{/i} too!{w=0.5}{nw}"
    extend 4kllan " Yeesh!"
    n 1ulrss "But...{w=0.5} they're in the minority,{w=0.1} at least.{w=1.5}{nw}"
    extend 2nslun " Isn't {i}that{/i} a relief?"
    n 1ullaj "Well,{w=0.1} anyway."

    if Natsuki.isEnamored(higher=True):
        n 1nsqss "I guess that just leaves you,{w=0.1} then."
        n 3usqsm "Are {i}you{/i} afraid of spiders?"
        n 3fsqsm "Better think through your answer carefully,{w=0.1} [player]."
        n 3fsldvl "You're already caught in {i}my{/i} web,{w=0.1} after all..."

        if random.randint(0,10) == 1:
            n 1fchsml "Ahuhuhu.~" # Yes, this is a Muffet reference

        else:
            n 4fsqsm "Ehehe."

        if Natsuki.isLove(higher=True):
            n 4uchtsl "Love you,{w=0.1} [player]!~"

    else:
        n 2tnmss "You got your answer,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fllss " So..."
        n 1fllsm "I think that about{w=0.5}{nw}"
        extend 3fsqss " {i}wraps{/i}{w=1}{nw}"
        extend 3usqsm " up my thoughts on the subject."
        n 1uchgn "Ehehe."

    return

# Player asks about Dan Salvato
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_dan_salvato",
            unlocked=True,
            prompt="What do you think of Dan Salvato?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC", "Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_dan_salvato:
    n 1tnmaj "Dan...?{w=1}{nw}"
    extend 2nslsl " Dan...{w=0.5} Salvato..."
    n 1fcsaj "Why...{w=0.3} is that name so...{w=0.5} familiar?"
    n 1fcsun "..."
    n 4fskaj "...!"
    n 2fsgaj "Oh..."
    n 1nllpu "Heh.{w=0.3} Yeah...{w=1.5}{nw}"
    extend 2fslan " {i}him{/i}."
    n 1fcsbo "..."
    n 1fplaj "I...{w=1}{nw}"
    extend 2fcsan " I just don't understand him,{w=0.2} [player]."
    n 1nsqbo "Like yeah,{w=1}{nw}"
    extend 1nslbo " sure,{w=0.5}{nw}"
    extend 1nsqaj " I get it."
    n 2ncsbo "He's my creator.{w=1}{nw}"
    extend 2kcsbo " Our creator."
    n 4fskwr "But did he have any {i}idea{/i} what he was doing?!{w=1}{nw}"
    extend 4fchwr " Any idea what he's responsible for?!"
    n 1fcsup "..."
    n 1fllup "Just...{w=1}{nw}"
    extend 2fllfu " take...{w=0.5} Monika,{w=0.2} for example."
    n 1fnmwr "Take {i}any{/i} of us!"
    n 1fcsfu "What we said,{w=0.3} what we did -{w=0.5}{nw}"
    extend 2fcufu " what we {i}thought{/i} -{w=0.5}{nw}"
    extend 2fnmfu " all of that was {i}his{/i} doing."
    n 4fsqfu "He wrote the stories.{w=1}{nw}"
    extend 4fsqaj " He typed up the code."
    n 1fskwr "...So what do I even {i}take{/i} from that, [player]?!"
    n 2fchwr "That {i}his{/i} hands {b}killed{/b} my friends?"
    n 2fchwrl "That {i}his{/i} hands {b}ruined{/b} my homelife?"
    n 1fcuful "If not directly,{w=0.3} then through Monika."
    n 1fcsful "..."
    n 1fcsajl "He might not have {i}made{/i} the others do...{w=1}{nw}"
    extend 2kcsajl " ...what they did."
    n 1kcsfuf "But he sure as hell tied the noose..."
    n 4fcsfuf "...forged the knife."
    n 1kskfuf "A-{w=0.2}and you!{w=0.5}{nw}"
    extend 1kskwrf " Did you even {i}know{/i} what you were in for?!"
    n 2kslupf "What you'd {i}see{/i}?!"
    n 1kcsupf "..."
    n 1kcsajf "I...{w=1} don't know,{w=0.3} [player]."
    n 1kcsunf "..."
    n 1kcsanf "Seriously.{w=1}{nw}"
    extend 2kplajf " I really don't."
    n 2knmbol "I don't know him,{w=1}{nw}"
    extend 2kslfrl " and I probably never will."
    n 1ksqbo "...And that's probably the worst part,{w=0.3} too."
    n 4kwdwr "D-{w=0.2}don't get me wrong!"
    extend 1kwdup " I don't want {i}anything{/i} to do with him!"
    extend 2fnmbo " Like,{w=0.3} at {i}all{/i}."
    n 1ncsbo "But...{w=1}{nw}"
    extend 1ncsaj " all these questions..."
    n 2kcssr "I can only imagine what the answers would be."

return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_outfits_unlock",
            unlocked=True,
            prompt="Custom outfits",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48 and not persistent.jn_custom_outfits_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_outfits_unlock:
    $ persistent.jn_custom_outfits_unlocked = True
    n 1nslpu "..."
    n 1usceml "...!"
    n 4uskeml "I've...{w=0.5}{nw}"
    extend 1nllem " just realized something.{w=1}{nw}"
    extend 2fslun " Something I {i}really{/i} don't like."
    n 1fbkwr "...And that's exactly how {i}long{/i} I've been stuck wearing the same bunch of clothing!{w=0.5}{nw}"
    extend 2fcswr " G-{w=0.2}gross!"
    n 4flrem "I mean...{w=1}{nw}"
    extend 2fsqemsbl " would {i}you{/i} feel comfortable wearing the same clothes basically every single day?"
    n 1kslansbl "Yeesh!"
    n 2fcsposbr "..."
    n 1fcsajsbr "Well,{w=0.3}{nw}"
    extend 1fnmemsbr " you know what?{w=0.75}{nw}"
    extend 3fcsgs " I'm done!"
    n 3fcspol "I don't have to put up with this!"
    n 4fsrpo "There's gotta be something I can do..."
    n 1ncspu "..."
    n 1uwdaj "...Wait!{w=1.5}{nw}"
    extend 3fllbg " Duh!{w=1.5}{nw}"
    extend 3fcsbs " Of course!"
    n 1ulraj "It's not like I {i}never{/i} had any clothes other than what I had in my bag!"
    n 1nllpu "And with the closet here too...{w=0.75}{nw}"
    extend 1fllpu " plus the extra clothes in my locker..."
    n 3ncssr "Hmm..."
    n 4fchbg "Yeah,{w=0.1} okay!{w=1.5}{nw}"
    extend 1nchsm " I think that should all work!"
    n 1nsqsm "..."
    n 4uwdajesu "Oh!{w=0.3}{nw}"
    extend 1unmca " Just to keep you in the loop,{w=0.1} [player]..."
    n 3uchsmeme "I should be able to wear whatever I want now!"
    n 1nllbg "I've got a couple of outfits in mind already,{w=0.5}{nw}"
    extend 3fcsbgedz " so it's not like I have any reason {i}not{/i} to show off some style."
    n 1ulraj "So...{w=0.5}{nw}"
    extend 4fcssm " don't be surprised if I wanna change my clothes from time to time,{w=0.1} alright?"
    n 1fsqsrl "A-{w=0.1}and no.{w=0.5}{nw}"
    extend 2flleml " You're {i}not{/i} gonna see {i}anything{/i}."
    n 2fslpol "I'm making {i}sure{/i} of that."
    n 1nslbo "..."
    n 1uslaj "But..."
    n 1unmbo "I guess I'd be open to suggestions."
    n 1ncsem "Just...{w=0.3} nothing embarrassing.{w=0.5}{nw}"
    extend 3nsqpo " Got it?"
    n 3nsrss "'preciated!"
    n 1ulrbo "Now...{w=0.5}{nw}"
    extend 1tnmss " where were we?"

    python:
        get_topic("talk_custom_outfits_unlock").lock()

        # We have to unload outfits before wearables due to dependencies
        jn_outfits.unloadCustomOutfits()
        jn_outfits.unloadCustomWearables()

        # We have to load wearables before outfits due to dependencies
        jn_outfits.loadCustomWearables()
        jn_outfits.loadCustomOutfits()

        # Now we've loaded back into memory, reload the persisted data
        jn_outfits.JNWearable.loadAll()
        jn_outfits.JNOutfit.loadAll()

    return

# Natsuki talks about her opinion and advice proper hygiene.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_maintaining_proper_hygiene",
            unlocked=True,
            prompt="Proper hygiene",
            category=["Health", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_maintaining_proper_hygiene:
    n 1nllsl "..."
    n 1ullaj "You know,{w=0.1} [player]..."
    n 1nllbo "I've been wondering...{w=0.5}{nw}"
    extend 2tnmpu " are you actually taking care of yourself?"
    n 1nsqsr "Like...{w=0.3} are you keeping up with proper hygiene?"
    n 3fnmpo "It's super important,{w=0.1} you know!"
    extend 1nslem " ...And not just because it's {i}actually{/i} gross if you don't."
    n 4ulraj "It isn't just about being physically healthy,"
    extend 4fnmaj " but it actually helps with your mental health too!{w=1}{nw}"
    n 3fllpo "I'm {i}serious{/i}!"
    n 1klrss "If you're already having a hard time in the old braincase,{w=0.5}{nw}"
    extend 2ksrsr " feeling gross physically as well as mentally isn't gonna help at all."
    n 1knmpu "We {i}both{/i} know someone who always looked scruffy,{w=0.1} [player].{w=1.5}{nw}"
    n 1kcssr "...And we both know how she felt."
    n 1kllun "..."
    n 3fcseml "A-{w=0.1}anyway!{w=1}{nw}"
    extend 3fnmpo " This is about {i}you{/i},{w=0.1} [player] -{w=0.5}{nw}"
    extend 4fnmaj " so listen up!"
    n 1fcsbg "This is gonna be a Natsuki special on taking care of yourself!{w=0.5}{nw}"
    extend 1fcssm " Ehehe."
    n 1fcsaj "First of all,{w=0.1} shower {w=0.1}-{w=0.3}{nw}"
    extend 3fnmaj " and {i}regularly{/i}!"
    n 1fllsl "If you skip showers,{w=0.1} you'll just constantly feel all gross and nasty.{w=0.5}{nw}"
    extend 4tnmsr " And you know what that leads to?"
    n 2nsgbo "Loss of motivation."
    n 1fnmaj "And you know what {i}that{/i} leads to?"
    n 2fcsem "...Not showering!{w=0.5}{nw}"
    extend 2knmpo " See where I'm going here?"
    n 1nllaj "So...{w=0.5}{nw}"
    extend 4fnmsl " just take the time to do it properly,{w=0.1} okay?"
    n 3fllss "It doesn't {i}need{/i} to be some kind of spa ritual,{w=0.1} just whatever gets you clean."

    if Natsuki.isLove(higher=True):
        n 4fslss "And besides,{w=0.5}{nw}"
        extend 3fsrssl " I don't wanna get snug with you if you're all stinky."
        n 3fnmpo "So you better stick at it,{w=0.1} [player]!"

    if persistent.jn_player_appearance_hair_length == "None":
        n 1fcsaj "Next up,{w=0.1} your head!"
        n 1ullpu "I know you said you didn't have any hair...{w=0.5}{nw}"
        extend 3fsqbg " but that doesn't mean you can just slack off up top!"
        n 1ulraj "You gotta make sure you keep your skin clean up there.{w=0.5}{nw}"
        extend 3nsqunsbl " Even if you don't have hair,{w=0.1} oil and all that stuff builds up."
        n 4fcsem "Gross!"
        n 1ullaj "But at least it's easy to solve if you're showering regularly,{w=0.5}{nw}"
        extend 3nnmbo " like I just said."

    else:
        n 1fcsaj "Next up,{w=0.1} your hair!"

        if not persistent.jn_player_appearance_hair_length:
            n 1tllss "Assuming you {i}have{/i} any,{w=0.1} that is."

        n 1nsqbo "You're {i}not{/i} gonna feel good about your appearance if your hair constantly looks like a used mop."
        n 3fchbg "So keep it clean,{w=0.1} and make sure you brush!{w=0.5}{nw}"
        extend 1ullss " Or do whatever else your usual hairstyle needs {w=0.1}-{w=0.3}{nw}"
        extend 4nnmbo " comb,{w=0.1} hairgel,{w=0.1} whatever."
        n 1tnmpu "Remember what I just said about showering,{w=0.1} [player]?"
        n 3fcsbo "The more you put it off,{w=0.1} the harder it is to do!{w=0.5}{nw}"
        extend 3fnmem " And if it gets too gummed up,{w=0.1} you might even have to shave it off!"
        n 1fsrbg "I don't wanna see you walking around like you just got an electric shock...{w=0.5}{nw}"
        extend 4fchgn " ...or as bald as an egg!"

        if persistent.jn_player_appearance_hair_length == "Long":
            n 4fspaj "And {i}especially{/i} since you've got such awesome long hair!{w=0.5}{nw}"
            extend 2fllan " What a waste!"

        n 1ulraj "So...{w=1}{nw}"
        extend 4fnmbo " take care of your hair too,{w=0.1} got it?"
        n 1fcssm "It's {i}just{/i} as important as the rest of you!"

    if get_topic("talk_natsukis_fang").shown_count > 0:
        n 1fcsaj "Finally,{w=0.1} brush your teeth!"
        n 1ullaj "I'll spare you the lecture this time,{w=0.5}{nw}"
        extend 3nnmbo " since we already talked about it and all."
        n 4nsqpu "...But you better not have forgotten about flossing,{w=0.1} [player]...{w=1.5}{nw}"
        extend 4fsqsm " 'Cause I sure haven't!"

    else:
        n 1fcsaj "Finally,{w=0.1} your teeth!{w=0.5}{nw}"
        extend 3fsqpu " Now those are something you {i}really{/i} don't wanna skip out on,{w=0.1} [player]."
        n 3kslan "Not only will your breath be {i}ghastly{/i}..."
        n 4fbkwr "But you'll lose your teeth too!{w=0.5}{nw}"
        extend 2flrun " Or at least end up with a bunch of fillings...{w=1}{nw}"
        extend 1ksqem " Expensive fillings!{w=1}{nw}"
        extend 2fsran " Yeesh!"
        n 4fsqpo "You'd {i}really{/i} have to be a dummy to prefer expensive treatments and a world of pain over a couple minutes of effort."
        n 1flrss "And besides..."
        n 3ksqsm "Who doesn't want a {i}blinding{/i} smile like me?"
        n 3uchgn "You won't get {i}that{/i} with tooth decay!"

    n 4kllss "But seriously,{w=0.1} [player].{w=0.5}{nw}"
    extend 4nsqsr " I {i}really{/i} don't want you flaking out on taking care of yourself."
    n 2fsqsr "I mean it.{w=1.5}{nw}"
    extend 2ksrpo " You deserve to feel and look good too."

    menu:
        n "Got it?"

        "Yes, I deserve to feel and look good too.":
            n 1fchbg "Now {i}that's{/i} what I like to hear!"
            $ Natsuki.calculatedAffinityGain()

        "...":
            n 1nsqsr "..."
            n 3tsqss "You...{w=0.3} really don't get how this all works,{w=0.1} do you?"
            n 1fcssm "Now,{w=0.1} repeat after me:{w=0.5}{nw}"
            extend 1fcsbg " 'I deserve to feel and look good too.'."

            menu:
                "I deserve to feel and look good too.":
                    n 3uchbg "See?{w=0.5}{nw}"
                    extend 3ksqsg " Was that {i}so{/i} hard?"
                    n 1fcssm "Ehehe."
                    $ Natsuki.calculatedAffinityGain()

    n 1ullss "But anyway,{w=0.1} yeah!{w=0.5}{nw}"
    extend 1nnmss " That's about all I had to say."

    if Natsuki.isLove(higher=True):
        n 4nsqss "And remember...{w=0.5}{nw}"
        extend 3nsldvl " I'll love you forever if you keep it up!~"
        n 1fchsml "Ehehe."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        extend 4uchbgl " Thanks,{w=0.1} [chosen_endearment]!"

    elif Natsuki.isEnamored(higher=True):
        n 3nslbgl "I {i}really{/i} like people who take care of themselves."
        n 4fsqpol "You'd do well to remember that, [player]."

    else:
        n 1fchbg "Thanks for hearing me out,{w=0.1} [player]!"
        n 1uslsg "...Or should I say..."
        n 3usqbg "Thanks for letting me{w=0.5}{nw}"
        extend 3fsqss " {i}clear{/i}{w=0.5}{nw}"
        extend 3usqsm " that up?"
        n 1nchgnelg "Ahaha!"

    return

# Natsuki gives her thoughts on Monika.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_monika",
            unlocked=True,
            prompt="How do you feel about Monika?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_monika:
    n 1fslsr "Monika."
    n 1kcsem "..."
    n 2knmsl "...Honestly?"
    n 1nllsl "I...{w=1} don't know {i}how{/i} I feel about Monika.{w=1}{nw}"
    extend 2kslpu " Not anymore."
    n 1nnmsl "I mean,{w=0.5}{nw}"
    extend 4knmpu " what do I even {i}say{/i},{w=0.1} [player]?"
    n 3flrpu "Yeah,{w=0.1} she would butt into my business sometimes.{w=1}{nw}"
    extend 3fsrsf " I didn't like when she would be all high and mighty...{w=1}{nw}"
    extend 3fslem " {i}or{/i} when she kept messing around with my stuff."
    n 1nllpu "But like...{w=0.5}{nw}"
    extend 4knmpu " I was never actually {i}mad{/i} or anything..."
    n 1fcsfr "Annoyed,{w=0.3} frustrated,{w=0.3} sure.{w=1}{nw}"
    extend 2fllpu " Anyone would be!"
    n 2kplem "But I looked up to her,{w=0.1} [player]!{w=1.5}{nw}"
    extend 4kllun " We {i}all{/i} did..."
    n 1kcsun "..."
    n 1fcsun "She wasn't {i}just{/i} the club president,{w=0.1} or smart."
    n 3fnmun "She was a role model.{w=1.5}{nw}"
    extend 3klrpu " ...And my friend."
    n 1ksrpu "But...{w=0.5}{nw}"
    extend 4knmem " that just makes it harder for me to understand,{w=0.1} [player]."
    n 1fcssl "I mean...{w=0.5}{nw}"
    extend 2fcsan " I...{w=1} know...{w=1} what she was dealing with.{w=1.5}{nw}"
    extend 1kslun " {i}I'm{/i} dealing with it right now!"
    n 4kwdem "But...{w=0.3} did she seriously have to {i}torture{/i} us?"
    n 2fcsem "I...{w=0.3} know...{w=0.3} we wouldn't have understood.{w=0.5}{nw}"
    extend 2kslsr " {i}Couldn't{/i} have understood."
    n 1fcsan "Especially when Yuri and I were wrapped up in those stupid fights..."
    n 4fnmsr "{i}I get that{/i}."
    n 2klrpu "But if she was that desperate...{w=0.5}{nw}"
    extend 1kcspu " couldn't she have just removed us all right from the start?{w=0.5}{nw}"
    extend 4knmem " Or literally {i}anything{/i} else?"
    n 1fcsfr "..."
    n 2kcspu "I don't know,{w=0.1} [player].{w=1.5}{nw}"
    extend 4knmca " I really don't."
    n 1ncssr "..."
    n 1nllpu "I guess..{w=1}{nw}"
    extend 2tnmpu " maybe it was the isolation?"
    n 1nlrsl "She was always getting excluded from everything since you turned up...{w=1}{nw}"
    extend 2nsrsr " I don't think she even {i}had{/i} a choice."
    n 4knmsl "...Maybe the same thing would've happened to me?"
    n 1fcseml "D-{w=0.1}don't get me wrong though!{w=0.5}{nw}"
    extend 3flrem " I'm never gonna forget what she did...{w=0.5}{nw}"
    extend 3fsrputsb " forgive what she did."
    n 1nlrpu "But...{w=1}{nw}"
    extend 4knmsr " she {i}was{/i} still my friend."
    n 1kllpu "So there's always gonna be a part of me that kinda wishes I {i}could{/i} forgive her."
    n 2kllbol "...Maybe that's why I wanna understand her actions so badly."

    return

# Natsuki gives her thoughts on Yuri.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_yuri",
            unlocked=True,
            prompt="How do you feel about Yuri?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_yuri:
    n 1kllpul "...Oh man,{w=1} Yuri..."
    n 2kcsuntsb "..."
    n 1ncspu "...I won't lie,{w=0.3} [player].{w=1.5}{nw}"
    extend 4ksqfr " I really,{w=0.5} {i}really{/i} didn't want to think about...{w=1} {i}that{/i} again."
    n 1kcssl "..."
    n 1ksrpu "How do I even {i}explain{/i} this..."
    n 3ncsem "Yuri and I were...{w=0.3} complicated.{w=1}{nw}"
    extend 3kllss " Even {i}before{/i} you joined the club."
    n 1nnmbo "We never fully saw eye-to-eye,{w=0.1} [player].{w=1.5}{nw}"
    extend 2nslca " You probably guessed that already anyway."
    n 1kwmpu "But we had an {i}understanding{/i},{w=0.1} you know?"
    n 1kllpul "She was...{w=1}{nw}"
    extend 1kcsunltsa " there...{w=1}{nw}"
    extend 2fcsunltsa " for me."
    n 2fsrunltsb "When I needed someone there the most.{w=1}{nw}"
    extend 1fnmem " When nobody else would get it...{w=1}{nw}"
    extend 4kslpu " Could even {i}hope{/i} to get it."
    n 1kwmpu "...{w=0.5}Do you even know how much that meant to me?"
    n 1knmsl "She just had a way of understanding you like nobody else could.{w=1}{nw}"
    extend 2fslem " Not {i}Monika{/i}.{w=1.5}{nw}"
    extend 1kslsrl " Not even {i}Sayori{/i}."
    n 1kllpu "But..."
    n 3fcssr "She just {i}changed{/i},{w=0.1} [player].{w=0.5}{nw}"
    extend 3klrsl " When you showed up,{w=0.1} I mean."
    n 4knmem "We {i}never{/i} had fights like that..."
    n 1tnmsr "Arguments?{w=0.5}{nw}"
    extend 2tllss " Well...{w=1} yeah!{w=1}{nw}"
    extend 2knmss " What kind of friends don't?"
    n 1klrsm "And we were always super different,{w=0.1} too."
    n 3nsrpo "She always had that prim and proper vibe.{w=1}{nw}"
    extend 1ncsaj " Refined...{w=1}{nw}"
    extend 1ncsss " elegant."
    n 2nslss "...{w=0.5}And I was just Natsuki.{w=1}{nw}"
    extend 1ncsss " Heh."
    n 1knmpu "But I never had the feeling before then that she just {i}didn't like me{/i}!"
    n 2fcsan "We were both just so caught up in that {i}stupid{/i} rivalry..."
    n 1fllan "It just took over everything!"
    n 2kllpu "And then when she started getting all possessive...{w=1}{nw}"
    extend 4knmsl " you know,{w=0.1} after Monika messed her all up."
    n 4kplem "...Do you know how {i}scary{/i} that was to me?{w=1.5}{nw}"
    extend 1kwdwr " Hearing those {i}words{/i} coming out of {i}her{/i} mouth?"
    n 1klrem "And the worst part?{w=1.5}{nw}"
    extend 2kcsem " I just...{w=0.3} went...{w=0.3} along with it.{w=1}{nw}"
    extend 2kplup " I had no {i}choice{/i},{w=0.1} [player]!"
    n 1fcsup "...Neither of us did."
    n 1fcsanl "Even when I {i}begged{/i} you for help,{w=0.1} I..."
    n 2kcsanltsa "I-..."
    n 1kcsupltsd "..."
    n 1fcsunltsa "..."
    n 4kcseml "...Sorry,{w=0.1} [player]."
    n 2ksrunl "I really don't think it's good for me to keep talking about this.{w=1}{nw}"
    extend 1ksqpul " ...About her."
    n 1fcssrl "I just...{w=1}{nw}"
    n 1kcseml "..."
    n 2fwmsrl "...I miss my friend.{w=1}{nw}"
    extend 4kllsr " I miss how she used to be."
    n 1kllaj "So...{w=0.5} remembering what happened?{w=0.5}{nw}"
    extend 2kskem " What she {i}became{/i}?"
    n 1fcsem "It...{w=1} just hurts,{w=0.1} [player].{w=1.5}{nw}"
    extend 2fcsunltsa " It hurts a lot."
    n 4fsqun "...And to be honest?"
    n 1ksrpu "...I'm not sure it ever {i}won't{/i}."

    return

# Natsuki gives her thoughts on Sayori.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_sayori",
            unlocked=True,
            prompt="How do you feel about Sayori?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_sayori:
    n 1nsrss "Heh.{w=1}{nw}"
    extend 2ksrss " Sayori..."
    n 1kcspu "..."
    n 4fcsunl "I...{w=0.5}{nw}"
    extend 1fcsem " still get mad at myself sometimes,{w=0.1} you know."
    n 2klrpu "I just can't {i}believe{/i} how I wrote off how she was feeling so easily."
    n 1kplun "...And how I forgot she even {i}existed{/i}."
    n 2fcsanl "If I'd have just {i}known{/i} how bad her mental health was...{w=1}{nw}"
    extend 4fcsupl " how much she was {i}hurting{/i}..."
    n 1fcsunl "..."
    n 1kcsem "..."
    n 2kslpu "It's...{w=1.5}{nw}"
    extend 2kplem " it's still just such a system shock,{w=0.1} you know?"
    n 1fcsem "She was always so...{w=1} so...{w=0.5}{nw}"
    extend 2ksrpo " just...{w=1} super excited and clingy!"
    n 1ksrss "Like she was just {i}vibrating{/i} with happiness!"
    n 1ksrun "..."
    n 4kplpul "...So can you even {i}imagine{/i} how it feels?"
    n 2fcsun "Knowing she was just wearing a mask,{w=1}{nw}"
    extend 1fcsfu " then dancing like a puppet under Monika's hand?"
    n 2ksrbol "...While her own mind was beating the absolute {i}crap{/i} out of her."
    n 1kcspuesi "..."
    n 1ncsss "Heh.{w=1}{nw}"
    extend 3nsqss " You know what?"
    n 1ncspu "I don't care about my cookie she took a giant bite out of."
    n 1nlrpu "I don't care about the dumb songs she'd sing,{w=1}{nw}"
    extend 3nslssl " or her...{w=0.3} awkward...{w=0.3} compliments."
    n 4tnmsr "At this point?"
    n 2ksrsrltsb "I think I'd do {i}anything{/i} just to see a genuine Sayori smile again..."
    n 2kcsssftsa "...And give her one of those big,{w=0.1} dumb hugs she liked so much."

    return

# Natsuki isn't a big tea drinker.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_tea",
            unlocked=True,
            prompt="Do you drink much tea?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 36",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_tea:
    $ already_discussed_thoughts_on_tea = get_topic("talk_thoughts_on_tea").shown_count > 0
    $ player_tea_coffee_preference_known = persistent.jn_player_tea_coffee_preference is not None

    if Natsuki.isNormal(higher=True):
        if already_discussed_thoughts_on_tea:
            n 1fcsaj "A-{w=0.1}actually,{w=0.2} hold up a second...{w=1}{nw}"
            extend 2tslpu " didn't we already talk about this?"

        else:
            n 1tnmaj "Huh?{w=0.2} Do I drink tea?"
            n 3fchgn "...Are you {i}sure{/i} you know who you're talking to?{w=0.5}{nw}"
            extend 1fllbg " I literally never make it myself!"
            n 2uslss "I mean,{w=0.5}{nw}"
            extend 1unmbo " I had it a few times in the club,{w=0.2} sure."
            n 1nlrpu "Yuri would prepare it for us all sometimes."
            n 2tsrss "But it was never like I asked for it or anything!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 2fsqsr "No,{w=0.5} [player]."
        n 1fsqbo "I don't really care for it."
        n 2fllpu "...I mean,{w=0.5}{nw}"
        extend 2nllsf " I {i}guess{/i} I'd drink it if it was offered."
        n 2nslsl "...From most people,{w=0.2} anyway."
        n 1fsqbo "Somehow I doubt that'd be the case for {i}you{/i}."

        return

    else:
        n 1fcsem "No,{w=2}{nw}"
        extend 2fsqan " and I'm certainly not drinking any of {i}yours{/i}."
        n 2fslemltsb "Not like it'd be {i}just{/i} tea anyway,{w=0.2} knowing a jerk like {i}you{/i}."

        return

    if already_discussed_thoughts_on_tea:
        n 1ullaj "Well,{w=0.2} anyway.{w=0.5}{nw}"
        extend 4unmbo " I wouldn't say my opinion has changed much."
        n 2nlraj "I get why people are into it,{w=0.2} though."

    else:
        n 1fllbo "..."
        n 3fcseml "T-{w=0.2}that's not to mean I think it sucks,{w=0.2} or something like that!"

        if get_topic("talk_favourite_drink").shown_count > 0:
            n 1nlrbo "I just have my own tastes.{w=0.75}{nw}"
            extend 4uspbg " Like hot chocolate!"

        else:
            n 1nlrbo "I just have my own tastes."

        n 1ullaj "But...{w=0.5}{nw}"
        extend 2nllbo " I guess I can see why people are into it so much."

    n 2tnmca "Tea contains caffeine,{w=0.2} right?{w=0.5}{nw}"
    extend 2tlrss " Not as much as coffee or anything,{w=0.2} but an edge is still an edge,{w=0.2} I guess."
    n 1unmaj "It comes in a whole bunch of flavors too!{w=0.5}{nw}"
    extend 4unmgs " I was actually kinda surprised at the variety!"
    n 1ullss "You've got your regular old black tea{w=0.3}{nw}"
    extend 2fslss " -{w=0.1} obviously -{w=0.3}{nw}"
    extend 1ulraj " but you've got green tea,{w=0.2} herbal tea..."
    n 4uspgs "Even flavored ones like cinnamon and peppermint!"
    n 2nslss "We only ever had oolong tea in the clubroom though,{w=0.5}{nw}"
    extend 2tnmss " so who knows?"
    n 1ulrbo "Maybe I'd warm up to it if I tried some that sounded good."

    if get_topic("talk_sleeping_well").shown_count > 0:
        n 1unmaj "Apparently some tea even helps you sleep!{w=0.75}{nw}"
        extend 2nsrss " ...Maybe I should've mentioned that in my sleeping tips.{w=0.5}{nw}"
        extend 2fchblesd " Oops~!"

    n 1ulraj "But...{w=0.5}{nw}"
    extend 4nslss " I've gone on enough."
    n 1unmbo "What about you,{w=0.2} [player]?"
    show natsuki 4tsqss
    $ menu_opening = "Drinking something else now?" if player_tea_coffee_preference_known else "What's your pick?"

    menu:
        n "[menu_opening]"

        "I prefer tea.":
            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "tea":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 1tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."

                else:
                    n 2tnmsm "A tea drinker now,{w=0.2} huh?{w=0.5}{nw}"
                    extend 1fchsm " Fair enough!"

            else:
                n 4unmaj "Tea?{w=0.5}{nw}"
                extend 1nllpu " Hmm..."
                n 1unmbo "Yeah,{w=0.2} that's about what I expected."
                n 2nlrbo "..."
                n 1tnmbg "What?"
                n 3tsqbg "Not like you raised a fuss about it earlier,{w=0.5}{nw}"
                extend 3tsqsm " right?"
                n 1kslsm "..."
                n 1nslss "Though...{w=1.5}{nw}"
                extend 4uslsr " not like you had much of a choice in it back then,{w=0.2} right?"

            $ persistent.jn_player_tea_coffee_preference = "tea"

        "I prefer coffee.":
            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "coffee":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 2tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."

                else:
                    n 3tsqct "Oho?{w=0.5}{nw}"
                    extend 3tsqbg " Coffee now,{w=0.2} huh?"
                    n 1fsrsm "Wow,{w=0.2} [player]."
                    n 3fchgnelg "Since when did you get so {i}bitter{/i}?"

            else:
                n 1unmaj "Oh?{w=1.5}{nw}"
                extend 3tnmss " You're a coffee drinker?"
                n 1nllpu "Hmm..."
                n 1nsqss "Then I guess the sessions in the club weren't your{w=0.5}{nw}"
                extend 3fsqbg " {i}cup of tea{/i}{w=0.5}{nw},"
                extend 3usqbg " huh?"
                n 1uchgn "..."
                n 1fchbg "Oh,{w=0.5}{nw}"
                extend 4fllbg " come on,{w=0.2} [player]!{w=0.3} Yeesh."
                n 1fsqsm "No need to be all {w=0.3}{i}bitter{/i}{w=0.3} about it."
                n 1fchsm "..."
                n 3kchbg "Okay,{w=0.2} okay!{w=0.5} I'm done!"
                n 3fsqsg "...For now."

            $ persistent.jn_player_tea_coffee_preference = "coffee"

        "I like both!":
            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "both":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 3tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."

                else:
                    n 4tnmaj "Oh?{w=0.5}{nw}"
                    extend 3tnmss " You like {i}both{/i} now?"
                    n 4tsqbg "...Are you {i}sure{/i} you aren't just a caffeine junkie,{w=0.2} [player]?"
                    extend 1nchgn " Ehehe."

            else:
                n 2tslajeqm "...Huh.{w=0.75}{nw}"
                extend 1tnmss " Really?"
                n 3nsrss "That's...{w=0.3} kinda weird,{w=0.2} actually."
                n 1fchbg "Most people like at least {i}one{/i} of the two more!"
                n 4fsqsg "Are you {i}sure{/i} you aren't just a caffeine junkie,{w=0.2} [player]?"

            $ persistent.jn_player_tea_coffee_preference = "both"

        "I don't like tea or coffee.":
            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "neither":
                    n 1tsqpu "Still not a fan,{w=0.2} huh?{w=0.5}{nw}"
                    extend 4fnmaj " You need to keep trying new stuff!"
                    n 3fsqpo "Where's your sense of adventure,{w=0.2} [player]?{w=0.5}{nw}"
                    extend 1fchts " Ehehe."

                else:
                    n 4tnmaj "Huh?{w=0.3} You don't like tea {i}or{/i} coffee now?{w=0.5}{nw}"
                    extend 1tsqun " Did I miss something?"
                    n 2tlrbo "...Or maybe you're just trying to sleep better?{w=0.5}{nw}"
                    extend 1tsrpu " Huh."

            else:
                n 1ullaj "That's...{w=0.75}{nw}"
                extend 2tllbo " kinda surprising,{w=0.2} actually."
                n 4fsrpu "Most people at {i}least{/i} like one or the other..."
                n 3fsqpo "You aren't just pulling my leg,{w=0.3}{nw}"
                extend 3ksqpo " are you?"
                n 4fslpol "I was being serious..."

            $ persistent.jn_player_tea_coffee_preference = "neither"

    n 1nllss "Well,{w=0.2} whatever.{w=0.5}{nw}"
    extend 1fchbg " Not like hot drinks are the be-all and end-all anyway."
    n 3fllss "But that being said...{w=0.3}{nw}"
    extend 3nsremsbl " I'm actually pretty parched after all that talking."
    n 4fsrpo "..."
    n 1unmss "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1usqsm " do me a favor?"
    n 1fsqsg "..."
    n 3fchbg "...Stick the kettle on,{w=0.2} would you?"
    n 3uchgnelg "Ahaha."

    return

# Natsuki gives her advice on how to make friends with other people.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_make_friends",
            unlocked=True,
            prompt="How do I make friends?",
            category=["Life", "Society", "You"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_make_friends:
    n 1tnmpu "Huh?{w=1}{nw}"
    extend 4tnmsleqm " You wanna know how to make {i}friends{/i}?"
    n 1tllbo "..."
    n 3ncsaj "Well.{w=1}{nw}"
    extend 3nlraj " I gotta say,{w=0.1} [player]."
    n 4fchgnelg "That's pretty up there in the weirdest questions you've asked me so far!"
    n 1fllss "But...{w=1}{nw}"
    extend 2ullaj " in all seriousness?"
    n 1tnmsf "{w=0.3}...Why?{w=1}{nw}"
    extend 1nlrss " Like why're you asking {i}me{/i},{w=0.3} I mean."

    if Natsuki.isLove(higher=True):
        n 3kslbgl "You've basically mastered getting to know me!{w=0.5}{nw}"
        extend 3fcspol " N-{w=0.1}not that I just let you,{w=0.1} obviously."

    elif Natsuki.isEnamored(higher=True):
        n 1ullaj "It's just...{w=1}{nw}"
        extend 3tnmssl " I {i}seriously{/i} doubt it's something {i}you'd{/i} struggle with,{w=0.5}{nw}"
        extend 3nsrssl " of all people."

    elif Natsuki.isAffectionate(higher=True):
        n 2ksqpol "Are we not {i}already{/i} friends,{w=0.1} [player]?"

    else:
        n 2nsrpo "I thought we were getting along okay,{w=0.1} at least..."

    n 4nsrpo "..."
    n 1ulraj "Well,{w=0.5}{nw}"
    extend 1nlrss " anyway..."
    n 1nchbs "Sure!{w=1}{nw}"
    extend 3fwlbgedz " I can show you the ropes!"
    n 4fnmaj "Right!{w=0.5}{nw}"
    extend 4ncsaj " So..."
    n 1unmbo "I think the most important thing is to have {i}something{/i} in common.{w=1}{nw}"
    extend 1flrss " You probably knew that much,{w=0.1} at least."
    n 4fnmpu "But I think people overthink what that actually {i}means{/i}!"
    n 4flrpu "You don't have to share hobbies,{w=0.5}{nw}"
    extend 2nlraj " or a ton of interests or anything like that."
    n 1ulrbo "I mean,{w=0.5}{nw}"
    extend 3fcsbg " just look at Yuri and me!{w=1}{nw}"
    extend 3uchgn " Classic example!"
    n 1ullaj "Sure,{w=0.1} we disagreed on literature.{w=1}{nw}"
    extend 4fnmaj " But we went to the same school {w=0.1}-{w=0.5}{nw}"
    extend 1fchbg " and we were members of the same club!"
    n 3fcssm "I guess what I'm getting at is that having {i}places{/i} in common is just as key as tastes!"
    n 1tllbo "If anything,{w=0.5}{nw}"
    extend 1tnmss " it actually makes it even easier if you {i}know{/i} you're gonna see them again!"
    n 3fcsaj "So {w=0.1}-{w=0.1} once you've got something in common,{w=0.5}{nw}"
    extend 1fchbg " it's all just a matter of contact!"
    n 4fsqsm "Now here's where you gotta use your brain,{w=0.1} [player]."
    n 1ullaj "Just...{w=1.5}{nw}"
    extend 4tnmca " {i}think{/i} a little about the situation and what to say,{w=0.1} you know?"
    n 1ullpu "Like,{w=0.5}{nw}"
    extend 2nnmaj " say you just started a new job in an office."
    n 2flrem "Don't just assume they're into manga or whatever {w=0.1}-{w=0.5}{nw}"
    extend 1kchbg " ease into it!{w=1}{nw}"
    extend 4fchbg " Lean into 'em with a coffee or something!"
    n 3fsqaj "Don't be fooled though,{w=0.1} [player]."
    n 3nslsl "You can't just expect to talk to someone once and be done...{w=0.5}{nw}"
    extend 3fnmss " you gotta keep at it,{w=0.1} too!"
    n 1ullbo "Physical talks,{w=0.1} online messaging,{w=0.5}{nw}"
    extend 1unmaj " whatever works."
    n 4uwdem "It's {i}super{/i} easy for a friendship -{w=0.5}{nw}"
    extend 1fllun " even an old one {w=0.1}-{w=0.5}{nw}"
    extend 2knmsl " to fizzle out because nobody is making an effort."
    n 4uskem "B-{w=0.1}but that's not to say you gotta go all out all the time though!"
    n 1fcsaj "It's all about striking a balance.{w=1}{nw}"
    extend 2fchbgsbl " People need downtime too!"
    n 4fslsr "{w=0.3}...And you shouldn't be the one putting in {i}everything{/i} to make it work."
    n 4fnmpu "Remember {w=0.1}-{w=0.1} a friendship has two sides."
    extend 1fchsm " You {i}know{/i} you've got a winner if they're doing their part too!"
    n 2nllss "But that all being said,{w=0.1} [player]..."
    n 1nnmsl "There's one thing more important than {cps=\10}{i}anything{/i}{/cps} else.{w=1.5}{nw}"
    extend 4fsqsr " Respect."
    n 2fsrem "Friends don't trash each other,{w=0.5}{nw}"
    extend 1fcsem " or give them crap for their interests!"
    n 4fsqsr "...And that goes {i}both{/i} ways,{w=0.1} [player]."
    n 2fsrbo "Someone being a 'friend' is {i}no{/i} excuse for them to act like a jerk whenever they want {w=0.1}-{w=0.5}{nw}"
    extend 2fsqpu " trust me."
    n 1fnmpu "I've {i}been{/i} there.{w=0.5}{nw}"
    extend 4kllsf " And it took a good friend to help me realize that."
    n 1ncsss "Heh."
    n 1ullpu "But...{w=1}{nw}"
    extend 3fchbg " yeah!"
    n 1tnmsm "I wouldn't get all stressed out about it,{w=0.1} [player].{w=1}{nw}"
    extend 3fcssm " Friendships are {i}formed{/i},{w=0.1} not forced."
    n 1fcsss "So take your time,{w=0.1} and just go with the flow.{w=1}{nw}"
    extend 4kllbg " That's all I'm saying!"
    n 2fsqsm "And besides..."
    n 2tsqsg "It's worked out for us so far,{w=0.1} huh?{w=0.5}{nw}"
    extend 1nchgnl " Ehehe."

    return

# Natsuki doesn't appreciate being asked to make funny impressions of her friends.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_impressions_of_the_other_girls",
            unlocked=True,
            prompt="Can you do any impressions of the other girls?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_impressions_of_the_other_girls:
    $ already_discussed_realizations_of_others = get_topic("talk_realizations_other_girls").shown_count > 0
    $ already_discussed_impressions_of_others = get_topic("talk_impressions_of_the_other_girls").shown_count > 0

    if Natsuki.isAffectionate(higher=True):
        if already_discussed_impressions_of_others:
            n 1fcsem "Oh,{w=0.75}{nw}"
            extend 2kslemesisbl " come {i}on{/i}..."
            n 2knmemsbl "This again?{w=0.75}{nw}"
            extend 4ksqemsbr " Seriously?"

        else:
            n 2fcsemesi "...{w=1}{nw}"

        n 1fcssrsbr "...No,{w=0.1} [player].{w=1}{nw}"
        extend 1kcssr " I can't."
        n 2fllun "..."
        n 2fcsemsbl "...Okay,{w=1}{nw}"
        extend 1fnmsll " look."
        n 1fcspul "..."
        n 1fllsl "It's not that I {i}couldn't{/i} do impressions of them.{w=1}{nw}"
        extend 2kllsr " I knew them well enough."
        n 4knmpu "...But that's exactly why I don't {i}want{/i} to,{w=0.1} [player]."
        n 2klrsf "Knowing how they felt,{w=0.5} what they thought..."

        if already_discussed_realizations_of_others:
            n 4ksrputsb "...How much I {i}miss{/i} them..."

        else:
            n 2ksrputsb "...How much they {i}hurt{/i}..."

        n 2knmemtsc "What kind of a sick jerk would I be to make jokes out of {i}that{/i}?"
        n 1fcsunltsa "..."
        n 1kcssl "So...{w=1}{nw}"
        extend 1nnmsf " I'm sorry,{w=0.1} [player].{w=1.5}{nw}"
        extend 2fslsf " But it's a no."
        n 1fcsunl "...And it always {i}will{/i} be."

    elif Natsuki.isNormal(higher=True):
        if already_discussed_impressions_of_others:
            n 2knmaw "[player]...{w=0.5}{nw}"
            extend 1knmwr " really?"
            n 4kslemlsbr "This {w=0.2}{i}again{/i}?"

        else:
            n 1knmpu "..."

        n 2knmemtsc "...Why on {i}Earth{/i} would I want do {i}that{/i}?"
        n 1kllpu "A-{w=0.3}and more importantly,{w=1}{nw}"
        extend 2fcsem " why would you even think to {i}ask{/i} me that,{w=0.1} [player]?"
        n 2ksqem "Do you have any {i}idea{/i} how much I think about them,{w=0.1} still?"

        if already_discussed_realizations_of_others:
            n 4fcseml "I even {i}told{/i} you how much I miss them,{w=0.1} [player]!"

        n 1kcsunltsa "..."
        n 1ncspu "...Alright,{w=0.5}{nw}"
        extend 2fcsun " look."
        n 1fcsem "I...{w=1}{nw}"
        extend 1fcssr " get...{w=1}{nw}"
        extend 2fsgem " that you were just trying to have fun."

        if already_discussed_impressions_of_others:
            n 2fsrun "...I {i}hope{/i},{w=0.2} at least."

        n 1fsqsr "But I am {i}not{/i} making jokes about my friends."
        n 2fcssr "Sorry,{w=0.1} [player]."
        n 2fslunl "But some things are just off-limits."

        if already_discussed_impressions_of_others:
            n 1fsqunl "And you {i}better{/i} respect that sooner rather than later."

    elif Natsuki.isDistressed(higher=True):
        n 1fskeml "...E-{w=0.3}excuse me?!"
        n 2fsqanltsb "Are you {i}seriously{/i} asking me to make fun of my {i}friends{/i}?"
        n 1fsqwrltsbean "Knowing {w=0.2}{i}full {w=0.2}well{/i}{w=0.2} what happened to them?!"

        if already_discussed_realizations_of_others:
            extend 2fcsfultsa " Knowing how much I {i}miss{/i} them?!"

        n 1fcsunl "..."
        n 1fsqem "Your sense of humor {i}{w=0.2}blows{w=0.2}{/i},{w=0.2} [player]."

        if already_discussed_impressions_of_others:
            n 2fsqanl "Now knock.{w=0.3}{nw}"
            extend 2fcsanl " It.{w=0.3}{nw}"
            extend 2fsqful " {i}Off{/i}."
            $ Natsuki.percentageAffinityLoss(5)

        else:
            n 1fcsan "Do {b}not{/b} try my patience again.{w=1.5}{nw}"
            extend 2fsqan " Jerk."
            $ Natsuki.calculatedAffinityLoss(2)

    else:
        n 2fnmantsc "...What is {i}{w=0.3}wrong{w=0.3}{/i} with you?{w=1.5}{nw}"
        extend 1fnmscltsf " Like,{w=0.1} what the {i}hell{/i} is wrong with your {w=0.2}{i}head{/i}?!"
        n 2fcsanltsd "I am {b}NOT{/b} doing that,{w=0.3}{nw}"
        extend 2fcsfultsd " let alone for a piece of work like{w=0.25}{nw}"
        extend 1fskwrftdc " {i}you{/i}!"

        $ Natsuki.calculatedAffinityLoss(3)

    return

# Natsuki muses on the school newspaper and bias in media.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_newspapers_and_bias",
            unlocked=True,
            prompt="Newspapers and bias",
            category=["Literature", "Media", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_newspapers_and_bias:
    n 1nllpu "...Huh.{w=1}{nw}"
    extend 4unmaj " You know,{w=0.1} [player]..."
    n 1tllaj "It's actually kinda weird,{w=0.1} looking back."
    n 2fllss "At the club,{w=0.3} I mean.{w=0.5}{nw}"
    extend 4tsqpu " You {i}do{/i} remember what kind of club it was,{w=0.1} right?"
    n 1tnmpu "...So don't you think it's weird how {i}few{/i} kinds of literature we actually looked at?"
    n 2nllaj "Yuri was always nose-deep in her books.{w=0.5}{nw}"
    extend 2nsqss " And we {i}all{/i} looked at poetry,{w=0.5}{nw}"
    extend 2fsrss " obviously."
    n 1knmaj "But we barely had anything in that room apart from textbooks!{w=0.5}{nw}"
    extend 4fllpo " We didn't even have the school newspaper in there!"
    n 3tsrss "Kind of a misnomer,{w=0.1} huh?"
    n 1tlrpu "But...{w=0.5}{nw}"
    extend 1tnmca " talking of newspapers..."
    n 3fnmca "It's actually super important to read into them properly,{w=0.1} you know."
    n 1knmajsbl "What?{w=0.5}{nw}"
    extend 2fsqpo " I'm being serious!"
    n 1fllss "Newspapers really {i}aren't{/i} just news anymore,{w=0.1} [player]...{w=1}{nw}"
    extend 3fcsaj " and they haven't been for a long time!"
    n 1flrpu "It's tricky,{w=0.5}{nw}"
    extend 4fnmca " but you gotta think a little whenever you open one up."
    n 3fchbg "They aren't owned and run by robots!{w=0.5}{nw}"
    extend 3fcsss " There's {i}always{/i} gonna be opinion that finds its way in somehow."
    n 1ullaj "I mean...{w=1}{nw}"
    extend 4fnmaj " take the school newspaper we had!"
    n 3tsqss "Do you {i}really{/i} think a paper run by {i}students{/i} is gonna be completely fair about the school?"
    n 1nlraj "Let's say the newspaper wanted more funding to print more copies or something,{w=0.5}{nw}"
    extend 1fnmbo " and needed a student vote to make that happen."
    n 4tnmpu "Are they seriously just gonna leave the fate of their paper up to {i}chance{/i}?"
    n 4fchts "Duh!{w=0.5}{nw}"
    extend 1fchgn " Of course not!{w=1}{nw}"
    extend 4fsqss " They'd fight for it!"
    n 1ulraj "Maybe they'd run extra articles to advertise it,{w=0.5}{nw}"
    extend 3fsqsmeme " and {i}only{/i} interview people who supported the paper!"
    n 1tlrss "Or just {i}happen{/i} to forget to mention all the funds they got last semester?{w=1}{nw}"
    extend 4kchblesd " How {i}convenient{/i}~!"
    n 3fcsbg "That's just one example,{w=0.1} obviously."
    n 1fnmaj "But the same thinking applies to any kind of journalism!{w=1}{nw}"
    extend 1nllca " Papers,{w=0.1} online articles,{w=0.5}{nw}"
    extend 4fnmca " whatever it is."
    n 1fcsbg "It's {i}all{/i} subject to bias!"
    n 2nllaj "So...{w=1}{nw}"
    extend 2tnmss " where am I going with this,{w=0.3} you ask?"
    n 1fcssm "Ehehe.{w=0.5}{nw}"
    extend 1fsqsm " I think it's pretty obvious."
    n 1fllss "I know I call you it a bunch already,{w=0.1} [player]..."
    n 1fcsss "But take it from me."
    n 3fsqsm "Only {i}real{/i} dummies believe {i}everything{/i} they read!"

    return

# Natsuki isn't afraid of flying, despite having never flown before
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_flying",
            unlocked=True,
            prompt="Are you afraid of flying?",
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            category=["Fears", "Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_flying:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "Flying,{w=0.1} huh?"
        n 4tllaj "...You know,{w=1}{nw}"
        extend 4ulraj " it's actually kinda weird,{w=0.75}{nw}"
        extend 1unmbo " when you think about it."
        n 3fllss "How people can be afraid of things they've never {i}actually{/i} experienced before,{w=0.1} I mean."
        n 1ullaj "It's pretty crazy how people have these kinds of built-{w=0.1}in fears,{w=0.5}{nw}"
        extend 2tnmss " huh?"

        if get_topic("talk_flying").shown_count > 0 or get_topic("talk_fear_of_flying").shown_count > 0:
            n 1ulraj "I mean,{w=0.5}{nw}"
            extend 2nsrss " like I told you before -{w=0.5}{nw}"
            extend 2tnmbo " I've never flown anywhere myself or anything."

        else:
            n 1ulraj "I mean,{w=0.5}{nw}"
            extend 2tnmbo " I've never flown anywhere myself or anything."

        n 4uskemlesh "B-{w=0.3}but that's not to say {i}I'm{/i} afraid of flying,{w=0.5}{nw}"
        extend 2fcspol " obviously!"
        n 1unmaj "I actually don't think it'd bother me all that much."
        n 4tlrpu "Though...{w=0.75}{nw}"
        extend 1unmbo " I guess I can see {i}why{/i} it would spook someone out."
        n 3fllbo "There's all the noise,{w=0.5}{nw}"
        extend 3fslem " the turbulence,{w=0.5}{nw}"
        extend 3ksqfr " plus the stress of being packed in a tube with a whole bunch of strangers."
        n 1klrss "And it isn't like you can {i}ignore{/i} crashes when they happen!{w=0.75}{nw}"
        extend 1klrsl " They're...{w=0.75}{nw}"
        extend 2kslsr " not...{w=0.5} pretty."
        n 4kslslsbl "...And an easy way to fill a front page."
        n 1unmpu "So yeah,{w=0.2} I can totally see it from that angle.{w=0.5}{nw}"
        extend 2flrpu " But..."
        n 2fnmbo "I think people forget just how {i}safe{/i} air travel is!"
        n 1ullaj "I get that their feelings -{w=0.5}{nw}"
        extend 2fslem " {i}and the news{/i} -{w=0.5}{nw}"
        extend 1unmbo " tell them otherwise.{w=0.75}{nw}"
        extend 4flrss " But it isn't like the statistics {i}lie{/i}!"
        n 4unmaj "Some studies have put the likelihood of biting the big one in a plane crash at one in 11{w=0.5}{nw}"
        extend 1uwdaj " {i}million{/i}."
        n 3fslss "Or,{w=0.1} to put it another way..."
        n 3unmem "You're more than {i}2,000{/i} times more likely to kick the bucket from a car accident than from a plane crash!"
        n 1tsqss "...And the list doesn't stop there,{w=0.1} either!"
        n 2ullss "Lightning strikes,{w=0.5}{nw}"
        extend 2ulraj " riding a bike,{w=0.5}{nw}"
        extend 1nsqsl " falling off something..."
        n 1fllss "They're all way riskier than any flight you {i}should{/i} be stepping on!"
        n 1nllsl "..."
        n 1fcspu "...I know,{w=0.1} I know.{w=0.5}{nw}"
        extend 3fsrpo " I'm not {i}totally{/i} blind to the risks,{w=0.1} [player]."
        n 1nllpu "It's just like anything."
        n 4unmpu "Things can go wrong.{w=1}{nw}"
        extend 2ksrpu " They {i}do{/i} go wrong."
        n 1kcsemesi "And that {i}is{/i} scary."
        n 3tlrpu "But...{w=0.75}{nw}"
        extend 3tnmss " honestly?"
        n 1fsqsm "It {i}is{/i} pretty reassuring to know that when I get the chance to jet off somewhere,{w=0.1} the most I'll realistically have to fear..."
        n 4fchgnelg "...Is probably gonna be the airline food!"

        if persistent._jn_player_has_flown:
            n 1fcsbg "Now that's a {i}real{/i} horror,{w=0.1} if I know one."
            n 3usqsg "Wouldn't {i}you{/i} agree,{w=0.3} [player]?{w=0.75}{nw}"

        else:
            n 3fcsbg "Now that's a {i}real{/i} horror,{w=0.1} if I know one.{w=0.75}{nw}"

        extend 1fsqsmeme " Ehehe."

    elif Natsuki.isDistressed(higher=True):
        n 3fcsemesi "Ugh..."
        n 2fsqem "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fsqfr " I'm not afraid of flying either."
        n 4fcsan "What exactly do you take me for?{w=0.75}{nw}"
        extend 4fsqan " And even if I {i}was{/i}..."
        n 1fnmfu "Do you {i}seriously{/i} think I'd be dumb enough to share that with someone like {i}you{/i}?"

    else:
        n 1fcsem "Oh,{w=1}{nw}"
        extend 2fsqwr " {w=0.2}shut {w=0.2}{b}up{/b},{w=0.2} [player]."
        n 2fcsantsa "As {i}if{/i} I'd be dumb enough to share any fears I have with a complete loser like{w=0.2}{nw}"
        extend 1fcswrltsa " {i}you{/i}."

    return

# Natsuki enjoys fanart and appreciates the effort that goes into creating it.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_what_do_you_think_about_fanart",
            unlocked=True,
            prompt="What do you think about fanart?",
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            category=["Art", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_what_do_you_think_about_fanart:
    if Natsuki.isAffectionate(higher=True):
        n 2fsqaj "Are you {i}kidding{/i},{w=0.1} [player]?{w=1}{nw}"
        extend 4uchbsedz " I {i}love{/i} fanart!"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Ooh!{w=1}{nw}"
        extend 3unmbg " Fanart?"
        n 3fllbg "Well,{w=0.1} duh!{w=1}{nw}"
        extend 3fcsbg " I'm {i}totally{/i} all for it!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcssf "Ugh...{w=1}{nw}"
        extend 2fsqsl " what now?"
        n 2tsqbo "...Fanart?"
        n 1nsrpu "..."
        n 2nllbo "Yeah,{w=0.3} fanart is fine.{w=1}{nw}"
        extend 2fslpu " I guess."
        n 1ncssf "I can appreciate the passion and effort that people put into their love of something."
        n 4nlrpu "Like...{w=1}{nw}"
        extend 1ncsaj " even if the artwork isn't the best,{w=0.5}{nw}"
        extend 1nllsr " or the music needs some practice,{w=0.5}{nw}"
        extend 1nnmsl " someone's effort still went into it."
        n 2tnmpu "And even if I don't exactly like who the fanart is for?"
        n 2fllsl "I can still admire the work that went into it."
        n 1fcssr "...Heh.{w=1}{nw}"
        extend 4fsqsr " And speaking of things that need work..."
        n 1fsqpu "I don't know if you're a creator or not,{w=0.1} [player]."
        n 2fsqfr "But I can tell this relationship isn't where {i}your{/i} work goes,{w=0.3} is it?{w=1}{nw}"
        extend 2fsran " Jerk."
        return

    else:
        n 1fcsantsa "Oh,{w=0.1} for-{w=0.5}{nw}"
        n 1fcsun "..."
        n 2fsqfutsb "Fanart?{w=1}{nw}"
        extend 2fsquptsb " Really,{w=0.1} [player]?"
        n 1fcsuptsa "..."
        n 2fcssstsa "...Heh."
        n 1fsqupltse "Why would {i}you{/i} bring up something people put so much work and love into?"
        n 1fcsemltsd "You {i}obviously{/i} don't care about either of those things,{w=0.1} do you?"
        return

    n 1ullss "I mean...{w=1}{nw}"
    extend 3fchgn " what's not to love?{w=1}{nw}"
    extend 3uchgnedz " Fanart is {i}awesome{/i}!{w=0.5}{nw}"
    extend 4fspajedz " And it comes in so many forms,{w=0.1} too!"
    n 1ulraj "Like sure,{w=0.1} people show their support for something in a bunch of ways.{w=0.5}{nw}"
    extend 1nllbo " Sharing posts,{w=0.1} attending events,{w=0.5}{nw}"
    extend 3nnmsm " all those kinds of stuff."
    n 3fcsbg "But I think it takes some real guts to stand up and create something new!"
    n 4uskajesh "T-{w=0.1}that's not to say those who don't make any aren't {i}real{/i} fans or anything like that!"
    n 2flleml "Of course not!{w=1}{nw}"
    extend 2flrpol " That's just being dumb."
    n 1ulraj "But...{w=1}{nw}"
    extend 1unmaj " I just think it's a super neat way to show how much you appreciate something."
    n 3fnmss "Plus with how active creators are on social media now,{w=0.5}{nw}"
    extend 3fchbg " it's super easy to reach out and share your work!"
    n 1fsldv "Not just with your favorite director,{w=0.1} or manga writer or whatever either,{w=0.5}{nw}"
    extend 4fspajedz " but with other fans too!"
    n 1fcsbg "Everybody wins,{w=0.1} right?{w=0.5}{nw}"
    extend 1nllbg " Ahaha..."
    n 2kllss "Well...{w=0.5}{nw}"
    extend 2nllsl " almost."
    n 1fsqpu "What I {i}really{/i} hate is when people look at something someone made,{w=0.5}{nw}"
    extend 3fcswr " and then just give them a bunch of grief over it!"
    n 1flrem "Like if the creator is learning and made a mistake,{w=0.1} or if they had another take on something.{w=1}{nw}"
    extend 4fcsan " It's so stupid!"
    n 1fcsaj "I get {i}constructive{/i} criticism,{w=1}{nw}"
    extend 2fsqan " but just being a jerk because it isn't {i}exactly{/i} how {i}you{/i} want it?{w=1}{nw}"
    extend 2fcsem " Come {b}on{/b}!"
    n 2fsrem "Get a grip."
    n 1fcsemesi "..."
    n 3fslsl "Hard to believe people can be so {i}entitled{/i} over something others do for free,{w=0.1} huh?{w=0.5}{nw}"
    extend 3fslpo " Jerks."
    n 3nllpo "Well,{w=0.1} anyway.{w=1}{nw}"
    extend 3nslpo " Enough about people like {i}that{/i}."
    n 1nlrbo "I don't know if you do any fanart or anything,{w=0.1} [player]..."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
        n 4fchsmleme "Probably~."

    n 2fnmpo "But you better not be letting people push you around over yours!"
    n 2fsqpo "...Or be giving people a hard time over theirs."
    n 1fcsbg "...Because that's where I {i}draw{/i} the line!{w=1}{nw}"
    extend 1fsqsm " Ehehe."

    return

# Natsuki gives her advice on interviewing for jobs, etc.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_interview_properly",
            unlocked=True,
            prompt="How to interview properly",
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            category=["Life", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_interview_properly:
    n 1fllbo "Hmm..."
    n 2tllbo "Hey,{w=0.5}{nw}"
    extend 4tnmpu " [player]."
    n 1tlrbo "It's kinda out of the blue,{w=0.5}{nw}"
    extend 2nsrss " but I was curious."
    n 2tnmaj "When was the last time you interviewed for something?"
    n 1tlrbo "Or...{w=0.5} now that I think about it...{w=1}{nw}"
    extend 4tnmpu " have you interviewed for {i}anything{/i} before?{w=1}{nw}"
    extend 4unmaj " Like,{w=0.1} at all?"
    n 2fslss "Because if there's one thing I've heard...{w=1}{nw}"
    extend 2fnmpo " it's how anxious everyone seems to get over interviewing!"
    n 2ksqposbl "I'm being serious!{w=0.5}{nw}"
    extend 4fllem " People just get so worked up over it all.{w=1}{nw}"
    extend 4fcsem " Like it's rocket science or something."
    n 1flraj "I mean...{w=1}{nw}"
    extend 1unmca " I've never had to interview for anything super important myself."
    n 1ulraj "We had some practice interviews at school,{w=0.1} obviously.{w=1}{nw}"
    extend 2nslss " I was too busy with studies to try at getting a part-time job or anything."
    n 2fsqsg "...But who says that doesn't mean I can teach you a thing or two?{w=0.75}{nw}"
    extend 2fchgn " Ehehe."
    n 1fsqsm "You should know what time it is by now..."
    n 1fcsbg "...So listen up,{w=0.1} [player]!"
    n 3fcscsesm "You're about to learn how to ace your interviews from a pro!"

    n 1fnmbg "So!{w=0.75}{nw}"
    extend 1fsqsm " The first order of business..."
    n 3fllbg "Research,{w=0.5}{nw}"
    extend 3tsqss " duh!"
    n 1usqaj "If there's one thing you gotta know before going to interview for something,{w=0.5}{nw}"
    extend 3fchgnelg " it's what you're actually interviewing {i}for{/i}!"
    n 1fllaj "You wouldn't skimp out on revising before a big test,{w=1}{nw}"
    extend 4tnmsl " and interviews really aren't much different when you think about it."
    n 4fnmss "Interviewing for some big-shot company?{w=1}{nw}"
    extend 1fcsbg " Check them out online and take notes!"
    n 1ullaj "Obviously you need to read up on what they do and where they actually {i}are{/i},{w=1}{nw}"
    extend 4fnmaj " but don't underestimate the power of trivia!"
    n 1ullpu "Even just knowing random stuff like when they were founded,{w=1}{nw}"
    extend 1nlrss " or what awards they won recently {w=0.1}-{w=0.5}{nw}"
    extend 3fcsss " it all shows the effort you're putting in."
    n 3tsqss "And when it comes down to the wire?"
    n 3fsqbg "Even something tiny like that can just about tip the scales."

    n 1fcsss "Next up...{w=0.5}{nw}"
    extend 2fnmca " revision!"
    n 4ullaj "It doesn't matter if you're trying to get a job,{w=1}{nw}"
    extend 4nlrbo " or land a new position on some sort of council."
    n 1nsqpu "Whatever it is...{w=0.5}{nw}"
    extend 3fchlgelg " you gotta be able to {i}prove{/i} you know what you're even talking about!"
    n 1ulraj "Of course, the revision totally depends on what you're going for."
    n 4usqss "Some kind of programming job?{w=0.5}{nw}"
    extend 4fchbg " Refresh yourself on all your weird terminology and techniques!"
    n 3tsgsm "Joining the history club?{w=1}{nw}"
    extend 3fcsss " Read up on some common history questions!"
    n 1nsqpu "And trust me,{w=0.75}{nw}"
    extend 1nsqsr " the {i}last{/i} thing you wanna do is embarrass yourself over simple stuff you should {i}really{/i} know..."
    n 1nllun "...Or something you forgot you mentioned on your application."
    extend 4kchblesd " Oops!"
    n 1nllaj "So...{w=0.5}{nw}"
    extend 3fcsss " study up,{w=0.1} 'kay?"

    n 1fchbg "Alright!{w=0.75}{nw}"
    extend 3tsqss " Keeping up so far,{w=0.1} [player]?"
    n 3fsqsm "You better be...{w=1}{nw}"
    extend 3fchgn " 'cause we're almost done here!"
    n 1unmaj "So,{w=0.1} next on the list -{w=0.5}{nw}"
    extend 1nsrss " and probably the most important of all..."
    n 4fspajedz "Presentation!"
    n 1fllaj "You can have the best credentials in the world,{w=1}{nw}"
    extend 3fsqsr " but that isn't gonna help much if you're mumbling everything {w=0.1}-{w=0.5}{nw}"
    extend 3fchlgelg " or if you just look ridiculous!"
    n 1fnmsr "So!"
    n 2fcspo "Make sure you dress properly for whatever it is.{w=1}{nw}"
    extend 2fllpu " If there's a dress code,{w=0.1} {i}follow it{/i}."
    n 2fsqpo "...And {i}don't{/i} flake out on your clothes.{w=1}{nw}"
    extend 4nlrbo " Iron them if they're all creased,{w=0.1} buy new ones if you need to.{w=0.2} That kind of thing."
    n 2tnmpu "But most of all,{w=0.1} [player]?"
    n 2fsqaj "{i}Never{/i}{w=0.2} forget the basics."
    n 1ullss "Be punctual,{w=0.1} be polite.{w=0.2} Remember {w=0.1}-{w=0.5}{nw}"
    extend 2fsqss " people want someone they can {i}like{/i},{w=0.75}{nw}"
    extend 2fsrpo " not just someone who can get the job done!"

    n 4unmajesu "...Oh,{w=0.5}{nw}"
    extend 2tnmpu " and [player]?"
    n 1fcspu "Just...{w=1}{nw}"
    extend 4knmsrlsbl " be honest too,{w=0.1} alright?"
    n 1fllsrl "It isn't a fault to admit when you don't know something."
    n 1tnmpu "And when you actually stop to think about it from their perspective,{w=1}{nw}"
    extend 2tnmem " if someone is prepared to just lie to your face at an interview..."
    n 2tsqem "...Then what {i}else{/i} are they gonna lie about?"
    n 1tllsssbl "Just some food for thought."

    n 1ncspuesi "..."
    n 1nlrss "...Wow,{w=0.5}{nw}"
    extend 3fchbgelg " I gotta learn when to stop rambling on!{w=0.2} Jeez!"
    n 3fsrssl "That was almost like an interview speech itself,{w=0.1} huh?"

    if Natsuki.isEnamored(higher=True):
        n 1ullpu "Or...{w=1}{nw}"
        extend 2nsrssl " I guess more like an induction,{w=0.1} really."
        n 2fsqdvf "You already got the job with me,{w=0.1} a-{w=0.3}after all."

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=1}{nw}"
            extend 1nchbll " Love you,{w=0.1} [player]~!"

        else:
            n 1fsrsml "Ehehe..."

    else:
        n 1ullpu "Or...{w=1}{nw}"
        extend 2tnmbo " since we're both stuck here?"
        n 1fsqsm "...More like an induction,{w=0.1} actually."
        n 3fchgn "Ehehe."

    return

# Natsuki gives the player her dim view on bullying, and bullies generally.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_bullying",
            unlocked=True,
            prompt="Bullying",
            category=["Society", "Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_bullying:
    n 1fslpu "..."
    n 2fcspuean "Tch!"
    n 2fsran "..."
    n 1tnmaj "Eh?{w=0.5}{nw}"
    extend 4uskemesh " O-{w=0.3}oh!{w=0.5}{nw}"
    extend 1uwdaj " [player].{w=1}{nw}"
    extend 2flrbglsbl " Ahaha."
    n 1fllbg "I...{w=0.5} was kinda just thinking out loud again."
    n 1ullpu "And,{w=0.75}{nw}"
    extend 2nslpu " well..."
    n 1nsqpu "I just had something else come to mind.{w=1}{nw}"
    extend 2fcsem " Something I {i}really{/i} can't stand."
    n 1fsqsr "Bullies.{w=1}{nw}"
    extend 2fcsfu " I can't think of anything I {i}hate{/i} more!"
    n 1flrem "Like,{w=0.5}{nw}"
    extend 4fsqfu " have you ever had the {i}pleasure{/i} of dealing with one?"
    n 1fcsan "It takes a {i}real{/i} piece of work to go out and mess with people on purpose."
    n 2fllwr "You don't even need to be {i}doing{/i} anything!"
    n 2flrem "Just looking the 'wrong' way,{w=0.3}{nw}"
    extend 2fllan " enjoying the 'wrong' thing {w=0.1}-{w=0.3}{nw}"
    extend 4fsqfu " any so-{w=0.1}called {i}excuse{/i},{w=0.1} they'll take."
    n 1fcsem "And when I say mess with people...{w=1}{nw}"
    extend 1fsqem " I don't just mean physically,{w=0.1} either!"
    n 2fllem "Bullies can do their dirty work in so many different ways,{w=0.1} especially with social media being what is is now.{w=1}{nw}"
    extend 2fcsfu " But that's just as toxic!"
    n 1fsqan "And worse yet,{w=0.5}{nw}"
    extend 2tsqem " if you try to stick up for yourself?{w=1}{nw}"
    extend 2fsrem " When you're exhausted of dealing with all of their crap?"
    n 1fcswrean "People get so high and mighty about it!{w=0.75}{nw}"
    extend 1flrem " Like {i}you're{/i} the reason there's a problem!"
    n 4fllaj "'Stop being so dramatic!'{w=0.5}{nw}"
    extend 4flrwr " 'You're just overreacting!'{w=0.5}{nw}"
    extend 2fcsemesi " Ugh."
    n 2tsqem "At this point?{w=0.75}{nw}"
    extend 2flrbo " I've heard it all."
    n 1fsrbosbl "{i}...Not like that makes it any less annoying.{/i}"
    n 1nllaj "But...{w=1}{nw}"
    extend 1nsqbo " one thing I {i}will{/i} tell you right now,{w=0.1} [player]."
    n 2fsqbol "Do {b}not{/b} let what others say stop you from dealing with it."
    n 2fllbol "It isn't {i}their{/i} problem {w=0.1}-{w=0.3}{nw}"
    extend 4fsqpul " and from experience?"
    n 1fsqsr "There's nothing a bully likes {i}more{/i} than someone who tries to ignore them,{w=0.1} or walk away."
    n 4uskemesu "...T-{w=0.3}that's not to say you gotta freak out or anything crazy like that!{w=0.75}{nw}"
    extend 1fcsem " Just..."
    n 3ksqpo "Read the room,{w=0.1} you know?{w=0.75}{nw}"
    extend 3fllpo " Context matters!"
    n 1fcsaj "Always make sure you use the best tools you have to get any jerks off your back."
    n 1fsrss "A school bully doesn't exactly have a manager they report to..."
    n 3fchgnelg "...And work is the {i}last{/i} place for a brawl!{w=0.75}{nw}"
    extend 3fslpol " As {i}boring{/i} as that is."
    n 1nllaj "So...{w=0.5}{nw}"
    extend 2fsrpol " stick up for yourself,{w=0.1} got it?"
    n 1fllss "And make sure you use your brain when you do.{w=1}{nw}"
    extend 3fchgn " That's all I'm saying!"

    if Natsuki.isEnamored(higher=True):
        n 3knmpo "You owe yourself that much,{w=0.1} right?{w=0.75}{nw}"
        extend 1fsqss " Besides,{w=0.1} [player]..."
        n 4fsrssl "I kinda like someone who can show a little guts.{w=0.75}{nw}"

        if Natsuki.isLove(higher=True):
            extend 4fwlcsl " Ehehe."

        else:
            extend 4fsldvless " Ehehe..."

    elif Natsuki.isHappy(higher=True):
        n 3kslpo "You owe yourself that much...{w=0.75}{nw}"
        extend 3ksqpolsbl " right?"

    else:
        n 3fsrpolsbl "You owe yourself {i}that{/i} much,{w=0.1} at least."

    return

# Natsuki calls the player by another name, assuming they aren't blocked from asking about it
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_change_name",
            unlocked=True,
            prompt="Can you call me something else?",
            conditional="persistent._jn_nicknames_player_allowed",
            category=["You"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_change_name:
    # The player hasn't been nicknamed before, or is rocking their normal name
    if (
        persistent._jn_nicknames_player_allowed
        and persistent._jn_nicknames_player_current_nickname == persistent.playername
    ):
        n 1unmaj "Huh?{w=0.5}{nw}"
        extend 2tnmbo " You want me to call you something else?"
        n 1ulraj "...I mean,{w=1}{nw}"
        extend 4tnmbo " I guess I can do that?"
        n 2nslsslesd "It's gonna be super weird calling you something {i}other{/i} than [player],{w=0.1} though..."
        n 1fcsbgl "Well,{w=0.1} whatever!{w=0.75}{nw}"
        extend 1uchgn " I'm not one to judge!"
        n 1unmbg "So..."
        show natsuki 3uchbgl at jn_center

    # Another nickname is being assigned
    else:

        # Account for strikes
        if persistent._jn_nicknames_player_bad_given_total == 0:
            n 4unmaj "Oh?{w=0.5}{nw}"
            extend 4unmbo " You wanna change your name again?"
            n 1fchbg "Okaaay!{w=0.75}{nw}"
            extend 1fchsml " Ehehe."
            show natsuki 3fchbgl at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 1:
            n 1unmbo "You want me to call you something else again?{w=0.75}{nw}"
            extend 4unmaj " Sure thing."
            show natsuki 4unmbo at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 2:
            n 2nsqtr "This again,{w=0.1} [player]?{w=0.75}{nw}"
            extend 1ncsaj " Alright,{w=0.1} fine."
            n 1ncspu "Just...{w=0.3}{w=1}{nw}"
            extend 2nsqsl " think about it properly,{w=0.1} alright?"
            n 1nllaj "So then..."
            show natsuki 2unmca at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 3:
            n 2fsqsr "..."
            n 1fcsboesi "..."
            n 1fslsl "...Fine,{w=0.1} [player]."
            n 2fsqpu "Just keep in mind what I said {i}last time{/i}."
            show natsuki 2nsqsl at jn_center

    # Validate the nickname, respond appropriately
    $ nickname = renpy.input(prompt="What were you thinking of,{w=0.3} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n 1nnmbo "Oh.{w=1}{nw}"
        extend 2nllpo " Well,{w=0.1} I guess that's alright...{w=1}{nw}"
        n 1uchgn "Just means less I gotta remember!{w=0.5}{nw}"
        extend 4fchsmelg " Ehehe."

        return

    else:
        $ nickname_type = jn_nicknames.getPlayerNicknameType(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 1fllpu "Are...{w=1}{nw}"
        extend 3tnmpu " you sure that's even a {i}name{/i}?"
        n 3tlrpo "..."
        n 1nlrss "...Yeah,{w=0.75}{nw}"
        extend 4nsqbgsbl " I think I'll just stick with [player].{w=0.5}{nw}"
        extend 4fchblsbr " Sorry!"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 1fsqemsbl "...Really,{w=0.1} [player]?{w=0.75}{nw}"
        extend 2fnmwrsbl " Why would you even {i}suggest{/i} that?"
        n 2flleml "You must have {i}known{/i} I wouldn't like it!"
        n 1fcsslesi "..."
        n 1ncspu "...Whatever.{w=1}{nw}"
        extend 2fsrsl " Maybe you just weren't using your head enough."
        n 2fcspu "Just...{w=0.3} {i}think{/i} a little more next time."
        n 4knmsll "Please?"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 2fskwrlesh "...E-{w=0.2}excuse me?!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 1fnmwr "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 1fnmfu " That's an {b}awful{/b} name!"
        n 2fcsan "...And I'd be even {i}more{/i} awful to use it!"
        n 2fsqfu "{i}Not{/i} happening,{w=0.1} [player]!"
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 1fscwresh "Y-{w=0.2}you said {i}what{/i} now?!{w=1}{nw}"
        extend 2fsqfuean " I-{w=0.1}is that some kind of joke?!"
        n 1fcssc "I am {i}not{/i} getting involved with dirt-slinging like that!"
        n 2fcsan "And unless you want a bar of soap express-shipped to your {b}mouth{/b}..."
        n 2fsqfu "I suggest {i}you{/i} don't either."
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 1fsgdv "..."
        n 3fchgnesm "Pffffft!"
        n 3fchbs "Come on,{w=0.3} you dork!{w=0.75}{nw}"
        extend 3fchgnelg " Be serious,{w=0.1} will you?"
        n 4flldvl "There's no way I'm calling you {i}that{/i}!"

        return

    else:
        $ neutral_nickname_permitted = False

        # Player going with what they're already called
        if nickname.lower() == player.lower():
            n 2tslsssbl "..."
            n 1tnmsssbl "...Business as usual then,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1fsqsm " Ehehe."
            n 3fchbl "Well,{w=0.2} whatever you say!"

            $ neutral_nickname_permitted = True

        # Player going back to the name they gave when starting JN originally
        elif nickname.lower() == persistent.playername.lower():
            n 2tsgcs "Oho?{w=0.75}{nw}"
            extend 2tsqsg " Finally getting bored of all the nicknames,{w=0.1} are we?"
            n 1fchsm "Ehehe."
            n 1fchbgeme "Right-o!{w=0.75}{nw}"
            extend 3fwlbl " Good old [nickname] it is!"

            $ neutral_nickname_permitted = True

        # A player might actually be named Natsuki, so we don't block it
        elif nickname.lower() == n_name.lower() and n_name.lower() != "natsuki":
            n 1nllaj "You...{w=1}{nw}"
            extend 2tsqbo " really {i}didn't{/i} think this one through,{w=0.1} did you?"
            n 2tsqpueqm "Do you even know how confusing that'd be?"
            n 1fcsbg "Nah.{w=0.5}{nw}"
            extend 3fchgnelg " Business as usual it is!"

        # Fallback for anything not categorised
        else:
            n 2tnmss "[nickname],{w=0.1} huh?"
            n 1fllbo "Hmm..."
            n 1unmbg "Well,{w=0.1} works for me!{w=0.75}{nw}"
            extend 4uchsmeme " Consider it done,{w=0.3} [nickname]!"

            if nickname.lower() == "natsuki":
                n 2nslsssbl "...Heh."
                n 1nsldvsbl "{i}Natsuki{/i}."

            $ neutral_nickname_permitted = True

        # Finally, assign the neutral/easter egg nickname if it was permitted by Natsuki
        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_player_current_nickname = nickname
            $ player = persistent._jn_nicknames_player_current_nickname

        return

    # Handle strikes
    if persistent._jn_nicknames_player_bad_given_total == 1:
        n 2fcsem "Yeesh...{w=1}{nw}"
        extend 2tnmem " who woke {i}you{/i} up on the wrong side of the bed this morning?"
        n 1fllsl "..."
        n 3fcsslesi "...Look,{w=0.1} [player]."
        n 1fnmsl "I get it.{w=0.75}{nw}"
        extend 1flrbo " Maybe you thought you were being funny or something."
        n 3fnmfr "Just knock it off,{w=0.1} alright?{w=1}{nw}"
        extend 3tsqpu " Because honestly?"
        n 1fslsl "I really {i}don't{/i} see the humor."

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_player_bad_given_total == 2:
        n 2fcsan "I honestly can't believe you,{w=0.1} [player].{w=1}{nw}"
        extend 1fsqfr " Were you even {i}listening{/i} last time?{w=1}{nw}"
        extend 4fnmem " Did you even {i}hear{/i} me?"
        n 3fcssfesi "..."
        n 1fsqsf "...Alright,{w=0.1} look.{w=1}{nw}"
        extend 1fsqbo " I'm just gonna get to the point,{w=0.1} so listen up."
        n 2fnmem "{i}Quit messing me around with this,{w=0.1} [player].{/i}"
        n 2fcsem "You make it...{w=0.75}{nw}"
        extend 1fcsunl " difficult...{w=0.75}{nw}"
        extend 1fsrunl " to like you when you behave like {i}that{/i}."

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_player_bad_given_total == 3:
        n 2fcsful "You are just {i}unreal{/i},{w=0.1} [player]."
        n 1fsqscean "{i}How many times{/i} do I have to give you crap over this to get you to wise up?!"
        n 1fsqwrean "Are you {i}trying{/i} to earn a smack?"
        n 2fcsfuesi "..."
        n 2fcsan "Well,{w=0.3} you know what?{w=1}{nw}"
        extend 1fsqan " I'm sick of it."
        n 1fcswr "I am {b}done{/b} giving you chances with this,{w=0.3} [player].{w=1} You're on {i}very{/i} thin ice."
        show natsuki 1fsqfu at jn_center

        menu:
            n "Comprende?"

            "I understand.":
                n 2fsqsr "Heh.{w=0.75}{nw}"
                extend 1fnmfr " {i}Now{/i} you understand,{w=0.1} do you?"
                n 4fsqem "...Then {i}act{/i} like it,{w=0.1} [player]."

                $ Natsuki.percentageAffinityLoss(3)

            "...":
                n 2fsqem "...Seriously,{w=0.1} [player]?{w=1}{nw}"
                extend 1fsqsr " You're really going to act like a child about this?"
                n 2fcsan "Quit it and {i}grow up{/i}."

                $ Natsuki.percentageAffinityLoss(5)

        # Apply penalty and pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    elif persistent._jn_nicknames_player_bad_given_total == 4:
        # Player is locked out of nicknaming themselves
        n 1fcsem "Heh.{w=1}{nw}"
        extend 2fsqemean " You just {i}couldn't resist{/i},{w=1}{nw}"
        extend 2fsqslean " could you?"
        n 1fcsan "I'm {b}done{/b} with you making a fool out of me with this."
        n 1fsqfu "Don't say I didn't warn you.{w=2}{nw}"
        extend 2fsrsr " Jerk."

        # Apply affinity/trust penalties, then revoke nickname priveleges and finally apply pending apology
        python:
            get_topic("talk_player_change_name").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_player_allowed = False
            persistent._jn_nicknames_player_current_nickname = persistent.playername
            player = persistent.playername
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    return

# Natsuki asks about the player's birthday.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_players_birthday_intro",
            unlocked=True,
            prompt="My birthday",
            category=["You"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_players_birthday_intro:
    # Already the player's birthday
    if jnIsPlayerBirthday():
        n 4tnmpueqm "Huh?{w=0.75}{nw}"
        extend 1tnmaj " What about your birthday,{w=0.2} [player]?"
        n 1fsqsm "We're {i}already{/i} celebrating it,{w=0.75}{nw}"
        extend 2tsqss " aren't we?"
        n 1fsqsm "Ehehe."
        n 3fcsbg "Sorry,{w=0.2} [player]..."
        n 3fchgnlelg "But no double-dipping for you!"

        return

    # Player has already discussed their birthday with Natsuki
    elif get_topic("talk_players_birthday_intro").shown_count > 0:
        n 4tnmpueqm "Huh?{w=0.75}{nw}"
        extend 1tnmbo " Your birthday?"

        if persistent._jn_player_birthday_day_month is not None:
            n 2fslaj "Wait...{w=1}{nw}"
            extend 2fsrpu " didn't you already share that with me?"
            n 1fskajesh "...{w=0.5}{nw}"
            n 4fnmem "H-{w=0.3}hey!"
            n 1fsqsm "Nice try,{w=0.2} [player].{w=1}{nw}"
            extend 3fcsbgesm " But you're not getting anything early!"
            n 3tsqsg "I guess you're just gonna have to wait~."
            n 1fchsm "Ehehe."

            return

        else:
            n 1unmaj "Oh,{w=0.2} right!{w=1}{nw}"
            extend 3tnmss " You never actually {i}told{/i} me,{w=0.2} did you?{w=0.75}{nw}"
            extend 1tllss " Duh!"
            n 1ullaj "So..."

        menu:
            n "Did you wanna share your birthday with me now,{w=0.2} [player]?"

            "Of course!":
                n 3fcssmesm "Ehehe.{w=0.5}{nw}"
                extend 1fcsbg " I knew you'd come around!"
                n 4usgcsl "I guess you really just can't say 'No' to a pretty girl,{w=0.2} huh?{w=1}{nw}"
                extend 4fllbgl " Ahaha."
                n 1uskajesh "Oh!{w=0.5}{nw}"
                extend 1nllss " Right,{w=0.2} before I forget."
                n 2fnmpu "Not that I'd {i}expect{/i} you to get it wrong,{w=0.2} but I wanna make a {b}permanent{/b} record of this."
                n 1ullbo "So...{w=1}{nw}"
                extend 3nsqpo " no messing around,{w=0.2} alright?{w=1}{nw}"
                extend 3nchgn " 'Preciated!"
                # Continue to input

            "I still don't feel comfortable sharing that.":
                n 2kwmsr "[player]...{w=1.5}{nw}"
                extend 2ksrbo " come on..."
                n 1kslca "I'm not gonna tease you about it,{w=0.2} or anything..."

                return

    # Player has never discussed their birthday with Natsuki before
    else:
        n 1nslbo "...Huh."
        n 2tnmbo "You know,{w=0.2} [player].{w=1}{nw}"
        extend 2unmaj " I actually think I'm kinda getting to know you a little more now."
        n 4flrbg "We've already been talking a bunch,{w=0.2} after all."

        if persistent.jn_player_appearance_eye_colour:
            n 1ulraj "I mean,{w=0.75}{nw}"
            extend 3nchbg " I even know what you {i}look{/i} like now!"
            n 3fchsmeme "If {i}that{/i} isn't a sign of trust,{w=0.2} I'm not sure what is."

        n 1nllpu "But...{w=1}{nw}"
        extend 1nnmsr " something just hit me.{w=1}{nw}"
        extend 2nsqca " Something important."
        n 4uskem "...And that's that I have literally no idea when your {i}birthday{/i} is!{w=1}{nw}"
        extend 1fbkwr " I never even thought to {i}ask{/i}!"
        n 1kcsemesi "Man...{w=1}{nw}"
        extend 3fslpol " I can't {i}believe{/i} I never brought that up earlier..."
        n 3fsqpo "And come on.{w=0.5}{nw}"
        extend 3nsqpo " Let's be real,{w=0.2} here."
        n 1fcswr "What kind of a friend misses birthdays?!"
        n 4kllbo "...Especially when there's only {i}one{/i} birthday to remember nowadays."
        n 4ksrsl "..."
        n 2fcseml "A-{w=0.3}anyway!"
        n 2flrpo "I'd have to be a real jerk not to {i}at least{/i} ask."

        if get_topic("talk_aging").shown_count > 0:
            n 2nllaj "I think I mentioned before how I don't really care how old you are,{w=1}{nw}"
            extend 2nllpol " I just wanna make sure I don't miss the date."
            n 1fcsbg "I'm not counting candles for anybody's cake!{w=0.5}{nw}"
            extend 3fcssmesm " Ahaha."

        n 4unmaj "So...{w=0.3} how about it,{w=0.2} [player]?"

        menu:
            n "Did you wanna share your birthday with me?"

            "Sure!":
                n 3fcsbgl "Y-yeah!{w=0.5}{nw}"
                extend 3fcssml " I knew you would!"
                n 1ullaj "I know I asked what kind of friend would miss a birthday..."
                n 2flrpo "But you can't miss something you didn't know about!"
                n 4uskajesh "Oh!{w=0.5}{nw}"
                extend 4nllss " Right,{w=0.2} before I forget."
                n 1fnmpu "Not that I'd {i}expect{/i} you to get it wrong,{w=0.2} but I wanna make a {b}permanent{/b} record of this."
                n 1ullbo "So...{w=1}{nw}"
                extend 3nsqpo " no messing around,{w=0.2} alright?{w=1}{nw}"
                extend 3nchgn " 'Preciated!"
                # Continue to input

            "I'm not comfortable sharing that.":
                n 1nnmbo "...Oh."
                n 2fcseml "W-{w=0.3}well,{w=0.2} that's fine,{w=0.5}{nw}"
                extend 2flrpo " I guess."
                n 2nsqpo "Just let me know if you change your mind then,{w=0.2} 'kay?"

                return

    n 1nchbg "Alright!"
    jump talk_players_birthday_input

label talk_players_birthday_input:
    n 1fsqsm "So...{w=1}{nw}"
    extend 3tsqsm " what {b}month{/b} were you born in,{w=0.2} [player]?"
    show natsuki 3tsqsm at jn_left

    # Get the month the player was born
    python:
        # Generate month options
        month_options = [
            ("January", 1),
            ("Feburary", 2),
            ("March", 3),
            ("April", 4),
            ("May", 5),
            ("June", 6),
            ("July", 7),
            ("August", 8),
            ("September", 9),
            ("October", 10),
            ("November", 11),
            ("December", 12),
        ]
    call screen scrollable_choice_menu(month_options)

    if isinstance(_return, int):
        show natsuki at jn_center
        $ player_birthday_month = _return

    $ response_month = datetime.date(datetime.date.today().year, player_birthday_month, 1).strftime("%B")
    n 4unmbo "[response_month],{w=0.2} huh?{w=1}{nw}"
    extend 1nchbg " Gotcha!"
    n 1unmss "And what about the {b}day{/b}?"

    # Get the day the player was born for the month they chose
    $ player_input_valid = False
    $ import calendar
    while not player_input_valid:
        $ player_input = renpy.input(
            prompt="What day were you born on?",
            allow=jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES, length=2
        )
        $ player_input = int(player_input) if player_input.isdigit() else None

        if not player_input or player_input == 0:
            n 4tsqpueqm "Huh?{w=1}{nw}"
            extend 2fnmpo " Come on,{w=0.2} [player]!{w=0.2} You gotta tell me what day!"

        # We use 2020 here, as it is a leapyear
        elif not jnGetIsDateValid(2020, player_birthday_month, player_input):
            n 1fsqsr "[player].{w=0.2} Please.{w=1}{nw}"
            extend 2nsqpo " Take this seriously."

        else:
            # Get ready to lead in to the next stage of setup
            $ player_input_valid = True
            $ persistent._jn_player_birthday_day_month = (player_input, player_birthday_month)

    n 3nchsm "Oki-doki!{w=0.5}{nw}"
    extend 3ullaj " So just to double check..."
    show natsuki 1tnmbo

    $ birthday_formatted = "{0} {1}{2}".format(
        jnGetMonthNameFromInt(persistent._jn_player_birthday_day_month[1]),
        persistent._jn_player_birthday_day_month[0],
        jn_utils.getNumberOrdinal(persistent._jn_player_birthday_day_month[0])
    )

    menu:
        n "Your birthday was [birthday_formatted],{w=0.2} right?"

        "Yes, that's right.":
            if persistent._jn_player_birthday_day_month == (29, 2):
                # Leap year, so celebrate on 28th instead and mark as leap year for future use
                $ persistent._jn_player_birthday_is_leap_day = True
                n 1fcspu "...Wait.{w=1}{nw}"
                extend 4tnmpueqm " Isn't that a leap day too?"
                n 2nllansbl "Yeesh..."
                n 2fslposbl "..."
                n 1fcsajsbl "Actually,{w=0.75}{nw}"
                extend 1unmaj " you know what?"
                n 3ullss "I'm...{w=1}{nw}"
                extend 3fcsbgl " juuuust{w=0.3} gonna chalk down the 28th as well."
                n 4fchgnl "Sorry [player]!{w=0.75}{nw}"
                extend 4fchbllelg " No escaping the birthday cheers for you!"

            else:
                n 3fchsm "Gotcha!"

            jump talk_players_birthday_outro

        "No, that's not right.":
            n 4tsqpueqm "Huh?{w=1}{nw}"
            extend 2nsqpo " Really?"
            n 2nsrss "Let's...{w=1} try that again."
            jump talk_players_birthday_input

label talk_players_birthday_outro:
    python:
        import datetime

        today_day_month = (datetime.date.today().day, datetime.date.today().month)
        before_birthday = (
            today_day_month[1] < persistent._jn_player_birthday_day_month[1]
            or (
                today_day_month[1] == persistent._jn_player_birthday_day_month[1]
                and today_day_month[0] < persistent._jn_player_birthday_day_month[0]
            )
        )

    if jnIsPlayerBirthday():
        # It's the player's birthday today
        n 1nchbg "Okaaay!{w=0.2} So I think that's-{w=0.5}{nw}"
        n 4uskemesh "...!{w=1}{nw}"
        n 1uskajl "Oh,{w=1.5}{nw}"
        extend 2kbkwrl " {b}CRAP{/b}!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 4knmeml "[player_initial]-{w=0.3}[player]!{w=0.2} It's TODAY?!{w=0.5}{nw}"
        extend 2flleml " Why didn't you {i}say{/i} anything?!"
        n 1nsrunl "Uuuuuu...{w=1}{nw}"
        extend 3kcsemedr " now I really look like a total jerk..."
        n 3ncsemesi "...{w=0.5}{nw}"
        n 1fcsem "Right!{w=1}{nw}"
        extend 1fcswr " Then there's only one thing for it!{w=1.5}{nw}"

        # Have to hard set this because we jump away from the label, and lose context of it for topic metric set on call_next_topic return
        $ birthday_topic = get_topic("talk_players_birthday_intro")
        $ birthday_topic.shown_count = 1
        $ birthday_topic.last_seen = datetime.datetime.now()

        # Prep for birthday
        $ jn_globals.force_quit_enabled = False
        stop music
        play audio switch_flip
        show black zorder JN_BLACK_ZORDER
        $ jnPause(5)
        $ push("holiday_player_birthday")

        # Go!
        $ renpy.jump("call_next_topic")

    elif before_birthday:
        # Player's birthday coming up
        n 3tsqbg "And hey!{w=0.75}{nw}"
        extend 3fwlsm " Looks like I still got some time after all!"
        n 1fchsmleme "Ehehe."

    else:
        # Player's birthday was missed
        n 4unmem "Wait,{w=0.5} seriously?{w=1}{nw}"
        extend 1knmem " I missed it already?{w=1.5}{nw}"
        extend 2nsrpo " Aww..."

    n 2nllpo "Well...{w=1}{nw}"
    extend 1nllss " thanks anyway.{w=1}{nw}"
    extend 3nlrdv " For sharing,{w=0.2} I mean."
    n 2nsrpo "..."
    n 1nsraj "I...{w=0.5}{nw}"
    extend 3tnmss " guess I better return the favor,{w=0.2} huh?"
    n 4nslcal "Just promise you won't make it all awkward."
    n 1ncsemlesi "..."
    n 2nsrssl "It's May 1st.{w=1}{nw}"
    extend 2nsqpol " Don't make me say it twice."

    $ persistent._jn_natsuki_birthday_known = True
    
    n 1nllpu "And...{w=1}{nw}"
    extend 4tnmbo " [player]?"
    n 1fsqss "I hope you know that you better prepare yourself."
    n 3fcsbg "'Cause I'm going all out next time!{w=1}{nw}"
    extend 1nchgn " Ehehe."

    if Natsuki.isLove(higher=True):
        n 4fchblleaf "Love you,{w=0.2} [player]~!"

    return

# Natsuki allows the player to see any poems she's written for them previously.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_can_i_see_a_poem",
            unlocked=True,
            prompt="Can I see a poem you've written for me?",
            conditional=(
                "len(jn_poems.JNPoem.filterPoems("
                    "jn_poems.getAllPoems(),"
                    "unlocked=True"
                ")) > 0"
            ),
            category=["Literature"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_can_i_see_a_poem:
    if Natsuki.isEnamored(higher=True):
        n 1fcsbg "Duh!{w=0.5}{nw}"
        extend 3nchgnl " Of course you can!"
        n 3fsqpol "I'd be offended if you {i}didn't{/i} wanna see them again.{w=1}{nw}"
        extend 1fsqsml " Ehehe."
        show natsuki 4klrsml at jn_left

    elif Natsuki.isAffectionate(higher=True):
        n 1unmajl "Huh?{w=1}{nw}"
        extend 2fllssl " Oh,{w=0.2} those."
        n 1fchbgl "Sure thing!{w=0.5}{nw}"
        extend 3tsqbgl " Just can't get enough of my amazing writing skills,{w=0.2} huh?"
        show natsuki 4flrsml at jn_left

    else:
        n 1unmajl "Huh?{w=1}{nw}"
        extend 1nllbo " Oh,{w=0.2} my poems."
        n 4unmbo "Sure,{w=0.2} I guess.{w=1}{nw}"
        extend 2tnmaj " Which one did you wanna see again?"
        show natsuki 4ulrbo at jn_left

    python:
        poem_options = []
        for poem in jn_poems.JNPoem.filterPoems(jn_poems.getAllPoems(), unlocked=True):
            poem_options.append((poem.display_name, poem))

        poem_options.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(poem_options, ("Nevermind.", None))

    if isinstance(_return, jn_poems.JNPoem):
        # A poem was selected, show it
        show natsuki at jn_center

        if Natsuki.isEnamored(higher=True):
            n 1unmaj "[_return.display_name]?{w=0.5}{nw}"
            extend 3nchsmeme " Okaaay!"
            n 3uchsml "Just a second,{w=0.2} [player]..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1unmbg "Here we are!{w=0.5}{nw}"
            extend 1nchsml " Ehehe."

            call show_poem(_return)

            n 2tnmsml "All done?{w=0.5}{nw}"
            extend 2nlrssl " I'll just put that back."
            show natsuki 4nsrsml

        elif Natsuki.isAffectionate(higher=True):
            n 1unmaj "[_return.display_name]?{w=0.2} That one?{w=0.5}{nw}"
            extend 1fchbg " Gotcha!"
            n 3fchsml "Just give me a second here..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1fchbgl "Found it!"

            call show_poem(_return)

            n 2tnmssl "All done?{w=0.75}{nw}"
            extend 2flrdvl " Ehehe."
            show natsuki 2fsrdvl

        else:
            n 1unmaj "That one?{w=0.5}{nw}"
            extend 1nnmss " Alright."
            n 4nllss "Just let me get it out..."

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            n 1ullaj "Well,{w=0.5}{nw}"
            extend 4nlrbol " here you go."

            call show_poem(_return)

            n 2tnmbol "All done?{w=0.5}{nw}"
            extend 2nslssl "I'll just put that back."
            show natsuki 4nslbol

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    else:
        # No poem was selected (player backed out)
        show natsuki at jn_center
        n 1nnmbo "Oh.{w=1}{nw}"

        if Natsuki.isAffectionate(higher=True) and random.randint(0, 10) == 1:
            extend 3nlrpol " Well,{w=0.2} okay then.{w=1}{nw}"
            extend 3fsqbll " Spoilsport.{w=0.75}{nw}"

        else:
            extend 3nlrpol " Well,{w=0.2} okay then."

    return

# Natsuki is more specific with her sweet tooth!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_chocolate_preference",
            unlocked=True,
            prompt="What sort of chocolate do you prefer?",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_chocolate_preference:
    if Natsuki.isAffectionate(higher=True):
        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 2tnmaj "Oh?{w=0.5}{nw}"
            extend 2tsqbo " This again,{w=0.2} huh?"
            n 4tsrsm "..."

        else:
            n 1unmaj "Ooh!{w=0.75}{nw}"
            extend 2tsqbg " My favorite type of chocolate,{w=0.2} you say?"

        n 1nslss "...Why,{w=0.5}{nw}"
        extend 4fsqsm " [player]?"
        n 3fcsbglsbl "Y-{w=0.2}you aren't trying to {i}sweeten{/i} me up or something,{w=0.2} are you?{w=0.75}{nw}"
        extend 3fsldvlsbl " Ehehe..."
        n 1fslbolsbl "..."
        n 3fcsbglsbl "W-{w=0.2}well,{w=0.2} anyway!"

    elif Natsuki.isNormal(higher=True):
        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 4tnmboeqm "Huh?{w=1}{nw}"
            extend 2tslpueqm " Didn't you ask me this already,{w=0.2} [player]?"
            n 1ullaj "Well,{w=0.75}{nw}"
            extend 1unmbo " I wouldn't say I've changed my mind..."

        else:
            n 4unmboeqm "Eh?{w=0.75}{nw}"
            extend 2tllbo " My favorite kind of chocolate,{w=0.5}{nw}"
            extend 2tnmss " huh?"
            n 2uupaj "That's...{w=1}{nw}"
            extend 4flrbo " actually a pretty tough one,{w=0.75}{nw}"
            extend 1tnmbo " to be honest."
            n 1ullaj "I mean..."

    elif Natsuki.isDistressed(higher=True):
        n 3fcsansbl "Oh,{w=1}{nw}"
        extend 3fsremsbl " {i}please{/i}."

        if get_topic("talk_chocolate_preference").shown_count > 0:
            n 2fcsemsbl "Really,{w=0.2} [player]?{w=1}{nw}"
            extend 2fsqemsbl " {i}This{/i} again?"

        else:
            n 2fsqslsbl "Really,{w=0.2} [player]?"

        n 1fcssl "..."
        n 3fcsemesi "...Fine.{w=0.75}{nw}"
        extend 3fslbo " For what it even {i}matters{/i} to you."
        n 1fllem "White chocolate,{w=0.2} probably."
        n 4tsqem "...Why?{w=1}{nw}"
        extend 2fcsem " It's cheap,{w=0.5} full of sugars and fats,{w=0.75}{nw}"
        extend 2fcssr " and I could always add it to whatever I wanted."
        n 1fsqfr "What?{w=1}{nw}"
        extend 1fsqaj " Don't act like you {i}seriously{/i} expected anything different.{w=0.75}{nw}"
        n 2fsran "As if {i}I{/i} was the one going to {i}fancy{/i} candy stores to pick out whatever I fancied."
        n 2fsqun "..."
        n 1fslun "Yeah.{w=1}{nw}"
        extend 1fcsfr " Not like I thought {i}you{/i} would get it."
        n 2fcsbo "Whatever."
        n 1flrpu "The others are fine too,{w=0.75}{nw}"
        extend 4fsrfr " I guess."
        n 1fllsl "Milk chocolate is just kinda boring.{w=1}{nw}"
        extend 2fslan " And there's no {i}way{/i} I could get dark chocolate with {i}my{/i} kind of budget."
        n 1fcsboesi "..."
        n 2fslaj "So...{w=1}{nw}"
        extend 2fslsl " yeah.{w=0.75}{nw}"
        extend 2fsrbo " That about sums it up."
        n 1fsqbo "..."
        n 1fnmfr "There.{w=0.3} Happy now?"
        n 2tsqem "Because unless you magically have something to sweeten {i}this{/i} experience up?"
        n 1fcssr "Heh."
        n 2fsqan "I think we're about done here,{w=0.2} {i}[player]{/i}."

        return

    else:
        n 1fcsan "Heh.{w=0.75}{nw}"
        extend 1fsqanltsb " My favorite type of chocolate?"

        if get_topic("event_warm_package").shown_count > 0:
            n 2fsqupltsb "Does your memory {i}seriously{/i} suck as much as your personality does?"
            n 1fcsunltsa "..."
            n 1fsqfrltsb "Allow me to {i}remind{/i} you,{w=0.2} {i}[player]{/i}."

        else:
            n 2fsqupltsb "You {i}really{/i} wanna know,{w=0.2} [player]?"
            n 1fcsunltsa "..."

        n 1fcsupltsa "Not whatever cheap,{w=0.75}{nw}"
        extend 2fnmanltsc " half-{w=0.2}expired{w=0.75}{nw}"
        extend 2fsqwrltsb " trash{w=0.75}{nw}"
        extend 1fnmfultsc " {i}you{/i} would hand me,{w=1}{nw}"
        extend 1fcsfultsa " that's for sure."
        n 2fsqanltsb "Jerk."

        return

    n 1fcstr "It's {i}gotta{/i} be white chocolate.{w=0.75}{nw}"
    extend 3fchbg " Any day of the week!"
    n 4nslcssbr "It {i}is{/i} practically overflowing with sugar...{w=0.75}{nw}"
    extend 4nsrdvsbr " and debatably even {i}chocolate{/i}..."

    if get_topic("event_warm_package").shown_count > 0:
        n 4uspajl "But that {i}taste{/i}!{w=0.75}{nw}"
        extend 1uchtsleme " Especially in hot chocolate!"

    else:
        n 1uspajl "But that {i}taste{/i}!"

    n 1kcsssl "So creamy and light,{w=1}{nw}"
    extend 3kcstsl " with just that hint of vanilla...{w=1}{nw}"
    extend 3fchbgl " I love it!"
    n 4unmajesu "Oh!{w=0.75}{nw}"
    extend 1fchbg " And it's even super convenient for baking!"
    n 1ullss "It's pretty inexpensive -{w=0.5}{nw}"
    extend 2nsrsssbl " since it really doesn't have much {i}actual{/i} cocoa at all -{w=0.5}{nw}"
    extend 2ulrss " I never have to worry about how strong it is,{w=0.75}{nw}"
    extend 2fchsm " plus it goes super well with regular old chocolate too!"
    n 1fchbl "Talk about multipurpose!"
    n 4tsqss "Bought some as a treat and can't finish the job?{w=0.75}{nw}"
    extend 1fchsmeme " No problemo!"
    n 1ullss "Just wrap it back up,{w=0.2} save it,{w=0.75}{nw}"
    extend 3fwlbg " and that's your next cake topping sorted!"
    n 3fcsss "So take it from me,{w=0.2} [player]:{w=1}{nw}"
    extend 3uchgn " it's a confectioner's best friend!"
    n 1fcssm "..."
    n 4unmajesu "...Ah!{w=1}{nw}"
    n 4fllbglsbr "T-{w=0.2}that's not to say the others are terrible,{w=0.2} or anything like that.{w=0.75}{nw}"
    extend 2unmajsbr " Chocolate is super subjective!{w=1}{nw}"
    extend 2nsrsssbr " But..."
    n 1tnmbo "I guess I just don't really see the appeal {i}as{/i} much."
    n 4nslss "Milk chocolate is {i}okay{/i},{w=0.2} but you kinda see it everywhere already."
    n 2fllpu "As for dark chocolate..."
    n 2nsrunsbl "..."
    n 2fcsbglsbr "W-{w=0.2}well,{w=1}{nw}"
    extend 4flrsslsbr " it totally has its place too!"
    n 1unmaj "Sometimes,{w=0.2} that dash of bitterness is just what you need!{w=0.75}{nw}"
    extend 1ullbo " Plus with all the antioxidants and generally the least sugar..."
    n 2tnmsssbl "A-{w=0.2}at least for chocolate?{w=1}{nw}"
    extend 2kchbgsbl " I guess it doesn't really get much healthier than that!"
    n 1fcsbg "So yeah!{w=0.75}{nw}"
    extend 4fllbgsbr " It {i}totally{/i} has its place,{w=0.2} like I said..."
    n 2fslposbr "...Just not in {i}my{/i} mouth.{w=0.75}{nw}"
    extend 2fchsmsbr " That's all I'm saying!"

    if (
        not jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlocked
        and Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
    ):
        # Unlock chocolate plaid outfit, if custom outfits unlocked
        n 2nslss "Man...{w=1}{nw}"
        extend 1ncsfs " all this talk of treats is bringing back all kinds of memories."
        n 2tllaj "In fact..."
        n 4tnmss "I'm {i}sure{/i} I had some kind of cute chocolate themed dress at some point.{w=0.75}{nw}"
        extend 2nchgn " Or at least it felt that way with all the colors."
        n 2ksrfssbl "...And Sayori practically drooling over it."
        n 2kchsm "Maybe I should go dig that out later..."

        $ jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlock()
        $ jn_outfits.getWearable("jn_necklace_tight_golden_necklace").unlock()

    n 1fllajlsbr "A-{w=0.2}anyway!{w=0.75}{nw}"
    extend 1fcsajl " Enough of me yammering on again.{w=0.75}{nw}"
    extend 2tlrsssbl " Jeez."
    n 1unmaj "What about you,{w=0.2} [player]?{w=0.75}{nw}"
    n 1fbkwreex "...Wait!{w=1}{nw}"
    extend 1fcsbg " Don't tell me!"
    n 4fcssresp "..."

    # Dialogue variations
    if Natsuki.isLove(higher=True):
        n 3fcsgs "It {i}has{/i} to be white chocolate.{w=0.75}{nw}"
        extend 3fchbl " Complete no-brainer.{w=1}{nw}"
        extend 4fcsss " Besides..."
        n 4fsldvlsbl "I-{w=0.2}I like to think I {i}know{/i} a sweetheart when I see one."
        n 2fchsmlsbl "Ehehe..."
        n 2fchblfsbl "L-{w=0.2}love you,{w=0.2} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fcsbg "...It's {i}gotta{/i} be white chocolate.{w=1}{nw}"
        extend 4fcssm " Besides..."
        n 2fllssless "H-{w=0.2}how else would our time together be this sweet?"
        n 2fchsmless "Ehehe..."

    elif Natsuki.isAffectionate(higher=True):
        n 1uupaj "...Probably milk chocolate,{w=0.75}{nw}"
        extend 3tsqsm " I'd guess."
        n 3fchgn "...You've gone about as soft,{w=0.2} after all!"

    else:
        n 1fcspu "It's...{w=1}{nw}"
        extend 2tnmpu " actually kinda hard to guess,{w=0.75}{nw}"
        extend 2tllsl " to be honest."
        n 1tnmss "I {i}would{/i} say dark chocolate,{w=0.5}{nw}"
        extend 4tsqss " but..."
        n 3fchgnl "I like to think you aren't {i}that{/i} bitter!{w=0.75}{nw}"
        extend 3nchgn " Ahaha."

    return

# Natsuki discusses her experiences and frustrations learning other languages.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_learning_languages",
            unlocked=True,
            prompt="Learning languages",
            category=["Society"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_learning_languages:
    $ already_discussed_learning_languages = get_topic("talk_learning_languages").shown_count > 0
    if already_discussed_learning_languages:
        n 1ncsemesi "..."
        n 1nsrem "Man...{w=1}{nw}"
        extend 2fcspo " I still can't believe I messed up my German {i}that{/i} badly last time.{w=0.75}{nw}"
        extend 2kslan " Yeesh."
        n 1tnmaj "But anyway,{w=0.2} it's like I said before.{w=0.5}{nw}"
        extend 4kbkwr " Learning a new language is {i}super{/i} tricky!"

    else:
        n 1nllpu "..."
        n 2fllsm "..."
        n 4fsqsm "..."
        n 1fcsss "Heh."
        n 2fcsaj "Ahem!"
        n 1fcssm "..."

        # Natsuki struggles with German
        n 3uchgn "Moin moin,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1usqsm " Was liegt an?{w=0.5}{nw}"
        extend 1fchss " Ehehe."
        n 3fcsbs "Ich wette du wusstest nicht, dass ich nicht {i}nur{/i} Englisch tue,{w=0.2} huh?"
        n 1tsqbg "Du solltest auch versuchen mehr Sprachen...{w=0.5} f-{w=0.2}fluessig..."
        n 2fsrbglsbl "f-{w=0.2}fliessend...?"
        n 1fsrunlesdsbr "..."
        n 2tsremlesssbr "zu reden...?{w=0.5}{nw}"
        extend 2fcsbglesssbr " Sprachfluss!"
        n 4flrbglsbr "O-oder wie man auch sagt -{w=0.3}{nw}"
        extend 1fcsbglsbl " wer rasst..."
        n 2fllunlesssbl "r-{w=0.2}rastet...!{w=0.5}{nw}"
        extend 2klremfesssbl " Hat Rosen...?{w=0.75}{nw}"
        extend 2kllemfesssbl " Mit Rost!"

        n 1fcsunfesssbr "..."
        n 2fcsanfesssbr "Nnnnnn-!"
        n 1fcsemlesssbr "Oh,{w=0.75}{nw}"
        extend 4fbkwrlesssbr " {i}forget it{/i}!{w=0.75}{nw}"
        extend 2kslpul " This is so embarrassing..."
        n 1fslunl "..."

        n 4uskemlesh "...!{w=0.5}{nw}"
        n 2fcswrl "N-{w=0.3}not like I couldn't do it!{w=0.75}{nw}"
        extend 2flleml " I can {i}totally{/i} ace it alone."
        n 1fcseml "I'm...{w=0.5}{nw}"
        extend 4fsrpol " just being put off.{w=0.5}{nw}"
        extend 4fsqpol " Having an {i}audience{/i},{w=0.2} and all."
        n 1fnmpu "But seriously,{w=0.2} [player].{w=0.75}{nw}"
        extend 3tnmaj " Have you ever {i}tried{/i} learning another language?"
        n 1fbkwr "It's super hard!{w=1}{nw}"
        extend 2fslpo " I don't know how people do it!"

    n 1tslpu "Like..."
    n 1unmaj "We had language classes in school -{w=0.5}{nw}"
    extend 2nslss " obviously -{w=0.75}{nw}"
    extend 2fnmpu " but there was never enough time to actually {i}practice{/i}!"
    n 1fllem "We'd get paired up with partners and practice pronunciations and such."
    n 4unmem "But when neither of you actually {i}know{/i} the language,{w=0.5}{nw}"
    extend 2fcswr " how're you meant to know when someone's doing something wrong?"
    n 1fllaj "Then with all the other studies flying around,{w=0.5}{nw}"
    extend 3fsrsr " it's not like we had the spare time to try it outside of school either."
    n 3tsqpu "Plus,{w=0.2} with how complex all the rules are and how much repetition you need,{w=0.5}{nw}"
    extend 3fcsem " one or two classes a week just doesn't cut it!"
    n 1fllpu "Like,{w=0.75}{nw}"
    extend 4fnmem " how is someone supposed to remember if some random household thing has a masculine or feminine name?"
    n 3flrwr "Or how to pronounce some random word-spaghetti that looks like someone just made it all up?!"
    n 1kcsemesi "Ugh..."
    n 1ucspu "I mean...{w=0.75}{nw}"
    extend 1unmpu " don't get me wrong!{w=0.5}{nw}"
    extend 3fcssl " It's not like I {i}didn't{/i} like learning a new language!"
    n 3nsrss "And at {i}least{/i} we got to pick which language we wanted to learn."
    n 3nsqpo "I just wish we got to actually,{w=0.2} well..."
    n 3kslpo "{i}Learn them{/i},{w=0.2} you know?"
    n 1fcsss "Heh.{w=0.5}{nw}"
    extend 4fslsr " Not like any of that ever stopped {i}Monika{/i},{w=0.2} of course."
    n 1nslpu "Though...{w=0.75}{nw}"
    n 2fnmsll "I still kinda feel like I was robbed of experiences in that way."
    n 1fllss "It's easy to forget there's a whole world out there when you only interact with a certain language-speaking part of it!"

    if get_topic("talk_flying").shown_count > 0:
        n 2tllaj "I think I mentioned before that I've never flown anywhere.{w=0.5}{nw}"
        extend 2tnmpu " But if I did?"
        n 1fcsss "I'd want to at least try to learn a little of the language for where I'm going."
        n 1fnmpu "Think about it!{w=0.75}{nw}"
        extend 1fcsbg " If you're already putting in all that money and effort to arrange it all..."
        n 3tsqsmesm "What's a little extra to show some respect,{w=0.2} right?"

    else:
        n 2tsqss "And with how much more you unlock when you know how to talk the languages there?"
        n 1fsqsr "You'd have to be a real dummy not to at {i}least{/i} think about it.{w=0.5}{nw}"
        extend 4fsqsm " Ehehe."

    n 1ullaj "But...{w=0.75}{nw}"
    extend 2nnmbo " that's just me,{w=0.2} I guess."
    n 2tnmss "What about you though,{w=0.2} [player]?"
    $ menu_opening = "Anything new in the language department?" if already_discussed_learning_languages else "You know any other languages?"

    menu:
        n "[menu_opening]"

        "I know another language.":
            if persistent._jn_player_is_multilingual:
                n 4uskemlesh "H-{w=0.3}huh?{w=0.75}{nw}"
                extend 2fnmeml " But you already said you knew another language!"
                n 2fsqsfl "...And you're telling me you went and learned another one?!"
                n 1fsrbol "Wow,{w=0.2} [player]..."
                n 3tsqss "...You really are a show-off,{w=0.2} huh?{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."

            else:
                n 1tsqcs "Oho?{w=0.75}{nw}"
                extend 3fsqbg " Well,{w=0.2} look at you!{w=0.5}{nw}"
                extend 3fsqss " Better not get too cocky now,{w=0.2} [player]..."
                n 1usqsm "You aren't the {i}only{/i} multilingual here,{w=0.2} after all.{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = True

        "I know multiple other languages.":
            if persistent._jn_player_is_multilingual:
                n 1fllem "Oh,{w=0.5}{nw}"
                extend 2fcswr " come {b}on{/b}!{w=0.75}{nw}"
                extend 2fsqem " Really?"
                n 1fslem "You're {i}such{/i} a show-off,{w=0.2} [player]."
                n 4fsqsm "...Ehehe."

            else:
                n 1fsqsr "..."
                n 2fsrpo "...Show-{w=0.2}off.{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = True

        "I'm trying to learn another language.":
            if persistent._jn_player_is_multilingual:
                n 1unmaj "Oh?{w=0.75}{nw}"
                extend 1flrbg " Well,{w=0.2} hey!"
                n 3fsqss "That makes both of us now,{w=0.2} huh?{w=0.5}{nw}"
                extend 4fsqsm " Ehehe."

            else:
                n 4fnmbgesu "Aha!{w=0.5}{nw}"
                extend 3tsqbg " So you're familiar with the struggle too,{w=0.2} huh?"
                n 1fsqsm "Ehehe."
                $ persistent._jn_player_is_multilingual = False

        "I don't know any other languages.":
            if persistent._jn_player_is_multilingual:
                n 1tsqaj "...Huh?"
                n 4uskemlesh "W-{w=0.2}wait a second!{w=0.5}{nw}"
                extend 2fsqem " You already {i}said{/i} you knew another language!"
                n 2fslpol "I wasn't born {i}yesterday{/i},{w=0.2} you jerk..."

            else:
                n 1unmem "...Huh?{w=0.5} Really?{w=0.5}{nw}"
                extend 2knmpo " Not even a little?"
                n 1ncspuesi "Man..."
                n 1nllpu "I gotta admit,{w=0.5}{nw}"
                extend 4nsqbo " that's kinda disappointing."
                n 1fsqbg "...Nothing stopping you from getting started though,{w=0.2} right?{w=0.5}{nw}"
                extend 2fsqsm " Ehehe."
                $ persistent._jn_player_is_multilingual = False

    n 1ullaj "Well,{w=0.2} anyway.{w=1}{nw}"
    extend 2tnmss " I think I've gone on long enough at this point,{w=0.2} huh?"
    n 2tlrss "And,{w=0.2} well...{w=0.75}{nw}"
    extend 4fsqbg " as they say in {i}Deutschland{/i}..."
    n 1ncsss "Alles hat ein Ende,{w=0.5}{nw}"
    extend 3uchgnlelg " nur die Wurst hat zwei!"

    return

# Natsuki pitches the idea of rage rooms and how they can be fun to the player.
# Natsuki smash!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_rage_rooms",
            unlocked=True,
            prompt="Rage rooms",
            category=["Entertainment", "Hobbies"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_rage_rooms:
    $ already_discussed_rage_rooms = get_topic("talk_rage_rooms").shown_count > 0

    if already_discussed_rage_rooms:
        n 2fslss "Man..."
        n 2ullaj "You know,{w=0.5}{nw}"
        extend 2tnmbo " [player]..."
        n 1fcssm "I still can't get my mind off rage rooms."
        n 1ulraj "I know we spoke about them before,{w=0.2} but..."
        n 3nsrss "Well,{w=0.75}{nw}"
        extend 3tnmpu " can you blame me?"

    else:
        n 1ullaj "Hey,{w=0.2} [player]..."
        n 1ulrbo "This is kinda random,{w=0.5}{nw}"
        extend 4ulraj " but..."
        n 2tnmpu "Have you ever been to a rage room before?"
        n 2nslsssbr "I've never actually {i}been{/i} to one myself,{w=0.75}{nw}"
        extend 1ncsaj " but oh.{w=0.5}{nw}"
        extend 1fcsaj " My.{w=0.5}{nw}"
        extend 1fcsaw " God.{w=0.5}{nw}"
        extend 2nsqsr " [player]."

    n 1fcspu "They...{w=0.75}{nw}"
    extend 1fcsaj " look...{w=0.75}{nw}"
    extend 4fspgsedz " {i}awesome{/i}!"
    n 4uwdaj "No,{w=0.2} really!{w=0.75}{nw}"
    extend 2fcspo " I'm serious!"
    n 1ullss "You basically get an entire room full of useless old junk:{w=0.5}{nw}"
    extend 1ulrbo " unwanted furniture,{w=0.2} decorations,{w=0.2} old computer hardware...{w=0.75}{nw}"
    extend 1nnmbo " as well as a bunch of tools and safety equipment."
    n 1nllpu "You know.{w=0.75}{nw}"
    extend 2ullaj " Goggles,{w=0.2} hammers,{w=0.5}{nw}"
    extend 2nllsm " that sort of thing."
    n 2tsqsm "And then...?"
    n 1fcssm "Ehehe."
    n 3fchbg "Come on,{w=0.2} [player]!{w=0.75}{nw}"
    extend 3fsqbg " What {i}else{/i} do you think it's all for?"
    n 3uchgnelg "...You get to beat the absolute {i}SNOT{/i} out of everything!"
    n 1unmbs "Seriously!{w=0.75}{nw}"
    extend 1fchbs " You just get to go wild!"
    n 2tsqbg "...And the best part?{w=1}{nw}"
    extend 1fchbg " You don't have to clean up afterwards either!{w=0.75}{nw}"
    extend 4fspgs " You can even take people {i}with{/i} you!"
    n 1fcsss "Man...{w=0.75}{nw}"
    extend 3fchgn " imagine {i}Yuri{/i} trying out something like that!"
    n 3nsrdvsbl "And Sayori..."
    n 4uwdbosbl "...There'd be no room {i}left{/i}!"
    n 1ullss "Of course,{w=0.5}{nw}"
    extend 1ullbo " they already supply a bunch of their own things you can smash up...{w=0.75}"
    n 1fchsm "But you can totally bring your own stuff too!{w=0.75}{nw}"
    extend 3nsrsmsbr " Well..."
    n 1nlrbo "So long as it's all safe to break up -{w=0.5}{nw}"
    extend 2nsrsssbl " no big batteries,{w=0.2} pressurized things,{w=0.2} or anything dumb like that."
    n 1fsqsm "Finally had enough of that garbage printer chewing up all your assignments?"
    n 1fcsbg "Nothing like some trial by combat to show who's on top!"
    n 4unmajesu "Oh!{w=0.5}{nw}"
    extend 1nnmbo " Don't get me wrong though."
    n 3nsrbgsbl "You still gotta pay regardless of if you brought your own junk,{w=0.75}{nw}"
    extend 3nsrposbl " of course...{w=1}{nw}"
    extend 3kslslsbl " and it really {i}isn't{/i} a way to deal with anger issues or anything like that."
    n 1fcssm "But I gotta say,{w=0.2} [player]."
    n 4fsqbg "If that doesn't sound like a {w=0.2}{i}smashing{/i}{w=0.2} way to relieve stress..."
    n 2uchgn "Then I don't know what is!{w=0.5}{nw}"
    extend 1fchsmeme " Ehehe."

    return

# Allows the player to ask Natsuki to take down any decorations in the room.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_take_down_deco",
            unlocked=True,
            prompt="Can you tidy away the decorations for me?",
            conditional="len(store.persistent._jn_holiday_deco_list_on_quit) > 0",
            category=["Holidays"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_take_down_deco:
    n 2tllpu "Just not feeling the celebrations today,{w=0.75}{nw}"
    extend 2tnmsl " [player]?"

    if len(jn_events.getHolidaysForDate()) == 0:
        n 2nslsssbl "I suppose they {i}have{/i} kinda overstayed their welcome..."
        n 2nslposbl "..."

    else:
        n 1ncsemesi "...{w=1}{nw}"

    n 1ulraj "Yeah,{w=0.5}{nw}"
    extend 1nlrbo " I can do that.{w=0.75}{nw}"
    extend 3nsrpo " I guess.{w=1}{nw}"
    extend 3fsqca " But you're cleaning it all up next time."
    n 1nllsl "Just give me a second here...{w=1}{nw}"
    show natsuki 1ncssl

    show black zorder 4 with Dissolve(0.5)
    $ jnPause(1)
    play audio chair_out
    $ jnPause(3)
    hide deco
    $ persistent._jn_holiday_deco_list_on_quit = []
    play audio clothing_ruffle
    $ jnPause(2)
    play audio drawer
    $ jnPause(3)
    play audio chair_in
    $ jnPause(1)
    show natsuki 1nlrbo at jn_center
    hide black with Dissolve(1.25)

    n 1ulraj "And I think that's everything!"

    return

# Natsuki adds her thoughts on vegetarianism/veganism.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_vegetarianism",
            unlocked=True,
            prompt="What do you think about vegetarianism?",
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            category=["Food", "Society"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_vegetarianism:
    $ already_discussed_vegetarianism = get_topic("talk_thoughts_on_vegetarianism").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_vegetarianism:
            n 2tnmpu "Huh?{w=0.5}{nw}"
            extend 2tnmsl " Vegetarianism?"
            n 1fcspu "...Wait."
            n 2tllboeqm "Didn't we talk about this before?"
            n 2tslbo "..."

        else:
            n 1tnmpu "Eh?{w=0.5}{nw}"
            extend 2tnmsleqm " Vegetarianism?"
            n 1tllaj "That's...{w=0.75}{nw}"
            extend 1ullss " definitely not a question I was expecting,{w=0.75}{nw}"
            extend 4tnmbo " I gotta say."
            n 1ulrpu "But...{w=0.75}{nw}"
            extend 2tsqss " why do you ask,{w=0.2} [player]?"
            n 2fsqsm "Looking to turn over a new leaf,{w=0.2} are we?{w=0.75}{nw}"
            extend 1fchsm " Ehehe."

        n 1ullss "Well,{w=0.2} anyway.{w=0.75}{nw}"
        extend 4tnmbo " In all seriousness?"
        n 1ulraj "I've never really thought about it that much,{w=0.5}{nw}"
        extend 2ulrbo " to be honest."
        n 2nsrss "We had vegetarian and vegan options at school,{w=0.75}{nw}"
        extend 2tnmbo " but I never really felt a particular drive to try them out or anything."
        n 4nslsssbr "And it's not like I can really try them {i}now{/i},{w=0.2} either."
        n 1unmeml "B-{w=0.2}but that's not to say they looked {i}bad{/i} or anything!"
        n 2fsldv "At least not to me."
        n 1fllss "Heck,{w=0.75}{nw}"
        extend 3fchgn " Monika shoveled that stuff down like there was no tomorrow!"
        n 1ulraj "Although...{w=1}{nw}"
        extend 3fcscaedz " I do think it's super admirable how people can put meat aside for so many reasons!{w=1}{nw}"
        extend 4uwdaj " Seriously!"
        n 1ullaj "I mean,{w=0.75}{nw}"
        extend 1nllsl " it's one thing to skip out on eating a particular type of meat.{w=0.75}{nw}"
        extend 2fcsss " Anyone can do that."
        n 1tnmpu "But dropping {i}everything{/i},{w=0.75}{nw}"
        extend 4unmem " or even refusing {i}any{/i} animal products whatsoever?"
        n 3fcsbg "Now {i}that{/i} takes some guts!{w=1.25}{nw}"
        extend 3fsldvsbl " ...Pun not intended."
        n 1ullaj "Of course,{w=0.5}{nw}"
        extend 2tllsl " maybe some people just don't like the taste.{w=0.75}{nw}"
        extend 2tnmbo " I totally get that.{w=1}{nw}"
        extend 1fnmaj " But there's a whole bunch of reasons people do it -{w=0.5}{nw}"
        extend 1fcsbg " and they're all just as valid!"
        n 3ulraj "Environmental concerns,{w=0.5}{nw}"
        extend 3nslun " animal welfare...{w=0.75}{nw}"
        extend 3kchbgsbr " even just to save money!"
        n 4tsqsssbr "Crazy to think how a single lifestyle choice can come from so many places,{w=0.2} huh?"
        n 1unmajesu "Oh -{w=0.5}{nw}"
        extend 2fllbgsbl " don't worry,{w=0.2} [player].{w=0.75}{nw}"
        extend 2nslpo " I'm not gonna get all preachy about it or anything like that."
        n 1unmca "It {i}is{/i} just a choice like anything else,{w=0.75}{nw}"
        extend 1nlrss " after all.{w=0.75}{nw}"
        extend 2nsrsssbl " And a personal one at that."
        n 4fwlbg "...As if that's gonna stop me suggesting it though!"
        n 2fsldv "Even if {i}I{/i} can't try it out myself right now..."
        n 1fsqsm "There's no excuse for you!{w=1}{nw}"
        extend 1fcsbg " Sorry,{w=0.2} [player]."
        n 3uchgn "'Fraid you aren't wriggling out of this one!"
        n 1fcsbg "So!"
        n 1ulraj "I don't know if you're practicing an animal-free diet already,{w=0.75}{nw}"
        extend 4fsqss " but if you aren't..."
        n 1fchbg "Why not give it a shot,{w=0.2} [player]?"
        n 1ullss "You don't need to go all out or anything -{w=0.5}{nw}"
        extend 3fchsm " you could swap out just a single meal a day and see how you're feeling!"
        n 4tlrss "Plus with all the recipes out there,{w=0.75}{nw}"
        extend 4tsqbg " the hard work is practically already done for you!{w=0.75}{nw}"
        extend 3fchsmeme " Easy peasy!"
        n 3tnmsm "And anyway,{w=0.75}{nw}"
        extend 1tllaj " even if it's only for a day or two,{w=0.2} and it doesn't work out:{w=0.5}{nw}"
        extend 4tsqsm " at least you can say you {i}tried{/i} it,{w=0.2} right?"
        n 4tslsm "Well,{w=0.2} at any rate -{w=0.5}{nw}"
        extend 1nslss " I've gone on long enough,{w=0.75}{nw}"
        extend 1fcsss " so I think that's about all I have to say on that topic."
        n 1fsqss "Besides,{w=0.2} [player]..."
        n 3fsqbg "Wouldn't want to turn you into a {i}vegetable{/i} now,{w=0.75}{nw}"
        extend 3tsqcs " would we?"
        n 3nchgnelg "Ehehe."

        if Natsuki.isLove(higher=True):
            n 4fchblleaf "Love you,{w=0.2} [player]~!"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_vegetarianism:
            n 1fcsemesi "..."
            n 2fslsl "Seriously,{w=0.75}{nw}"
            extend 2fsqsl " [player]?"
            n 2nsqsr "This {i}again{/i}?"

        else:
            n 1fcsem "...Really,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2fsqsr " {i}Vegetarianism{/i}?"
            n 2fcssl "..."

        n 1fcssl "..."
        n 1nsrsl "Whatever.{w=1}{nw}"
        extend 2fsrsr " It's not like I have much to say about it."
        n 1nnmbo "I never really practiced it or anything like that,{w=0.75}{nw}"
        extend 1nllsl " but I can at least respect the effort people make."
        n 2fcsaj "It takes some real guts to cut out so many options from your diet.{w=0.75}{nw}"
        extend 2flrca " Or even from your lifestyle completely."
        n 4nlrtr "People do it for a whole bunch of reasons,{w=0.75}{nw}"
        extend 4nsrsl " obviously."
        n 1nlrpu "But...{w=1}{nw}"
        extend 1nnmsl " I guess it's cool how a single lifestyle choice can link tons of people together."
        n 1ullsl "The environment,{w=0.5}{nw}"
        extend 2nslsf " animal welfare...{w=0.75}{nw}"
        extend 2ksrbo " even just fruits and veggies being cheaper to buy in bulk."
        n 1fcsca "It's all just as valid.{w=0.75}{nw}"
        extend 1ncssl " Just like the choice to start going animal-free or not."
        n 2ncsss "...Heh.{w=0.75}{nw}"
        extend 2fsqsl " And speaking of choices people make..."
        n 4fnmem "No prizes for guessing who should be making better ones right now,{w=0.75}{nw}"
        extend 1fsqan " {i}[player]{/i}."

    else:
        if already_discussed_vegetarianism:
            n 1fcsan "Oh,{w=0.75}{nw}"
            extend 2fsqupl " take a hike already,{w=0.2} [player]."
            n 2fsleml "I'm {i}still{/i} not giving you an answer.{w=0.75}{nw}"
            extend 1fsqful " A-{w=0.2}and why should I?"
            n 1fcsanltsa "{i}Anything{/i} I ever say to you is wrong,{w=0.75}{nw}"
            extend 2fcssrltsa " apparently."
            n 2fnmfultsc "Isn't that right?"

        else:
            n 1fsqeml "...Wow.{w=0.75}{nw}"
            extend 2fnmanltsc " And why should I even {i}bother{/i} answering,{w=0.2} [player]?"
            n 2fllunltsc "Knowing you?"
            n 1fcsfultsa "Whatever answer I give is gonna be the {i}wrong{/i} one anyway,{w=0.75}{nw}"
            extend 2fsqfultsb " isn't it?"
            n 2fcsupltsa "Jerk."

    return

# Natsuki shares her thoughts on motivation and how she manages hers.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_motivated",
            unlocked=True,
            prompt="Staying motivated",
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            category=["Life"],
            affinity_range=(jn_affinity.NORMAL, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_motivated:
    n 1kcsemesi "...{w=1.25}{nw}"
    n 2ksrem "Man..."
    n 2fsrsl "..."
    n 4flrfl "You know,{w=0.2} [player].{w=0.75}{nw}"
    extend 4fsqfl " If there's one thing I {i}really{/i} can't stand?"
    n 1fllem "It's when for whatever reason,{w=0.2} I just can't get motivated about anything.{w=1}{nw}"
    extend 1fcsgs " It's the worst!"
    n 4flrfl "Like...{w=0.75}{nw}"
    extend 2fsrsl " when nothing seems worth the effort,{w=0.75}{nw}"
    extend 2ksqsl " or you feel like you're just putting something off.{w=0.75}{nw}"
    extend 4knmajsbr " Even if you actually wanna do it!"
    n 3fnman "And then?{w=0.5}{nw}"
    extend 3fllfl " If you {i}don't{/i} snap out of it somehow?"
    n 1fcsan "You end up feeling all crappy about not getting something done!{w=0.75}{nw}"
    extend 1fbkwr " It {i}stinks{/i}!"
    n 2fcsem "Ugh.{w=1.25}{nw}"
    extend 2fslem " Feels like you just can't win sometimes."
    n 4unmfllsbl "...T-{w=0.2}that's not to say I feel like that often or anything!{w=0.75}{nw}"
    extend 3fcsemlsbl " N-{w=0.2}no way!{w=0.75}{nw}"
    extend 3fcsbgsbr " I've {i}always{/i} got things under control."
    n 1fcsss "Heh."
    n 4fsqss "...And you know why,{w=0.2} [player]?"
    n 4fsqcs "Yeah.{w=0.75}{nw}"
    extend 2fcsbg " I bet you do."
    n 2fchgn "'Cause I know just how to tell that kind of mood to stick it!"

    if get_topic("talk_time_management").shown_count > 0:
        n 1ullaj "I mean,{w=0.75}{nw}"
        extend 2tllbo " I think I mentioned timeboxing before.{w=0.75}{nw}"
        extend 2nslss " Having at least {i}some{/i} kind of structure to follow can help."
        n 1tnmaj "But personally?{w=0.75}{nw}"

    else:
        n 1tlraj "Personally?{w=0.75}{nw}"

    extend 1unmaj " I find most of the problem is just getting in the right mood -{w=0.5}{nw}"
    extend 4ulraj " and there's no shortage of ways to get there."
    n 3fchgn "Like music!"
    n 3fcsbg "Nothing beats my tried-and-true music playlists to kick me out of a rut!{w=0.75}{nw}"
    extend 3fcssmeme " A good tune or two {i}always{/i} gets me pumped."
    n 4fnmaj "But you need to do what works for {i}you{/i},{w=0.2} [player]!"

    if persistent.jn_player_tea_coffee_preference in ["tea", "coffee"]:
        n 1fsqss "Downing some [persistent.jn_player_tea_coffee_preference],{w=1}{nw}"

    else:
        n 1ullbo "Getting some caffeine in your system,{w=0.75}{nw}"

    extend 2ulraj " cracking open the windows for some fresh air,{w=0.75}{nw}"
    extend 2fcsbg " getting off your backside -{w=1}{nw}"
    extend 2fnmfl " whatever it is!"
    n 4fcsaj "It's all about getting that momentum going...{w=0.75}{nw}"
    extend 4fcsca " and then keeping it!"
    n 2nsqsr "Seriously.{w=0.5}{nw}"
    extend 2fsrem " The worst thing you can do is get all fired up and just drop whatever you're doing straightaway.{w=0.75}{nw}"
    extend 2fnmgs " You gotta commit!"
    n 1fsrca "And don't let yourself get distracted -{w=0.5}{nw}"
    extend 4fcscaesm " one thing at a time.{w=0.75}{nw}"
    extend 4fcssm " And finish what you start!"

    n 1fsqfl "But most importantly,{w=0.2} [player]?"
    n 1fcsfl "Just...{w=0.75}{nw}"
    extend 2nsrpo " don't be totally dumb about it.{w=1}{nw}"
    extend 2fnmbo " Forcing yourself into stuff,{w=0.2} I mean."
    n 4fcstr "Coming back with a fresh mindset is just as valid as trying to push past the block."
    n 4flrem "Like yeah,{w=0.75}{nw}"
    extend 3fsrsl " no kidding.{w=1}{nw}"
    extend 3nsqca " It sucks feeling like you're throwing time away."
    n 4tllfl "But it's not like you'll never get to try again,{w=0.75}{nw}"
    extend 4tnmbo " or get another time to do stuff!"
    n 2fcsaj "Coming back later is only a waste of time if you {i}convince{/i} yourself it is -{w=1}{nw}"
    extend 2fsqca " or you convince yourself that you'll never even start something."

    n 1nllaj "And hey.{w=1}{nw}"
    extend 4fsqss " You know what's {i}never{/i} a waste of time,{w=0.2} [player]?"

    if Natsuki.isLove(higher=True):
        n 3fchgnl "Spending more time with yours truly!"
        n 3fcsbgl "N-{w=0.2}now that's something I {i}know{/i} you of all people find motivating.{w=0.75}{nw}"
        extend 1fsqsml " Ehehe."
        n 4fchbgl "Love you too,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 3fcssmledzsbl "Spending more time with yours truly!"
        n 3fcsbglsbl "N-{w=0.2}now {i}that's{/i} something anyone should find motivating!{w=1}{nw}"
        extend 4fsrsmlsbl " Ehehe."

    else:
        n 3fchbgedz "Getting more pro tips from yours truly!"
        n 3fcsbg "You're welcome,{w=0.2} [player]~!{w=1}{nw}"
        extend 3fchsm " Ahaha."

    return

# Natsuki finds and introduces the joke book, unlocking daily jokes.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_unlock",
            unlocked=True,
            conditional="not persistent._jn_daily_jokes_unlocked",
            affinity_range=(jn_affinity.HAPPY, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_unlock:
    n 2nllsl "..."
    n 2fllsl "..."
    n 2fcsflesi "..."
    n 2nlrfl "You know,{w=0.2} [player].{w=0.75}{nw}"
    extend 1nnmsl " I just thought of something.{w=0.75}{nw}"
    extend 4fslfl " Something that's really starting to bug the crap out of me."
    n 2unmbo "You stop by here often enough,{w=0.2} right?{w=0.75}{nw}"
    extend 2nlraj " To visit,{w=0.2} I mean."
    n 4unmemeshsbl "N-{w=0.2}not that I don't appreciate it,{w=0.2} or anything like that!{w=0.75}{nw}"

    if Natsuki.isEnamored(higher=True):
        extend 4nslsllsbl " You should know I do by now.{w=1}{nw}"

    elif Natsuki.isAffectionate(higher=True):
        extend 2fcsajlsbl " I-{w=0.2}I totally do!{w=1}{nw}"
        
    else:
        extend 4fcsemsbl " O-{w=0.2}of course I do!"
        n 2fcspo "Even if you {i}do{/i} kinda owe it to me.{w=1}{nw}"

    extend 1nlrsl " But..."
    n 1fcsaj "It's just..."
    n 4fslun "..."
    n 4fcsansbl "Nnnnn...!"
    n 1fbkwrsbr "It just gets so {w=0.3}{i}boring{/i}!{w=1}{nw}"
    extend 1fcswr " Like nothing {i}ever{/i} changes around here!{w=1}{nw}"
    extend 2flrgs " It's always the same,{w=0.75}{nw}"
    extend 2fcsgs " and I'm sick of it!"
    n 1fslsl "Ugh..."
    n 4fcsemesi "..."
    n 2fcswr "What we need is variety!"
    n 2fcsgs "Something different!{w=0.75}{nw}"
    extend 4fcspo " And nothing different ever happened by just sitting around {i}waiting{/i} for it."
    n 3fllfl "There HAS to be something like that around here somewhere..."
    n 3fslbo "..."
    n 4nllaj "...Actually.{w=0.75}{nw}"
    extend 2unmfl " You know what?{w=1}{nw}"
    extend 2fcsca " Just give me a couple minutes."
    n 4flrpu "There's gotta be something in the closet I missed before."

    show natsuki 1fcsbo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio chair_out
    $ jnPause(4)

    n "Alright...{w=1}{nw}"
    extend " what have we got..."
    n "..."
    n "Oh,{w=0.2} for-!"
    n "Since when did this become the official school {i}dumping ground{/i}?!{w=1}{nw}"
    extend " Half this stuff wasn't even {i}ours{/i}!"

    play audio stationary_rustle_a
    $ jnPause(2.5)
    play audio gift_slide
    $ jnPause(3)

    n "Jeez...{w=1}{nw}"
    extend " what is this?{w=0.75}{nw}"
    extend " A library?"
    n "How much more of this stuff is there...?"

    play audio gift_slide
    $ jnPause(3)

    n "...Huh?{w=1.25}{nw}"
    extend " What's..."
    n "..."
    n "Wait...{w=1}{nw}"
    extend " i-{w=0.2}is that my homework?!{w=0.75} WHO-{w=0.5}{nw}"
    play audio gift_close
    n "Ack-!"
    n "..."
    n "Nnnnng...{w=1.5}{nw}"
    extend " m-{w=0.5}my head..."
    n "W-{w=0.2}who the hell just {b}balances{/b} books like that?!{w=0.75}{nw}"
    extend " I am {i}seriously{/i} gonna...!"
    n "..."
    n "..."
    n "...Wait a second.{w=1.5}{nw}"
    extend " Oh.{w=0.2} My.{w=0.2} Gosh."
    n "This...{w=1.25}{nw}"
    extend " is...{w=1.25}{nw}"
    extend " {b}PERFECT{/b}!"
    n "..."
    n "...!"

    $ jnPause(2)
    
    show natsuki 1fcssmeme
    play audio chair_in
    $ jnPause(1.5)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    n 4fchbg "[player]!{w=0.5} [player]!"
    n 4uchgneme "Guess what I fooound~?{w=0.75}{nw}"
    extend 4fsqsmeme " Ehehe."
    n 4fcsbs "It's...{w=1.5}{nw}"

    show natsuki 1uchgn
    show joke_book zorder JN_PROP_ZORDER
    play audio page_turn
    $ jnPause(3)

    extend 1uchgnedz " our old homeroom joke book!{w=0.75}{nw}"
    extend 1fchbgedz " Duh!"
    n 1fcsbg "And just when I was starting to wonder if this place had {i}any{/i} literature!"
    n 1fsrbgsbl "...Well...{w=0.75}{nw}"
    extend 1fsrposbl " any that {i}isn't{/i} just my own stuff,{w=0.2} anyway."
    n 1fsqsm "..."
    n 1tsqbosbl "..."
    n 1fnmflsbl "What?{w=0.75}{nw}"
    extend 1fcsposbl " Don't you start giving me that,{w=0.2} [player].{w=1}{nw}"
    extend 1fcsaj " Besides."
    n 1tsqbg "Did {i}you{/i} have anything better?"
    n 1tsqcs "..."
    n 1fcscsesm "..."
    n 1fcsbg "Yep!{w=0.75}{nw}"
    extend 1fcssm " That's about what I expected.{w=1}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsss "Man...{w=1}{nw}"
    extend 1fchbg " I can't wait to start cracking out some of these!{w=0.75}{nw}"
    extend 1uchgn " This is gonna be great,{w=0.2} I just know it!"
    n 1nchsmeme "..."
    n 1unmaj "Oh -{w=0.5}{nw}"
    extend 1nllaj " I should probably mention,{w=0.2} [player]."
    n 1nslca "I don't want to end up blowing through this thing too quickly.{w=0.75}{nw}"
    extend 1nsqslsbr " Or we'd just end up right back where we were.{w=1.25}{nw}"
    extend 1ulraj " So..."
    n 1fcsbg "I'm just gonna pick out something daily to torture you with.{w=0.75}{nw}"
    extend 1fchbg " No reason to overdo it."
    n 1fsqss "Sounds like a plan,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsss " Of course it does."
    n 1fcsgs "So!{w=0.5}{nw}" 
    extend 1fcsbg " You better start looking forward to it..."
    n 1fchgn "'Cause I {i}definitely{/i} am!{w=1}{nw}"
    extend 1nchgn " Ehehe."

    n 1fllsm "..."
    n 1fllbg "In fact...{w=1}{nw}"
    extend 1fsqbg " you know what,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsbg " Why wait?"
    n 1fsqsm "You know what they say,{w=0.2} after all.{w=1}{nw}"
    extend 1fchgn " No time like the present!"

    $ persistent._jn_daily_jokes_unlocked = True
    call talk_daily_joke(from_unlock=True)
    
    return

# Natsuki reads out a daily joke.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_joke",
            unlocked=True,
            prompt="Daily joke",
            conditional="persistent._jn_daily_jokes_unlocked and persistent._jn_daily_jokes_enabled and not persistent._jn_daily_joke_given",
            affinity_range=(jn_affinity.HAPPY, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_joke(from_unlock=False):
    if not from_unlock:
        $ dialogue_choice = random.randint(1, 6)
        if dialogue_choice == 1:
            n 1nchgn "Okaaay!{w=1}{nw}"
            extend 3fsqbg " I think we both know what it's time for now,{w=0.2} huh?{w=1.25}{nw}"
            extend 3fsqsm " Ehehe."

        elif dialogue_choice == 2:
            n 4fcsbg "Alright!{w=1}{nw}"
            extend 2tlrss " I think it's about time,{w=0.2} [player].{w=1.25}{nw}"
            extend 2tsqsm " Don't you?"

        elif dialogue_choice == 3:
            n 2fcsaj "Right!{w=1}{nw}"
            extend 2fcsbg " I think now's as good a time as any."
            n 4tlrbo "Now where did I leave that book..."

        elif dialogue_choice == 4:
            n 4tllbo "Hmmm..."
            n 4tnmaj "You know what,{w=0.2} [player]?{w=1}{nw}"
            extend 3fsqbg " I think it's about that time again."
            n 3fcssm "Ehehe."

        elif dialogue_choice == 5:
            n 2ulraj "You know,{w=0.2} [player]...{w=1}{nw}"
            extend 2flrcs " I think it's about that time.{w=1.25}{nw}"
            extend 4fsqcs " Don't you?"

        elif dialogue_choice == 6:
            n 1fcsbg "Alright!{w=1}{nw}"
            extend 4fwrbg " I think it's about time for the old joke book!{w=0.75}{nw}"
            extend 4fcssm " Ehehe."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        show joke_book zorder JN_PROP_ZORDER
        $ Natsuki.setIsReadingToRight(True)
        show natsuki reading
        hide black with Dissolve(0.5)
        $ jnPause(0.5)

    $ daily_jokes = jn_jokes.getUnseenJokes()

    if not daily_jokes:
        $ jn_jokes.resetJokes()
        n 1fcsemesi "..."
        n 1fsrpo "Man...{w=1}{nw}"
        extend 1tnmbo " we really {i}are{/i} going through these things,{w=0.2} huh?{w=1.25}{nw}"
        extend 1fcsflsbl " I'm gonna run out of jokes completely at this rate!"
        n 1nsrslsbr "..."
        n 1nsrajsbr "You...{w=1.25}{nw}"
        extend 1flrsssbr " don't mind if I just starting picking them out at random,{w=0.2} right?"
        n 1fcsgslsbr "D-{w=0.2}don't get me wrong!"
        extend 1fllflsbr " I'm still gonna at least {i}try{/i} and keep things fresh!{w=1}{nw}"
        extend 1fcsposbr " O-{w=0.2}obviously."
        n 1nsqpo "Just don't give me any funny looks if I pick one you've already heard.{w=1.25}{nw}"
        extend 1fsqpo " Capiche?"

        if Natsuki.isLove(higher=True):
            n 1fsqsm "Ehehe.{w=1}{nw}"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 1fchbll " Love you too,{w=0.2} [chosen_tease]!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fsqsm "Ehehe.{w=1}{nw}"
            extend 1uchgnl " 'ppreciated,{w=0.2} [player]!"

        $ daily_jokes = jn_jokes.getUnseenJokes()

    n 1fcsss "Now,{w=0.75}{nw}" 
    extend 1fsqsm " let's see..."

    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    $ jnPause(3)
    play audio page_turn
    $ jnPause(2)

    $ daily_joke = random.choice(daily_jokes)
    if daily_joke.joke_category == jn_jokes.JNJokeCategories.corny:
        $ dialogue_choice = random.randint(1, 4)
        if dialogue_choice == 1:
            n 1nsrflsbl "Oh,{w=0.2} jeez."

        elif dialogue_choice == 2:
            n 1ncsemesi "..."

        elif dialogue_choice == 3:
            n 1nslposbl "..."

        elif dialogue_choice == 4:
            n 1nsrem "...{i}Seriously{/i}?"
            n 1ncsemesi "..."

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.bad:
        $ dialogue_choice = random.randint(1, 3)
        if dialogue_choice == 1:
            n 1fcsemesi "..."

        elif dialogue_choice == 2:
            n 1fupem "Oh,{w=0.5} for-{w=1.25}{nw}"
            n 1fcssl "..."

        elif dialogue_choice == 3:
            n 1fsrem "Ugh..."

    else:
        $ dialogue_choice = random.randint(1, 6)
        if dialogue_choice == 1:
            n 1fcsss "Ah!{w=0.75}{nw}"
            extend 1fchgn " This'll do!"

        elif dialogue_choice == 2:
            n 1unmbs "Oh!{w=0.5} Oh!{w=0.75}{nw}"
            extend 1fcsbs " How about this?"

        elif dialogue_choice == 3:
            n 1fcsbg "Aha!{w=0.75}{nw}"
            extend 1fsqsm " Here we go!"

        elif dialogue_choice == 4:
            n 1fspgs "Hmm...{w=0.75}{nw}"
            extend 1fnmbg " how about this one,{w=0.2} [player]?"

        elif dialogue_choice == 5:
            n 1nchgn "Alright!{w=0.75}{nw}"
            extend 1fcsbg " Let's try {i}this one{/i} on for size!"

        elif dialogue_choice == 6:
            n 1unmbg "Oh!{w=0.75}{nw}"
            extend 1fchgn " I got one!{w=0.5} I got one!"

        n 1fcsaj "A-{w=0.2}hem!"
        n 1fcssm "..."

    call expression daily_joke.label

    $ daily_joke.setSeen(True)
    $ persistent._jn_daily_joke_given = True
    $ Natsuki.calculatedAffinityGain(bypass=True)
    $ dialogue_choice = random.randint(1, 3)
    
    if daily_joke.joke_category == jn_jokes.JNJokeCategories.funny:
        if dialogue_choice == 1:
            n 1uchgn "See?{w=1}{nw}"
            extend 1fchbg " I {i}told{/i} you this book had some good stuff!"
            n 1fwlbg "You're welcome,{w=0.2} [player]!"
            extend 1fchsmeme " Ehehe."

        elif dialogue_choice == 2:
            n 1fllbg "Man..."
            n 1fchgn "I am {w=0.2}{i}so{/i}{w=0.2} bookmarking that one.{w=1}{nw}"
            extend 1fchsmeme " Ehehe."
            n 1uchgn "'preciate you tuning in,{w=0.2} [player]!"

        else:
            n 1fchdvesm "Pfffft-!"
            n 1fchbg "Okay,{w=0.2} okay.{w=0.75}{nw}"
            extend 1flrbg " You gotta admit.{w=1}{nw}"
            extend 1fcsbg " That one {w=0.2}{i}was{/i}{w=0.2} pretty good."
            n 1fchbg "You bet you're getting another tomorrow,{w=0.2} [player]!"

        show natsuki 1fchsm

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.corny:
        if dialogue_choice == 1:
            n 1fsrem "...Yeesh."
            n 1fsrca "..."
            n 1fcsbgsbl "W-{w=0.2}well,{w=0.5}{nw}"
            extend 1fcstrsbl " I never said they'd be {w=0.2}{i}good{/i}{w=0.2} jokes!"
            n 1fchgn "Sorry,{w=0.2} [player]~!"

        elif dialogue_choice == 2:
            n 1nsqsr "..."
            n 1nslaj "I'm...{w=1.25}{nw}"
            extend 1nllss " starting to realize {i}why{/i} we never saw this book very often."
            n 1ullss "Well -{w=0.3}{nw}"
            extend 1fwlbg " Better luck next time,{w=0.2} [player]!"
            n 1fchsm "Ahaha."

        else:
            n 1nlrfl "...Wow.{w=1.25}{nw}"
            extend 1fsqpo " I'm actually starting to think that the book itself is the joke at this point."
            n 1nslpo "..."
            n 1nllaj "Well,{w=0.5}{nw}"
            extend 1fcsfl " I'm still not going back on what I said.{w=1}{nw}"
            extend 1fchgn " Sorry [player]."
            n 1fsqbg "But that's all you're getting for today!"

        show natsuki 1fchsm

    elif daily_joke.joke_category == jn_jokes.JNJokeCategories.bad:
        if dialogue_choice == 1:
            n 1fcsfl "...Okay,{w=1.25}{nw}"
            extend 1fbkwr " who the hell approved {i}that{/i} one?{w=0.75}{nw}"
            extend 1fcsgs " Jeez!"
            n 1fslpo "I can't believe someone {i}actually{/i} paid money for this.{w=1.25}{nw}"
            extend 1fcsaj " Whatever."
            n 1fsrfl "The next one better be good.{w=1}{nw}"
            extend 1fcspoesi " That's all {i}I've{/i} got to say."

        elif dialogue_choice == 2:
            n 1fcsemesi "..."
            n 1fsqwr "Really?{w=1.25}{nw}"
            extend 1fllfl " Is {i}one{/i} good joke so much to ask for?{w=1}{nw}"
            extend 1fcsfl " Come {w=0.2}{i}on{/i}."
            n 1flrfl "I'm done with this thing."
            n 1fsrem "{i}'Award winning'{/i},{w=1}{nw}"
            extend 1fcsfl " my {i}butt{/i}."

        else:
            n 1fcssl "..."
            n 1fcsan "Uuuuuu-!"
            n 1fbkwr "Why do so many of these just {w=0.2}{i}stink{/i}{w=0.2}?!{w=1.25}{nw}"
            extend 1fcswrl " Seriously!"
            n 1fcsgssbr "The only joke here is how much these writers were paid!"
            n 1fsrslesi "..."
            n 1fsqtr "You know what?{w=1}{nw}"
            extend 1fcsca " I think that's more than enough for today."

        show natsuki 1fcspo

    else:
        if dialogue_choice == 1:
            n 1fcsbg "Thanks for listening~!{w=0.75}{nw}"
            extend 1fchsm " Ehehe."

        elif dialogue_choice == 2:
            if Natsuki.isLove(higher=True):
                n 1fwlsml "Love you too,{w=0.2} [player]!{w=0.75}{nw}"
                extend 1fchsml " Ehehe."

            else:
                n 1fchgn "You're welcome,{w=0.2} [player]!"

        else:
            n 1fsqbg "Same time tomorrow,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1nchgn " Ehehe."

        show natsuki 1fchsm

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1.5)
    play audio drawer
    hide joke_book
    show natsuki 1fchsmeme
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    return

# Natsuki is asked to start telling daily jokes again.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_start",
            unlocked=True,
            prompt="Can you start telling me daily jokes?",
            category=["Jokes"],
            conditional="persistent._jn_daily_jokes_unlocked and not persistent._jn_daily_jokes_enabled",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_start:
    n 2usqss "Oho?{w=1}{nw}"
    extend 4nlrbg " What's this now,{w=0.75}{nw}"
    extend 4tsqbg " all of a sudden?"
    n 2fcsbg "Seems you really {w=0.2}{i}can't{/i}{w=0.2} get enough of my amazing joke delivery after all!"
    n 2fsqsmeme "Ehehe."
    n 1fcsss "Well in that case,{w=1}{nw}"
    extend 4fnmss " you better prepare yourself,{w=0.2} [player]."
    n 3fchgn "'Cause I'm gonna pick out all the {i}extra{/i} corny ones now.{w=1}{nw}" 
    extend 3nchgn " Juuuust for you~!"

    if Natsuki.isLove(higher=True):
        n 3fchbll "Love you,{w=0.2} [player]!"

    $ persistent._jn_daily_jokes_enabled = True

    return

# Natsuki is asked to stop telling daily jokes.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_stop",
            unlocked=True,
            prompt="Can you stop telling me daily jokes?",
            category=["Jokes"],
            conditional="persistent._jn_daily_jokes_unlocked and persistent._jn_daily_jokes_enabled",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_stop:
    n 1unmem "H-{w=0.3}huh?{w=1}{nw}"
    extend 4fcseml " Wait,{w=0.5}{nw}" 
    extend 4fnmeml " what?"
    n 1fcswr "A-{w=0.2}and just what is {i}that{/i} meant to mean,{w=0.2} [player]?!"
    extend 3fnmfl " Huh?"
    n 3fnmgs "You got some kind of problem with the book?"
    n 4fsqwr "You think my delivery just stinks?{w=1}{nw}"
    extend 4fbkwr " Is that it?!"
    n 2fcspo "..."
    n 2fsqcs "..."
    n 2fchdvesm "Pfffft-!{w=1}{nw}"
    extend 1fchbs " Relax,{w=0.2} [player]!{w=0.75}{nw}"
    extend 4fchgn " Relax!{w=0.75}{nw}"
    extend 3klrbg " Man..."
    n 3fnmbg "You {i}really{/i} gotta see the look on your face sometimes.{w=1}{nw}"
    extend 3uchgn " Priceless!"
    n 4ullaj "Nah,{w=0.2} it's fine.{w=1}{nw}"
    extend 4nllbo " I guess."
    n 1nsrpo "It's not like they're the {i}best{/i} jokes anyway.{w=1}{nw}"
    extend 1nlrfl " You know.{w=1}{nw}"
    extend 2nsrsslsbr " Not being {i}mine{/i} and all,{w=0.2} o-{w=0.2}of course."
    n 4nlraj "So...{w=1}{nw}"
    extend 4tnmca " just let me know whenever you get bored or something,{w=0.2} I suppose."
    extend 4fcstr " Besides."
    n 4fchgn "...Not like I'm ever gonna pass up a chance to make you squirm!{w=1}{nw}"
    extend 4fcssm " Ahaha."

    if Natsuki.isLove(higher=True):
        n 3fchtsl "Love you too,{w=0.2} [player]~!"

    $ persistent._jn_daily_jokes_enabled = False

    return

# Ask Natsuki to let the player see a previously seen joke.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_daily_jokes_seen_before_start",
            unlocked=True,
            prompt="What jokes have you told me before?",
            category=["Jokes"],
            conditional="persistent._jn_daily_jokes_unlocked and jn_jokes.getShownBeforeJokes() is not None",
            affinity_range=(jn_affinity.HAPPY, None),
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_daily_jokes_seen_before_start:
    if persistent._jn_daily_jokes_enabled:
        n 4ccsss "Oh?{w=0.75}{nw}"
        extend 4ccsbg " What's this now,{w=0.2} all of a sudden?{w=0.75}{nw}"
        extend 3fsqbg " {i}Someone{/i} just can't get enough of the joke book,{w=0.2} huh?"
        n 3fcssm "Ehehe."
        n 4ullaj "Well...{w=1}{nw}"
        extend 5cllss " I didn't exactly take notes or anything on the ones I've told you...\n{w=0.75}{nw}"
        extend 2fcssssbr " but I'm pretty sure I can figure it out!"
        n 4unmaj "Just give me a sec here..."

    else:
        n 1csqss "Oh?{w=0.75}{nw}"
        extend 4fnmss " Am I hearing this right?"
        n 4fsqbg "{i}Now{/i} you suddenly wanna hear all about the jokes?{w=0.75}{nw}"
        extend 3fcsbg " The ones you practically {i}begged{/i} me to stop telling you?"
        n 3tsqss "...{i}Those{/i} jokes?"
        n 4fsqsm "..."
        n 4fcssm "Ehehe."
        n 2fcsbs "Say no more,{w=0.2} say no more.{w=0.75}{nw}"
        extend 2fchgn " [n_name] has got you covered!"
        n 4ccsss "Just give me a sec here..."

    show natsuki 4fcssmeme
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_joke_book_held"))
    show natsuki 1fchsmeme
    $ jnPause(2.25)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    if random.choice([True, False]):
        n 1fchbgeme "Alright!{w=0.75}{nw}"
        extend 1fcsbg " Talk to me,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1tnmss " What did you wanna hear again?"

    else:
        n 1fchbgeme "Okaaay!{w=0.75}{nw}"
        extend 1fchgn " Here we go,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1tsqsm " Which one did you wanna hear?"

    call talk_daily_jokes_seen_before_loop

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 1nchsmeme
    $ jnPause(2.25)
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    return

label talk_daily_jokes_seen_before_loop:
    python:
        joke_options = []
        for joke in jn_jokes.getShownBeforeJokes():
            joke_options.append((joke.display_name, joke))

        joke_options.sort(key = lambda option: option[0])

    show natsuki option_wait_holding at jn_left
    call screen scrollable_choice_menu(
        joke_options,
        ("Nevermind.", None),
        400,
        "mod_assets/icons/joke_book.png")
    show natsuki at jn_center
    $ joke_choice = _return

    if isinstance(joke_choice, jn_jokes.JNJoke):
        $ dialogue_choice = random.randint(1, 3)
        if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
            if dialogue_choice == 1:
                n 1unmaj "Ooh!{w=0.75}{nw}"
                extend 1unmbg " Yeah!{w=0.5}{nw}"
                extend 1fchbg " I love that one!"

            elif dialogue_choice == 2:
                n 1tsqss "[joke_choice.display_name],{w=0.2} huh?"
                n 1fchsm "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " You got it,{w=0.2} [player]!"
            
            else:
                n 1uspbg "Oh!{w=0.2} Oh!{w=0.5}{nw}"
                extend 1uchgn " I love that one!"

            show natsuki 1udwsm

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny:
            if dialogue_choice == 1:
                n 1csqfl "...Seriously?{w=0.75}{nw}"
                extend 1fllfl " But it wasn't even {i}that{/i} good,{w=0.2} [player]!"
                n 1ccsemesi "..."

            elif dialogue_choice == 2:
                n 1csrem "Man...{w=1}{nw}"
                extend 1tnmem " you're {i}sure{/i} you wanna hear that one again?{w=0.75}{nw}"
                extend 1nslsl " Fine."
            
            else:
                n 1nsqflsbr "...That one {i}again{/i}?{w=0.75}{nw}"
                extend 1cslemsbr " Jeez..."

            show natsuki 1ndwbo

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
            if dialogue_choice == 1:
                n 1fcsan "Oh,{w=0.2} for-{w=0.5}{nw}"
                n 1ccsemesi "..."
                n 1csrtr "You just {i}had{/i} to pick out that one,{w=0.5}{nw}"
                extend 1csqca " huh?"
                n 1cslaj "...Fine.{w=0.75}{nw}"
                extend 1ccsaj " Whatever."

            elif dialogue_choice == 2:
                n 1ccsemesi "..."
                n 1clrfl "Really,{w=0.2} [player]?{w=0.75}{nw}"
                extend 1csqfl " {i}That{/i} one?"
                n 1nslposbr "...Fine."
            
            else:
                n 1fupfl "Ugh...{w=1}{nw}"
                extend 1cnmfl " for real?"
                n 1clraj "You {i}can't{/i} be serious,{w=0.2} [player].{w=0.75}{nw}"
                extend 1csqemsbr " [joke_choice.display_name]?"
                n 1ccsslesisbr "..."

            show natsuki 1cdwca

        else:
            if dialogue_choice == 1:
                n 1unmaj "[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1fchbg " Sure!"

            elif dialogue_choice == 2:
                n 1tnmss "[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1fcssm " You got it!"
            
            else:
                n 1udwaj "[joke_choice.display_name]?{w=0.75}{nw}"
                extend 1unmbo " That one?"
                n 1nchbg "'Kay!{w=0.75}{nw}"
                extend 1fcsbg " Here we go!"

            show natsuki 1cdwsm

        play audio page_turn

        if random.choice([True, False]):
            $ jnPause(1.25)
            play audio page_turn

        $ jnPause(1.25)

        n 1fcsaj "A-{w=0.2}hem!"
        n 1fcsbo "..."

        call expression joke_choice.label

        $ dialogue_choice = random.randint(1, 3)
        if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
            if dialogue_choice == 1:
                n 1flrss "Man...{w=1}{nw}"
                extend 1fchgn " I swear that one never gets old!{w=0.75}{nw}"
                extend 1nchgnl " Ahaha."
            
            elif dialogue_choice == 2:
                n 1fcssm "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " Yep!"
                n 1fchbsl "Now that's what I call [n_name] approved!"

            else:
                n 1fcssmeme "Ehehe.{w=0.75}{nw}"
                extend 1ulrss " Well,{w=0.2} what can I say?"
                n 1fwlbgl "Gotta love it,{w=0.2} [player]!"

            n 1ullss "Anyway..."
            show natsuki 1tnmss

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny:
            if dialogue_choice == 1:
                n 1nsrfl "...Yeah."
                n 1fcsaj "I gotta say.{w=0.75}{nw}"
                extend 1cllbo " I wouldn't complain if {i}that{/i} one never showed up again.{w=0.75}{nw}"
                extend 1ccsbosbr "\nJust saying."

            elif dialogue_choice == 2:
                n 1ccsflesi "..."
                n 1csraj "I seriously can't believe someone {i}paid{/i} for this.{w=0.75}{nw}"
                extend 1fcsfl " Ugh."
                n 1cllsl "Whatever."

            else:
                n 1csrfl "I...{w=1}{nw}"
                extend 1ccsfl " think that one should have {i}stayed{/i} in the book,{w=0.5}{nw}"
                extend 1csqcasbl " [player]."
                n 1csrcasbl "..."

            n 1nlraj "So..."
            show natsuki 1tnmbo

        elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
            if dialogue_choice == 1:
                n 1ccsemesi "..."
                n 1clrfl "Alright.{w=0.75}{nw}"
                extend 1clrca " That's that one dealt with.{w=0.75}{nw}"
                extend 1csrca " {i}Again{/i}."

            elif dialogue_choice == 2:
                n 1ccsflesi "..."
                n 1cllfl "Yeah.{w=0.75}{nw}"
                extend 1cllsl " That aged about as well as I expected.{w=1}{nw}"
                extend 1cslpo " {i}Like trash{/i}."
            
            else:
                n 1ccssssbl "Heh.{w=0.75}{nw}"
                extend 1ccstr " I suppose at least {i}some{/i} things don't change.{w=0.75}{nw}"
                extend 1csrbo " {i}Like that joke still sucking{/i}."

            n 1ccsajsbl "Well,{w=0.2} whatever.{w=0.75}{nw}"
            extend 1nllaj " So..."
            show natsuki 1tnmsl

        else:
            if dialogue_choice == 1:
                n 1fcssmeme "Ehehe.{w=0.75}{nw}"
                extend 1fchbg " There you go,{w=0.2} [player]!"
            
            elif dialogue_choice == 2:
                n 1fnmbg "...And there you go,{w=0.2} [player]!{w=0.75}{nw}"
                extend 1fcssmesm " Better appreciate it!"

            else:
                n 1fwrsm "...And that's all she wrote!{w=0.75}{nw}"
                extend 1fchsm " Ehehe."

            n 1ulraj "So..."
            show natsuki  1unmbo

        menu:
            n "Did you wanna pick out another one [player],{w=0.2} or...?"

            "Sure!":
                if joke_choice.joke_category == jn_jokes.JNJokeCategories.corny or joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
                    n 1nlrsl "...Alright.{w=0.75}{nw}"
                    extend 1csrsssbl " Just try and pick out a good one this time."

                else:
                    n 1nchbg "Gotcha!{w=0.75}{nw}"
                    extend 1tnmss " What else did you wanna hear again?"

                jump talk_daily_jokes_seen_before_loop

            "That's it for now.":
                if joke_choice.joke_category == jn_jokes.JNJokeCategories.funny:
                    n 1fcsss "Oh?{w=0.75}{nw}"
                    extend 1fsqss " What's wrong,{w=0.2} [player]?{w=0.75}{nw}"
                    extend 1fnmsm " Had enough {i}already{/i}?"
                    n 1fcssm "Ehehe."
                    n 1fcsbg "Fine,{w=0.2} fine.{w=0.75}{nw}"
                    extend 1flrsm " I'll put it away..."
                    n 1fsqcs "...Now that we've had enough{w=0.5}{nw}" 
                    extend 1fnmss " {i}pun{/i}{w=0.5}{nw}"
                    extend 1fsqbg " and all."
                    n 1nchgn "Ahaha.{w=0.75}{nw}"

                    if Natsuki.isLove(higher=True):
                        extend 1fchbll " Love you too,{w=0.2} [player]~!"
                    
                    else:
                        extend 1fcsbs " No regrets,{w=0.2} [player]!"

                    show natsuki 1fchsmeme

                elif joke_choice.joke_category == jn_jokes.JNJokeCategories.corny:
                    n 1ncsss "Heh.{w=0.75}{nw}"
                    extend 1ulrfl " Well...{w=1}{nw}"
                    extend 1nslsssbl " can't say I blame you,{w=0.2} [player]."
                    n 1nllsssbr "I'll just...{w=0.75}{nw}"
                    extend 1nslbosbr " put this away."

                    show natsuki 1nlrbosbl

                elif joke_choice.joke_category == jn_jokes.JNJokeCategories.bad:
                    n 1nslfl "...Yeah.{w=0.75}{nw}"
                    extend 1ccsfl " Actually,{w=0.2} you know what?{w=0.75}{nw}"
                    extend 1cnmaj " Good call."
                    n 1ccsposbr "I've about had enough of this anyway."

                    show natsuki 1nsrposbr

                else:
                    n 1unmaj "About done here,{w=0.2} [player]?{w=0.75}{nw}"
                    extend 1nchsm " No worries!"
                    n 1clrss "We'll just...{w=1}{nw}"
                    extend 1csqss " {i}close the book{/i}{w=0.5}{nw}"
                    extend 1csqbg " on this one."

                    if Natsuki.isLove(higher=True):
                        n 1fchgn "Ehehe.{w=0.75}{nw}"
                        extend 1fchblleme " Love you too,{w=0.2} [player]~!"
                    
                    else:
                        n 1fchgnelg "You're welcome,{w=0.2} [player]!"

                    show natsuki 1fchsmeme

    else:
        n 1tlraj "Well...{w=1}{nw}"
        extend 1tnmbo " if you say so,{w=0.2} [player]."
        n 1tllss "I'll just...{w=1}{nw}"
        extend 1cslss " put this thing back."

        show natsuki 1nslbo

    return

# Natsuki expresses her annoyance at clothing not always being made with all sizes in mind.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fitting_clothing",
            unlocked=True,
            prompt="Clothing problems",
            category=["Fashion"],
            conditional="persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fitting_clothing:
    n 2cllbo "..."
    n 2cllfl "You know,{w=0.2} [player]..."
    n 2tnmbo "I don't remember ever complaining about my height that much.{w=0.75}{nw}"
    extend 4nsrss "\nNot {i}really{/i}."
    n 4ulraj "I mean...{w=1}{nw}"
    extend 3clrsl " it always seemed pointless getting all worked up about it.{w=0.75}{nw}"
    extend 3nsrposbr " It's not like I was ever going to be tall {i}eventually{/i}."
    n 4csrca "...Especially not now."
    n 1ulraj "But...{w=1}{nw}" 
    extend 1unmaj " I guess I just came to realize it's like my teeth,{w=0.75}{nw}"
    extend 2nnmbo " or my hair or whatever."
    n 2fcstr "You just gotta make the most of it.{w=1}{nw}"
    extend 4fcsgsl " A-{w=0.2}and why shouldn't I?{w=0.75}{nw}"
    extend 3fcsbgl " I'm totally rocking what I've got!"

    n 1csqsl "But {w=0.3}Oh.{w=0.75} My.{w=0.75} God,{w=0.75}{nw}"
    extend 2csrem " [player]."
    n 2fsqem "Clothes shopping.{w=1}{nw}"
    extend 1fcsan " I swear.{w=1}{nw}"
    extend 4fbkwr " It's like my own special hell!"
    n 4fcswrl "Have you even {i}considered{/i} what getting new clothes is like when you're this small?!"
    n 2fllfll "Seriously -{w=0.5}{nw}"
    extend 2fbkwrl " it's the worst!{w=1}{nw}"
    extend 2fcsgs " And it doesn't even matter where you go!"
    n 4ftlfl "Medium?{w=0.5}{nw}"
    extend 4ftrfl " Small?{w=0.5}{nw}"
    extend 2fsqem " {i}Extra{/i} Small?{w=0.75}{nw}"
    extend 2fcsgs " As if it matters!"
    n 1fslem "Those aren't sizes -{w=0.5}{nw}"
    extend 4fcsan " I'm just picking how much of a {b}joke{/b} the fit is!"
    n 1flrfl "Yeah,{w=0.2} sure.{w=0.75}{nw}"
    extend 4flrca " I {i}know{/i} oversize is a thing.{w=1}{nw}"
    extend 2fsrtr " Obviously."
    n 2flrgs "But come {w=0.3}{nw}" 
    extend 2fcsgs "{b}on{/b}!"
    n 4ksqfl "Is it {i}really{/i} too much to want sleeves that {i}don't{/i} dangle off my arms too?"
    n 1fllfl "I mean,{w=0.2} half the time I walked over to check out the adult's clothes,{w=0.75}{nw}"
    extend 1fnmem " I'd have to walk right back out again!"
    n 2fsrsl "...And there's only so many times you can try the kids section before people start giving you stupid looks."
    
    n 2fcsemesi "Ugh..."
    n 1cslbo "It's just embarrassing.{w=1}{nw}"
    extend 4fslsl " And usually a {i}complete{/i} waste of time too."
    n 4cllfl "I get that some places do a...{w=0.75}{nw}"
    extend 1cslflsbr " {i}petite{/i}{w=0.75}{nw}"
    extend 1cslcasbr " line,{w=0.75}{nw}"
    extend 2fcswrsbr " but it's all still {i}just{/i} as expensive as the normal stuff!"
    n 2fcsem "Yeesh..."
    n 4fllem "They don't even use as much material.{w=1}{nw}"
    extend 4ftlem " They could at least throw in a discount or something."
    n 2fsrfl " ...{i}Jerks{/i}."
    n 2nsrpo "..."
    n 2ncstr "Well,{w=0.2} whatever.{w=0.75}{nw}"
    extend 1fnmca " Stores might be short of options.{w=0.75}{nw}"
    extend 1fsrca " And {i}courtesy{/i}."
    n 3fcsaj "But I can assure you:{w=0.5}{nw}" 
    extend 3fcsbg " my imagination {i}never{/i} comes up short!"

    $ pastel_goth_getup = jn_outfits.getOutfit("jn_pastel_goth_getup")
    if not pastel_goth_getup.unlocked:
        python:
            import copy

            pastel_goth_getup.unlock()
            topic_outfit = copy.copy(pastel_goth_getup)
            topic_outfit.hairstyle = jn_outfits.getOutfit(Natsuki.getOutfitName()).hairstyle

        n 3fllpu "..."
        n 3fllss "...In fact.{w=1}{nw}"
        extend 4fsqss " You know what?"
        n 2fcsbg "Forget just rambling on about it.{w=0.75}{nw}"
        extend 2fcssm " You should know I'm way better than that by now."
        n 4fchgn "...So I'm gonna {i}prove{/i} it!"
        n 3fcsbgsbl "Y-{w=0.2}you better sit tight,{w=0.2} [player]..."
        n 3fchgn "'Cause I'm gonna show you what {i}real{/i} craftsmanship looks like!{w=0.75}{nw}"
        extend 3nchgn " Ehehe."
        show natsuki 1fcssmeme

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        play audio chair_out
        $ jnPause(3)

        n  "Alright...{w=1}{nw}"
        extend  " now where did I...?"
        n  "Aha!"

        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(1)

        if Natsuki.isLove(higher=True):
            n "N-{w=0.2}no peeking!{w=0.75} Ehehe..."

        elif Natsuki.isEnamored(higher=True):
            n "N-{w=0.2}no peeking!"

        else:
            n "H-{w=0.2}hey!{w=0.75} You better not be peeking!"

        $ jnPause(1)
        play audio zipper
        $ Natsuki.setOutfit(outfit=topic_outfit, persist=False)

        show natsuki 2fsrdvlsbl
        $ jnPause(2)
        n "And..."
        play audio chair_in
        $ jnPause(0.25)
        hide black with Dissolve(1.5)
        $ jnPause(1.5)

        n 2fchbglsbl "Ta-da!"
        n 2csqsm "Can you guess where {i}this{/i} came from,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fcssm " Ehehe."
        n 4fslss "As much as I complained about resorting to the kids section..."

    else:
        n 4ullaj "I'm pretty sure I showed my handiwork off already,{w=0.75}{nw}"
        extend 1fcsbg " so I'll spare you the fashion show,{w=0.2} [player]."
        n 3fsqsm "...This time."
        n 3tnmss "Like I said before though -{w=0.5}{nw}"
        extend 4fslss " as much as I complained about resorting to the kids section..."

    n 3fcsbg "There's nothing some good old fashioned know-how,{w=0.2} a needle,{w=0.75}{nw}"
    extend 3fchgn " and a bunch of my patches can't fix!{w=1}{nw}"
    extend 3nchgn " Ahaha."
    
    n 4clrss "Well,{w=0.2} anyway.{w=0.75}{nw}"
    extend 2csrsmsbl " I think I've just about gone on long enough.{w=1}{nw}"
    extend 2fcsajsbl " As good as it was getting all that off my chest."
    n 1fcsss "Heh.{w=0.75}{nw}"
    extend 4cslbg " Besides,{w=0.2} all this talk about stuff never being the right size?"
    n 4fnmss "I guess you could say moving on is only...{w=1}{nw}"
    extend 3fsqbg " {i}fitting{/i}{w=1}{nw}"
    extend 3fchgn ",{w=0.2} right?"

    if Natsuki.isLove(higher=True):
        n 3fchsm "Ehehe.{w=0.5}{nw}"
        extend 3fchbll " Love you too,{w=0.2} [player]!"

    else:
        n 3fchsm "Ehehe.{w=0.5}{nw}"
        extend 3uchgn " No regrets,{w=0.2} [player]!"

    return

# Natsuki discusses her favourite - and least favourite - subjects.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favorite_subject",
            unlocked=True,
            prompt="What's your favorite subject?",
            category=["Education"],
            conditional="jn_utils.get_total_gameplay_hours() >= 2",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favorite_subject:
    $ already_discussed_topic = get_topic("talk_favorite_subject").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_topic:
            n 2ccsbo "...Wait.{w=0.75}{nw}"
            extend 2tnmpu " Didn't we go through this already,{w=0.2} [player]?{w=1}{nw}"
            extend 2clrbo " Huh."
            n 1clraj "Well,{w=0.2} whatever.{w=0.75}{nw}" 
            extend 4tllaj " It's not like much has changed.{w=1}{nw}"
            extend 2cslem " I {i}still{/i} can't stick math!"
        
        else:
            n 2cslem "Not {i}math{/i},{w=0.5}{nw}"
            extend 2fsrfl " I'll tell you that much."
            n 1nsrsl "..."
            n 1cllslsbr "..."
            n 4cnmflsbr "...What?{w=0.75}{nw}"
            extend 4fllgs " I'm being serious!{w=0.75}{nw}"
            extend 2fbkwr " I just can't stand it!"

        n 2fcsgs "I mean,{w=0.2} I totally get all the normal stuff.{w=0.75}{nw}"
        extend 4flrfl " Addition,{w=0.2} subtraction,{w=0.2} fractions.{w=0.5}{nw}"
        extend 1fcsca " That's child's play.{w=0.75}{nw}"
        extend 2clrca " I don't really care about {i}that{/i}."
        n 1fcsfl "It's just..."
        n 4fsrun "..."
        n 4fcswr "It's when you get all those {i}stupid{/i} rules you have to remember!{w=0.75}{nw}"
        extend 2fbkwr " There's just way too many of them!"
        n 2fllwr "Like...{w=1}{nw}"
        extend 2fcsgs " how am {i}I{/i} meant to remember three different flavors of mumbo-jumbo for calculating some random part of a triangle?"
        n 2flran "What am I even gonna {i}do{/i} with that?{w=0.75}{nw}"
        extend 1fsrwr " Measure out the perfect pizza slice?!{w=0.75}{nw}"
        extend 2fcsem " Come on."
        n 4fcsan "And don't even get me {i}started{/i} on calculus...{w=1}{nw}"
        extend 2fslsl " or {i}algebra{/i}."
        n 2fsqem "And I {i}really{/i} hated having to spend my nights cramming the crap out of it before{w=0.25}{nw}"
        extend 2fcsan " every{w=0.3} single{w=0.3}{nw}" 
        extend 2fsran " exam."
        n 4fcsan "It's..."
        n 1csrsl "..."
        n 1ccsflsbr "...Just not how my brain works.{w=0.75}{nw}"
        extend 4cslbolsbr " At all."
        n 4fcsgslsbr "B-{w=0.2}but that's not to say nobody would help or anything like that!{w=0.75}{nw}"
        extend 2fllflsbr " Monika always kept trying to offer when she had the time.{w=0.75}{nw}"
        extend 2cllbo " But..."
        n 1kllbo "..."

        if Natsuki.isAffectionate(higher=True):
            n 2csrbolsbr "...It's just embarassing.{w=0.75}{nw}"
            extend 2knmbolsbr " You know?{w=0.75}{nw}"
            extend 4fcsfl " And as much as I can't stand the subject..."
            n 1cslbol "...It's not like I {i}don't{/i} wanna be good at it too."

            if Natsuki.isEnamored(higher=True):
                n 1cslcal "E-{w=0.2}even if it's just so I can {i}say{/i} I can do it."
                n 4cslunl "..."
            
            else:
                n 1fcstrlsbr "Just like everything else."
                n 4cllsllsbr "..."

            n 2ccsfllsbr "A-{w=0.2}anyway!{w=0.75}{nw}"
            extend 4fcspo " We're getting off track here."
            n 4tllpu "Favorite subject,{w=0.5}{nw}" 
            extend 3tnmss " huh?"
            n 3csqsm "Ehehe.{w=0.75}{nw}"
            extend 4fsqbg " You really need to ask?{w=0.75}{nw}"

            if already_discussed_topic:
                extend 2fcsbg " You hadn't {i}already{/i} guessed,{w=0.2} [player]?"

            else:
                extend 2fcsbg " You seriously don't remember,{w=0.2} [player]?"

        else:
            n 1ccsfllsbl "...Forget it.{w=0.75}{nw}"
            extend 2csrcalsbl " It doesn't matter."
            n 2fcsajlsbl "A-{w=0.2}and besides.{w=0.75}{nw}"
            extend 2fcspo " This was already getting way off track."
            n 4unmaj "Favorite subject,{w=0.5}{nw}"
            extend 4tnmbo " huh?"
            n 2ccsss "Heh.{w=1}{nw}"
            
            if already_discussed_topic:
                extend 2fcsbg " You really don't remember,{w=0.2} [player]?"

            else:
                extend 2fcsbg " As if the answer hadn't already practically slapped you in the face."
        
        n 4uchgn "...Literature,{w=0.75}{nw}"
        extend 3fchgn " duh!"
        n 3fsqsm "You didn't seriously think I just pulled my poetry out of thin air or something,{w=0.5}{nw}"
        extend 3fsqbg " did you?{w=0.75}{nw}"
        extend 3fchgn " Nope!"
        n 4fllss "I mean,{w=0.75}{nw}"
        extend 1fcsss " I {i}am{/i} a natural..."
        n 2fcstr "...But you're only kidding yourself if you think you can get away without putting in actual effort too."
        n 2tllaj "Really though -{w=0.5}{nw}"
        extend 1tnmfl " how could anyone dislike something with so much variety?{w=0.75}{nw}"
        extend 4fspgs " Literature is {b}awesome{/b}!"
        n 4fcsbg "Epic stories...{w=0.75}{nw}"
        extend 4unmfl " life-changing experiences...{w=0.75}{nw}"
        extend 4clrss " anything and everything you could {i}possibly{/i} imagine..."
        n 2tsqfl "...And all I gotta do is turn the pages?{w=0.75}{nw}"
        extend 4fchgn " Sign me up!"
        n 2flrss "I've probably called you it a bunch before already,{w=0.2} [player]."
        n 2fsqsm "...But only a {i}real{/i} dummy would {i}check out{/i} on an offer that good.{w=0.75}{nw}"
        extend 2fcssm " Ehehe."
        n 4ulraj "Well,{w=0.2} anyway.{w=0.75}{nw}"
        extend 2tlrbo " I think I've gone on about that long enough.{w=0.75}{nw}"
        extend 2tsqfl " Who wants to spend all day talking about courses and topics of all things?"

        if Natsuki.isLove(higher=True):
            n 4ccsbgl "Besides,{w=0.2} [player]."
            n 3fcsbgl "Don't you recognize a far more interesting subject..."
            n 3fsqssl "...When it's already sat right in front of you?{w=0.75}{nw}"
            extend 3fsldvlsbr " Ehehe."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbgfsbr "L-{w=0.2}love you too,{w=0.2} [chosen_tease]!"

        elif Natsuki.isEnamored(higher=True):
            n 4fcsssl "Besides..."
            n 3fcsbglsbr "D-{w=0.2}don't you have something {i}way{/i} more interesting in front of you that you should be learning from instead?{w=0.75}{nw}"
            extend 1fslsslsbr " Ehehe..."

        else:
            n 4csqbg "In fact..."
            n 4fcsss "I guess you could say it's about time we...{w=0.75}{nw}"
            extend 3fsqbg " {i}changed the subject{/i}{w=0.75}{nw}"
            extend 3fchgn ",{w=0.2} right?"
            n 1nchgn "Ehehe."

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_topic:
            n 4fcsan "...Seriously?{w=0.75}{nw}"
            extend 4fsqan " You're telling me you weren't even {i}listening{/i} the first time?"
            n 1fcsfr "..."
            n 2fcsem "...Whatever.{w=0.75}{nw}"
            extend 2fslem " I don't care."
            n 2fslsl "I still can't stand maths."

        else:
            n 2fcssl "..."
            n 2fslsl "...I guess I can at least tell you what I {i}don't{/i} like.{w=1}{nw}"
            extend 2fcsfl " Math."

        n 4fsqfl "...And no,{w=0.2} not because I'm just hopeless at it or anything stupid like that.{w=1}{nw}"
        extend 4fsrem " {i}Despite{/i} what you probably think."
        n 1fcsem "It's just...{w=1}{nw}"
        extend 2fcsfl " it's way too complicated."
        extend 2fllan " It's ridiculous!"
        n 2fcsan "How is {i}anyone{/i} meant to remember so much random nonsense?{w=0.75}{nw}"
        extend 1flrem " Especially around exams."
        n 2fupfl "Because nothing makes me {i}love{/i} a subject more than having to no-life it{w=0.5}{nw}" 
        extend 4fcsan " every{w=0.3} single{w=0.3} time{w=0.3}{nw}" 
        extend 4fslan " an exam shows up."
        n 1fcssl "..."
        n 4fcsfl "I...{w=0.75}{nw}"
        extend 2fsran " get...{w=0.75}{nw}"
        extend 2fsrsr " that I could have just asked for help.{w=1}{nw}"
        extend 2fsqem " From my {w=0.2}{i}friends{/i}{w=0.3}, anyway."
        n 1clrsl "But that's not the point."
        n 2csrsl "Sometimes you just want to do stuff yourself.{w=1}{nw}"
        extend 2fsrfr " To not {i}need{/i} to rely on someone else constantly.{w=1.25}{nw}"
        extend 2fnmfl " And you know what?"
        n 1fllfl "Why not?{w=0.75}{nw}"
        extend 1fslan " Besides..."
        n 4fslem "Not like there's always gonna be {i}someone{/i} you can rely on."
        n 2fllem "...Right,{w=0.75}{nw}" 
        extend 2fsqem " {i}[player]{/i}?"

    else:
        if already_discussed_topic:
            n 2fslan "You {i}seriously{/i} think you're getting a different answer..."
            n 2fsqan "...If you just ask {i}again{/i}?{w=0.75}{nw}"
            extend 2fnmup " Do I {b}look{/b} like I was born yesterday?"
            n 4fnman "...And why exactly should I tell {i}you{/i},{w=0.2} anyway?"

        else:
            n 2fsqan "...Really?{w=0.75}{nw}"
            extend 2fsqfl " My favorite subject?"
            n 4fnman "...And why exactly should I tell {i}you{/i}?"

        n 4fsqfutsb "So you can start lecturing me about it?"
        n 2fcssltsa "Heh.{w=1}{nw}"
        extend 2fcsemtsa " Yeah.{w=1}{nw}"
        extend 2fsqantsb " {i}No thanks{/i}."
        n 4fsqupltsb "Now {i}get out of my face{/i}."
    
    return

# Natsuki talks about her drawing skills and art classes.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_can_you_draw",
            unlocked=True,
            prompt="Can you draw?",
            category=["Art"],
            conditional="jn_utils.get_total_gameplay_hours() >= 6",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_can_you_draw:
    $ already_discussed_topic = get_topic("talk_can_you_draw").shown_count > 0

    if Natsuki.isNormal(higher=True):
        if already_discussed_topic:
            n 2ccsbo "Wait...{w=1}{nw}"
            extend 2tnmpu " drawing?{w=0.75}{nw}"
            extend 2fsrpu " I could have sworn we talked about this before,{w=0.2} [player]...{w=1}{nw}"
            extend 4ncsbo " huh."
            n 4nllaj "Well,{w=0.2} anyway."
            n 4fslpo "I'm still kinda peeved about how my school handled art classes."
            n 2nnmaj "Like yeah,{w=0.2} we had them...{w=1}{nw}"
            extend 2fsrbo " but they weren't exactly super in-depth or anything.{w=0.75}{nw}"

        else:
            n 4tnmaj "Huh?{w=0.75}{nw}"
            extend 4cllbo " Can I draw?{w=0.75}{nw}"
            extend 1tslpu " Like...{w=0.3} portraits,{w=0.2} landscapes,{w=0.5}{nw}" 
            extend 2tnmaj " that kind of thing?"
            n 2ccsss "Heh.{w=0.75}{nw}"
            extend 2cslaj " I wish!{w=0.75}{nw}"
            extend 2fsqbo " And believe me -{w=0.5}{nw}"
            extend 4fcsss " you'd know about it if I had {i}that{/i} kind of talent."
            n 1nnmaj "I mean,{w=0.2} have you even {i}seen{/i} the sort of stuff people post online now?"
            n 4uspgs "It's insane!{w=0.75}{nw}"
            extend 3nlrss " I have no idea how they do it!"
            n 1csrbo "...Or even where they start,{w=0.2} for that matter."
            n 2nnmaj "We had art class during school,{w=0.5}{nw}"
            extend 2fslpo " obviously.{w=0.75}{nw}"
            extend 2cnmaj " But it wasn't really super in-depth or anything.{w=0.75}{nw}"

        extend 2fcsaj " Like...{w=0.3} at all."
        n 4clrpu "In fact.{w=0.75}{nw}"
        extend 1csrbo " the more I think about it..."
        n 2fcswr "It hardly even {i}qualified{/i} as art class at all!{w=0.75}{nw}"
        extend 2fllgs " It felt like we barely broke out the canvas!"
        n 2fcsan "I swear -{w=0.5}{nw}"
        extend 1csraj " so many lessons were just an exercise in page turning more than {i}painting{/i}."
        n 4ctrpu "I get that art has a lot of history behind it.{w=0.75}{nw}"
        extend 4csrfl " And of course there's tons of styles out there to learn.{w=0.75}{nw}"
        extend 4fcssl " I get it."
        n 1flrgs "But come{w=0.5}{nw}" 
        extend 2fcsgs " {b}on{/b}!{w=1}{nw}"
        extend 2fslup " What's even the point in studying so much about all these different artists and styles..."
        n 4fsqem "...If we barely even had the time to cover any of the basics?{w=0.75}{nw}"
        extend 4fcsup " Let alone try any of the stuff we studied out!"
        n 2cslem "A-{w=0.2}and besides!{w=0.75}{nw}"
        extend 2fslem " All those artists already had their turn.{w=0.75}{nw}"
        extend 4fcsgs " I wanna create cool things too!"
        n 1fcsemesi "Ugh..."
        n 2csrflsbl "You'd think the one time they want to encourage creativity would be when they'd give the textbooks a rest."
        n 2ccssl "..."
        n 2clrpu "I guess it wouldn't have been so bad if I could have just practiced outside school.{w=0.5}{nw}"
        extend 2tlrbo " Like at home or whatever.{w=0.75}{nw}"
        extend 4unmpu " Or maybe even the art club!"
        n 1nslss "Heh."
        n 4nslslsbr "No prizes for guessing why neither of those were gonna work out."
        n 4ccsajsbr "Putting all that aside though.{w=0.75}{nw}"
        extend 1unmaj " Honestly?"
        n 3csrpul "It's not that I wouldn't want to be able to draw cool stuff.{w=0.75}{nw}"
        extend 3tnmaj " Are you kidding?{w=0.75}{nw}"
        extend 4fchgn " That'd be awesome!"

        if Natsuki.isAffectionate(higher=True):
            n 2csrpusbl "It's just that..."
            n 2ksrbol "..."
            n 2fcspul "It's...{w=1}{nw}" 
            extend 1cslpu " intimidating.{w=1}{nw}"
            extend 2ksqsl " Trying to teach yourself something like that."
            n 2cllaj "It's fine if you've always been drawing,{w=0.2} or you have some kind of teacher."
            n 2cnmbol "...But what if you don't {i}have{/i} that kind of direction anywhere?"

            if Natsuki.isEnamored(higher=True):
                n 2ccsajl "People always say it's just down to practice,{w=0.75}{nw}"
                extend 2fsrsllsbl " or to look up some random course online or whatever.{w=0.75}{nw}"
                extend 2fnmflsbl " A-{w=0.2}and I'm not saying they're wrong!"
                n 2fcsposbr "That's just being ignorant."
                n 2fcsajsbr "Everyone has their own approach,{w=0.2} obviously.{w=1}{nw}"
                extend 2cslslsbr " But..."
                n 2kslbolsbr "...I guess I just never found mine.{w=1.25}{nw}"
                extend 4ccsssl " Not {i}yet{/i},{w=0.2} anyway."
                n 2ulrpu "Though...{w=1}{nw}"
                extend 4unmbo " what about you,{w=0.2} [player]?"
            
            else:
                n 2ncspuesi "..."
                n 2csrbo "I don't know."
                n 2ksrbosbr "..."
                n 4fcsajlsbl "A-{w=0.2}anyway!{w=0.75}{nw}"
                extend 2ccsca " I'm kinda bored of listening to myself now.{w=0.75}{nw}"
                extend 2tnmbo " So what about you,{w=0.2} [player]?"

        else: 
            n 2clrca "But...{w=1}{nw}"
            extend 2ksrpu " that's..."
            n 1fcsbo "..."
            n 1fcscalsbr "N-{w=0.2}nevermind."
            extend 1cllsll " I guess it doesn't even matter now anyway."
            n 4fcsajsbl "Besides.{w=0.2} I think I'm about done listening to myself talk for now."
            n 4nlraj "So...{w=0.75}{nw}"
            extend 4unmbo " what about you,{w=0.2} [player]?"

        if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
            n 4fwdaw "...Wait!{w=0.75}{nw}"
            extend 3fcsbg " Don't tell me!{w=0.75}{nw}"
            extend 3fcsbs " I've got a pretty good hunch for this kind of thing{w=0.5}{nw}"
            extend 3fsqss " if I say so myself."
            n 3fcssm "Ehehe."
            n 4fcsbg "Yep!"
            n 4fsqsmeme "You've got 'artist' written all over you."
            n 3fsqsssbr "All the more reason to be grateful you've always got {i}such{/i} a great subject on hand,{w=0.5}{nw}" 
            extend 3fcsbgsbr " am I right?"

        else:
            show n 4tnmbo
            menu:
                n "Do you get up to much drawing,{w=0.2} or...?"

                "Yes, I draw often!":
                    n 4fsqcs "Oh?{w=0.75}{nw}"
                    extend 3fsqss " Fancy yourself an artist,{w=0.2} huh?"
                    n 3fcssm "Ehehe."
                    n 3fllss "Well,{w=0.5}{nw}"
                    extend 3fsqcs " you better consider yourself lucky,{w=0.2} [player].{w=0.75}{nw}"
                    extend 3fcsbgsbr " Not every day such an {i}amazing{/i} subject just plonks itself down right in front of you!"

                "No, I don't usually draw.":
                    n 3tnmsl "Really?{w=0.75}{nw}"
                    extend 3cslca " Aww..."
                    n 3ullaj "I'll admit,{w=0.2} I am kinda disappointed.{w=1}{nw}"
                    extend 4tllbo " I get it though.{w=0.75}{nw}"
                    extend 2cslsssbr " Not like {i}I'm{/i} one to judge for that."
                    extend 4fsqsm " Yet."

                "I don't draw anymore.":
                    n 3kslpu "Aww..."
                    n 3tslbo "..."
                    n 3ccsfl "...Wait.{w=0.2} 'Anymore'?{w=0.75}{nw}"
                    extend 3csqem " What do you mean,{w=0.2} {i}'anymore'{/i}?{w=0.5}{nw}"
                    extend 3fcsgs " You gotta get back into it,{w=0.2} [player]!"
                    n 3tnmaj "Why not?{w=0.75}{nw}"
                    extend 3fcsbgsbr " {i}Especially{/i} when you've been blessed with {i}such{/i} a good subject to get started!{w=0.75}{nw}"
                    extend 3fcssmsbr " Ehehe."

        n 1ullaj "Well anyway.{w=0.75}{nw}"
        extend 2ccsaj " You know what?{w=0.75}{nw}"
        extend 2fcsbg " Who's to say I couldn't learn to draw at some point?"
        n 2utraj "There's gotta be some art supplies I can steal from somewhere around here."
        n 2nsrsssbl "Not like the art club's gonna need 'em now.{w=0.75}{nw}"
        extend 1tsqss " And who knows,{w=0.2} [player]?"
        n 3fcscsesm "I bet there's a Picasso in me yet!"
        n 3fnmbg "I just gotta{w=0.5}{nw}"
        extend 3fsqbg " {i}ease-l{/i}{w=0.5}{nw}"
        extend 3fchgn " into it first!{w=0.75}{nw}"
        extend 3nchgn " Ehehe."

        if Natsuki.isLove(higher=True):
            n 3fchbll "Love you too,{w=0.2} [player]~!"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_topic:
            n 2fcsemesi "..."
            n 4fcsfl "No,{w=0.2} [player].{w=1}{nw}"
            extend 4fsqan " Like I {i}already{/i} told you.{w=0.75}{nw}"
            extend 4fslsl " I can't."
            n 1fnmsf "What did you expect?{w=0.75}{nw}"
            extend 1flrem " I already said how my art classes sucked,{w=0.5}{nw}"
            extend 2fsqsl " if you were even paying attention."

        else:
            n 2fsqsl "No,{w=0.2} [player].{w=0.75}{nw}"
            extend 2fsrem " I can't.{w=0.75}{nw}"
            extend 2fcssf " If that really matters to you."
            n 2fllem "And not because I never wanted to learn or anything like that either."
            n 2fsqfl "You'd think art class of all places would be the best place to try and pick it up."

        n 2fsrpu "We barely even got out the art supplies -{w=0.75}{nw}"
        extend 2ftrem " we spent way more time learning about how {i}other people{/i} worked than actually learning ourselves!"
        n 1fnmsl "It was just a complete disappointment."
        n 1fcsbo "..."
        n 2fsqsl "Look.{w=0.2} I'm not dumb.{w=1}{nw}"
        extend 2fcsfl " I get that you gotta learn about why people do art,{w=0.75}{nw}"
        extend 2cslbo " or all the different styles and how they work."
        n 2fcsfl "But come{w=0.5}{nw}"
        extend 2fcsgs " {b}on{/b}!{w=0.75}{nw}"
        extend 2fslsf " It's not like the practical part is any less important."
        n 2cslpu "I wouldn't even care so much if we'd at least covered all of the basics {i}before{/i} dusting off all the stupid textbooks.{w=0.75}{nw}"
        extend 2fcssl " Not all of us have the time for an art club."
        n 2fsrem "...Or the luxury of practicing at home."
        n 2csrss "Heh.{w=0.75}{nw}"
        extend 2fcssf " I would say there's not much stopping me from trying to learn now.{w=0.75}{nw}"
        extend 2cslsf " Not like spare time is a problem anymore."
        n 2fnmsl "But honestly?"
        n 2fsqem "{i}Something{/i} tells me I'm not gonna be in the mood for that a whole lot."
        n 2fslan "I wonder why..."
        extend 2fsqem " {i}[player]{/i}."

    else:
        if already_discussed_topic:
            n 2fslan "...Seriously?{w=1}{nw}"
            extend 2fsqan " What am I,{w=0.2} a broken record?"
            n 2fsquptsb "The only thing I'm drawing right now is an end to this {i}stupid{/i} conversation."
            n 4fsqanltsb "Jerk."

        else:
            n 2fcssstsa "...Heh.{w=1}{nw}"
            extend 2fslfltsb " Can I draw?{w=1.25}{nw}"
            extend 2fsqantsb " Really?"
            n 2fcssftsa "..."
            n 2fcsfltsa "...Actually.{w=0.75}{nw}"
            extend 2fsqfutsb " You know what?"
            n 2fcsemtsa "Yeah.{w=0.2} I am.{w=0.75}{nw}"
            extend 2fsqantsb " At drawing conclusions."
            n 4fnmfultsf "...And I've got plenty drawn about the likes of {b}you{/b}."

    return

# Ask Natsuki to remind the player next time she runs out of topics.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_enable_no_topics_reminder",
            unlocked=True,
            prompt="Can you remind me next time you run out of topics?",
            category=["Natsuki", "Reminders"],
            conditional="not persistent._jn_natsuki_out_of_topics_remind",
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_enable_no_topics_reminder:
    $ already_discussed_topic = get_topic("talk_enable_no_topics_reminder").shown_count > 0

    n 1tnmpueqm "Huh?{w=0.75}{nw}"
    extend 4tnmbo " Topics?{w=0.75}{nw}"
    extend 2tsrfl " What do you...?"
    n 2ttrsl "..."

    if already_discussed_topic:
        n 4fnmwrleexsbr "...H-{w=0.2}hey!{w=0.75}{nw}"
        extend 4fsqwrl " Now hold on just a second here,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fcsgs " I know {i}exactly{/i} what this is all about!"
        n 2fllfl "You even said before that you wanted me to {i}stop{/i} reminding you..."
        n 2fnmgs "And now you're getting on my case about reminding you{w=0.3}{nw}" 
        extend 4fcsgs " {i}again{/i}!{w=1}{nw}"
        extend 2fsrfl " Jeez..."
        n 2cslpu "Do I really have to remind you how to make a {i}decision{/i} too now [player],{w=0.5}{nw}" 
        extend 2csqpu " or what?"
        n 2fsqpo "..."
        n 2fsqcs "..."
        n 2fcssm "Ehehe.{w=0.75}{nw}"
        extend 4nlrss " Nah,{w=0.5}{nw}"
        extend 1csrss " it's fine.{w=0.75}{nw}"
        extend 1csrbo " {i}I guess{/i}."
        n 4ccsaj "Just...{w=1}{nw}"
        extend 2csqca " don't make some kind of habit out of it.{w=0.75}{nw}"
        extend 2cslcasbr " I hate sounding like a broken record."
        
        if Natsuki.isEnamored(higher=True):
            n 2fcsbglsbr "E-{w=0.2}even if you do enjoy listening to me go on about it {i}that{/i} much.{w=0.75}{nw}"
            extend 2fsqsmlsbr " Ehehe."

            if Natsuki.isLove(higher=True):
                n 4fchbglsbl "Love you,{w=0.2} [player]~!"

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsajlsbr "E-{w=0.2}even if you {i}do{/i} enjoy hearing me go on about it that much.{w=0.75}{nw}"
            extend 2ccsbolsbl " Got it?"

        else:
            n 2fcsaj "A-{w=0.2}and I'm sure you would too.{w=0.75}{nw}"
            extend 2fcspo " Capiche?"

    else:
        if Natsuki.isEnamored(higher=True):
            n 2unmajesu "Oh!{w=0.75}{nw}"
            extend 4nllsssbr " Yeah,{w=0.2} I remember."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchsm "Sure thing,{w=0.2} [chosen_tease]!{w=0.75}{nw}"
            extend 3fsqss " Better not catch you making any complaints though,{w=0.2} [player]."
            n 4fcsbg "After all..."
            n 3uchgnl "{i}You{/i} asked for it!{w=0.75}{nw}"
            extend 3fchsmleme " Ehehe."

        elif Natsuki.isAffectionate(higher=True):
            n 4unmajesu "Oh!{w=0.75}{nw}"
            extend 4nslsssbr " Right,{w=0.5} that."
            n 2fchbg "Sure thing!{w=0.75}{nw}"
            extend 2fsqbg " Just remember,{w=0.2} [player]..."
            n 2nchgn "You asked for it!"

        else:
            n 2unmfleex "Oh!{w=0.75}{nw}"
            extend 2cllsssbr " Heh.{w=0.75}{nw}"
            extend 4cslsssbr " Right."
            n 2ullaj "I mean...{w=1}{nw}"
            extend 2tnmbo " sure thing,{w=0.2} I guess."
            n 2ccspo "J-{w=0.2}just don't get all antsy when I gotta tell you what's up again,{w=0.2} got it?"


    $ persistent._jn_natsuki_out_of_topics_remind = True
    return

# Natsuki expresses her frustration towards people being inconsiderate with their audio in public.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_playing_things_out_loud",
            unlocked=True,
            prompt="Playing things out loud",
            category=["Wind-ups"],
            conditional="jn_utils.get_total_gameplay_hours() >= 4",
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_playing_things_out_loud:
    $ already_discussed_topic = get_topic("talk_windup_playing_things_out_loud").shown_count > 0
    if already_discussed_topic:
        n 7csrca "..."
        n 3fcsflesi "..."
        n 3cllfl "You know,{w=0.2} [player]..."
        n 7tnmsl "I'm pretty sure I went through it all before.{w=0.75}{nw}"
        extend 7clrflsbl " And I don't even know why it still bothers me so much."
        n 4fsrem "But I {i}still{/i} can't stand when some people feel the need to just blast what {i}they{/i} wanna listen to out loud in front of everyone else."
        n 2fsrca "..."
        n 2fnmfll "What?{w=0.75}{nw}"
        extend 2csqfll " Do I look like I'm making it all up or something?{w=0.75}{nw}"
        extend 4fcsgsl " It's the {i}worst{/i}!"

    else:
        n 7cslsl "..."
        n 3fslan "Tch!"
        n 3fsrbo "..."
        n 3ccsss "Heh."
        n 4cllfl "Hey,{w=0.2} [player]...{w=1}{nw}"
        extend 2cnmaj " you wanna know what winds me up?"
        n 2fnmfl "And I mean{w=0.5}{nw}"
        extend 4fsqem " {i}really{/i}{w=0.5}{nw}"
        extend 4fsran " gets on my nerves?"
        n 2fcsemesi "..."
        n 2fllaj "When you're taking some sort of public transport,{w=0.2} or you're just hanging around somewhere.{w=0.75}{nw}"
        extend 2fllfl " That kind of thing."
        n 4fcsanean "...And then some total jerk feels the need to pull out their phone just to blast out what {i}they{/i} feel like listening to."
        n 4fsrsl "..."
        n 2fnmwrl "H-{w=0.2}hey!{w=0.75}{nw}"
        extend 2fcspol " I'm being serious here,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fbkwrl " It's the {i}worst{/i}!"

    n 3flrem "I mean,{w=0.2} come on.{w=0.75}{nw}"
    extend 3fupwr " Where do I even {i}start{/i}?"
    n 6fcsgs "First off,{w=0.5}{nw}"
    extend 3fllan " you can basically guarantee that whatever it is,{w=0.75}{nw}" 
    extend 3fslan " it's {i}never{/i} gonna sound good."
    n 4fbkwr "Nothing ever {i}does{/i} when you're blasting it out of crappy phone speakers or busted-up headphones!"
    n 4fcsan "Bonus points too if it's some kid playing on something their parents gave them just to shut them up."
    n 1nsqem "And{w=0.3} Oh.{w=0.75}{nw}"
    extend 2csqfl " My.{w=0.75}{nw}"
    extend 2fsqem " God,{w=0.5}{nw}"
    extend 4fsrfu " [player]."
    n 4fcsup "{i}The echoing{/i}."
    n 3fsqgs "Do you even know how much worse it gets when you're stuck inside the train,{w=0.5}{nw}" 
    extend 3fcsgs " or literally anything else?"
    n 3fcsan "Talk about an earache.{w=0.75}{nw}"
    extend 7fllem " Especially if you just wanted to relax before the day starts!"
    n 4fsrem "{i}And{/i} you can forget about trying to hold any kind of conversation too with all that noise in the background."
    n 2fcssl "Heh.{w=0.75}{nw}"
    extend 2fsqfr " Then you know what the worst part is,{w=0.2} [player]?"
    n 4fllem "If you even try to call them out,{w=0.5}{nw}"
    extend 4csqem " you just know they'll make a massive scene over it too,{w=0.5}{nw}" 
    extend 4fslfu " or make it sound like you're just freaking out!"
    n 6ftlgs "'But you don't {i}have{/i} to listen to it!'{w=0.5}{nw}"
    extend 3ftrwr " 'You can play what you want too!'\n{w=0.75}{nw}"
    extend 3fsran "As if that makes everything just a-okay,{w=0.5}{nw}" 
    extend 3fsqan " right?"
    n 1fcsem "Cut me a break."
    n 2flran "Like just how inconsiderate can you get?{w=0.75}{nw}"
    extend 2fcsan " Seriously?!"
    n 4fslem "B-{w=0.2}besides,{w=0.5}{nw}"
    extend 4fcsgs " it's not like you can just choose {i}not{/i} to hear whatever they decide to grace your ears with."
    n 2fsrsll "...And not all of us can afford all the fancy noise cancelling stuff either."
    n 1ccsemesi "Ugh..."
    n 2fllsl "Jerks.{w=0.75}{nw}"
    extend 2fslbol " Makes me wanna yank that stupid phone or whatever out of their hands and toss it out the window."

    if get_topic("talk_using_headphones_carefully").shown_count > 0:
        n 1ccsfll "And I know I said before that shutting yourself away from the world with headphones was a bad idea."
        $ descriptor = "{i}trying{/i} to be" if Natsuki.isAffectionate(higher=True) else "being kinda"
        n 5csrsl "But at least you're still [descriptor] considerate.{w=0.75}{nw}"
        extend 5cnmbol " You know?"

        if Natsuki.isAffectionate(higher=True):
            n 1ccsfll "I just..."
            n 4csrsll "..."

    n 4ccsfllesi "..."
    n 2cslajl "...Look.{w=0.75}{nw}"
    extend 2ccsbo " I'm not dumb.{w=0.75}{nw}"
    extend 1clrfl " I get that if you're in a public space then you gotta accommodate others who want to use it too."
    n 3fslem "But that doesn't give any old jerk the right to use it how {i}they{/i} want at the expense of everyone else!"
    n 3fsrsl "...Let alone act so entitled over the whole stupid thing.{w=0.75}{nw}"
    extend 3fsrfl " Yeesh."
    n 3fnmca "..."
    n 4ccsflsbl "...Yeah,{w=0.2} yeah.{w=0.75}{nw}"
    extend 1cllcasbl " I know.{w=0.75}{nw}"

    if already_discussed_topic:
        extend 2cllflsbr " I'm not gonna let myself get all wound up about it.{w=0.75}{nw}"
        extend 2cslflsbr " Again."

    else:
        extend 2ccstrlsbr " I'm not gonna let myself get {i}that{/i} wound up about it."

    if Natsuki.isEnamored(higher=True):
        n 2fcsssl "...E-{w=0.2}even if I know you just can't get enough of the sound of my voice."

    elif Natsuki.isAffectionate(higher=True):
        n 2csrpol "...Even if I bet you just enjoy listening to my stupid rants by now."

    n 2ulraj "So...{w=1}{nw}"
    extend 2cnmca " I'm just gonna say this."
    n 1tllfl "I don't really care what you listen to or how you listen to it in your own four walls,{w=0.2} [player]."

    if Natsuki.isEnamored(higher=True):
        n 5csrssl "And I {i}seriously{/i} doubt you of all people would do something like that.{w=0.75}{nw}"
        $ descriptor = "you're still" if Natsuki.isLove(higher=True) else "you are"
        extend 5csqssl " Even if [descriptor] a big dope sometimes."

    elif Natsuki.isAffectionate(higher=True):
        n 4csrsslsbr "And I kinda doubt you're the sort of person who does that kind of thing anyway."

    else:
        n 2tlraj "And I kinda doubt you're {i}that{/i} much of a jerk anyway."

    n 2clrfl "But...{w=1}{nw}"
    extend 2csgfl " if I hear about you blasting some kind of [player] broadcast out there in front of everyone when {w=0.3}{i}literally{/i}{w=0.5}{nw}" 
    extend 2csqfl " no-one asked?"
    n 4fcsbs "...Then you can bet your butt I'm going to give {i}your{/i} ears something extra-special to listen to!{w=0.75}{nw}"
    extend 4fsqsmeme " Ehehe."

    if Natsuki.isLove(higher=True):
        n 2fchbgl "Love you,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 2fchgnl "You're welcome,{w=0.2} [player]!"

    else:
        n 2nchgn "Hope you learned something,{w=0.2} [player]!"

    return

# Natsuki discusses her work "experience" and frustrations with the placement process.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_experience",
            unlocked=True,
            prompt="Did you ever have any work experience?",
            category=["Society"],
            conditional="jn_utils.get_total_gameplay_days() >= 2",
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_experience:
    $ already_discussed_work_experience = get_topic("talk_work_experience").shown_count > 0
    if Natsuki.isNormal(higher=True):
        if already_discussed_work_experience:
            n 7csrfl "Wait...{w=1}{nw}"
            extend 7tnmfl " work experience?{w=0.75}{nw}"
            extend 3ccsajsbr " H-{w=0.2}hang on a sec."
            n 7tnmbosbr "Didn't you ask me about that already,{w=0.2} [player]?{w=0.75}{nw}"
            extend 7tllsl " Huh."
            n 4tllaj "Well,{w=0.5}{nw}"
            extend 4ullaj " whatever.{w=0.75}{nw}"
            extend 2cnmfl " I guess I don't mind sharing my...{w=1}{nw}"
            extend 2csrfl " {i}experience{/i}{w=0.5}{nw}"
            extend 2csrsl " again."
            n 1ccsem "If you can even call it that,{w=0.2} a-{w=0.2}anyway."
            n 3cllfl "Like I was saying before,{w=0.2} we never properly got to choose our placements or anything like that."

        else:
            n 3tlrbo "Work experience,{w=0.5}{nw}"
            extend 3tnmbo " huh?"
            n 4ccsflsbl "...Wait.{w=0.75}{nw}"
            extend 4nsqflsbl " Don't tell me.{w=0.75}{nw}"
            extend 2csqem " You mean like some kind of placement while I was in school?{w=0.75}{nw}"
            extend 2tsqfl " Or like an internship?"
            n 1cnmsl "{i}That{/i} kind of work experience?"
            n 2fcsslesi "..."
            n 2ccsfl "Heh.{w=0.75}{nw}"
            extend 2cllfl " Yeah.{w=0.75}{nw}"
            extend 4cslfr " The whole process was an {i}experience{/i} alright."
            n 7nllaj "So.{w=0.75}{nw}"
            extend 7ullfl " I don't know how it works for you,{w=0.2} [player].{w=0.75}{nw}"
            extend 3tnmsl " But at my school at least?{w=0.75}{nw}"
            extend 3clrem " We didn't even get to properly {i}choose{/i} our placements."

        n 1fnmem "Seriously -{w=0.5}{nw}" 
        extend 4fllgs " it was a total crapshoot!{w=0.75}{nw}"
        extend 2fslan " Nothing but dumb luck!"

        if already_discussed_work_experience:
            n 2ccsslsbr "And no,{w=0.2} like I said -{w=0.5}{nw}"

        else:
            n 2ccsemsbr "And no,{w=0.2} [player],{w=0.2} before you ask -{w=0.5}{nw}"

        extend 1csqemsbr " we didn't get a choice on if we {i}wanted{/i} to do it either."
        n 4clraj "We all had this online form we had to fill out in the computer room,{w=0.5}{nw}"
        extend 4fsqfl " but it wasn't like we could just type in a place we already had in mind.\n{w=0.75}{nw}"
        extend 2fupem "Of {i}course{/i} not."
        n 2fcsgs "Nope!{w=0.75}{nw}"
        extend 2fllem " It was just a bunch of pre-filled options we had to pick between.{w=0.75}{nw}"
        extend 4fslan " They weren't even good ones!"
        n 2flrem "There were a couple of office places,{w=0.2} sure."
        n 2fnman "But most of them were just working in some random store!{w=0.75}{nw}"
        extend 4fcswr " The whole point of those is that you don't even {i}need{/i} experience to do them!"
        n 2fsrem "...And we had to pick {i}three{/i} of them too.{w=0.5} {i}In order of preference{/i}."
        n 1fcssl "Heh.{w=0.75}{nw}" 
        extend 4fsqfl " The worst part,{w=0.2} [player]?{w=0.75}{nw}"

        if already_discussed_work_experience:
            extend 4fslsl " It {i}still{/i} bugs me talking about it a second time."

        else:
            extend 4fllfl " You're not even gonna {i}believe{/i} this."

        n 4fnmgs "We had to write out a complete cover letter for all of them too!{w=0.75}{nw}"
        extend 2fsran " There was a word count and everything!"
        n 2ccsemesi "..."
        n 2fcsbosbr "I get it.{w=0.75}{nw}"
        extend 7cllflsbl " It was supposed to give us practice on how to apply for stuff in the future."
        n 3fcsgs "But {i}seriously{/i}!"
        n 2fslan "Do you know how much of a pain it is to sound convincing for something you don't even {i}care{/i} about?"
        n 2fcswr "We didn't even know about half of the places we could pick until they showed up on the list!"
        n 1fsran "It isn't like the places we were applying to didn't {i}know{/i} we had to do it either -{w=0.5}{nw}"
        extend 3fcsan " it's all a total act anyway!"
        n 3fllem "So then we were stuck trying to desperately research all these places,{w=0.5}{nw}"
        extend 3fnmem " what they even did,{w=0.5}{nw}"
        extend 4flran " how to actually {i}get{/i} there..."
        n 1fsqan "...While trying to play up how {i}amazing{/i} for the job we were and beat everyone else in submitting it!"
        n 2fslsl "Then with everyone applying for all the good ones,{w=0.5}{nw}" 
        extend 2fslem " the teachers would just send off your last choice instead.{w=0.75}{nw}"
        extend 4fnmbo " Or dump you with some place nobody wanted at all."

        $ already_discussed_interviews = get_topic("talk_how_to_interview_properly").shown_count > 0
        if already_discussed_interviews:
            n 1csrsl "Talk about a complete waste of time."
            n 2clrflsbl "I already mentioned before that I never had the time for a part-time job or anything like that outside of school."
            n 4csqslsbl "...So why did they think we'd have a couple of weeks to blow on something like {i}that{/i}?"
            n 2fcsfl "{i}Especially{/i} when it isn't even paid work."

        else:
            n 2fcsfl "Ugh..."
            n 6tsqfl "And with the constant assignments plus all the regular lessons too?{w=0.75}{nw}"
            extend 4fllfl " I didn't even have time for a {i}paid{/i} job!{w=0.75}{nw}"
            extend 2fcsaj " Let alone just forking over all my effort for {i}free{/i}."

        n 2csrfl "Yeah,{w=0.2} yeah.{w=0.75}{nw}"
        extend 2clrfl " We get to spend time in a real workplace so we know what to expect later,{w=0.5}{nw}"
        extend 1clrbo " or build some connections."
        n 2ccsflsbr "It's just that..."
        n 5cslbosbr "..."

        if Natsuki.isAffectionate(higher=True):
            n 4fcsemsbr "I-{w=0.2}it's just so {i}annoying{/i}!{w=0.75}{nw}"
            extend 4knmemsbr " You know?{w=0.75}{nw}"
            extend 2csrfllsbl " With so much going on at the same time,{w=0.2} I mean."
            n 1csrsllsbl "..."
            n 4ccspulsbl "I...{w=1}{nw}"
            extend 4fcspul " don't...{w=1}{nw}"
            extend 2flrbol " mind helping a place out."
            n 5csrpul "If it's about something I actually {i}care{/i} about."
            n 5cnmeml "...But why does {i}my{/i} future have to suffer for it?"
            n 2cslsll "It's not like I couldn't just land a job at one of those places when I actually needed the work.{w=0.75}{nw}"
            extend 2knmbol " Right?"

            if Natsuki.isEnamored(higher=True):
                n 1ccsss "Heh.{w=0.75}{nw}"
                extend 1csrpu " Besides."
                n 1clrsll "I was already told my future was just gonna be stacking shelves."
                n 2kslsll "...The last thing I needed was a preview."
                n 2kslbol "..."
                n 4ccsemlsbr "A-{w=0.2}anyway!"

            else:
                n 2kslbol "..."
                n 4ccscasbr "A-{w=0.2}anyway."

            n 5cslbo "As if all the time spent looking and filling stuff out actually ended up meaning much."
            n 4unmgs "Not that I didn't {i}try{/i} or anything like that!{w=0.75}{nw}"
            extend 2fcsgssbr " O-{w=0.2}of course I did!{w=0.75}{nw}"
            extend 2fllslsbr " Just my luck that everyone felt like picking the only places {i}I{/i} could stomach."
            n 5flrflsbr "And it wasn't like I could even get to many other places either."
            n 5clrslsbr "Not with my...{w=1}{nw}" 
            extend 1ksrslsbr " situation."
            n 1nlraj "So..."
            n 2nslbo "They agreed to let me pull some time in the school library instead.\n{w=0.75}{nw}"
            extend 2cslss "At least I got to study when it wasn't busy."
            n 2kslsllsbr "...And I always got home on time.{w=1}{nw}"
            extend 5cslbol " I guess I could appreciate that."

            $ office_outfit = jn_outfits.getOutfit("jn_office_outfit")
            if Natsuki.isEnamored(higher=True) and persistent.jn_custom_outfits_unlocked and not office_outfit.unlocked:
                n 7cllbo "..."
                n 7cllfl "...Actually.{w=0.75}{nw}"
                extend 7tllbo " Now that I think about it..."
                n 3tnmfl "I'm pretty sure I still have the outfit I put together for my placement somewhere too.{w=0.75}{nw}"
                extend 3nlrfl " Huh."
                n 4tlrsl "..."
                n 4tsrss "In fact.{w=0.75}{nw}"
                extend 7cnmss " You know what?{w=0.75}{nw}"
                extend 6ccsss " Just give me a minute here."
                n 3fcsbslsbl "Someone's gotta show you what a {i}real{/i} professional looks like,{w=0.2} a-{w=0.2}after all!"
                
                show natsuki 4fcssmlsbl
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio chair_out

                $ jnPause(3)
                play audio drawer
                $ jnPause(1.5)
                play audio clothing_ruffle
                $ jnPause(1.5)
                n "Hey!{w=0.5} N-{w=0.2}no peeking!"
                $ jnPause(1)
                play audio zipper
                $ jnPause(3)
                $ office_outfit.unlock()
                $ Natsuki.setOutfit(outfit=office_outfit, persist=False)

                play audio chair_in
                $ jnPause(3)
                show natsuki 5csrdvlsbr at jn_center
                hide black with Dissolve(1.25)

                n 5csqbolsbr "..."
                n 5ccssslsbr "W-{w=0.2}well?{w=0.75}{nw}"
                extend 4cnmajlsbr " Don't lie,{w=0.2} [player]!{w=0.75}{nw}"
                extend 4cllbglsbr " After all."
                n 3fcsbglsbl "I don't need to be a proper librarian to read {i}you{/i} like a book.{w=0.75}{nw}"

                if Natsuki.isLove(higher=True) and get_topic("talk_school_uniform").shown_count > 0:
                    extend 4fslbglsbl " Besides..."
                    n 6fsgsmlsbl "D-{w=0.2}didn't you {i}like{/i} a girl in uniform,{w=0.2} [player]?{w=0.75}{nw}"

                extend 3fsqsmlsbl " Ehehe."
                n 5fcsbgsbl "Obviously I didn't {i}have{/i} to dress up for it or anything like that.{w=0.75}{nw}"
                extend 2flrbg " But come on."
                n 2fchgn "Who {i}wouldn't{/i} pass up a break from school uniform,{w=0.2} right?"

            else:
                n 1ccsfllesi "..."

        else:
            n 4ccsflsbr "N-{w=0.2}nevermind.{w=0.75}{nw}"
            extend 2ccsposbr " Obviously my placement was fine.{w=0.75}{nw}"
            extend 2csrbosbr " Though it's not like any of that matters now anyway."

        if persistent._jn_player_had_work_placement is None:
            n 1ulraj "But...{w=1}{nw}"
            extend 4clrflsbl " I've gone on way too much already.{w=0.75}{nw}"
            extend 5csrbosbl " Again.{w=0.75}{nw}"
            extend 2tlraj " So..."
            n 7tnmaj "What about you though,{w=0.2} [player]?"

            show natsuki option_wait_curious
            menu:
                n "Did you ever have any kind of work placement,{w=0.2} or...?"

                "Yes, I've had a work placement.":
                    $ persistent._jn_player_had_work_placement = True
                    n 4fnmbg "Aha!{w=0.75}{nw}"
                    extend 3fcsbg " I knew it!{w=0.75}{nw}"
                    extend 6fsqsm " Just couldn't slip your way out of it,{w=0.2} huh?"
                    n 7tllss "Well...{w=0.3} I can't really say I'm surprised.{w=0.75}{nw}"
                    extend 7ccssmesm " Not like {i}you{/i} could talk yourself out of it if I couldn't."

                "No, I haven't had a work placement.":
                    $ persistent._jn_player_had_work_placement = False
                    n 3nsrsl "...Hmph.{w=0.75}{nw}"
                    extend 3fcspo " Lucky."
                    n 7clraj "Though I gotta ask,{w=0.2} [player]."
                    n 7tnmfl "Is that because you just never went somewhere that did those?"
                    n 6fcsbg "...Or are you just sitting around waiting for your turn?"
                    n 3fsqsm "..."
                    n 3fcssm "Ehehe.{w=0.75}{nw}"
                    extend 4csgbg " Did I call you out?"

                "I have a work placement now.":
                    $ persistent._jn_player_had_work_placement = True
                    n 3ccsss "Oh?{w=0.75}{nw}"
                    extend 7ccsbg " And I suppose you're working hard then,{w=0.2} [player]?"
                    n 7csqsm "...Heh."
                    n 6fsqbg "Or are you hardly working?"
                    n 3fsqsm "..."
                    n 3fcssmeme "Ehehe."

            n 4ulrss "Well,{w=0.2} whatever."

        else:
            n 1nlraj "But...{w=1}{nw}"
            extend 5clrpu " I've gone on for way too long already.{w=0.75}{nw}"
            extend 5csrbosbl " I really gotta stop doing that."

        if Natsuki.isEnamored(higher=True):
            n 3clrfl "I still wouldn't say I really rate my work placement."
            n 7tlrbo "But...{w=1}{nw}"
            extend 7tnmca " being here with you,{w=0.2} [player]?"
            n 4ccsssl "Heh."
            n 4cllsslsbr "...Yeah,{w=0.5}{nw}"
            extend 5ccssmlsbr " I'd say that's an {i}experience{/i} I can be pretty happy about."
            n 5clrbglsbr "E-{w=0.2}even if you {i}are{/i} a bunch of work sometimes.{w=0.75}{nw}"
            extend 2fchsmfsbr " Ehehe."

            if Natsuki.isLove(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 5fchblfeaf "L-{w=0.2}love you too,{w=0.2} [chosen_tease]!"

        elif Natsuki.isAffectionate():
            n 3clrfl "I still wouldn't say I rate my experience honestly."
            n 7tlrbo "But...{w=1}{nw}"
            extend 7tnmfl " being stuck here with you,{w=0.2} [player]?"
            n 5tllbolsbr "..."
            n 5tllsslsbr "Well...{w=1}{nw}"
            extend 6ccsbglsbl " I-{w=0.2}I guess I could think of a worse placement!"
            n 3ccssmlsbl "Ehehe."

        elif Natsuki.isHappy():
            n 5clrfl "I wouldn't exactly say I rate my experience,{w=0.2} to be honest."
            n 7clrpu "But...{w=1}{nw}"
            extend 7tnmpu " just sitting around here talking to you?{w=0.75}{nw}"
            extend 7ullbo " Well..."
            n 2fchgn "I guess I can think of plenty worse placements!{w=0.75}{nw}"
            extend 2nchgn " Ahaha."

        else:
            n 7ulraj "I wouldn't exactly say I rate my experience,{w=0.2} to be honest."
            n 7tlrfl "But...{w=1}{nw}"
            extend 7tnmfl " just sitting around here with you?"
            n 4tllaj "Well...{w=1}{nw}"
            extend 4nchgn " I guess I could do worse!"
            n 2csrajsbl "J-{w=0.2}just don't make it all awkward,{w=0.2} [player].{w=0.75}{nw}"
            extend 5cslposbl " Capiche?"

    elif Natsuki.isDistressed(higher=True):
        if already_discussed_work_experience:
            n 1ccsemesi "..."
            n 2cslem "Seriously,{w=0.75}{nw}" 
            extend 2csqem " [player]?{w=0.75}{nw}"
            extend 4fsqfl " This {i}again{/i}?{w=0.75}{nw}"
            extend 4fnmfl " Were you even {i}listening{/i} the first time or what?"
            n 1fcsfr "..."
            n 1flrfl "...Fine.{w=0.75}{nw}"
            extend 2fcsfl " Besides."
            n 4fllsl "I'm not gonna discriminate against the{w=0.5}{nw}" 
            extend 4fsqsl " {i}hard of hearing{/i}."
            n 1fcsfl "So.{w=0.75}{nw}"
            extend 1flrbo " Like I was saying before..."

        else:
            n 4nsqfl "...What?{w=0.75}{nw}"
            extend 4tsqsl " Work experience?"
            n 4nslfl "Oh."
            n 2fcsfl "Heh.{w=0.75}{nw}"
            extend 2flrfl " Yeah.{w=0.75}{nw}"
            extend 2fsrpu " I had an {i}experience{/i} alright.{w=0.75}{nw}"
            extend 4csqsl " If that actually matters."

        n 1nllaj "My school did placements,{w=0.75}{nw}" 
        extend 1nllsl " but it wasn't some kind of big event if that's what you were thinking."
        n 2fslfr "Though some actual {i}notice{/i} would have been nice."
        n 2fcsaj "Nope -{w=0.5}{nw}"
        extend 4flrem " we were all just shuffled off to the computer room one day,{w=0.5}{nw}"
        extend 4fnmfl " and told to log into some special placement website."
        n 3cslfl "Then we had to pick some choices from a list of places that were accepting students to do work placements."
        n 3ctlfl "There were a couple decent places,{w=0.2} sure.{w=0.75}{nw}"
        extend 3fcsan " But {i}everybody{/i} went for those!{w=0.75}{nw}"
        extend 3fsran " And then you'd just be shipped off to some dump nobody cared about instead if you weren't the teacher's favorite."
        n 1fcsem "...And no,{w=0.2} [player].{w=0.75}{nw}"
        extend 2nsqsl " We didn't get the option to pass.{w=0.75}{nw}"
        extend 2cllsl " We {i}all{/i} had to do it."
        n 4fllem "It wasn't just picking stuff from a list either -{w=0.5}{nw}"
        extend 4fsqfl " cover letters and interviews too.{w=0.75}{nw}"
        extend 4fsrfl " The whole stupid process."
        n 1flrsl "I don't even know who they thought they were kidding."
        extend 2fsrsl " It wasn't like those places {i}weren't{/i} just going to accept whoever the school sent them."
        n 2fllfl "And then all of that around our regular studies just to rub it in.\n{w=0.75}{nw}"
        extend 4fslem "As if we'd just {i}magically{/i} find the time around all the assignments and exams or something."
        n 4fcsemesi "..."
        n 2fcssl "I get it,{w=0.2} okay?{w=0.75}{nw}"
        extend 1fsrem " I'm not dumb.{w=0.75}{nw}"
        extend 2ccsem " {i}Obviously{/i} life skills and connections matter."
        n 4fcsfl "But come{w=0.5}{nw}"
        extend 4fcsgs " {b}on{/b}!{w=0.75}{nw}"
        extend 3flrsl " As if I'm missing out on {i}super important{/i} life experience stacking{w=0.5}{nw}" 
        extend 3fsran " shelves,{w=0.5}{nw}" 
        extend 3fllem " or playing cashier for two weeks."
        n 1fcsem "Ugh..."
        n 2flrsl "I wouldn't have cared so much if I didn't have everything else to keep on top of.{w=0.75}{nw}"
        extend 2fsrsl " Or if the work was actually {i}paid{/i}.{w=0.75}{nw}"
        extend 2fsrem " What a waste of time."
        n 1fcsfl "Not like any of that matters now though,{w=0.2} I guess."
        n 4fsqfl "After all."

        if Natsuki.isUpset(higher=True):
            n 4fslsl "Being here right now already feels like a job enough to me,{w=0.5}{nw}"
            extend 4fsqfr " {i}[player]{/i}."
            
        else:
            n 4fcsan "Dealing with {i}you{/i} right now feels like a job enough to me,{w=0.5}{nw}"
            extend 4fsqan " {i}[player]{/i}."

    else:
        if already_discussed_work_experience:
            n 1fcsfltsa "Heh.{w=1}{nw}"
            extend 1fsqantsb " What do I look like?{w=1.25}{nw}"
            extend 4fnmuptsc " Your personal {i}soundboard{/i}?"
            n 4fcsantsa "Like I already {i}told you{/i} -{w=0.75}{nw}"
            extend 4fcswrtsa " it sucked,{w=0.2} okay?!{w=1}{nw}"
            extend 2fsqwrtsb " Is that what you wanted to hear?!"
            n 2fslantsb "I never wanted to do any,{w=0.2} and I was made to anyway."
            n 4fsqfultsb "Much like this conversation.{w=1}{nw}"
            extend 4fcsanltsa " I'm {i}done{/i} talking about this,{w=0.2} {i}[player]{/i}."

        else:
            n 1fsqfltsb "...Really?{w=1}{nw}"
            extend 4fnmantsc " And since when did you care about any of my experiences,{w=0.75}{nw}" 
            extend 4fsqantsc " {i}[player]{/i}?"
            n 4fcsuntsa "..."
            n 2fcsemtsa "You know what?{w=1}{nw}"
            extend 2fcsantsa " I don't care.{w=1}{nw}"
            extend 1fnmantsc " You want an answer so bad?{w=1.25}" 
            extend 2fsquptsb " {b}Fine{/b}."
            n 2flrantsc "It was crap.{w=1}{nw}"
            extend 4fnmfutsc " Okay?!{w=1.25}{nw}"
            extend 4fcsfutsa " The {i}entire{/i} process."
            n 1fslantsb "From applying to all the stupid choices,{w=0.75}{nw}"
            extend 1fslfrtsb " to writing out pointless letters.{w=1}{nw}"
            extend 2fsqantsb " All of it."
            n 2fcsunltsa "Heh.{w=1}{nw}"
            extend  4fcsgtltsa " And yet somehow?"
            n 4fsqgtltsb "I'd still prefer that to being stuck here with the likes of{w=0.5}{nw}"
            extend 1fsqwrltse " {b}YOU{/b}!"

        if Natsuki.isRuined():
            $ chosen_insult = jn_utils.getRandomInsult()
            n 2fcsfultse "{i}[chosen_insult].{/i}"

    return

# Prompt Natsuki to play a game of Blackjack!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_blackjack",
            unlocked=True,
            prompt="Do you want to play Blackjack?",
            conditional="persistent._jn_blackjack_unlocked",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_blackjack:
    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 2ccsbgl "Duh!{w=0.75}{nw}"
        extend 4fchgnl " Of course I wanna play with you,{w=0.2} [chosen_tease]!{w=0.75}{nw}"
        extend 4fchsml " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 2ccssml "Blackjack again,{w=0.2} huh?"
        n 2fsqsml "Ehehe.{w=0.75}{nw}"
        extend 4fnmbgl " You bet I do,{w=0.2} [player]!"

    else:
        n 2unmss "You wanna play blackjack again?{w=0.75}{nw}"
        extend 2fchbg " Sure thing,{w=0.2} [player]!"

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_card_pack":
        n 7csqbg "Just as well I didn't pack the cards up yet,{w=0.2} huh?"

    else:
        $ dialogue_choice = random.randint(1, 5)
        if dialogue_choice == 1:
            n 4nchgn "Time to break out the cards!"

        elif dialogue_choice == 2:
            n 4fcssmeme "Just gotta get set up real quick..."

        elif dialogue_choice == 3:
            n 4fcsss "Just give a second here..."

        elif dialogue_choice == 4:
            n 4fchbg "I'll grab the cards!"

        else:
            n 4fdwsm "Let me just set up here..."

        show natsuki 4fcssmeme
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1.5)
        play audio drawer
        $ jnPause(1)
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
        show natsuki 4fchsm
        hide black with Dissolve(1)

    $ get_topic("talk_play_blackjack").shown_count += 1 # Have to increment here manually thanks to jump
    jump blackjack_intro

# Natsuki goes over the rules of blackjack again, for if the player has already heard the explanation pre-game
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_blackjack_rules",
            unlocked=True,
            prompt="Can you go over the rules of Blackjack again?",
            conditional="persistent._jn_blackjack_unlocked and persistent._jn_blackjack_explanation_given",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_blackjack_rules:
    if Natsuki.isLove(higher=True):
        n 2tllss "Need a little refresher,{w=0.5}{nw}"
        extend 2tnmbo " huh [player]?"
        n 7tlrsl "..."
        n 7tlraj "Well...{w=1}{nw}"
        extend 7tlrss " I guess I can't be too surprised,{w=0.75}{nw}" 
        extend 7tsqss " knowing you."
        n 6ccssslsbr "A-{w=0.2}all too hard to pay attention with such a pretty face,{w=0.2} right?{w=0.75}{nw}"
        extend 3csldvlsbr " Ehehe."
        n 4ccsbglsbr "...A-{w=0.2}anyway."

    elif Natsuki.isEnamored(higher=True):
        n 1ccsbg "Oh?"
        n 1flrbg "Someone needs a reminder already,{w=0.5}{nw}" 
        extend 1fsqss " huh?"
        n 1fsqsm "..."
        n 1fchsm "Ahaha.{w=0.75}{nw}"
        extend 1nlrbg " Nah,{w=0.2} it's fine.{w=0.75}{nw}"
        extend 1unmbo " I don't mind going through it again."
        n 1fsqbg "...So long as you keep your ears pricked {i}this{/i} time,{w=0.2} at least.{w=0.75}{nw}"
        extend 1fsqsm " Ehehe."

    else:
        n 1ccsss "Heh.{w=0.75}{nw}"
        extend 1nsqsl " Wow,{w=0.2} [player]."
        n 4nsgfl "You seriously forgot{w=0.5}{nw}"
        extend 4csqfl " already?"
        n 2csqbo "..."
        n 2fcssm "Ehehe."
        n 1tlrss "Nah,{w=0.5}{nw}"
        extend 3clrss " It's fine."
        n 7ccsbg "I can't expect {i}everyone{/i} to have memory as good as mine,{w=0.5}{nw}" 
        extend 7fcssmesm " after all."

    $ get_topic("talk_remind_blackjack_rules").shown_count += 1 # Have to increment manually here thanks to jump
    jump blackjack_explanation

# Natsuki isn't a fan of shaving!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_shaving",
            unlocked=True,
            prompt="Shaving",
            category=["Wind-ups", "Fashion"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_shaving:
    $ already_discussed_shaving = get_topic("talk_windup_shaving").shown_count > 0
    if already_discussed_shaving:
        n  "..."
        n  "I mean,{w=0.5}{nw}"
        extend  " I know I said it isn't exactly something I've really gotta deal with here.{w=0.75}{nw}"
        extend  " F-{w=0.2}for now,{w=0.2} anyway."
        n  "But I still can't get over how much of a relief it is not having to think about shaving anymore."
        n  "..."
        n  "H-{w=0.2}hey!{w=0.75}{nw}"
        extend  " Don't give me that look,{w=0.2} [player]!{w=0.75}{nw}"
        extend  " You know perfectly well what I'm talking about,{w=0.2} just like before.{w=0.75}{nw}"
        extend  " It's the {i}worst{/i}!"
        n  "First off,{w=0.5}{nw}"

    else:
        n  "..."
        n  "Tch!"
        n  "...Ugh."
        n  "Man.{w=0.75}{nw}" 
        extend  " I totally forgot about how much that got on my nerves."
        n  "You know what I {i}really{/i} can't stand,{w=0.2} [player]?{w=0.75}{nw}"
        extend  " B-before I got stuck here,{w=0.2} I mean."
        n  "..."
        n  "...Shaving."
        n  "..."
        n  "...Yeah.{w=0.75}{nw}"
        extend  " You know exactly what I'm talking about.{w=0.75}{nw}"
        extend  " I can practically see it on your face."
        n  "Seriously,{w=0.2} [player] -{w=0.5}{nw}"
        extend  " it's actually the worst!{w=0.75}{nw}"
        extend  " I can't stand it!"
        n  "It's like every part of it all is practically {i}designed{/i} to piss you off!"
        n  "Yeah.{w=0.75}{nw}"
        extend  " You better be sitting comfortably,{w=0.2} [player].{w=0.75}{nw}"
        extend  " 'Cause I've got a real bucket list to go off on this one."
        n  "So first off,{w=0.5}{nw}"

    extend  " let's give a {i}huge{/i} round of applause to everybody's favorite pain in the backside:{w=0.75}{nw}"
    extend  " the human body!"
    n  "I don't know about you,{w=0.2} [player].{w=0.75}{nw}" 
    extend  " But depending on how fast your hair grows?{w=0.75}{nw}"
    extend  " You're gonna be looking at anywhere from days to hours between shaves."
    n  "Of course!{w=0.75}{nw}"
    extend  " Because nobody{w=0.5}{nw}" 
    extend  " {i}ever{/i}{w=0.5}{nw}"
    extend  " had anything better to do in the morning than blow a bunch of time obsessing over how {i}silky smooth{/i} their features are,{w=0.5}{nw}"
    extend  " right?"
    n  "And don't even get me started on how counter-intuitive it all is either."
    n  "Go too slow?"
    extend  " Go too fast?{w=0.75}{nw}"
    extend  " Just {i}look{/i} at your razor the wrong way?"
    n  "Surprise!{w=0.75}{nw}"
    extend  " Hope you stocked up on band-aids.{w=0.75}{nw}"
    extend  " 'Cause you know what you're gonna be doing for the next ten minutes."
    n  "I mean,{w=0.2} seriously -{w=0.5}{nw}"
    extend  " It isn't even like you gotta worry about that for the hair on your head.{w=0.75}{nw}"
    extend  " Why does it {i}have{/i} to be so different for hair anywhere else?"
    n  "Cut me a break."

    n  "Oh -{w=0.5}{nw}" 
    extend  " and did I mention just how much you have to pay for the privilege?{w=0.75}{nw}"
    extend  " It doesn't even matter what you use!"
    n  "Those razors with the replaceable bits on the end?{w=0.75}{nw}"
    extend  " Hope you enjoy squeezing as much out of each one as you can to save on the refills!"
    n  "Going disposable?{w=0.75}{nw}"
    extend  " Yeah,{w=0.2} because I{w=0.5}{nw}" 
    extend  "{i}totally{/i}{w=0.5}{nw}"
    extend  " enjoy emptying the trash just like how they're emptying my bank account."
    n  "...Not."
    n  "Even the stupid fancy electric ones don't help!{w=0.75}{nw}"
    extend  " they're even {i}more{/i} expensive than everything else!{w=0.75}{nw}"
    extend  " And we all know just how much fun it is having {i}another{/i} thing that keeps running out of juice."
    n  "'Our closest shave ever!'.{w=0.75}{nw}"
    extend  " Yeah,{w=0.2} right.{w=0.75}{nw}"
    extend  " More like shaving away all your savings."

    n  "Heh.{w=0.75}{nw}"
    extend  " And whatever you buy?{w=0.75}{nw}" 
    extend  " It never feels like you'll even get the kind of shave you wanted in the first place."
    n  "Yeah,{w=0.2} yeah.{w=0.75}{nw}"
    extend  " Say whatever you want,{w=0.2} [player].{w=0.75}{nw}"
    extend  " I've heard it all before."
    n  "'You just gotta let your skin soak,{w=0.2} Natsuki!.'{w=0.75}{nw}"
    extend  " 'It's easy!{w=0.2} Just follow the grain!.'{w=0.75}{nw}"
    extend  " 'Don't forget to lather up every time!.'{w=0.75}{nw}"
    extend  " You think I haven't {i}tried{/i} that already?!"
    n  "Like...{w=1}{nw}"
    extend  " Come {w=0.5}{nw}{i}on{/i}!{w=0.75}{nw}"
    extend  " Is this meant to be a morning routine?{w=1}{nw}" 
    extend  " Or some kind of cult ritual?"
    n  "At least a ritual doesn't leave your legs looking like a war zone either."
    n  "Ugh..."

    if already_discussed_shaving:
        n  "..."
        n  "...Look.{w=0.75}{nw}"
        extend  " I'm not gonna go all out and work myself up about all this.{w=0.75}{nw}"
        extend  " Again."
        n  "Not like just complaining about something ever achieved anything anyway."
        
    else:
        n  "You'd think something practically everybody's had to deal with for so long would actually be {i}solved{/i} by now,{w=0.5}{nw}"
        extend  " right?"
        n  "..." # sigh
        n  "..." # grump
        n  "Alright,{w=0.2} look.{w=0.75}{nw}"
        extend  " I've already gone on about this long enough.{w=0.75}{nw}"
        extend  " And I really don't want shaving of all things living rent-free in my head again."

    n  "So...{w=1}{nw}" 
    extend  " I'm just gonna say this."

    $ chosen_descriptor = "babe" if Natsuki.isLove(higher=True) else player
    if already_discussed_shaving:
        n  "Like I said before.{w=0.75}{nw}"
        extend  " I don't really care or anything if you shave or not,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"

    else:
        n  "I don't particularly care or anything if you shave or not,{w=0.2} [chosen_descriptor].{w=0.75}{nw}"

    extend  " T-{w=0.2}that's your call,{w=0.2} obviously.{w=0.75}{nw}"
    extend  " I'm not gonna think any less of someone not wanting to go through all of...{w=1}{nw}"
    extend  " That."
    n  "..."
    n  "But...{w=1}{nw}"
    extend  " If you {i}do{/i} somehow have some kind of magical morning routine that {i}actually{/i} works for you?"
    n  "...Heh."
    n  "Then I hope you know just who you have to share it with first.{w=0.75}{nw}"
    extend  " T-{w=0.2}that's all I'm saying!"

    # Tease about sharing approach with Nat
    if Natsuki.isLove(higher=True):
        n  "And besides,{w=0.2} [player].{w=0.75}{nw}"
        extend  " I-{w=0.2}isn't that just what couples do?"
        n  "Ehehe."
        n  "L-{w=0.2}love you too,{w=0.2} [player]!"

    elif Natsuki.isEnamored(higher=True):
        n  "A-{w=0.2}and besides,{w=0.2} [player].{w=0.75}{nw}"
        extend  " You know what they say."
        n  "Sharing is caring,{w=0.2} right?"
        $ chosen_tease = jn_utils.getRandomTeaseName()
        n  "Thanks a bunch,{w=0.2} you big [chosen_tease]!"

    elif Natsuki.isAffectionate(higher=True):
        n  "And besides,{w=0.2} [player].{w=0.75}{nw}"
        extend  " If you don't?{w=1}{nw}"
        extend  " Well..."
        n  "Let's just say I'll show you a {i}real{/i} close shave instead."
        n  "Ehehe."
        n  "'Preciated,{w=0.2} [player]!"

    else:
        n  "Ehehe."
        n  "Thanks a bunch,{w=0.2} [player]!~"

    return
