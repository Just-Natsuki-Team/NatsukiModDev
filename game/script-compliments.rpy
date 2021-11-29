default persistent._compliment_database = dict()

init 0 python in jn_compliments:
    import random
    import store

    COMPLIMENT_MAP = dict()

    # Compliment types
    TYPE_AMAZING = 0
    TYPE_BEAUTIFUL = 1
    TYPE_CONFIDENT = 2
    TYPE_CUTE = 3
    TYPE_HILARIOUS = 4
    TYPE_INSPIRATIONAL = 5
    TYPE_STYLE = 6
    TYPE_THOUGHTFUL = 7

    # The last compliment the player gave to Natsuki
    last_compliment_type = None

    def get_all_compliments():
        """
        Gets all compliment topics which are available

        OUT:
            List<Topic> of compliments which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            COMPLIMENT_MAP.values(),
            affinity=store.jn_affinity.get_affinity_state(),
            unlocked=True
        )

init 1 python:
    try:
        # Resets - remove these later, once we're done tweaking affinity/trust!
        persistent._compliment_database.clear()

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

label player_compliments_start:
    python:
        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in jn_compliments.get_all_compliments()
        ]
        compliment_menu_items.sort()

    call screen scrollable_choice_menu(compliment_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're amazing!",
            label="compliment_amazing",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_AMAZING:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uskemf "[player]...{w=0.3} honestly!{w=0.2} Jeez..."
            n 1kllssl "But...{w=0.3} thanks.{w=0.2} It really means a lot to me."
            n 1fchbgl "You're amaazing too,{w=0.1} though.{w=0.2} Remember that!"

        else:
            n 1kchbgl "Jeez,{w=0.1} [player]...{w=0.3} you're really doling out the compliments today,{w=0.2} aren't you?"
            n 1kllbgl "Don't get me wrong{w=0.1} -{w=0.1} I'm not complaining!"
            n 1ksqsm "Make sure you don't leave yourself out though,{w=0.1} 'kay?"
            n 1kchsml "Ehehe."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1kwmpul "Y{w=0.1}-you really think so,{w=0.1} [player]?"
            n 1kllsrl "..."
            n 1fcssrl "I-{w=0.1}I don't like to admit it,{w=0.1} you know."
            n 1klrssl "But...{w=0.3} that means... a lot to me,{w=0.1} [player]."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n 1kwmnvl "Really.{w=0.2} Thank you.{w=0.2} You're honestly [chosen_descriptor]."
            n 1klrnvl "..."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1kwmsmf "Love you,{w=0.1} [player]..."

            $ relationship("affinity+")

        else:
            n 1flrbsl "O-{w=0.1}oh!{w=0.2} Aha!{w=0.2} I knew you'd admit it eventually!"
            n 1nchgnl "W-{w=0.1}well,{w=0.1} I'm just glad both of us agree on that."
            n 1flrbgl "Thanks,{w=0.1} [player]!"

            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n 1fwmpul "But...{w=0.3} don't think that means you don't have something going for you too!"
                n 1fllssl "You're...{w=0.3} pretty awesome too,{w=0.1} [player].{w=0.2} You better remember that,{w=0.1} 'kay?"
                n 1klrbgl "Ahaha..."

            $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_AMAZING
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're beautiful!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_BEAUTIFUL:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uskwrf "J-{w=0.1}jeez,{w=0.1} [player]...!"
            n 1fcsanf "Uuuuuu-!"
            n 1fbkwrf "Are you trying to put me on the spot or what?!{w=0.2} You already told me thaaat!"
            n 1flrpof "..."
            n 1klrpol "..."
            n 1klrpul "...I-I'll take it,{w=0.1} though."
            n 1fllsll "The compliment,{w=0.1} I mean."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1kllssl "T-{w=0.1}thanks again,{w=0.1} [chosen_tease]."

        else:
            n 1fskwrf "E-{w=0.1}excuse me?!"
            n 1fbkwrf "[player]!{w=0.2} What did I tell you?!"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1fcsanf "Seriously...{w=0.3} are you trying to give me a heart attack or something,{w=0.1} [chosen_tease]?!"
            n 1fllpof "..."

            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n 1fcspuf "Just...{w=0.3} save it until I can be sure you really mean it,{w=0.1} alright?"
                n 1kllpol "Jeez..."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uskpuf "H-{w=0.1}huh?!"
            n 1uskajf "Wait..."
            n 1uskpuf "Y-{w=0.1}you really think I'm..."
            n 1uscunf "I-{w=0.3}I'm..."
            n 1fcsunf "..."
            n 1fnmunf "[player]..."
            n 1knmpuf "You know you're not meant to just say things like that..."
            n 1kllpuf "Unless you really mean it?"
            n 1kcsunf "..."
            n 1klrssf "...I...{w=0.3} believe you,{w=0.1} though.{w=0.2} Just don't make me regret saying that,{w=0.1} okay?"
            n 1klrbgl "T-{w=0.1}thanks,{w=0.1} [player]."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n 1kwmsmf "...Love you,{w=0.1} [player]...{w=0.3} Ahaha..."

            $ relationship("affinity+")

        else:
            n 1uscemf "W{w=0.1}-w{w=0.1}-what?"
            n 1fskwrf "W-{w=0.1}what did you say?!"
            n 1fcsanf "Nnnnnnnnnn-!"
            n 1fbkwrf "Y-{w=0.1}you can't just say things like that so suddenly,{w=0.1} you dummy!"
            n 1fllemf "Sheesh..."

            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n 1kllunl "..."
                n 1flrajl "I mean,{w=0.1} I'm flattered,{w=0.1} but..."
                n 1fcsanl "Uuuuuu...{w=0.3} just stop it for now,{w=0.1} okay?"
                n 1fllpof "You're making this all super awkward..."

            $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_BEAUTIFUL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how confident you are!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CONFIDENT:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1fchbg "Ehehe.{w=0.2} I'm glad you still think so,{w=0.1} [player]!"
            n 1uchsm "That's what it means to be a pro,{w=0.1} right?"
            n 1kllss "Ahaha..."

        else:
            n 1fchbg "Ahaha.{w=0.2} I'm glad you still think so, [player]!"
            n 1uchsm "I try my best,{w=0.1} after all."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1fchbg "Ehehe.{w=0.2} I just radiate confidence,{w=0.1} don't I?"
            n 1kllss "..."
            n 1kllsl "Well...{w=0.3} to tell you the truth,{w=0.1} [player]."
            n 1fcssr "I...{w=0.3} really...{w=0.3} wish I could say it was {i}all{/i} genuine."
            n 1kllsr "But having you here with me...{w=0.3} it helps,{w=0.1} you know.{w=0.2} A lot."
            n 1klrss "So...{w=0.3} thanks,{w=0.1} [player].{w=0.2} Really."
            $ relationship("affinity+")

        else:
            n 1uskajl "H-{w=0.1}huh?"
            n 1fchbgl "O-{w=0.1}oh!{w=0.2} Well of course you do!"
            n 1fcsbgl "I have a lot to be confident about,{w=0.1} after all!"
            n 1flrssl "Wouldn't you agree?"

            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n 1uchgnl "Oh,{w=0.1} who am I kidding.{w=0.2} Of course you do."
                n 1uchbsl "Ahaha!"

            $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're cute!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CUTE:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "..."
            n "..."
            n "..."
            n "Urgh!"
            n "Alright,{w=0.1} fine!{w=0.2} Fine!{w=0.2} You win,{w=0.1} okay?!"
            n "I'm kinda...{w=0.3} maybe...{w=0.3} sorta...{w=0.3} somehow..."
            n "In an abstract way..."
            n "...{w=0.3}'cute.'"
            n "..."
            n "There.{w=0.3} I said it, [player].{w=0.3} I said it.{w=0.3} Hooray for you."
            n "Are we done?{w=0.3} Are you happy?{w=0.3} Are you {i}pleased{/i} with yourself now?"
            n "Jeez..."
            n "I swear,{w=0.1} you're such a goofball sometimes..."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n "Besides,{w=0.1} I'm not even the cutest here,{w=0.1} anyhow..."
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n "I guess I'll let you figure out the rest,{w=0.1} [chosen_tease].{w=0.2} Ehehe."

        else:
            n "Nnnnnnn-!"
            n "How many times do I have to say this,{w=0.1} [player]?!"
            n "{i}I'm not cute!{/i}"
            n "Jeez..."
            n "Now I {i}know{/i} you just wanted me to say that,{w=0.1} didn't you?"
            n "Really now...{w=0.3} you're such a jerk sometimes,{w=0.1} [player]."

            if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
                n "You're just lucky I like you,{w=0.1} honestly."
                n "Or I wouldn't be nearly this patient.{w=0.2} Ehehe."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "A-{w=0.1}Aha!{w=0.2} Nope!"
            n "Nice try,{w=0.1} [player]!"
            n "You're not gonna get me to say it that easily!{w=0.2} Ehehe."

        else:
            n "W-{w=0.1}what?{w=0.2} What did you just say?!"
            n "..."
            n "..."
            n "I...{w=0.3} must have misheard you."
            n "Yeah.{w=0.2} I totally misheard you.{w=0.2} One hundred percent."

    $ last_compliment_type = jn_compliments.TYPE_CUTE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of humour!",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_HILARIOUS:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Aww,{w=0.1} [player]!{w=0.2} Thanks!{w=0.2} I pride myself on that."
            n "You aren't too shabby yourself,{w=0.1} you know!"
            n "But anyway{w=0.1} -{w=0.1} I'll keep it up,{w=0.1} just for you.{w=0.2} Ehehe."

        else:
            n "Ehehe.{w=0.2} I'm glad you're still having fun listening to me,{w=0.1} [player]."
            n "Thanks!{w=0.2} I'll keep it up!"

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Huh?{w=0.2} You do?"
            n "...{w=0.3}To tell you the truth,{w=0.1} [player]?"
            n "I'm honestly...{w=0.3} really glad to hear that."
            n "It's probably dumb,{w=0.1} but I always worry a little about how much fun you're having here."
            n "I don't want you to get all bored..."
            n "So...{w=0.3} thanks for telling me that,{w=0.1} [player].{w=0.2} Truly."
            n "It means a lot."
            $ relationship("affinity+")

        else:
            n "O-{w=0.1}Oh?{w=0.2} Aha!{w=0.2} Well,{w=0.1} I'm glad to hear it!"
            n "You know what that means,{w=0.1} right?"
            n "It means you have great taste,{w=0.1} [player].{w=0.2} Ahaha!"
            $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_HILARIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="You're an inspiration to me!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_INSPIRATIONAL:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Ehehe. Thanks again for that, [player]."
            n "I hope you know you're just as inspiring to me!"

        else:
            n "Ehehe.{w=0.2} What can I say?{w=0.2} I'm a pro,{w=0.1} after all!"
            n "But thanks,{w=0.1} [player]!"
            n "I'm glad you still find inspiration in yours truly!"

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "H-{w=0.1}huh?{w=0.2} I'm inspirational to you?"
            n "Ahaha...{w=0.3} well...{w=0.3} of course I am!"
            n "..."
            n "Though I'm glad to hear it,{w=0.1} all the same."
            $ relationship("affinity+")

        else:
            n "H-{w=0.1}huh?{w=0.2} I'm an inspiration to you?"
            n "Well...{w=0.3} o-{w=0.1}of course you'd think that!"
            n "I mean,{w=0.1} role models don't come much better than me,{w=0.1} after all."
            n "Why,{w=0.1} I'm practically an idol,{w=0.1} right?{w=0.2} Ahaha!"
            n "..."
            n "...Right?"
            $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_INSPIRATIONAL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of style!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_STYLE:
        if jn_globals.current_outfit:
            # Non-uniform dialogue
            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "Ehehe.{w=0.2} Still awestruck by my sense of fashion,{w=0.1} [player]?"
                n "You can't deny I'm a snappy dresser!"

                if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                    n "I don't just dress for me though,{w=0.1} [chosen_tease]~"
                    n "Ahaha!"

            else:
                n "Oh?{w=0.2} Someone could stand to take a few points,{w=0.1} huh?"
                n "Ehehe!"
                n "Relax,{w=0.1} relax!{w=0.2} I'm kidding,{w=0.1} [player].{w=0.2} Don't worry."
                n "But thanks again!"

        else:
            # Uniform dialogue
            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "I mean...{w=0.3} thanks again,{w=0.1} [player]..."
                n "But it isn't like I picked out these clothes myself,{w=0.1} you know!"
                n "A confidence boost is always welcome though."

            else:
                n "Ah...{w=0.3} well...{w=0.3} thanks again,{w=0.1} I think?"
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n "But you could at least save the compliments for my own clothes,{w=0.1} [chosen_tease]..."
                n "I appreciate the sentiment though...{w=0.3} I guess..."

    else:

        if jn_globals.current_outfit:
            # Uniform dialogue
            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "H-{w=0.1}huh?{w=0.2} You like my sense of style?"
                n "I mean,{w=0.1} it's not like I can do much styling in this sort of getup..."
                n "But thanks,{w=0.1} [player]."

            else:
                n "W-{w=0.1}what?{w=0.2} My sense of style?"
                n "But [player]!{w=0.2} It isn't like I came up with this look myself!"
                n "..."
                n "Unless..."
                n "A-{w=0.1}are you saying I look good in {i}uniform{/i}?"
                n "..."
                n "A-{w=0.1}ah!{w=0.2} Gross!{w=0.2} I don't like where this is going at all!"
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n "Jeez,{w=0.1} [chosen_tease]..."

        else:
            # Non-uniform dialogue
            if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                n "Ehehe.{w=0.2} I'm just happy you like this outfit,{w=0.1} [player]!"
                n "But then...{w=0.3} should I really be surprised?"
                n "I-{w=0.1}I'm the one wearing it,{w=0.1} a-{w=0.1}after all!"

            else:
                n "H-{w=0.1}ha!{w=0.2} I'm glad you agree!"
                n "It's only natural though,{w=0.1} right?{w=0.2} I like to pride myself on my sense of style!"
                n "Good job for noticing,{w=0.1} [player]."
                n "Ehehe!"

    $ last_compliment_type = jn_compliments.TYPE_STYLE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how thoughtful you are!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_aff.HAPPY, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    if jn_compliments.last_compliment_type == jn_compliments.TYPE_THOUGHTFUL:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Nnnnn-!{w=0.2} what did I tell you,{w=0.1} [player]?"
            n "I'm just...{w=0.3} giving as good as I get,{w=0.1} alright?"
            n "Jeez...{w=0.3} are you trying to put me on the spot or what?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES).capitalize()
            n "[chosen_tease]..."
            n "But...{w=0.3} I'm just really glad you appreciate it,{w=0.1} [player]."

            if jn_affinity.get_affinity_state() >= jn_affinity.LOVE:
                n "You're totally worth the effort."

        else:
            n "Uuuuu...{w=0.3} jeez,{w=0.1} [player]..."
            n "I already said it was nothing!{w=0.2} Are you trying to put me on the spot?"
            n "It's fine,{w=0.1} so...{w=0.3} don't worry about it,{w=0.1} alright?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES).capitalize()
            n "[chosen_tease]..."

    else:
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Honestly,{w=0.1} [player]?{w=0.2} Don't worry about it,{w=0.1} 'kay?"
            n "You've done so much for me already..."
            n "So...{w=0.3} I'm just returning the favour,{w=0.1} that's all."
            n "Ehehe..."

        else:
            n "Ah,{w=0.1} jeez,{w=0.1} [player]..."
            n "It's nothing,{w=0.1} honestly!"
            n "I-{w=0.1}I'm just trying to be friendly,{w=0.1} you know?"
            n "Yeah!{w=0.2} Totally no special treatment going on here.{w=0.2} Nope!"

        $ relationship("affinity+")

    $ last_compliment_type = jn_compliments.TYPE_THOUGHTFUL
    return
