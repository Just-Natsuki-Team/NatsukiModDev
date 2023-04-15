default persistent._jn_joke_list = dict()
default persistent._jn_daily_jokes_unlocked = False
default persistent._jn_daily_joke_given = False
default persistent._jn_daily_jokes_enabled = True

image joke_book = "mod_assets/props/joke_book_held.png"

init python in jn_jokes:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    __ALL_JOKES = {}

    class JNJokeCategories(Enum):
        neutral = 1
        funny = 2
        corny = 3
        bad = 4

    class JNJoke:
        def __init__(
            self,
            label,
            joke_category,
            conditional=None,
        ):
            self.label = label
            self.is_seen = False
            self.shown_count = 0
            self.joke_category = joke_category
            self.conditional = conditional

        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each joke from the persistent.
            """
            global __ALL_JOKES
            for joke in __ALL_JOKES.values():
                joke.__load()

        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each joke to the persistent.
            """
            global __ALL_JOKES
            for joke in __ALL_JOKES.values():
                joke.__save()

        @staticmethod
        def filterJokes(
            joke_list,
            is_seen=None
        ):
            """
            Returns a filtered list of jokes, given a joke list and filter criteria.

            IN:
                - label - list of labels the joke must have 
                - is_seen - bool is_seen state the joke must be

            OUT:
                - list of jokes matching the search criteria
            """
            return [
                _joke
                for _joke in joke_list
                if _joke.__filterJoke(
                    is_seen
                )
            ]

        def asDict(self):
            """
            Exports a dict representation of this joke; this is for data we want to persist.

            OUT:
                dictionary representation of the joke object
            """
            return {
                "is_seen": self.is_seen,
                "shown_count": self.shown_count
            }

        def setSeen(self, is_seen):
            """
            Marks this joke as seen.
            """
            self.is_seen = is_seen
            self.shown_count += 1
            self.__save()

        def __load(self):
            """
            Loads the persisted data for this joke from the persistent.
            """
            if store.persistent._jn_joke_list[self.label]:
                self.is_seen = store.persistent._jn_joke_list[self.label]["is_seen"]
                self.shown_count = store.persistent._jn_joke_list[self.label]["shown_count"]

        def __save(self):
            """
            Saves the persistable data for this joke to the persistent.
            """
            store.persistent._jn_joke_list[self.label] = self.asDict()

        def __filterJoke(
            self,
            is_seen=None
        ):
            """
            Returns True, if the joke meets the filter criteria. Otherwise False.

            IN:
                - is_seen - bool is_seen state the joke must be

            OUT:
                - True, if the joke meets the filter criteria. Otherwise False
            """
            if is_seen is not None and not self.is_seen == is_seen:
                return False

            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False

            return True

    def __registerJoke(joke):
        if joke.label in __ALL_JOKES:
            jn_utils.log("Cannot register joke name: {0}, as a joke with that name already exists.".format(joke.label))

        else:
            __ALL_JOKES[joke.label] = joke
            if joke.label not in store.persistent._jn_joke_list:
                joke.__save()

            else:
                joke.__load()

    def getJoke(joke_name):
        """
        Returns the joke for the given name, if it exists.

        IN:
            - joke_name - str joke name to fetch

        OUT: Corresponding JNJoke if the joke exists, otherwise None 
        """
        if joke_name in __ALL_JOKES:
            return __ALL_JOKES[joke_name]

        return None

    def getAllJokes():
        """
        Returns all jokes.
        """
        return __ALL_JOKES.values()

    def selectJokes():
        """
        Returns a list of all unseen jokes, or None if zero that are unlocked and unseen exist.
        
        OUT:
            - List of JNJoke jokes, or None
        """
        joke_list = JNJoke.filterJokes(
            joke_list=getAllJokes(),
            is_seen=False
        )

        return joke_list if len(joke_list) > 0 else None

    def resetJokes():
        """
        Resets the is_seen state for all jokes.
        """
        for joke in getAllJokes():
            joke.is_seen = False

        JNJoke.saveAll()

    __registerJoke(JNJoke(
        label="joke_clock_eating",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_anime_animated",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_pirate_shower",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_cinderella_soccer",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_blind_fish",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_skeleton_music",
        joke_category=JNJokeCategories.corny,
        conditional="persistent.jn_custom_music_unlocked"
    ))
    __registerJoke(JNJoke(
        label="joke_skeleton_communication",
        joke_category=JNJokeCategories.corny,
        conditional="jn_jokes.getJoke('joke_skeleton_music').shown_count > 0"
    ))
    __registerJoke(JNJoke(
        label="joke_ocean_greeting",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_tractor_trailer",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_tentacle_tickles",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_basic_chemistry",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_upset_cat",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_cute_chicks",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_lumberjack_axeception",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_tallest_building",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_baking_baseball",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_soya_tofu",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_distrust_atoms",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_running_latte",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_guitar_stringing_along",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_snek_maths",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_balloonist_hot_air",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_author_cover_story",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_wrapped_up_quickly",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_carpentry_nailed_it",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_neutrons_no_charge",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_train_sound_track",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_bored_typist",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_regular_moovements",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_rabbit_lottery",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_trees_logged_out",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_con_crete",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_footless_snakes",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_bigger_ball",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_meeting_walls",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_hour_feeling",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_spotless_tigers",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_missing_bell",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_cheesy_pizza",
        joke_category=JNJokeCategories.bad
    ))

label joke_clock_eating:
    n 1fcsbg "Hey,{w=0.2} [player]..."
    n 1fsqbg "Have {i}you{/i} ever tried eating a clock?"
    n 1fsqcs "..."
    n 1tsqss "...No?"
    n 1ullaj "Well,{w=0.2} I can't say I blame you."
    n 1fllss "It's very...{w=1.25}{nw}" 
    extend 1fsqbg " {i}time{w=0.3} consuming{/i}."

    return

label joke_anime_animated:
    n 1ulraj "Say,{w=0.2} [player]..."
    n 1unmbo "You know how some people get really into their anime?{w=1}{nw}"
    extend 1nslsssbr " Like they {i}constantly{/i} mention it every chance they get."
    n 1tllsl "If they get super excited over an episode..."
    n 1tsqss "Would that make them...{w=1.25}{nw}"
    extend 1fsqbg " {i}anime{/i}{w=0.75}-ted?"

    return

label joke_pirate_shower:
    n 1unmfl "Did you know pirates wouldn't let their victims shower,{w=0.75}{nw}"
    extend 1ulraj " once they captured them?"
    n 1tlrsl "...Why?"
    n 1fcssm "Heh.{w=0.75}{nw}" 
    extend 1fsqsm " Isn't it obvious?"
    n 1fsrsssbl "...'Cause they'd just {i}wash up on shore{/i}."

    return

label joke_cinderella_soccer:
    n 1fchbg "Let's talk princesses,{w=0.2} [player]!"
    n 1tnmss "Any idea why Cinderella was so bad at soccer?"
    n 1tsqsm "..."
    n 1tsqss "...No?"
    n 1fchgn "...'Cause she kept running away from the {i}ball{/i}!"

    return

label joke_blind_fish:
    n 1fcsaj "Alright,{w=0.2} [player]..."
    n 1tsqsl "What do you call a fish without eyes?"
    n 1tsqfs "..."
    n 1fcsss "Nope,{w=0.5}{nw}" 
    extend 1fsrss " it's not {i}blind{/i}."
    n 1nsqcasbl "...It's {i}fsh{/i}."

    return      

label joke_skeleton_music:
    n 1fcsaj "Alright!{w=0.75}{nw}"
    extend 1nslsssbr " Seeing as you love music so much,{w=0.2} [player]..."
    n 1tsqsssbr "What's a skeleton's favourite instrument?"
    n 1nsrsssbr "..."
    n 1nsrposbl "...A xylo-{w=1}{i}bone{/i}."

    return 

label joke_skeleton_communication:
    n 1nsrsssbl "Here's another {i}spooky{/i} one for you.{w=0.75}{nw}"
    extend 1tnmsssbl " How do skeletons keep in touch with each other?"
    n 1fcssssbl "It's obvious.{w=0.75}{nw}"
    extend 1nslsssbr " They use a tele-{w=0.5}{i}bone{/i}."

    return    

label joke_ocean_greeting:
    n 1fcsbg "Alright!"
    n 1fcsss "What did the ocean say to the sand?"
    n 1fsqsm "..."
    n 1fcsbg "Nothing -{w=0.5}{nw}" 
    extend 1fchgn " it just {i}waved{/i}!"

    return  

label joke_tractor_trailer:
    n 1fllaj "I was meant to see a film all about tractors,{w=0.75}{nw}"
    extend 1fcspo " but I ended up missing it!"
    n 1ulraj "It's fine though,{w=0.2} really."
    n 1fsqss "I didn't catch see the tractor..."
    n 1fchbg "...But I at least saw the {i}trailer{/i}!"

    return     

label joke_tentacle_tickles:
    n 1fcsbg "So!{w=0.75}{nw}"
    extend 1fsqbg " How many tickles does it take to make an octopus laugh?"
    n 1fsqcs "..."
    n 1fllss "You'd need...{w=0.75}{nw}"
    extend 1fwlbg " {i}ten{/i}{w=1}-tickles!"

    return

label joke_basic_chemistry:
    n 1fcsbs "Time for a chemistry test,{w=0.2} [player]!"
    n 1fcsbg "What do you get when you mix sulfur,{w=0.5}{nw}"
    extend 1fllss " tungsten,{w=0.5}{nw}"
    extend 1fnmbg " and silver?"
    n 1usqcs "..."
    n 1fcsbg "{i}SWAG{/i},{w=0.5}{nw}"
    extend 1fchgn " of course!"

    return

label joke_upset_cat:
    n 1ulraj "How do you know if you've upset a cat?"
    n 1tnmsm "..."
    n 1fcssm "Ehehe."
    n 1fcsss "You get a...{w=1}{nw}"
    extend 1fsqss " {i}{w=0.2}fe{w=0.2}-line{/i}{w=0.75}{nw}"
    extend 1fwlbg " for the exit!"
    
    return

label joke_cute_chicks:
    n 1fslem "Why was the lonely farmer excited to go to the show-barn?"
    n 1fslsl "..."
    n 1fsrem "...Because he heard it'd be full of{w=0.75}{nw}" 
    extend 1fcsem " 'cute{w=0.75}{nw}" 
    extend 1fslsl " chicks'."

    return

label joke_lumberjack_axeception:
    n 1unmaj "What would a lumberjack do if they couldn't cut down a tree?"
    n 1flrsm "..."
    n 1flrss "They'd make an...{w=1}{nw}"
    extend 1fsqbg " {i}axe{/i}{w=1.25}{nw}"
    extend 1nchgn "-ception!"

    return

label joke_tallest_building:
    n 1fcsbg "Seeing as you love literature so much,{w=0.75}{nw}"
    extend 1fsqsm " this should be easy."
    n 1fcsaj "So!{w=1}{nw}"
    extend 1tnmss " Why are libraries the tallest buildings?"
    n 1fsqsm "..."
    n 1fchbg "...Because they have the most {i}stories{/i}!"

    return

label joke_baking_baseball:
    n 1unmbo "You enjoy baking,{w=0.2} right?"
    n 1fsqss "...So what do baking and baseball both have in common?"
    n 1tsqfs "..."
    n 1fcsbg "Easy!{w=0.75}{nw}"
    extend 1fwlbg " You gotta keep an eye on the {i}batter{/i}!"

    return

label joke_soya_tofu:
    n 1fsqbg "Fancy yourself a culinary expert,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsbg " Then riddle me this!"
    n 1fnmss "How does soya milk defend itself?"
    n 1fnmsm "..."
    n 1tsqss "Well?{w=1}{nw}" 
    extend 1fsqbg " Isn't it obvious?"
    n 1nchgn "It does {w=0.3}{i}to-{w=0.3}fu{/i}!"

    return

label joke_distrust_atoms:
    n 1nlrbo "You know,{w=0.2} [player]..."
    n 1fnmbo "I never liked studying physics.{w=0.75}{nw}"
    extend 1fslfl " {i}Especially{/i} atomic theory."
    n 1fslsl "..."
    n 1tnmem "What?{w=1}{nw}"
    extend 1flrfl " Can you blame me?{w=0.75}{nw}"
    extend 1fcsgs " It's ridiculous!"
    n 1fcspo "How am I meant to take it {i}seriously{/i}..."
    n 1fsqsm "...when the atoms {i}make up{/i} everything?"

    return

label joke_running_latte:
    n 1fcsfl "What do you call a barista that didn't make it to work on time?"
    n 1nsrsl "..."
    n 1ncsfl "Running...{w=1.25}{nw}" 
    extend 1fslcasbl " {i}latte{/i}."

    return

label joke_guitar_stringing_along:
    n 1unmpu "Did you hear about the band who just dropped their guitarist?"
    n 1fllfl "{i}Apparently{/i} they promised to practice with everyone,{w=0.75}{nw}"
    extend 1fnmgs " but they just never turned up!{w=0.75}{nw}"
    extend 1fcswr " What a jerk!"
    n 1fcspo "..."
    n 1fcsaj "Well,{w=0.75}{nw}"
    extend 1fllfl " I guess you could say they were just...{w=0.75}{nw}"
    extend 1fsqss " {i}stringing{/i}{w=1.25}{nw}"
    extend 1fcsbg " everyone along!"

    return

label joke_snek_maths:
    n 1ncsfl "...What kind of reptile would you trust to do long sums?"
    n 1nsqsl "..."
    n 1nslpo "..."
    n 1nsqem "...{i}An adder{/i}."
    
    return

label joke_balloonist_hot_air:
    n 1nsqsl "...What do an arrogant balloonist and their balloon have in common?"
    n 1ncsemesi "..."
    n 1nsrem "They're both full of...{w=0.75}{nw}"
    extend 1nslajsbr " {i}hot{w=0.3} air{/i}."
    
    return

label joke_author_cover_story:
    n 1fsqsg "You better not {i}book it{/i} after this one,{w=0.2} [player]..."
    n 1fcsbg "What does an author do when they need an excuse for a day off?"
    n 1fsqsm "..."
    n 1fcssm "Ehehe.{w=0.75}{nw}"
    extend 1fchbg " What else?"
    n 1uchgn "...They'd write a {i}cover story{/i}!"

    return

label joke_wrapped_up_quickly:
    n 1unmaj "Did you hear about the packaging company that went bust?"
    n 1tnmbo "..."
    n 1tllss "No?{w=0.75}{nw}"
    extend 1ncsss " I guess I shouldn't be too surprised."
    n 1fcsbg "After all."
    n 1fsqbg "They sure...{w=1}{nw}"
    extend 1fsqsm " {i}wrapped things up{/i}{w=0.75}{nw}"
    extend 1fchgn " quickly!"

    return

label joke_carpentry_nailed_it:
    n 1ullbo "You know..."
    n 1tnmbo "I never really got into carpentry much."
    n 1tlraj "But...{w=1}{nw}"
    extend 1fsqss " if I did?"
    n 1uchgn "...I bet I'd totally {w=0.3}{i}nail{/i}{w=0.3} it!"

    return

label joke_neutrons_no_charge:
    n 1fsqsm "I hope you're ready for some physics,{w=0.2} [player]."
    n 1fcsbg "So!{w=1}{nw}"
    extend 1fsqbg " Why don't neutrons have to pay entry fees when they go anywhere?"
    n 1fsqcs "..."
    n 1fcsbg "'Cause for neutrons...{w=1}{nw}" 
    extend 1uchgn " there's never any {i}charge{/i}!"

    return

label joke_train_sound_track:
    n 1fcsbg "What's a train driver's favourite thing to listen to while they're working?"
    n 1fnmsm "..."
    n 1tsqss "No?{w=0.75}{nw}"
    extend 1fcssm " Ehehe."
    n 1fcsbg "Sound{w=0.2}{i}tracks{/i},{w=1}{nw}"
    extend 1fchbg " of course!"

    return

label joke_bored_typist:
    n 1fcsfl "...Why did the typist end up quitting their job?"
    n 1fsrbo "..."
    n 1fcsemesi "..."
    n 1fcsfl "...Because they were key-{w=0.3}{i}bored{/i}."

    return

label joke_regular_moovements:
    n 1nsqem "Why shouldn't cows be made to walk up and down stairs too often?"
    n 1fsrsl "..."
    n 1fsrpu "Because it isn't part of their regular..."
    n 1fcsflesi "..."
    n 1fslflsbr "...{i}moo{/i}{w=1}-vements."

    return

label joke_rabbit_lottery:
    n 1nlraj "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1unmaj "did {i}you{/i} know that there's actually a rabbit {i}lottery{/i}?"
    n 1fcsbg "Not what you expected to hear,{w=0.2} I bet."
    n 1fchbg "But it makes perfect sense when you think about it!{w=1}{nw}"
    extend 1fsqsm " After all..."
    n 1fsqss "...How else do they join the{w=0.5}{nw}" 
    extend 1fnmbg " {i}bun{/i}{w=0.75}{nw}" 
    extend 1uchgn "-percent?"

    return

label joke_trees_logged_out:
    n 1fcsaj "So!{w=1}{nw}"
    extend 1fcsbg " Why is it so hard to find trees online,{w=0.2} [player]?"
    n 1fsqsg "..."
    n 1fnmss "Because they're always...{w=1}{nw}"
    extend 1fsqbg " {i}logged{/i}{w=1}{nw}"
    extend 1fchgn " out!"

    return

label joke_con_crete:
    n 1ullaj "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " did you hear about the construction project that got shut down?"
    n 1flrgs "Apparently all the materials were suddenly swapped out for cheap crap!{w=0.75}{nw}"
    extend 1fcsan " It wasn't even up to code!{w=1}{nw}"
    extend 1fsran " A complete scam!"
    n 1fcsaj "Turns out..."
    n 1fllfl "They got stuck with{w=0.5}{nw}"
    extend 1fsqbg " {i}con{/i}{w=1}{nw}"
    extend 1nchgn "-crete!"

    return

label joke_footless_snakes:
    n 1ulraj "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " have you ever wondered how to measure snakes?"
    n 1uwdaj "Like they are so long!"
    n 1fsqcs "What measurement could be possibly the best?"
    n 1fcsss "Well,{w=0.2} my guess would be in inches or centimetre...{w=0.5}"
    n 1nsrss " Because they...{w=1}{nw}"
    extend 1nchgn " have no {i}feet{/i}!"

    return

label joke_bigger_ball:
    n 1ullbo "You know..."
    n 1nslss "When I was playing sports lately..."
    n 1uwdaj "I wondered why the ball keeps getting bigger!{w=0.5}"
    n 1flrfl "Then it{w=1}{nw}" 
    extend 1fsqcs " {i}hit{/i} me!"

    return

label joke_meeting_walls:
    n 1fsqfl "...What did the wall say to the other wall?"
    n 1fcspo "..."
    n 1fslbo "We'll meet at the{w=1}{nw}"
    extend 1fsqbo " {i}corner{/i}."

    return

label joke_hour_feeling:
    n 1fcsaj "So!{w=1}{nw}"
    extend 1fsqsm " What did the clock ask the watch,{w=0.2} [player]?"
    n 1fsldv "..."
    n 1fchgn "{i}Hour{/i}{w=1} you doing?"

    return

label joke_spotless_tigers:
    n 1ulraj "So,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " did you ever ask yourself why tigers have stripes?"
    n 1fcsss "It is not a fashion choice,{w=0.2} that's for sure!"
    n 1fsqsm "It is because they don't want to be{w=1}{nw}"
    extend 1fchgn " {i}spotted{/i}!"

    return

label joke_missing_bell:
    n 1fsqsm "Knock,{w=0.2} knock,{w=0.2} [player]!"

    menu:
        "Who's there?":
            pass

    n 1fcsaj "Nobel."

    menu:
        "Nobel who?":
            pass

    n 1nnmbo "{i}No bell{/i},{w=1}{nw}"
    extend 1fchgn " so I just knocked!"

    return

label joke_cheesy_pizza:
    n 1fsqfl "...I've found a joke about pizza."
    n 1ftrsl "Ugh..."
    n 1fsqaj "But it is too{w=1}{nw}"
    extend 1fcspo " {i}cheesy{/i}."
    
    return
