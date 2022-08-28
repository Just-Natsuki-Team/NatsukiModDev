default persistent._farewell_database = dict()
default persistent.jn_player_first_farewell_response = None
default persistent.jn_player_force_quit_state = 1

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
            ("I'm going to do some chores.", "farewell_option_chores")
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
    n 1fskwrlsbr "[player]!{w=0.2} H-{w=0.1}hang on!{w=0.5}{nw}"
    extend 1fbkwrleexsbr " Wait just a second!"
    n 1fskemlsbl "..."
    n 1kllemlsbl "..."
    n 1kplpu "...Y-{w=0.1}you are coming back,{w=0.1} right?"
    n 1kllunsbl "..."
    n 1kwmemesssbr "...Right?"
    menu:
        "I'll be back.":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.will_be_back)
            $ Natsuki.calculatedAffinityGain(bypass=True)
            n 1unmemlesu "...!{w=0.5}{nw}"
            n 1fllemless "Y-{w=0.1}yeah!{w=0.5}{nw}"
            extend 1fsqpolsbr " You better."
            n 1flremlsbl "Y-{w=0.1}you are reponsible for this,{w=0.1} like I said.{w=0.5}{nw}"
            extend 1flrpol " So..."
            n 1kllpol "..."

        "I don't know.":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.unknown)
            n 1kskem "..."
            n 1kskwr "N-{w=0.5}no!"
            n 1kcsan "You can't do this to me!{w=0.5}{nw}"
            extend 1fcsuptsa " N-{w=0.1}not now..."
            n 1kcsunltsa "..."
            n 1ksqunl "..."
            n 1kplpul "Please,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " it isn't much to ask for...{w=2}{nw}"
            extend 1kwmemsbr " right?"

        "...":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)
            n 1knmemsbr "[player],{w=0.1} c-{w=0.5}come on..."
            n 1kllpu "If this is a joke,{w=0.5}{nw}"
            extend 1fnmgs " it really isn't funny!{w=2}{nw}"
            extend 1knmgssbl " I-{w=0.1}I'm serious!"
            n 1kllunsbl "..."
            n 1knmaj "Please,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " it isn't much to ask for...{w=2}{nw}"
            extend 1kwmem " right?"

    return { "quit": None }

# Only chosen for the first time the player leaves via force quit
label farewell_force_quit:
    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.first_force_quit)
    if not persistent.jn_player_first_farewell_response:
        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.force_quit)

    hide screen hkb_overlay
    show glitch_garbled_a zorder 99 with hpunch
    hide glitch_garbled_a
    stop music
    play audio glitch_c

    n 1uskem "H-{w=0.3}huh?{w=1}{nw}"
    extend 1uscwr " N-{w=0.3}no!{w=0.2} Wait!!{w=0.2} PLEASE-{w=0.3}{nw}"
    show natsuki 1kchupltsa

    play audio static
    show glitch_garbled_b zorder 99 with hpunch
    hide glitch_garbled_b

    return { "quit": None }

# Non-generic farewells - each of these should be registered under FAREWELL_OPTIONS. Affectionate + only.

label farewell_option_sleep:
    if jn_admissions.last_admission_type in (jn_admissions.TYPE_SICK , jn_admissions.TYPE_TIRED):
        # Sick/tired
        n 1kllsl "...[player]."
        n 1knmpu "I...{w=0.75}{nw}" 
        extend 1klrpu " think that'd be a good idea.{w=0.5} You know."
        $ feeling_like = "feeling sick" if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK else "feeling tired"
        n 1klrpu "With what you said earlier about [feeling_like] and all."
        n 1ulraj "So...{w=0.75}{nw}"
        extend 1knmpo " go get some rest,{w=0.1} alright?{w=1}{nw}" 
        extend 1fcspol " We can just talk later anyway."
        n 1fnmgsl "Now get going,{w=0.1} [player]!"
        extend 1fchsml " Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 1fchbgl "Don't let the bedbugs bite!"

        elif Natsuki.isLove(higher=True):
            n 1fchblledz "Love you too~!"

    elif jn_get_current_hour() > 22 or jn_get_current_hour() < 6:
        # Late night
        n 1fwdajesh "A-{w=0.2}and I should think so,{w=0.1} too!{w=0.5}{nw}"
        extend 1tnmem " It seriously took you {i}that{/i} long to notice the time?!"
        n 1fllposbl "Jeez...{w=0.5}{nw}"
        extend 1nllpo " but better late than never,{w=0.1} I guess."
        n 1fllsm "Ehehe.{w=0.5}{nw}"
        extend 1fchsm " Sleep well,{w=0.1} [player]!"

        if Natsuki.isEnamored(higher=True):
            n 1fchbll "See you soon~!"

        elif Natsuki.isLove(higher=True):
            n 1nchsml "Love you~!"

    elif jn_get_current_hour() >= 21:
        # Standard night
        n 1unmaj "About ready to turn in,{w=0.1} huh?"
        n 1ullaj "That's fine...{w=0.5}{nw}"
        extend 1fslca " I guess."
        n 1fcsct "I know you need your beauty sleep and all."
        n 1fsqsm "...Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbll "Sleep tight,{w=0.2} [chosen_tease]!{w=0.5}{nw}"
            extend 1uchsmledz " See you tomorrow~!"

        else:
            n 1fchbgl "No worries!{w=0.2} Sleep well,{w=0.1} [player]!"
        
    elif jn_get_current_hour() >= 19:
        # Early night
        n 1unmaj "Huh?{w=0.75}{nw}" 
        extend 1tnmaj " You're taking an early night?"
        n 1nnmbo "Oh.{w=0.5}{nw}" 
        extend 1nllpu " Well..."
        n 1ullaj "That's fine.{w=0.75}{nw}" 
        extend 1nslpo " I suppose."
        n 1fsqcal "You better stay up with me later though.{w=0.75}{nw}"
        extend 1fsrtrl " You know."
        n 1fsqbglsbl "To make up for lost time and all."
        n 1fchbll "Night,{w=0.1} [player]!"

    else:
        # Nap
        n 1tnmbo "Huh?{w=1}{nw}" 
        extend 1tnmpu " You're taking naps now?"
        n 1tsqcaesd " ...Really?"
        n 1ncsemesi "Jeez...{w=1}{nw}" 
        extend 1fllca " I swear I'm gonna be feeding you next at this rate..."
        n 1fsqdv "..."
        n 1fchbg "Oh,{w=0.3} relax!"
        n 1nchgnelg "I'm kidding,{w=0.1} I'm kidding!{w=0.5}{nw}"
        extend 1tllss " Sheesh."
        n 1fchbg "See you later,{w=0.1} [player]~!"

        if Natsuki.isLove(higher=True):
            n 1uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_eat:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fcsgs "W-{w=0.1}well,{w=0.1} duh!{w=0.5} You {i}said{/i} you were starving!"
        n 1fllpoesi "Jeez..."
        n 1fdtposbr "Just make it something healthy,{w=0.1} got it?"
        n 1fsqsm "...Ehehe."
        n 1fchbg "Enjoy,{w=0.1} [player]!"

    elif jn_get_current_hour() in (7, 8):
        n 1fnmgs "Yeah!{w=0.3} You better!{w=0.5}{nw}"
        extend 1fsqtr " You {i}do{/i} know what they say about breakfast,{w=0.1} right?"
        n 1fsqsml "...Ehehe."
        n 1fchbg "Bon appetit,{w=0.1} [player]!"

    elif jn_get_current_hour() in (12, 13):
        n 1unmaj "Heading out for lunch,{w=0.1} [player]?"
        n 1ulrbo "That's cool,{w=0.3} that's cool."
        n 1nsqsm "Just remember though...{w=0.3}{nw}"
        extend 1fsqss " you are what you eat~."
        n 1fchsm "...Ehehe.{w=0.5}{nw}"
        extend 1uchsm " Enjoy!"

    elif jn_get_current_hour() in (18, 19):
        n 1unmaj "Dinner time,{w=0.1} huh?{w=0.5}{nw}"
        extend 1unmbg " No probs!"
        n 1nlrpu "Just...{w=0.5}{nw}"
        extend 1fdtposbr " make sure it isn't a ready meal.{w=0.5}{nw}"
        extend 1fsqpo " Got it?"
        n 1fsqsm "...Ehehe."
        n 1fchbg "Enjoy,{w=0.1} [player]~!"

    else:
        n 1unmaj "Oh?{w=0.2} You're gonna grab a bite to eat?"
        n 1nllaj "That's fine."
        n 1nsqpo "You better not be filling up on junk though,{w=0.1} [player]."
        n 1fsqsm "...Ehehe.{w=0.5}{nw}"
        extend 1uchbg " Enjoy~!"

    return { "quit": None }

label farewell_option_going_out:
    if jn_is_new_years_eve():
        n 1tsqbg "Oho?{w=0.2} Going out for the new year,{w=0.1} are we?{w=0.5}{nw}"
        extend 1fchbg " Can't say I blame you!"
        n 1ullaj "Just...{w=0.5}{nw}"
        extend 1nsqsl " don't be an idiot out there,{w=0.1} okay?"
        n 1fslsl "I don't want you messing around with drinks and fireworks like a complete moron and getting hurt."
        n 1ullpu "But...{w=0.5}{nw}"
        extend 1uchbg " yeah!{w=0.2} Have fun out there,{w=0.1} [player]!"
        n 1usqbg "And if I don't see you sooner?"
        n 1fbkbs "Happy new year!"

    elif jn_is_easter():
        n 1unmaj "Oh?{w=0.2} You're heading off now?"
        n 1unmbg "Did you have a meal planned for today or something?"
        n 1tlrsm "It {i}is{/i} Easter,{w=0.1} after all!{w=0.5}{nw}"
        extend 1uchsm " Ehehe."
        n 1ullss "Well,{w=0.1} anyway.{w=0.5}{nw}"
        extend 1uchgn " See you later,{w=0.1} [player]!"

    elif jn_is_halloween():
        n 1usqss "Ooh?{w=0.2} Heading out for Halloween,{w=0.1} [player]?"
        n 1fsqsm "Just don't forget..."
        n 1fsqbg "I want my share of treats too!"
        n 1fchgn "Ehehe.{w=0.5}{nw}"
        extend 1uchbg " Have fun~!"

    elif jn_is_christmas_eve():
        n 1unmbo "Oh?{w=0.2} You're heading out for Christmas Eve?"
        n 1kllsl "Well...{w=0.3} okay."
        n 1kllajl "...You will be back in time for Christmas though...{w=0.5}{nw}"
        extend 1knmsll " right?"
        n 1klrbgl "...Ahaha.{w=0.3}"
        extend 1kchbg " See you later,{w=0.1} [player]!"

    elif jn_is_christmas_day():
        n 1unmbo "Huh?{w=0.2} You're heading off now?"
        n 1kllsl "Well...{w=0.3} alright."
        n 1kllss "Thanks for dropping by today though,{w=0.1} [player]."
        n 1kcsssl "It...{w=0.3} really meant a lot to me."
        n 1kchss "See you later,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1kchbg " And Merry Christmas!"

    else:
        n 1unmaj "Oh?{w=0.2} You're heading out,{w=0.1} [player]?"
        n 1fchbg "No worries!{w=0.2} I'll catch you later!"
        n 1nchbg "Toodles~!"

    if Natsuki.isLove(higher=True):
        n 1uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_work:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1knmaj "H-{w=0.1}huh?{w=0.2} You're going to work now?"
        $ time_concern = "late" if jn_get_current_hour() >= 20 else "early"
        n 1kllajsbr "But...{w=0.5}{nw}" 
        extend 1knmgssbr " it's super [time_concern] though,{w=0.1} [player]..."
        n 1kllsll "..."
        n 1fcspusbr "Just...{w=1}{nw}" 
        extend 1kllsl " be careful,{w=0.2} alright?"
        n 1fsqpol "And you {i}better{/i} come visit when you get back."

        if Natsuki.isLove(higher=True):
            n 1fnmcal "Take care,{w=0.1} [player]!"

        else:
            n 1fnmcal "Take care,{w=0.1} [player]!{w=1}{nw}"
            extend 1kchsmleaf " I love you!"
            n 1kllcalsbr "..."

    else:
        n 1unmajesu "Oh?{w=0.2} You're working today?"

        if jn_is_easter():
            n 1uskgs "...And on Easter,{w=0.1} of all days?{w=0.5}{nw}"
            extend 1fslpo " Man..."

        elif jn_is_christmas_eve():
            n 1fskgsl "...On Christmas Eve?{w=0.5}{nw}"
            extend 1kcsemledr " You've gotta be kidding me..."

        elif jn_is_christmas_day():
            n 1fskwrl "...On {i}Christmas{/i}?!{w=0.5}{nw}"
            extend 1kcsemledr " Ugh..."
            n 1fslpol "..."
            n 1fslajl "Well..."

        elif jn_is_new_years_eve():
            n 1fskgsl "...And on New Year's Eve,{w=0.1} too?!{w=0.5}{nw}"
            extend 1kcsemledr " Jeez..."

        elif not jn_is_weekday():
            n 1uwdaj "A-{w=0.1}and on a weekend,{w=0.1} too?{w=0.5}{nw}"
            extend 1kslpu " Man..."

        n 1nlrpo "It sucks that you've gotta work,{w=0.1} but I get it.{w=0.2} I guess."
        n 1fnmpo "...You better come finish when you visit though."
        n 1fsqsm "Ehehe."
        n 1fchbg "Take it easy,{w=0.1} [player]!{w=0.2} Don't let anyone push you around!"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1uchbgf "You got this,{w=0.1} [chosen_endearment]!{w=0.2} Love you~!"

        elif Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1uchbgl "I believe in you,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_school:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1tnmem "...School?{w=1}{nw}" 
        extend 1fskgsesh " A-{w=0.1}At this hour?"

        if jn_is_easter():
            n 1kwdgs "...And on {i}Easter{/i},{w=0.1} of all days?}"

        elif jn_is_christmas_eve():
            n 1fskgsl "...And on {i}Christmas Eve{/i}?"

        elif jn_is_christmas_day():
            n 1fskwrl "...And on {i}Christmas{/i}?!"

        elif jn_is_new_years_eve():
            n 1fskgsl "...And on New Year's Eve,{w=0.1} too?!"

        if not jn_is_weekday():
            extend 1uskwr " A-{w=0.1}and on a {i}weekend{/i} too?!"

        n 1fbkwrean "What the hell kind of school is thaaaat?!"
        n 1kllpo "Jeez.{w=0.5}{nw}"
        extend 1fslsr " And I thought my school experience was bad enough."
        n 1kcspu "Just...{w=0.5}{nw}"
        extend 1knmpu " take care getting there,{w=0.1} alright?"
        $ time_concern = "late" if jn_get_current_hour() >= 20 else "early"
        extend 1fllsrsbl " It's really [time_concern],{w=0.1} after all."
        n 1kllss "Study hard,{w=0.1} [player]!"

    else:
        if jn_is_easter():
            n 1uskgs "...And on Easter,{w=0.1} of all days?{w=0.5}{nw}"
            extend 1fslpo " Man..."

        elif jn_is_christmas_eve():
            n 1fskgsl "...On Christmas Eve?{w=0.5}{nw}"
            extend 1fcseml " You've gotta be kidding me..."

        elif jn_is_christmas_day():
            n 1fskwrl "...On {i}Christmas{/i}?!{w=0.5}{nw}"
            extend 1fcseml " Ugh..."
            n 1fslpol "..."
            n 1fslajl "Well..."

        elif jn_is_new_years_eve():
            n 1fskgsl "...And on New Year's Eve,{w=0.1} too?!{w=0.5}{nw}"
            extend 1fcseml " Jeez..."

        elif jn_is_weekday():
            n 1unmaj "Off to school,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nchsm " No worries!"

        else:
            n 1tnmpu "Huh?{w=0.2} You're at school today?{w=0.5}{nw}"
            extend 1nsqpu "...On a {i}weekend{/i}?"
            n 1fslpu "..."
            n 1fsqpo "Gross..."

        n 1tsqsm "Sucks to be you though,{w=0.1} huh?{w=0.5}{nw}"
        extend 1fchsm " Ehehe."
        n 1fchbg "No slacking off,{w=0.1} [player]!{w=0.2} I'll see you later!"

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1uchbgf "Love you!"

    return { "quit": None }

label farewell_option_misc_activity:
    n 1knmpu "H-{w=0.1}huh?{w=0.5}{nw}"
    extend 1kllaj " And you gotta leave to do that too?"
    n 1fcsun "Nnnnnn...{w=0.5}{nw}"
    extend 1kcsaj " okay."
    n 1fnmpol "...But you better come visit once you're done."
    extend 1klrpo "{w=0.2} Got it?"
    n 1kllpo "See you soon,{w=0.1} [player]!"

    if Natsuki.isLove(higher=True):
        n 1kllssf "Love you!"

    return { "quit": None }

label farewell_option_play:
    n 1fsqaj "...Really,{w=0.5} [player]?"
    n 1nslpu "You'd seriously rather play some {i}game{/i}...{w=0.5}{nw}"
    extend 1fsqsf " than hang out with {i}me{/i}?"
    n 1fcssl "..."
    n 1uchgneme "Well,{w=0.1} your loss!{w=0.5}{nw}"
    extend 1fchbgelg " Ahaha!"
    n 1nllbg "No,{w=0.1} no.{w=0.2} It's fine.{w=0.2} You go do that,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nsqbg " Besides..."
    n 1usqct "You sure could use the practice,{w=0.1} huh?{w=0.5}{nw}"
    extend 1fchsm " Ehehe."
    $ chosen_tease = jn_utils.getRandomTease()
    n 1fchbg "Catch you later,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_studying:
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fskgs "[player_initial]-{w=0.1}[player]!"
    n 1fllansbr "If I'd known you were meant to be studying I'd have thrown you out myself!{w=0.5}{nw}"
    extend 1fcspoesi " Geez..."
    n 1nsqposbl "I really hope you don't have exams tomorrow or something like that..."
    n 1flrpo "But either way,{w=0.1} you'll be fine.{w=0.2} Just go!{w=0.5}{nw}"
    extend 1fwdaj " Go!"
    n 1fchgn "...Shoo,{w=0.1} you dummy!{w=0.2} Ehehe.{w=0.5}{nw}"
    extend " We'll talk later!"

    if Natsuki.isLove(higher=True):
        n 1uchbgf "Love you~!"

    return { "quit": None }

label farewell_option_chores:
    if store.jn_get_current_hour() >= 20 or store.jn_get_current_hour() <= 4:
        n 1tnmaj "...Chores?{w=0.5}{nw}"
        extend 1tsqem " At {i}this{/i} time?"
        n 1nllbo "I gotta say,{w=0.1} [player]."
        n 1nsqdv "You're either dedicated or desperate.{w=0.5}{nw}"
        extend 1nchsm " Ehehe."
        n 1ullss "Well,{w=0.1} whatever.{w=0.5}{nw}"
        extend 1tnmss " Just hurry up and go sleep,{w=0.1} 'kay?"

        if Natsuki.isLove(higher=True):
            n 1uchbg "Later,{w=0.1} [player]!"
            extend 1uchbgf " Love you~!"

        else:
            n 1fchbg "Later,{w=0.1} [player]!"

    else:
        n 1tnmsg "Stuck on chore duty,{w=0.1} huh?"
        n 1nchsm "Ehehe.{w=0.2} Yeah,{w=0.1} that's fine.{w=0.5}{nw}"
        extend 1fchgn " You go take care of your clean streak!"

        if Natsuki.isLove(higher=True):
            n 1uchbg "Later,{w=0.1} [player]!{w=0.5}{nw}"
            extend 1uchbgf " Love you~!"

        else:
            n 1fchbg "Ehehe.{w=0.2} Later,{w=0.1} [player]!"

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
    extend 1kplsfl " you're leaving now,{w=0.2} [player]?" 
    n 1klrcal "Well...{w=1}" 
    extend 1ksrcal " okay."
    n 1fnmtrf "Y-{w=0.2}you better take care,{w=0.2} [player]!{w=0.5}" 
    extend 1kchssfeaf " You mean the world to me!"

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
    n 1fsqtrl "You know I don't like saying goodbye,{w=0.1} [player]..."
    n 1kcssllesi "..."
    n 1fcsgsfess "I-{w=0.2}I'll be okay!{w=1}{nw}"
    extend 1fcsajf "Just..."
    n 1knmpof "...get back here soon,{w=0.2} alright?"
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
    extend 1fslpol " I never like saying goodbye to you..."
    n 1kslbol "But...{w=0.5}{nw}" 
    extend 1kslssl " I guess it can't be helped sometimes."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1fcsajl "S-{w=0.2}so!"
    n 1fsqtrf "You better take care of yourself out there,{w=0.1} [chosen_endearment]." 
    n 1fchgnl "...'Cuz I'm counting on you!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 1fchblleaf "Later,{w=0.2} [chosen_tease]!"

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
    n 1unmajl "Oh?{w=0.2} You're heading out now?"
    n 1flrpol "That's...{w=0.5} fine.{w=0.75}{nw}" 
    extend 1fsrsll " I guess."
    n 1kplcal "...You know I'll really miss you,{w=0.1} [player]."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1flrssfsbr "S-{w=0.2}so you better do your best for me,{w=0.1} [chosen_endearment]!"
    n 1fchsmf "Ehehe.{w=0.75}{nw}"
    extend 1uchsmfeaf " See you soon!"

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
    n 1unmajl "Huh?{w=0.2} You're leaving now?"
    n 1fcssll "I always hate it when you have to go somewhere..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kcssml "...But I know you'll always be back for me,{w=0.1} [chosen_endearment]."
    n 1fllssfsbl "N-{w=0.2}not like you {i}have{/i} a choice,{w=0.2} obviously!"
    n 1fsqsmf " Ehehe."
    n 1fchblfeaf "Make me proud,{w=0.2} [player]!{w=0.3} I'm rooting for you!"

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
    n 1kllpul "Awww...{w=0.75}{nw}" 
    extend 1kllpol " well okay."
    n 1fnmcal "You take care of yourself,{w=0.2} got it?" 
    extend 1fcsssl " Or you'll have me to deal with!"
    n 1fsqsml "Ehehe."
    n 1fchbgfeaf "Bye now!{w=0.5} I love you~!"

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
    n 1kwmpol "Time to go,{w=0.1} [player]?"
    n 1kllssl "Sometimes I wish you could just stay forever..."
    n 1fcsajf "But I understand you've got stuff to do."
    n 1fslssfsbl "...Even if it isn't as important as me."
    extend 1nchgnl " Ehehe."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1fchbgf "Later,{w=0.2} [chosen_endearment]!"

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
    n 1unmajl "Hmm?{w=0.2} You're leaving now?"
    n 1knmsll "Aww,{w=0.1} man..."
    n 1kllpol "And I was having fun,{w=0.1} too..."
    n 1unmbgl "Well,{w=0.1} if you gotta go,{w=0.1} you gotta go!"
    n 1uchbgl "Take care,{w=0.1} [player]!{w=0.2} Make me proud!"

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
    n 1unmajl "You're going,{w=0.1} [player]?"
    n 1kplpol "Uuuuu...{w=0.3} okay..."
    n 1knmpol "Hurry back if you can,{w=0.1} alright?"
    n 1nnmsml "I'll be waiting for you!"
    n 1nchbgl "Goodbye,{w=0.1} [player]!"

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
    n 1unmajl "Huh?{w=0.2} You're leaving?"
    n 1kcssfl "..."
    n 1kcssll "That's fine...{w=0.3} I'll be okay..."
    n 1fplcaf "You better come back soon,{w=0.1} alright [player]?"
    n 1kchsml "Goodbye!{w=0.2} I'll be waiting!"

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
    n 1unmajl "Oh?{w=0.2} Heading off now,{w=0.1} [player]?"
    n 1kllpol "I...{w=0.3} wish you didn't have to..."
    n 1knmssl "But I get that you have things to do."
    n 1knmajl "You better come see me later,{w=0.1} promise?"
    n 1fchdvl "Don't make me come find you!{w=0.2} Ehehe."

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
    n 1unmajl "Mmm?{w=0.2} You're going now,{w=0.1} [player]?"
    n 1fcspol "I was hoping you'd be around longer..."
    n 1nllnvl "Well,{w=0.2} I'll be okay!"
    n 1fnmcaf "Take care of yourself,{w=0.1} [player]!{w=0.2} A-{w=0.1}and not just for your sake,{w=0.1} got it?"
    n 1kchbgl "See you later!"

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
    n 1tnmajl "You're leaving now,{w=0.1} [player]?"
    n 1fllcal "Nnnnnn...{w=0.3} alright."
    n 1knmcaf "You better be back later,{w=0.1} okay?{w=0.2} I...{w=0.3} enjoy our time together."
    n 1kllsmf "See you soon,{w=0.1} [player]!"

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
    n 1fllcal "Well,{w=0.1} I guess you had to leave eventually."
    n 1fnmpol "Doesn't mean I have to like it,{w=0.1} though..."
    n 1kplpol "Come see me soon,{w=0.1} 'kay?"

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
    n 1unmsm "Going now,{w=0.1} [player]?{w=0.2} I'll see you later!"

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
    n 1unmaj "Heading off now,{w=0.1} [player]?"
    n 1nnmsm "Alright!{w=0.2} Take care!"

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
    n 1nchss "Okaaay!{w=0.2} I'll be waiting for you!"
    n 1nnmsm "Stay safe,{w=0.1} [player]!"

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
    n 1nnmbg "See you later,{w=0.1} [player]!"
    n 1nchsm "Take care!"

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
    n 1nchbg "Goodbye,{w=0.1} [player]!"
    n 1nchsm "Come see me soon,{w=0.1} alright?"

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
    n 1nchsm "See you later,{w=0.1} [player]!"
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
    n 1nnmss "Later,{w=0.1} [player]!"

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
    n 1nchsm "Goodbye,{w=0.1} [player]!"

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
    n 1nwmss "'kay!{w=0.2} Bye for now!"

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
    n 1nchbg "See ya,{w=0.1} [player]!"

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
    n 1nnmsl "Bye,{w=0.1} [player]."
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
    n 1nnmsf "Later,{w=0.1} [player]."
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
    n 1fllsf "'kay.{w=0.2} Later."
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
    n 1flrsf "Goodbye,{w=0.1} [player]."
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
    n 1fsqsf "See you around."
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
    n 1fcssf "Yeah."
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
    n 1fcsup "Yep."
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
    n 1fsqsltsb "Uh huh."
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
    n 1fcssftsa "..."
    n 1kcsuptsa "..."
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
    n 1fslsrtsb "'kay."
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
    n 1uskwrl "What?{w=0.2} You're leaving?{w=0.2} But you've barely been here at all today,{w=0.1} [player]!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 1fnmpol "You've literally only been here for [time_in_session_descriptor]!"
    menu:
        n "You really can't stay just a little longer?"

        "Sure, I can stay a little longer.":
            n 1uchbsl "Yay{nw}!"
            n 1uskgsl "I-I mean...!"
            if Natsuki.isLove(higher=True):
                n 1kllssl "T-{w=0.1}thanks,{w=0.1} [player]. It means a lot to me."
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 1kplssl "Really.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
                n 1klrbgl "...A-{w=0.1}anyway!"

            else:
                n 1fnmbgl "Yeah!{w=0.2} That's what I thought!"
                n 1fcsbgl "Yeah..."
                n 1fnmunl "..."
                n 1fbkwrf "Stop looking at me like that,{w=0.1} jeez!"
                n 1fllpof "Ugh..."

            n 1fllbgl "N-{w=0.1}now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True

        "If you say so.":
            n 1kllpol "[player]..."
            n 1knmpol "I'm not...{w=0.3} forcing you to be here.{w=0.1} You know that,{w=0.1} right?"
            menu:
                n "Are you sure you wanna stay?"

                "Yes, I'm sure.":
                    n 1knmpol "Well,{w=0.1} if you're sure."
                    n 1kllcal "I just want to make sure I don't sound all naggy."
                    if Natsuki.isEnamored(higher=True):
                        $ chosen_endearment = jn_utils.getRandomEndearment()
                        n 1knmssl "Thanks,{w=0.1} [chosen_endearment]. You know it means a lot to me."

                    else:
                        n 1nlrcaf "Thanks,{w=0.1} [player].{w=0.2} It means a lot."

                    $ Natsuki.calculatedAffinityGain()
                    $ jn_globals.player_already_stayed_on_farewell = True

                "No, I have to go.":
                    n 1knmcal "Well...{w=0.3} okay,{w=0.1} [player]."
                    n 1knmpol "Take care out there,{w=0.1} alright?"
                    n 1uchsml "See you later!"

                    return { "quit": None }

        "Sorry, [n_name]. I really have to leave.":
            n 1fllanl "Nnnnnn-!"
            n 1kcssll "..."
            n 1klrsll "Well...{w=0.3} okay."
            n 1kllpol "Just don't take too long,{w=0.1} alright?"
            n 1knmsml "See you later,{w=0.1} [player]!"

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
    n 1knmgsl "N-{w=0.1}now wait just one second,{w=0.1} [player]!{w=0.2} This isn't fair at all!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 1knmpol "You've barely been here [time_in_session_descriptor],{w=0.1} and you're already going?"
    menu:
        n "Come on!{w=0.2} You'll stay a little longer,{w=0.1} won't you?"

        "Sure, I can stay a while.":
            n 1fcsbsl "H-{w=0.1}Ha!{w=0.2} I knew it."
            n 1fsqdvl "Ehehe.{w=0.1} Looks like I win again,{w=0.1} [player]!"
            menu:
                n "O-or maybe you just can't bring yourself to leave my side?"

                "You got me, [n_name]. I couldn't leave you even if I tried.":
                    $ player_was_snarky = False
                    n 1uscwrf "W-{w=0.2}wha...?"
                    n 1fcsunf "Nnnnnnn-!"
                    $ player_initial = list(player)[0]
                    n 1fbkwrf "[player_initial]-{w=0.2}[player]!"
                    n 1fllwrf "Don't just come out with stuff like that!"
                    n 1fllpof "Jeez...{w=0.3} you're such a dummy sometimes..."

                "Yeah, yeah.":
                    $ player_was_snarky = True
                    n 1fsqbgf "Ehehe.{w=0.2} What's wrong,{w=0.1} [player]?"
                    n 1tsqdvf "A little too close to the truth?"
                    n 1uchbsfelg "Ahaha!"

            n 1nllbgl "Well,{w=0.1} either way,{w=0.1} I'm glad you can stay a little longer!"

            if player_was_snarky:
                n 1nsqbgf "Or...{w=0.3} perhaps you should be thanking {i}me{/i}?{w=0.2} Ehehe."

            n 1nchsml "So...{w=0.3} what else did you wanna do today?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Fine, I guess.":
            n 1fbkwrf "You {i}guess{/i}?{w=0.2} What do you mean,{w=0.1} you guess?!"
            n 1fnmpol "Jeez...{w=0.3} what's with the attitude today,{w=0.1} [player]?"
            n 1fllpof "Well,{w=0.1} anyway...{w=0.3} Thanks for staying with me a little longer."
            n 1fsgsgl "...{i}I guess{/i}."
            n 1uchgnlelg "Ahaha!{w=0.2} Oh,{w=0.1} lighten up,{w=0.1} [player]!{w=0.2} I'm just messing with you!"
            n 1tllsml "Ehehe.{w=0.2} Now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry [n_name], I can't right now.":
            n 1fcsunf "Uuuu-"
            n 1kllcaf "Well,{w=0.1} I guess that's fine.{w=0.2} It can't be helped,{w=0.1} after all."
            n 1fnmajf "But you gotta make it up to me,{w=0.1} alright?"
            n 1kchbgl "Stay safe,{w=0.1} [player]!{w=0.2} I'll see you later!"

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
    n 1knmaj "Huh?{w=0.2} You don't really have to leave already,{w=0.1} do you?"
    n 1fllsf "It feels like you've barely been here!"
    n 1flldv "I-{w=0.1}I totally bet you can hang out with me a little longer!{w=0.2} Right,{w=0.1} [player]?"
    menu:
        n "{w=0.3}...right?"

        "Right!":
            n 1fcsbgl "A-Aha!{w=0.2} I knew it!"
            n 1fllbg "I-{w=0.1}I totally don't need you here,{w=0.1} or anything dumb like that!"
            n 1flldvl "You'd have to be pretty lonely to be {i}that{/i} dependent on someone else...{w=0.3} ahaha..."
            n 1klrsll "..."
            n 1fcswrf "J-{w=0.1}jeez!{w=0.2} Let's just get back to it already..."
            n 1fllajf "Now,{w=0.1} where were we?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry, I really need to go.":
            n 1fllbgf "O-{w=0.1}oh...{w=0.3} aha..."
            n 1fllpol "That's fine,{w=0.1} I guess..."
            n 1fnmbg "I'll see you later then,{w=0.1} [player]!"
            n 1knmpo "Don't keep me waiting,{w=0.1} alright?"

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
    n 1kskwrf "N-no!{w=0.2} You can't leave yet!"
    n 1kllupf "..."
    n 1kcssfl "[player]..."
    n 1klrsff "{w=0.3} I...{w=0.3} really...{w=0.3} want you here right now."
    menu:
        n "Just stay with me a little longer...{w=0.3} please?"

        "Of course!":
            n 1kchbsf "Yes!{nw}"
            n 1knmajf "I-I mean...!"
            n 1kllslf "..."
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            n 1kllnvf "T-{w=0.1}thanks,{w=0.1} [player].{w=0.1} You're [chosen_descriptor],{w=0.1} you know that?"
            n 1kplsmf "Really.{w=0.1} Thank you."
            n 1kllbgf "N-{w=0.1}now,{w=0.1} where were we? Heh..."
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "I can't right now.":
            n 1kllsff "Oh..."
            n 1knmajl "Well,{w=0.1} if you gotta go,{w=0.1} it can't be helped,{w=0.1} I guess..."
            n 1kplpol "Come back soon,{w=0.1} alright?"
            n 1klrsmf "Or you'll have to make it up to me...{w=0.3} ahaha..."
            n 1knmsmf "Stay safe,{w=0.1} [player]!"

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
    n 1knmsrf "[player]...{w=0.3} do you really have to leave now?"
    n 1kplsrf "I know you have stuff to do,{w=0.1} but I...{w=0.3} really...{w=0.3} wanna spend more time with you."
    menu:
        n "Are you sure you have to go?"

        "I can stay a little longer.":
            n 1kplsmf "[player]..."
            n 1kchsmf "Thank you.{w=0.2} That really means a lot to me right now."
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            n 1kwmssf "Y-{w=0.1}You're [chosen_descriptor],{w=0.1} [player]."
            n 1kcssmf "Truly.{w=0.1} Thanks..."
            n 1kcssmf "..."
            n 1kllbgf "Aha...{w=0.3} so what else did you wanna do today?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()

        "Sorry, I really have to go.":
            n 1kllsrf "Oh..."
            n 1kplsmf "I'd be lying if I said I wasn't disappointed,{w=0.1} but I understand."
            n 1kwmsrf "Just be careful out there,{w=0.1} okay?"
            n 1kllsrf "..."
            n 1kwmsmf "I-{w=0.1}I love you,{w=0.1} [player]..."
            n 1kchsmf "I'll see you later."

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
    n 1tnmaj "H-{w=0.1}huh?{w=0.2} You're going this early?"
    n 1kllsl "...Oh."

    if Natsuki.isEnamored(higher=True):
        n 1klrssl "I...{w=0.3} was hoping we could hang out longer...{w=0.3} but if you gotta go,{w=0.1} then you gotta go."
        n 1unmbgl "Thanks for stopping by though,{w=0.1} [player].{w=0.2} I really appreciate it."
        n 1knmssl "Just don't rush things for my sake,{w=0.1} alright?"

    else:
        n 1fchbgf "I-{w=0.1}I mean,{w=0.1} it was cool of you to drop by,{w=0.1} [player]!"

    n 1uchgnl "Take care out there,{w=0.1} 'kay?{w=0.2} Don't do anything dumb!"

    if Natsuki.isLove(higher=True):
        n 1uchbsf "Love you,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 1uchbgl "See you later,{w=0.1} [chosen_tease]!"

    else:
        n 1uchsml "See ya!"

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
    n 1nnmbg "Heading off now,{w=0.1} [player]?{w=0.2} No worries!"

    if Natsuki.isEnamored(higher=True):
        n 1nchbgl "I hope your day is as great as you are."

        if Natsuki.isLove(higher=True):
            n 1nchsmf "Ehehe.{w=0.2} Love you,{w=0.1} [player]~!"

        else:
            n 1uchsml "Later!"

    else:
        n 1unmbg "See ya!"

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
    n 1unmaj "Oh?{w=0.2} Leaving a little later today,{w=0.1} [player]?"
    n 1ullaj "I guess that's fine...{w=0.3} just remember to come visit soon,{w=0.1} 'kay?"

    if Natsuki.isAffectionate(higher=True):
        n 1fnmcal "I'll be mad if you don't."
        n 1uchbgl "Ehehe.{w=0.2} Stay safe,{w=0.1} [player]!"

    else:
        n 1nnmsm "Stay safe!"

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
    n 1unmaj "Huh?{w=0.2} You're heading off now,{w=0.1} [player]?"
    n 1ullaj "Well...{w=0.3} alright."
    n 1nchsm "Have a good evening!"

    if Natsuki.isAffectionate(higher=True):
        n 1kwmsml "Come see me soon,{w=0.1} 'kay?"

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
    n 1unmaj "Oh?{w=0.2} Are you turning in now?"
    n 1nnmbg "Well...{w=0.3} I can't say I blame you."
    n 1uchsm "Good night,{w=0.1} [player]!"

    if Natsuki.isAffectionate(higher=True):
        n 1uchbgl "Sweet dreams!"

    return { "quit": None }
