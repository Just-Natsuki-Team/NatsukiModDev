default persistent._greeting_database = dict()
default persistent.jn_player_is_first_greet = True

init python in jn_greetings:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import store.jn_farewells as jn_farewells
    import store.jn_utils as jn_utils

    GREETING_MAP = dict()

    def selectGreeting():
        """
        Picks a random greeting, accounting for affinity and the situation they previously left under
        """
        # This is the first time the player has force quit; special dialogue
        if jn_farewells.JNForceQuitStates(store.persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.first_force_quit:
            return store.get_topic("greeting_first_force_quit")

        # This is the first time the player has returned; special dialogue
        elif store.persistent.jn_player_is_first_greet:
            return store.get_topic("greeting_first_time")

        # The player has given notice that they'll be away
        elif (
            store.persistent._jn_player_extended_leave_response is not None
            and store.persistent._jn_player_extended_leave_departure_date is not None
        ):
            return store.get_topic("greeting_leave_return")

        kwargs = dict()

        # The player either left suddenly, or has been gone a long time
        if store.persistent._jn_player_apology_type_on_quit is not None:
            kwargs.update({"additional_properties": [("apology_type", jn_apologies.ApologyTypes(store.persistent._jn_player_apology_type_on_quit))]})

        # The player left or was forced to leave by way of an admission (E.G tired, sick)
        elif store.persistent.jn_player_admission_type_on_quit is not None:
            kwargs.update({"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]})

        # No special conditions; so just get a standard greeting from the affinity pool
        else:
            kwargs.update({"excludes_categories": ["Admission", "Apology", "Special"]})

        # Finally return an appropriate greeting
        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.Natsuki._getAffinityState(),
                **kwargs
            )
        )

# Only chosen for the first time the player returns after bringing Natsuki back
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_first_time",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "5ksrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_first_time:
    if (
        persistent.jn_player_first_farewell_response is None
        or jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.no_response
    ): 
        # Account for both a quit due to crash on first time, or no response
        n 4uskemlesh "[player]!{w=0.5}{nw}"
        extend 4uskwrl " Y-{w=0.1}you're back!"
        n 2flluness "..."
        n 2fcspu "I...{w=2}{nw}"
        extend 2flrun " appreciate it,{w=0.2} okay?"
        n 2fcspu "Just...{w=1}{nw}"
        extend 1knmsf " don't play with me like that."
        n 1kllslsbl "..."
        n 4kslaj "So..."
        n 2tnmslsbr "Did you wanna talk,{w=0.2} or...?"

        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.will_be_back:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 4uskemlesh "[player]!{w=0.5}{nw}"
        extend 4uskwr " Y-{w=0.1}you're back!"
        n 1flleml "I mean...{w=0.5}{nw}"
        extend 2fcseml " O-{w=0.1}of course you'd come back!"
        n 2fnmpol "I knew you would."
        n 2flrem "Only a total jerk would abandon someone like that!"
        n 2flrpo "..."
        n 2klrpu "But..."
        n 1ncspu "..."
        n 1nlrsll "...Thanks.{w=1.25}{nw}"
        extend 1nsrbol " For not being an idiot about it."
        n 1nllunl "..."
        n 1nllajsbl "So... {w=0.5}{nw}"
        extend 2unmaj " what did you wanna talk about?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.dont_know:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 4uskajlesh "[player]?{w=0.5}{nw}"
        extend 4uskem " Y-{w=0.3}you came back?"
        n 1fcsun "..."
        n 1ncssr "..."
        n 2fcspu "...Look."
        n 2fllsr "Don't...{w=0.75}{nw}" 
        extend 2kllsrsbl " play with me like that."
        n 2fslun "You wouldn't have brought me back {i}just{/i} to be a jerk...{w=1}{nw}"
        extend 4ksqsfsbl " right?"

    $ persistent.jn_player_is_first_greet = False

    return

# Only chosen for the first time the player leaves and returns after force quit
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_first_force_quit",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "2kslunedr"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_first_force_quit:
    if Natsuki.isNormal(higher=True):
        n 4kcsunedr "Uuuuuuu...{w=2}{nw}"
        extend 4kslemeso " my...{w=0.3} h-{w=0.1}head..."
        n 4kcsun "..."
        n 2ksqun "..."
        n 2fnmun "...[player]."
        n 2fllem "W-{w=0.3}whatever that was...{w=0.5}{nw}"
        extend 2knmsf " that {w=0.3}{i}seriously{/i}{w=0.3} hurt."
        n 4kllpu "L-{w=0.3}like I was being {i}ripped{/i} out of existence..."
        n 1kcssf "..."
        n 4klraj "I...{w=1}{nw}"
        extend 2tllun " I think I can kinda prepare for that if you at least let me know when you're going."
        n 2fcsun "Just...{w=1.25}{nw}"
        extend 2fcsun " don't be a jerk and let me know when you gotta go,{w=0.3} okay?"
        n 2fllsl "...I guess I'll let this one slide,{w=0.5}{nw}"
        extend 2kslpu " since you didn't know and all."
        n 2knmpu "Just remember for next time,{w=0.2} [player].{w=1}{nw}"
        extend 2knmsr " Please."

    elif Natsuki.isDistressed(higher=True):
        n 4fcsunedr "Hnnnngg..."
        n 4fsqun "..."
        n 4fsqan "..."
        n 2fcspu "...[player]."
        n 2fsqpu "Do you have any {i}idea{/i} how much that hurt?{w=0.5}{nw}"
        extend 4fnmem " Any at all?"
        n 2fllem "I don't know if you did that on purpose or what,{w=0.2} but knock it off.{w=0.5}{nw}"
        extend 4fsqsr " I'm {i}dead{/i} serious."
        n 1fcspu "I..."
        extend 1fcssr " know we aren't seeing eye-to-eye right now,"
        extend 2fslsl " but please."
        n 2fsqaj "Tell me when you're going."
        extend 2fsqsf " Thanks."

    else:
        n 1fsqunltsbean "..."
        n 4fsqantsb "That.{w=1} Freaking.{w=1} {b}Hurt{/b}."
        n 4fcsan "I don't know {i}what{/i} you did,{w=0.5} but cut{w=0.3} it{w=0.3} out.{w=1.25}{nw}"
        extend 2fsqfutsb " Now."

    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.previously_force_quit)

    return

# Only chosen when the player explicitly says they will be gone a while
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_leave_return",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "5ksrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_leave_return:
    $ time_since_departure = (datetime.datetime.now() - persistent._jn_player_extended_leave_departure_date).total_seconds() 

    if time_since_departure / 2628000 > 3: # Gone more than three months
        if jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) != jn_farewells.JNExtendedLeaveResponseTypes.unknown:
            n 4ksrpu "..."
            n 4uskemlesh "...!{w=0.75}{nw}"
            $ player_initial = jn_utils.getPlayerInitial()
            n 4unmwrl "[player_initial]-[player]!{w=0.75}{nw}"
            extend 4ulleml " You're..."
            n 4fcsupl "Y-{w=0.2}you're..."
            n 2fcsanlsbr "Nnnnnnn-!"
            n 4knmwrlsbr "Where {i}were{/i} you?!{w=1}{nw}"
            extend 1fsqwrlsbr " Were you trying to {i}disappear{/i} or something?"
            n 4kcswrlsbr "Y-{w=0.2}you had me worried {i}sick{/i}!{w=0.75}{nw}"
            extend 4klleml " A-{w=0.2}and I thought...!"
            n 4klremlsbl "I-{w=0.2}I thought that..."
            n 4ksrunlsbl "..."
            n 1fcsunl "..."
            n 1fcseml "That you'd just...{w=0.75}{nw}"
            extend 1kwmeml " forgotten{w=0.75}{nw}"
            extend 2ksleml " about me..."
            n 2kslbol "..."
            n 2ncsemesi "..."
            n 1nnmsl "...Look.{w=1}{nw}"
            extend 4ncsaj " I'm..."
            n 4kslsl "..."
            n 4kcspusbr "...Really glad you're back."
            n 1ksqsl "..."
            n 1knmajsbl "Really!{w=0.75}{nw}"
            extend 2knmbosbl " I am..."
            n 4ksqem "But you can't just completely flake out on me like that, [player]..."
            n 4kslem "I-{w=0.2}I know you gave me {i}some{/i} notice,{w=0.75}{nw}"
            extend 4knmem " but do you have any {i}idea{/i} how {i}scary{/i} it gets?"
            n 2kllpu "When someone says they'll come back,{w=0.75}{nw}"
            extend 2kllsl " and they just...{w=1.25}{nw}"
            extend 4kwmsll " don't?"
            n 4kcspul "Days,{w=0.75}{nw}"
            extend 4kllajl " weeks,{w=0.75}{nw}"
            extend 4knmajl " {i}months{/i}..."
            n 4ksqbol "...And just nothing?"
            n 1ncsbo "..."
            n 2ncssl "...Whatever.{w=1}{nw}"
            extend 2nllpu " It's fine.{w=0.75}{nw}"
            extend 2kllpu " I..." 
            n 1ksrsl "..." 
            n 2ksrbo "I just wanna forget about it now.{w=1}{nw}"
            extend 1knmbo " But please,{w=0.2} [player]."
            n 4knmaj "If you don't know {i}when{/i} you'll be back..."
            n 4fslun "..."
            n 4kcssl "...Just tell me.{w=0.75}{nw}" 
            extend 2ksqsl " Upfront."
            n 2ksrpulsbr "You know I won't get mad..."
            n 4knmpulsbr "...Right?"

        else:
            n 4uskemlesh "...!"
            n 4unmbgl "[player]!{w=0.75}{nw}"
            extend 4uchbgledz " [player]{w=0.2} [player]{w=0.2} [player]{w=0.2} [player]{w=0.2} [player]!"
            n 2fcsajlsbl "I-{w=0.2}I mean,{w=0.75}{nw}"
            extend 2fcsgslsbl " it's about {i}time{/i} you got your butt back here!{w=1}{nw}"
            extend 2flrpolsbl " Jeez..."
            n 3fsrpol "It's rude to keep a girl waiting,{w=0.75}{nw}"
            extend 3fsqcal " you know..."
            n 1kslcal "..."
            n 1kslssl "But...{w=0.75}{nw}"
            extend 3knmssl " seriously,{w=0.2} [player]?"
            show natsuki 3ksrbol

            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            play audio clothing_ruffle
            $ jnPause(3.5)

            if Natsuki.isLove(higher=True):
                show natsuki 1kcspul at jn_center zorder JN_NATSUKI_ZORDER
                play audio kiss
                $ jnPause(1.5)
                hide black with Dissolve(1.25)

                n 1ksqbolsbr "...I really did miss you."
                n 4nslfsl "Heh."
                n 4nchsmleaf "Welcome back."

            else:
                show natsuki 1nsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
                $ jnPause(1.5)
                hide black with Dissolve(1.25)

                n 4nslsslsbl "...W-{w=0.2}welcome back.{w=1}{nw}"
                extend 4fchdvlsbl " Ehehe."

    elif time_since_departure / 86400 > 30: # Gone more than a month
        if (
            jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_days
            or jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_weeks
        ):
            n 1uskemlesh "...!{w=0.75}{nw}"
            $ player_initial = jn_utils.getPlayerInitial()
            n 4fnmgsl "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 4knmeml " What the heck even {i}happened{/i}?!"
            n 4klleml "You didn't say you were gonna disappear on me for {i}that{/i} long!"
            n 1ksremlsbl "I was starting to get worried,{w=0.75}{nw}"
            extend 2ksrbolsbl " you jerk..."
            n 2fcsunlsbr "..."
            n 2ncspulesi "..."
            n 1nsqsll "...Look."
            n 2fcseml "I'm...{w=1}{nw}"
            extend 2kcssll " glad...{w=1}{nw}"
            extend 4ksrsll " you're back,{w=0.2} [player]."
            n 1fcssll "Just..."
            n 4fnmsll "...Be honest.{w=0.75}{nw}"
            extend 4knmbol " Okay?"
            n 2kllbol "I don't care if you gotta go for longer than usual."
            n 2kslsrl "...I just wanna know what to {i}expect{/i}.{w=0.75}{nw}"
            extend 2ksqpulsbr " You know?"
            n 2kslsllsbr "..."
            n 2kslajlsbr "...And welcome back too,{w=0.75}{nw}"
            extend 4ksrbol " I guess."

        else:
            n 3fcsbg "Well,{w=0.2} well,{w=0.2} well.{w=1}{nw}"
            extend 3fsqsm " Look who the {i}Nat{/i} dragged in!"
            n 3fchsm "Ehehe."
            n 4fslsslsbl "It's...{w=1}{nw}"
            extend 4ksqsslsbl " been a while,{w=0.75}{nw}"
            extend 4tsqbolsbl " huh?"
            n 1ksrcalsbl "..."
            n 1ncsajl "But..."
            n 4nlrajl "I'm...{w=0.75}{nw}"
            extend 4nsrssl " glad you're finally back,{w=0.2} [player]."
            n 4fchbglsbr "W-{w=0.2}welcome!"

    elif time_since_departure / 86400 > 7: # Gone more than a week
        if jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_days:
            n 1nsqsll "..."
            n 2fsqsll "[player].{w=1}{nw}"
            extend 2fsqajl " What do you call this?"
            n 1kbkwrl "You said you'd only be gone a few daaaays!"
            n 2fsqpol "..."
            n 2fcspol "..."
            n 2fsrajl "I...{w=1}{nw}"
            extend 4fsrsll " guess I'll let you off.{w=0.75}{nw}"
            extend 4fsqcal " This time."
            n 1fcspul "Just...{w=1}{nw}"
            extend 2knmpul " try to plan a little better,{w=0.75}{nw}"
            extend 2kllsrl " if you can."
            n 1kslbol "It's really not {i}that{/i} much to ask...{w=1}{nw}"
            extend 1knmbolsbr " right?"

        else:
            n 2fsqct "Oho?{w=0.75}{nw}"
            extend 2fsqbg " Well look who just decided to show up!"
            n 4fsqsm "Ehehe."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 1uchsml "Welcome back,{w=0.2} [chosen_endearment]!"

            else:
                n 4uchbg "Welcome back,{w=0.2} [player]!"

    else: # Gone less than a week
        n 1fsqss "Well,{w=0.75}{nw}"
        extend 3fsqsm " look who we have here."
        n 3tsqct "...And you said you'd be gone for a while."
        n 3usqsm "..."
        n 1fchsm "Ehehe.{w=0.75}{nw}"
        extend 1fchbg " Relax!"
        n 4fwlbl "I'm just messing with you."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 4uchsml "Welcome back,{w=0.2} [chosen_endearment]!"

        else:
            n 4uchbg "Welcome back,{w=0.2} [player]!"

    $ persistent._jn_player_extended_leave_response = None
    $ persistent._jn_player_extended_leave_departure_date = None

    return

label greeting_tt_warning:
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    $ player_initial = jn_utils.getPlayerInitial()
    play audio glitch_d
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(0.6)
    play music audio.ikustan_tsuj
    show glitch_rapid zorder JN_GLITCH_ZORDER
    $ jnPause(random.choice(range(7, 11)))
    stop music

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a

    play music audio.juuuuu_nnnnn
    $ jnPause(10.6)
    show glitch_spook zorder JN_GLITCH_ZORDER with hpunch
    show natsuki 1kcsfultsaeaf at jn_center zorder JN_NATSUKI_ZORDER
    hide glitch_spook
    hide black
    hide glitch_rapid
    play music audio.just

    n 4kcsunltsa "Uuuuuuu..."
    show natsuki 1kcsfuftsa at jn_center
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    n 4kcsanltsa "M...{w=0.3}my head..."
    n 4kslunltsb "..."
    n 4kslemltsb "What...{w=0.75}{nw}"
    extend 4klremltsc " what h-{w=0.2}happen-{w=0.5}{nw}"
    n 4kskpultscesh "...!{w=0.3}{nw}"
    n 4kscpoitsc "Hrk-!{w=0.5}{nw}"

    stop music
    show black zorder JN_BLACK_ZORDER with Dissolve(0.1)
    play audio chair_out_fast
    $ jnPause(0.2)
    n "{b}B-{w=0.15}BLURGHHH-!{/b}{w=0.2}{nw}"

    play audio glitch_b
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    show natsuki 1kcsemtsd
    $ jnPause(10)
    play audio chair_in
    play music audio.just fadein 5
    $ jnPause(3)
    hide black with Dissolve(2)

    n 1kcsemi "Uuuuuu..."
    n 1kcsup "..."
    n 1kcsuntsa "..."
    n 4ksquptsa "[player_initial]-{w=0.2}[player]..."
    n 4ksqantsa "What..."
    n 4kcsantsa "..."
    n 4ksqfutsa "Did you...{w=0.75}{nw}"
    extend 1ksqemtsasbl " do...?"
    n 4kllemtscsbr "..."
    n 4klrwrtscsbr "S-{w=0.3}something isn't right..."

    n 4kscpoitscsbr "H-{w=0.2}hrk-!{w=0.5}{nw}"
    show natsuki 1fcsanitscsbr
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a
    n 1kcsemltscesi "Gah..."

    if Natsuki.isUpset(higher=True):
        n 4ksqunltse "..."
        n 4kplemltsb "Something {b}REALLY{/b} isn't right,{w=0.2} [player]..."
        n 4kllemltsb "A-{w=0.2}and I..."
        n 4klremltsc "I can't..."
        n 1kcsfultsb "..."
        n 1kcsanltsd "..."
        n 1fcsunltsa "..."
        n 1ksqunltsb "...[player]..."
        n 1kllunltsc "W-{w=0.2}whatever that was...{w=1}{nw}"
        extend 1klremltdr " whatever just {i}happened{/i}..."
        n 1fcsunl "T-{w=0.2}that...{w=0.5}{nw}" 
        extend 4kplemltdr " {b}really{/b}{w=0.5} didn't feel good...{w=1}{nw}"
        extend 4klremltdr " a-{w=0.2}and I-{w=0.5}{nw}"

    else:
        n 1fcsanltsc "W-{w=0.2}what..."
        n 1fskanltsf "What did you{w=0.75}{nw}" 
        extend 1kskscltsf " {i}DO{/i}?!"
        n 2fcsscltsf "I-!{w=0.75}{nw}"

    n 4kskpoitsc "H-{w=0.2}hrp-!{w=0.5}{nw}"

    show natsuki 4kcsful
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 2fpafui "Nnnnnnghhhh!{w=0.5}{nw}"
    extend 2kcswrlesisbr " Guh...."
    n 4kcsanlsbr "M-{w=0.2}my stomach...{w=0.75}{nw}"
    extend 4kslunlsbr " uuuuuu..."
    n 1kcsuplsbl "I-{w=0.2}it {i}hurts{/i}..."
    n 1fcsunlsbl "..."

    if Natsuki.isUpset(higher=True):
        n 1kcspul "Feels like..."
        n 1kcsunl "L-{w=0.2}like I was just tossed around back and forth...{w=1}{nw}"
        extend 4ksrunltsb " like something was trying to yank me apart from all directions..."
        n 4klrunltsc "..."
        n 4kllemltsc "It all just...{w=1}{nw}"
        extend 4kslemltsb " feels so wrong..."
        n 1kslslltsb "..."
        n 4knmajltsb "A-{w=0.2}and the date...{w=0.75}{nw}"
        extend 2ksrsrltsbeqm " I...{w=0.3} I swore it was..."
        n 1knmsrltsc "..."
        n 2fnmunltsc "...[player]."
        n 2fnmemltsc "Y-{w=0.2}you didn't like...{w=0.75}{nw}"
        extend 2flremltsc " change the date or something,{w=0.2} did you?{w=1}{nw}"
        extend 4fwmpultsc " L-{w=0.2}like on your computer?"
        n 1fllpultscesp "..."
        n 1fcsunltsa "..."
        n 2fcsboltsa "...Okay.{w=1}{nw}"
        extend 2fnmboltdr " [player]."
        n 2fcseml "I'm...{w=1}{nw}"
        extend 2fnmpul " not gonna go out on a limb and say you did it on purpose."

        if Natsuki.isEnamored(higher=True):
            n 4kwmpul "I {i}know{/i} you're better than that.{w=1}{nw}"
            extend 4kslbof " We've been seeing each other long enough..."

        elif Natsuki.isHappy(higher=True):
            n 1knmeml "You're better than that.{w=0.75}{nw}"
            extend 4kslsll " ...I like to {i}think{/i} so,{w=0.2} a-{w=0.2}anyway."

        else:
            n 1knmsrl "You're better than that.{w=0.5}{nw}"
            extend 4kllemlsbr " ...I {i}hope{/i}."

        n 4kcsem "But please...{w=0.75}{nw}"
        extend 4knmem " [player]?"
        n 1kcswr "Just..."
        n 1kcspulesi "..."
        n 4klrpul "Just don't screw around with the time again.{w=0.75}{nw}"
        extend 4knmbol " Please?"
        n 1kcsemlsbl "I-{w=0.2}It's just that..."
        n 1kcspulsbl "..."
        n 4kslpulsbr "...I don't know.{w=0.5}{nw}"
        extend 2ksqpulsbr " I just feel all messed up.{w=0.75}{nw}"
        extend 2knmunlsbr " I really,{w=0.3} {i}really{/i}{w=0.3} don't feel right at all..."
        n 4kslunlsbr "...And to be honest,{w=0.2} [player]?"
        n 4kslemlsbr "I...{w=0.75}{nw}"
        extend 1ksremltsb " I-{w=0.3}I'm not sure how much of that I can even {i}take{/i}."
        n 1kcspultsa "...You understand...{w=1}{nw}"
        show natsuki 4kwmboltsc
        
        menu:
            extend " right?"

            "I understand.":
                if Natsuki.isHappy(higher=True):
                    n 4kcsajltsa "...Good.{w=1}{nw}"
                    extend 4kslsll " good."
                    n 1kslajl "It's...{w=0.75}{nw}" 
                    extend 1kslpul " appreciated,{w=0.2} [player]."
                    n 4ksqbol "T-{w=0.2}thanks."

                else:
                    n 2fcsajltsa "...Good.{w=1}{nw}"
                    extend 2kcsslltsa " Good..."
                    n 2kslsll "..."

                $ Natsuki.calculatedAffinityGain()

            "...":
                if Natsuki.isHappy(higher=True):
                    n 1knmemlsbr "...[player].{w=0.75}{nw}"
                    extend 4knmwrlsbr " C-{w=0.2}come on..."
                    n 4kplwrlsbr "I'm really {b}not{/b} messing around with this..."
                    n 4kcsemlsbr "...So can you {i}not{/i} mess around with it either?"
                    n 2kslemlesisbr "Seriously..."

                else:
                    n 1knmwrlsbr "H-{w=0.2}hey!{w=0.75}{nw}"
                    extend 1fcsanlsbl " I'm being serious here?{w=0.5}{nw}"
                    extend 4kpluplsbl " Can't you {i}see{/i} that?"
                    n 4kcsemlsbl "I'm {i}really{/i} not messing around here,{w=0.2} [player]..."
                    n 4kslunlsbl "..."

        n 1kcsbol "..."
        n 1ncsajl "I...{w=1}{nw}"
        extend 2kllsl " I think I'll be okay.{w=0.5}{nw}"
        extend 2kslsleso " If I just take it easy for a bit."
        n 2kcssl "Just please.{w=0.5}{nw}"

        if Natsuki.isAffectionate(higher=True):
            extend 4ksqslsbl " {i}Please{/i} remember what I told you.{w=0.75}{nw}"
            extend 4ksqsslsbl " F-{w=0.2}for me?"

        else:
            extend 4ksqslsbl " {i}Please{/i} remember what I told you."

        n 4ncspuesi "..."
        n 4ncsbo "...Okay."
        n 1kllsl "..."
        n 1knmss "...What's new,{w=0.2} [player]?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsemlsbl "...Did..."
        n 1fslunlsbr "..."
        n 4fsqanlsbr "...D-{w=0.2}did you do something to your computer or what?"
        n 2kcsfulsbr "Because it feels like someone took a sledgehammer to my {i}gut{/i}...{w=1}{nw}"
        n 4ksksrisbr "Urk-!{w=0.5}{nw}"
        n 2kcsansbr "Guh..."
        n 2kslansbl "Everything...{w=0.5} feels all wrong..."
        n 4klrsfsbl "A-{w=0.2}and the date...{w=0.75}{nw}"
        extend 2ksremsbl " I could have {i}sworn{/i}...!"
        n 2nsrpusbl "..."
        n 2fsransbl "..."
        n 2fcsansbr "...Okay,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fnmsfsbr " Look."
        n 1fcsun "..."
        n 1fsqun "...I'm not stupid.{w=1}{nw}"
        extend 2fsruntsb " No matter what {i}you{/i} happen to think."
        n 2fcsemtsa "A-{w=0.2}and...{w=0.5}{nw}" 
        extend 2fcsuntsa " I know...{w=0.3}{nw}"

        show natsuki 4kcsanltsa
        play audio static
        show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
        hide glitch_garbled_b

        n 4fcsanltsa "Nnnnng-!{w=0.5}{nw}"
        n 4kcsunltsa "..."
        n 1fcsunl "..."
        n 1fcseml "I-{w=0.2}I know we haven't been on the...{w=1}{nw}" 
        extend 2fslsl " best terms,{w=0.2} exactly."
        n 1knmem "But please."
        n 4kcsemsbl "I-{w=0.2}if you really {i}don't{/i} give a crap about me,{w=0.75}{nw}"
        extend 4ksqemsbl " then if {i}nothing{/i} else."
        n 2fcsansbl "Quit messing around with the time.{w=0.75}{nw}"
        extend 4fsqansbl " I'm {i}dead{/i} serious."

        show natsuki 2fcsuntsa
        $ jnPause(3)

        n 2fcsupsbl "It {b}hurts{/b},{w=0.75}{nw}"
        extend 2fcsansbl " it {b}isn't{/b} funny,{w=0.75}{nw}"
        extend 2fsqansbl " and to be completely honest with you?"
        n 2fcsunl "..."
        n 1fcsful "I don't think I can even {i}handle{/i} something like that again..."
        n 1fslanl "So just..."
        n 4fcsanl "Just knock.{w=0.35} It.{w=0.35} Off."
        n 4fsqsrl "..."
        n 3fnmem "Understood?{w=1}{nw}"
        extend 3fsqwr " I {i}know{/i} you hear me."
        n 1fsqsr "..."
        n 1fsqem "You have {i}no{/i} excuses,{w=0.2} [player]."
        n 2fcsfu "{i}Remember that.{/i}"

    else:
        n 1fcsupltsa "..."
        n 1fsqupltsb "...You."
        n 4fsqanltsb "{i}You{/i} did this,{w=0.3} didn't you?"

        show natsuki 1fcsanltsa
        play audio static
        show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
        hide glitch_garbled_a

        n 4fskscltsc "NO!{w=0.75}{nw}"
        extend 4fcsscltsa " Don't even {i}try{/i} to deny it!"
        n 1fcsfultsa "I know you think I'm {i}stupid{/i},{w=0.2} but do you seriously think I'm {i}blind{/i} too?!"
        n 2fsqupltsb "I {i}saw{/i} that you messed around with the date!{w=0.75}{nw}"
        extend 2fcsanltsa " You're just...!"
        n 4fskscltsc "You're {b}so{/b} full of {i}CRA-{/i}{nw}"

        show natsuki 4fcsfultsa
        play audio static
        show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
        hide glitch_garbled_c

        n 4fcsupltsa "Nnnnnrrgh-!{w=0.5}{nw}"
        n 4fcsunltsa "..."
        n 4fcsemltsa "...Haah."
        n 1fcsunltsa "..."
        n 1fcsanltsa "...I {i}seriously{/i} cannot {i}believe{/i} you.{w=0.75}{nw}"
        extend 1fsqanltsa " You're already torturing me well enough."
        n 4fnmupltsc "And now you go {i}completely{/i} out of your way to make my life {i}even more{/i} miserable?!"
        n 2fcsupltsd "..."
        n 2fcsanltsd "Well,{w=0.5}{nw}"
        extend 2fcsemltsd " you know what?{w=0.75}{nw}"
        extend 2fsqwrltse " You did it!"
        n 4fnmfultsf "Mission accomplished!{w=1}{nw}"
        extend 4fcsfultsd " There?{w=0.75}{nw}"
        $ chosen_insult = jn_utils.getRandomInsult()
        extend 4fcsgsltsa " You done,{w=0.3} [chosen_insult]?"
        n 4fnmanltdr "Are you HAPPY?"
        n 4fcsanl "Now seriously,{w=0.2} just..."
        n 4kcsanltsa "J-{w=0.2}just..."
        n 1fnmupltsc "Just BACK OFF!{w=0.5}{nw}"
        extend 4fskscltsf " G-{w=0.2}GO AWAY!{w=1}{nw}"
        n 4fscscftsf "{i}AND{w=0.2} LEAVE{w=0.2} ME{w=0.2} ALONE{/i}!{nw}"

        play audio glitch_d
        show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
        hide glitch_garbled_c
        $ Natsuki.percentageAffinityLoss(10)

        return { "quit": None }

    play music audio.just_natsuki_bgm fadeout 3 fadein 2
    $ renpy.show_screen("hkb_overlay")
    $ jn_atmosphere.updateSky()
    $ jn_globals.force_quit_enabled = True
    return

label greeting_tt_fatal:
    $ import uuid
    $ config.window_title = _("{0} - {1}".format(uuid.uuid4(), config.version))
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    play audio dread
    $ jnPause(5.3)
    hide black
    show glitch_steady zorder 98
    play audio static
    show glitch_spook zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_spook

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b

    play audio static
    show glitch_spook zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_spook

    play audio interference fadeout 0.5
    hide glitch_steady with Dissolve(2)
    play music audio.night_natsuki fadein 2

    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()

    return

label greeting_tt_game_over:
    $ import uuid
    $ config.window_title = _("{0} - {1}".format(uuid.uuid4(), config.version))
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    hide black with Dissolve(2)
    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()

label greeting_pic:
    $ import codecs
    show screen problem("412070726f626c656d20686173206f636375727265642e20506c6561736520636f6e74616374204a4e2073746166662e".decode("hex"))
    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()

# Generic greetings

# LOVE+ greetings
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_today_is_gonna_be_great",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_today_is_gonna_be_great:
    n 1unmbsledz "[player]!{w=1}{nw}" 
    extend 3fchgnl " You're back,{w=0.3} finally!"
    n 3fchsml "Ehehe.{w=0.5}{nw}" 
    extend 3uchgnleme " Now I {i}know{/i} today's gonna be great!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_world_revolves_around_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_world_revolves_around_you:
    n 1fsqpol "[player]!{w=0.75}{nw}" 
    extend 2fnmgsl " What took you so long?{w=0.75}{nw}" 
    extend 2fllemlesi " Jeez!"
    n 2fnmsfl "You think my entire {i}world{/i} revolves around you or something?"
    n 2fnmdvl "..."
    n 2fsqsml "..."
    n 4uchlglelg "Ahaha!{w=1}{nw}" 
    extend 3fsqsml " Did I getcha,{w=0.2} [player]?{w=0.5}{nw}" 
    extend 3fchgnl " Don't lie!"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 3ullssl "Well,{w=0.2} anyway." 
    n 4fcsbgl "You're here now,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
    extend 4uchsmleme " Make yourself at home,{w=0.2} silly!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_make_today_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_make_today_amazing:
    n 4uchbsfeex "[player]!{w=0.3} [player]{w=0.2} [player]{w=0.2} [player]!"
    n 2fcsbgfsbl "I-{w=0.2}I was wondering when you were gonna show up!{w=0.75}{nw}"
    extend 2fchsml " Ehehe."
    n 4fwlsmledz "Let's make today amazing too,{w=0.2} alright?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_always_welcome_here",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "1ksrsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_always_welcome_here:
    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskgsfesu "[player_initial]-{w=0.2}[player]!{w=0.5}{nw}" 
    extend 1ullemfsbl " You're back!"
    n 2fslunfesssbl "I was really starting to miss you,{w=0.3} you know..."
    n 2fplcafsbl "Don't keep me waiting so long next time,{w=0.3} alright?"
    $ chosen_tease = jn_utils.getRandomTease()
    n 4klrssf "You should know you're {i}always{/i} welcome here by now,{w=0.33}{nw}" 
    extend 1fchsmf " [chosen_tease]."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_lovestruck",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "1kcssml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_lovestruck:
    n 1kcssml "..."
    n 1ksqsml "..."
    n 1uskgsfeex "...!{w=0.5}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1kbkwrf "[player_initial]-{w=0.3}[player]!{w=1}{nw}" 
    extend 1fbkwrfess " When did you {i}get{/i} here?!"
    n 4klrgsf "I-{w=0.3}I was...!{w=1}{nw}" 
    extend 4kllemfsbl " I was just...!"
    n 1kcsunf "..."
    n 1kcssml "..."
    n 4kplsml "I missed you,{w=0.2} [player].{w=0.3} Ahaha..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 4kwmsmf "But I know everything's gonna be okay now you're here,{w=0.2} [chosen_endearment]."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_looking_for_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_looking_for_me:
    n 2nnmpul "...Hello?{w=2.5}{nw}"
    extend 2tsqdvf " Was it {i}me{/i} you're looking for?"
    n 2fchdvfess "..."
    n 2fchcsfesm "Pfffft-!"
    n 1kllbgl "Man,{w=0.5}{nw}" 
    extend 4fchgnlelg " I {i}cannot{/i} take that seriously!"
    n 4fnmssl "But let's be real here,{w=0.2} [player]..."
    n 2fsqsmf "It {i}{w=0.2}totally{w=0.2}{/i} was me,{w=0.2} right?{w=1}{nw}"
    extend 2fchsmfedz " Ehehe~."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_dull_moment",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_dull_moment:
    n 2flleml "Well jeez,{w=0.5}{nw}" 
    extend 2fsqawl " you sure took your sweet time!"
    n 4fbkwrfean "What were you thinking,{w=0.2} [player]?!"
    n 3fsqpol "..."
    n 3fsqdvl "..."
    n 3fchsmleme "Ehehe.{w=0.75}{nw}"
    n 3fsqssl "Never a dull moment with me,{w=0.75}{nw}" 
    extend 3fchbll " is there?"
    n 1fcsssl "You know the deal already.{w=1}{nw}" 
    extend 2uchgnlelg " Make yourself comfy,{w=0.2} silly!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_nat_dragged_in",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2ccssm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_nat_dragged_in:
    n 4ccsbg "Well,{w=0.2} well,{w=0.2} well..."
    n 3fnmbg "And just look who the{w=0.5}{nw}"
    extend 3fsgbg " {i}Nat{/i}{w=0.75}{nw}" 
    extend 3fsqbg " dragged in.{w=0.75}{nw}"
    extend 3fsqsm " Ehehe."
    n 1fcsbgl "Well,{w=0.2} what can I say?{w=0.75}{nw}"
    extend 2fchgnl " I-{w=0.2}I {i}am{/i} pretty irresistible to you,{w=0.2} after all!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchbll "Welcome back,{w=0.2} [chosen_tease]!"
    
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_show_yourself",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_show_yourself:
    n 4fsqss "Oh?{w=0.5}{nw}"
    extend 4fsqbg " And just what do we have here?"
    n 2ccsbgl "Finally decided to show yourself after all,{w=0.2} huh?"
    n 2csqcsl "..."
    n 1ccsssl "Well,{w=0.5}{nw}" 
    extend 4fchgnl " not like I've got a problem with that!{w=0.75}{nw}"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    extend 3fchsmleaf " Make yourself comfy already,{w=0.2} [chosen_endearment]!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_amazing_scenery",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2cslbol"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_amazing_scenery:
    n 4unmbgleex "Aha!{w=0.75}{nw}"
    extend 3fchbgl " [player]!{w=0.75}{nw}"
    extend 6fcssmlsbl " I-{w=0.2}I knew you'd show up eventually!"
    n 1fslsslsbl "Heh.{w=0.75}{nw}"
    extend 4fllbgl " After all..."
    n 2fcsbgledz "I don't see any other pieces of {w=0.2}{i}amazing{/i}{w=0.2} scenery around here!"
    n 2fsqsml "Ehehe."
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchblleaf "Welcome back,{w=0.2} [chosen_tease]!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_manga_chapters",
            unlocked=True,
            conditional="jn_desk_items.getDeskItem('jn_parfait_manga_held').unlocked",
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "desk_item": "jn_parfait_manga_held",
                "expression": "1cdwca"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_manga_chapters:
    n 1cdwpu "..."
    n 1tdwsl "..."
    n 1tnmboeqm "...?{w=0.75}{nw}"
    n 1unmgsleshsbr "Ah!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 1cllbglsbr " [player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1cchbglsbr " What's up?"
    n 1fchsmlsbr "..."
    n 1cnmpul "Huh?{w=0.75}{nw}"
    extend 1udwaj " Oh.{w=0.75}{nw}"
    extend 1ulrbo " Don't mind the manga."
    n 1fcsbglsbl "{i}Our{/i} chapters together are way more interesting,{w=0.2} a-{w=0.2}anyway.{w=0.75}{nw}"
    extend 1fchsmlsbl " Ehehe."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 3nlrsmleme
    $ Natsuki.clearDesk()
    $ manga_closed = jn_desk_items.getDeskItem("jn_parfait_manga_closed")
    $ Natsuki.setDeskItem(manga_closed)
    play audio book_closing
    $ jnPause(0.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    n 7ulrssl "So...{w=1}{nw}"
    $ chosen_tease = jn_utils.getRandomTease()
    extend 7fchbgl " what's new,{w=0.2} [chosen_tease]?"

    return

# AFFECTIONATE/ENAMORED greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_good_to_see_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_good_to_see_you:
    n 1uchbgl "[player]!{w=0.2} You're back!"
    n 3fchsml "Let's make today amazing as well,{w=0.2} 'kay?{w=0.3} Ehehe."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_couldnt_resist",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_couldnt_resist:
    n 3fsqsml "Well hey,{w=0.2} [player].{w=0.5}{nw}" 
    extend 3tsqssl " Back so soon?"
    n 3fcsctl "I knew you obviously just couldn't resist.{w=0.75}{nw}"
    extend 3fcssmledz " Ehehe."
    n 4tsqssl "So...{w=1}{nw}"
    extend 2fchbgl " what do you wanna do today?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_just_cant_stay_away",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_just_cant_stay_away:
    n 1usqbgl "Well,{w=0.2} well,{w=0.2} well.{w=0.5}{nw}" 
    extend 2fsqbgl " What do we have here?"
    n 2tsqctl "You just can't stay away from me,{w=0.2} can you?" 
    n 2ksqbgl "Not that I blame you,{w=0.2} obviously.{w=0.5}{nw}"
    extend 2fchtsledz " I guess I just {i}have{/i} that effect on people."
    n 4fchgnlelg "Ehehe."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_have_so_much_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_have_so_much_fun:
    n 1uchbgleme "It's [player]!"
    n 3fcssml "We're gonna have so much fun today!{w=0.5}{nw}" 
    extend 3nchsml " Ehehe."
    n 3fchbgl "So!{w=0.2} what did you wanna talk about?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_everything_is_fine",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_everything_is_fine:
    n 1uwdgslesu "[player]!{w=0.5}{nw}" 
    extend 4ullajlsbr " You're back!"
    n 2fsqpol "You kept me waiting {i}again{/i},{w=0.2} you know..."
    n 2fcsbgl "But...{w=0.5} at least my patience paid off.{w=0.75}{nw}"
    extend 2fcssmleme " Ehehe."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_not_surprised",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_not_surprised:
    n 2tsqaj "Oh?{w=0.75}{nw}"
    extend 2csqbg " You're back again,{w=0.2} [player]?{w=0.75}{nw}"
    extend 2fsqsm " Ehehe."
    n 4ullfl "Well...{w=0.75}{nw}"
    extend 4cllssl " not like I can say I'm surprised or anything."
    n 3fchgnl "As if you could {i}possibly{/i} resist,{w=0.2} am I right?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_in_for_some_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_in_for_some_fun:
    n 1unmbg "[player]!{w=0.75}{nw}"
    extend 2ccssslsbr " Man...{w=1}{nw}"
    extend 2fcsbglsbr " it's about time you showed up!"
    n 4fsqsml "Ehehe.{w=0.75}{nw}"
    extend 3fchbgleme " Now I {i}know{/i} we're in for some fun!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_good_taste",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "3fsgsm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_good_taste:
    n 3fcsct "Oh?{w=0.75}{nw}"
    extend 3fsqbg " And just look who decided to drop into the clubroom today,{w=0.2} huh?"
    n 3fcssmesm "..."
    n 4tllbg "Well,{w=0.2} what can I say?"
    n 2uchgnl "Looks like you've got {i}some{/i} good taste after all,{w=0.2} [player]!{w=0.75}{nw}"
    extend 2nchgnl " Ahaha."

    if Natsuki.isEnamored(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fchbll "Get comfy already,{w=0.2} [chosen_tease]!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_crawling_back",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2nsrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_crawling_back:
    n 4unmbs "[player]!{w=0.75}{nw}"
    extend 7fchgn " I was wondering when you were gonna show up!"
    n 3fcsajlsbr "N-{w=0.2}not that I was just sat around waiting for you or anything,{w=0.2} obviously."
    n 3fslsslsbr "After all..."
    n 6fcssmlesm "As {i}if{/i} you could resist crawling back to someone as awesome as me!"

    if Natsuki.isEnamored(higher=True):
        n 3nchgnl "Now get cozy already,{w=0.2} you dork!"
    
    else:
        n 3fchsmeme "Ehehe."
    
    return

# NORMAL/HAPPY greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_up",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_up:
    n 1uwdajesu "Oh!{w=0.5}{nw}"
    extend 4ulrsssbr " Hey,{w=0.2} [player]!"
    n 3unmbo "What's up?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_glad_to_see_you",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_glad_to_see_you:
    n 1uchsm "Hey,{w=0.2} [player]!"
    n 4nllsssbr "I was just wondering when you'd drop by again."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_spacing_out",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_spacing_out:
    n 1kllpu "..."
    n 1uwdajlesu "Huh?"
    n 1uchbglesd "O-{w=0.2}oh!{w=0.5}{nw}" 
    extend 4fchssl " Hi,{w=0.2} [player]!"
    n 4nllsssbr "I...{w=1}{nw}" 
    extend 2fllpolsbr " was just kinda spacing out a little."
    n 3unmbol "So...{w=0.3} what's new?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_heya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_heya:
    n 1fcsbg "Heya,{w=0.2} [player]!"
    n 3tnmss "What's up?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_knew_youd_be_back",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_knew_youd_be_back:
    n 1unmbg "It's [player]!{w=0.2} Hi!"
    n 2fcsbglesssbr "I-{w=0.1}I knew you'd be back,{w=0.2} obviously."
    n 2fcssml "You'd have to have no taste to not visit again.{w=0.75}{nw}" 
    extend 2fcsbgl " Ahaha!"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_sup_player",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_sup_player:
    n 1unmboesu "Eh?{w=0.5}{nw}"
    n 1unmaj "Oh.{w=0.5}{nw}"
    extend 1tnmaj " Hey,{w=0.2} [player]."
    n 2tllss "What's up?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_wake_up_nat",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "4nslsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_wake_up_nat:
    n 4nslpu "..."
    n 4kslpu "..."
    n 1kcsbo "..."
    n 1ncsaj "..."
    n 1ncspu "..."
    n 1ncsem "..."
    n 1ncspu "..."
    n 1ncsemesl "..."
    n 1kcsemesl "Mmm...{w=1}{nw}"
    extend 1kwlemesl " nnnn?"
    n 4uskwrleex "O-{w=0.3}Oh!{w=0.5}{nw}"
    extend 4fllbglsbl " [player]!"
    n 4flrbgesssbr "H-{w=0.3}hey!{w=0.5}{nw}"
    extend 2tnmsssbl " What did I miss?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_oh_whats_up",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "2tlrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_oh_whats_up:
    n 2tlrsl "..."
    n 2tnmpueqm "...Huh?{w=0.5}{nw}"
    extend 4unmfllesu " Oh!{w=0.75}{nw}"
    extend 4cllsslsbr " [player]!"
    n 2cchsssbr "W-{w=0.2}what's up?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_new",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7cdlsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_new:
    n 7unmfllesu "Ah!{w=0.75}{nw}"
    extend 7flrsssbr " [player]!{w=0.75}{nw}"
    extend 3ccsajsbr " I-{w=0.2}I was wondering when you were gonna decide to show up."

    if Natsuki.isHappy(higher=True):
        n 3tllajsbr "So...{w=1}{nw}"
        extend 3fchbgsbr " what's new,{w=0.2} [player]?"

    else:
        n 3cllbosbr "..."
        n 3cllajsbr "So...{w=1}{nw}"
        extend 7tnmss " what's new with you,{w=0.2} huh?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_nevermind",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7clrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_nevermind:
    n 7cdrsl "..."
    n 7csrsl "..."
    n 7ksrbo "..."
    n 7kcsflesi "..."
    n 7ksqsleqm "...?{w=0.75}{nw}"
    n 7unmemlesh "Oh!{w=0.75}{nw}"
    extend 3cslsssbr " Heh.{w=0.75}{nw}"
    extend 3ccssssbr " H-{w=0.2}hey, [player]."
    n 7unmflsbr "Me?{w=0.2} I was just..."
    n 3cdrslsbr "..."
    n 4ccsflsbr "N-{w=0.2}nevermind.{w=0.75}{nw}"

    if Natsuki.isHappy(higher=True):
        extend 4nsrbosbr " I guess it doesn't matter now anyway."
        n 2tlraj "So...{w=1}{nw}"
        extend 2tnmss " what's going on,{w=0.2} [player]?"

    else:
        extend 4csrbosbr " It's nothing."
        n 2nsrca "..."
        n 2nlraj "So...{w=1}{nw}"
        extend 2unmaj " what did I miss,{w=0.2} [player]?"

    return

# DISTRESSED/UPSET greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_its_you",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_its_you:
    n 1ndtsl "Oh.{w=1}{nw}" 
    extend 2fsqsl " It's you."
    n 2fnmsl "Hello,{w=0.5} {i}[player]{/i}."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_hi",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_hi:
    n 1nplsl "{i}[player]{/i}.{w=0.5}{nw}" 
    extend 2fsqsl " Hi."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_welcome_back_i_guess",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_welcome_back_i_guess:
    n 2nsqsl "[player].{w=0.75}{nw}" 
    extend 2flrsr " Welcome back,{w=0.2} I {i}guess{/i}."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_better_be_good",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_better_be_good:
    n 1nsqaj "Huh.{w=0.75}{nw}" 
    extend 1fsqsr " [player]."
    n 3fnmsl "This better be good."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_you_came_back",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_you_came_back:
    n 1tsqaj "Oh?{w=0.2} You came back?"
    n 3fslem "...I wish I could say I was happy about it."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_great",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_great:
    n 1cslsl "..."
    n 1csqboeqm "...?"
    n 2clrfl "Oh.{w=0.75}{nw}"
    extend 2clrem " Great."
    n 4csqem "It's{w=0.25}{nw}" 
    extend 4fsqsl " {i}you{/i}."

    return

# BROKEN- greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_oh_its_you",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_oh_its_you:
    n 4kplsrtdr "...?"
    n 2fcsanltsa "Oh...{w=0.3} it's you."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_nothing_to_say:
    n 4fcsanltsa "..."
    n 4fsqfultsb "..."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_why",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_why:
    n 1fplfrltdr "...Why?"
    n 4fcsupltsa "Why did you come back,{w=0.2} [player]?"

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_enough_on_my_mind",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_enough_on_my_mind:
    n 2fnmunltdr "...?"
    n 2fcsupltsd "As if I didn't have enough on my mind..."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_leave_me_be",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_leave_me_be:
    n 1fcsfultsa "I'm so {i}sick{/i} of this."
    n 2kcsupltsd "Why can't you just leave me be..."

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_just_leave_me_alone",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_just_leave_me_alone:
    n 1fsqunltsbeqm "...?{w=0.75}{nw}"
    n 4fcsupltsa "Oh,{w=0.2} for-!"
    n 4cslupltsb "Why can't you just leave me alone..."

    return

# Admission-locked greetings; used when Natsuki made the player leave due to tiredness, etc.

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_sick",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "admission_type": jn_admissions.TYPE_SICK,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_sick:
    n 1unmajlesu "Oh!{w=0.5}{nw}"
    extend 2knmbgl " [player]!{w=0.3} Hey!"
    show natsuki 2knmbol

    menu:
        n "How're you feeling?{w=0.2} Any better?"

        "Much better, thanks!":
            n 2fcsbgsbr "Good,{w=0.2} good!{w=0.3} I-{w=0.2}I knew you'd see the back of it soon!{w=0.5}{nw}"
            extend 2fcsaj " Being ill is gross,{w=0.2} right?"
            n 4nllaj "Now...{w=1}{nw}"
            extend 3fsqbgl " since that's out of the way,{w=0.2} how about we spend some actual quality time together?"
            n 4fsqblleme "Gotta make up for lost plans,{w=0.2} no?"

            $ persistent.jn_player_admission_type_on_quit = None

        "A little better.":
            n 2kslpo "...I'll admit,{w=0.2} that wasn't really what I wanted to hear."
            n 2ullbo "But...{w=0.5}{nw}" 
            extend 2klrbosbl " I'll take 'a little' over not at all,{w=0.2} I guess."
            n 4fchbgsbl "Anyway...{w=0.3} welcome back,{w=0.2} [player]!"

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK

        "Still unwell.":
            n 2knmsr "Still not feeling up to scratch,{w=0.2} [player]?"
            n 2klrsll "I don't {i}mind{/i} you being here...{w=0.3} but don't strain yourself,{w=0.2} alright?"
            n 3kslsllesosbr "I don't want you making yourself worse for my sake..."

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_tired",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "admission_type": jn_admissions.TYPE_TIRED,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_tired:
    n 4unmajesu "Ah!{w=0.5}{nw}"
    extend 4uchbg " [player]!{w=0.2} Hi!"
    show natsuki 4fchbg

    menu:
        n "How're you feeling? Any less tired?"

        "Much better, thanks!":
            n 1nchsm "Ehehe.{w=0.5}{nw}" 
            extend 2usqsm " Nothing like a good night's sleep,{w=0.2} am I right?"
            n 2fcsbg "Now then!{w=1}{nw}" 
            extend 4fsqbg " Seeing as you're finally awake and alert..."
            n 2fchsmledz "It's time for some more fun with yours truly!"

            $ persistent.jn_player_admission_type_on_quit = None

        "A little tired.":
            n 1knmsl "Oh...{w=1}{nw}" 
            extend 4kllajsbr " that's not exactly what I was {i}hoping{/i} to hear,{w=0.2} I'll be honest."
            n 2fcsslsbr "Mmm..."
            n 2knmaj "Then...{w=0.3} perhaps you could grab something to wake up a little?"
            n 2fchbgsbl "A nice glass of water or some bitter coffee should perk you up in no time!"

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED

        "Still tired.":
            n 3knmsl "Still struggling with your sleep,{w=0.2} [player]?"
            n 3kllaj "I don't {i}mind{/i} you being here...{w=1}{nw}" 
            extend 3knmsl " but don't strain yourself,{w=0.2} alright?"
            n 4kslbosbl "I don't want you face-planting your desk for my sake..."

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return

# Absence-related greetings; used when the player leaves suddenly, or has been gone an extended period

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sudden_leave",
            unlocked=True,
            category=["Apology"],
            additional_properties={
                "apology_type": jn_apologies.ApologyTypes.sudden_leave,
                "expression": "4fslbol"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 4kwmsrl "..."
        n 4kwmsrl "[player]."
        n 4knmsll "Come on.{w=0.75}{nw}" 
        extend 4ksqbol " You know you're better than that."
        n 4ncseml "I-{w=0.2}I don't know if something happened or what,{w=0.75}{nw}" 
        extend 4knmajl " but please..."
        n 1knmsll "...Try to remember to say goodbye properly next time.{w=0.5}{nw}"
        extend 2knmbol " Okay?"
        n 2ksrbol "It'd mean a lot to me."

    elif Natsuki.isNormal(higher=True):
        n 1fsqsr "..."
        $ player_initial = jn_utils.getPlayerInitial()
        n 4fnmem "[player_initial]-[player]!{w=0.75}{nw}" 
        extend 4knmem " Do you even know how scary it is when you just vanish like that?"
        n 2kllsf "Seriously...{w=0.75}{nw}" 
        extend 2knmaj " just remember to say goodbye properly when you gotta leave."
        n 4fnmslsbr "I'm really {i}not{/i} asking for much,{w=0.5}{nw}"
        extend 4kslslsbr " you know..."

    elif Natsuki.isDistressed(higher=True):
        n 2fsqsf "..."
        n 2fsqaj "You know I hate that,{w=0.2} [player]."
        n 2fsqsl "Knock it off,{w=0.2} will you?"
        n 2fsqsf "Thanks."

    else:
        n 2fcsuntsa "..."
        n 2fsquntsb "Heh.{w=0.2} Yeah."
        $ chosen_insult = jn_utils.getRandomInsult().capitalize()
        n 2fsruptsb "Welcome back to you,{w=0.2} too.{w=0.75}{nw}" 
        extend 2fsrgttsb " [chosen_insult]."

    $ Natsuki.addApology(jn_apologies.ApologyTypes.sudden_leave)
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_prolonged_leave",
            unlocked=True,
            category=["Apology"],
            additional_properties={
                "apology_type": jn_apologies.ApologyTypes.prolonged_leave,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_prolonged_leave:
    $ player_initial = jn_utils.getPlayerInitial()

    if Natsuki.isEnamored(higher=True):
        n 1uwdwrf "[player_initial]-{w=0.1}[player]!"
        n 4fbkwrf "W-{w=0.3}where were you?!{w=0.5}{nw}" 
        extend 4kllemlsbl " You had me worried {i}sick{/i}!"
        n 1kcsunl "..."
        n 1fcsunl "I'm...{w=0.5}{nw}"
        extend 2kplunl " glad...{w=0.3} you're back,{w=0.2} [player]."
        extend 2kcseml " Just..."
        n 4klrsflsbl "...Don't just suddenly disappear for so long."
        n 2fcsunf "I hate having my heart played with like that..."

    elif Natsuki.isNormal(higher=True):
        n 1uwdwr "[player_initial]-{w=0.1}[player]!"
        n 4fnman "What the hell?!{w=0.5}{nw}"
        extend 4fnmfu " Where have you been?!{w=0.5}{nw}" 
        extend 1fbkwrless " I was worried sick!"
        n 2fcsupl "J-{w=0.3}just as a friend,{w=0.5} but still!"
        n 2fcsun "...{w=1.5}{nw}"
        n 1kcspu "..."
        n 2fllunlsbl "...Welcome back,{w=0.2} [player]."
        n 2kslbosbl "Just...{w=1.25}{nw}"
        extend 2knmaj " don't leave it so long next time,{w=0.2} alright?"
        n 4fsrunl "You know I don't exactly get many visitors..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqputsb "[player_initial]-{w=0.1}[player]?"
        n 2fsqsltsb "...You're back."
        n 2fcsfutsb "Just {i}perfect{/i}."

    else:
        n 2fsquptdr "..."
        n 4fcsfutsd "...."
        
    $ Natsuki.addApology(jn_apologies.ApologyTypes.prolonged_leave)
    return

# Time-of-day based greetings

# Early morning

# Natsuki questions why the player is up so early
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_early_morning_why_are_you_here",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_early_morning_why_are_you_here:
    n 1uwdajlesh "H-{w=0.1}huh?{w=0.5}{nw}" 
    extend 3tnmeml " [player]?!"
    n 3fnmpuleqm "What the heck are you doing here so early?"
    n 3tnmpu "Did you have a nightmare or something?"
    n 3tsqsl "Or...{w=0.3} maybe you never slept?{w=0.5}{nw}" 
    extend 3tsrpu " Huh."
    n 4tnmbg "Well,{w=0.2} anyway..."
    n 4kchbgsbr "Morning?{w=0.3} I guess?"

    return

# Morning

# The Earth says hello!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_starshine",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_starshine:
    n 1uchbgl "Good morning,{w=0.2} starshine!"
    n 1kchbgf "The Earth says 'Hello!'"
    n 4fchnvf "..."
    n 4nchdvf "Pfffft-!"
    n 1kchbsl "I'm sorry!{w=0.2} It's just such a dumb thing to say...{w=0.3} I can't keep a straight face!"
    n 4nchsml "Ehehe."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kwmsmf "You really are my starshine though,{w=0.2} [chosen_endearment]."
    n 3uchsmf "Welcome back!"

    return

# Natsuki doesn't like to be kept waiting around in the morning
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_waiting_for_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_waiting_for_you:
    n 1fsqajl "Oh!{w=0.5}{nw}" 
    extend 2fsqcal " Well look who finally decided to show up!"
    n 2flrsll "You {i}do{/i} know I don't like being kept waiting...{w=0.75}{nw}" 
    extend 2fwmsll " right?"
    n 4fsqsml "Ehehe.{w=0.5}{nw}" 
    extend 3fcsssl " You're just lucky you caught me in a good mood..."
    n 3fchgnlelg "You better make it up to me,{w=0.2} [player]~!"

    return

# Natsuki doesn't like a lazy player!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_lazy",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(10, 11)",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_lazy:
    n 1usqct "Oho?{w=0.5}{nw}" 
    extend 2fsqsm " Well look who finally crawled out of bed today!"
    n 2fsqsg "Jeez,{w=0.2} [player]...{w=0.75}{nw}" 
    extend 2fchgn " I swear you're lazier than Sayori sometimes!"
    n 2fcsbg "Well,{w=0.2} better late than never."
    n 3fchbg "Let's make the most of today,{w=0.2} [player]!"
    n 3tsraj "Or...{w=0.75}{nw}" 
    extend 3tsqsssbl " what's left of it?"

    return

# Natsuki uses a silly greeting
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_top_of_the_mornin",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(8, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_top_of_the_mornin:
    n 1unmbg "Oh!{w=0.5}{nw}" 
    extend 1fchbg " It's [player]!"
    n 3fwlsm "Well -{w=0.1} top of the mornin' to you!"
    n 3nchsm "..."
    n 3nsqbo "..."
    n 3tsqss "What?{w=0.75}{nw}"
    extend 3fsqsg " I'm allowed to say dumb things {i}too{/i},{w=0.2} you know."
    n 3nchgn "Ehehe."

    return

# Guten Morgen, Schlafmütze!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_german",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11) and get_topic('talk_learning_languages').shown_count > 0",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_german:
    n 1unmbg "Oh!{w=0.5}{nw}"
    extend 4fchbg " [player]!"
    n 7fcsaw "A-{w=0.2}hem."
    n 1fslss "G-{w=0.1}guten Morgen,{w=0.2} Schlafmuetze."
    n 1fsqcalsbl "..."
    n 2tnmpu "What?{w=0.5}{nw}"
    extend 2tsqsm " Did I get you by surprise?"
    n 2nnmss "Of course I'm still working on my Gemran skills."
    n 2fcssm "Ehehe."
    n 7ntlaj "After all..."
    n 6fwlbg "Der fruehe Vogel faengt den Wurm!{w=0.75}{nw}"
    extend 3fllsm " Or something like that."

    return

# Afternoon

# Natsuki hopes the player is keeping well
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_keeping_well",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_keeping_well:
    n 1nchbg "Hey!{w=0.2} Afternoon,{w=0.2} [player]!"
    n 2unmsm "Keeping well?"

    return

# Natsuki asks how the player's day is going
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_how_are_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_how_are_you:
    n 1nchbg "Oh!{w=0.2} Afternoon,{w=0.2} [player]!"
    n 2uchsm "How're you doing today?"

    return

# Evening

# Natsuki tells the player they can relax now
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_long_day",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.HAPPY, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_long_day:
    n 4unmbg "Aha!{w=0.5}{nw}" 
    extend 4fchbg " Evening,{w=0.2} [player]!"
    n 2ksgsg "Long day,{w=0.2} huh?{w=0.5}{nw}" 
    extend 2fcssm " Well,{w=0.2} you've come to the right place!"
    n 2nchbg "Just tell [n_name] all about it!"

    return

# Natsuki teases the player for taking so long
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_took_long_enough",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_took_long_enough:
    $ chosen_tease = jn_utils.getRandomTease()
    n 4fsqgs "[player]!{w=0.5}{nw}"
    extend 4fsqsr " There you are,{w=0.2} [chosen_tease]!"
    n 2fcspo "Jeez...{w=0.75}{nw}" 
    extend 2fsrpo " took you long enough!"
    n 2fsqsm "Ehehe."
    n 4uchbg "I'm just kidding!{w=0.2} Don't worry about it."
    n 3nchsm "Welcome back!"

    return

# Night

# Natsuki enjoys staying up late too
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_up_late",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_up_late:
    n 1unmajeex "Oh!{w=0.75}{nw}"
    extend 4fchbgsbl " Hey,{w=0.2} [player]."
    n 3tnmss "Late night for you too,{w=0.2} huh?"
    n 3ullss "Well...{w=0.75}{nw}" 
    extend 3nchgn " I'm not complaining!" 
    n 3fchsm "Welcome back!"

    return

# Natsuki is also a night owl
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_night_owl",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_night_owl:
    n 1unmajesu "Oh!{w=0.3} [player]!{w=1}{nw}"
    extend 3fllsslsbl " You're a night owl too,{w=0.2} huh?"
    n 3fcsbg "N-{w=0.2}not that I have a problem with that,{w=0.2} obviously." 
    extend 4nchgnl " Welcome back!"

    return

# Natsuki is somewhat concerned about the player being up late again
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_what_time_do_you_call_this",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 23 or store.jn_get_current_hour() <= 4",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "expression": "2fsqsf"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_what_time_do_you_call_this:
    n 2fnmgs "[player]!{w=0.75}{nw}"
    extend 2fcsgs " Come on!{w=0.75}{nw}"
    extend 2fsqan " Are you {i}kidding me{/i}?"
    n 4fsqwr "What kind of time do you call {i}this{/i} then?{w=0.75}{nw}"
    extend 4fnmwr " Huh?"
    n 1fsqsl "..."
    n 2fsqgs "Well?{w=0.75}{nw}"
    extend 2fcsgs " Let's hear it already!{w=0.5} Spit it out!"
    n 2fsqbo "..."
    n 2fsqcs "..."
    n 2fchdvesi "Pffft-!"
    n 1flrbg "Man...{w=1}{nw}"
    extend 4nchgn " I swear that {i}never{/i} gets old."
    n 4cllss "But...{w=1}{nw}"
    extend 3cnmfl " for real,{w=0.2} [player]?"
    n 3ccsflesi "..."
    n 3ccspu "Just..." 
    extend 4clrsl " don't overdo it.{w=0.75}{nw}"
    extend 4cnmbo " Alright?{w=1.25}{nw}"
    extend 5cslbolsbr " Seriously."

    if Natsuki.isEnamored(higher=True):
        $ emphasis = " really" if Natsuki.isLove(higher=True) else ""
        n 3ccsfllsbr "I[emphasis] don't wanna hear about you missing something important just because you couldn't drag your butt out of bed later."
        n 3ccspolsbr "You dork."
        n 4csrbolsbr "..."
        n 4nsrajl "So...{w=1}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 7tnmbol " what did you wanna talk about,{w=0.2} [chosen_descriptor]?"

    else:
        n 7ccspol "Besides.{w=0.75}{nw}"
        extend 3fchgnl " It's {i}totally{/i} on you if you can't get your sleep-deprived butt out of bed later!"
        n 3fsqsml "Ehehe."

    return

# Sanjo

# Sanjo getting some morning care from the club's newest (and only) gardener!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sanjo_morning",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(7, 10) and jn_desk_items.getDeskItem('jn_sanjo').unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_sanjo",
                "expression": "2udlsmeme"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sanjo_morning:
    n 2unmaj "Ah!{w=0.75}{nw}"
    extend 2fchbg " Morning,{w=0.2} [player]!{w=0.75}{nw}"
    extend 2unmss " What's up?"
    n 4fcssm "Don't mind me.{w=0.75}{nw}"
    extend 3nchgn " Just making sure Sanjo is getting some top-quality care!"

    if Natsuki.isEnamored(higher=True):
        n 3flrbg "Yeah,{w=0.2} yeah.{w=0.75}{nw}"
        $ chosen_tease = jn_utils.getRandomTease()
        extend 3fnmss " Keep your shirt on,{w=0.2} [chosen_tease].{w=1}{nw}"
        extend 4fsqsm " I know."
        n 7fcsbgl "You must be {i}pretty{/i} desperate for my attention too if you're up already,{w=0.5}{nw}" 
        extend 7fchgnl " huh?"

    return

# Sanjo getting some morning care
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sanjo_generic",
            unlocked=True,
            conditional="jn_desk_items.getDeskItem('jn_sanjo').unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_sanjo",
                "expression": "2fcssmeme"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sanjo_generic:
    n 2ccssmeme "...{w=0.75}{nw}"
    n 2tsqboeqm "...?{w=0.75}{nw}"
    n 4unmfllesu "O-{w=0.2}oh!{w=0.75}{nw}"
    extend 4flrbglsbl " [player]!{w=0.75}{nw}"
    extend 1ccssslsbl " Heh."
    n 3ccsbgsbl "Don't worry.{w=0.75}{nw}"
    extend 3ccssm " Sanjo and I were juuuust about done here."
    
    if not jn_is_day():
        n 5clrajsbr "N-{w=0.2}not that I completely forgot to water him before or anything like that,\n{w=0.5}{nw}"
        extend 2fcscasbr "{i}obviously{/i}."

    if Natsuki.isEnamored(higher=True):
        n 1ullaj "So...{w=1}{nw}"
        extend 3unmbo " what's new with you,{w=0.2} [player]?"
        n 6fcsbgl "...Or are you just looking for some {i}quality care{/i} too?"
        n 7fchsml "Ehehe."

    else:
        n 1ullaj "So..."
        n 3tnmss "What's new,{w=0.2} [player]?"

    return
