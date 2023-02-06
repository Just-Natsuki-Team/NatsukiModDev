default persistent._admission_database = dict()

# Retain the last admission made on quitting the game, so Natsuki can react on boot
default persistent.jn_player_admission_type_on_quit = None

init 0 python in jn_admissions:
    import random
    import store

    ADMISSION_MAP = dict()

    # Admission types
    TYPE_ANGRY = 0
    TYPE_ANXIOUS = 1
    TYPE_ASHAMED = 2
    TYPE_BORED = 3
    TYPE_CONFIDENT = 4
    TYPE_EXCITED = 5
    TYPE_HAPPY = 6
    TYPE_HUNGRY = 7
    TYPE_INSECURE = 8
    TYPE_PROUD = 9
    TYPE_SAD = 10
    TYPE_SICK = 11
    TYPE_TIRED = 12

    # The last admission the player gave to Natsuki
    last_admission_type = None

    def get_all_admissions():
        """
        Gets all admission topics which are available

        OUT:
            List<Topic> of admissions which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            ADMISSION_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_admissions_start:
    python:
        admission_menu_items = [
            (_admission.prompt, _admission.label)
            for _admission in jn_admissions.get_all_admissions()
        ]
        admission_menu_items.sort()

    call screen scrollable_choice_menu(admission_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Angry",
            label="admission_angry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_angry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY:
        n 1kcsemesi "Jeez,{w=0.2} [player]...{w=1}{nw}"
        extend 2ksqposbl " you're really still all worked up?"
        n 2fnmpo "...Did you actually {i}go{/i} spend some time outside,{w=0.2} like I said?"
        n 2klrsl "..."
        n 4klrsssbl "I honestly don't know what else I can suggest,{w=0.75}{nw}" 
        extend 4knmbosbl " really."
        n 1fcsflsbl "Just...{w=1}{nw}" 
        extend 1fnmajsbl " try and stay calm,{w=0.75}{nw}"
        extend 2fcscasbl " and think things through {i}properly{/i}."
        n 2knmca "Alright?"
        n 1kllsl "The last thing anyone needs is you storming off and getting hurt,{w=0.75}{nw}" 
        extend 4kllfl " or doing something..."
        n 4kslsr "...that you can't easily take back."
        n 2ncsaj "Trust me.{w=0.75}{nw}"
        extend 2tnmfl " Doing stuff in anger,{w=0.2} because you let it all get to you?{w=0.75}{nw}"
        extend 2fcssl " It {i}never{/i} turns out better that way."
        n 2kslsl "I should know."
        n 1ncsaj "So give yourself some time,{w=0.2} [player].{w=1}{nw}"
        extend 1ullbo " Space too,{w=0.2} if you need it."
        n 4fcsca "{i}Then{/i} just take it as it comes."
        n 4nlrpu "You can at least manage that...{w=0.75}{nw}"
        
        if Natsuki.isEnamored(higher=True):
            extend 4knmpu " right?{w=1}{nw}"
            extend 4knmsslsbl " F-{w=0.2}for me?"
            n 3knmsllsbl "And for yourself,{w=0.75}{nw}"
            extend 3klrbolsbl " if nothing else."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 4fchsmlsbl "You got this,{w=0.2} [chosen_endearment]!{w=0.5}{nw}"
                extend 4fchbgleafsbl " Just like always!"

        else:
            extend 4knmpu " right?"
            n 2fcsbolsbl "You owe yourself that much,{w=0.2} at least."

    else:
        n 4tnmpu "Huh?{w=0.75}{nw}" 
        extend 4knmfl " You're {i}angry{/i}?"
        n 1kllan "Yeesh...{w=0.75}{nw}" 
        extend 2knmaj " what's got you so worked up?{w=0.75}{nw}" 
        extend 2fcsgs " That's no good at all,{w=0.2} [player]!"
        n 2fcsflsbl "I-{w=0.2}I know it's probably ironic coming from me,{w=0.75}{nw}" 
        extend 4fcstr " but let's just cool things down a little.{w=0.5}{nw}"
        extend 4knmca " 'Kay?"
        n 1fcsaj "Just being mad never solved anything,{w=0.2} so let's focus."
        n 2ncsfl "Alright.{w=0.75}{nw}"
        extend 2nlrfl " Now,{w=0.2} what would {i}I{/i} do if something -{w=0.5}{nw}" 
        extend 2fsrca " or someone -{w=0.5}{nw}" 
        extend 4tnmsl " {i}really{/i} got on my nerves?"
        n 1tllaj "Personally if I get all hot-headed,{w=0.75}{nw}" 
        extend 3fcsss " I like to take a walk.{w=0.75}{nw}"
        extend 3unmaj " You know -{w=0.5}{nw}"
        extend 3nlrbo " distance myself from the problem." 
        n 4fcscs "It worked for me back in the club,{w=0.2} after all."
        n 3fcsbg "It's actually pretty amazing what some fresh air and a little power-walk can do!"
        n 3ulraj "So...{w=1}{nw}"
        extend 1tnmbo " why not give that a try first,{w=0.2} [player]?"
        n 4nsrsssbr "Even if it {i}isn't{/i} a super massive help with how you're feeling..."
        n 2fcsbgsbr "A little exercise never hurt anyone either!{w=0.75}{nw}"
        extend 4fchsmsbr " Ehehe."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANGRY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Anxious",
            label="admission_anxious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_anxious:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANXIOUS:
        n 4knmpu "You're still feeling anxious,{w=0.2} [player]?"
        n 1nsrun "Uuuuuuuu..."
        n 2ksrflsbr "I'm really {w=0.3}{i}not{/i}{w=0.3} the best person for this sort of thing..."
        n 2knmbosbr "But perhaps you could try some distractions to keep your mind off whatever it is?"
        n 4kllsssbr "You could pick up a series you haven't finished,{w=0.75}{nw}" 
        extend 4tllbosbr " or continue a hobby or something."
        n 1fslunsbl "Nnnnnn...{w=0.75}{nw}" 
        extend 4kslemsbl " what else..."
        n 1unmajesu "Oh!{w=0.5}{nw}" 
        extend 3fcspo " Try to avoid soda,{w=0.2} coffee and things like that too."
        n 3flrca "I mean,{w=0.75}{nw}"
        extend 1fsrss " they aren't great for you anyway.{w=1}{nw}"
        extend 4nsrslsbl " But I think loading up on caffeine and sugar is the {i}last{/i} thing you need right now."
        n 4tnmbo "Besides that,{w=0.5}{nw}" 
        extend 1kllss " I usually find listening to music works for me.{w=0.75}{nw}"
        extend 4unmaj " But don't feel like you have to do whatever I find helps -{w=0.5}{nw}"
        extend 3fchbgsbr " you should totally do whatever {i}you{/i} usually find comforting!"
        n 3unmbo "You don't have to push the boat out or anything:{w=0.5}{nw}"
        extend 4ullfl " a favourite game,{w=0.5}{nw}"
        extend 2nsrsm " some dumb old manga series...{w=1}{nw}"
        extend 2fchbg " whatever keeps that noggin of yours busy!"
        n 4fsqcs "...And if nothing else comes to mind?"
        n 4fchgn "You could always get stuck into some good old busywork!"
        n 2uslss "There's {i}always{/i} some kind of chore that needs doing anyway,{w=0.75}{nw}"
        extend 2usqcs " right?"
        n 1fsqsm "Ehehe."
        n 3fcsbs "Don't worry -{w=0.5}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
        extend 3uchgnl " you got this,{w=0.2} [chosen_descriptor]!"

    else:
        n 4tnmpu "Huh?{w=0.75}{nw}"
        extend 4knmfl " You're feeling anxious,{w=0.5}{nw}" 
        extend 4knmbo " [player]?"
        n 1kllsssbl "...What brought this on,{w=0.5}{nw}"
        extend 1knmsssbl " all of a sudden?{w=0.75}{nw}"
        extend 2knmcasbl " You don't have some kind of big thing coming up soon,{w=0.2} do you?"
        n 2ksrslsbl "..."
        n 2ksrsssbr "W-{w=0.2}well,{w=0.75}{nw}"
        extend 4ksrpusbr " I gotta admit.{w=1}{nw}"
        extend 1knmslsbr " I don't really know what kind of advice I can give you this time,{w=0.2} [player]..."
        n 3fcssllsbr "But what I do know is this."
        n 3fcsbol "Everything is gonna be fine." 
        n 4fcsssl "Everything {i}will{/i} work out,{w=0.2} eventually.{w=0.75}{nw}"
        extend 4fchbgl " It always does!"
        n 1fllss "I mean,{w=0.5}{nw}"
        extend 2fslss " it might not always be in the way you {i}expect{/i},{w=0.75}{nw}"
        extend 2tslbo " or even necessarily the way you {i}want{/i}..."
        n 4fnmbo "But getting all stressed out about something won't make it any easier,{w=0.2} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1fchsml "And you know I'll always be here to listen."

        else:
            n 1fcscal "Plus if nothing else,{w=0.2} I'll always be here to listen."

        n 2nlrbo "So...{w=0.75}{nw}" 
        extend 2knmbosbr " try and put your mind at rest,{w=0.2} okay?"
        n 1fcsbol "I-{w=0.2}I know it's tough...{w=0.75}{nw}"
        extend 1kllsll " but just try,{w=0.75}{nw}" 
        extend 4knmsll " alright?"

        if Natsuki.isEnamored(higher=True):
            n 4klrssl "A-{w=0.2}and besides."
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            n 1fchsml "You should know I've {i}always{/i} got your back by now,{w=0.75}{nw}"
            extend 1fchbll " [chosen_descriptor]."
            
            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "Love you,{w=0.2} [player]~!"

            else:
                n 4fchsml "Ehehe."
                $ chosen_tease = jn_utils.getRandomTease()
                n 4fchbgl "Do your best,{w=0.2} [chosen_tease]"
        
        else:
            n 4fcssslsbl "B-{w=0.2}besides..."
            n 2fsqbglsbl "With someone like {i}me{/i} backing you up?{w=0.75}{nw}"
            extend 2fsrdvlsbl " Well..."
            n 3fchbgl "I daresay you've got nothing to worry about,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3fchsmleme " Ehehe."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANXIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Ashamed",
            label="admission_ashamed",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_ashamed:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ASHAMED:
        n 1knmbo "[player]...{w=0.75}{nw}" 
        extend 4ksrslsbl " you aren't {i}seriously{/i} still feeling ashamed of yourself,{w=0.5}{nw}"
        extend 4ksqsrsbl " are you?"
        n 2fcsbo "..."
        n 2fcsfl "Well,{w=0.5}{nw}" 
        extend 1fcsgs " sorry [player] -{w=0.5}{nw}"
        extend 4fchgn " but I'm not giving up on you {i}that{/i} easily!"
        n 3flrss "And hey,{w=0.5}{nw}"
        extend 3fnmbg " newsflash:{w=0.75}{nw}"
        extend 3fsqbg " you're not giving up that easily either!"

        if Natsuki.isEnamored(higher=True):
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()

        else:
            $ chosen_descriptor = player

        n 4fcsbs "Now go put things right,{w=0.2} [chosen_descriptor]!"

        if Natsuki.isEnamored(higher=True):
            n 4fchsml "I believe in you!"
            
        else:
            n 4fwlsm "You better not let me down!"

    else:
        n 1unmem "Huh?{w=1}{nw}" 
        extend 4kcsfl " Wait,{w=0.75}{nw}" 
        extend 4knmfl " what?"
        n 4kllbo "You're feeling...{w=0.75}{nw}" 
        extend 2knmbo " ashamed?{w=0.75}{nw}" 
        extend 2knmflsbr " Of yourself?"
        n 2ksrpu "...Why,{w=0.5} [player]?{w=0.75}{nw}" 
        extend 2fnmpol " You didn't go out and do something {w=0.2}{i}really{/i}{w=0.2} dumb,{w=0.2} did you?"
        n 2fcscal "..."
        n 4fcstrl "Well...{w=0.3} whatever you did,{w=0.5}{nw}" 
        extend 2fcsgsl " I-{w=0.2}I'm sure you didn't mean it!"
        n 3fnmfl "And more importantly,{w=0.5}{nw}" 
        extend 3fcsss " you're going to work your butt off to put things right.{w=0.75}{nw}" 
        extend 3fcssmedz " I just know it!"
        n 4fcsbg "You're gonna step up to the plate,{w=0.2} and that's all there is to it."
        n 2nllaj "So...{w=0.75}{nw}" 
        extend 2fnmca " don't let me down,{w=0.2} got it?"
        n 2fnmaj "And you aren't going to let yourself down either."

        show natsuki 2fnmca
        menu:
            "Right?"

            "Right!":
                n 1fchbs "Exactly!{w=0.5}{nw}"
                extend 4fsqcs " See?{w=0.75}{nw}"
                extend 4fcssmeme " Just like I told you!"

            "...":
                n 1nsqbo "..."
                n 2fcssr "I don't think you get it,{w=0.2} [player]."
                n 2uchgn "...So I guess we gotta do things the hard way!"
                n 4fcsbg "Now,{w=0.5}{nw}" 
                extend 1fnmss " repeat after me:{w=0.5}{nw}" 
                extend 2fcsss " 'I'm not gonna let myself down!'"

                show natsuki 2fcscs
                menu:
                    "I'm not gonna let myself down!":
                        n 2usqcsesm "See?{w=1}{nw}"
                        extend 2fchbg " I {i}knew{/i} you had it in you!{w=0.5}{nw}"
                        extend 2fsqcs " Ehehe."

        n 4fchbg "Now go get 'em,{w=0.2} [player]!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ASHAMED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Bored",
            label="admission_bored",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_bored:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_BORED:
        n 4nslsssbl "Wow...{w=1}{nw}"
        extend 4nslflsbl " I guess you really weren't exaggerating then,{w=0.5}{nw}"
        extend 4tnmbosbl " huh?"
        n 2fsqfl "Did you actually {i}try{/i} doing what I suggested?{w=0.75}{nw}"
        extend 2fcsca " Sheesh..."
        n 1nlrsl "..."
        n 4ulraj "Well,{w=0.75}{nw}"
        extend 3tlraj " if there's really {i}nothing{/i} to for you to do {i}here{/i}..."
        n 3fcsbg "Then why not check out what everyone else is doing for a change?"
        n 4ullbo "Friends,{w=0.5}{nw}"
        extend 4ulraj " family...{w=0.75}{nw}"
        extend 3fsqcs " that colleague you always plan to hang out with...{w=1}{nw}"
        extend 3fcsgs " {i}someone{/i}'s gotta have {i}something{/i} going on,{w=0.2} [player]!"
        n 4fchgn "...So get up off your butt already and find out!{w=0.75}{nw}"
        extend 4ullss " Phone around or something!"
        n 2tnmsl "Or,{w=0.2} you know..."
        n 2tsqsmesm "Pick up that game or book you were {i}totally{/i} gonna check out at some point...?"
        n 2usqcs "..."
        n 2fnmss "What?{w=0.75}{nw}"
        extend 4fcsbg " Called you out yet again,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fsqcs " Ehehe."
        n 2fnmfl "Now come on!{w=0.75}{nw}"
        extend 2fcsbg " There's never a shortage of stuff to do to pass the time.{w=1}{nw}"
        extend 2uchgn " Time for you to get up and go find it!"

        if Natsuki.isAffectionate(higher=True):
            $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
            n 4fwlsm "Off you go,{w=0.2} [chosen_descriptor]!"

            if Natsuki.isLove(higher=True):
                n 1fchsml "Love you~!"

    # Unlock Snap if not already unlocked
    elif not persistent.jn_snap_unlocked:
        $ persistent.jn_snap_unlocked = True
        n 4fcsfl "Wait...{w=0.75}{nw}"
        extend 4tnmpu " you're bored?{w=0.75}{nw}"
        n 1fcsflsbr "H-{w=0.2}hang on for just a second."
        n 2fnmeml "A-{w=0.2}and what are you trying to say,{w=0.2} exactly?!{w=1}{nw}"
        extend 2fnmgsl " Huh?"
        n 2fcsgslsbr "How could you possibly be bored with someone as awesome as me around?"
        n 2fslposbr "Jeez,{w=0.2} [player]..."
        n 4fcsposbl "You make it sound like I'm {i}not{/i} trying to liven things up around here or something."
        n 1nsrposbl "..."
        n 4tsrfl "Though..."
        n 3nlrss "Well,{w=0.2} even I gotta admit.{w=1}{nw}"
        extend 3tnmfl " there isn't {i}exactly{/i} a whole lot going on here.{w=0.75}{nw}"
        extend 3fcscal " Besides me,{w=0.2} I mean."
        n 1fslsl "There's gotta be something else around here."
        n 1nslss "It is...{w=0.75}{nw}"
        extend 2tslpu " was...?{w=0.75}{nw}"
        extend 2tnmbo " A classroom,{w=0.2} right?"
        n 4tlrca "There has to be {i}something{/i} someone left in a desk,{w=0.2} or..."
        n 4unmfleex "...!{w=0.75}{nw}"
        n 4fnmbg "Aha!{w=0.5}{nw}"
        extend 1fchbg " I just remembered!{w=0.75}{nw}"
        extend 1fcssm " Just give me a second here..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio drawer
        show natsuki 4fchgn
        $ jnPause(4)
        hide black with Dissolve(1)

        n 4uchgn "Yes!{w=0.75}{nw}" 
        extend 4fchsmeme " I knew it was still here!"
        n 2fsqcs "Betcha' didn't know I had playing cards stashed away,{w=0.2} huh?"
        n 2fchbl "Turns out these desk drawers {i}are{/i} handy,{w=0.2} after all!{w=1}{nw}"
        extend 2fcssm " And you {i}always{/i} gotta have something prepared for a rainy day at school."
        n 4nllss "I...{w=0.75}{nw}"
        extend 1nsrca " don't exactly know a whole lot of card games...{w=0.75}{nw}"
        extend 1fsrpo " yet."
        n 3fsqss "But I'll tell you one thing,{w=0.2} [player]."
        n 3fchbs "I've got a mean hand at Snap!{w=0.75}{nw}"
        extend 4fsqbs " And I am just {i}itching{/i} to prove it right now."
        n 2fsqss "So..."
        n 2tnmsm "What about it then,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2tsqsm " Care to test your mettle?"

        show natsuki 2fsqcs
        menu:
            n  "Not like you have any excuse not to,{w=0.2} right?"

            "Sure,{w=0.2} why not?":
                jump snap_intro

            "Not right now.":
                n 4usqct "Oh?{w=0.75}{nw}"
                extend 4tsqsm " Not right now,{w=0.2} you say?"
                n 3ullss "Fine,{w=0.2} fine.{w=0.75}{nw}"
                extend 3fcsbg " That's cool with me."
                n 3uchgn "Just means I get to look forward to kicking your butt later instead!{w=0.75}{nw}"
                extend 4nchgn " Ehehe."

                show natsuki 1fchsmeme
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(2)
                play audio drawer
                $ jnPause(4)
                hide black with Dissolve(1)

    else:
        n 1tnmfl "Huh?{w=0.75}{nw}" 
        extend 4tnmpu " You're bored?"
        n 2fnmgsl "A-{w=0.2}and just what is {i}that{/i} supposed to mean,{w=0.2} [player]?!"
        n 2flreml "Am I boring?{w=0.75}{nw}"
        extend 4fcsgsl " Huh?{w=1}{nw}"
        extend 4fnmfll " Am I not fun enough to be with?"
        n 4fbkwrl "Are you not entertained?!"
        n 2fsqpol "..."
        n 2fsqdvl "..."
        n 1fcsajl "Oh,{w=0.5}{nw}"
        extend 4uchgnl " lighten up a little,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4flrss " Man..."
        n 3fcsbg "But really,{w=0.2} come on!{w=0.75}{nw}"
        extend 3tnmfl " If you're seriously bored enough to tell me about it..."
        n 4fchbg "Then get up off your butt and do something,{w=0.2} you dork!{w=0.75}{nw}"
        extend 2tsqss " You {i}do{/i} have a world beyond this screen,{w=0.2} you know!{w=0.75}{nw}"
        extend 2fcspolsbl " T-{w=0.2}that's a lot more than {i}I've{/i} got!"
        n 2tllss "And if {i}that{/i} isn't enough,{w=0.75}{nw}" 
        extend 4fchbgedz " there's an even {i}bigger{/i} one right at your fingertips!"
        n 3fcsbg "Now if {i}those{/i} aren't some prime opportunities to beat the boredom right there..."
        n 3fchbg "Then I don't know what is!{w=0.75}{nw}"
        extend 1fchsm " Ehehe."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 1fnmbg "Now stop complaining and get a move on,{w=0.2} [chosen_descriptor]!"
        n 2fsqbl "Time's wasting!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_BORED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Confident",
            label="admission_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_confident:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_CONFIDENT:
        n 2nchsm "Ahaha.{w=0.75}{nw}"
        extend 4tsqcs " Still full of confidence,{w=0.2} I see!"

        if Natsuki.isEnamored(higher=True):
            n 4ullaj "Not like it's any big surprise or anything like that,{w=0.2} though.{w=0.75}{nw}"
            extend 1ullbo " I mean..."
            n 2fchbgl "I like to think you've got a bunch to be confident about!"

        else:
            n 4fsqcs "...And I wonder who you have to thank for that?"

        n 2fcssm "Ehehe."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 2fchbl "You're welcome,{w=0.2} [chosen_descriptor]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 2fcssmeme "Ehehe.{w=0.75}{nw}"
        extend 2tnmbg " See,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fchbgsbr " I {i}knew{/i} you'd snap out of it eventually!"

        if Natsuki.isEnamored(higher=True):
            n 3nllpu "But...{w=0.75}{nw}"
            extend 3tnmsl " in all seriousness?"
            n 4nlrpul "I'm just...{w=0.75}{nw}" 
            extend 1ksrsll " really glad to know you're better now,{w=0.2} [player]."
            n 2fcssml "That's all that matters."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 4kchsmleafsbl "L-{w=0.2}love you,{w=0.2} [chosen_endearment]."

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsfllsbr "N-{w=0.2}not that I care {i}that{/i} much, o-{w=0.2}of course!"
            n 2nlrbolsbr "But...{w=0.75}{nw}" 
            extend 4ncsajl " I'm glad to know you're okay now,{w=0.2} [player]." 
            n 2fcscaesi "That's what matters."
            n 2kslca "..."

        else:
            n 2tsqcs "No guessing who you have to thank,{w=0.2} huh?{w=0.75}{nw}"
            extend 1fsqsm " Ehehe."
            n 4fcsbgedz "You're welcome!"

    else:
        n 2tsqct "Oh?{w=0.75}{nw}"
        extend 2tsqbg " Feeling confident today,{w=0.75}{nw}"
        extend 2tsqcs " huh?"
        n 4fchbg "Well,{w=0.2} more power to you!"
        n 1fcssmesm "It's never a bad thing to have more confidence in yourself.{w=0.75}{nw}"
        extend 1ullss " I mean...{w=1}{nw}"
        extend 3fchgn " look at me!"
        n 3unmaj "Don't get me wrong though -{w=0.5}{nw}"
        extend 4nlrss " I'm not saying it's always {i}easy{/i},{w=0.75}{nw}"
        extend 4nlrsl " obviously."
        n 1tnmsl "Especially if you messed up or something,{w=0.75}{nw}"
        extend 1tslss " or if you aren't feeling great."
        n 4tnmss "But hey!{w=0.75}{nw}"
        extend 2tsqsm " If that's how you're feeling?{w=0.75}{nw}"
        extend 2fchbg " Well,{w=0.2} I'm not gonna rob it from you!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Excited",
            label="admission_excited",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_excited:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_EXCITED:
        n 2fllss "Man...{w=0.75}{nw}"
        extend 2tsqss " you must {i}really{/i} be pumped if you're still going on about it,{w=0.5}{nw}"
        extend 2tsqcs " huh?"
        n 4fchsm "Ehehe."
        n 3fchbg "Good on you,{w=0.2} [player]!"

    else:
        n 4fspgs "Oh!{w=0.5} Oh!{w=0.75}{nw}"
        extend 4unmbg " Did something happen?{w=0.75}{nw}"
        extend 4fnmtr " Is something gonna happen?"
        n 4fnmca "..."
        n 2tnmaj "Well?"
        n 3fnmgs "Come on,{w=0.2} [player]!{w=0.75}{nw}"
        extend 3fnmfl " Spill the beans!{w=0.75}{nw}"
        extend 4fbkwr " You gotta tell me!"
        n 2fsqpo "Don't tell me you're just gonna hog all the news to yourself..."
        n 2fsqcs "..."
        n 2fchsm "Ehehe.{w=0.5}{nw}"
        extend 4fllss " Nah,{w=0.2} it's fine.{w=0.75}{nw}"
        extend 2fcsbg " Glad to hear you've got stuff to look forward to!{w=0.75}{nw}"
        extend 2flrss " Well..."
        n 2fcsssedz "Besides seeing yours truly,{w=0.2} {i}obviously{/i}.{w=0.75}{nw}"
        extend 1fchsmeme " Ehehe."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_EXCITED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Happy",
            label="admission_happy",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_happy:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HAPPY:
        n 3nlraj "Wow...{w=0.75}{nw}" 
        extend 3unmaj " it's all just sunshine and rainbows with you today,{w=0.2} isn't it?"
        n 4fsqsm "Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 2uchgn "Keep up the smiles,{w=0.2} [player]!"

        else:
            n 2fchbg "Good on you,{w=0.2} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 2tnmsl "...Feeling better now,{w=0.2} [player]?"
        n 2kllbo "..."
        n 4kllpu "I'll admit.{w=1}{nw}"
        extend 4nslsll " I was getting kinda worried.{w=1}{nw}"
        extend 2kslcal " I hate seeing my friends getting all upset."
        n 2ncscal "Life is just way too short for all that."

        if Natsuki.isEnamored(higher=True):
            n 2knmbolsbl "And you deserve to be happy too,{w=0.2} you know."
            n 2ncssll "Remember that."
            n 2ksrbol "..."
            n 2nsrajl "S-{w=0.2}so...{w=0.75}{nw}" 
            extend 4tnmsllsbl " where were we?"

        else:
            n 2nslsll "Everyone deserves to at least be happy,{w=0.2} after all."
            n 2flrbolsbl "N-{w=0.2}now let's just get back to it already."
            n 2ksrbolsbl "..."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4tnmsl "Feeling better,{w=0.2} [player]?{w=0.75}{nw}" 
        extend 4fnmfl " I'm not surprised!"
        n 2fcstr "You just aren't yourself when you're hungry."
        n 2nslss "Trust me...{w=0.75}{nw}" 
        extend 1nslslsbr " I would know."
        n 2fcsaj "Just don't let it get {i}that{/i} bad next time!"
        n 2fsqfl "...Or I really will give you a mouthful.{w=1}{nw}"
        extend 1fsqsm " Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3nchgnl "Love you,{w=0.2} [chosen_tease]~!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1fcssm "Ehehe.{w=0.75}{nw}"
        extend 2fwlbg " Glad to see you're back in action, [player]!"
        n 2ullaj "It's kinda funny,{w=0.2} actually."
        n 2tnmfl "Nothing makes you appreciate feeling normal more than being sick,{w=0.2} huh?"
        n 4fchgn "I guess you'd know that a whole lot better now!"

        if Natsuki.isLove(higher=True):
            n 4fchblleaf "Love you too,{w=0.2} [player]!"

    else:
        n 4tnmss "Oh?{w=0.75}{nw}" 
        extend 4usqsm " Someone's in a good mood today!"
        n 3fcsbgedz "Is a certain {i}someone{/i} being around helping,{w=0.2} I wonder?"
        n 3fsqsmeme "Ehehe."
        n 4fchbg "Good for you,{w=0.2} [player]!"

        if Natsuki.isEnamored(higher=True):
            n 2fcssmesm "If you're happy,{w=0.2} I'm happy!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HAPPY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Hungry",
            label="admission_hungry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_hungry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4fcsfl "...Wait.{w=1}{nw}"
        extend 4tsqpu " What?{w=0.75}{nw}"
        extend 2tnmfl " You're {i}still{/i} hungry?"
        n 2fsqfl "...Or did you seriously not get something when I told you to earlier?"
        n 1fcsfl "Either way,{w=0.75}{nw}"
        
        if Natsuki.isEnamored(higher=True):
            extend 2fchgn " I'm not your babysitter!{w=0.75}{nw}"
            extend 2fsrdvlsbl " E-{w=0.2}even if you {i}wish{/i} I was!"

        else:
            extend 2fchgn " I'm not your babysitter!"

        n 2fcsaj "Now get off that butt of yours and sort something out already!{w=1}{nw}"
        extend 2flrss " Yeesh..."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 4fcsbg "Just keep it healthy,{w=0.2} [chosen_descriptor]!"

        if Natsuki.isAffectionate(higher=True):
            n 4fsqbg "Someone's gotta make sure you're staying in tip-top shape,{w=0.2} after all.{w=0.5}"
            extend 2fchsmleme " Ehehe."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 2knmbo "...[player]."
        n 2ncssl "I...{w=1}{nw}" 
        extend 4knmca " get if you're hungry,{w=0.2} okay?{w=0.75}{nw}"
        extend 4knmaj " Really.{w=1}{nw}"
        extend 1fcssl " Everybody's gotta eat."
        n 1kllfl "Just..."
        n 1kslbo "..."
        n 4ncsbo "Don't use food or snacks as a way to feel better if you're feeling down.{w=1}{nw}"
        extend 4ksqbol " Alright?"
        n 2unmeml "I-{w=0.2}I'm not trying to parent you or anything!{w=0.5}{nw}"
        extend 2fcspol " Of course not.{w=0.75}{nw}"
        extend 2ksrsll " But I'd be a pretty crappy friend if I didn't at least say {i}something{/i} about it."
        n 1ncspu "So please.{w=0.75}{nw}"
        extend 4ksqca " Just don't overdo it."
        n 3nlrsl "A treat is fine,{w=0.2} and it might help you feel better."
        extend 3nsrpu " I can get that."
        n 3ksqbo "But it's not gonna fix what made you feel that way in the first place."
        
        if Natsuki.isEnamored(higher=True):
            n 4klrbol "And you know you can come talk to me if you really need to...{w=1}{nw}"
            extend 4knmbol " right?"

        elif Natsuki.isAffectionate(higher=True):
            n 4fcsbol "A-{w=0.2}and you can always come talk to me,{w=0.2} you know."
            n 4ksrcal "..."

        else:
            n 4ksrbo "...Enjoy your meal,{w=0.2} [player]."

    else:
        n 4tnmpu "Huh?{w=0.75}{nw}" 
        extend 4tsqem " You're {i}hungry{/i}?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 2tnmfl "...Then what're you telling {i}me{/i} for?{w=0.75}{nw}" 
        extend 2fchgn " Go get something to eat,{w=0.2} you big dope!"
        
        if Natsuki.isEnamored(higher=True):
            n 1fcsaj "Honestly...{w=0.75}{nw}"
            extend 2tsqss " what am I gonna do with you,{w=0.2} huh?"

        else:
            n 1fcsaj "Honestly...{w=0.75}{nw}"
            extend 2fllfl " what am I,{w=0.5}{nw}"
            extend 2fsqpo " your mom or something?"
            n 2nsrfl "Jeez..."

        n 1fcsaj "Now go make something already!"
        n 4nsrslsbr "...And no,{w=0.2} [player],{w=0.75}"
        extend 4nsqsl " before you ask."
        n 3fcsbg "Junk food doesn't count!"

        if Natsuki.isAffectionate(higher=True):
            n 3fsqsm "You weren't a trash can last time I checked.{w=0.75}{nw}"
            extend 3fchgnelg " So no garbage for you~!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HUNGRY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Insecure",
            label="admission_insecure",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_insecure:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 2knmbosbr "You're {i}still{/i} feeling all beat up about that,{w=0.2} [player]?"
        n 2klrbosbr "..."
        n 2nlrfl "You...{w=0.75}{nw}" 
        extend 2fnmbol " do remember what I said though,{w=0.2} right?"
        n 1fcsfl "Everybody has their own pace.{w=0.75}{nw}"
        extend 4fcsca " You are no exception.{w=0.75}{nw}"
        extend 2tnmaj " And honestly?"
        n 2fcsbo "I don't really care what it is.{w=1}{nw}"

        if Natsuki.isEnamored(higher=True):
            extend 2tnmbol " So long as we're together?"

        else:
            extend 2tnmfl " So long as we're friends?"

        n 2fcstrl "We'll just have to find it together."
        n 1nllcal "..."
        n 4nsleml "...Man,{w=0.75}{nw}"
        extend 4fslsslsbr " that was corny.{w=0.75}{nw}"
        extend 1fnmpu " But seriously,{w=0.2} [player]."
        n 3fchbgsbr "Don't sweat it!"
        n 3fcsbgsbr "Besides..."
        n 3fsrcs "When someone like {i}me{/i} has your back?"
        n 4fcsbgledz "I daresay you've got nothing to worry about!{w=0.75}"
        extend 1nchgnl "Ehehe."

        if Natsuki.isLove(higher=True):
            n 1fchsmleaf "Love you,{w=0.2} [player]~!"

    else:
        n 1fcsfl "...Wait,{w=0.5}{nw}" 
        extend 2knmpu " what?"
        n 2tnmbo "You're feeling insecure?"
        n 1knmslsbr "...What brought this on all of a sudden,{w=0.2} [player]?"
        n 4ncspu "..."
        n 4ncsaj "I...{w=0.75}{nw}" 
        extend 4klrsl " can't really comment on what made you feel that way.{w=1}{nw}"
        extend 1ksrbo " And I'm not gonna pretend I can."
        n 2fnmbol "But you better listen here,{w=0.2} [player] -{w=0.75}{nw}" 
        extend 2fsqbol " and listen good."
        n 2fcseml "I don't care if you think people don't like you.{w=0.75}{nw}" 
        extend 2fnmbolsbr " {i}I{/i} like you."
        n 4flrfll "I don't care if think you have no talents.{w=0.75}{nw}" 
        extend 1fcscalesi " {i}I{/i} know you do."
        n 1fcstrl "I don't care if people think you're falling behind.{w=0.75}{nw}" 
        extend 2fnmsll " {i}I{/i} know you'll catch up."
        n 2fcsajl "Just..." 
        n 2kslbol "..."
        n 4kcsfll "Give yourself time and space,{w=0.2} [player].{w=0.75}{nw}"
        extend 4knmbol " Alright?"

        if Natsuki.isEnamored(higher=True):
            n 1knmbol "I get how you're feeling.{w=0.75}{nw}"
            extend 2knmpul " I really do.{w=1}{nw}"
            extend 2ksqsfl " I've {i}been{/i} there."

        else:
            n 2fcsbol "I get how crappy you're probably feeling right now."

        n 2fcstrl "And I'm not gonna let a friend keep feeling that way without a fight.{w=0.75}{nw}"
        extend 2fnmtrl " But you need to put in some effort too."
        n 4fllfll "You can do that...{w=0.75}{nw}"

        show natsuki 4knmbol
        menu:
            extend " right?"

            "Right.":
                n 1fcsbo "...Good.{w=0.75}{nw}" 
                extend 4flrfl " Or you'll have me to deal with too.{w=0.75}{nw}"
                extend 4fnmfl " And trust me."
                n 2fsqpo "...You {i}really{/i} don't want that.{w=1}{nw}"
                extend 2flrss " Ahaha."
                n 4klrbo "So..."
                n 2knmsssbr "Did you wanna talk about something else?"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_INSECURE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Proud",
            label="admission_proud",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_proud:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_PROUD:
        n 2nslaj "Wow...{w=1}{nw}"
        extend 2tnmpo " {i}still{/i} in the mood for gloating,{w=0.2} are you?"
        n 4ucsfl "That's fine.{w=0.75}{nw}"
        extend 4ncsfl " That's fine.{w=1}{nw}"
        extend 4nlrfl " So long as you aren't getting too carried away."
        n 1nnmca "Just remember,{w=0.2} [player] -{w=0.5}{nw}"
        extend 3fnmss " if there's one thing I'm good at..."
        n 3fcsbg "...It's knocking people down a peg or two!"
        n 4ullfl "Well...{w=0.5}{nw}"
        extend 2fchgn " when they need it,{w=0.2} anyway.{w=1}{nw}"
        extend 1nchgneme " Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchblleme "Love you too,{w=0.2} [chosen_tease]~!"

    else:
        n 2tnmct "Oh?{w=0.75}{nw}"
        extend 2fsqbg " And what are {i}you{/i} so proud about?{w=1}{nw}" 
        extend 2fnmbg " Huh?"
        n 4fsqsm "Well?"
        n 4fsqbg "Spit it out,{w=0.2} [player]!{w=1}{nw}"
        extend 3fcsbg " It must be pretty amazing,{w=0.2} after all.{w=1}{nw}"
        extend 4fsqss " Right?"
        n 2tsqcs "..."
        n 2fchcs "Ehehe."
        n 4ullaj "Well,{w=0.75}{nw}"
        extend 4tnmbo " whatever it is.{w=0.75}{nw}"
        extend 3fcsbg " You'd have to be pretty smug about it to share it with me!"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 3fchbg "Good job,{w=0.2} [chosen_descriptor]!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_PROUD
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Sad",
            label="admission_sad",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sad:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1knmsl "Oh...{w=0.3} I'm really sorry to hear you're still feeling upset,{w=0.2} [player]."
        n 1kllsl "I'm...{w=0.3} not sure if it's my place to say this,{w=0.2} but..."
        n 1knmpu "Do you have others you can share this with?{w=0.2} Friends,{w=0.2} or family?"
        menu:
            "I do.":
                n 1kllss "Then maybe you should share how you feel."
                n 1kchbg "A problem shared is a problem halved,{w=0.2} as they say!"
                n 1knmsl "But seriously,{w=0.2} [player].{w=0.2} Don't be afraid to ask for help,{w=0.2} alright?"
                n 1klrsl "Everyone needs help sometimes."

            "I don't.":
                n 1ncssf "That's...{w=0.3} not what I was hoping to hear,{w=0.2} honestly."
                n 1kllsr "I'm sorry to hear that,{w=0.2} [player].{w=0.2} Truly."
                n 1nnmpu "But know this."
                n 1knmsr "You've got my support,{w=0.2} okay?"
                n 1klrpol "I-if that helps,{w=0.2} I mean."

            "They already know.":
                n 1kcspu "Good! Good..."
                n 1knmpo "I just hope they were supportive of you,{w=0.2} [player].{w=0.2} You at least deserve that much."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1kchnvf "I love you,{w=0.2} [chosen_endearment]."

        n 1kllpu "I hope you start to feel better soon!"

    else:
        n 1knmpo "Oh...{w=0.3} I'm really sorry to hear you're upset,{w=0.2} [player]."
        n 1knmpu "Did something happen?{w=0.2} You can tell me about it,{w=0.2} [player].{w=0.2} I won't judge."
        n 1ncssr "..."
        n 1nwmpu "It's...{w=0.3} okay,{w=0.2} [player].{w=0.2} Everything is gonna be okay."

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "Now,{w=0.2} take some deep breaths for me,{w=0.2} alright?"
            n 1uchsm "That's it,{w=0.2} [player].{w=0.2} Keep breathing."

        n 1kllpu "Whatever happened,{w=0.2} I'm sure it'll all work out."
        n 1ucssl "What matters is that you're okay,{w=0.2} [player].{w=0.2} So let's concentrate on fixing that, alright?"
        n 1kwmsm "We can work on that here,{w=0.2} okay?"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SAD
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Sick",
            label="admission_sick",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sick:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1knmsl "[player]...{w=0.3} you're still feeling sick?"
        n 1knmbo "How long have you felt like this now?"
        menu:
            "A few hours.":
                n 1kllsr "That's...{w=0.3} not great to hear,{w=0.2} [player]."
                n 1tnmsr "Perhaps you should get some rest soon{w=0.2} -{w=0.2} hopefully you'll feel better."

                if Natsuki.isEnamored(higher=True):
                    n 1knmsl "Let me know if it keeps up,{w=0.2} okay?"

            "A few days.":
                n 1fcssl "[player]."
                n 1fnmca "You need to make sure you see someone soon."
                n 1knmaj "Especially if you start to hurt anywhere,{w=0.2}  or if you've been sick,{w=0.2} or anything like that..."
                n 1knmsl "Try and get extra rest too,{w=0.2} okay?"

            "A week or so.":
                n 1fnmsl "[player]..."
                n 1knmsl "Have you seen anybody about this yet?"

                menu:
                    "Yes, I have.":
                        n 1kllbo "Well...{w=0.3} fine."
                        n 1knmbo "I...{w=0.3} really hope they were able to help you,{w=0.2} [player]."
                        n 1knmpu "Make sure you get some extra rest,{w=0.2} okay?"

                    "No, I haven't.":
                        n 1fnmpu "[player]...{w=0.3} that's no good."
                        n 1knmpo "I trust you know your own limits...{w=0.3} but please,{w=0.2} take care of yourself."
                        n 1klrpol "Your health...{w=0.3} matters to me, you know."

                        # Add pending apology
                        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

            "Longer.":
                n 1knmpo "..."
                n 1kllpo "I...{w=0.3} don't really know what to say to you,{w=0.2} [player]."
                n 1knmpu "I just hope you feel better soon."
                n 1knmsl "Take it easy,{w=0.2} alright?"

                if Natsuki.isAffectionate():
                    n 1kllcal "I hate seeing you unwell like this..."

                elif Natsuki.isEnamored(higher=True):
                    n 1kllsfl "It really hurts me seeing you unwell like this..."

                if Natsuki.isLove(higher=True):
                    n 1kcssff "I love you,{w=0.2} [player].{w=0.2} Please get well soon."

                # Add pending apology
                $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)


    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1ulrsf "You know,{w=0.2} you can start to feel unwell if you haven't eaten for a while,{w=0.2} [player]."
        n 1nnmsf "Have you eaten something today?{w=0.2} Like a proper meal?"
        menu:
            "Yes, I have.":
                n 1tllsl "Huh...{w=0.3} then maybe it was something you ate that's making you feel sick?"
                n 1tnmsl "Go lie down if you need to,{w=0.2} [player].{w=0.2} Alright?"

            "No, I haven't.":
                n 1fskem "T-then obviously you should have something now,{w=0.2} [player]!"
                n 1fllpo "It doesn't have to be some big fancy dish or anything,{w=0.2} you know."
                n 1knmsl "Even something small like some candy or whatever.{w=0.2} Just to get your energy level up."
                n 1kllpo "That's not much to ask,{w=0.2} is it?"

                if Natsuki.isEnamored(higher=True):
                    n 1kllss "Now go get something already, silly! Ahaha..."

    else:
        n 1knmsl "Feeling under the weather,{w=0.2} [player]?"

        if Natsuki.isEnamored(higher=True):
            n 1kllsl "I wish there was something I could do to help..."

        n 1fwmsl "You aren't straining yourself by being here,{w=0.2} are you?"
        n 1klrsl "I don't wanna get in the way of you feeling better."

        if Natsuki.isEnamored(higher=True):
            n 1kwmsll "Your health has to come first over our time together."

        else:
            n 1flrpul "I'm not selfish like that."

        n 1knmpo "So...{w=0.3} promise you'll leave and rest if you have to,{w=0.2} got it?"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1knmssl "I love you,{w=0.2} [chosen_endearment].{w=0.2} I...{w=0.3} really hope you get better soon..."

        elif Natsuki.isAffectionate(higher=True):
            n 1knmbol "I hope you feel better soon,{w=0.2} [player]..."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Tired",
            label="admission_tired",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_tired:
    # Calculate how long the player has been here so far
    $ total_hours_in_session = jn_utils.get_current_session_length().total_seconds() / 3600

    if jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1unmpu "Huh?{w=0.2} You're still tired?"
        n 1fnmpo "Did you not get any rest,{w=0.2} [player]?"
        n 1fllpo "I don't want you getting all cranky..."
        n 1klrsm "So...{w=0.3} go to bed, alright?"
        n 1nchbg "I'll see you later,{w=0.2} [player]!"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1nchsml "Love you,{w=0.2} [chosen_endearment]!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fsqsml "Don't let the bed bugs bite!{w=0.2} Ehehe."

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1tllpu "Well,{w=0.2} you did say you weren't happy earlier,{w=0.2} [player]."
        n 1unmca "If you're already tired,{w=0.2} I think you should sleep on it."
        n 1unmsr "Are you gonna turn in,{w=0.2} [player]?"
        menu:
            "Yes, I will.":
                n 1fcssm "Good...{w=0.3} you'll feel better soon,{w=0.2} okay?"

                if Natsuki.isAffectionate(higher=True):
                    n 1nwmsm "I promise."

                n 1nchbg "Sleep well,{w=0.2} [player]!"

                $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
                return { "quit": None }

            "No, not yet.":
                n 1ulrpo "Well...{w=0.3} if you're sure,{w=0.2} [player]."
                n 1fsgsm "Now,{w=0.2} let's see if I can't improve your mood,{w=0.2} huh?"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1ulrpo "I'm really not surprised if you're already sick,{w=0.2} [player]."
        n 1fnmpo "You should get some rest."
        n 1kllss "We can talk later,{w=0.2} alright?"
        n 1knmsm "Take it easy,{w=0.2} [player]!"

        # Add pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_SICK
        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fskem "I'm not surprised you're feeling tired if you're hungry!"
        n 1kchgn "Stop sitting around and go eat something,{w=0.2} [player]!"
        n 1tnmsl "Just take it easy getting up,{w=0.2} alright?{w=0.2} I don't want you fainting on me."
        n 1klrsf "And trust me,{w=0.2} I don't think you want that either..."

    elif total_hours_in_session >= 24:
        n 1fbkwrl "[player]!"
        n 1kskem "You've been here for like a day now{w=0.2} -{w=0.2} It's no wonder you're tired!"
        n 1fnmpo "You better get some sleep right now!{w=0.2} And I don't wanna see you come back until you've slept!"
        n 1fcspo "Sheesh..."
        n 1knmpo "Now get going,{w=0.2} [player]!{w=0.2} I'll see you later,{w=0.2} 'kay?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 1unmbg "Sleep well,{w=0.2} [chosen_tease]!"

        if Natsuki.isLove(higher=True):
            n 1uchsml "Love you~!"

        elif Natsuki.isAffectionate(higher=True):
            n 1nllsml "Sweet dreams! Ehehe."

        # Add pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        return { "quit": None }

    elif total_hours_in_session >= 12:
        n 1fbkwr "[player]!"
        $ chosen_tease = jn_utils.getRandomTease()
        n 1fnmpo "I'm not surprised you're feeling tired{w=0.2} -{w=0.2} you've been here ages,{w=0.2} [chosen_tease]!"
        n 1fllpo "You need to get some sleep...{w=0.3} you're gonna be all cranky later at this rate!"
        n 1kllpo "I appreciate the company but make sure you turn in soon,{w=0.2} alright?"

        if 1knmpul Natsuki.isLove(higher=True):
            n 1klrpul "You know I don't like it when you don't take care of yourself like this..."

        elif Natsuki.isAffectionate(higher=True):
            n 1fcspol "You should know better than to treat yourself like this by now,{w=0.2} [player]..."

        n 1fllsfl "Don't let me down,{w=0.2} got it?"

        # Add pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

    elif jn_get_current_hour() > 21 or jn_get_current_hour() < 3:
        n 1fskem "[player]!"
        n 1fnmem "I'm not surprised you're tired!{w=0.2} Have you even seen the time?!"
        $ chosen_tease = jn_utils.getRandomTease()
        n 1knmpu "It's the middle of the night,{w=0.2} [chosen_tease]!"
        n 1fcsanl "Nnnn...{w=0.3} you should really turn in soon,{w=0.2} you know..."
        n 1fnmpol "I don't want you to be all cranky later because you didn't get enough sleep."
        n 1flrpol "And neither do you,{w=0.2} I'm sure."
        n 1kcspo "Just...{w=0.3} try to get to bed soon,{w=0.2} okay?{w=0.2} {i}Before{/i} your keyboard becomes your pillow."

        if Natsuki.isLove(higher=True):
            n 1ksqpol "Besides...{w=0.3} you do know I'm not actually strong enough to carry you to bed myself...{w=0.3} right?"

        n 1kllssl "Ahaha..."

        # Add pending apology
        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

    else:
        n 1knmsl "Feeling tired,{w=0.2} [player]?"
        n 1kllbo "You should think about turning in soon{w=0.2} -{w=0.2} even just for a nap."
        n 1fcseml "Don't worry about me if you need to rest!{w=0.2} I'll be fine!"
        n 1knmpo "Just make sure you let me know when you decide to go,{w=0.2} [player]."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return
