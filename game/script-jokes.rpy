default persistent._jn_joke_list = dict()
default persistent._jn_daily_jokes_unlocked = False
default persistent._jn_daily_joke_given = False

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
        conditional="getJoke('joke_skeleton_music').shown_count > 0"
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
    n 1nsrsssbl "Here's another {i}spooky{/i} one for you.{w=1}{nw}"
    extend 1tnmsssbl " How do skeletons keep in touch with each other?"
    n 1fcssssbl "It's obvious.{w=1}{nw}"
    extend 1nslsssbr " They use a tele-{w=0.75}{i}bone{/i}."

    return    

label joke_ocean_greeting:
    n 1fcsbg "Alright!"
    n 1fcsss "What did the ocean say to the sand?{w=0.3}{nw}"
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
    extend 1fcsem " 'cute {w=0.75}{nw}" 
    extend 1fslsl " chicks'."

    return

label joke_lumberjack_axeception:
    n 1unmaj "What would a lumberjack do if they couldn't cut down a tree?"
    n 1flrsm "..."
    n 1flrss "They'd make an...{w=1}"
    extend 1fsqbg " {i}axe{/i}{w=1.25}"
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
