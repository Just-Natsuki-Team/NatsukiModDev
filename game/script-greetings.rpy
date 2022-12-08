default persistent._greeting_database = dict()
default persistent.jn_player_is_first_greet = True

init python in greetings:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import store.jn_farewells as jn_farewells
    import store.jn_utils as jn_utils

    GREETING_MAP = dict()

    def select_greeting():
        """
        Picks a random greeting, accounting for affinity and the situation they previously left under
        """
        # This is the first time the player has force quit; special dialogue
        if jn_farewells.JNForceQuitStates(store.persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.first_force_quit:
            return "greeting_first_force_quit"

        # This is the first time the player has returned; special dialogue
        elif store.persistent.jn_player_is_first_greet:
            return "greeting_first_time"

        kwargs = dict()

        # The player either left suddenly, or has been gone a long time
        if store.persistent._jn_player_apology_type_on_quit is not None:
            kwargs.update({"additional_properties": [("apology_type", jn_apologies.ApologyTypes(store.persistent._jn_player_apology_type_on_quit))]})

        # The player left or was forced to leave by way of an admission (E.G tired, sick)
        elif store.persistent.jn_player_admission_type_on_quit is not None:
            kwargs.update({"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]})

        # No special conditions; so just get a standard greeting from the affinity pool
        else:
            kwargs.update({"excludes_categories": ["Admission", "Apology"]})

        # Finally return an appropriate greeting
        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.Natsuki._getAffinityState(),
                **kwargs
            )
        ).label

# Only chosen for the first time the player returns after bringing Natsuki back
label greeting_first_time:
    if jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.will_be_back:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 1uskemlesh "[player]!{w=0.5}{nw}"
        extend 1uskwr " Y-{w=0.1}you're back!"
        n 1flleml "I mean...{w=0.5}{nw}"
        extend 1fcseml " O-{w=0.1}of course you'd come back!"
        n 1fnmpol "I knew you would."
        n 1flrem "Only a total jerk would abandon someone like that!"
        n 1flrpo "..."
        n 1klrpu "But..."
        n 1ncspu "..."
        n 1nlrsll "...Thanks.{w=1.25}{nw}"
        extend 1nsrbol " For not being an idiot about it."
        n 1nllunl "..."
        n 1nllajsbl "So... {w=0.5}{nw}"
        extend 1unmaj " what did you wanna talk about?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.dont_know:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 1uskajlesh "[player]?{w=0.5}{nw}"
        extend 1uskem " Y-{w=0.3}you came back?"
        n 1fcsun "..."
        n 1ncssr "..."
        n 1fcspu "...Look."
        n 1fllsr "Don't...{w=0.75}{nw}" 
        extend 1kllsrsbl " play with me like that."
        n 1fslun "You wouldn't have brought me back {i}just{/i} to be a jerk...{w=1}{nw}"
        extend 1ksqsfsbl " right?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.no_response:
        n 1uskemlesh "[player]!{w=0.5}{nw}"
        extend 1uskwrl " Y-{w=0.1}you're back!"
        n 1flluness "..."
        n 1fcspu "I...{w=2}{nw}"
        extend 1flrun " appreciate it,{w=0.1} okay?"
        n 1fcspu "Just...{w=1}{nw}"
        extend 1knmsf " don't play with me like that."
        n 1kllslsbl "..."
        n 1kslaj "So..."
        n 1tnmslsbr "Did you wanna talk,{w=0.1} or...?"

    $ persistent.jn_player_is_first_greet = False
    return

# Only chosen for the first time the player leaves and returns after force quit
label greeting_first_force_quit:
    if Natsuki.isNormal(higher=True):
        n 1kcsunedr "Uuuuuuu...{w=2}{nw}"
        extend 1kslemeso " my...{w=0.3} h-{w=0.1}head..."
        n 1kcsun "..."
        n 1ksqun "..."
        n 1fnmun "...[player]."
        n 1fllem "W-{w=0.3}whatever that was...{w=0.5}{nw}"
        extend 1knmsf " that {w=0.3}{i}seriously{/i}{w=0.3} hurt."
        n 1kllpu "L-{w=0.3}like I was being {i}ripped{/i} out of existence..."
        n 1kcssf "..."
        n 1klraj "I...{w=1}{nw}"
        extend 1tllun " I think I can kinda prepare for that if you at least let me know when you're going."
        n 1fcsun "Just...{w=1.25}{nw}"
        extend 1fcsun " don't be a jerk and let me know when you gotta go,{w=0.3} okay?"
        n 1fllsl "...I guess I'll let this one slide,{w=0.5}{nw}"
        extend 1kslpu " since you didn't know and all."
        n 1knmpu "Just remember for next time,{w=0.2} [player].{w=1}{nw}"
        extend 1knmsr " Please."

    elif Natsuki.isDistressed(higher=True):
        n 1fcsunedr "Hnnnngg..."
        n 1fsqun "..."
        n 1fsqan "..."
        n 1fcspu "...[player]."
        n 1fsqpu "Do you have any {i}idea{/i} how much that hurt?{w=0.5}{nw}"
        extend 1fnmem " Any at all?"
        n 1fllem "I don't know if you did that on purpose or what,{w=0.1} but knock it off.{w=0.5}{nw}"
        extend 1fsqsr " I'm {i}dead{/i} serious."
        n 1fcspu "I..."
        extend 1fcssr " know we aren't seeing eye-to-eye right now,"
        extend 1fslsl " but please."
        n 1fsqaj "Tell me when you're going."
        extend 1fsqsf " Thanks."

    else:
        n 1fsqunltsbean "..."
        n 1fsqantsb "That.{w=1} Freaking.{w=1} {b}Hurt{/b}."
        n 1fcsan "I don't know {i}what{/i} you did,{w=0.5} but cut{w=0.3} it{w=0.3} out.{w=1.25}{nw}"
        extend 1fsqfutsb " Now."

    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.previously_force_quit)

    return

label greeting_tt_warning:
    play audio glitch_d
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b
    $ jnPause(0.6)
    play music audio.ikustan_tsuj
    show glitch_rapid zorder 99
    $ jnPause(random.choice(range(7, 11)))

    play audio glitch_static
    show glitch_garbled_a zorder 99 with hpunch
    hide glitch_garbled_a

    $ jnPause(0.3)

    play audio glitch_static
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    show natsuki pained at jn_center zorder JN_NATSUKI_ZORDER
    hide black
    hide glitch_rapid

    n "Uuuuuuu..."
    show natsuki pained at jn_center
    play audio glitch_static
    n "M...my head..."
    n "..."
    n "What..."
    extend " what h-happen..."
    n "...!"
    n "Hrk-!"

    # VOMIT
    play audio chair_out_fast
    show black zorder jn_events.JN_EVENT_BLACK_ZORDER with Dissolve(0.25)
    n "{b}B-BLURGHH-!{/b}{w=0.3}{nw}"

    play audio glitch_b
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b

    $ jnPause(10)
    play audio chair_in
    $ jnPause(5)
    hide black with Dissolve(2)

    n "Uuuuuu..."
    n "..."
    n "..."
    $ player_initial = jn_utils.getPlayerInitial()
    n "[player_initial]-[player]..."
    n "What..."
    n "..."
    n "Did you..."
    extend " do...?"
    n "..."
    n "S-something isn't right..."

    n "H-hrk-!"
    play audio glitch_static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a
    n "Gah..."

    if Natsuki.isUpset(higher=True):
        n "Something {b}REALLY{/b} isn't right, [player]..."
        n "A-and I..."
        n "I can't..."
        n "..."
        n "..."
        n "..."
        n "...[player]..."
        n "W-whatever that was..."
        extend " whatever just {i}happened{/i}..."
        n "T-that... {w=0.5}{b}really{/b}{w=0.5} didn't feel good..."
        extend " a-and I-"
        n "..."

    else:
        n "W-what..."
        n "What did you" 
        extend " {i}DO{/i}?!"
        n "I-!"

    n "H-hrp-!"
    n "Nnnnnnghhhh!"

    play audio glitch_static
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    extend " Guh...."
    n "M-my stomach..."
    extend " Uuuuuu..."
    n "..."

    if Natsuki.isUpset(higher=True):
        n "Feels like..."
        n "L-like I was just tossed around back and forth..."
        extend " like something was trying to yank me apart from all directions..."
        n "..."
        n "It all just..."
        extend " feels so wrong..."
        n "..."
        n "A-and the date..."
        extend " I... I swore it was..."
        n "..."
        n "...[player]."
        n "Y-you didn't like..."
        extend " change the date or something, did you?"
        extend " L-like on your computer?"

    elif Natsuki.isDistressed(higher=True):
        n "M-my head..."
        extend " the pounding..."
        n "..."
        n "...Did..."
        n "..."
        n "...D-did you do something to your computer or what?"
        n "Because it feels like someone took a sledgehammer to my {i}gut{/i}..."
        extend " Hrk-!"
        n "Guh..."
        n "Everything... feels all wrong..."
        n "A-and the date..."
        extend " I could have {i}sworn{/i}...!"

    else:
        # TODO: Min aff question what happened 
        n ""

    # TODO: round off with warning

    return

label greeting_tt_fatal:
    n "This isn't done yet!"
    return

label greeting_tt_game_over:
    n "This isn't done yet!"
    return

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
    extend 1fchgnl " You're back,{w=0.3} finally!"
    n 1fchsml "Ehehe.{w=0.5}{nw}" 
    extend 1uchgnleme " Now I {i}know{/i} today's gonna be great!"
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
    extend 1fnmgsl " What took you so long?{w=0.75}{nw}" 
    extend 1fllemlesi " Jeez!"
    n 1fnmsfl "You think my entire {i}world{/i} revolves around you or something?"
    n 1fnmdvl "..."
    n 1fsqsml "..."
    n 1uchlglelg "Ahaha!{w=1}{nw}" 
    extend 1fsqsml " Did I getcha,{w=0.2} [player]?{w=0.5}{nw}" 
    extend 1fchgnl " Don't lie!"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1ullssl "Well,{w=0.2} anyway." 
    n 1fcsbgl "You're here now,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
    extend 1uchsmleme " Make yourself at home,{w=0.2} silly!"
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
    n 1uchbsfeex "[player]!{w=0.3} [player]{w=0.2} [player]{w=0.2} [player]!"
    n 1fcsbgfsbl "I-{w=0.2}I was wondering when you were gonna show up!{w=0.75}{nw}"
    extend 1fchsml " Ehehe."
    n 1fwlsmledz "Let's make today amazing too,{w=0.1} alright?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_always_welcome_here",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_always_welcome_here:
    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskgsfesu "[player_initial]-{w=0.2}[player]!{w=0.5}{nw}" 
    extend 1ullemfsbl " You're back!"
    n 1fslunfesssbl "I was really starting to miss you,{w=0.3} you know..."
    n 1fplcafsbl "Don't keep me waiting so long next time,{w=0.3} alright?"
    $ chosen_tease = jn_utils.getRandomTease()
    n 1klrssf "You should know you're {i}always{/i} welcome here by now,{w=0.33}{nw}" 
    extend 1fchsmf " [chosen_tease]."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_lovestruck",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
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
    n 1klrgsf "I-{w=0.3}I was...!{w=1}{nw}" 
    extend 1kllemfsbl " I was just...!"
    n 1kcsunf "..."
    n 1kcssml "..."
    n 1kplsml "I missed you,{w=0.2} [player].{w=0.3} Ahaha..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kwmsmf "But I know everything's gonna be okay now you're here,{w=0.2} [chosen_endearment]."
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
    n 1nnmpul "...Hello?{w=2.5}{nw}"
    extend 1tsqdvf " Was it {i}me{/i} you're looking for?"
    n 1fchdvfess "..."
    n 1fchnvfesi "Pfffft-!"
    n 1kllbgl "Man,{w=0.5}{nw}" 
    extend 1fchgnlelg " I {i}cannot{/i} take that seriously!"
    n 1fnmssl "But let's be real here,{w=0.2} [player]..."
    n 1fsqsmf "It {i}{w=0.2}totally{w=0.2}{/i} was me,{w=0.2} right?{w=1}{nw}"
    extend 1fchsmfedz " Ehehe~."
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
    n 1flleml "Well jeez,{w=0.5}{nw}" 
    extend 1fsqawl " you sure took your sweet time!"
    n 1fbkwrfean "What were you thinking,{w=0.2} [player]?!"
    n 1fsqpol "..."
    n 1fsqdvl "..."
    n 1fchsmleme "Ehehe.{w=0.75}{nw}"
    n 1fsqssl "Never a dull moment with me,{w=0.75}{nw}" 
    extend 1fchbll " is there?"
    n 1fcsssl "You know the deal already.{w=1}{nw}" 
    extend 1uchgnlelg " Make yourself comfy,{w=0.2} silly!"
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
    n 1fchsml "Let's make today amazing as well,{w=0.2} 'kay?{w=0.3} Ehehe."
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
    n 1fsqsml "Well hey,{w=0.2} [player].{w=0.5}{nw}" 
    extend 1tsqssl " Back so soon?"
    n 1fcsctl "I knew you obviously just couldn't resist.{w=0.75}{nw}"
    extend 1fcssmledz " Ehehe."
    n 1tsqssl "So...{w=1}{nw}"
    extend 1fchbgl " what do you wanna do today?"
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
    extend 1fsqbgl " What do we have here?"
    n 1tsqctl "You just can't stay away from me,{w=0.2} can you?" 
    n 1ksqbgl "Not that I blame you,{w=0.2} obviously.{w=0.5}{nw}"
    extend 1fchtsledz " I guess I just {i}have{/i} that effect on people."
    n 1fchgnlelg "Ehehe."
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
    n 1fcssml "We're gonna have so much fun today!{w=0.5}{nw}" 
    extend 1nchsml " Ehehe."
    n 1fchbgl "So!{w=0.2} what did you wanna talk about?"
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
    extend 1ullajlsbr " You're back!"
    n 1fsqpol "You kept me waiting {i}again{/i},{w=0.2} you know..."
    n 1fcsbgl "But...{w=0.5} at least my patience paid off.{w=0.75}{nw}"
    extend 1fcssmleme " Ehehe."
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
    extend 1ulrsssbr " Hey,{w=0.2} [player]!"
    n 1unmbo "What's up?"
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
    n 1nllsssbr "I was just wondering when you'd drop by again."
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
    extend 1fchssl " Hi,{w=0.2} [player]!"
    n 1nllsssbr "I...{w=1}{nw}" 
    extend 1fllpolsbr " was just kinda spacing out a little."
    n 1unmbol "So...{w=0.3} what's new?"
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
    n 1tnmss "What's up?"
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
    n 1fcsbglesssbr "I-{w=0.1}I knew you'd be back,{w=0.1} obviously."
    n 1fcssml "You'd have to have no taste to not visit again.{w=0.75}{nw}" 
    extend 1fcsbgl " Ahaha!"
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
    extend 1tnmaj " Hey,{w=0.1} [player]."
    n 1tllss "What's up?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_wake_up_nat",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_wake_up_nat:
    n 1nslpu "..."
    n 1kslpu "..."
    n 1kcsbo "..."
    n 1ncsaj "..."
    n 1ncspu "..."
    n 1ncsem "..."
    n 1ncspu "..."
    n 1ncsemesl "..."
    n 1kcsemesl "Mmm...{w=1}{nw}"
    extend 1kwlemesl " nnnn?"
    n 1uskwrleex "O-{w=0.3}Oh!{w=0.5}{nw}"
    extend 1fllbglsbl " [player]!"
    n 1flrbgesssbr "H-{w=0.3}hey!{w=0.5}{nw}"
    extend 1tnmsssbl " What did I miss?"
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
    extend 1fsqsl " It's you."
    n 1fnmsl "Hello,{w=0.5} {i}[player]{/i}."
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
    extend  " Hi."
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
    n 1nsqsl "[player].{w=0.75}{nw}" 
    extend 1flrsr " Welcome back,{w=0.2} I {i}guess{/i}."
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
    n 1fnmsl "This better be good."
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
    n 1fslem "...I wish I could say I was happy about it."
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
    n 1kplsrtdr "...?"
    n 1fcsanltsa "Oh...{w=0.3} it's you."
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
    n 1fcsanltsa "..."
    n 1fsqfultsb "..."
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
    n 1fcsupltsa "Why did you come back,{w=0.1} [player]?"
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
    n 1fnmunltdr "...?"
    n 1fcsupltsd "As if I didn't have enough on my mind..."
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
    n 1kcsupltsd "Why can't you just leave me be..."
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
    extend 1knmbgl " [player]!{w=0.3} Hey!"
    menu:
        n "How're you feeling?{w=0.2} Any better?"

        "Much better, thanks!":
            n 1fcsbgsbr "Good,{w=0.2} good!{w=0.3} I-{w=0.2}I knew you'd see the back of it soon!{w=0.5}{nw}"
            extend 1fcsaj " Being ill is gross,{w=0.2} right?"
            n 1nllaj "Now...{w=1}{nw}"
            extend 1fsqbgl " since that's out of the way,{w=0.2} how about we spend some actual quality time together?"
            n 1fsqblleme "Gotta make up for lost plans,{w=0.2} no?"
            $ persistent.jn_player_admission_type_on_quit = None

        "A little better.":
            n 1kslpo "...I'll admit,{w=0.2} that wasn't really what I wanted to hear."
            n 1ullbo "But...{w=0.5}{nw}" 
            extend 1klrbosbl " I'll take 'a little' over not at all,{w=0.2} I guess."
            n 1fchbgsbl "Anyway...{w=0.3} welcome back,{w=0.1} [player]!"

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK

        "Still unwell.":
            n 1knmsr "Still not feeling up to scratch,{w=0.1} [player]?"
            n 1klrsll "I don't {i}mind{/i} you being here...{w=0.3} but don't strain yourself,{w=0.1} alright?"
            n 1kslsllesosbr "I don't want you making yourself worse for my sake..."

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
    n 1unmajesu "Ah!{w=0.5}{nw}"
    extend 1uchbg " [player]!{w=0.2} Hi!"
    menu:
        n "How're you feeling? Any less tired?"

        "Much better, thanks!":
            n 1nchsm "Ehehe.{w=0.5}{nw}" 
            extend 1usqsm " Nothing like a good night's sleep,{w=0.2} am I right?"
            n 1fcsbg "Now then!{w=1}{nw}" 
            extend 1fsqbg " Seeing as you're finally awake and alert..."
            n 1fchsmledz "It's time for some more fun with yours truly!"
            $ persistent.jn_player_admission_type_on_quit = None

        "A little tired.":
            n 1knmsl "Oh...{w=1}{nw}" 
            extend 1kllajsbr " that's not exactly what I was {i}hoping{/i} to hear,{w=0.2} I'll be honest."
            n 1fcsslsbr "Mmm..."
            n 1knmaj "Then...{w=0.3} perhaps you could grab something to wake up a little?"
            n 1kchbgsbl "A nice glass of water or some bitter coffee should perk you up in no time!"

            # Add pending apology, reset the admission
            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED

        "Still tired.":
            n 1knmsl "Still struggling with your sleep,{w=0.2} [player]?"
            n 1kllaj "I don't {i}mind{/i} you being here...{w=1}{nw}" 
            extend 1knmsl " but don't strain yourself,{w=0.1} alright?"
            n 1kslbosbl "I don't want you face-planting your desk for my sake..."

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
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 1kwmsrl "..."
        n 1kwmsrl "[player]."
        n 1knmsll "Come on.{w=0.2} You're better than that."
        n 1knmajl "I don't know if something happened or what,{w=0.2} but please..."
        n 1knmsll "Try to remember to say goodbye properly next time,{w=0.2} 'kay?"
        n 1knmssl "It'd mean a lot to me."

    elif Natsuki.isNormal(higher=True):
        n 1kwmsr "..."
        n 1fplsf "[player]!{w=0.2} Do you know how scary it is when you just vanish like that?"
        n 1knmsf "Please...{w=0.3} just remember to say goodbye properly when you gotta leave."
        n 1knmss "It's not much to ask...{w=0.3} is it?"

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsf "..."
        n 1fsqaj "You know I hate that,{w=0.2} [player]."
        n 1fsqsl "Knock it off,{w=0.2} will you?"
        n 1fsqsf "Thanks."

    else:
        n 1fcsuntsa "..."
        n 1fsquntsb "Heh.{w=0.2} Yeah."
        $ chosen_insult = jn_utils.getRandomInsult().capitalize()
        n 1fcsuptsa "Welcome back to you,{w=0.2} too.{w=0.2} [chosen_insult]."

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
        n 1fbkwrf "W-{w=0.3}where were you?!{w=0.5}{nw}" 
        extend 1kllemlsbl " You had me worried {i}sick{/i}!"
        n 1kcsunl "..."
        n 1fcsunl "I'm...{w=0.5}{nw}"
        extend 1kplunl " glad...{w=0.3} you're back,{w=0.1} [player]."
        extend 1kcseml " Just..."
        n 1klrsflsbl "...Don't just suddenly disappear for so long."
        n 1fcsunf "I hate having my heart played with like that..."

    elif Natsuki.isNormal(higher=True):
        n 1uwdwr "[player_initial]-{w=0.1}[player]!"
        n 1fnman "What the hell?!{w=0.5}{nw}"
        extend 1fnmfu " Where have you been?!{w=0.5}{nw}" 
        extend 1fbkwrless " I was worried sick!"
        n 1fcsupl "J-{w=0.3}just as a friend,{w=0.5} but still!"
        n 1fcsun "...{w=1.5}{nw}"
        n 1kcspu "..."
        n 1fllunlsbl "...Welcome back,{w=0.1} [player]."
        n  "Just...{w=1.25}{nw}"
        extend 1knmaj " don't leave it so long next time,{w=0.1} alright?"
        n 1fsrunl "You know I don't exactly get many visitors..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqputsb "[player_initial]-{w=0.1}[player]?"
        n 1fsqsltsb "...You're back."
        n 1fcsfutsb "Just {i}perfect{/i}."

    else:
        n 1fsquptdr "..."
        n 1fcsfutsd "...."
        
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
    extend 1tnmeml " [player]?!"
    n 1fnmpuleqm "What the heck are you doing here so early?"
    n 1tnmpu "Did you have a nightmare or something?"
    n 1tsqsl "Or...{w=0.3} maybe you never slept?{w=0.5}{nw}" 
    extend 1tsrpu " Huh."
    n 1tnmbg "Well,{w=0.1} anyway..."
    n 1kchbglsbr "Morning?{w=0.3} I guess?"
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
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_starshine:
    n 1uchbgl "Good morning,{w=0.1} starshine!"
    n 1kchbgf "The Earth says 'Hello!'"
    n 1fchnvf "..."
    n 1nchdvf "Pfffft-!"
    n 1kchbsl "I'm sorry!{w=0.2} It's just such a dumb thing to say...{w=0.3} I can't keep a straight face!"
    n 1nchsml "Ehehe."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kwmsmf "You really are my starshine though,{w=0.1} [chosen_endearment]."
    n 1uchsmf "Welcome back!"
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
    n 1fsqajl "Oh! Well look who finally decided to show up!"
    n 1fwmsll "You know I don't like being kept waiting...{w=0.3} right?"
    n 1fsqsgl "Ehehe.{w=0.2} You're just lucky I'm in a good mood."
    n 1nsqbgl "You better make it up to me,{w=0.1} [player]~!"
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
    n 1nsqbg "Oho!{w=0.2} Well look who finally crawled out of bed today!"
    n 1fsqsg "Jeez,{w=0.1} [player]...{w=0.3} I swear you're lazier than Sayori sometimes!"
    n 1nchsm "Ehehe."
    n 1unmsm "Well,{w=0.1} you're here now -{w=0.1} and that's all I care about."
    n 1nnmbg "Let's make the most of today,{w=0.1} [player]!"
    n 1tsqaj "Or...{w=0.3} what's left of it?"
    n 1nchgn "Ahaha."
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
    n 1unmbg "Oh!{w=0.2} It's [player]!"
    n 1uwlsm "Well -{w=0.1} top of the mornin' to you!"
    n 1uchsm "..."
    n 1knmpo "What?{w=0.2} I'm allowed to say dumb things too,{w=0.1} right?"
    n 1nchgnl "Ehehe."
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
    n 1nchbg "Hey!{w=0.2} Afternoon,{w=0.1} [player]!"
    n 1unmsm "Keeping well?"
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
    n 1nchbg "Oh!{w=0.2} Afternoon,{w=0.1} [player]!"
    n 1uchsm "How're you doing today?"
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
            affinity_range=(jn_affinity.NORMAL, None),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_long_day:
    n 1unmbg "Aha!{w=0.2} Evening,{w=0.1} [player]!"
    n 1ksgsg "Long day,{w=0.1} huh?{w=0.2} Well,{w=0.1} you've come to the right place!"
    n 1nchbg "Just tell Natsuki all about it!"
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
    n 1fsqsr "[player]!{w=0.2} There you are,{w=0.1} [chosen_tease]!"
    n 1fsqpo "Jeez...{w=0.3} took you long enough!"
    n 1fsqsm "Ehehe."
    n 1uchbg "I'm just kidding!{w=0.2} Don't worry about it."
    n 1nchsm "Welcome back!"
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
    extend 1fchbgsbl " Hey,{w=0.2} [player]."
    n 1tnmss "Late night for you too,{w=0.2} huh?"
    n 1ullss "Well...{w=0.75}{nw}" 
    extend 1nchgn " I'm not complaining!" 
    n 1fchsm "Welcome back!"
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
    extend 1fllsslsbl " You're a night owl too,{w=0.2} huh?"
    n 1fcsbg "N-{w=0.2}not that I have a problem with that,{w=0.2} obviously." 
    extend 1nchgnl " Welcome back!"
    return
