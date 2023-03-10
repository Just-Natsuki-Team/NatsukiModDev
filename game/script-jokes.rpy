default persistent._jn_joke_list = ()
default persistent._jn_daily_jokes_unlocked
default persistent._jn_daily_joke_given = False

image joke_book = "mod_assets/props/joke_book_held.png"

init python in jn_jokes:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    __ALL_JOKES = {}

    class JNJoke:
        def __init__(
            self,
            label,
            conditional=None,
        ):
            self.label = label
            self.is_seen = False
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
                "is_seen": self.is_seen
            }

        def setSeen(self, is_seen):
            """
            Marks this joke as seen.
            """
            self.is_seen = is_seen
            self.__save()

        def __load(self):
            """
            Loads the persisted data for this joke from the persistent.
            """
            if store.persistent._jn_joke_list[self.label]:
                self.is_seen = store.persistent._jn_joke_list[self.label]["is_seen"]

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

    __registerJoke(JNDailyJoke(
        label="joke_test_joke"
    ))

    __registerJoke(JNDailyJoke(
        label="joke_test_with_condition",
        conditional="persistent.jn_total_visit_count > 30"
    ))

label joke_test_joke:
    n "This is a joke"
    n "No, really"
    n "This isn't finished"
    n "What a joke"
    n "Roflmao"

    return

label joke_test_with_condition:
    n "Some test joke w/ condition"

    return
