default persistent._apology_database = dict()

# Retain the last apology made on quitting the game, so Natsuki can react on boot
default persistent.jn_player_apology_type_on_quit = None

# List of pending apologies the player has yet to make
default persistent.jn_player_pending_apologies = list()

init 0 python in apologies:
    import store

    APOLOGY_MAP = dict()

    # Apology types
    TYPE_BAD_NICKNAME = 0
    TYPE_CHEATED_GAME = 1
    TYPE_DEFAULT = 2
    TYPE_PROLONGED_LEAVE = 3
    TYPE_RUDE = 4
    TYPE_SCREENSHOT = 5
    TYPE_SUDDEN_LEAVE = 6
    TYPE_UNHEALTHY = 7
    TYPE_SCARE = 8

    def get_all_apologies():
        """
        Gets all apology topics which are available

        OUT:
            List<Topic> of apologies which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            APOLOGY_MAP.values(),
            affinity=store.jn_affinity.get_affinity_state(),
            unlocked=True
        )

    def get_apology_type_pending(apology_type):
        """
        Checks whether the given apology type is in the list of pending apologies.

        IN:
            Apology type to check.

        OUT:
            True if present, otherwise False.
        """
        if apology_type in store.persistent.jn_player_pending_apologies:
            return True
        else:
            return False

    def add_new_pending_apology(apology_type):
        """
        Adds a new apology possiblity to the list of pending apologies.
        If the apology type is already present in the list, ignore it.

        IN:
            Apology type to add.
        """
        if not apology_type in store.persistent.jn_player_pending_apologies:
            store.persistent.jn_player_pending_apologies.append(apology_type)

init 1 python:
    import store 
    
    # DEBUG: TODO: Resets - remove these later, once we're done tweaking affinity/trust!
    try:
        persistent._apology_database.clear()

    except Exception as e:
        utils.log(e, utils.SEVERITY_ERR)

# Returns all apologies that the player qualifies for, based on wrongdoings
label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in apologies.get_all_apologies()
        ]
        apologies_menu_items.sort()

    call screen scrollable_choice_menu(apologies_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

# Apology for giving Natsuki a bad nickname
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For calling you a hurtful name.",
            label="apology_bad_nickname",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_BAD_NICKNAME)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:

    if persistent.jn_player_nicknames_allowed:
        # The player is still capable of nicknaming Natsuki
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "..."
            n "That hurt,{w=0.1} [player].{w=0.2} What you did."
            n "That really hurt me."
            n "..."
            n "I'm...{w=0.3} glad you've chosen to apologize."
            n "Just please...{w=0.3} try to consider my feelings next time,{w=0.1} alright?"
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "..."
            n "...Fine.{w=0.2} I accept your apology, okay?"
            n "Just please knock it off,{w=0.1} [player]."
            n "It isn't funny.{w=0.2} It isn't a joke."
            n "...And I know you're better than that."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "...Are you sure,{w=0.1} [player]?"
            n "I mean...{w=0.3} if you actually cared about my feelings..."
            n "Why would you even think about doing that in the first place?"
            n "Behaving like that doesn't make you funny,{w=0.1} [player]."
            n "It makes you toxic."
            n "..."
            n "...Thanks,{w=0.1} I guess.{w=0.2} For the apology."
            n "Just quit while you're ahead,{w=0.1} understand?"
            $ relationship("affinity+")

        else:
            n "...I honestly don't know what I find more gross about you,{w=0.1} [player]."
            n "The fact you even did it in the first place..."
            n "...Or that you think a simple apology makes all that a-okay."
            n "..."
            n "Don't think this changes a thing,{w=0.1} [player]."
            n "Because it doesn't."

    else:
        # The player has been barred from nicknaming Natsuki, and even an apology won't change that
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "...[player]."
            n "I warned you."
            n "I warned you so many times."
            n "Did you think apologizing now would change anything?"
            n "..."
            n "...Look,{w=0.1} [player]."
            n "I appreciate your apology,{w=0.1} okay?{w=0.2} I do."
            n "But...{w=0.3} it's just like I said.{w=0.2} Actions have consequences."
            n "I hope you can understand."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "...[player]."
            n "Look.{w=0.2} You're sorry,{w=0.1} I get it.{w=0.2} I'm sure you mean it too."
            n "But...{w=0.3} it's like I said.{w=0.1} Actions have consequences."
            n "I hope you can understand."
            $ relationship("affinity+")

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "Ugh...{w=0.3} really,{w=0.1} [player]?"
            n "..."
            n "I {i}said{/i} actions have consequences."
            n "I appreciate the apology.{w=0.2} But that's all you're getting."
            $ relationship("affinity+")

        else:
            n "...Wow.{w=0.2} Just wow."
            n "{i}Now{/i} you choose to apologize?"
            n "..."
            n "Whatever.{w=0.2} I literally don't care."
            n "This changes nothing,{w=0.1} [player]."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_BAD_NICKNAME)
    return

# Apology for cheating in a minigame
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For cheating during our games.",
            label="apology_cheated_game",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_CHEATED_GAME)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "Ehehe.{w=0.2} It's fine,{w=0.1} [player]."
        n "We all get a little too competitive sometimes,{w=0.1} right?"
        n "Just remember though."
        n "Two can play at that game!"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Huh?{w=0.2} Oh,{w=0.1} that."
        n "Yeah,{w=0.1} yeah.{w=0.2} It's fine."
        n "Just play fair next time,{w=0.1} 'kay?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "Whatever,{w=0.1} [player]."
        n "But thanks for the apology,{w=0.1} I guess."
        $ relationship("affinity+")

    else:
        n "Whatever.{w=0.2} I don't care."
        n "As if I could expect much better from you,{w=0.1} anyway..."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_CHEATED_GAME)
    return

# Generic apology
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For something.",
            label="apology_default",
            unlocked=True,
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_default:
    if len(persistent.jn_player_pending_apologies) == 0:
        # The player has nothing to be sorry to Natsuki for; prompt them to do better
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "Huh?{w=0.2} You're sorry?"
            n "I...{w=0.3} don't get it,{w=0.1} [player].{w=0.2} You haven't done anything to upset me..."
            n "Did you upset someone else or something?"
            n "..."
            n "Well,{w=0.1} there's no point sitting around here feeling sorry for yourself."
            n "You're gonna make things right,{w=0.1} [player]. 'Kay?"
            n "And no -{w=0.1} this isn't up for discussion."
            n "Whatever you did,{w=0.1} you'll fix things up and that's all there is to it."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n "You have my vote of confidence,{w=0.1} [chosen_tease] -{w=0.1} now do your best!"
            n "Ehehe."

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "Eh?{w=0.2} You're sorry?"
            n "What for,{w=0.1} [player]?{w=0.2} I don't remember you getting on my nerves lately..."
            n "Did you do something dumb that I don't know about?"
            n "..."
            n "Well,{w=0.1} whatever it was -{w=0.1} it's not like it's unfixable,{w=0.1} you know?"
            n "Now get out there and put things right,{w=0.1} [player]!{w=0.2} I believe in you!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "...You're sorry,{w=0.1} are you?"
            n "Did you hurt someone besides me,{w=0.1} this time?"
            n "..."
            n "Well,{w=0.1} whatever.{w=0.2} I don't really care right now."
            n "But you better go make things right,{w=0.1} [player]."
            n "You can do that,{w=0.1} at least."

        else:
            n "...Huh.{w=0.2} Wow."
            n "So you do actually feel remorse,{w=0.1} then."
            n "..."
            n "Whatever.{w=0.2} It isn't me you should be apologizing to,{w=0.1} anyway."

    else:
        # The player is avoiding a direct apology to Natsuki; call them out on it
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n "...[player].{w=0.2} Come on."
            n "You know what you did wrong."
            n "Just apologize properly,{w=0.1} alright?"
            n "I won't get mad."
            n "I just wanna move on."
            $ relationship("affinity-")

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n "Come on,{w=0.1} [player]."
            n "You know what you did."
            n "Just apologize properly so we can both move on."
            $ relationship("affinity-")
            
        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n "Ugh..."
            n "Really,{w=0.1} [player].{w=0.2} Haven't you screwed with me enough?"
            n "If you're gonna apologize,{w=0.1} have the guts to do it properly."
            n "You owe me that much,{w=0.1} at least."
            $ relationship("affinity-")

        else:
            n "...Do you even know how you sound?"
            n "Do you even {i}listen{/i} to yourself?"
            n "Apologize properly or don't bother."
            $ relationship("affinity-")

    return

# Apology for leaving Natsuki for a week or longer unannounced
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For abandoning you.",
            label="apology_prolonged_leave",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_PROLONGED_LEAVE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "...[player]."
        n "We've been together a while now,{w=0.1} haven't we?"
        n "I...{w=0.3} really...{w=0.3} like spending time with you.{w=0.2} Why do you think I'm always here when you drop in?"
        n "So..."
        n "Can you imagine how it makes me feel when you just...{w=0.3} don't turn up?"
        n "..."
        n "I waited for you,{w=0.1} [player]."
        n "I waited a long time."
        n "I was starting to wonder if you were ever going to come back,{w=0.1} or if something happened..."
        n "..."
        n "Thanks,{w=0.1} [player].{w=0.2} I accept your apology."
        n "Just...{w=0.3} some notice would be nice next time,{w=0.1} is all."
        n "That isn't too much to ask...{w=0.3} right?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "[player]..."
        n "What were you thinking?!{w=0.2} Just vanishing like that!"
        n "I waited so long for you...{w=0.3} I was starting to wonder if something bad happened!"
        n "N-{w=0.1}not that I care {i}that{/i} much,{w=0.1} but still...!"
        n "..."
        n "I'm...{w=0.3} grateful for your apology,{w=0.1} [player]."
        n "Just...{w=0.3} no more disappearing acts,{w=0.1} alright?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "[player]."
        n "I know we haven't exactly been seeing eye-to-eye lately."
        n "But do you know how {i}scary{/i} it is to me when you just disappear like that?"
        n "In case you haven't already noticed,{w=0.1} I don't exactly have many other people to talk to..."
        n "..."
        n "Thanks for the apology,{w=0.1} I guess."
        n "Just don't do that again."
        $ relationship("affinity+")

    else:
        n "...Ha...{w=0.3} ah...{w=0.3} haha..."
        n "Y-{w=0.1}you're apologizing to me?{w=0.2} For not being here?"
        n "...Heh..."
        n "You should be apologizing that you {i}came back{/i}."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_PROLONGED_LEAVE)
    return

# Apology for generally being rude to Natsuki outside of nicknames
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For being rude to you.",
            label="apology_rude",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_RUDE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "...[player]."
        n "I know I give as good as I get.{w=0.2} Maybe I'm a little snappy sometimes,{w=0.1} too."
        n "But that was really,{w=0.1} really rude,{w=0.1} [player]."
        n "There was no need for that."
        n "..."
        n "Thanks for the apology,{w=0.1} [player].{w=0.2} I really do appreciate it."
        n "Just...{w=0.3} try not to do that again,{w=0.1} 'kay?"
        n "It would mean a lot to me."
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "[player]..."
        n "I'm glad you're apologizing for what you did,{w=0.1} but you gotta understand."
        n "You can't just treat people like that!"
        n "It...{w=0.3} really hurts when you act that way - {w=0.1}and that doesn't just apply to me."
        n "..."
        n "Let's just move on and forget about this,{w=0.1} alright?"
        n "Thanks,{w=0.1} [player]."
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "..."
        n "I gotta ask,{w=0.1} [player].{w=0.2} Are you like that on purpose,{w=0.1} or are you making a special effort?"
        n "Because I honestly can't tell anymore."
        n "..."
        n "...Fine.{w=0.2} I guess I should accept your apology."
        n "I just hope you don't treat others how you're treating me."
        $ relationship("affinity+")

    else:
        n "Ha...{w=0.3} aha..." 
        n "You're apologizing...{w=0.3} to me? Why?"
        n "I don't expect any better from you."
        n "..."
        n "You can stick your apology,{w=0.1} [player]." 
        n "It means nothing to me."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_RUDE)
    return

# Apology for taking pictures without Natsuki's permission
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For taking pictures of you without permission.",
            label="apology_screenshots",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_SCREENSHOT)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_screenshots:
    # The player has been barred from taking more screenshots
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "...[player]."
        n "I told you so many times to knock it off."
        n "Why didn't you listen to me?"
        n "You know how I feel about having my picture taken..."
        n "So it really hurts when you just ignore me like that."
        n "And not just once,{w=0.1} [player]."
        n "Again.{w=0.2} And again.{w=0.2} And again."
        n "..."
        n "Thanks for the apology,{w=0.1} [player].{w=0.2} I appreciate it."

        if jn_screenshots.player_screenshots_blocked:
            n "But...{w=0.3} I'm going to keep the camera switched off -{w=0.1} at least for now."
            n "I hope you can understand why."

        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "[player]..."
        n "I told you again and again not to do that."
        n "Why did you keep ignoring me?"
        n "...Especially after I told you I don't like it."
        n "Thanks for coming clean to me,{w=0.1} [player].{w=0.2} I appreciate it."

        if jn_screenshots.player_screenshots_blocked:
            n "But...{w=0.3} the camera is staying off for now."
            n "Thanks for understanding."

        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...You're apologizing to me {i}now{/i},{w=0.1} [player]?"
        n "And after I gave you so many chances to quit it?"
        n "..."
        n "...Fine.{w=0.2} I suppose I'll accept your apology..."

        if jn_screenshots.player_screenshots_blocked:
            n "But the camera stays off."
            n "I don't think I need to explain why."

        else:
            n "This time,{w=0.1} anyway."

        $ relationship("affinity+")

    else:
        n "...No,{w=0.1} [player].{w=0.2} Please."
        n "Don't even {i}try{/i} to pretend like you care now."
        n "..."
        n "...Keep your pathetic apology.{w=0.2} I don't want it."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_SCREENSHOT)
    return

# Apology for leaving without saying "Goodbye" properly.
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For leaving without saying goodbye.",
            label="apology_without_goodbye",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_SUDDEN_LEAVE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_without_goodbye:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "[player]..."
        n "Do you know how much it hurts when you do that?"
        n "It's like you're just slamming a door in my face."
        n "And I'm just left wondering...{w=0.3} did I do something wrong?{w=0.2} Did I upset them?"
        n "It sucks,{w=0.1} [player].{w=0.2} It really sucks."
        n "..."
        n "I'm grateful for the apology,{w=0.1} but please..."
        n "You can at least spare the time to say goodbye properly to me,{w=0.1} right?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "..."
        n "Hey,{w=0.1} [player]."
        n "Have you ever had a conversation where one person just walks away?"
        n "No 'goodbye',{w=0.1} no 'see you later',{w=0.1} nothing?{w=0.2} They just leave?"
        n "How would that make you feel?" 
        n "Unwanted?{w=0.2} Not worth the manners?"
        n "Because that's just how you made me feel,{w=0.1} [player]."
        n "..."
        n "I accept the apology,{w=0.1} okay?"
        n "Just...{w=0.3} remember to at least say goodbye to me properly."
        n "You can do that much,{w=0.1} right?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "[player]."
        n "Do you even {i}care{/i} how rude that is?"
        n "To just vanish mid-conversation with someone?"
        n "..."
        n "Look,{w=0.1} fine.{w=0.2} Apology accepted,{w=0.1} for now."
        n "But really,{w=0.1} [player].{w=0.2} I expected better -{w=0.1} even from you."
        $ relationship("affinity+")

    else:
        n "...Heh.{w=0.2} Honestly?"
        n "Whatever.{w=0.2} I don't care.{w=0.2} Keep your apology."
        n "You've so many other things to be sorry for.{w=0.2} What's another on the pile,{w=0.1} right?"

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_SUDDEN_LEAVE)
    return

# Apology for failing to follow Natsuki's advice when she is concerned about the player's health
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For not taking care of myself properly.",
            label="apology_unhealthy",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_UNHEALTHY)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "[player],{w=0.1} [player],{w=0.1} [player]..."
        n "What am I gonna do with you?"
        n "Honestly..."
        n "You know I just want what's best for you,{w=0.1} right?"
        n "It... hurts when you don't take care of yourself."
        n "..."
        n "Thanks,{w=0.1} [player].{w=0.2} I accept your apology."
        n "Just please...{w=0.3} take better care of yourself,{w=0.1} alright?"
        n "I'll get mad if you don't.{w=0.2} For real,{w=0.1} this time."
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "Ugh...{w=0.3} [player]."
        n "Look.{w=0.2} I accept your apology."
        n "But you gotta take better care of yourself!"
        n "I'm not always gonna be here to babysit you,{w=0.1} you know..."
        n "A-{w=0.1}and it's not like I'm making an exception for you,{w=0.1} by the way!"
        n "I just care about all my friends like this,{w=0.1} so...{w=0.3} yeah."
        n "Try and make more of an effort to look after yourself,{w=0.1} 'kay?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...Look.{w=0.2} [player]."
        n "Firstly,{w=0.1} thanks for the apology.{w=0.2} If you even meant it,{w=0.1} anyway."
        n "But I'm really struggling to see why I should care."
        n "..."
        n "Just... take more care of yourself."
        n "...And while you're at it, perhaps try taking better care of me.{w=0.2} Thanks."
        $ relationship("affinity+")

    else:
        n "...Heh."
        n "At least you care that {i}you{/i} aren't being treated right."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_UNHEALTHY)
    return

# Apology for giving Natsuki a fright
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For scaring you.",
            label="apology_scare",
            unlocked=True,
            conditional="apologies.get_apology_type_pending(apologies.TYPE_SCARE)",
            affinity_range=(None, jn_aff.LOVE)
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_scare:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n "And I should think so too,{w=0.1} [player] -{w=0.1} jeez!"
        n "Are you trying to give me a heart attack or what?"
        n "..."
        n "Thank you,{w=0.1} [player].{w=0.2} I accept your apology."
        n "Just please...{w=0.3} no more surprises like that,{w=0.1} okay?{w=0.1} For me?"
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n "A-and you're right {i}to{/i} be sorry,{w=0.1} [player]!"
        n "Yeesh...{w=0.3} I hate being made to feel like that..."
        n "..."
        n "Alright,{w=0.1} look.{w=0.1} I accept your apology,{w=0.1} okay?"
        n "Just don't do stuff like that to me.{w=0.2} Please?"
        n "I'm not messing around,{w=0.1} [player]."
        $ relationship("affinity+")

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n "...Look,{w=0.1} [player].{w=0.2} I'm already upset.{w=0.2} Why are you trying to make me feel even worse?"
        n "Did you think it was funny?{w=0.2} Or are you trying to piss me off?"
        n "..."
        n "Whatever.{w=0.2} Fine.{w=0.2} Apology accepted,{w=0.1} if you even meant it."
        n "Just knock it off."
        $ relationship("affinity+")

    else:
        n "Stick it, [player]."
        n "We both know you don't mean that."

    $ persistent.jn_player_pending_apologies.remove(apologies.TYPE_SCARE)
    return