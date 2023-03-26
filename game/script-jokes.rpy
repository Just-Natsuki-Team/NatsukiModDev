default persistent._jn_joke_list = dict()
default persistent._jn_daily_jokes_unlocked = False
default persistent._jn_daily_joke_given = False

image joke_book = "mod_assets/props/joke_book_held.png"

init python in jn_jokes:
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
        joke_category=jn_jokes.JNJokeCategories.neutral
    ))

    __registerJoke(JNJoke(
        label="joke_anime_bounce",
        joke_category=jn_jokes.JNJokeCategories.funny
    ))

    __registerJoke(JNJoke(
        label="joke_pirate_shower",
        joke_category=jn_jokes.JNJokeCategories.corny
    ))

    __registerJoke(JNJoke(
        label="joke_cinderella_soccer",
        joke_category=jn_jokes.JNJokeCategories.funny
    ))

    __registerJoke(JNJoke(
        label="joke_blind_fish",
        joke_category=jn_jokes.JNJokeCategories.funny
    ))

    __registerJoke(JNJoke(
        label="joke_skeleton_music",
        joke_category=jn_jokes.JNJokeCategories.neutral,
        conditional="persistent.jn_custom_music_unlocked"
    ))

    __registerJoke(JNJoke(
        label="joke_skeleton_communication",
        joke_category=jn_jokes.JNJokeCategories.neutral,
        conditional="jn_jokes.getJoke('joke_skeleton_music').shown_count > 0"
    ))

    __registerJoke(JNJoke(
        label="joke_ocean_greeting",
        joke_category=jn_jokes.JNJokeCategories.neutral
    ))

    __registerJoke(JNJoke(
        label="joke_tractor_trailer",
        joke_category=jn_jokes.JNJokeCategories.bad
    ))

    __registerJoke(JNJoke(
        label="joke_tentacle_tickles",
        joke_category=jn_jokes.JNJokeCategories.funny
    ))

label joke_clock_eating:
    n "Hey,{w=0.2} [player]..."
    n "Have {i}you{/i} ever tried eating a clock?"
    extend " No?"
    n "Well, I can't say I blame you."
    n "It's very...{w=0.5} {i}time{w=0.3} consuming{/i}.{w=0.75}{nw}"
    extend " Ehehe."

    return

label joke_anime_bounce:
    n "Listen here [player]."
    n "You know how anime gets you really bouncy and jolly,{w=0.3}{nw}"
    extend " right?"
    n "Well, it's the same for me."
    n "That's why I'm always so...{w=0.5} {i}anime-ated{/i}.{w=0.75}{nw}"
    n " Got it?{w=0.5}{nw}"
    extend " Ehehe."

    return

label joke_pirate_shower:
    n "Okay,{w=0.2} [player]..."
    n "What do {i}you{/i} think why pirates never take a shower before they walk the plank?"
    n "Well obviously...{w=0.5}{nw}"
    extend " because they just {i}wash up on shore{/i}."

    return

label joke_cinderella_soccer:
    n "Let's talk about princesses,{w=0.2} [player]!"
    n "Any idea why Cinderella was so bad at soccer?{w=0.3}"
    n "Well duh!{w=0.5}{nw}"
    extend " She kept running away from the {i}ball{/i}!{w=0.5}"

    return

label joke_blind_fish:
    n "Okay,{w=0.2} [player]..."
    n "What do you call a fish without eyes?{w=0.5}"
    n "I'll give you a hint,{w=0.5} it's not blind!{w=0.75}"
    n " It's...{w=0.5} {i}fsh{/i}.{w=0.5}{nw}"
    extend " Pffff-!{w=0.5}"

    return      

label joke_skeleton_music:
    n "As I know you like to share music with me, [player]...{w=0.3}{nw}"
    extend " I'm sure you will enjoy this one too!"
    n "So...{w=0.3}{nw}"
    extend " What do you think is a skeleton's favourite instrument?"
    n "A...{w=0.5} xylo{i}bone{/i}.{w=0.75}"

    return 

label joke_skeleton_communication:
    n "Okay,{w=0.2} [player].{w=0.3}{nw}"
    extend " I found another spooky joke for you!"
    n "How do skeletons keep in touch with each other?"
    n "Only one possible solution...{w=0.5}{nw}"
    extend " With the help of the tele{i}bone{/i}{w=0.75}!"

    return    

label joke_ocean_greeting:
    n "Ready,{w=0.2} [player]?{w=0.3}"
    n "What did the ocean say to the sand?{w=0.3}{nw}"
    extend " Any guesses?{w=0.3} It's simple."
    n "Nothing{w=0.5} - it just {iwaved.{w=0.75}"

    return  

label joke_tractor_trailer:
    n "Time to pay attention,{w=0.1} [player]!"
    n "A colleague asked me if I watched the movie 'Tractor'...{w=0.5}"
    n "I did not.{w=0.3}{nw}"
    extend " But I watched the {i}trailer{/i}...{w=0.75}"

    return     

label joke_tentacle_tickles:
    n "Hey,{w=0.2} [player]..."
    n "Can you guess how many tickles it take to make an octopus laugh?"
    n "Four?{w=0.3} Eight?{w=0.3} No!{w=0.1}{nw}"
    extend " {i}Ten{/i}-tickles!"

    return