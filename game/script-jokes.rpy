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
        confusing = 5

    class JNJoke:
        def __init__(
            self,
            label,
            display_name,
            joke_category,
            conditional=None,
        ):
            self.label = label
            self.display_name = display_name
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
            is_seen=None,
            shown_count=None
        ):
            """
            Returns a filtered list of jokes, given a joke list and filter criteria.

            IN:
                - label - list of labels the joke must have 
                - is_seen - bool is_seen state the joke must be
                - shown_count - int number of times the joke must have been seen before

            OUT:
                - list of jokes matching the search criteria
            """
            return [
                _joke
                for _joke in joke_list
                if _joke.__filterJoke(
                    is_seen,
                    shown_count
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
            is_seen=None,
            shown_count=None
        ):
            """
            Returns True, if the joke meets the filter criteria. Otherwise False.

            IN:
                - is_seen - bool is_seen state the joke must be
                - shown_count - int number of times the joke must have been seen before

            OUT:
                - True, if the joke meets the filter criteria. Otherwise False
            """
            if is_seen is not None and not self.is_seen == is_seen:
                return False

            elif shown_count is not None and self.shown_count < shown_count: 
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

    def getUnseenJokes():
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

    def getShownBeforeJokes():
        """
        Returns a list of all jokes shown at least once previously, or None if zero that are unlocked and shown before exist.
        
        OUT:
            - List of JNJoke jokes, or None
        """
        joke_list = JNJoke.filterJokes(
            joke_list=getAllJokes(),
            shown_count=1
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
        display_name="Eating clocks",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_anime_animated",
        display_name="Anime",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_pirate_shower",
        display_name="Pirate hygiene",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_cinderella_soccer",
        display_name="Cinderella",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_blind_fish",
        display_name="Fish eyesight",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_skeleton_music",
        display_name="Skeletal music",
        joke_category=JNJokeCategories.corny,
        conditional="persistent.jn_custom_music_unlocked"
    ))
    __registerJoke(JNJoke(
        label="joke_skeleton_communication",
        display_name="Skeletal communication",
        joke_category=JNJokeCategories.corny,
        conditional="jn_jokes.getJoke('joke_skeleton_music').shown_count > 0"
    ))
    __registerJoke(JNJoke(
        label="joke_ocean_greeting",
        display_name="Ocean greetings",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_tractor_trailer",
        display_name="Tractor-trailer",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_tentacle_tickles",
        display_name="Tentacles",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_basic_chemistry",
        display_name="Basic chemistry",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_upset_cat",
        display_name="Upsetting a cat",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_cute_chicks",
        display_name="Cute chicks",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_lumberjack_axeception",
        display_name="Lumberjacks",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_tallest_building",
        display_name="Tallest building",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_baking_baseball",
        display_name="Baking and baseball",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_soya_tofu",
        display_name="Tofu",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_distrust_atoms",
        display_name="Atomic theory",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_running_latte",
        display_name="Barista",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_guitar_stringing_along",
        display_name="Guitarist",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_snek_maths",
        display_name="Snake mathematics",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_balloonist_hot_air",
        display_name="Hot air",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_author_cover_story",
        display_name="Cover story",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_wrapped_up_quickly",
        display_name="Packaging",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_carpentry_nailed_it",
        display_name="Nailed it",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_neutrons_no_charge",
        display_name="Neutrons",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_train_sound_track",
        display_name="Sound tracks",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_bored_typist",
        display_name="Typists",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_regular_moovements",
        display_name="Cows and stairs",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_rabbit_lottery",
        display_name="Rabbit lottery",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_trees_logged_out",
        display_name="Logging out",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_con_crete",
        display_name="Con-crete",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_footless_snakes",
        display_name="Measuring snakes",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_bigger_ball",
        display_name="Ball sports",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_meeting_walls",
        display_name="Meeting walls",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_hour_feeling",
        display_name="Clock and the watch",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_spotless_tigers",
        display_name="Tiger's stripes",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_missing_bell",
        display_name="No bell",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_cheesy_pizza",
        display_name="Pizza",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_veggie_mood",
        display_name="Vegetarian moods",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_scarecrow_award",
        display_name="Scarecrows",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_sundae_school",
        display_name="School",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_burned_tongue",
        display_name="Burned tongues",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_pointless_pencil",
        display_name="Pencils",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_know_the_drill",
        display_name="The drill",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_can_do_attitude",
        display_name="Cannery",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_out_of_ctrl",
        display_name="Out of control",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_dishwashing",
        display_name="Dishwashing",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_escape_artists",
        display_name="Escape artist",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_shoemakers",
        display_name="Shoemakers",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_lead_times",
        display_name="Dog walkers",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_shark_literature",
        display_name="Shark literature",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_developers_committed",
        display_name="Developers",
        joke_category=JNJokeCategories.funny
    ))
    __registerJoke(JNJoke(
        label="joke_shelved_plans",
        display_name="Plans",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_action_figures",
        display_name="Action",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_befriending_sharks",
        display_name="Befriending sharks",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_fisherman_broadcast",
        display_name="Fishermen video calls",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_lighthouse_keeper",
        display_name="Lighthouse keeper",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_bakers",
        display_name="Bakers",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_ravioli_pasta_way",
        display_name="Ravioli",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_spices",
        display_name="Spices",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_movie_theater_concessions",
        display_name="Movie theater",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_octo_puss",
        display_name="Eight-legged cat",
        joke_category=JNJokeCategories.bad
    ))
    __registerJoke(JNJoke(
        label="joke_roller_blade",
        display_name="Shaving as a skater",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_psychic_medium",
        display_name="Psychic meals",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_ex_press_delivery",
        display_name="Ex-press",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_keymakers_lockstep",
        display_name="Keymakers",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_tube_piping_hot",
        display_name="Tube cuisine",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_entomology_programming",
        display_name="Entomology",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_booked_it",
        display_name="Author pulled over",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_sheep_flock",
        display_name="Cults",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_multiple_choice",
        display_name="Multiple choice",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_horse_hairstyles",
        display_name="Horse hairstyles",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_new_heights",
        display_name="Mountain climbers",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_coffee_grind",
        display_name="Instant coffee",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_sting_operation",
        display_name="Bee theft",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_sculptors_steak_marbled",
        display_name="Sculptors",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_rhetorical",
        display_name="Rhetorical",
        joke_category=JNJokeCategories.confusing
    ))
    __registerJoke(JNJoke(
        label="joke_fuzz",
        display_name="Fuzz",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_restroom_comedian",
        display_name="Restroom comedian",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_glasses_framed",
        display_name="Eyeglasses",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_surround_sound",
        display_name="Audio technician",
        joke_category=JNJokeCategories.corny
    ))
    __registerJoke(JNJoke(
        label="joke_rose_thorns",
        display_name="Roses",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_acrobats_somersault",
        display_name="Acrobats",
        joke_category=JNJokeCategories.neutral
    ))
    __registerJoke(JNJoke(
        label="joke_frog_seating",
        display_name="Frog seating",
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
    n 1tsqsssbr "What's a skeleton's favorite instrument?"
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
    n 1fcsbg "What's a train driver's favorite thing to listen to while they're working?"
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
    extend 1unmaj " did {i}you{/i} know that there's actually a rabbit {i}lottery{/i}?"
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
    extend 1tnmfl " have {i}you{/i} ever wondered how snakes are measured?"
    n 1uwdaj "Especially with all those different sizes!"
    extend 1fsqcs " What kind of measurement would even work {i}best{/i}?"
    n 1fcsss "Well,{w=0.2} I guess you'd just be stuck with metric..."
    n 1fsqbg "...'Cause you definitely aren't using{w=0.5}{nw}"
    extend 1nchgn " {i}feet{/i}!"

    return

label joke_bigger_ball:
    n 1ullbo "You know..."
    n 1nslsssbl "I ended up visiting the school nurse the last time I played sports."
    n 1uwdaj "I wondered why the ball kept getting bigger..."
    n 1unmfl "...But then it{w=0.25}{nw}" 
    extend 1fchbgsbr " {i}hit{/i} me!"

    return

label joke_meeting_walls:
    n 1fsqfl "...What did the wall say to the other wall?"
    n 1ftlemesi "..."
    n 1fslbo "We'll meet at the{w=1}{nw}"
    extend 1fsqbo " {i}corner{/i}."

    return

label joke_hour_feeling:
    n 1fcsaj "So!{w=0.5}{nw}"
    extend 1fsqsm " How did the clock greet the watch,{w=0.2} [player]?"
    n 1fsldv "..."
    n 1fchgn "{i}Hour{/i}{w=1} you doing?"

    return

label joke_spotless_tigers:
    n 1ulraj "So,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " ever asked yourself why tigers have stripes?"
    n 1fcsss "It's not a fashion choice,{w=0.2} that's for sure..."
    n 1fsqsm "...It's because they don't want to be{w=0.5}{nw}"
    extend 1fchgn " {i}spotted{/i}!"

    return

label joke_missing_bell:
    n 1fsqsm "Knock,{w=0.2} knock,{w=0.2} [player]!"

    show natsuki 1fchsm

    menu:
        "Who's there?":
            pass

    n 1ucsaj "Nobel."

    show natsuki 1fsqcs

    menu:
        "Nobel who?":
            pass

    n 1nnmbo "{i}No-bel{/i},{w=1}{nw}"
    extend 1fchgn " so I just knocked!"

    return

label joke_cheesy_pizza:
    n 1fsqfl "...I've found a joke about pizza."
    n 1fsrfl "But...{w=0.75}{nw}"
    extend 1fcsem " ugh."
    n 1fslsl "Yeah.{w=0.3} There's no way I'm sharing something...{w=1}{nw}"
    extend 1nsqpo " {i}that cheesy{/i}."
    
    return

label joke_veggie_mood:
    n 1nslsssbl "Heh.{w=0.75}{nw}"
    extend 1fcssssbl " Let's see who {i}this{/i} reminds you of,{w=0.2} [player]."
    n 1ccsajsbl "A-{w=0.2}hem!"
    n 1tnmbo "Do you have {i}any{/i} idea when vegetarians get mood swings?"
    n 1nllss "Well...{w=0.75}{nw}"
    extend 1fcssmesm " I do."
    n 1fcsbg "...When they're out of their {i}gourd{/i},{w=0.75}{nw}"
    extend 1fchbg " obviously!"
    
    return

label joke_scarecrow_award:
    n 1fsqfl "...Why did the scarecrow get an award?"
    n 1ncsemesi "..."
    n 1fcsbo "Because..."
    n 1fsqfl "It was {i}outstanding{/i}{w=0.75}{nw}" 
    extend 1nsrca " in its field."
    
    return

label joke_sundae_school:
    n 1ullaj "You know..."
    n 1tnmbo "I've been thinking about school a bunch lately."
    n 1ulraj "I mean,{w=0.5}{nw}"
    extend 1unmfl " there were {i}so{/i} many schools I could've gone to -{w=0.5}{nw}"
    extend 1fspbg " one even did culinary classes!"
    n 1fcsan "But the schedule meant going in on a {i}weekend{/i}!{w=0.5}{nw}"
    extend 1fllwr " Who {i}does{/i} that?!"
    n 1fcsem "Ugh..."
    n 1flrfl "Talk about a...{w=1}{nw}"
    extend 1fsqss " {i}sundae{/i}{w=0.75}{nw}" 
    extend 1uchgn " school!"
    
    return

label joke_burned_tongue:
    n 1ullaj "You know,{w=0.75}{nw}"
    extend 1tnmbo " I never understood why hipsters hung around coffee shops so much."
    n 1nsrbo "Like...{w=0.3} what's so fun about sitting around sipping from a cup all day?"
    n 1nllfl "In fact,{w=0.2} only yesterday I saw one of them in a café..."
    n 1unmaj "And they kept burning their tongue!{w=0.5} Like it was on purpose or something!{w=0.75}{nw}"
    extend 1tnmss " Wondering why,{w=0.2} [player]?"
    n 1flrss "Because they drank their coffee...{w=1}{nw}"
    extend 1fchgn " {i}before it was cool{/i}!"

    return

label joke_pointless_pencil:
    n 1fllfl "Man..."
    n 1fcsem "I was {i}trying{/i} to work on my poetry,{w=0.2} and my pencil just decided to break!{w=0.75}{nw}"
    extend 1fslpo " Great."
    n 1cllaj "I was {i}going{/i} to tell a joke about it..."
    n 1tnmbo "But now?{w=0.5}{nw}"
    extend 1fsqsm " It's {i}pointless{/i}."

    return

label joke_know_the_drill:
    n 1ulraj "You know,{w=0.2} [player]..."
    n 1nsqsl "I always used to get annoyed at people doing construction work.{w=0.75}{nw}"
    extend 1fnmem " {i}Especially{/i} on the weekends!"
    n 1fllfl "Like...{w=1}{nw}"
    extend 1fcsbo " I get they have a job to do.{w=0.75}{nw}"
    extend 1fsran " But do they seriously have to start so {i}early{/i}?!{w=0.75}{nw}"
    extend 1fcsan " Yeesh!"
    n 1cslsl "..."
    n 1cslaj "But...{w=1}{nw}"
    extend 1cllca " you do get used to all the noise after a while,{w=0.2} I suppose."
    n 1cnmss "I guess eventually you just...{w=1}{nw}"
    extend 1fsqbg " {i}know the drill{/i},{w=0.75}{nw}"
    extend 1nchgn " right?"

    return

label joke_can_do_attitude:
    n 1fcsbg "Let's see how well you can {i}process{/i} this one,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsbs "So!{w=0.75}{nw}"
    extend 1tsqss " Ever wondered what it takes to land a job in a cannery?"
    n 1tsqsm "..."
    n 1fsqsm "No?{w=0.75}{nw}"
    extend 1fcsbs " Come on,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1fcssmesm " Isn't it obvious?"
    n 1fcsbg "...You just need a{w=0.5}{nw}"
    extend 1fsqbg " {i}can{/i}-do{w=1}{nw}"
    extend 1uchgn " attitude!"

    return

label joke_out_of_ctrl:
    n 1fllbo "I gotta say,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fsqfl " I'm starting to get {i}really{/i} sick of all these stories about shortages."
    n 1fnmem "Seriously -{w=0.5}{nw}"
    extend 1fcsgs " it's ridiculous!{w=0.75}{nw}"
    extend 1flrfl " Like why is it so hard to just order stuff in,{w=0.2} all of a sudden?"
    n 1fcsgs "I mean,{w=0.5}{nw}"
    extend 1fslpo " even just the other day I heard about places running out of parts for keyboards!"
    n 1fcsss "...Heh."
    n 1fcstr "I guess their management must really be{w=0.5}{nw}"
    extend 1fsqbg " out of {i}Control{/i},{w=0.75}{nw}"
    extend 1fchgn " huh?"

    return

label joke_dishwashing:
    n 1csqfl "Why isn't dishwashing considered a competitive sport?"
    n 1csrsl "..."
    n 1fcsemesi "..."
    n 1nsqfl "Because victory is handed to you...{w=1.25}{nw}" 
    extend 1cslcasbr " on a {i}plate{/i}."

    return

label joke_escape_artists:
    n 1ccsflesi "..."
    n 1cllsl "Why shouldn't you rely on an escape artist to turn up to an invitation?"
    n 1csrbosbr "..."
    n 1ccsemsbr "..."
    n 1nsrtrsbr "...Because they're always getting{w=0.5}{nw}" 
    extend 1csqcasbr " {i}tied down{/i}."

    return

label joke_shoemakers:
    n 1fllfl "Why don't shoemakers go anywhere sunny on vacation?"
    n 1fslca "..."
    n 1ccsemesi "..."
    n 1csrem "...Because they've already{w=0.5}{nw}" 
    extend 1csrsl " {i}tanned{/i}."

    return

label joke_lead_times:
    n 1ccsfl "...Alright.{w=0.75}{nw}"
    extend 1csqem " You asked for this,{w=0.2} [player]."
    n 1csqsl "Why is it so hard to land a job as a dog walker nowadays?"
    n 1cslsl "..."
    n 1ccssl "Heh."
    n 1cdlfl "...Because there's such a long{w=0.5}{nw}" 
    extend 1fslfl " {i}lead time{/i}."

    return

label joke_shark_literature:
    n 1fcsbs "Alright!{w=0.75}{nw}"
    extend 1fdwbg " How about this one,{w=0.5}{nw}" 
    extend 1fsqsm " [player]?"
    n 1fcsbg "What kind of literature do you hand a shark?"
    n 1fnmsm "..."
    n 1usqss "No?{w=0.75}{nw}"
    extend 1fsqsm " Not even a guess?"
    n 1fcssmesm "How disappointing.{w=0.75}{nw}"
    extend 1fcsbg " Isn't it obvious,{w=0.2} [player]?"
    n 1fnmss "You give them stuff they can really...{w=1}{nw}" 
    extend 1fsqbg " {i}sink their teeth into{/i},{w=0.75}{nw}" 
    extend 1fchgn " duh!"
    
    return

label joke_developers_committed:
    n 1ttrpu "You know,{w=0.2} [player]...{w=1}{nw}"
    extend 1tlraj " I've always wondered."
    n 1tsqfl "Is it hard for developers to start relationships?{w=0.75}{nw}"
    extend 1tllbo " The ones that mess around with code and all that stuff?"
    n 1tsqsl "..."
    n 1tsqfl "No?{w=0.75}{nw}"
    extend 1clrpu " Huh.{w=1}{nw}"
    extend 1csqss " You sure,{w=0.2} [player]?"
    n 1fcsss "'Cause from what I'm reading here..."
    n 1nchgn "...They always seem to be pretty {i}committed{/i} already!"

    return

label joke_shelved_plans:
    n 1ccstr "I gotta say,{w=0.2} [player].{w=0.75}{nw}"
    extend 1cslca " I'm still pretty bummed out about being stuck here and everything,{w=0.2} you know."
    n 1cllbo "..."
    n 1tnmfl "What?{w=0.75}{nw}"
    extend 1tnmbo " Didn't I tell you?"
    n 1fcsgs "I actually landed an interview for a part-time job after school at a bookstore!{w=0.75}{nw}"
    extend 1fcspo " I applied online and everything!"
    n 1knmfl "...But how am I supposed to get there now?"
    n 1ccsemesi "Ugh..."
    n 1nsrpo "..."
    n 1ncsaj "Well."
    n 1tllss "I guess those plans are gonna have to be{w=0.5}{nw}"
    extend 1fsqbg " {i}shelved{/i}{w=0.75}{nw}"
    extend 1nchgn " after all,{w=0.2} huh?"

    return

label joke_action_figures:
    n 1fsrem "...Seriously can't believe I'm telling {i}this{/i} one.{w=0.75}{nw}"
    extend 1ccsem " Ugh."
    n 1ccstresi "..."
    n 1nsqsl "What kind of gift do movie directors love the most?"
    n 1fllbosbr "..."
    n 1fcsflsbr "...{i}Action{/i}{w=0.75}{nw}"
    extend 1fsqflsbr " figures."

    return

label joke_befriending_sharks:
    n 1ccsss "Heh.{w=0.75}{nw}"
    extend 1fsqss " You ready,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fnmbg " You're gonna be like a fish out of water after this one."
    n 1fcsaj "So!{w=0.75}{nw}"
    extend 1fcsbg " How do you go about making friends with a shark?"
    n 1fsqsm "..."
    n 1fsqss "No?{w=0.75}{nw}"
    extend 1flrss " Wow,{w=0.2} [player]..."
    n 1fsgbg "Isn't it obvious?"
    n 1fllss "You just gotta{w=0.75}{nw}"
    extend 1fsqbg " {i}chum{/i}{w=0.75}{nw}"
    extend 1nchgn " them up first!"

    return

label joke_fisherman_broadcast:
    n 1csqfl "...Why is it so hard to get a video call with a fisherman?"
    n 1csrca "..."
    n 1ccspuesi "..."
    n 1clrem "...Because they only do broad-{w=0.75}{nw}"
    extend 1csqup "{i}casts{/i}."

    return

label joke_lighthouse_keeper:
    n 1fsrpu "I seriously can't believe I'm telling {i}this{/i} one."
    n 1ccsbo "..."
    n 1cllfl "What happens when a lighthouse keeper gets promoted?"
    n 1cllslsbr "..."
    n 1ccsemesisbr "..."
    n 1ccsajsbr "Their career becomes...{w=1}{nw}"
    extend 1csrflsbr " {i}brighter than ever{/i}."

    return

label joke_bakers:
    n 1ccsemesi "..."
    n 1clrtr "How do you describe a baker about to break their own baking record?"
    n 1csrsl "..."
    n 1ccsflsbl "...Man,{w=0.5}{nw}" 
    extend 1fslemsbl " this is dumb."
    n 1cllajsbl "They'd be...{w=1}{nw}"
    extend 1csqemsbl " {i}on a roll{/i}."

    return

label joke_ravioli_pasta_way:
    n 1cslflsbr "...I can't {i}believe{/i} I'm reading this one out.{w=0.75}{nw}"
    extend 1ccsslsbr " Yeesh."
    n 1csrbo "..."
    n 1clrfl "Did you hear about the chef who just couldn't lay off the ravioli?"
    n 1cnmsl "..."
    n 1ccsemesi "..."
    n 1cllfl "They...{w=1}{nw}"
    extend 1csqup " {i}pasta{/i}{w=0.75}{nw}"
    extend 1csrsl " way."
    
    return

label joke_spices:
    n 1csqbg "'Kay.{w=0.75}{nw}"
    extend 1fcsbs " So!"
    n 1unmss "When would a chef start adding extra paprika and chili powder to a dish you ordered?"
    n 1cnmsm "..."
    n 1csqss "No?{w=0.75}{nw}"
    extend 1fcsaj " Come on,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1fnmbg " Even {i}you{/i} should have nailed this one!"
    n 1fcsbg "...When they want to{w=0.5}{nw}"
    extend 1fsqss " {i}spice{/i}{w=0.75}{nw}"
    extend 1fchbs " up your life,{w=0.5}{nw}" 
    extend 1nchgn " of course!"

    return

label joke_movie_theater_concessions:
    n 1tllfl "Hey,{w=0.5}{nw}"
    extend 1tnmaj " [player] -{w=0.5}{nw}"
    extend 1unmaj " did you hear about the movie theater that got shut down recently?"
    n 1csrem "Talk about a bummer!{w=0.75}{nw}"
    extend 1unmem " Seriously -{w=0.5}{nw}" 
    extend 1fllem " the owners had to completely sell up and everything!"
    n 1ccsfl "Apparently they just couldn't come to a decent arrangement with all their costs and licensing stuff."
    n 1csrss "Heh."
    n 1ccsss "I guess you could say...{w=1}{nw}"
    extend 1fchgn " they just didn't make enough {i}concessions{/i}!"

    return

label joke_octo_puss:
    n 1ccsfl "Ugh...{w=1}{nw}"
    extend 1clrfll " this one just sounds mean.{w=0.75}{nw}"
    extend 1fsrsll " Gross."
    n 1ccspuesi "..."
    n 1cllfl "What do you call a cat born with double the amount of legs?"
    n 1cllsl "..."
    n 1fslsl "..."
    n 1fcsfl "...An octo-{w=0.75}{nw}"
    extend 1fsrbo "{i}puss{/i}."
    
    return

label joke_roller_blade:
    n 1fcsbg "Let's see how much this one {i}grinds{/i} you,{w=0.5}{nw}" 
    extend 1fsqbg " [player]!"
    n 1fcsaj "So!{w=0.75}{nw}"
    extend 1unmaj " What does a professional skater use for a clean shave?"
    n 1tsqsm "..."
    n 1tsqss "No?{w=0.75}{nw}"
    extend 1fsqbg " Not even a guess?{w=0.75}{nw}"
    extend 1fsgsm " Ehehe."
    n 1fcsbs "Easy!"
    n 1ullbg "They'd use a roller-{w=0.75}{nw}"
    extend 1uchbg " {i}blade{/i}!{w=0.75}{nw}"
    extend 1fchgn " Duh!"

    return

label joke_psychic_medium:
    n 1fcsgs "Right!{w=0.75}{nw}"
    extend 1fsqbg " Here's a {i}reading{/i} for you,{w=0.5}{nw}" 
    extend 1fsgsm " [player]!"
    n 1ccsbg "What kind of meal size would a psychic order?"
    n 1csqcs "..."
    n 1fsgsmeme "Ehehe."
    n 1fcsbs "...They'd get a {i}medium{/i},{w=0.75}{nw}"
    extend 1fchbg " obviously!"

    return

label joke_ex_press_delivery:
    n 1nlraj "By the way,{w=0.2} [player] -{w=0.5}{nw}"
    extend 1unmfl " did you hear about the newspaper that shut down recently?"
    n 1fllfl "They barely even gave notice.{w=0.75}{nw}"
    extend 1fsgem " So everyone just had to pack up and find new jobs immediately!{w=0.75}{nw}"
    extend 1fcsfl " What a joke."
    n 1cnmaj "A couple even ended up going into courier work!"
    n 1ncsss "...Heh."
    n 1clrsssbl "I guess you could say they specialize in...{w=1}{nw}"
    extend 1fsqbg " {i}ex-press{/i}{w=0.75}{nw}"
    extend 1fchgn " deliveries!"
    
    return

label joke_keymakers_lockstep:
    n 1ccsemesi "..."
    n 1ctrfl "...How do keymakers and their colleagues walk around at work?"
    n 1csrslsbr "..."
    n 1csqfl "...In lock-{w=0.75}{nw}" 
    extend 1cslup "step."
    
    return

label joke_tube_piping_hot:
    n 1ccsbg "Let's see if this one's your flavor,{w=0.5}{nw}" 
    extend 1fsgsm " [player]."
    n 1fcsbg "Can you eat food someone prepared inside a tube?"
    n 1fsqsm "..."
    n 1ullbg "Well,{w=0.2} yeah!{w=0.75}{nw}"
    extend 1fchbg " Sure you can!"
    n 1flrss "It's just gotta be served{w=0.5}{nw}"
    extend 1fsgbg " {i}piping{/i}{w=0.75}{nw}"
    extend 1fchbg " hot,{w=0.5}{nw}" 
    extend 1fchsmeme " that's all!"

    return

label joke_entomology_programming:
    n 1fnmbg "Okay!{w=0.75}{nw}"
    extend 1fcsbg " Why did the entomologist think about taking up programming?"
    n 1fnmsm "..."
    n 1tllss "Well,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1tsgss " Isn't it obvious?"
    n 1nchgn "'Cause they heard they'd be constantly finding {i}bugs{/i}!"
    
    return

label joke_booked_it:
    n 1fcsbg "Alright!{w=0.75}{nw}"
    extend 1fnmbg " Let's see if you can paper-{w=0.75}{nw}"
    extend 1fsgss "{i}back{/i}{w=0.5}{nw}"
    extend 1fcssmesm " this one,{w=0.2} [player]."
    n 1fcsaj "So!"
    n 1unmfl "Did you hear about that famous author the police pulled over the other day?"
    n 1tnmsl "..."
    n 1csqsm "No?"
    n 1ccsss "Heh.{w=0.75}{nw}"
    extend 1flrbg " Can't say I'm surprised."
    n 1fchbg "...'Cause he {i}booked{/i} it,{w=0.75}{nw}" 
    extend 1fchgnelg " obviously!"
    
    return

label joke_sheep_flock:
    n 1fcsfl "Ugh..."
    n 1fsrca "Whoever added this one {i}definitely{/i} had wool between their ears.{w=0.75}{nw}"
    extend 1fsraj " That's all I'm saying."
    n 1fcsflesi "..."
    n 1cllbo "Whatever.{w=0.75}{nw}"
    extend 1cnmfl " Why are sheep the best at starting a cult?"
    n 1clrsl "..."
    n 1csrsl "..."
    n 1csqfl "...Because they already have a{w=0.5}{nw}"
    extend 1cslem " {i}flock{/i}."

    return

label joke_multiple_choice:
    n 1ccsbg "Let me{w=0.5}{nw}" 
    extend 1csqbg " {i}quiz{/i}{w=0.5}{nw}" 
    extend 1fsqsm " you on this one,{w=0.2} [player]."
    n 1fcsbg "Alright!"
    n 1unmaj "So,{w=0.2} why are multiple choice exams the worst way you can test someone?"
    n 1tsgsm "..."
    n 1csgss "Really?"
    n 1csqbg "Not even a guess,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fsqsm " Ehehe."
    n 1fcsbg "Easy -{w=0.5}{nw}"
    extend 1fchgnelg " 'cause it's just a {i}box-ticking exercise{/i}!"

    return

label joke_horse_hairstyles:
    n 1ccsem "I seriously can't believe {i}this{/i} is the one I gotta read out.{w=0.75}{nw}"
    extend 1csrsl " Ugh."
    n 1ccsflesi "..."
    n 1csqfl "What kind of hairstyle should you never give to a horse?"
    n 1csqsl "..."
    n 1csrbo "..."
    n 1csrem "...A {i}pony{/i}{w=0.5}{nw}"
    extend 1csqem "-tail."

    return

label joke_new_heights:
    n 1csqaj "What happens when a mountain climber gets a promotion?"
    n 1cslsl "..."
    n 1ccsflesi "Ugh..."
    n 1cllpu "...They reach{w=0.75}{nw}"
    extend 1csqem " {i}new heights{/i}."

    return

label joke_coffee_grind:
    n 1ccsbg "Let's see how you{w=0.5}{nw}"
    extend 1csgbg " {i}take{/i}{w=0.5}{nw}"
    extend 1fnmbg " this one,{w=0.5}{nw}"
    extend 1fsqsm " [player]!"
    n 1fcsgs "So!{w=0.75}{nw}"
    extend 1fnmss " Why did the barista finally start offering instant coffee?"
    n 1fsqsm "..."
    n 1fcsss "Heh."
    n 1flrbs "'Cause they were sick of the {i}grind{/i},{w=0.75}{nw}"
    extend 1fchgnelg " of course!"

    return

label joke_sting_operation:
    n 1clraj "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmsl " did you hear about all the thefts targeting beekeepers recently?"
    n 1ccsfl "I mean,{w=0.5}{nw}"
    extend 1fcswr " come on!{w=0.75}{nw}"
    extend 1fsqem " {i}Bees{/i}?{w=0.75}{nw}"
    extend 1fllem " How low could you {i}possibly{/i} get?"
    n 1fllpu "Though...{w=1}{nw}"
    extend 1cllbo " I gotta admit.{w=0.75}{nw}" 
    extend 1unmfl " How they caught them in the end?"
    n 1ccsss "Heh."
    n 1ccsbg "Now that's what I call a{w=0.5}{nw}" 
    extend 1fsqbg " {i}sting{/i}{w=0.75}{nw}"
    extend 1fchgn " operation!"
    
    return

label joke_sculptors_steak_marbled:
    n 1fcsbg "'Kay!{w=0.75}{nw}"
    extend 1fsqbg " So,{w=0.2} [player]..."
    n 1fsgss "How do sculptors prefer their steaks?"
    n 1fsgsm "..."
    n 1tsqbg "No?{w=0.75}{nw}"
    extend 1fcssmesm " Come on,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1tlrbg " Isn't it obvious?"
    n 1tsgbg "...With plenty of{w=0.5}{nw}"
    extend 1fsqbg " {i}marbling{/i},{w=0.75}{nw}"
    extend 1fchbs " duh!"

    return

label joke_rhetorical:
    n 1ccsaj "...So."
    n 1cdwpu "...What do you get if you cross a joke{w=0.5}{nw}"
    extend 1tsqsl " with a rhetorical question?"
    
    return

label joke_fuzz:
    n 1ccsflesi "...Man,{w=0.2} this is dumb.{w=0.75}{nw}"
    extend 1csrsl " Fine."
    n 1ccsaj "Who do you call for someone who only steals wool,{w=0.2} yarn,{w=0.2} and fluffy socks?"
    n 1cnmbo "..."
    n 1cllbo "..."
    n 1cnmfl "...The{w=0.5}{nw}" 
    extend 1cslfl " {i}fuzz{/i}."

    return

label joke_restroom_comedian:
    n 1ccsemesi "..."
    n 1clrbo "Why did the comedian insist on warming up his act in the restroom?"
    n 1csqbo "..."
    n 1cslfl "...I can't believe I'm saying this."
    n 1ccsfl "So he always had jokes...{w=1}{nw}"
    extend 1csqpo " {i}on tap{/i}."

    return

label joke_glasses_framed:
    n 1fsqbg "Let's see how you handle this one.{w=0.75}{nw}"
    extend 1fcsaj " So!"
    n 1csqbg "How does someone with glasses react to being told bad news?"
    n 1csqsm "..."
    n 1fsqss "Heh.{w=0.75}{nw}"
    extend 1csgbg " Don't you know,{w=0.2} [player]?"
    n 1flrss "It all depends on how you{w=0.5}{nw}"
    extend 1fsqbg " {i}frame{/i}{w=0.5}{nw}"
    extend 1fchbs " the situation!"

    return

label joke_surround_sound:
    n 1csqflsbl "Don't say I didn't warn you,{w=0.2} [player]."
    n 1ccsfl "How do audio technicians get over feeling lonely?"
    n 1csrca "..."
    n 1ccsem "Ugh."
    n 1cllem "They use...{w=1}{nw}"
    extend 1cnmfl " {i}surround{/i}{w=0.5}{nw}"
    extend 1csqfl " {i}sound{/i}."

    return

label joke_rose_thorns:
    n 1ccsss "You better{w=0.5}{nw}"
    extend 1csgbg " {i}prick{/i}{w=0.5}{nw}"
    extend 1fnmbg " your ears for this one!"
    n 1fcsaj "'Kay!{w=0.75}{nw}"
    extend 1fcssm " So."
    n 1tsqbg "Why did the gardener give up on planting roses?"
    n 1fnmsm "..."
    n 1ccssmesm "Heh."
    n 1clrbg "'Cause they were turning out to be a real{w=0.5}{nw}"
    extend 1csqbg " {i}thorn{/i}{w=0.75}{nw}" 
    extend 1fchbs " in his side!"

    return

label joke_acrobats_somersault:
    n 1ccssmesm "Heh.{w=0.75}{nw}"
    extend  1fsqbg " Riddle me this,{w=0.2} [player]!"
    n 1fcsbg "What kind of move do acrobats practice most in the middle of the year?"
    n 1fnmsm "..."
    n 1fcsbs "Duh!"
    n 1fsqbg "They'd practice{w=0.5}{nw}"
    extend 1fsgbg " {i}summer{/i}{w=0.75}{nw}"
    extend 1fchbg " -saults,{w=0.5}{nw}"
    extend 1fchgn " of course!"

    return

label joke_frog_seating:
    n 1cslem "Who did they annoy to have to include {i}this{/i} one?{w=0.75}{nw}"
    extend 1ccsem " Ugh."
    n 1clrsl "What kind of seating do you set out for a frog?"
    n 1csrsl "..."
    n 1ccsflesi "..."
    n 1cllfl "A {i}toad{/i}-{w=0.75}{nw}"
    extend 1fsqca " stool."

    return
