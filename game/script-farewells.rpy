default persistent._farewell_database = dict()

default persistent.jn_player_first_farewell_response = None
default persistent.jn_player_force_quit_state = 1

default persistent._jn_player_extended_leave_response = None
default persistent._jn_player_extended_leave_departure_date = None

init python in jn_farewells:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    from store import Natsuki
    FAREWELL_MAP = dict()

    class JNFirstLeaveTypes(Enum):
        """
        Ways in which the player may choose to first leave Natsuki; this decides dialogue upon returning.
        """
        will_be_back = 1
        dont_know = 2
        no_response = 3
        force_quit = 4

        def __int__(self):
            return self.value

    class JNForceQuitStates(Enum):
        """
        Tracking for player force quits; this decides dialogue on returning.
        """
        not_force_quit = 1
        first_force_quit = 2
        previously_force_quit = 3

        def __int__(self):
            return self.value

    class JNExtendedLeaveResponseTypes(Enum):
        """
        Ways in which the player may respond when telling Natsuki they will be gone a while.
        """
        a_few_days = 1
        a_few_weeks = 2
        a_few_months = 3
        unknown = 4

        def __int__(self):
            return self.value

    def get_farewell_options():
        """
        Returns the list of all farewell options when saying Goodbye to Natsuki.
        """
        return [
            ("I'm going to sleep.", "farewell_option_sleep"),
            ("I'm going to go eat something.", "farewell_option_eat"),
            ("I'm going out somewhere.", "farewell_option_going_out"),
            ("I'm going to work.", "farewell_option_work"),
            ("I'm going to school.", "farewell_option_school"),
            ("I'm going to play something else.", "farewell_option_play"),
            ("I'm going to do some studying.", "farewell_option_studying"),
            ("I'm going to do something else.", "farewell_option_misc_activity"),
            ("I'm going to do some chores.", "farewell_option_chores"),
            ("I'm going away for a while.", "farewell_option_extended_leave")
        ]

    def select_farewell():
        """
        Picks a random farewell, accounting for affinity
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        if store.persistent.jn_player_first_farewell_response is None:
            return "farewell_first_time"

        kwargs = dict()

        farewell_pool = store.Topic.filter_topics(
            FAREWELL_MAP.values(),
            affinity=Natsuki._getAffinityState(),
            excludes_categories=["Failsafe"],
            **kwargs
        )

        return random.choice(farewell_pool).label

label farewell_start:
    $ push(jn_farewells.select_farewell())
    jump call_next_topic

# Only chosen for the first time the player chooses to say Goodbye
label farewell_first_time:
    n 1uskem "W-{w=0.1}wait,{w=0.1} you're leaving?"
    n 4fskwrlsbr "[player]!{w=0.2} H-{w=0.1}hang on!{w=0.5}{nw}"
    extend 4fbkwrleexsbr " Wait just a second!"
    n 4fskemlsbl "..."
    n 2kllemlsbl "..."
    n 2kplpu "...Y-{w=0.1}you are coming back,{w=0.1} right?"
    n 2kllunsbl "..."
    n 4kwmemesssbr "...Right?"

    menu:
        "I'll be back.":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.will_be_back)
            $ Natsuki.calculatedAffinityGain(bypass=True)
            n 4unmemlesu "...!{w=0.5}{nw}"
            n 1fllemless "Y-{w=0.1}yeah!{w=0.5}{nw}"
            extend 1fsqpolsbr " You better."
            n 2flremlsbl "Y-{w=0.1}you are responsible for this,{w=0.1} like I said.{w=0.5}{nw}"
            extend 2flrpol " So..."
            n 2kllpol "..."

        "I don't know.":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.dont_know)
            n 1kskem "..."
            n 4kskwr "N-{w=0.5}no!"
            n 4kcsan "You can't do this to me!{w=0.5}{nw}"
            extend 4fcsuptsa " N-{w=0.1}not now..."
            n 1kcsunltsa "..."
            n 1ksqunl "..."
            n 2kplpul "Please,{w=0.1} [player]...{w=0.5}{nw}"
            extend 2kllpu " it isn't much to ask for..."
            n 4kwmemsbr "Right?"

        "...":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)
            n 1knmemsbr "[player],{w=0.1} c-{w=0.5}come on..."
            n 1kllpu "If this is a joke,{w=0.5}{nw}"
            extend 4fnmgs " it really isn't funny!{w=2}{nw}"
            extend 4knmgssbl " I-{w=0.1}I'm serious!"
            n 1kllunsbl "..."
            n 1knmaj "Please,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " it isn't much to ask for..."
            n 4kwmem "Right?"

    return { "quit": None }

# Only chosen for the first time the player leaves via force quit
label farewell_force_quit:
    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.first_force_quit)
    if not persistent.jn_player_first_farewell_response:
        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.force_quit)

    hide screen hkb_overlay
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a
    stop music
    play audio glitch_c

    n 1uskem "H-{w=0.3}huh?{w=1}{nw}"
    extend 4uscwr " N-{w=0.3}no!{w=0.2} Wait!!{w=0.2} PLEASE-{w=0.3}{nw}"
    show natsuki 4kchupltsa at jn_center zorder JN_NATSUKI_ZORDER

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_b

    return { "quit": None }

# Non-generic farewells - each of these should be registered under FAREWELL_OPTIONS. Affectionate + only.

label farewell_option_sleep:
    if jn_admissions.last_admission_type in (jn_admissions.TYPE_SICK , jn_admissions.TYPE_TIRED):
        # Sick/tired
        n 2kllsl "...[player]."
        n 2knmpu "I...{w=0.75}{nw}" 
        extend 2klrpu " think that'd be a good idea.{w=0.5} You know."
        $ feeling_like = "feeling sick" if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK else "feeling tired"
        n 2klrpu "With what you said earlier about [feeling_like] and all."
        n 4ulraj "So...{w=0.75}{nw}"
        extend 4knmpo " go get some rest,{w=0.1} alright?{w=1}{nw}" 
        extend 2fcspol " We can just talk later anyway."
        n 2fnmgsl "Now get going,{w=0.1} [player]!"
        extend 4fchsml " Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 3fchbgl "Don't let the bedbugs bite!"

        elif Natsuki.isLove(higher=True):
            n 3fchblledz "Love you too~!"

    elif jn_get_current_hour() > 22 or jn_get_current_hour() < 6:
        # Late night
        n 4fwdajesh "A-{w=0.2}and I should think so,{w=0.1} too!{w=0.5}{nw}"
        extend 2tnmem " It seriously took you {i}that{/i} long to notice the time?!"
        n 2fllposbl "Jeez...{w=0.5}{nw}"
        extend 2nllpo " but better late than never,{w=0.1} I guess."
        n 4fllsm "Ehehe.{w=0.5}{nw}"
        extend 1fchsm " Sleep well,{w=0.1} [player]!"

        if Natsuki.isEnamored(higher=True):
            n 3fchbll "See you soon~!"

        elif Natsuki.isLove(higher=True):
            n 3nchsml "Love you~!"

    elif jn_get_current_hour() >= 21:
        # Standard night
        n 1unmaj "About ready to turn in,{w=0.1} huh?"
        n 4ullaj "That's fine...{w=0.5}{nw}"
        extend 2fslca " I guess."
        n 4fcsct "I know you need your beauty sleep and all."
        n 3fsqsm "...Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "Sleep tight,{w=0.2} [chosen_tease]!{w=0.5}{nw}"
            extend 3uchsmledz " See you tomorrow~!"

        else:
            n 3fchbgl "No worries!{w=0.2} Sleep well,{w=0.1} [player]!"
        
    elif jn_get_current_hour() >= 19:
        # Early night
        n 1unmaj "Huh?{w=0.75}{nw}" 
        extend 4tnmaj " You're taking an early night?"
        n 4nnmbo "Oh.{w=0.5}{nw}" 
        extend 1nllpu " Well..."
        n 4ullaj "That's fine.{w=0.75}{nw}" 
        extend 2nslpo " I suppose."
        n 2fsqcal "You better stay up with me later though.{w=0.75}{nw}"
        extend 4fsrtrl " You know."
        n 3fsqbglsbl "To make up for lost time and all."
        n 3fchbll "Night,{w=0.1} [player]!"

    else:
        # Nap
        n 1tnmbo "Huh?{w=1}{nw}" 
        extend 4tnmpu " You're taking {i}naps{/i} now?"
        n 2tsqcaesd " ...Really?"
        n 2ncsemesi "Jeez...{w=1}{nw}" 
        extend 2fllca " I swear I'm gonna be feeding you next at this rate..."
        n 4fsqdv "..."
        n 3fchbg "Oh,{w=0.3} relax!"
        n 3nchgnelg "I'm kidding,{w=0.1} I'm kidding!{w=0.5}{nw}"
        extend 3tllss " Sheesh."
        n 4fchbg "See you later,{w=0.1} [player]~!"

        if Natsuki.isLove(higher=True):
            n 1uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_eat:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fcsgs "W-{w=0.1}well,{w=0.1} duh!{w=0.5} You {i}said{/i} you were starving!"
        n 2fllpoesi "Jeez..."
        n 2fdtposbr "Just make it something healthy,{w=0.1} got it?"
        n 4fsqsm "...Ehehe."
        n 2fchbg "Enjoy,{w=0.1} [player]!"

    elif jn_get_current_hour() in (7, 8):
        n 1fnmgs "Yeah!{w=0.3} You better!{w=0.5}{nw}"
        extend 2fsqtr " You {i}do{/i} know what they say about breakfast,{w=0.1} right?"
        n 4fsqsml "...Ehehe."
        n 2fchbg "Bon appetit,{w=0.1} [player]!"

    elif jn_get_current_hour() in (12, 13):
        n 2unmaj "Heading out for lunch,{w=0.1} [player]?"
        n 1ulrbo "That's cool,{w=0.3} that's cool."
        n 4nsqsm "Just remember though...{w=0.3}{nw}"
        extend 2fsqss " you are what you eat~."
        n 4fchsm "...Ehehe.{w=0.5}{nw}"
        extend 3uchsm " Enjoy!"

    elif jn_get_current_hour() in (18, 19):
        n 3unmaj "Dinner time,{w=0.1} huh?{w=0.5}{nw}"
        extend 2unmbg " No probs!"
        n 1nlrpu "Just...{w=0.5}{nw}"
        extend 2fdtposbr " make sure it isn't a ready meal.{w=0.5}{nw}"
        extend 2fsqpo " Got it?"
        n 2fsqsm "...Ehehe."
        n 1fchbg "Enjoy,{w=0.1} [player]~!"

    else:
        n 1unmaj "Oh?{w=0.2} You're gonna grab a bite to eat?"
        n 2nllaj "That's fine."
        n 2nsqpo "You better not be filling up on junk though,{w=0.1} [player]."
        n 2fsqsm "...Ehehe.{w=0.5}{nw}"
        extend 4uchbg " Enjoy~!"

    return { "quit": None }

label farewell_option_going_out:
    if jnIsNewYearsEve():
        n 3tsqbg "Oho?{w=0.2} Going out for the new year,{w=0.1} are we?{w=0.5}{nw}"
        extend 3fchbg " Can't say I blame you!"
        n 1ullaj "Just...{w=0.5}{nw}"
        extend 4nsqsl " don't be an idiot out there,{w=0.1} okay?"
        n 2fslsl "I don't want you messing around with drinks and fireworks like a complete moron and getting hurt."
        n 1ullpu "But...{w=0.5}{nw}"
        extend 1uchbg " yeah!{w=0.2} Have fun out there,{w=0.1} [player]!"
        n 2usqbg "And if I don't see you sooner?"
        n 1fchbs "Happy new year!"

    elif jnIsEaster():
        n 1unmaj "Oh?{w=0.2} You're heading off now?"
        n 4unmbg "Did you have a meal planned for today or something?"
        n 4tlrsm "It {i}is{/i} Easter,{w=0.1} after all!{w=0.5}{nw}"
        extend 3uchsm " Ehehe."
        n 4ullss "Well,{w=0.1} anyway.{w=0.5}{nw}"
        extend 2uchgn " See you later,{w=0.1} [player]!"

    elif jnIsHalloween():
        n 3usqss "Ooh?{w=0.2} Heading out for Halloween,{w=0.1} [player]?"
        n 3fsqsm "Just don't forget..."
        n 2fsqbg "I want my share of treats too!"
        n 2fchgn "Ehehe.{w=0.5}{nw}"
        extend 1fchbg " Have fun~!"

    elif jnIsChristmasEve():
        n 1unmbo "Oh?{w=0.2} You're heading out for Christmas Eve?"
        n 1kllsl "Well...{w=0.3} okay."
        n 4kllajl "...You will be back in time for Christmas though...{w=0.5}{nw}"
        extend 4knmsll " right?"
        n 2nsrssl "...Ahaha.{w=0.3}"
        extend 1nchbgsbl " See you later,{w=0.1} [player]!"
        n 1kslslsbl "..."

    elif jnIsChristmasDay():
        n 1unmbo "Huh?{w=0.2} You're heading off now?"
        n 2kllsl "Well...{w=0.3} alright."
        n 2kllss "Thanks for dropping by today though,{w=0.1} [player]."
        n 4kcsssl "It...{w=0.3} really meant a lot to me."
        n 4kchss "See you later,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1kchbg " And Merry Christmas!"

    else:
        n 2unmaj "Oh?{w=0.2} You're heading out,{w=0.1} [player]?"
        n 2fchbg "No worries!{w=0.2} I'll catch you later!"
        n 2nchbg "Toodles~!"

    if Natsuki.isLove(higher=True):
        n 4uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_work:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1knmaj "H-{w=0.1}huh?{w=0.2} You're going to work now?"
        $ time_concern = "late" if jn_get_current_hour() >= 20 else "early"
        n 4kllajsbr "But...{w=0.5}{nw}" 
        extend 4knmgssbr " it's super [time_concern] though,{w=0.1} [player]..."
        n 1kllsll "..."
        n 1kllajl "Are you..."
        show natsuki 4tnmbol

        menu:
            n "Are you gonna work from home today,{w=0.2} or...?"

            "Yes, I'm working from home.":
                n 1ncsssl "Heh.{w=0.75}{nw}"
                extend 2nllpul " I {i}guess{/i} that's something,{w=0.75}{nw}"
                extend 2nslsll " at least."
                n 4fslpol "Still doesn't mean I gotta like it,{w=0.2} though."
                n 4fcspol "Just..."
                n 1kllbol "...Keep an eye on the clock.{w=0.75}{nw}"
                extend 1knmbol " Alright?"
                n 2fsqcal "I don't wanna hear about you staying back late or anything."
                
                if Natsuki.isLove(higher=True):
                    n 2fchsml "Take it easy,{w=0.2} [player]!{w=0.75}{nw}"
                    extend 2fchssleafsbl " L-{w=0.2}love you!"

                else:
                    n 2fchssl "Take it easy,{w=0.2} [player]!"
                    n 2kslsll "..."

            "No, I have to head out.":
                n 4kcsemlesi "Man...{w=1}{nw}"
                extend 4ksqbol " {i}really{/i}?"
                n 1ksrsllsbr "..."
                n 1fcspusbr "Just...{w=1}{nw}" 
                extend 4kllsl " be careful,{w=0.2} alright?"
                n 2fsqpol "And you {i}better{/i} come visit when you get back."

                if Natsuki.isLove(higher=True):
                    n 2fnmcal "Take care,{w=0.1} [player]!{w=1}{nw}"
                    extend 4kchsmleaf " I love you!"
                    n 4kllcalsbr "..."

                else:
                    n 2fnmcal "Take care,{w=0.1} [player]!"

    else:
        n 1unmajesu "Oh?{w=0.2} You're working today?"

        if jnIsEaster():
            n 1uskgs "...And on Easter,{w=0.1} of all days?{w=0.5}{nw}"
            extend 1fslpo " Man..."

        elif jnIsChristmasEve():
            n 4fskgsl "...On Christmas Eve?{w=0.5}{nw}"
            extend 2kcsemledr " You've gotta be kidding me..."

        elif jnIsChristmasDay():
            n 4fskwrl "...On {i}Christmas{/i}?!{w=0.5}{nw}"
            extend 1kcsemledr " Ugh..."
            n 2fslpol "..."
            n 2fslajl "Well..."

        elif jnIsNewYearsEve():
            n 4fskgsl "...And on New Year's Eve,{w=0.1} too?!{w=0.5}{nw}"
            extend 1kcsemledr " Jeez..."

        elif jnIsPlayerBirthday():
            n 1kwdgsl "...And on your {i}birthday{/i} too?!{w=1}{nw}"
            extend 1kslanl " Yikes,{w=0.75}{nw}" 
            extend 1kslsll " [player]..."

        elif not jn_is_weekday():
            n 1uwdaj "A-{w=0.1}and on a weekend,{w=0.1} too?{w=0.5}{nw}"
            extend 2kslpu " Man..."

        n 2nlrpo "It sucks that you've gotta work,{w=0.1} but I get it.{w=0.5}{nw}" 
        extend 2nsrpo " I guess."
        n 4fnmpo "...You better come vist when you finish though."
        n 4fsqsm "Ehehe."
        n 3fchbg "Take it easy,{w=0.1} [player]!{w=0.2} Don't let anyone push you around!"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 3uchbgf "You got this,{w=0.1} [chosen_endearment]!{w=0.2} Love you~!"

        elif Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3uchbgl "I believe in you,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_school:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1tnmem "...School?{w=1}{nw}" 
        extend 4fskgsesh " A-{w=0.1}At this hour?"

        if jnIsEaster():
            n 1kwdgs "...And on {i}Easter{/i},{w=0.1} of all days?}"

        elif jnIsChristmasEve():
            n 1fskgsl "...And on {i}Christmas Eve{/i}?"

        elif jnIsChristmasDay():
            n 1fskwrl "...And on {i}Christmas{/i}?!"

        elif jnIsNewYearsEve():
            n 1fskgsl "...And on New Year's Eve,{w=0.1} too?!"

        if not jn_is_weekday():
            extend 1uskwr " A-{w=0.1}and on a {i}weekend{/i} too?!"

        n 4fbkwrean "What the hell kind of school is thaaaat?!"
        n 2kllpo "Jeez.{w=0.5}{nw}"
        extend 2fslsr " And I thought my school experience was bad enough."
        n 2kcspu "Just...{w=0.5}{nw}"
        extend 4knmpu " take care getting there,{w=0.1} alright?"
        $ time_concern = "late" if jn_get_current_hour() >= 20 else "early"
        extend 1fllsrsbl " It's really [time_concern],{w=0.1} after all."
        n 4kllss "Study hard,{w=0.1} [player]!"

    else:
        if jnIsEaster():
            n 4uskgs "...And on Easter,{w=0.1} of all days?{w=0.5}{nw}"
            extend 2fslpo " Man..."

        elif jnIsChristmasEve():
            n 4fskgsl "...On Christmas Eve?{w=0.5}{nw}"
            extend 2fcseml " You've gotta be kidding me..."

        elif jnIsChristmasDay():
            n 4fskwrl "...On {i}Christmas{/i}?!{w=0.5}{nw}"
            extend 2fcseml " Ugh..."
            n 2fslpol "..."
            n 2fslajl "Well..."

        elif jnIsNewYearsEve():
            n 4fskgsl "...And on New Year's Eve,{w=0.1} too?!{w=0.5}{nw}"
            extend 2fcseml " Jeez..."

        elif jn_is_weekday():
            n 2unmaj "Off to school,{w=0.1} [player]?{w=0.5}{nw}"
            extend 2nchsm " No worries!"

        else:
            n 1tnmpu "Huh?{w=0.2} You're at school today?{w=0.5}{nw}"
            extend 2nsqpu " ...On a {i}weekend{/i}?"
            n 2fslpu "..."
            n 2fsqpo "Gross..."

        n 2tsqsm "Sucks to be you though,{w=0.1} huh?{w=0.5}{nw}"
        extend 2fchsm " Ehehe."
        n 3fchbg "No slacking off,{w=0.1} [player]!{w=0.2} I'll see you later!"

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4uchbgf "Love you!"

    return { "quit": None }

label farewell_option_misc_activity:
    n 1knmpu "H-{w=0.1}huh?{w=0.5}{nw}"
    extend 1kllaj " And you gotta leave to do that too?"
    n 4fcsun "Nnnnnn...{w=0.5}{nw}"
    extend 1kcsaj " okay."
    n 2fnmpol "...But you better come visit once you're done.{w=1}{nw}"
    extend 2klrpo " Got it?"
    n 2kllpo "See you soon,{w=0.1} [player]!"

    if Natsuki.isLove(higher=True):
        n 4kllssf "Love you!"

    return { "quit": None }

label farewell_option_play:
    n 1fsqaj "...Really,{w=0.5} [player]?"
    n 4nslpu "You'd seriously rather play some {i}game{/i}...{w=0.5}{nw}"
    extend 2fsqsf " than hang out with {i}me{/i}?"
    n 2fcssl "..."
    n 2uchgneme "Well,{w=0.1} your loss!{w=0.5}{nw}"
    extend 2fchbgelg " Ahaha!"
    n 1nllbg "No,{w=0.1} no.{w=0.2} It's fine.{w=0.2} You go do that,{w=0.1} [player].{w=0.5}{nw}"
    extend 4nsqbg " Besides..."
    n 2usqct "You sure could use the practice,{w=0.1} huh?{w=0.5}{nw}"
    extend 2fchsm " Ehehe."
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchbg "Catch you later,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_studying:
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fskgs "[player_initial]-{w=0.1}[player]!"
    n 2fllansbr "If I'd known you were meant to be studying I'd have thrown you out myself!{w=0.5}{nw}"
    extend 2fcspoesi " Geez..."
    n 2nsqposbl "I really hope you don't have exams tomorrow or something like that..."
    n 2flrpo "But either way,{w=0.1} you'll be fine.{w=0.2} Just go!{w=0.5}{nw}"
    extend 4fwdaj " Go!"
    n 4fchgn "...Shoo,{w=0.1} you dummy!{w=0.2} Ehehe.{w=0.5}{nw}"
    extend 4fchbl " We'll talk later!"

    if Natsuki.isLove(higher=True):
        n 1uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_chores:
    if store.jn_get_current_hour() >= 20 or store.jn_get_current_hour() <= 4:
        n 1tnmaj "...Chores?{w=0.5}{nw}"
        extend 2tsqem " At {i}this{/i} time?"
        n 2nllbo "I gotta say,{w=0.1} [player]."
        n 2nsqdv "You're either dedicated or desperate.{w=0.5}{nw}"
        extend 1nchsm " Ehehe."
        n 1ullss "Well,{w=0.1} whatever.{w=0.5}{nw}"
        extend 3tnmss " Just hurry up and go sleep,{w=0.1} 'kay?"

        if Natsuki.isLove(higher=True):
            n 3uchbg "Later,{w=0.1} [player]!"
            extend 4uchbgf " Love you~!"

        else:
            n 3fchbg "Later,{w=0.1} [player]!"

    else:
        n 2tnmsg "Stuck on chore duty,{w=0.1} huh?"
        n 2nchsm "Ehehe.{w=0.2} Yeah,{w=0.1} that's fine.{w=0.5}{nw}"
        extend 2fchgn " You go take care of your clean streak!"

        if Natsuki.isLove(higher=True):
            n 3uchbg "Later,{w=0.1} [player]!{w=0.5}{nw}"
            extend 3uchbgf " Love you~!"

        else:
            n 3fchbg "Ehehe.{w=0.2} Later,{w=0.1} [player]!"

    return { "quit": None }

label farewell_option_extended_leave:
    n 1tnmpueqm "Eh?{w=0.75}{nw}"
    extend 1knmaj " A while?"
    n 2fnmsr "..."
    n 2fsqaj "...What do you mean 'a while',{w=0.2} [player]?{w=0.75}{nw}"
    extend 2fnmgs " Huh?"
    n 3fllem "Are you trying to avoid me?{w=1}{nw}"
    extend 3knmem " Am I {i}not{/i} the best to be around?"
    n 4fbkwrl "I-{w=0.2}is {i}that{/i} it?!"
    n 2fsqpol "..."
    n 2fsqsml "..."
    n 2fcsaj "Oh,{w=0.5}{nw}"
    extend 2fchgn " lighten up,{w=0.2} [player]!{w=1}{nw}"
    extend 4ullss " Sheesh!"
    n 4fchbg "You should know when I'm pulling your leg by now,{w=0.75}{nw}"
    extend 1fchbl " you dork."
    n 1ulrss "Well,{w=0.2} anyway.{w=0.75}{nw}"
    extend 2ulraj " It's totally fine."
    n 2fcsajsbl "I can {i}easily{/i} handle a few days alone.{w=0.75}{nw}"
    extend 2fchbgsbl " No sweat!"
    n 4nslbosbl "..."
    n 4nslaj "But...{w=0.75}{nw}"
    extend 4nllsl " just so I know...."
    show natsuki 2knmbo
    
    menu:
        n "Did you plan on being away long,{w=0.2} or...?"

        "A few days.":
            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_days)
            n 1kchdvesi "Pffff-!{w=0.75}{nw}"
            extend 2tsqbg " And to think you were probably getting all worked up over it too!{w=0.75}{nw}"
            extend 2fcssm " Ehehe."
            n 3fcsbg "Yeah,{w=0.2} that's no problem at all.{w=1}{nw}"
            extend 3fchgn " Now get going already!"

            if Natsuki.isLove(higher=True):
                n 3kchbgl "See ya later,{w=0.2} [player]!{w=0.75}{nw}"
                extend 4fchsmleafsbl " L-{w=0.2}love you!"

            elif Natsuki.isEnamored(higher=True):
                n 3fchbg "See ya later,{w=0.2} [player]!"
                n 4kslsssbl "..."

        "A few weeks.":
            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_weeks)
            n 2tnmpu "A few weeks,{w=0.75}{nw}"
            extend 2tnmbo " huh?"
            n 4kllbo "..."
            n 4kllss "That's...{w=0.75}{nw}"
            extend 2nslsl " a little longer than I hoped."
            n 2fcsgslsbl "B-{w=0.2}but I'll be fine!{w=0.75}{nw}"
            extend 2fcspolsbl " I've {i}totally{/i} got this.{w=1}{nw}"
            extend 2fcsbglsbl " Don't you worry!"
            n 2nslsslsbl "Ehehe..."
            n 1fchbgsbl "L-{w=0.2}later, [player]!"
            
            if Natsuki.isLove(higher=True):
                n 1kchsmlsbl "Love you!"
                n 4ksrsll "..."

            elif Natsuki.isEnamored(higher=True):
                n 4kcspuesi "..."

        "A few months.":
            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_months)
            n 4knmpu "...A few {i}months{/i}?"
            n 2kslpu "..."
            n 2kslaj "That's...{w=1}{nw}"
            extend 1klrsl " a lot longer than I expected."
            n 1fcsca "..."
            n 2fcsajlsbl "I-{w=0.2}I mean,{w=0.75}{nw}"
            extend 2fcsgslsbl " I'll be totally fine!"
            n 2kslbolsbl "But..."
            n 1ncsbolesi "..."
            n 1nsrbol "N-{w=0.2}nevermind.{w=0.75}{nw}"
            extend 2fcstrl " I got this!{w=1}{nw}"
            extend 2nslsslsbl " ...I think."
            n 3klrbolsbl "T-{w=0.2}take care,{w=0.2} [player]."
            extend 3knmbolsbl " 'Kay?"

            if Natsuki.isLove(higher=True):
                n 3fcsajlsbr "...You know how much you mean to me,{w=1}{nw}"
                extend 4kllbolsbr " a-{w=0.2}after all..."

            elif Natsuki.isEnamored(higher=True):
                n 3fnmcalsbr "I'll get mad if you don't."
                n 3kslbolsbr "..."

            else:
                n 3kslbolsbr "..."

        "I'm not sure.":
            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.unknown)
            n 1uskemlesh "...H-{w=0.2}huh?{w=0.75}{nw}"
            extend 4knmemlsbr " You don't even {i}know{/i} when you'll be back?"
            n 4kllunlsbr "..."
            n 4kllpulsbr "But...{w=0.75}{nw}"
            extend 4klrbolsbl " you {i}will{/i} be back...{w=1}{nw}"
            extend 4knmbolsbl " right?"
            n 1ksqbol "..."
            n 1kcsemlesi "..."
            n 1kslpol "...I'll be fine.{w=1}{nw}"
            extend 2nslpol " I guess.{w=1}{nw}"
            extend 2kslpul " Just..."
            n 4fcsunl "..."
            n 2kcseml "Don't keep me waiting too long.{w=0.75}{nw}"
            extend 4knmbol " Please?"

            if Natsuki.isLove(higher=True):
                n 2ksrbofsbr "...You know how much you mean to me,{w=0.75}{nw}"
                extend 4ksqbofsbr " a-{w=0.2}after all..."

            elif Natsuki.isEnamored(higher=True):
                n 2kslajlsbl "...Later,{w=0.2} [player]."
                n 2kslsllsbl "..."

            else:
                n 2kslajl "Later,{w=0.2} [player]."
                n 2kslsll "..."

    $ import datetime
    $ persistent._jn_player_extended_leave_departure_date = datetime.datetime.now()

    return { "quit": None }

# Generic farewells

# LOVE+ farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_you_mean_the_world_to_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_you_mean_the_world_to_me:
    n 1kllpul "Aww...{w=1}{nw}"
    extend 4kplsfl " you're leaving now,{w=0.2} [player]?" 
    n 4klrcal "Well...{w=1}{nw}" 
    extend 2ksrcal " okay."
    n 2fnmtrf "Y-{w=0.2}you better take care,{w=0.2} [player]!{w=0.5}{nw}" 
    extend 4kchssfeaf " You mean the world to me!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_dont_like_saying_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_dont_like_saying_goodbye:
    n 4fsqtrl "You know I don't like saying goodbye,{w=0.1} [player]..."
    n 4kcssllesi "..."
    n 2fcsgsfess "I-{w=0.2}I'll be okay!{w=1}{nw}"
    extend 2fcsajf " Just..."
    n 4knmpof "...Get back here soon,{w=0.2} alright?"
    n 1kchssfeaf "I-{w=0.2}I love you,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_counting_on_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_counting_on_you:
    n 1fcsunl "Uuuu...{w=0.75}{nw}" 
    extend 2fslpol " I never like saying goodbye to you..."
    n 2kslbol "But...{w=0.5}{nw}" 
    extend 2kslssl " I guess it can't be helped sometimes."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 2fcsajl "S-{w=0.2}so!"
    n 4fsqtrf "You better take care of yourself out there,{w=0.1} [chosen_endearment]." 
    n 3fchgnl "...'Cuz I'm counting on you!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fchblleaf "Later,{w=0.2} [chosen_tease]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_do_your_best",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_do_your_best:
    n 1unmajl "Oh?{w=0.5}{nw}" 
    extend 3tnmbol " You're heading out now?"
    n 4flrpol "That's...{w=0.5} fine.{w=0.75}{nw}" 
    extend 2fsrsll " I guess."
    n 2kplcal "...You know I'll really miss you,{w=0.1} [player]."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 2flrssfsbr "S-{w=0.2}so you better do your best for me,{w=0.1} [chosen_endearment]!"
    n 4fchsmf "Ehehe.{w=0.75}{nw}"
    extend 2uchsmfeaf " See you soon!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_rooting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_rooting_for_you:
    n 3unmajl "Huh?{w=0.5}{nw}" 
    extend 3tnmsll " You're leaving now?"
    n 1fcssll "I always hate it when you have to go somewhere..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kcssml "...But I know you'll always be back for me,{w=0.1} [chosen_endearment]."
    n 2fllssfsbl "N-{w=0.2}not like you {i}have{/i} a choice,{w=0.2} obviously!{w=0.75}{nw}"
    extend 2fsqsmf " Ehehe."
    n 4fchblfeaf "Make me proud,{w=0.2} [player]!{w=0.5}{nw}" 
    extend 4fchsmfeaf " I'm rooting for you!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_me_to_deal_with",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_me_to_deal_with:
    n 1unmajl "You're leaving now,{w=0.1} [player]?"
    n 4kllpul "Awww...{w=0.75}{nw}" 
    extend 2kllpol " well okay."
    n 1fnmcal "You take care of yourself,{w=0.2} got it?" 
    extend 3fcsssl " Or you'll have me to deal with!"
    n 3fsqsml "Ehehe."
    n 3fchbgfeaf "Bye now!{w=0.5} I love you~!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_wish_you_could_stay_forever",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_wish_you_could_stay_forever:
    n 3kwmpol "Time to go,{w=0.1} [player]?"
    n 3kllssl "Sometimes I kinda wish you could just stay forever..."
    n 4fcsajf "But I understand you've got stuff to do."
    n 2fslssfsbl "...Even if it {i}isn't{/i} always as important as me.{w=0.75}{nw}"
    extend 2nchgnl " Ehehe."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1fchbgf "Later,{w=0.2} [chosen_endearment]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_that_time_again",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_that_time_again:
    n 4nslss "Heh.{w=0.75}{nw}"
    extend 2nllfl " That time again,{w=0.75}{nw}"
    extend 2tnmbo " huh?"
    n 1csrsll "..."
    n 1ccsajlsbr "You should know by now I never look forward to it,{w=0.2} [player].{w=0.75}{nw}"
    extend 4csrcalsbr " But I guess it's gotta be done at some point."
    n 3fsqssl "...Doesn't mean you're off the hook for coming back though.{w=0.5}{nw}"
    extend 3fsqsml " Ehehe."
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fcsbgl "Better not keep me waiting,{w=0.2} [chosen_tease]!"
    n 4fchbgleafsbl "L-{w=0.2}love you!"

    return { "quit": None }

# AFFECTIONATE/ENAMORED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_was_having_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_was_having_fun:
    n 3unmajl "Eh?{w=0.5}{nw}" 
    extend 3tnmpul " You're leaving now?"
    n 4kcsemesi "Man..."
    n 1fllpol "And I was actually having fun,{w=0.2} too...{w=1}{nw}"
    extend 2fsqpol " talk about being a buzzkill,{w=0.2} [player]."
    n 2fcspol "..."
    n 1fchbll "Well,{w=0.1} if you gotta go,{w=0.1} you gotta go!"
    n 2nchgnl "Now get out there,{w=0.1} dummy!{w=1}{nw}"
    extend 2fwlbgl " See you later!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_waiting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_waiting_for_you:
    n 2unmajl "You're going,{w=0.1} [player]?"
    n 2fcsanl "Uuuuu...{w=1.5}{nw}"
    extend 1kllpol " okay."
    n 4fsqgsl "But you better be back here soon."
    extend 3fcsajf " It's rude to keep someone waiting around for you,{w=0.2} a-{w=0.1}after all."
    n 4fslssfsbl "Ahaha."
    n 3fchbglsbr "L-{w=0.1}later,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_ill_be_okay",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_ill_be_okay:
    n 1unmajlesu "Huh?{w=0.5}{nw}" 
    extend 4knmajlsbl " You're leaving?"
    n 4fslunl "..."
    n 1fcsgsfsbl "T-{w=0.1}that's fine!{w=1}{nw}"
    extend 1fcsssledz " I'll be okay!"
    n 2fsqpol "Which is more than I can say for you if you keep me waiting again,{w=0.2} [player]..."
    n 2fsqsml "Ehehe."
    n 3nchgnl "See you later~!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_dont_make_me_find_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_dont_make_me_find_you:
    n 2unmbol "Oh?{w=0.5}{nw}" 
    extend 2unmajl " Heading off now,{w=0.1} [player]?"
    n 1kllpol "I...{w=0.75}{nw}" 
    extend 4kslpol " wish you didn't have to..."
    n 4fcsajl "But I get that you have things to do."
    n 2fsqcal "You better come see me later though.{w=0.5}{nw}" 
    extend 2fsqtrl " Promise?"
    n 2fcsbgl "Don't make me come find you!"
    n 4fchgnl "...Now get going already,{w=0.2} you dope!{w=0.75}{nw}"
    extend 3fchbll " See you soon!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_take_care_for_both",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_take_care_for_both:
    n 1unmpul "Mmm?{w=0.5}{nw}" 
    extend 3tnmajl " You're going now,{w=0.1} [player]?"
    n 3kcsemlesi "...Fine,{w=0.3} fine.{w=1.25}{nw}"
    extend 4fsqtrl " But on one condition!"
    n 4kslcalsbr "..."
    n 2knmtrlsbr "..Just take care of yourself,{w=0.5}{nw}"
    extend 2knmsllsbr " okay?"
    n 2fcspofsbl "A-{w=0.1}and not just for your own sake."
    extend 2kslssfsbl " Heh."
    n 1kchssfesssbl "See you later!"
    n 4kslslfsbr "..."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_enjoy_our_time_together",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_enjoy_our_time_together:
    n 2tnmajl "You're leaving now,{w=0.2} [player]?"
    n 2fllcal "Nnnnnn...{w=0.5}{nw}" 
    extend 4ksltrl " alright."
    n 2fcsgsl "But you better be back later,{w=0.2} you hear?"
    n 2fllajl "I...{w=0.75}{nw}"
    extend 4kslcafsbr " enjoy our time together."
    n 2kchssfsbl "See you soon,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_see_me_soon:
    n 1ullajl "Well,{w=0.3}{nw}" 
    extend 1fllcal " I guess you had to leave eventually."
    n 2fsqpol "Doesn't mean I have to like it,{w=0.2} though..."
    n 4knmpol "Come see me soon,{w=0.2} 'kay?"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_making_it_up",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_making_it_up:
    n 4kslfl "Man...{w=1}{nw}"
    extend 4cnmfll " really?{w=0.75}{nw}"
    extend 4csreml " Come {i}on{/i}..."
    n 2ccsslesi "..."
    n 2fcstr "Fine,{w=0.2} fine."
    n 2fcspo "...But you're {i}totally{/i} making it up to me when you're back.{w=0.75}{nw}"
    extend 4fchbleme " Sorry~!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fcsbglsbr "N-{w=0.2}now get out of here already,{w=0.2} [chosen_tease]!"
    n 3fchbgl "Catch you later!"

    return { "quit": None }

# HAPPY/AFFECTIONATE farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_going_now",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_going_now:
    n 2unmaj "Going now,{w=0.2} [player]?{w=0.75}{nw}"
    extend 2nchsm " See you later!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_heading_off",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_heading_off:
    n 1unmaj "Heading off now,{w=0.2} [player]?"
    n 3nnmsm "Alright!{w=0.5}{nw}" 
    extend 3fchsm " Take care!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_stay_safe",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_stay_safe:
    n 1nchss "Okaaay!{w=0.75}" 
    extend 2tnmss " I guess I'll catch you later then."
    n 2fchsm "Stay safe,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_take_care",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_take_care:
    n 4nnmbg "See you later,{w=0.2} [player]!"
    n 4fchsm "Take care!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_see_me_soon:
    n 1nchbg "Bye,{w=0.2} [player]!"
    n 4fchsmlsbr "Come see me soon,{w=0.2} alright?"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_catch_you_later",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_catch_you_later:
    n 1tnmboeqm "Huh?{w=0.75}{nw}"
    extend 2unmaj " You're heading off now?"
    n 2fcsbg "Gotcha!{w=0.75}{nw}"
    extend 2fchbgl " Catch you later,{w=0.2} [player]!"
    n 2csrsllsbl "..."

    return { "quit": None }

# NORMAL/HAPPY farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_you_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_you_later:
    n 1nchsm "See you later,{w=0.2} [player]!"
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_later:
    n 2nnmss "Later,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_goodbye:
    n 4nchsm "Goodbye,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_kay",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_kay:
    n 1fcsbg "'kay!{w=0.5}{nw}" 
    extend 2fchbg " Bye for now!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_ya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_ya:
    n 3nchbg "See ya,{w=0.2} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_oh_right",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_oh_right:
    n 1tnmfleqm "Huh?{w=0.75}{nw}"
    extend 1ullbo " Oh,{w=0.2} right."
    n 1cchsm "Later,{w=0.2} [player]!"

    return { "quit": None }

# UPSET/DISTRESSED farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_bye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_bye:
    n 1nnmsl "Bye,{w=0.2} [player]."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_later",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_later:
    n 2nnmsf "Later,{w=0.2} [player]."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_kay",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_kay:
    n 3fllsf "'kay.{w=0.2} Later."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_goodbye:
    n 1nnmbo "Oh.{w=0.5}{nw}"
    extend 2fslsf " Goodbye."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_see_you_around",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_see_you_around:
    n 2fsqsf "See you around."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_yeah_bye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_yeah_bye:
    n 1fslfl "...Yeah.{w=1}{nw}"
    extend 1fsqsl " {b}Bye{/b}."

    return { "quit": None }

# DISTRESSED/BROKEN/RUINED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yeah",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yeah:
    n 2fcssfltsa "Yeah."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yep",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yep:
    n 2fcsupltsa "Yep."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_uh_huh",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_uh_huh:
    n 1fsqsrltsb "Uh huh."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_nothing_to_say:
    n 2fcssftsa "..."
    n 4kcsupltsa "..."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_kay",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_kay:
    n 3fslsrltsb "'kay."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_good",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_good:
    n 4fsqanltse "{i}Good{/i}."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_door_hit_you",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_door_hit_you:
    n 2fsqemltsb "Hope the door hits you on the way out.{w=0.75}{nw}"
    extend 2fsranltsb " Jerk."

    return { "quit": None }

# Farewells that allow the player to choose to stay

# Natsuki calls the player out on how long they've been here, and asks for more time together
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n 1uskwrlesh "What?{w=0.75}{nw}" 
    extend 4knmemlsbl " You're leaving?{w=1}{nw}" 
    extend 4fnmgslsbl " B-{w=0.1}but you've {i}barely{/i} even been here at all today,{w=0.2} [player]!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 3fcsgslsbr "I mean,{w=0.75}{nw}"
    extend 3fnmpol " you've literally only been here for [time_in_session_descriptor]!"

    show natsuki 3knmpol at jn_center zorder JN_NATSUKI_ZORDER
    menu:
        n "You seriously can't stay just a little longer?"

        "Sure, I can stay a little longer.":
            n 4uchbsl "Yay{nw}{w=0.33}!"
            n 4uskgsl "I-{w=0.2}I mean...!"

            if Natsuki.isLove(higher=True):
                n 1kllssl "T-{w=0.1}thanks,{w=0.1} [player]. It means a lot to me."
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 2kplssl "Really.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
                n 4ksrunl "..."

            else:
                n 1fnmbgl "Y-{w=0.2}yeah!{w=0.5}{nw}" 
                extend 2fcsbgl " That's what I thought!"
                n 2fcssslsbl "Yeah..."
                n 2fnmunl "..."
                n 4fbkwrf "Stop looking at me like that,{w=0.1} jeez!"
                n 3fllpof "Ugh..."

            n 1fllbgl "N-{w=0.1}now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True

        "If you say so.":
            n 1kllpol "...[player]."
            n 2fcspulsbr "I'm not...{w=1}{nw}" 
            extend 2knmsllsbr " {i}forcing{/i} you to be here.{w=1}{nw}" 
            extend 2kllsslsbr " You {i}do{/i} know that,{w=0.5}{nw}" 
            extend 4knmpulsbl " right?"
            n 1ksrsrlsbl "..."
            n 4ksrbolsbl "So..."
            show natsuki 3ksqsrlsbl at jn_center zorder JN_NATSUKI_ZORDER

            menu:
                n "Are you sure you wanna stay?"

                "Yes, I'm sure.":
                    n 3klrpol "Well...{w=0.5}{nw}" 
                    extend 4ksqpol " if you say so."
                    n 1fllcal "I just want to make sure I'm not being a jerk about it."
                    n 4kllpul "But..."

                    if Natsuki.isLove(higher=True):
                        $ chosen_endearment = jn_utils.getRandomEndearment()
                        n 4knmssl "Thanks,{w=0.2} [chosen_endearment].{w=0.75}{nw}" 
                        extend 1kchsslsbl " I really appreciate it."

                    elif Natsuki.isEnamored(higher=True):
                        n 4knmssl "Thanks,{w=0.2} [player].{w=0.75}{nw}" 
                        extend 1kchsslsbl " I...{w=0.3} really appreciate it."

                    else:
                        n 4flrcaf "Thanks,{w=0.2} [player].{w=0.75}{nw}" 
                        extend 1fcscafsbl " It means a lot."

                    $ Natsuki.calculatedAffinityGain()
                    $ jn_globals.player_already_stayed_on_farewell = True

                "No, I have to go.":
                    n 3knmcal "Well...{w=0.3} okay,{w=0.1} [player]."
                    n 4knmpol "Take care out there,{w=0.1} alright?"
                    n 4fchsmlsbl "See you later!"

                    if Natsuki.isEnamored(higher=True):
                        n 2kslcalsbr "..."

                    elif Natsuki.isAffectionate(higher=True):
                        n 2kslbolsbr "..."

                    else:
                        n 2kslbosbr "..."

                    return { "quit": None }

        "Sorry, [n_name]. I really have to leave.":
            n 1fllanl "Nnnnnn-!"
            n 4kcssll "..."
            n 4klrsll "Well...{w=0.3} okay."
            n 2kllpol "Just don't take too long,{w=0.1} alright?"
            n 2fchsmlsbr "See you later,{w=0.1} [player]!"

            if Natsuki.isEnamored(higher=True):
                n 2kslcalsbr "..."

            elif Natsuki.isAffectionate(higher=True):
                n 2kslbolsbr "..."

            else:
                n 2kslbosbr "..."

            return { "quit": None }

    return

# Natsuki calls the player out on how long they've been here, and asks for more time together (alt)
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask_alt",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask_alt:
    n 4knmajl "N-{w=0.2}now wait just one second,{w=0.2} [player]!{w=1}{nw}"
    extend 2fcsgsl " T-{w=0.2}this isn't fair at all!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 2flleml "You've barely been here [time_in_session_descriptor],{w=0.75}{nw}" 
    extend 2fnmajl " and you're {i}already{/i} going?"

    show natsuki 2fcsgslsbl at jn_center zorder JN_NATSUKI_ZORDER
    menu:
        n "Come on!{w=0.5} You'll stay a little longer,{w=0.2} won't you?"

        "Sure, I can stay a while.":
            n 3fcsbsl "H-{w=0.3}Ha!{w=0.75}{nw}" 
            extend 3fsqsslsbr " I knew it."
            n 4fsqsml "Ehehe.{w=0.5}{nw}" 
            extend 1fsqbgleme " Looks like I win again,{w=0.1} [player]!"

            show natsuki 3fcsbgledzsbl at jn_center zorder JN_NATSUKI_ZORDER
            menu:
                n "O-or maybe you just couldn't bring yourself to leave someone as {i}awesome{/i} as me?"

                "You got me, [n_name]. I couldn't leave you even if I tried.":
                    n 2uskwrfesh "W-{w=0.3}wha...?"
                    n 4fcsanf "Nnnnnnn-!"
                    $ player_initial = jn_utils.getPlayerInitial()
                    n 1fbkwrfess "[player_initial]-{w=0.3}[player]!{w=0.75}{nw}"
                    extend 4fllwrf " Don't just come out with stuff like that!"
                    n 2fcspofesi "Yeesh..."

                    if Natsuki.isEnamored(higher=True):
                        extend 2flrpof " I swear you take things way too far sometimes."
                        n 4fsrunfess "..."
                        n 2fcsemlsbr "A-{w=0.2}anyway!"

                    elif Natsuki.isAffectionate(higher=True):
                        extend 2fsqpolsbl " are you {i}trying{/i} to give me a heart attack or something?"
                        n 2fcsajlsbl "A-{w=0.2}anyway."

                    else:
                        extend 2fslsslsbl " your comedy routine {i}definitely{/i} needs more work,{w=0.2} I'll tell you that much!"
                        n 2fcsbolsbl "Well,{w=0.2} anyway..."

                "Whatever, Natsuki.":
                    $ player_was_snarky = True
                    n 3tsqssl "Oh?{w=0.75}{nw}" 
                    extend 3fcsbgl " What's wrong,{w=0.1} [player]?"
                    n 4fsqbgleme "A little {i}too{/i} close to the truth?"
                    extend 4nchgnl " Ehehe."
                    n 1nllssl "Well,{w=0.2} either way."

            n 3fcsbglsbl "I'm just glad you saw the light."
            extend 3fchbll " Even if did take a little persuasion."
            n 1ullaj "So...{w=0.75}{nw}" 
            extend 3fchsm " is there something else you wanna talk about?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Fine, I guess.":
            n 1fsqpu "...You {i}guess{/i}?"
            n 3fnmgsl "What do you mean,{w=0.2} {i}you guess{/i}?!"
            n 3fcspolesi "Jeez...{w=1}{nw}"
            extend 4kslcal " you make it sound like I chained you to the desk or something..."
            n 1fcsajl "Well,{w=0.2} anyway."
            n 2nllbo "I suppose some thanks are in order then."
            n 2nsqbo "..."
            n 2flrem "...{i}I guess{/i}."
            n 4fsgsm "..."
            n 4uchgnlelg "Oh,{w=0.2} lighten up,{w=0.2} [player]!"
            extend 3fchbglelg " Man!"
            n 3fchgnl "You should {i}know{/i} by now I give as good as I get!"
            n 3fchsml "Ehehe."
            n 1tllss "Now,{w=0.2} where were we?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry [n_name], I can't right now.":
            n 1fcsunl "Uuuu-"
            n 1kcspulesi "..."
            n 4fslsll "...I guess that's fine."
            n 3fcsbol "You've got things to do.{w=0.5}{nw}" 
            extend 3fsrcal " I get it."
            n 1fnmtrl "But you're {i}definitely{/i} gonna come visit later."
            n 2kllcal "..."
            n 2knmcasbl "Right?"

            return { "quit": None }
    return

# Natsuki tries to confidently ask her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n 4unmboesu "Huh?{w=0.75}{nw}" 
    extend 2knmaj " You don't really {i}have{/i} to leave already,{w=0.1} do you?"
    n 1fcsgsl "I mean,{w=0.5}{nw}"
    extend 2fllgslsbr " come on!{w=1}{nw}"
    extend 2fnmsf " It feels like you've barely been here!"
    n 3fcseml "I-{w=0.2}in fact,{w=0.75}{nw}"
    extend 3fcsgslsbl " I bet you could {i}easily{/i} hang out with me a little longer!"
    n 1fnmajlsbl "Right,{w=0.2} [player]?"
    n 1fllunlsbr "..."
    show natsuki 4knmbolsbr at jn_center zorder JN_NATSUKI_ZORDER

    menu:
        n "...Right?"

        "Right!":
            n 3fcsbgfsbl "A-{w=0.3}Aha!{w=0.75}{nw}" 
            extend 3flrsslsbl " I knew it!"
            n 1fcsgsl "N-{w=0.2}not like I needed you here, or anything dumb like that.{w=1.25}{nw}"
            extend 2fcspolesi " {i}Obviously{/i}."
            n 2fslemlsbr "You'd have to be pretty lonely to be {i}that{/i} dependent on someone else."
            n 2kslsllsbr "..."
            n 1fcswrfesh "Well,{w=0.2} a-{w=0.2}anyway!{w=1}{nw}"
            extend 4fcspol " Enough of that!"
            n 2fllajl "You already said you were staying,{w=0.2} so..."
            n 4fsldvlsbr "..."

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry, I really need to go.":
            n 1fllsll "...Heh.{w=1}{nw}"
            extend 1fslcal " Right."
            n 2fslunl "..."
            n 2fcswrlsbr "W-{w=0.2}well,{w=0.2} that's fine!"
            n 3flrpolesi "I guess that means I'll just have to test your obedience another time.{w=1}{nw}"
            extend 3fsrdvless " Ehehe."
            n 3fcsbgless "L-{w=0.2}later,{w=0.2} [player]!"

            return { "quit": None }
    return

# Natuski really doesn't want to be alone today; she pleads for her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_pleading_ask:
    n 4kskwrfesh "N-{w=0.3}no!{w=0.5}{nw}" 
    extend 4fbkwrfess " You can't leave yet!"
    n 1klluplsbr "..."
    n 2fcsunl "..."
    n 2fcspulesi "..."
    n 1fnmcal "[player]..."
    n 1fcsemfsbr "I...{w=0.75}{nw}" 
    extend 2fcsunfesssbr " really...{w=1}{nw}" 
    extend 2kslunfesssbr " want you here right now."

    show natsuki 4ksqslfsbl at jn_center zorder JN_NATSUKI_ZORDER

    menu:
        n "Just a few more minutes?{w=0.5} Please?"

        "Of course!":
            n 4kchbsf "Yes!{w=0.66}{nw}"
            n 3fllwrfesh "I-{w=0.2}I mean...!"
            n 3kllslfsbl "..."
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            n 4kllcaf "T-{w=0.2}thanks,{w=0.1} [player].{w=3}{nw}" 
            extend 4fcspofess " You're [chosen_descriptor],{w=0.3} you know that?"
            n 1kllssf "Really.{w=1.5}{nw}" 
            extend 4kslssf " Thank you."
            n 2fcsajfsbr "N-{w=0.2}now,{w=0.75}{nw}" 
            extend 2tnmssfsbr " where were we?"
            n 4flrdvfsbr "Heh..."

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "I can't right now.":
            n 1kslbof "...Oh."
            n 2fcsajlsbl "Well,{w=0.3} if you gotta go,{w=0.3} it can't be helped,{w=0.75}{nw}" 
            extend 2ksrcal " I guess..."
            n 4ksqsll "Just come back soon,{w=0.3} alright?"
            n 1kslpul "..."
            n 4knmbol "...And [player]?"
            n 4ksqbof "..."
            
            if Natsuki.isLove(higher=True):
                show natsuki 4kslsgf at jn_center zorder JN_NATSUKI_ZORDER
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                play audio clothing_ruffle
                $ jnPause(3.5)
                play audio kiss
                $ jnPause(2.5)
                n "L-{w=0.2}love you!"

            else:
                n 1kcsunfess "...I'll miss you.{w=0.75}{nw}"
                show natsuki 4kllunfess
                $ jnPause(1.5)

            return { "quit": None }
    return

# Natsuki gently asks her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_gentle_ask:
    n 1kllsrf "[player]...{w=0.75}{nw}" 
    extend 4knmsrf " do you really have to leave now?"
    n 3kcsbof "I know you have stuff to do,{w=0.5} but..."

    show natsuki 3knmpuf at jn_center zorder JN_NATSUKI_ZORDER
    menu:
        n "You're sure you can't stay even a little longer?"

        "I can stay a little longer.":
            n 4kwmssfeaf "[player]..."
            n 4fcsbofesssbr "T-{w=0.2}thanks.{w=0.75}{nw}"
            extend 2ksrsgf " That...{w=0.5} really means a lot to me."
            n 2ksqcaf "Truly.{w=0.5} Thanks..."
            n 1ksrcaf "..."

            show natsuki 1fbkcaf at jn_center zorder JN_NATSUKI_ZORDER
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            play audio clothing_ruffle
            $ jnPause(3.5)
            show natsuki 1ncspuf at jn_center zorder JN_NATSUKI_ZORDER
            hide black with Dissolve(1.25)

            n 1kslsmfsbl "..."
            n 4kslssfsbl "So..."
            extend 3knmsslsbr " where were we?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry, I really have to go.":
            n 1kllsrf "Oh..."
            n 2fcsemf "I'd be lying if I said I wasn't disappointed...{w=1.5}{nw}" 
            extend 2kslcaf " but I understand."
            n 1kwmsrf "Just be careful out there,{w=0.1} okay?"
            n 1kllsrf "..."
            n 4kwmsmf "I-{w=0.1}I love you,{w=0.1} [player]..."
            n 4kchssfsbl "I'll see you later."

            if (random.choice([True, False])):
                show natsuki 1ksrsgfsbl at jn_center zorder JN_NATSUKI_ZORDER
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                play audio clothing_ruffle
                $ jnPause(3.5)
                play audio kiss
                $ jnPause(2.5)

            return { "quit": None }
    return

# Time-of-day based farewells

# Early morning

# Natsuki thanks the player for visiting so early
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_early_morning_going_this_early",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_early_morning_going_this_early:
    n 1unmpuesu "Eh?{w=1}{nw}"
    extend 3nllsl " Oh."
    n 3nllaj "Well...{w=0.75}{nw}"
    extend 1tnmss " I guess I shouldn't really be surprised.{w=1}{nw}"
    extend 1nlrpol " You must have had a reason to be up this early."
    n 4nsrsslsbr "...I'd hope,{w=0.2} anyway."
    n 3fcssslsbr "Take care out there,{w=0.1} alright?{w=1}{nw}" 
    extend 3nchgnlelg " Don't do anything dumb!"

    if Natsuki.isLove(higher=True):
        n 3fchsmfeaf "Love you,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3fchbll "See you later,{w=0.2} [chosen_tease]!"

    else:
        n 3fchsml "See ya!"

    return { "quit": None }

# Morning

# Natsuki wishes the player a good day
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_morning_heading_off",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_morning_heading_off:
    n 3unmaj "Heading off now,{w=0.2} [player]?{w=1}{nw}" 
    extend 3fchbg " No worries!"

    if Natsuki.isEnamored(higher=True):
        n 3fchbglsbr "I hope your day is as awesome as you are!"

        if Natsuki.isLove(higher=True):
            n 4nchsmf "Ehehe.{w=0.75}{nw}" 
            extend 4fchbgfeaf " Love you,{w=0.1} [player]~!"

        else:
            n 3uchsml "Later!"

    else:
        n 3fchsml "See 'ya!"

    return { "quit": None }

# Afternoon

# Natsuki asks that the player visit later
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_afternoon_come_visit_soon",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_afternoon_come_visit_soon:
    n 1unmaj "Oh?{w=0.75}{nw}" 
    extend 2unmbo " Leaving a little later today,{w=0.1} [player]?"
    n 2ullaj "I guess that's fine...{w=1}{nw}" 
    extend 1fnmca " just remember to come visit soon,{w=0.2} 'kay?"

    if Natsuki.isAffectionate(higher=True):
        n 3fsqcal "I'll be mad if you don't."
        n 3fsqsml "Ehehe.{w=0.75}{nw}" 
        extend 3nchgnlelg " Stay safe,{w=0.2} [player]!"

    else:
        n 3fchsmlsbl "Stay safe!"

    return { "quit": None }

# Evening

# Natsuki wishes the player a good evening
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_evening_good_evening",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_evening_good_evening:
    n 4unmboesu "Eh?{w=0.75}{nw}" 
    extend 1unmaj " You're heading off now,{w=0.1} [player]?"
    n 2ullaj "Well...{w=1}{nw}" 
    extend 2nslcal " alright."
    n 3fchsmlsbl "Have a good evening!"

    if Natsuki.isAffectionate(higher=True):
        n 3kslsllsbl "..."
        n 3kwmbol "...And come see me soon,{w=0.2} alright?"

        if Natsuki.isLove(higher=True):
            n 4kchsmleafsbl "L-{w=0.2}love you!"

    return { "quit": None }

# Night

# Natsuki can't fault the player for turning in
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_night_good_night",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_night_good_night:
    n 3unmaj "Oh?{w=0.75}{nw}" 
    extend 3tnmsl " Are you turning in now?"
    n 4ulraj "Well...{w=1}{nw}" 
    extend 1nlrca " I can't say I blame you.{w=1.25}{nw}"
    extend 2fsqsm " Ehehe."
    n 2uchsm "Good night,{w=0.2} [player]!"

    if Natsuki.isAffectionate(higher=True):
        n 3uchbgl "Sweet dreams!"

    return { "quit": None }
