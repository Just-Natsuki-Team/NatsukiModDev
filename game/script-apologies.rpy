default persistent._apology_database = dict()

# Retain the last apology made on quitting the game, so Natsuki can react on boot
default persistent._jn_player_apology_type_on_quit = None

# List of pending apologies the player has yet to make
default persistent._jn_player_pending_apologies = list()

init 0 python in jn_apologies:
    from Enum import Enum
    import store

    APOLOGY_MAP = dict()

    class ApologyTypes(Enum):
        """
        Identifiers for different nickname types.
        """
        bad_nickname = 1
        cheated_game = 2
        generic = 3
        prolonged_leave = 4
        rude = 5
        sudden_leave = 6
        unhealthy = 7
        scare = 8
        bad_player_name = 9

        def __str__(self):
            return self.name

        def __int__(self):
            return self.value

    def get_all_apologies():
        """
        Gets all apology topics for the currently pending apologies, as well as the generic

        OUT:
            List<Topic> for all current pending apologies
        """
        return_apologies = [
            store.get_topic("apology_generic")
        ]
        for apology_type in store.persistent._jn_player_pending_apologies:
            return_apologies.append(store.get_topic(str("apology_{0}".format(ApologyTypes(apology_type)))))

        return return_apologies

# Returns all apologies that the player qualifies for, based on wrongdoings
label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in jn_apologies.get_all_apologies()
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
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:
    if persistent._jn_nicknames_natsuki_allowed:
        # The player is still capable of nicknaming Natsuki
        if Natsuki.isEnamored(higher=True):
            n 1fcssl "...[player].{w=1}{nw}"
            extend 2fsqsl " You {i}really{/i} have to ask yourself something here."
            n 2fcsaj "Hear me out."
            n 2fcsbo "..."
            n 2nllpu "I'm...{w=0.75}{nw}"
            extend 4nllsl " willing...{w=1}{nw}"
            extend 4nnmca " to let you call me something else."
            n 1flrbo "Something {i}other{/i} than the name I've been called all my life."
            n 3tnmpu "You {i}do{/i} know what that's all about,{w=0.2} right?{w=0.75}{nw}"
            extend 3tsqsl " What it means?"
            n 1ncsaj "It's a show of trust."
            n 2fsqem "...So what do you {i}seriously{/i} think it shows when you use that trust to {i}insult{/i} me?"
            n 2fcspu "..."
            n 2nllsl "I'm...{w=0.75}{nw}" 
            extend 1kslbo " glad you've chosen to apologize."
            n 1kcssl "Just please...{w=0.75}{nw}" 
            extend 4ksqsll " try to consider my feelings next time."
            n 2ksrajl "It's really {i}not{/i} much to ask.{w=0.75}{nw}"
            extend 2tsqbol " Right?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 2fcsbo "..."
            n 2ncspuesi "..."
            n 2nslsl "...Fine.{w=0.75}{nw}"
            extend 2fcsaj " I accept your apology,{w=0.2} okay?"
            n 1fsqsl "Just knock it off now,{w=0.2} [player]."
            n 4fllpu "It isn't {i}funny{/i}.{w=0.5}{nw}" 
            extend 4fnmem " It isn't a {i}joke{/i}."
            n 2fcsca "...And I know you're better than {i}that{/i}."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsem "...Heh.{w=0.75}{nw}"
            extend 4fsqwr " Oh,{w=0.2} {i}really{/i}?"
            n 2fllem "...You sure,{w=0.2} [player]?"
            n 2fcsem "Because I mean...{w=0.75}{nw}" 
            extend 2fsqsl " if you {i}actually{/i} cared about my feelings..."
            n 4fnman "Why would you even {i}think{/i} about doing that in the first place?"
            n 1fcsan "You aren't funny,{w=0.2} [player]."
            extend 4flrem " You aren't making anyone {i}laugh{/i}."
            n 2fsqfu "...You're just being an ass."
            n 2fcsbo "..."
            n 2fcsem "...Whatever.{w=0.75}{nw}"
            extend 1fslbo " I'll take your apology."
            n 1fsqsl "But I'm not taking much more crap from you."
            n 2fnmsl "Got it?"

            $ Natsuki.calculatedAffinityGain()

        else:
            n 2fcsan "...I honestly don't know what I find more {i}gross{/i} about you,{w=0.2} [player]."
            n 2fcsaj "The fact you even did it in the first place..."
            n 4fsqful "...Or that you think a simple apology makes all that a-{w=0.2}okay."
            n 1fcssrl "..."
            n 1fcsanltsa "Don't think this changes anything,{w=0.2} {i}[player]{/i}."
            n 4fsqsrltsb "Because it {i}doesn't.{/i}"

    else:
        # The player has been barred from nicknaming Natsuki, and even an apology won't change that
        if Natsuki.isEnamored(higher=True):
            n 1ncspu "...[player]."
            n 1fcssl "I warned you.{w=1}{nw}"
            extend 4fnmun " I warned you {i}{w=0.3}so{w=0.3} many{w=0.3} times{/i}."
            n 1fsqem "Did you seriously think apologizing {i}now{/i} would change anything?"
            n 2fcsslesi "..."
            n 2fllsl "...Look."
            n 2nllbo "I appreciate the apology,{w=0.5}{nw}" 
            extend 1fnmbo " okay?"
            n 2kcspu "But I am {i}not{/i} gonna have my trust broken any more with this.{w=1}{nw}"
            extend 4kslsl " Not again."
            n 1fcsaj "...So you better get used to 'Natsuki',{w=0.2} [player]."
            n 2fsrsl "'Cause {i}clearly{/i} you struggle with anything else.'"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssl "...[player]."
            n 2flrsl "Look.{w=1}{nw}" 
            extend 2fnmem " You're sorry.{w=0.75}{nw}" 
            extend 1fcsem " I get it."
            n 4fsqsr "But I am {i}done{/i} with you making a fool out of me with this."
            extend 4fsqem " Capiche?"
            n 1fsqca "...It's always going to be {i}just{/i} 'Natsuki' to you."
            n 2fslsl "Thanks for understanding."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsem "Ugh..."
            n 4fslem "Really,{w=0.75}{nw}"
            extend 4fsqfr " [player]?"
            n 2fcsfr "..."
            n 1fcsaj "I {i}said{/i} actions have consequences.{w=1}{nw}"
            extend 2fsqan " So I guess now you're just going to have to learn the hard way."
            n 2fcssl "Yeah,{w=0.2} I'll take your apology." 
            n 2fsqsr "But that's {i}all{/i} you're getting."

            $ Natsuki.calculatedAffinityGain()

        else:
            n 1fslan "...Wow.{w=0.75}{nw}" 
            extend 1fcsanl " Just wow."
            n 4fnmfultsc "{i}Now{/i} you choose to apologize?"
            n 2fcsunltsa "..."
            n 2fcsemltsa "Whatever.{w=1}{nw}" 
            extend 2fcsfultsa " I literally don't care."
            n 4fsqupltsb "You can stick your {w=0.2}half-{w=0.2}assed{w=0.2} apology,{w=0.2} [player]."
            n 1fcsfultsa "This changes {i}nothing{/i}."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_nickname)
    return

# Apology for cheating in a minigame
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For cheating during our games.",
            label="apology_cheated_game",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if Natsuki.isEnamored(higher=True):
        n 1tnmpueqm "Eh?{w=0.75}{nw}"
        extend 4nlrss " Oh,{w=0.2} yeah."
        n 1nlrbo "It's fine."
        n 2nsrpu "...It just gets annoying sometimes.{w=0.75}{nw}"
        extend 4tnmbo " You know?"
        n 4fllsl "When you're {i}trying{/i} to have fun and someone else keeps going way overboard just to win.{w=0.75}{nw}"
        extend 2nllca " It just spoils it for me.{w=0.75}{nw}"
        extend 2kslcal " I can't play like that."
        n 4nllbo "But...{w=0.75}{nw}"
        extend 1knmss " I appreciate the apology.{w=0.75}{nw}"
        extend 4fsqsm " Just remember though,{w=0.2} [player]..."
        n 3fcsbgl "Two can play at that game!"

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isNormal(higher=True):
        n 2tsqpueqm "Huh?{w=0.75}{nw}" 
        extend 2nlrbo " Oh,{w=0.2} that."
        n 1ncsaj "Yeah,{w=0.2} yeah.{w=0.75}{nw}" 
        extend 1nslca " It's fine."
        n 2tnmca "Just play fair next time,{w=0.2} alright?"
        n 2nslsssbl "It's really not hard...{w=1}{nw}"
        extend 2tnmbosbl " is it?"

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isDistressed(higher=True):
        n 2fcssresi "..."
        n 2fslsr "Fine.{w=0.75}{nw}"
        extend 2fcsem " Yeah.{w=0.75}{nw}"
        extend 1fsqfr " Whatever,{w=0.2} [player]."
        n 2nsrsl "But thanks for the apology,{w=0.2} I guess."

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    else:
        n 4fcsanl "Oh,{w=0.5}{nw}" 
        extend 2fcsupl " whatever.{w=0.5}{nw}" 
        extend 1fsrfultsb " I really couldn't give a {i}crap{/i} anymore."
        n 4fsqgtltsb "As if I could expect much better from {i}you{/i},{w=0.2} anyway."

        $ persistent.jn_snap_player_is_cheater = False

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.cheated_game)
    return

# Generic apology
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For something.",
            label="apology_generic",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_generic:
    if len(persistent._jn_player_pending_apologies) == 0:
        # The player has nothing to be sorry to Natsuki for; prompt them to do better
        if Natsuki.isEnamored(higher=True):
            n 2tnmpu "Huh?{w=0.75}{nw}" 
            extend 2tnmbo " You're sorry?"
            n 1nlrss "I...{w=1}{nw}" 
            extend 4tnmsl " don't get it,{w=0.2} [player].{w=0.75}{nw}" 
            extend 2tslca " You haven't done anything to upset {i}me{/i},{w=0.2} at least..."
            n 2tnmsl "Did you upset someone else or something?"
            n 1ncssl "..."
            n 4fchbg "Well,{w=0.5}{nw}" 
            extend 3fcsbg " there's no point sitting around here feeling sorry for yourself!"
            n 3fcssm "You're gonna make things right,{w=0.2} [player].{w=0.75}{nw}" 
            extend 3fcsbg " 'Kay?"
            n 4nllfl "And no -{w=0.75}{nw}" 
            extend 2fcscaesm " this isn't up for discussion."
            n 1fcsss "Whatever you did,{w=0.2} you'll fix things up and that's just all there is to it."
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            n 3fchbg "You have my vote of confidence,{w=0.2} [chosen_descriptor] -{w=0.3}{nw}"
            extend 3fwlbg " now do your best!{w=0.75}{nw}"
            extend 3fchgn " Ehehe."

        elif Natsuki.isNormal(higher=True):
            n 2tnmpu "Eh?{w=0.5}{nw}" 
            extend 2tnmbo " You're sorry?"
            n 1tllaj "What for,{w=0.2} [player]?{w=0.75}{nw}" 
            extend 4tslaj " I don't remember you getting on my nerves lately..."
            n 2fsqcal "...Did you go and do something dumb that I don't know about?"
            n 1ncsca "..."
            n 4unmaj "Well,{w=0.75}{nw}" 
            extend 2ulraj " whatever it was -{w=0.5}{nw}" 
            extend 2tlrss " it's not like it's unfixable,{w=0.75}{nw}" 
            extend 4fnmsm " you know?"
            n 3fcsbg "Now get out there and put things right,{w=0.2} [player]!"
            n 3fchsmeme "You got this!"

        elif Natsuki.isDistressed(higher=True):
            n 1fcsfl "Heh.{w=0.75}{nw}"
            extend 1fsqbo " You're sorry,{w=0.2} are you?"
            n 4fsran "Did you hurt someone {i}besides{/i} me,{w=0.5}{nw}" 
            extend 4fsqan " this time?"
            n 2fcssl "..."
            n 2fsqsl "...Whatever.{w=0.5}{nw}" 
            extend 2fslfr " I really don't care right now."
            n 2fsqem "But you {i}better{/i} go make things right,{w=0.2} [player]."
            n 2fllsl "You can do that,{w=0.5}{nw}" 
            extend 2fslsl " at least."

        else:
            n 1fcsfl "...Huh.{w=0.75}{nw}" 
            extend 1fcsan " Wow."
            n 4fsqgtl "So you {i}do{/i} actually feel remorse,{w=0.2} then."
            n 2fcsunl "..."
            n 2fsqfultsb "Whatever.{w=0.75}{nw}" 
            extend 2fsrgtltsb " It isn't {i}me{/i} you should be apologizing to,{w=0.2} anyway."

    else:
        # The player is avoiding a direct apology to Natsuki; call them out on it
        if Natsuki.isEnamored(higher=True):
            n 1kllsl "...[player].{w=0.75}{nw}" 
            extend 4knmsl " Come on."
            n 2ksqsr "You {i}know{/i} what you did wrong.{w=0.75}{nw}"
            extend 2ksqbo " So just apologize properly already."
            n 4kllbo "I won't get mad."
            n 1kslbol "I just wanna move on."

            $ Natsuki.percentageAffinityLoss(2.5)

        elif Natsuki.isNormal(higher=True):
            n 1fnmsf "Come on,{w=0.2} [player].{w=1}{nw}"
            extend 2fnmaj " You know what you did."
            n 2nslsl "Just apologize properly so we can both move on."

            $ Natsuki.percentageAffinityLoss(2)

        elif Natsuki.isDistressed(higher=True):
            n 2fupem "Ugh..."
            n 2fnman "Really,{w=0.2} [player].{w=0.75}{nw}" 
            extend 4fsqan " Haven't you screwed with me enough?"
            n 1fcsgs "If you're gonna apologize,{w=0.75}{nw}" 
            extend 2fcsan " have the guts to do it {i}properly{/i}."
            n 2fsqsf "You owe me that much,{w=0.2} at least."

            $ Natsuki.percentageAffinityLoss(1.5)

        else:
            n 4fsqfu "...Do you even know how you sound?"
            n 4fnmgtltsc "Do you even {i}listen{/i} to yourself?"
            n 2fcsfultsa "Apologize properly or{nw}" 
            extend 2fsqfultsb " {i}get out of my face{/i}."

            $ Natsuki.percentageAffinityLoss(1)

    return

# Apology for leaving Natsuki for a week or longer unannounced
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For abandoning you.",
            label="apology_prolonged_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if Natsuki.isEnamored(higher=True):
        if Natsuki.isLove(higher=True):
            n 1ncssl "...[player]."
            n 1kllfl "We've...{w=0.75}{nw}" 
            extend 2knmbo " been together a while now,{w=0.2} haven't we?"
            n 2ksrbol "A-{w=0.2}and you know I like spending time with you.{w=1}{nw}" 
            extend 4knmbol " Why do you {i}think{/i} I'm always here whenever you show up?"

        else:
            n 1ncssl "...[player]."
            n 1kllfl "We've...{w=0.75}{nw}" 
            extend 2knmbo " been here together a while now,{w=0.2} haven't we?"
            n 2fcsun "I...{w=0.75}{nw}" 
            extend 1fcsfll " really...{w=0.75}{nw}" 
            extend 4ksrbol " like spending time with you.{w=1}{nw}" 
            extend 4knmbol " Why do you {i}think{/i} I'm always here whenever you show up?"
            
        n 4klrfll "So can you imagine how it feels when you just...{w=1}{nw}" 
        extend 1klrsll " don't turn up?"
        n 1fcsunl "..."
        n 1fcssll "I waited for you,{w=0.2} [player]."
        n 4kslbol "I waited a really long time."
        n 4kllemlsbl "I was starting to wonder if you were ever going to come back...{w=0.75}{nw}" 
        extend 4kllunlsbl " o-{w=0.2}or if something happened."
        n 1kcspulesi "..."
        n 2nsqbol "...Thanks,{w=0.2} [player].{w=0.75}{nw}" 
        extend 2ksrbol " For the apology, I mean.{w=1}{nw}"
        extend 2ksrfsl " It's appreciated."
        n 4kcsajl "Just..." 
        n 1kslsrl "..."
        n 2knmsll "Just some notice would be nice,{w=0.2} is all."
        n 2klrsll "That isn't too much to ask..." 
        n 4knmbol "Right?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcsunl "[player]..."
        n 4fnmgsl "What were you even {i}thinking?!{/i}{w=0.75}{nw}" 
        extend 4fcsgsl " Just vanishing like that!"
        n 1fbkwrlsbl "I don't have a crystal ball!{w=0.75}{nw}"
        extend 2flremlsbl " How am {i}I{/i} meant to know if you'd be back?{w=0.75}{nw}"
        extend 2fcswrlsbl " Or if something happened?!"
        n 2fcssll "..."
        n 2nslbo "..."
        n 1ncspu "...Look."
        extend 4fnmbol " I appreciate the apology.{w=0.75}{nw}"
        extend 2flrfll " And I get that you've got stuff to do.{w=0.75}{nw}"
        extend 2fsrbolsbl " It's not like we're not super close or anything like that,{w=0.2} e-{w=0.2}either."
        n 4fnmbol "But can you at least {i}tell{/i} me when you're gonna go,{w=0.2} like I said?"
        n 2fcspol "I-{w=0.2}if I wanted a disappearing act,{w=0.2} I would have asked,{w=0.2} after all."
        n 2ksrpol "..."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fsqfr "...[player]."
        n 2fcsfr "I know we haven't exactly been seeing eye-to-eye lately."
        n 4fnman "But do you even {i}care{/i} how scary it is to me when you just disappear?"
        n 1flrem "In case you haven't already {i}noticed{/i},{w=0.75}{nw}" 
        extend 4fcsem " I don't exactly have many {i}other{/i} people to talk to..."
        n 1fcssr "..."
        n 2fslpu "I guess I should say thanks.{w=1}{nw}"
        extend 2fslbo " For the apology."
        n 2fcsbo "Just...{w=0.75}{nw}" 
        extend 2fcsemsbr " don't do that again."

        $ Natsuki.calculatedAffinityGain()

    else:
        n 1fcsem "...Ha...{w=0.5}{nw}" 
        extend 1fcsssltsa " ah...{w=0.5}{nw}" 
        extend 1fsrflltse " haha..."
        n 4fsqflltse "Y-{w=0.2}you're apologizing to me?{w=0.75}{nw}" 
        extend 4fnmflltsf " For not being here?"
        n 1fcsunltsd "...Heh..."
        n 4fsqgtltse "You should be apologizing that you {i}came back{/i}."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.prolonged_leave)
    return

# Apology for generally being rude to Natsuki outside of nicknames
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For being rude to you.",
            label="apology_rude",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if Natsuki.isEnamored(higher=True):
        n 4fcsca "...[player]."
        n 4nllsl "I know I give as good as I get.{w=0.75}{nw}" 
        extend 1nslsssbr " And maybe I {i}am{/i} little snappy sometimes."
        n 3fcsaj "But that was really,{w=0.75}{nw}" 
        extend 3fcsem " {i}seriously{/i}{w=0.5}{nw}" 
        extend 3fsqem " rude."
        n 3fcsfl "There was no need for that at all."
        n 1ncssl "..."
        n 4nllsl "Thanks for the apology,{w=0.2} [player].{w=0.75}{nw}" 
        extend 2knmsl " I appreciate it."
        n 2fcspu "Just...{w=0.3} try not to do that again."
        extend 2knmpol " Please?"
        n 1klrbol "It would mean a lot -{w=0.5}{nw}"
        extend 4knmbol " and we {i}both{/i} know you're better than that."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcssr "...[player]."
        n 2fcspu "I'm...{w=1}{nw}" 
        extend 2nsrsl " glad you're apologizing for what you did.{w=0.75}{nw}" 
        extend 2fsqaj " But you gotta understand."
        n 4fnmgs "You can't just {i}treat{/i} people like that!"
        n 3knmfl "Do you seriously think people are gonna {i}like{/i} you if you act that way?"
        n 3ncsemesi "Yeesh..."
        n 1ncsbo "..."
        n 2nllaj "I'll spare you the lecture,{w=0.75}{nw}"
        extend 2nnmsl " this time.{w=0.75}{nw}"
        extend 2nsrss " ...And the bar of soap."
        n 2nsrca "I just wanna move on from this."
        n 2nsraj "Thanks,{w=0.2} [player]."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fcsun "..."
        n 2fcsss "Heh.{w=0.75}{nw}"
        extend 2fsqem " Let me ask you something,{w=0.75} {i}[player]{/i}."
        n 4fnmfl "...Are you like that on {i}purpose{/i}?{w=0.75}{nw}" 
        extend 3fsqan " or are you making a special effort to be a jerk lately?"
        n 3fcsem "Because I honestly can't tell."
        n 1fcssl "..."
        n 2fcsaj "...Fine.{w=0.75}{nw}" 
        extend 2fllfr " I guess I should accept your apology.{w=0.75}{nw}"
        extend 2fslfr " For what {i}that's{/i} worth."
        n 2fsqsl "Don't expect others to accept it so readily."

        $ Natsuki.calculatedAffinityGain()

    else:
        n 1fcsss "Ha...{w=0.3} aha..."
        n 4fcsfll "You're apologizing...{w=0.75}{nw}" 
        extend 4fsqupl " to me?{w=1}{nw}" 
        extend 2fnmupltsc " Why?"
        n 2fcsfultsa "I don't expect any better from you {i}anyway{/i}."
        n 2fcsunltsa "..."
        n 2fsqgtltsc "You can {i}stick{/i} your apology,{w=0.2} [player]."
        n 1fsqanltsc "It means {i}nothing{/i} to me."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.rude)
    return

# Apology for leaving without saying "Goodbye" properly.
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For leaving without saying goodbye.",
            label="apology_sudden_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 3ksrsl "[player]..."
        n 3knmsll "Do you {i}know{/i} how much it hurts when you do that?"
        extend 3ksleml " Like..." 
        extend 4ksqeml " seriously?"
        n 1kcsfll "It's like you might as well be slamming a door in my face."
        n 2klrfll "And I'm just sat here like...{w=0.75}{nw}" 
        extend 2klrpulsbl " 'Did I do something?'{w=0.75}{nw}"
        extend 2kllemlsbl " 'Why did they just bail on me?'"
        n 1ksqfllsbl "...Right before I get ripped out of existence."
        n 4kcsfll "It sucks,{w=0.2} [player].{w=0.5} It really sucks.{w=1}{nw}"
        extend 4fsrunl " A-{w=0.2}and it hurts."
        n 4ncspul "..."
        n 2kllsll "I'm grateful for the apology,{w=0.5}{nw}" 
        extend 2kslsll " but please..."
        n 2ksqsll "Just let me know when you're heading off."
        n 2ksqbolsbr "You can at least spare the time to say goodbye properly to me,{w=0.2} right?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 2fllsl "..."
        n 2fnmsl "Hey,{w=0.2} [player]."
        n 2fnmaj "Have you ever had a conversation where one person just walks away?"
        n 2flrfl "No 'Goodbye',{w=0.5}{nw}" 
        extend 2fllfl " no 'See you later',{w=0.5}{nw}" 
        extend 2fnmem " nothing?{w=0.5}{nw}" 
        extend 1ksqem " They just leave?"
        n 4fsqbo "...How would that make you feel?"
        n 4tsqaj "Unwanted?{w=0.75}{nw}" 
        extend 4fsqfl " Not worth the manners?"
        n 2fllsl "Because that's just how you made me feel,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fslsl " And you {i}know{/i} it hurts when you do that,{w=0.2} too."
        n 1fcssl "..."
        n 2flrsl "I accept the apology,{w=0.2} okay?"
        n 2nsrpu "Just...{w=0.75}{nw}" 
        extend 4knmsl " remember to at least say goodbye to me properly."
        n 4tllbo "You can do that much.{w=0.75}{nw}"
        extend 4ksqbosbr " Right?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "[player]."
        n 2fsqan "Do you even {i}care{/i} how rude that is?"
        n 2fsqfu "To just vanish mid-conversation with someone?{w=1}{nw}"
        extend 2fnmem " Even knowing doing that {i}hurts{/i}?"
        n 1fcssr "..."
        n 1fsqsr "Look,{w=0.2} fine.{w=0.75}{nw}" 
        extend 4flrfr " Apology accepted.{w=0.75}{nw}" 
        extend 4fsrsl " For now."
        n 3fsqfl "Don't expect me to accept it again."

        $ Natsuki.calculatedAffinityGain()

    else:
        n 2fcsfl "...Heh.{w=0.75}{nw}" 
        extend 2fsqanl " Honestly?"
        n 2fcsanl "Whatever.{w=0.5} I don't care.{w=0.75}{nw}" 
        extend 2fslupl " Keep your crappy apology."
        n 2fslemltsb "You've so many other things to be sorry for." 
        n 2fsqemltsb "So what's {i}another{/i} on the pile.{w=0.75}{nw}" 
        extend 4fsqgtltsb " Right?"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.sudden_leave)
    return

# Apology for failing to follow Natsuki's advice when she is concerned about the player's health
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For not taking care of myself properly.",
            label="apology_unhealthy",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if Natsuki.isEnamored(higher=True):
        n 3fcsssl "[player],{w=0.5} [player],{w=0.5} [player]..."
        n 3tsqssl "What {i}am{/i} I gonna do with you?{w=0.75}{nw}"
        extend 4nslsslsbr " Honestly..."
        n 4kslbolsbr "..."
        n 4kslpulsbr "But..."
        n 1knmsll "I do really care about you,{w=0.2} you know."
        n 2klrsll "It...{w=1}{nw}" 
        extend 2ksrsll " hurts{w=0.5} when you don't take care of yourself."
        n 2kcssllesi "..."
        n 1ksrbol "Thanks,{w=0.2} [player].{w=0.75}{nw}" 
        extend 2ksqssl " I accept your apology."
        n 2knmbol "Just look after yourself better from now on,{w=0.2} alright?"
        n 2kllbol "I'll get mad if you don't.{w=0.75}{nw}" 
        extend 2fslpol " For real,{w=0.2} this time."
        
        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "L-{w=0.2}love you too,{w=0.2} [chosen_tease]!"

        else:
            n 2fsqsml "Ehehe."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcseml "Ugh...{w=0.75}" 
        extend 1fcspol " [player]."
        n 2fnmbo "Look.{w=0.5}{nw}" 
        extend 2ksrsl " I accept your apology."
        n 4knmaj "But you gotta take better care of yourself!"
        n 3fcspoesm "I'm not always gonna be here to babysit you,{w=0.2} you know..."
        n 2flremlsbl "A-{w=0.2}and no,{w=0.5}{nw}"
        extend 2fsqpolsbl " you aren't an exception."
        n 4fcsfll "I-{w=0.2}I just care about all my friends like this,{w=0.75}{nw}" 
        extend 4fllfll " so...{w=1}{nw}" 
        extend 1nllsll " yeah."
        n 2knmsll "Just make more of an effort to look after yourself."
        n 2fcsfllsbl "Or you'll have me to deal with.{w=0.75}{nw}"
        extend 2fcsbosbl " And trust me." 
        n 2fcscaesi "You really don't want that."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "...Look.{w=0.75}{nw}" 
        extend 2fsqsl " [player]."
        n 2flrsl "Thanks for the apology.{w=0.75}{nw}" 
        extend 2fsrem " I guess.{w=0.75}{nw}" 
        extend 2fsrfl " If you even {i}meant{/i} it,{w=0.2} anyway."
        n 1fcsem "But I'm really struggling to see why I should care."
        n 4fsrem "If you can't even take care of {i}yourself{/i}..."
        n 2fsqan "...Then what does that say about me?"
        n 2fsqsl "..."
        n 2fcsfl "Yeah.{w=1}{nw}"
        extend 2fllsl " Just some food for thought,{w=0.75}{nw}"
        extend 2fsqfr " [player]."

        $ Natsuki.calculatedAffinityGain()

    else:
        n 1fcsun "...Heh."
        n 2fcsanltsa "At least you care that {i}you{/i} aren't being treated right."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.unhealthy)
    return

# Apology for giving Natsuki a fright
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For scaring you.",
            label="apology_scare",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_scare:
    if Natsuki.isEnamored(higher=True):
        n 4fskwrl "A-{w=0.2}and I should think so too,{w=0.2} [player]!" 
        extend 1fcswrl " Jeez!"
        n 2fwmpof "Are you trying to give me a heart attack or what?"
        n 2fcspolesi "..."
        n 2kllbol "...Thanks,{w=0.2} [player].{w=0.75}{nw}" 
        extend 1kslbol " Apology accepted.{w=0.75}{nw}"
        extend 4kcsbol " Just please..." 
        n 4ksqbol "...No more surprises like that,{w=0.2} okay?"
        n 2ksrfll "I...{w=0.75}{nw}"
        extend 2ksrsll " really {i}don't{/i} need them."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 4fbkwrl "A-{w=0.2}and you're right to {i}be{/i} sorry,{w=0.2} [player]!"
        n 4flleml "I {i}hate{/i} being made to feel like that!{w=0.75}{nw}"
        extend 1kcseml " Jeez..."
        n 2fcspo "..."
        n 2fcsaj "Alright,{w=0.5}{nw}" 
        extend 1flrsl " look.{w=0.75}{nw}" 
        extend 4knmsl " I accept your apology,{w=0.2} okay?"
        n 3kslfl "Just don't do stuff like that to me.{w=1}{nw}"
        extend 3knmfl " Please?"
        n 3nsrsl "I'm not messing around,{w=0.2} [player]."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fsqsl "...Look,{w=0.2} [player].{w=0.75}{nw}" 
        extend 2fcsan " I'm already upset.{w=1}{nw}" 
        extend 2fnmwr " Why are you trying to make me feel even worse?"
        n 1fsqfu "Did you think it was funny?{w=0.75}{nw}" 
        extend 4fsqem " Or are you just trying to piss me off?"
        n 1fcssr "..."
        n 2fcssl "Whatever.{w=0.5} Fine.{w=0.75}{nw}" 
        extend 2flrsl " Apology accepted,{w=0.2} if you even {i}meant{/i} it."
        n 2fsqsf "Just knock it off."

        $ Natsuki.calculatedAffinityGain()

    else:
        n 4fsqfu "Stick it,{w=0.2} [player]."
        n 4fcsanltsa "We {i}both{/i} know you don't mean that."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.scare)
    return

# Apology for giving Natsuki a bad nickname
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For asking you to call me a bad name.",
            label="apology_bad_player_name",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_player_name:
    if persistent._jn_nicknames_player_allowed:
        # The player is still capable of nicknaming Natsuki
        if Natsuki.isEnamored(higher=True):
            n 1ncspuesi "..."
            n 2nllsl "...It's fine,{w=0.2} [player]."
            n 2ncsaj "Just..."
            n 1ksrsl "..."
            n 4kcstr "I really hate when I try to do something nice...{w=1}{nw}"
            extend 4ksqsr " and it just gets thrown back in my face,{w=0.2} you know?"
            n 1fcstr "I didn't {i}have{/i} to listen to what you wanted."
            n 2knmsrl "...So do you seriously think saying stuff like that {i}makes{/i} me want to do that again in the future?"
            n 2fllsrl "Because it {i}doesn't{/i},{w=0.2} [player]."
            n 2fcssrl "..."
            n 2kcsajsbl "...Look.{w=1}{nw}"
            extend 1nllpul " It's all water under the bridge,{w=0.2} okay?{w=0.75}{nw}"
            extend 4fllpol " I accept your apology."
            n 3fnmpol "Just use your noggin next time.{w=0.75}{nw}"
            extend 3fcspol " I {i}know{/i} there's one on your shoulders somewhere."
            n 3fsrunl "...Just don't start trying to prove me wrong on that.{w=0.75}{nw}"
            extend 4ksqpol " Please?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1tnmpueqm "...Huh?{w=1}{nw}"
            extend 4nnmsl " Oh,{w=0.3} right.{w=0.75}{nw}"
            extend 4fslbol " The whole name thing."
            n 1ncspuesi "..."
            n 2fsqca "...That was still a jerkish thing to do,{w=0.5}{nw}"
            extend 2fslca " you know."
            n 2fcsemlsbl "You're just lucky I don't keep pointless grudges forever." 
            extend 4fcsca " I'm a bigger person than that."
            n 1nllaj "So...{w=1}{nw}"
            extend 1nnmsl " you're forgiven.{w=0.75}{nw}"
            extend 3nsrbo " I guess."
            n 3fnmcal "Just think about what you come out with.{w=0.5}{nw}"
            extend 3ksrcalsbr " It really isn't hard,{w=0.2} is it?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 2fcsan "...You are just unbelievable,{w=0.2} [player]."
            n 4fsqfu "Did it {i}seriously{/i} take you this long to admit you were wrong to say that?"
            n 1flrem "Like,{w=0.5}{nw}"
            extend 2fnmsc " are you {i}trying{/i} to be funny?"
            n 2fsqup "...Or are you really just {b}that{/b} arrogant?"
            n 1fcsan "..."
            n 4fsqanean "...You know what?{w=0.5}{nw}"
            extend 4fcsfuean " Fine.{w=1}{nw}"
            extend 2fllwr " Who cares?{w=0.75}{nw}"
            extend 2fsqfultsb " You clearly don't."
            n 2fcsfrtsa "I'll accept your half-baked {i}attempt{/i} at an apology."
            n 2fsqfutsb "But only because it's less effort than getting angry about it."

        else:
            n 1fsquntdr "Heh.{w=0.75}{nw}"
            extend 1fsqantsb " {i}Now{/i} you apologize,{w=0.2} huh?"
            n 1fnmanltsfean "After all this time?"
            n 1fcsanltsd "..."
            n 1fcsfultsa "You know what?{w=1}{nw}"
            extend 1fsqfultsb " Maybe I {i}should{/i} just call you that name."
            n 1fskscftdc "Why not?!{w=1}{nw}"
            extend 1fskfuftdc " Not like you {i}aren't{/i} acting like it."
            extend 1fcsanltsd " Jerk."

    else:
        # The player has been barred from nicknaming Natsuki, and even an apology won't change that
        if Natsuki.isEnamored(higher=True):
            n 1nllsl "..."
            n 4knmsl "[player]."
            n 4knmaj "...Exactly how many times did I warn you?"
            n 2fnmem "How many times did I {i}forgive{/i} you?{w=1}{nw}"
            extend 2fcsemean " Because I honestly lost count."
            n 1kcsfresi "..."
            n 3nsqsr "Sorry,{w=0.2} [player].{w=0.5}{nw}"
            extend 3flltr " Every joke runs its course."
            n 4fsqunl "And I am {i}not{/i} going to be the butt of this one again."
            n 4fcsajl "So."
            n 4fllcal "Fine.{w=0.5} I'll accept your apology..."
            n 3fsqcalesi "...And you're going to accept the consequences."
            n 3fcstrl "Sorry,{w=0.3} [player]."
            extend 3fsqbol " But we're done with names here."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 4fcsemesi "...You've got to be kidding me,{w=0.5} right?"
            n 2fllaj "You were a jerk so many times to me about that..."
            n 2fsqan "...And you leave it this long to even {i}apologize{/i}?"
            n 2fcsemesi "..."
            n 4fsqtr "You're just lucky I'm not one for holding dumb grudges."
            n 3fcsaj "So,{w=0.3} [player]."
            n 3fslpo "I guess I'll accept the apology."
            n 4fnmfr "...But you can {i}forget{/i} about me accepting any more of your nicknames."
            n 2fsqtr "I'm done being messed around."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 2fcsan "{i}Wow{/i}.{w=1}{nw}"
            extend 2fcsfu " I would say I'm speechless,{w=0.3} if it were literally {i}anyone{/i} else."
            n 4fsqfuean "But {i}you{/i}?"
            n 2fcsem "I've about come to {i}expect{/i} this sort of crap from you."
            n 2fsqwrean "So you know what?{w=0.75}{nw}"
            extend 4fcssclean " Screw this,{w=0.75}{nw}"
            extend 3fskscltsc " and screw your apology!"
            n 1fcsscltsa "If {i}you{/i} aren't gonna listen,{w=0.5}{nw}"
            extend 2fllscltsc " then you can tell me why I {b}should{/b}!"

        else:
            n 1fcsfultdrean "Oh,{w=1}{nw}"
            extend 4fcsscltsaean " take a hike,{w=0.5}{nw}"
            extend 4fsqscltsbean " [player]!"
            n 2fcswrltsd "You {i}need{/i} a walk if you {i}seriously{/i} think after all of your crap,{w=0.75}{nw}"
            extend 4fskwrftdcean " I'm gonna be the one listening to {b}you{/b}!"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_player_name)
    return
