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
        n 1tnmsm "Still trying to beat the boredom,{w=0.2} [player]?"
        n 1nllpo "Did you actually try doing what I said?"
        n 1flrpu "Hmm..."
        n 1fnmbg "Well,{w=0.2} you could try phoning around!{w=0.2} You gotta have friends or family you can visit,{w=0.2} right?"
        n 1nllbg "Or...{w=0.3} perhaps you could try reading,{w=0.2} or picking up something new?"
        n 1fsqsm "I guess what I'm trying to say is..."
        n 1fsqbg "There's no shortage of stuff to do,{w=0.2} [player]."
        n 1fchgn "You just gotta find it!"

        if Natsuki.isEnamored(higher=True):
            n 1uchbg "Now,{w=0.2} go!{w=0.2} And make sure you tell me all about it later,{w=0.2} 'kay?"

        else:
            n 1usqbg "Well?{w=0.3} What're you waiting for?"
            n 1nchgn "Go for it,{w=0.2} [player]!"

    # Unlock Snap if not already unlocked
    elif not persistent.jn_snap_unlocked:
        n 1unmaj "You're bored,{w=0.2} huh?"
        n 1nlrpo "Well,{w=0.2} now that you mention it...{w=0.3} there isn't {i}exactly{/i} a whole lot going on here."

        if Natsuki.isEnamored(higher=True):
            n 1fllssl "Besides me,{w=0.2} anyway.{w=0.2} Ehehe."

        n 1flrpo "Hmm...{w=0.3} there's gotta be something else..."
        n 1fcspo "Think,{w=0.2} Natsuki!{w=0.2} Think..."
        n 1fllpu "..."
        n 1fsgbg "Aha!{w=0.2} I think I got it!{w=0.2} Let me just check something real quick..."

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

        n 1fchgn "Yes!{w=0.2} It's still here!"
        n 1fsgsg "Betcha' didn't know I had playing cards,{w=0.2} right?"
        n 1nchgn "Turns out these desk drawers {i}are{/i} handy,{w=0.2} after all!"
        n 1nnmsm "I always had a pack here ready for a rainy day."
        n 1kllsll "...Uhmm."
        n 1nnmsl "Hey...{w=0.3} [player]?{w=0.2} Don't judge me for it,{w=0.2} but..."
        n 1nlrun "I...{w=0.3} never really learned all the really fancy card game rules or anything like that."
        n 1ullaj "So...{w=0.3} we're playing Snap."
        n 1fllssl "...At least until I do some reading up,{w=0.2} anyway."
        $ persistent.jn_snap_unlocked = True
        n 1nnmss "So..."
        n 1uchgn "What about it then,{w=0.2} [player]?{w=0.2} Fancy a game or two?"
        menu:
            n "Not like you have much of an excuse not to,{w=0.2} right?"

            "Sure,{w=0.2} why not?":
                jump snap_intro

            "Not right now.":
                n 1fllpo "Aww...{w=0.3} but I already got the cards out and everything!"
                n 1unmpo "Well...{w=0.3} whatever."
                n 1nnmsm "Just let me know whenever you feel like a game then."

                play audio drawer
                with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    else:
        n 1tnmaj "Huh?{w=0.2} You're bored?"
        n 1fnmaj "And just what is that supposed to mean,{w=0.2} [player]?"
        n 1fsqpo "Am I not fun enough to be with?"
        n 1fbkwr "Are you not entertained?!"
        n 1flrpo "..."
        n 1fsqsm "..."
        n 1uchgn "Relax!{w=0.2} Relax,{w=0.2} [player], jeez!"
        n 1ullaj "Well,{w=0.2} if you're bored..."
        $ chosen_tease = jn_utils.getRandomTease()
        n 1uchbs "Then get up off your butt and do something about it,{w=0.2} [chosen_tease]!"
        n 1tlrbg "Jeez,{w=0.2} [player]...{w=0.3} there's a big, wide world out there just waiting for you!"
        n 1tsqbg "And if that isn't enough,{w=0.2} there's an even bigger one right at your fingertips!"
        n 1fsqss "Or you could,{w=0.2} you know."

        if Natsuki.isEnamored(higher=True):
            n 1kwmsgl "Spend more time with yours truly?"
            n 1knmpol "I'm not that dull...{w=0.3} right?"

        else:
            n 1fchbg "Appreciate that you get to spend more time with me!"
            n 1flrpol "N-{w=0.2}not that I'd totally appreciate it,{w=0.2} or anything,{w=0.2} of course.{w=0.2} Ahaha..."

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
        n 1fsgsm "Still full of confidence,{w=0.2} I see?"
        n 1nchbg "Well,{w=0.2} I'm glad to hear it!"

        if Natsuki.isEnamored(higher=True):
            n 1kwlsml "You've got a lot to be confident of,{w=0.2} [player]."
            n 1fchsml "You better remember that!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 1fchbg "Really?{w=0.2} That's awesome,{w=0.2} [player]!"
        n 1kllss "I was hoping you'd snap out of those feelings sooner rather than later."
        n 1klrpo "I don't like when you talk like that,{w=0.2} you know..."

        if Natsuki.isAffectionate():
            n 1fcspol "N-{w=0.2}not that I care {i}that{/i} much, o-{w=0.2}of course!"
            n 1fllsll "But...{w=0.3} I'm glad to know you're okay now,{w=0.2} [player]. That's what matters."

        elif Natsuki.isEnamored(higher=True):
            n 1kllsll "I'm just really glad to know you're better now,{w=0.2} [player]."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1knmssf "I love you, [chosen_endearment].{w=0.2} Please don't forget that,{w=0.2} alright?"
            n 1klrpof "I'll get mad if you do.{w=0.2} Ahaha..."

    else:
        n 1nchgn "Ahaha!{w=0.2} I'm glad to hear that,{w=0.2} [player]!"
        n 1unmaj "Being confident in yourself and your abilities can be really difficult sometimes."
        n 1ullbo "Especially if you messed up,{w=0.2} or if you aren't feeling well."
        n 1fchbg "But if you're feeling that way about yourself,{w=0.2} I'm not gonna rob you of it!"

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
        n 1fnmsm "Still pumped up,{w=0.2} are we [player]?"
        n 1fsqsm "I bet you just can't wait,{w=0.2} huh?{w=0.2} Ehehe."

    else:
        n 1fsptr "Oh?{w=0.2} Did something happen?{w=0.2} Is something {i}gonna{/i} happen?"
        n 1fchbg "Whatever it is,{w=0.2} good to know you're looking forward to it!"
        n 1unmsm "It's always awesome to have something you can get excited over,{w=0.2} right?"

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
        n 1ksqsg "Wow...{w=0.3} it's all sunshine and rainbows with you today,{w=0.2} isn't it?"
        n 1fchbg "Ahaha!"
        n 1fchbg "Good for you,{w=0.2} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1kwmss "Feeling better now,{w=0.2} [player]?"
        n 1kllbg "That's...{w=0.3} a relief,{w=0.2} ahaha..."

        if Natsuki.isAffectionate(higher=True):
            n 1kllunl "..."
            n 1klrbgl "S-{w=0.2}so...{w=0.3} where were we?"

        else:
            n 1fllunl "..."
            n 1fcswrl "Jeez...{w=0.3} if you're okay,{w=0.2} then let's get back to it already!"
            n 1klrpol "Dummy..."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fsqbg "Feeling better,{w=0.2} [player]?{w=0.2} I'm not surprised!"
        n 1fchbg "You just aren't yourself when you're hungry.{w=0.2} Ehehe."
        n 1kllsl "Trust me...{w=0.3} I would know."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1nnmsm "Feeling better,{w=0.2} [player]?{w=0.2} I'm glad to hear it!"
        n 1nchbg "Nothing makes you appreciate feeling normal more than being sick,{w=0.2} right?"

    else:
        n 1usqbg "Oh?{w=0.2} Someone's in a good mood today!"
        n 1fchbg "Good for you,{w=0.2} [player]!"

        if Natsuki.isAffectionate(higher=True):
            n 1uchsm "If you're happy,{w=0.2} I'm happy!"

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
        n 1tnmpu "What?{w=0.2} You're still hungry?"
        n 1fnmpo "Or did you not get something when I told you to earlier?"
        n 1fchgn "Well...{w=0.3} either way,{w=0.2} get off your butt and go get something then!"
        n 1fllpol "Jeez,{w=0.2} [player]...{w=0.3} I'm not your babysitter!"

        if Natsuki.isEnamored(higher=True):
            n 1fsqsml "A-{w=0.2}as much as you probably wish I was,{w=0.2} right?{w=0.2} Ahaha!"
            n 1uchbs "Now get going already!{w=0.2} Bon appetit,{w=0.2} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1knmsl "[player]...{w=0.3} you told me you were sad earier."
        n 1klrsl "I don't mind if you're hungry,{w=0.2} but try not to comfort-eat,{w=0.2} okay?"
        n 1knmpu "You might feel a little better...{w=0.3} but it won't fix what made you sad."
        n 1knmsm "Try to enjoy your meal,{w=0.2} alright?"

        if Natsuki.isAffectionate(higher=True):
            n 1kwmsml "I'm here for you if you need me,{w=0.2} [player]."

    else:
        n 1unmpu "Huh?{w=0.2} You're hungry?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 1fupem "Then what're you telling {i}me{/i} for?{w=0.5}{nw}" 
        extend 1fchgnelg " Go get something to eat,{w=0.2} [chosen_tease]!"
        n 1fllaj "Honestly...{w=0.75}{nw}" 
        extend 1fcspo " what am I going to do with you,{w=0.2} [player]?"
        n 1fchbg "Now go make something already!{w=0.2} Just don't fill yourself up on junk!"

        if Natsuki.isEnamored(higher=True):
            n 1fsqbg "I want you fighting fit for when we hang out,{w=0.2} 'kay?"
            n 1uchgn "We're gonna have so much to do together,{w=0.2} after all!"

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
        n 1knmsl "You're still feeling insecure about yourself,{w=0.2} [player]?"
        n 1kllsl "You...{w=0.3} do remember what I said though,{w=0.2} right?"
        n 1ncssl "Everybody has their own pace.{w=0.2} I don't care what yours is.{w=0.2} We'll take it together."
        n 1fchgn "...Wow{w=0.2}, that seriously sounded super corny."
        n 1kllnv "But really,{w=0.2} [player]...{w=0.3} try not to sweat it,{w=0.2} okay?"
        n 1fchbgl "The great Natsuki has your back,{w=0.2} after all!"

    else:
        n 1knmsl "Huh?{w=0.2} You're feeling insecure?{w=0.2} Where did that come from,{w=0.2} [player]?"
        n 1kllsl "..."
        n 1knmpu "I...{w=0.3} can't really comment on what made you feel that way..."
        n 1fnmpu "But you better listen,{w=0.2} and listen good,{w=0.2} [player]."
        n 1fcspu "I don't care if people don't like you.{w=0.2} I like you."
        n 1fcsbo "I don't care if people think you have no talents.{w=0.2} I know you do."
        n 1fnmbo "I don't care if people think you're falling behind.{w=0.2} I know you'll catch up."
        n 1kllsl "Just...{w=0.3} give yourself time and space,{w=0.2} [player]."
        n 1kwmsl "These thoughts you're having...{w=0.3} they can lead you to some really bad places.{w=0.2} Trust me."
        n 1fwmsl "I'm not gonna let that happen without a fight{w=0.2} -{w=0.2} but you gotta fight too,{w=0.2} [player].{w=0.2} Got it?"
        menu:
            "Okay.":
                n 1fnmsl "...Good.{w=0.2} Or you'll have me to deal with too."
                n 1kllsm "..."
                if Natsuki.isAffectionate(lower=True):
                    n 1flrajl "Message received?{w=0.2} T{w=0.2}-then let's get back to it already!"
                    n 1flrpol "Jeez..."

                else:
                    n 1kwmpul "...You know I meant every single word I said,{w=0.2} right?"
                    n 1kcssll "So please...{w=0.3} don't give up.{w=0.2} We both need you to win,{w=0.2} [player]."

                    if Natsuki.isLove(higher=True):
                        $ chosen_endearment = jn_utils.getRandomEndearment()
                        n 1kwmsmf "I really do love you, [chosen_endearment]."
                        n 1kchbgf "You know I'll always have your back,{w=0.2} dummy..."

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
        n 1fsqbg "Really,{w=0.2} [player]?{w=0.2} Still gloating,{w=0.2} are we?"
        n 1tsqbg "You {i}do{/i} know what they say about pride,{w=0.2} right?"
        n 1fsqsm "..."
        n 1kchlg "I'm just kidding,{w=0.2} [player]!{w=0.2} Jeez!"
        n 1kchgn "You should see your face sometimes!"
        n 1nnmsm "Well,{w=0.2} it's cool to see you're still feeling good about yourself!"

    else:
        n 1tsgbg "Oh?{w=0.2} You're feeling proud,{w=0.2} huh?"
        n 1fsqsm "You must be pretty pleased with yourself to brag to me about it."
        n 1fchbg "Well...{w=0.3} whatever it was -{w=0.2} good work,{w=0.2} [player]!"

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
