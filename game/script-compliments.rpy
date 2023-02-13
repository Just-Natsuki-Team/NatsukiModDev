default persistent._compliment_database = dict()

init 0 python in jn_compliments:
    from Enum import Enum
    import random
    import store

    COMPLIMENT_MAP = dict()

    class JNComplimentTypes(Enum):
        """
        Identifiers for different compliment types.
        """
        amazing = 1
        beautiful = 2
        confident = 3
        cute = 4
        hilarious = 5
        inspirational = 6
        style = 7
        thoughtful = 8

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
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

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
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_amazing").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.amazing:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 4uskemfesh "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}" 
            extend 1fcsemfsbr " Honestly!{w=0.75}{nw}" 
            extend 4kwmemfsbr " Again?!{w=1}{nw}" 
            extend 4kslpofsbr " Jeez..."
            n 2nslsllsbr "..."
            n 2nslpulsbr "But...{w=0.75}{nw}" 
            extend 1ksqcalsbr " thanks.{w=0.5} It really...{w=0.75}{nw}" 
            extend 4ksrcalsbr " means a lot to me."
            n 4ksqajlsbr "...And [player]?"
            n 1kslbolsbr "..."
            n 2fcstrl "...You're pretty amazing too." 
            n 2fcspol "A-{w=0.2}and you better remember that."

            if Natsuki.isLove(higher=True):
                n 2kchssleaf "L-{w=0.2}love you,{w=0.2} [player]!"

        else:
            n 1nslsslsbr "Jeez,{w=0.2} [player]...{w=0.5}{nw}"
            extend 1klrbolsbr " you...{w=0.5} really are doling out the compliments today,{w=0.5}{nw}" 
            extend 4ksrsslsbr " huh?"
            n 2fcsajl "D-{w=0.2}don't get me wrong though!{w=0.5}{nw}" 
            extend 2fcsbglsbl " I'm not complaining!"
            extend 2fcssmlsbl " I-{w=0.2}it's good to know we {i}both{/i} agree!"
            extend 4nslsslsbr " Just..."
            n 1ksqbolsbr "Make sure you don't leave yourself out though,{w=0.2} 'kay?"
            n 4kllsslsbr "You're {i}almost{/i} as amazing,{w=0.2} a-{w=0.2}after all."
            n 3fsqdvlsbr "...{i}Almost{/i}."
            extend 3fchbllsbr " Ehehe."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1kwmpul "...Y{w=0.2}-you really think so,{w=0.5}{nw}" 
            extend 1kllpul " [player]?"
            n 4kllsrl "..."
            n 1ncsssl "Heh."
            n 2fslpolsbl "It's always super embarrassing to say it,{w=0.2} you know."
            n 2kslbol "..."
            n 2ncspul "But...{w=0.75}{nw}"
            extend 2kwmbol " thanks."
            n 4fcsajlsbr "It means...{w=0.75}{nw}" 
            extend 1ksrsllsbr " a lot to me,{w=0.5} [player]."
            n 1ksqsllsbr "Really.{w=0.75}{nw}" 
            extend 4ksqbol " Thank you.{w=0.75}{nw}" 
            extend 4kcspul " You're honestly...{w=1}{nw}" 
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            extend 1ksrcal " [chosen_descriptor],{w=0.3} [player]."
            n 1ksrfsl "..."

            if Natsuki.isLove(higher=True):
                n 4kchssf "L-{w=0.2}love you."

        else:
            n 1uskgslesh "O-{w=0.2}oh!{w=0.5}{nw}" 
            extend 4fllbglesssbr " A-{w=0.2}aha!{w=0.5}{nw}" 
            extend 2fcsbglsbr " Well,{w=0.2} I knew you'd {i}have{/i} to admit it {i}eventually{/i}!"
            n 2fcssmlsbl "I'm just glad to hear {i}both{/i} of us agree on that.{w=0.75}{nw}"
            extend 1fsldvlsbl " Ehehe."

            if Natsuki.isAffectionate(higher=True):
                n 3fcsssl "J-{w=0.2}just remember though,{w=0.2} [player]..."
                n 3fchbll "You're at {i}least{/i} second best!"

            else:
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchgnlsbr "Thanks,{w=0.2} [chosen_tease]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.amazing
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're beautiful!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_beautiful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.beautiful:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 1fcsanlesssbl "Uuuuuu-!"
            n 4kwdgslesssbl "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 1kbkwrless " You already told me thaaaaat!"
            n 4ksqemlsbr "You really gotta do it {i}again{/i}?!"
            n 2ksrbolsbr "..."
            n 2ncsemlesisbr "..."
            n 1ncsbolsbr "...Fine.{w=0.75}{nw}"
            extend 4kslbolsbl " I'll take it."
            n 2fcscalsbl "The compliment,{w=0.2} I mean.{w=0.75}{nw}"
            extend 2fcstrlsbl " Just..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1ksrcal "..."
            n 4ncsssl "...Heh.{w=1}{nw}"
            extend 4nslfsl " Nevermind."
            
            if Natsuki.isLove(higher=True):
                n 2kslbol "T-{w=0.2}thanks again,{w=0.2} [chosen_tease]."
                n 1kslfsfeaf "...Y-{w=0.2}you always make me feel prettier."

            else:
                n 2kslbol "T-{w=0.2}thanks again,{w=0.2} [chosen_tease]."
                n 1kslcaf "..."

        else:
            n 4fskgslesh "E-{w=0.2}excuse me?!"
            n 1fwmgslsbl "[player]!{w=0.5}{nw}" 
            extend 4fbkwrlsbl " What did {i}literally{/i} just I tell you?!"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcsgsl "Are you {i}trying{/i} to give me a heart attack or something?!{w=0.75}{nw}"
            extend 2fsleml " Sheesh..."
            n 2fslpol "..."
            n 4fcsajl "I-{w=0.2}I mean,{w=0.75}{nw}"
            extend 3fcspol " I know I already look great!{w=1}{nw}"
            extend 3fsrdvlsbl " I {i}always{/i} look top-{w=0.2}notch, o-{w=0.2}of course."
            n 2fcsemlsbl "But you {i}really{/i} don't have to..."
            n 2fslunlsbl "T-{w=0.2}to keep...!"
            n 1fcsunlsbl "..."
            n 4fcsemlsbr "Oh,{w=0.5}{nw}"
            extend 2flrbolsbr " forget it!"

            if Natsuki.isAffectionate(higher=True):
                n 2fcscalsbr "You know what I mean,{w=0.2} a-{w=0.2}anyway..."

            n 2ksrbolsbr "..."

    else:
        if Natsuki.isEnamored(higher=True):
            n 4uskemlesh "H-{w=0.2}huh?!"
            n 1fcseml "Wait..."
            n 1kllemlsbl "Y-{w=0.2}you really think I'm..."
            n 1fslunfsbl "I-{w=0.3}I'm..."
            n 4fcsunfesssbr "..."
            n 2kcsbolsbr "..."
            n 2ksqbolsbr "[player]..."
            n 1kllbolsbr "You {w=0.2}{i}do{/i}{w=0.2} know you're not meant to just say things like that..."
            n 4kwmslfsbl "Unless you really mean them?"

            if Natsuki.isLove(higher=True):
                n 1knmajlsbl "I-{w=0.2}it's not that I don't believe you!{w=1}{nw}"
                extend 2klrsslsbl " O-{w=0.2}of course not!"
                n 4ksrbolsbl "...You should know that by now."
                n 2ksrpulsbl "But..."
                n 4ksrsll "..."
                n 1ksrfsl "...Thanks,{w=0.2} [player].{w=1}{nw}"
                extend 1ksrssl " Really{w=0.2}, heh."
                n 4ksqfsl "Thank you."
                n 3fcssmless "...Just don't forget {i}who{/i} helps me feel that way.{w=0.75}{nw}"
                extend 3fsqbll " You goof."
                n 4fchsmleaf "Ehehe."

            else:
                n 1kslcafsbl "..."
                n 2fcstrlesssbr  "I-{w=0.2}I mean...!"
                n 2nsrsllsbr "...{w=0.75}{nw}"
                extend 2ksrbolsbr "Really."
                n 2ksrfslsbr "T-{w=0.2}thanks, [player]."

        else:
            n 1uskemlesh "W{w=0.2}-w{w=0.2}-what?"
            n 1fskeml "W-{w=0.2}what did you say?!"
            n 4fcsanfsbr "Nnnnnnnnnn-!"
            n 4fbkwrfsbr "Y-{w=0.2}you can't just {i}say{/i} things like that so suddenly!"
            n 2fllemlsbl "Sheesh...{w=0.75}{nw}"
            extend 2fslpolsbl " come on,{w=0.2} [player]..."
            n 1fcsbolsbr "..."
            n 1fcsemlsbr "I-{w=0.2}I mean,{w=0.75}{nw}" 
            extend 3fsrbglsbr " I'm glad we both agree,{w=0.75}{nw}" 
            extend 4fsrunlsbr " but..."
            n 1fcsunlesssbl "Uuuuuu...!"
            n 1fcsemlsbl "Just..." 
            n 1kslcal "..."
            n 2ksqsllsbr "...Think a little before you just blurt stuff out like that.{w=0.75}{nw}"
            extend 2fsrsllsbr " I-{w=0.2}it just makes everything all awkward."
            n 1fsrsslsbr "...Heh.{w=0.75}{nw}"
            extend 4fcsajlsbr " A-{w=0.2}and besides,{w=0.75}{nw}"
            n 3fcsbglsbl " I {i}always{/i} look stunning anyway!{w=0.75}{nw}"
            extend 3nslsslsbl " So...{w=0.5}{nw}" 
            extend 3nslbol " yeah."
            n 3kslsllsbr "..."

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.beautiful
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how confident you are!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_confident").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.confident:
        n 1fcssmleme "Ehehe.{w=0.5}{nw}"
        extend 2fcsbg " Well,{w=0.2} I'm glad you still agree,{w=0.2} [player]!"
        n 2fllsm "Besides,{w=0.5}{nw}"
        extend 2fcssm " it's only natural."
        
        if Natsuki.isEnamored(higher=True):
            n 4nslssl "E-{w=0.2}especially with you around,"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 3fchbll " [chosen_tease]."

        else:
            n 2fcsbgedz "Brimming with confidence,{w=0.5}{nw}"
            extend 2flrbs " always unfazed..."
            n 3uchgnl "...That's just what it means to be a pro,{w=0.2} right?"
    
    else:
        n 4fsqct "Oho?{w=1}{nw}"
        extend 3fsqcs " You do,{w=0.2} do you?"
        n 3fchgn "Now that's {i}just{/i} what I like to hear!"
        n 4fcsbg "After all,{w=0.5}{nw}"
        extend 2fcssmeme " don't I just {i}radiate{/i} confidence?"
        n 4tsqbg "Come on,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fchgn " No need to be shy!{w=0.5}{nw}"
        extend 4fsqbg " You {i}gotta{/i} tell me!"
        n 3fllct "Is it the eyes?"
        n 3fcsbg "The smile?"
        n 3usqsm "The {i}killer{/i} personality?"
        n 4fchsmedz "Ehehe."
        n 2fcsss "Well,{w=0.2} whatever it is..."
        
        if Natsuki.isLove(higher=True):
            n 4nsrsmsbl "..."
            n 4fcssmlsbl "I-{w=0.2}I hope I inspire you just as much as you inspire me.{w=0.75}{nw}"
            extend 4fchdvlsbl " Ehehe."
            n 1fchbgleafsbr "L-{w=0.2}love you,{w=0.2} [player]!"

        elif Natsuki.isEnamored(higher=True):
            n 2fcsbg "I hope I inspire some confidence in you too!"
            n 2fslbglsbr "N-{w=0.2}not that you need it {i}too{/i} much,{w=0.2} a-{w=0.2}anyway."
            n 2fchbglsbr "Y-{w=0.2}you're welcome,{w=0.2} [player]!"

        else:
            n 2fchgnl "I better inspire some confidence in you too!"
            n 2fwlsm "You're welcome,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.confident
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I think you're cute!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_cute").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.cute:
        if Natsuki.isEnamored(higher=True):
            n 1fskwrleshsbr "..."
            n 4fcsanlsbr "..."
            n 4fcsfulsbl "..."
            n 1fcsfufsbl "Urgh!"
            n 4fcsgsf "Alright,{w=0.5}{nw}" 
            extend 1fcsemfsbl " fine!{w=0.5}{nw}" 
            extend 2fcswrfsbl " Fine!{w=0.5}{nw}" 
            extend 2fbkwrfsbl " You win,{w=0.2} okay?!"
            n 2fcsunfesi "..."
            n 2fcsemf  "I'm kinda...{w=0.5} maybe...{w=0.75}{nw}" 
            extend 1fslemf " sorta..." 
            n 1fcsgsf "Somehow..."
            n 4fsqemf "In some {i}abstract{/i} way..."
            n 1fsrsrf "..."
            n 1fsqpuf "...{w=0.3}'cute.'"
            n 2fsqslf "..."
            n 2fcsemf "There.{w=0.75}{nw}" 
            extend 2fcsgsf " I said it,{w=0.2} [player].{w=0.75}{nw}" 
            extend 2fcspof " I said it.{w=0.75}{nw}" 
            extend 2fllpof " {i}Hooray{/i} for you."
            n 1fsqpof "Are we done?{w=0.75}{nw}" 
            extend 4fnmpof " Are you happy?{w=0.75}{nw}" 
            extend 2fcsgsf " Are you {i}pleased{/i} with yourself now?"
            n 1flrpof "Jeez..."
            n 2fsqpof "I swear,{w=0.2} you're such a goofball sometimes..."

            if Natsuki.isLove(higher=True):
                n 1fcspol "A-{w=0.2}and besides,{w=0.2} [player]."
                n 3fcsajl "All this talk about {i}cuteness{/i}?{w=0.75}{nw}"
                extend 3flrcal " Being {i}adorable{/i}?"
                n 1fsqssl "...Heh."
                n 2fcssslsbl "S-{w=0.2}sounds like some pretty bad projection,{w=0.5}{nw}" 
                extend 4fcsbglsbl " i-{w=0.2}if you ask me."
                n 3fsqcsl "..."
                n 3fsqbgl "...Am I right,{w=0.5} {i}[player]{/i}?"
                n 3fsqsmlsbr "Ehehe."
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbllsbr "L-{w=0.2}love you too,{w=0.2} [chosen_tease]~!"

            else:
                n 1fcsajl "Just...{w=1}{nw}"
                extend 2fsrcal " don't let this get to your head."
                n 2fsqajlsbl "...Or you're gonna find out exactly how {w=0.4}{i}not{/i}{w=0.4} cute{w=0.4} I can be too."
                n 4fsqfsl "Ehehe."

        else:
            n 1fcsanfsbl "Nnnnnnn-!"
            n 4fcsgsf "H-{w=0.2}how many times do I have to explain this?!"
            extend 4fllemf " Do I really have to spell it out for you too,{w=0.2} [player]?!"
            n 4fcsanf "For the {i}last time{/i}..."
            n 1fbkwrfsbl "{i}I'M{w=0.3} NOT{w=0.3} CUTE!!{/i}"
            n 1flremf "Jeez..."
            n 2fsrpol "..."
            n 2fsqeml "...You just {i}wanted{/i} me to say that,{w=0.2} didn't you?"
            n 4fcspolesi "Honestly...{w=0.75}{nw}"
            extend 3fsqcal " you can be such a jerk sometimes,{w=0.2} [player]."

            if Natsuki.isAffectionate(higher=True):
                n 3nslcal "..."
                n 1nllajl "Well..."
                n 2fcspol "Just count yourself lucky you're in my good books."
                n 2fsqsslsbl "O-{w=0.2}or I wouldn't be {i}nearly{/i} this patient.{w=0.75}{nw}" 
                extend 2fsqsmlsbl " Ehehe."

            else:
                n 3nslcal "..."
                n 1nllajl "Well...{w=0.75}{nw}"
                extend 1nslpol " whatever."
                n 2fcscal "Just be grateful that I'll hold back on the whole lecture for you."
                n 2fsqssl "...This time."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fcsbslsbr "A-{w=0.2}Aha!{w=0.5}{nw}" 
            extend 2fchbglsbr " Nope!"
            n 2fsqfslsbr "..."
            n 4fsqsmlsbr "Nice try,{w=0.2} [player]..."
            n 3fcsbgl "But you're not gonna get me to say it {i}that{/i} easily!{w=0.5}{nw}"
            extend 3fcssmlsbl " Ehehe."

        else:
            n 4uskemfesh "W-{w=0.2}what?" 
            n 4fnmemfsbl "{i}What{/i} did you just say?!"
            n 1fllunfsbl "..."
            n 1nsrsrfsbr "..."
            n 2fsrssfsbr "I...{w=0.75}{nw}" 
            extend 2fsqunfsbr " must have misheard you."
            n 4fcsbgl "Y-{w=0.2}yeah.{w=0.5}{nw}" 
            extend 3fchbgl " Yeah!{w=0.75}{nw}" 
            extend 3fcssslsbl " I {i}totally{/i} misheard you!{w=0.5} O-{w=0.2}one hundred percent."
            n 3fslunlsbl "..."

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.cute
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of humor!",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_hilarious").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.hilarious:
        n 4usqss "Oh...?"
        n 3tsqcs "What is this?{w=0.75}{nw}"
        extend 3fcsbg " An encore or something?"
        n 4uchgnl "Well,{w=0.3} I'm taking it!"
        n 2fsqfs "Don't you worry,{w=0.2} [player]..."

        if Natsuki.isEnamored(higher=True):
            n 2fchbgleme "You aren't escaping {i}our{/i} routine any time soon!{w=0.5}{nw}"
            extend 4fchsml " Ehehe."

            if Natsuki.isLove(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbll "Love you too,{w=0.2} [chosen_tease]~!"
            
        else:
            n 2fchsmeme "You aren't escaping {i}my{/i} routine any time soon!{w=0.5}{nw}"
            extend 2nchgnl " Ahaha."

    else:
        if Natsuki.isEnamored(higher=True):
            n 4fcscs "Oho?{w=0.75}{nw}"
            extend 3fcsbg " What's that,{w=0.2} [player]?"
            n 3fchgnlelg "So you {w=0.2}{i}do{/i}{w=0.2} recognize talent when you see it!{w=0.75}{nw}"
            extend 4fcssml " Ehehe..." 
            n 2nslfsl "..."
            n 2nslbol "But...{w=0.75}{nw}" 
            extend 2tsqcal " seriously,{w=0.2} [player]?"
            n 1ksrcal "..."
            n 1klrss "I'm honestly...{w=0.75}{nw}" 
            extend 4nsrss " kinda glad to hear that."
            n 1fcsajlsbr "I-{w=0.2}I know it's dumb.{w=0.75}{nw}" 
            extend 4nslbolsbr " But I always kinda worry about how much fun you're having here."
            n 4nlrcalsbr "With me,{w=0.2} I mean."
            n 4ksqbolsbl "I...{w=0.3} don't want you to get all bored..."
            n 2fcsajlsbl "T-{w=0.2}that'd just be super lame."
            n 1kllbol "So...{w=0.5}{nw}" 
            extend 1knmbol " thanks,{w=0.2} [player].{w=0.5}{nw}" 
            extend 2klrfsl " Really."
            n 2nsrsslsbl "It means a lot."

            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "Y-{w=0.2}you always know just what to say."

        else:
            n 1fcssm "Ehehe.{w=0.75}{nw}"
            extend 2fchgneme " Oh,{w=0.2} you {i}bet{/i} I got an amazing sense of humor!"
            n 4ullss "But...{w=0.5}{nw}"
            extend 3fcsbsl " I'm just glad we both recognize that."

            if Natsuki.isAffectionate(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbll "Much obliged,{w=0.2} [chosen_tease]!"

            else:
                n 3fchbgl "Much obliged,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.hilarious
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="You're an inspiration to me!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_inspirational").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.inspirational:
        n 1nchgn "Ahaha.{w=0.75}{nw}" 
        extend 2fcsbg " Well,{w=0.2} what can I say?{w=0.75}{nw}" 
        extend 2fchsmedz " I guess it must be natural~."
        n 1nchsm "But thanks,{w=0.2} [player]!"
        n 4fsqsm "Don't worry."
        extend 3fwlbg " You can always count on yours truly for {i}all{/i} your inspiration needs!"

        if Natsuki.isEnamored(higher=True):
            n 3fsrssl "J-{w=0.2}just like I know I can count on you.{w=0.75}{nw}"
            extend 1fchsml " Ehehe."

    else:
        n 4unmemleex "H-{w=0.2}huh?{w=0.75}{nw}"
        extend 2flrbglsbr " W-{w=0.2}well,{w=0.2} yeah!{w=0.75}{nw}"
        extend 2fcsbglsbr " Duh!"
        n 2fchgnsbr "Of course I am,{w=0.2} you dope!{w=1}{nw}"
        extend 4fllct " In fact..."
        n 1fcsct "I daresay you'd be hard pressed to find a {i}better{/i} role model than me."
        n 3fsqsmeme "Ehehe."

        if Natsuki.isEnamored(higher=True):
            n 3ullaj "Well,{w=0.2} anyway.{w=0.75}{nw}"
            extend 4fwlbg " You're welcome,{w=0.2} [player]!"
            n 2fchbgl "I'll {i}always{/i} be around to inspire you."

            if Natsuki.isLove(higher=True):
                n 2nsrsmlsbl "...You do the same for me,{w=0.2} a-{w=0.2}after all."

        else:
            n 3fcsbgedz "Well,{w=0.2} feel free to be inspired by me anytime,{w=0.2} [player].{w=1}{nw}"
            extend 4fsqss " After all..."
            n 2fwlbg "That's just what the pros are for,{w=0.2} right?"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.inspirational
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love your sense of style!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_style").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.style:
        if not Natsuki.isWearingOutfit("jn_school_uniform"):

            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1fcssm "Ehehe.{w=0.5}{nw}" 
                extend 3fcsbgeme " Still awestruck by my sense of fashion,{w=0.2} [player]?"
                n 3ullss "Well,{w=0.5}{nw}" 
                extend 4tllsm " if nothing else -{w=0.5}{nw}"
                extend 2fcssm " you can't deny I'm a snappy dresser."

                if Natsuki.isLove(higher=True):
                    n 2fsqsml "Don't you worry.{w=0.75}{nw}"
                    extend 2uchgnledz " I'll keep looking fabulous juuuust for you~!"

                else:
                    n 2fchsml "Thanks a bunch,{w=0.2} [player]!{w=0.75}{nw}"
                    extend 2fchgnledz " 'Preciated!"

            else:
                n 4tnmaj "Oh?{w=0.5}{nw}" 
                extend 2tsqss " Sounds like {i}someone{/i} is just itching to take a few points,{w=0.2} huh?"
                n 2fsqsm "Ehehe."
                n 1fchbg "Relax,{w=0.2} relax!{w=0.5}{nw}" 
                extend 1uchsm " I'm kidding,{w=0.2} [player].{w=0.3} Don't worry."
                n 4fsqsm "...Mostly."
                n 3fwlbl "But thanks again!"

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 4usqct "Oh?{w=0.75}{nw}"
                extend 4fsqctl " You never told me you had a thing for uniforms,{w=0.2} [player]."
                n 2fsqbglsbl "I-{w=0.2}is there something you wanna tell me?{w=0.75}{nw}"
                extend 2fnmsglsbl " Huh?"
                n 1flldvlsbl "..."
                n 4fchdvlesisbr "Pfffft-!"
                n 4fcsajl "Oh,{w=0.5}{nw}"
                extend 1fchbgl " relax,{w=0.2} [player]!{w=0.75}{nw}"
                extend 2fllbgl " Jeez..."
                n 2fchsmlsbr "Y-{w=0.2}you should know when I'm pulling your leg by now,{w=0.2} you dork.{w=1}{nw}"
                extend 1fcsssl " And besides..."
                n 2flldvl "I {i}know{/i} I totally rock the school look."
                n 2fchbll "But thanks anyway!"

            else:
                n 2fsqsmlsbl "Still head-over-heels for the educated look,{w=0.5}{nw}"
                extend 2fcssslsbl " huh?"
                n 2fcsbglesssbl "W-{w=0.2}well,{w=0.75}{nw}"
                extend 2fllbglesssbr " I guess that just means I can make {i}anything{/i} look good!"
                n 1fslsslesssbr "Ahaha..."

    else:

        if not Natsuki.isWearingOutfit("jn_school_uniform"):

            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1fchsmleme "Ehehe.{w=0.75}{nw}" 
                extend 1nchsml " I'm just happy you like this outfit,{w=0.2} [player]!"
                n 1ulrbol "But then...{w=0.75}{nw}" 
                extend 4tlrbol " now that I think about it..."
                n 2tsqssl "Should I {i}really{/i} be surprised?"
                n 3fcsbgl "I-{w=0.2}I {i}am{/i} the one wearing it,{w=0.5}{nw}" 
                extend 3uchgnl " after all!"

                if Natsuki.isLove(higher=True):
                    n 3fchblleaf "Love you too,{w=0.2} [player]~!"

            else:
                n 1fcsbglsbl "H-{w=0.2}ha!{w=0.5}{nw}" 
                extend 2flrbglsbl " I'm glad you agree!"
                n 4fcssml "It's only natural though,{w=0.2} right?{w=0.5}{nw}" 
                extend 2fcsbgledz " I like to pride myself on my {i}superb{/i} sense of style!"
                n 2fwlbll "Good job noticing,{w=0.2} [player]!"
                extend 2fchgnl " Ehehe."

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1tnmpul "M-{w=0.2}my sense of style?"
                n 1tslpu "..."
                n 4tslaj "You...{w=0.75}{nw}"
                extend 2fsldv " {i}do{/i} see what I'm wearing,{w=0.75}{nw}"
                extend 2fchgn " right?"
                n 1nlrss "Man...{w=0.75}{nw}"
                extend 2fsqsm " you're such a dork sometimes,{w=0.2} [player].{w=0.75}{nw}"
                extend 2fcsbg " But it's the thought that counts!"
                n 4fchsm "Ehehe."
                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
                n 2fchgnl "'Preciated as always,{w=0.2} [chosen_descriptor]!"

            else:
                n 1tnmpuleqm "M-{w=0.2}my sense of style..."
                n 4tsqpu "...What?{w=0.75}{nw}"
                extend 2tnmdv " You mean my school uniform?"
                n 4fchdvesi "Pfffft-!"
                n 1fchbselg "What kind of compliment is {i}that{/i}?!"
                n 2tlrsslsbl "You really {w=0.2}{i}aren't{/i}{w=0.2} good at this sort of thing are you,{w=0.5}{nw}" 
                extend 2tnmsmlsbl " [player]?{w=0.5}{nw}"
                extend 2fsqsmlsbl " Ehehe."
                n 1fcsbgl "Well,{w=0.75}{nw}"
                extend 1fllbgl " I-{w=0.2}I guess you tried!{w=0.75}{nw}"
                extend 4fcssmeme " And isn't that always what matters?"
                n 3fchgn "Thanks anyway,{w=0.2} you goof!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.style
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="I love how thoughtful you are!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_thoughtful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.thoughtful:
        if Natsuki.isEnamored(higher=True):
            n 1unmaj "...Wow.{w=0.75}{nw}"
            extend 1ulrbo " You...{w=0.75}{nw}"
            extend 4tnmssl " really are still hung up over that, huh?"
            n 1ncsajl "But seriously,{w=0.2} [player] -{w=0.5}{nw}"
            extend 3fchbglsbl " don't worry about it!{w=0.75}{nw}"
            extend 3fcssmlesisbl " It's totally fine."
            n 1fllbol "Besides,{w=0.75}{nw}"
            $ friend_type = "girlfriend" if Natsuki.isLove(higher=True) else "friend"
            extend 2fcseml " what kind of [friend_type] would I be if I {i}wasn't{/i} at least trying to be thoughtful?"
            n 2fsrbglsbr "P-{w=0.2}plus it looks like you're trying just as much anyway!"
            n 4tsrbolsbr "..."
            n 1tsrpu "Well,{w=0.5}{nw}" 
            extend 1fsrsssbl " if it puts your mind at ease...{w=1}{nw}"
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            extend 3fcssml " no worries,{w=0.2} [chosen_descriptor]!"
            n 3fchgnledz "You don't have to ask me to keep it up!"

        else:
            n 1unmpul "H-{w=0.2}huh?{w=0.75}{nw}"
            extend 1fllbgl " Oh,{w=0.2} right.{w=0.5}{nw}"
            extend 4fsldvl " Ahaha."
            n 2unmaj "Well,{w=0.5}{nw}"
            extend 2ulraj " just like I was saying before -{w=0.5}{nw}"
            extend 2fcsaj " it's really {i}not{/i} much to ask at all."
            n 3fchgn "...So don't worry about it,{w=0.2} you goof!"
            n 3fwlsm "It's no sweat off my back!"

    else:
        if Natsuki.isEnamored(higher=True):
            n 2nslss "Man...{w=0.75}{nw}"
            extend 2fchgnl " you make it sound like I had to put effort in or something!"
            n 1fcssmlsbl "Ahaha."
            n 4ullss "Nah,{w=0.75}{nw}" 
            extend 3fcsss " it's nothing."
            n 1unmbo "Being a little thoughtful is what {i}most{/i} people deserve,{w=0.2} at least.{w=1}{nw}"
            extend 2flrca " I kinda just consider that being a decent person."
            n 2ulraj "That being said though,{w=0.2} [player]." 
            n 1fcscal "I don't mind putting in a bit more for you..."
            n 4fsqssl "...But only a {i}bit{/i}.{w=0.75}{nw}"
            extend 4fchsml " Ehehe."

            if Natsuki.isLove(higher=True):
                n 1fchgnl "Love you too,{w=0.2} [player]~!"

            else:
                n 1fchbgl "Any time,{w=0.2} [player]!"

        else:
            n 2tnmpuleqm "Eh?{w=0.75}{nw}"
            extend 2tnmajl " Thoughtful?"
            n 1fllbglesssbl "W-{w=0.2}well...{w=0.75}{nw}"
            extend 4fchbglsbl " yeah!{w=0.75}{nw}"
            extend 4fsrdvlsbl " At least I {i}like{/i} to think so, anyway."
            n 3unmbo "It's not like it's much to ask though.{w=1}{nw}"
            extend 3nllsssbr " Being thoughtful,{w=0.2} I mean."
            n 1ulrbosbr "Honestly,{w=0.5}{nw}"
            extend 2tlrcasbr " it's really the {i}least{/i} anyone can expect."
            n 2uchgn "But hey,{w=0.2} I'll take it!"
            n 2fchsm "You're welcome,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.thoughtful
    return
