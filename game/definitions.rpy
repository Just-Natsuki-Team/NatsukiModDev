default persistent.playername = ""
default player = persistent.playername

# Generic data
default persistent.jn_total_visit_count = 0
default persistent.jn_first_visited_date = datetime.datetime.now()
default persistent.jn_last_visited_date = datetime.datetime.now()
default persistent._jn_player_tt_state = 0
default persistent._jn_player_tt_instances = 0

#Our main topic pool
default persistent._event_list = list()

#Early imports
init -990 python:
    import datetime
    import easter
    _easter = easter.easter(datetime.datetime.today().year)

    # zorder constants; use these in place of hard-coded values!
    # Remember that higher zorder values are displayed closer to the player!
    JN_GLITCH_ZORDER = 99
    JN_BLACK_ZORDER = 10
    JN_OVERLAY_ZORDER = 5
    JN_PROP_ZORDER = 4
    JN_NATSUKI_ZORDER = 3
    JN_DECO_ZORDER = 2
    JN_LOCATION_ZORDER = 1

define JN_NEW_YEARS_DAY = datetime.date(datetime.date.today().year, 1, 1)
define JN_VALENTINES_DAY = datetime.date(datetime.date.today().year, 2, 14)
define JN_EASTER = datetime.date(_easter.year, _easter.month, _easter.day)
define JN_NATSUKI_BIRTHDAY = datetime.date(datetime.date.today().year, 5, 1)
define JN_HALLOWEEN = datetime.date(datetime.date.today().year, 10, 31)
define JN_CHRISTMAS_EVE = datetime.date(datetime.date.today().year, 12, 24)
define JN_CHRISTMAS_DAY = datetime.date(datetime.date.today().year, 12, 25)
define JN_NEW_YEARS_EVE = datetime.date(datetime.date.today().year, 12, 31)

init -3 python:
    from collections import OrderedDict
    import datetime
    from Enum import Enum
    import re
    import store.jn_affinity as jn_affinity
    import store.jn_utils as jn_utils
    import webbrowser

    class JNTimeBlocks(Enum):
        early_morning = 1
        mid_morning = 2
        late_morning = 3
        afternoon = 4
        evening = 5
        night = 6

        def __str__(self):
            return self.name

    #Constants for types. Add more here if we need more organizational areas
    TOPIC_TYPE_FAREWELL = "FAREWELL"
    TOPIC_TYPE_GREETING = "GREETING"
    TOPIC_TYPE_NORMAL = "NORMAL"
    TOPIC_TYPE_ADMISSION = "ADMISSION"
    TOPIC_TYPE_COMPLIMENT = "COMPLIMENT"
    TOPIC_TYPE_APOLOGY = "APOLOGY"
    TOPIC_TYPE_EVENT = "EVENT"

    TOPIC_LOCKED_PROP_BASE_MAP = {
        #Things which shouldn't change
        "conditional": True,
        "unlocked": True,
        "nat_says": True,
        "player_says": True,
        "shown_count": True,
        "last_seen": True,
        "unlocked_on": True,

        #Things which can change
        "label": False, #NOTE: even if this isn't saved, we need to iter it
        "affinity_range": False,
        "trust_range": False,
        "category": False,
        "prompt": False,
        "location": False,
        "additional_properties": False
    }

    class Topic(object):
        """
        Topic class. Manages all topics

        PROPERTIES:
            - label: renpy label this topic corresponds to
            - prompt: prompt for this topic in menus
            - category: how to categorize this topic
            - unlocked: whether we show this topic to the user in menus or not
            - location: whether or not this topic is bound to a location or not. If bound, then the value will be a string representing the location
            - shown_count: amount of times the user has seen this topic
            - last_seen: datetime.datetime representing the time the user last saw this topic
            - unlocked_on: datetime.datetime representing when the user unlocked this topic
            - additional_properties: extra properties which don't directly affect the topic
        """

        def __init__(
            self,
            persistent_db,
            label,
            prompt="",
            conditional=None,
            category=None,
            unlocked=False,
            nat_says=False,
            player_says=False,
            affinity_range=None,
            trust_range=None,
            location=None,
            additional_properties=None
        ):
            """
            Topic constructor

            IN:
                persistent_db - persistent dict reference to store the topic data in
                label - renpy label (as string) this topic corresponds to
                prompt - string representing the prompt to use for this topic in menus
                    (Default: '')
                conditional - condition under which this topic should be allowed to be shown
                    (Default: None)
                category - list of strings representing categories to group this topic under. If None, an empty list is assigned
                    (Default: None)
                unlocked - whether or not this topic is displayed to the user in menus
                    (Default: False)
                nat_says - whether or not this topic will be brought up by Natsuki
                    (Default: False)
                player_says - whether ot not this topic is to be prompted by the player
                    (Default: False)
                location - location this topic is bound to. If None, it can be shown in all locations
                    (Default: None)
                additional_properties - dictionary representing additional properties which don't directly affect the topic itself. If None, an empty dict is assigned
                    (Default: None)
            """
            #First, verify that we're actually using a dict here. Cannot have other types
            if not isinstance(persistent_db, dict):
                raise Exception("Persistent database provided is not of type dict")

            #Store the internal reference to its data db
            self.__persistent_db = persistent_db

            #Verify the label is legal
            if not renpy.has_label(label):
                raise Exception("Label {0} does not exist.".format(label))

            #Validate the affinity range prior to it
            if not jn_affinity._isAffRangeValid(affinity_range):
                raise Exception("Affinity range: {0} is invalid.".format(affinity_range))

            #First, we'll add all of the items here which which shouldn't change from the persisted data
            self.label = label
            self.conditional = conditional
            self.unlocked = unlocked
            self.nat_says = nat_says
            self.player_says = player_says
            self.affinity_range = affinity_range
            self.trust_range = trust_range

            #Some extra properties for internal use
            self.shown_count = 0
            self.last_seen = None
            self.unlocked_on = None

            #Now, if it's in the db, we should load its data
            if label in persistent_db:
                self.__load()

            #Next, we'll handle properties which can change
            if category is None:
                category = list()

            self.category = category
            self.prompt = prompt
            self.location = location

            if additional_properties is None:
                additional_properties = list()

            self.additional_properties = additional_properties

            #And finally, add this all back to the persistent dict
            persistent_db[label] = dict()
            self.__save()

        def __eq__(self, other):
            """
            Equals override for the Topic class

            Checks if the labels are equivalent, as otherwise, loading data should be from the same persistent key

            IN:
                other - comparitor

            OUT:
                boolean:
                    - True if the topic labels are the same
                    - False otherwise
            """
            if isinstance(other, Topic):
                return self.label == other.label
            return False

        def __repr__(self):
            """
            repr override
            """
            return "<Topic object (label '{0}' at {1})>".format(self.label, hex(id(self)))

        def as_dict(self):
            """
            Exports a dict representation of the data to be persisted

            OUT:
                dictionary representation of the topic object (excluding the persistent_db property)
            """
            return {
                key:value
                for key, value in self.__dict__.items()
                if key != "_m1_definitions__persistent_db"
            }

        def check_conditional(self):
            """
            Evaluates the topic's conditional
            """
            if self.conditional is not None:
                try:
                    return eval(self.conditional, globals=store.__dict__)

                except Exception as e:
                    store.jn_utils.log("Error evaluating conditional on topic '{0}'. {1}".format(self.label, e.message), jn_utils.SEVERITY_ERR)
                    return False

            return True

        def curr_affinity_in_affinity_range(self, affinity_state=None):
            """
            Checks if the current affinity is within this topic's affinity_range

            IN:
                affinity_state - Affinity state to test if the topic can be shown in. If None, the current affinity state is used.
                    (Default: None)
            OUT:
                True if the current affinity is within range. False otherwise
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()

            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)

        def __load(self):
            """
            Internal load funtion

            NOTE: Will raise a KeyError of the lock map doesn't have the persist key in it
            """
            for persist_key, value in self.__persistent_db[self.label].iteritems():
                if TOPIC_LOCKED_PROP_BASE_MAP[persist_key]:
                    self.__dict__[persist_key] = value

        def __save(self):
            """
            Saves this topic object to persistent

            NOTE: Will raise a KeyError of the lock map doesn't have the persist key in it
            """
            for persist_key, value in self.as_dict().items():
                if TOPIC_LOCKED_PROP_BASE_MAP[persist_key]:
                    self.__persistent_db[self.label][persist_key] = value

        @staticmethod
        def _save_topic_data():
            """
            Saves all topics
            """
            for topic in store.topic_handler.ALL_TOPIC_MAP.values():
                topic.__save()

        def has_additional_property_with_value(self, property_key, property_value):
            """
            Returns whether this topic has a given additional_attribute key with
            the supplied value

            IN:
                self - Reference to this topic
                property_key - The key under additional_properties to test against
                property_value - The value to test the value under the property_key

            OUT:
                True if the property exists and matches the given value, otherwise False, or raises an Exception if missing/undefined
            """
            if property_key not in self.additional_properties:
                return False

            return self.additional_properties[property_key] is property_value

        def derandom(self):
            """
                makes topic unable to be randomly brought up by Nat
                also makes it available through talk_menu
            """
            self.nat_says = False
            self.player_says = True

        def lock(self):
            """
            Locks this topic, so it cannot be selected or brought up in random dialogue.
            """
            self.unlocked = False
            self.__save()

        def unlock(self):
            """
            Unlocks this topic.
            """
            self.unlocked = True
            self.__save()

        def _filter_topic(
            self,
            unlocked=None,
            nat_says=None,
            player_says=None,
            is_seen=None,
            location=None,
            affinity=None,
            trust=None,
            shown_count=None,
            includes_categories=list(),
            excludes_categories=list(),
            additional_properties=list()
        ):
            """
            Filters this topic accordng to conditions

            IN:
                unlocked - boolean: Whether or not this topic is unlocked
                nat_says - boolean: Whether or not this topic is something Nat says
                player_says - boolean: Whether or not this topic is something the Player says
                is_seen - boolean: Whether or not this topic should be seen
                location - string: The location this topic should be visible in
                affinity - integer: An affinity state to check whether or not the topic can be shown
                trust - integer: A trust state to check whether or not the topic can be shown
                includes_categories - list: A list of categories, all of which this topic MUST have
                excludes_categories - list: A list of categories, none of which this topic should have
                additional_properties - list: A list of additional properties, can be either string or tuple
                    If tuple, the first item is the key, the second is the expected value. If just string, only presence is validated

                NOTE: If these values are None or empty, checks on them are not performed.

            OUT:
                boolean - True if all checks pass, False otherwise
            """
            if unlocked is not None and unlocked != self.unlocked:
                return False

            if nat_says is not None and nat_says != self.nat_says:
                return False

            if player_says is not None and player_says != self.player_says:
                return False

            if is_seen is not None and renpy.seen_label(self.label) != is_seen:
                return False

            if location is not None and location != self.location:
                return False

            if affinity and not self.curr_affinity_in_affinity_range(affinity):
                return False

            if trust and not self.evaluate_trust_range(trust):
                return False

            if not self.check_conditional():
                return False

            if shown_count is not None and self.shown_count == shown_count:
                return False

            if includes_categories and len(set(includes_categories).intersection(set(self.category))) != len(includes_categories):
                return False

            if excludes_categories and self.category and len(set(excludes_categories).intersection(set(self.category))) > 0:
                return False

            if additional_properties:
                for additional_prop in additional_properties:
                    #Key and value checks
                    if isinstance(additional_prop, tuple):
                        if not self.has_additional_property_with_value(*additional_prop):
                            return False

                    #Just key checks
                    else:
                        if additional_prop not in self.additional_properties:
                            return False

            #All checks pass
            return True

        @staticmethod
        def filter_topics(
            topic_list,
            unlocked=None,
            nat_says=None,
            player_says=None,
            is_seen=None,
            location=None,
            affinity=None,
            trust=None,
            shown_count=None,
            includes_categories=list(),
            excludes_categories=list(),
            additional_properties=list()
        ):
            """
            Filters this topic accordng to conditions

            IN:
                topic_list - List of topics to filter down

                See _filter_topic for the rest of the properties

                NOTE: If these values are None or empty, checks on them are not performed.

            OUT:
                List of topics matching the filter criteria
            """
            return [
                _topic
                for _topic in topic_list
                if _topic._filter_topic(
                    unlocked,
                    nat_says,
                    player_says,
                    is_seen,
                    location,
                    affinity,
                    trust,
                    shown_count,
                    includes_categories,
                    excludes_categories,
                    additional_properties
                )
            ]

    #Now we'll start with generic functions which we'll use at higher inits
    def registerTopic(Topic, topic_group=TOPIC_TYPE_NORMAL):
        """
        Registers a topic to the maps to allow it to be picked from the topic delegate.

        IN:
            Topic - Topic object representing the topic to be added
            topic_group - group to map this topic to
                (Default: TOPIC_TYPE_NORMAL (in other words, a standard topic, not greeting/farewell/special))

        NOTE: Should be used at init 5
        """
        local_map = store.topic_handler.TOPIC_CODE_MAP.get(topic_group)

        if local_map is None:
            raise Exception("Topic type '{0}' is not a registered map.")

        elif not isinstance(local_map, dict):
            raise Exception("Topic map for type '{0}' is not a dict.")

        #Now that type-checks are done, let's add this to the map
        local_map[Topic.label] = Topic

    def push(topic_label):
        """
        Pushes a topic to the topic stack, adding it to the front of the list

        IN:
            topic_label - Topic.label of the topic you wish to push
        """
        persistent._event_list.insert(0, topic_label)

    def queue(topic_label):
        """
        Queues a topic to the topic stack, adding it to the back of the list

        IN:
            topic_label - Topic.label of the topic you wish to queue
        """
        persistent._event_list.append(topic_label)

    def jn_topic_in_event_list(topic_label):
        """
        Returns whether or not a topic is in the event list

        IN:
            topic_label - Topic.label of the topic you wish to check

        OUT:
            boolean - True if the topic is in the event list, False otherwise
        """
        return topic_label in persistent._event_list

    def jn_topic_in_event_list_pattern(topic_pattern):
        """
        Returns whether or not a topic is in the event list

        IN:
            topic_pattern - Pattern to match against the topic labels

        OUT:
            boolean - True if the topic is in the event list, False otherwise
        """
        return any(
            re.match(topic_pattern, topic_label)
            for topic_label in persistent._event_list
        )

    def jn_rm_topic_occurrence_from_event_list(topic_label):
        """
        Removes a single occurrence of a topic from the event list

        IN:
            topic_label - label of the topic you wish to remove
        """
        if topic_label in persistent._event_list:
            persistent._event_list.remove(topic_label)

    def jn_rm_topic_from_event_list(topic_label):
        """
        Removes all occurrences of a topic from the event list

        IN:
            topic_label - label of the topic you wish to remove
        """
        persistent._event_list = [
            _topic_label
            for _topic_label in persistent._event_list
            if _topic_label != topic_label
        ]

    def jn_rm_topic_from_event_list_pattern(topic_label_pattern):
        """
        Removes all occurrences of a topic from the event list

        IN:
            topic_label_pattern - regex identifier of the topic you wish to remove
        """
        persistent._event_list = [
            _topic_label
            for _topic_label in persistent._event_list
            if not re.match(topic_label_pattern, _topic_label)
        ]

    def menu_list(menu_topics, additional_topics):
        """
        Returns a list of items ready for a menu

        IN:
            menu_topics - List<Topic> of topics
            additional_topics - optional, array of tuples
                syntax: [("prompt1", "label2"), ("prompt2", "label2"), ...]
        OUT:
            array of tuples usable by menu()
        """
        menu_items = []
        for topic in menu_topics:
            menu_items.append((topic.prompt, topic.label))

        for topic in additional_topics:
            menu_items.append(topic)
        return menu_items.sort()

    def menu_dict(menu_topics):
        """
        Builds a dict of items ready for use in a categorized menu

        IN:
            menu_topics - A List<Topic> of topics to populate the menu

        OUT:
            Dictionary<string, List<string>> representing a dict of category: [ ...prompts ]
        """
        # Python doesn't support ordered dictionaries... we have to do things the hard way here.

        # Get the topic categories that the given topics share, and order them
        topic_categories = []
        for topic in menu_topics:
            for category in topic.category:
                if category not in topic_categories:
                    topic_categories.append(category)
        topic_categories.sort()

        # Set up an ordered dictionaty, this will retain the order of what we return for the menu items
        ordered_menu_items = OrderedDict()
        for topic_category in topic_categories:
            ordered_menu_items[topic_category] = []

        # Feed the topics into the ordered dictionary - remember that each topic can have multiple categories!
        for topic in menu_topics:
            for category in topic.category:
                ordered_menu_items[category].append(topic)

        return ordered_menu_items

    def jnNoDismissDialogue(event, interact=True, **kwargs):
        """
        Callback for whenever Natsuki talks.
        """
        if event == "show" or event == "begin":
            # Prevent skip before dialogue
            global allow_dismiss
            allow_dismiss = False

        elif event == "slow_done":
            # Allow skip after dialogue
            global allow_dismiss
            allow_dismiss = True

    def jnClickToContinue(silent=True):
        """
        Requires the player to click to advance the game for a given step.
        If Auto is enabled, it is disabled until the player clicks to advance, then reenabled.

        IN:
            - silent - If False, plays a notification sound on click. Defaults to True.
        """
        global allow_dismiss
        global _dismiss_pause

        allow_dismiss = True
        _dismiss_pause = True

        pre_click_afm = preferences.afm_enable
        preferences.afm_enable = False

        renpy.pause()
        _dismiss_pause = False
        preferences.afm_enable = pre_click_afm

        if not silent:
            if jn_is_day():
                renpy.play("mod_assets/buttons/sounds/button_click_day.ogg")
            
            else:
                renpy.play("mod_assets/buttons/sounds/button_click_night.ogg")

    def jnIsNewYearsDay(input_date=None):
        """
        Returns True if the input_date is New Year's Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_NEW_YEARS_DAY.day and input_date.month == store.JN_NEW_YEARS_DAY.month

    def jnIsValentinesDay(input_date=None):
        """
        Returns True if the input_date is Valentine's Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_VALENTINES_DAY.day and input_date.month == store.JN_VALENTINES_DAY.month

    def jnIsEaster(input_date=None):
        """
        Returns True if the input_date is Easter; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_EASTER.day and input_date.month == store.JN_EASTER.month

    def jnIsHalloween(input_date=None):
        """
        Returns True if the input_date is Halloween; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_HALLOWEEN.day and input_date.month == store.JN_HALLOWEEN.month

    def jnIsChristmasEve(input_date=None):
        """
        Returns True if the input_date is Christmas Eve; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_CHRISTMAS_EVE.day and input_date.month == store.JN_CHRISTMAS_EVE.month

    def jnIsChristmasDay(input_date=None):
        """
        Returns True if the input_date is Christmas Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_CHRISTMAS_DAY.day and input_date.month == store.JN_CHRISTMAS_DAY.month

    def jnIsNewYearsEve(input_date=None):
        """
        Returns True if the input_date is New Year's Eve; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_NEW_YEARS_EVE.day and input_date.month == store.JN_NEW_YEARS_EVE.month

    def jnIsNatsukiBirthday(input_date=None):
        """
        Returns True if the input_date is Natsuki's birthday; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date.day == store.JN_NATSUKI_BIRTHDAY.day and input_date.month == store.JN_NATSUKI_BIRTHDAY.month

    def jnIsPlayerBirthday(input_date=None):
        """
        Returns True if the input_date is the player's birthday; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if not store.persistent._jn_player_birthday_day_month:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        if (
            ((input_date.year % 4 == 0 and input_date.year % 100 != 0) or (input_date.year % 400 == 0))
            or store.persistent._jn_player_birthday_day_month != (29, 2)
        ):
            # Leap year or birthday isn't on a leap day, so do direct comparison
            return (input_date.day, input_date.month) == store.persistent._jn_player_birthday_day_month

        else:
            # Not a leap year, account for birthdays on 29th February
            return (input_date.day, input_date.month) == (28, 2)

    def jnIsAnniversary(input_date=None):
        """
        Returns True if the input_date is the player and Natsuki's anniversary; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if not store.persistent._jn_player_anniversary_day_month:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        if (
            ((input_date.year % 4 == 0 and input_date.year % 100 != 0) or (input_date.year % 400 == 0))
            or store.persistent._jn_player_anniversary_day_month != (29, 2)
        ):
            # Leap year or anniversary isn't on a leap day, so do direct comparison
            return (input_date.day, input_date.month) == store.persistent._jn_player_anniversary_day_month

        else:
            # Not a leap year, account for anniversaries on 29th February
            return (input_date.day, input_date.month) == (28, 2)

    def jnIsDate(input_date):
        """
        Returns True if the current date's day and month match the given day and month; otherwise False

        IN:
            - input_date - The datetime date to check against
        """
        return (datetime.date.today().day == input_date.day and datetime.date.today().month == input_date.month)

    def jnGetIsDateValid(input_year=2020, input_month=1, input_day=1):
        """
        Returns True if the given year, month and day correspond to a valid date; otherwise False

        IN:
            - input_year - int year of the date to check. Defaults to 2020 for leapyear checks.
            - input_month - int month of the date to check.
            - input_day - int day of the date to check.
        """
        try:
            new_date = datetime.datetime(input_year, input_month, input_day)
            return True

        except:
            return False

    def jnGetMonthNameFromInt(month):
        """
        Gets the month name from an integer.

        IN:
            - month - int month
        """
        month_map = {
            1: "January",
            2: "Feburary",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return month_map.get(month)

    def jn_get_current_hour():
        """
        Gets the current hour (out of 24) of the day.

        OUT:
            Integer representing the current hour of the day.
        """
        return datetime.datetime.now().hour

    def jn_is_weekday():
        """
        Gets whether the current day is a weekday (Monday : Friday).

        OUT:
            True if weekday, otherwise False
        """
        return datetime.datetime.now().weekday() < 5

    def jn_get_current_time_block():
        """
        Returns a type describing the current time of day as a segment.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        current_hour = jn_get_current_hour()
        if current_hour in range(3, 5):
            return JNTimeBlocks.early_morning

        elif current_hour in range(5, 9):
            return JNTimeBlocks.mid_morning

        elif current_hour in range(9, 12):
            return JNTimeBlocks.late_morning

        elif current_hour in range(12, 18):
            return JNTimeBlocks.afternoon

        elif current_hour in range(18, 22):
            return JNTimeBlocks.evening

        else:
            return JNTimeBlocks.night

    def jn_is_time_block_early_morning():
        """
        Returns True if the current time is judged to be early morning.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(3, 5)

    def jn_is_time_block_mid_morning():
        """
        Returns True if the current time is judged to be mid morning.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(5, 9)

    def jn_is_time_block_late_morning():
        """
        Returns True if the current time is judged to be late morning.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(9, 12)

    def jn_is_time_block_morning():
        """
        Returns True if the current time is judged to be morning generally, and not a specific time of morning.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(3, 12)

    def jn_is_time_block_afternoon():
        """
        Returns True if the current time is judged to be afternoon.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(12, 18)

    def jn_is_time_block_evening():
        """
        Returns True if the current time is judged to be evening.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(18, 22)

    def jn_is_time_block_night():
        """
        Returns True if the current time is judged to be night.

        Time blocks are absolute, and not modified by user preferences on sunrise/sunset.
        """
        return jn_get_current_hour() in range(22, 3)

    def jn_is_day():
        """
        Returns True if the current time is judged to be day, taking into account user preferences on sunrise/sunset.
        """
        return datetime.time(jn_locations.getHourFromSunriseSunsetValue(store.persistent._jn_sunrise_setting)) <= datetime.datetime.now().time() < datetime.time(jn_locations.getHourFromSunriseSunsetValue(store.persistent._jn_sunset_setting, is_sunset=True))

    def jn_open_google_maps(latitude, longitude):
        """
        Opens Google Maps in a new tab/window in the default browser centred on the given latitude and longitude.

        IN:
            - latitude - The latitude to centre the map on.
            - longitude - The longitude to centre the map on.
        """
        url = "https://www.google.com/maps/place/{0},{1}".format(latitude, longitude)
        webbrowser.open(url)

    def jnPause(delay, hard=True):
        """
        Equivalent to Ren'Py's pause, but we assume a hard pause so players cannot skip.

        IN:
            - delay - int/decimal amount of time in seconds to wait for
            - hard - bool flag for whether the player can skip the pause or not. Defaults to true, as in not skippable.
        """
        renpy.pause(delay=delay, hard=hard)

    def jnGetDisplayableFromTags(tags):
        """
        Given a tag, returns the displayable corresponding to it.
        
        IN:
            - tags - Str or tuple tags identifying the image
        OUT:
            - If the image exists, the displayable for that image - otherwise a Null displayable
        """
        if isinstance(tags, basestring):
            tags = set(tags.split())

        return renpy.display.image.images[tags] if tags in renpy.display.image.images else Null()

# Variables with cross-script utility specific to Just Natsuki
init -990 python in jn_globals:
    import re
    import store

    # Tracking; use these for data we might refer to/modify mid-session, or anything time sensitive
    current_session_start_time = store.datetime.datetime.now()

    # Flags; use these to set/refer to binary states

    # Tracks whether the player opted to stay for longer when Natsuki asked them to when quitting; True if so, otherwise False
    player_already_stayed_on_farewell = False

    # Tracks if the player is permitted to force quit; use this to block force quits during sequences
    force_quit_enabled = True

    # List of weather to push
    weather_stack = []

    # Constants; use these for anything we only want defined once and used in a read-only context: anything defined here should be used in more than one application!

    # Links

    # GitHub
    LINK_JN_GITHUB = "https://github.com/Just-Natsuki-Team/NatsukiModDev"
    LINK_JN_LATEST = "{0}/releases/latest".format(LINK_JN_GITHUB)

    # OpenWeatherMap; used for setting up weather in-game
    LINK_OPEN_WEATHER_MAP_HOME = "https://openweathermap.org"
    LINK_OPEN_WEATHER_MAP_SIGN_UP = "https://home.openweathermap.org/users/sign_up"
    LINK_OPEN_WEATHER_MAP_API_KEYS = "https://home.openweathermap.org/api_keys"

    # LatLong.net; used for helping the player find their coordinates when setting up location manually
    LINK_LAT_LONG_HOME = "https://www.latlong.net"

    # Alphabetical (excluding numbers) values allowed for text input
    DEFAULT_ALPHABETICAL_ALLOW_VALUES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-' "

    # Numerical values allowed for text input
    DEFAULT_NUMERICAL_ALLOW_VALUES = "1234567890"

    #The current label we're in
    current_label = None

    #The last label we were in
    last_label = None

    # Channel registration

    # Channel for looping weather sfx
    renpy.music.register_channel("weather_loop", "sfx", True)

init 10 python in jn_globals:
    # The current affection state. We default this to 5 (NORMAL)
    current_affinity_state = store.jn_affinity.NORMAL

#Stuff that's really early, which should be usable basically anywhere
init -999 python in jn_utils:
    import datetime
    import easter
    from Enum import Enum
    import hashlib
    import os
    import shutil
    import store
    import threading
    import uuid
    import pprint
    import pygame

    #Make log folder if not exist
    _logdir = os.path.join(renpy.config.basedir, "log")
    if not os.path.exists(_logdir):
        os.makedirs(_logdir)

    #We always want to log and keep history
    __main_log = renpy.renpy.log.open("log/log", append=True, flush=True)

    SEVERITY_INFO = 0
    SEVERITY_WARN = 1
    SEVERITY_ERR = 2

    LOGSEVERITY_MAP = {
        SEVERITY_INFO: "[{0}] [INFO]: {1}",
        SEVERITY_WARN: "[{0}] [WARNING]: {1}",
        SEVERITY_ERR: "[{0}] [ERROR]: {1}"
    }

    __KEY_HASH = "4d753616e2082a70b8ec46439c26e191010384c46e81d488579c3cca35eb3d6c"

    def log(message, logseverity=SEVERITY_INFO):
        """
        Writes a message to the main log file (DDLC/log/log.txt)

        IN:
            - message - message to write to the log file
            - logseverity - Severity level of the log message (Default: INFO)
        """
        global __main_log
        __main_log.write(
            LOGSEVERITY_MAP.get(
                logseverity,
                LOGSEVERITY_MAP[SEVERITY_INFO]
            ).format(datetime.datetime.now(), message)
        )

    def prettyPrint(object, indent=1, width=150):
        """
        Returns a PrettyPrint-formatted representation of an object as a dict.

        IN:
            - object - the object to be converted
            - indent - the level of indentation in the formatted string
            - width - the maximum length of each line in the formatted string, before remaining content is shifted to next line

        OUT:
            Formatted string representation of object __dict__
        """
        return pprint.pformat(object.__dict__, indent, width)

    def getFileExists(path):
        """
        Checks to see if the specified file exists.

        IN:
            - path - The path to check

        OUT:
            - True if the file exists, otherwise False
        """
        return os.path.isfile(path)

    def createDirectoryIfNotExists(path):
        """
        Checks to see if the specified directory exists, and creates it if not
        Returns True if a directory was created, otherwise False

        IN:
            - path - The path to check

        OUT:
            - True if a directory was created, otherwise False
        """
        if not os.path.exists(path) or getFileExists(path):
            os.makedirs(path)
            return True

        return False

    def deleteFileFromDirectory(path):
        """
        Attempts to delete the file at the given path.

        IN:
            - path - The path to delete the file at.

        OUT:
            - True if the file was deleted, otherwise False
        """
        if getFileExists(path):
            try:
                os.remove(path)
                return True

            except Exception as exception:
                log("Failed to delete file on path {0}; {1}".format(path, exception.message))
                return False

        return False

    def deleteDirectory(path):
        """
        Attempts to delete the directory at the given path.

        IN:
            - path - The path of the directory to delete.

        OUT:
            - True if the directory was deleted, otherwise False
        """
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                return True

            except Exception as exception:
                log("Failed to delete directory at path {0}; {1}".format(path, exception.message))
                return False

        return False

    def escapeRenpySubstitutionString(string):
        """
        Escapes a string to account for Ren'Py substitution.
        Use this when displaying names of items that may contain the Ren'Py substitution characters, such as file names from users.

        IN:
            - string - The string to escape and return
        OUT:
            - string with Ren'Py substition characters handled
        """
        return string.replace("[", "[[").replace("{", "{{")

    def getAllDirectoryFiles(path, extension_list=None):
        """
        Runs through the files in the specified directory, filtering files via extension check if specified
        Returns a list containing tuples representing (file_name, file_path)

        IN:
            - path - the file path to search
            - extension_list - optional list of file extensions; only files with these extensions will be returned. These must be supplied without "."

        OUT:
            - Tuple representing (file_name, file_path)
        """
        return_file_items = []

        for file in os.listdir(path):
            if (not extension_list or any(file_extension == file.rpartition(".")[-1] for file_extension in extension_list)):
                return_file_items.append((escapeRenpySubstitutionString(file), os.path.join(path, file)))

        return return_file_items

    def fireAndForgetFunction(function, args=()):
        """
        Creates and starts a new, untracked background thread given a function and args that runs without blocking execution.
        This will not return a result, therefore only use this for things like void functions where no return is expected/needed.
        
        IN:
            - function - the function to call in the new thread
            - args - parameters to be passed to the function; must be of type list or tuple
        """

        if not callable(function):
            jn_utils.log("Failed to launch thread; function is not callable.")
            return

        if not isinstance(args, tuple) and not isinstance(args, list):
            jn_utils.log("Failed to launch thread; args must be of types list or tuple.")
            return

        if isinstance(args, list):
            args = tuple(args)

        thread = threading.Thread(name=uuid.uuid4(), target=function, args=args)
        thread.daemon = True
        thread.start()

    def getSupportedMusicFileExtensions():
        """
        Returns a list of the music file extensions JN supports.
        """
        return {"mp3", "ogg", "wav"}

init -100 python in jn_utils:
    import codecs
    import random
    import re
    import store
    import store.jn_utils as jn_utils
    import store.jn_globals as jn_globals

    def get_current_session_length():
        """
        Returns a timedelta object representing the length of the current game session.

        OUT:
            datetime.timedelta object representing the length of the current game session
        """
        return datetime.datetime.now() - store.jn_globals.current_session_start_time

    def get_total_gameplay_length():
        """
        Returns a timedelta object representing the total time the player has spent with Natsuki.

        OUT:
            datetime.timedelta object representing the length of the total game time
        """
        if store.persistent.jn_first_visited_date is not None:
            return datetime.datetime.now() - store.persistent.jn_first_visited_date

        else:
            return datetime.datetime.now() - datetime.datetime.today()

    def get_total_gameplay_seconds():
        """
        Returns the number of seconds the player has spent with Natsuki in total.

        OUT:
            - Seconds spent with Natsuki since starting JN
        """
        return get_total_gameplay_length().total_seconds()

    def get_total_gameplay_minutes():
        """
        Returns the number of minutes the player has spent with Natsuki in total.

        OUT:
            - Minutes spent with Natsuki since starting JN
        """
        return get_total_gameplay_length().total_seconds() / 60

    def get_total_gameplay_hours():
        """
        Returns the number of hours the player has spent with Natsuki in total.

        OUT:
            - Hours spent with Natsuki since starting JN
        """
        return get_total_gameplay_length().total_seconds() / 3600

    def get_total_gameplay_days():
        """
        Returns the number of days the player has spent with Natsuki in total.

        OUT:
            - Days spent with Natsuki since starting JN
        """
        return get_total_gameplay_length().total_seconds() / 86400

    def get_total_gameplay_months():
        """
        Returns the number of months the player has spent with Natsuki in total.

        OUT:
            - Months spent with Natsuki since starting JN
        """
        return get_total_gameplay_length().total_seconds() / 2628000

    def get_time_in_session_descriptor():
        """
        Get a descriptor based on the number of minutes the player has spent in the session, up to 30 minutes

        OUT:
            Brief descriptor relating to the number of minutes spent in the session
        """
        minutes_in_session = get_current_session_length().total_seconds() / 60

        if minutes_in_session <= 1:
            return "like a minute"

        elif minutes_in_session <= 3:
            return "a couple of minutes"

        elif minutes_in_session > 3 and minutes_in_session <= 5:
            return "like five minutes"

        elif minutes_in_session > 5 and minutes_in_session <= 10:
            return "around ten minutes"

        elif minutes_in_session > 10 and minutes_in_session <= 15:
            return "around fifteen minutes"

        elif minutes_in_session > 15 and minutes_in_session <= 20:
            return "around twenty minutes"

        elif minutes_in_session <= 30:
            return "about half an hour"

        else:
            return "a while"

    def getNumberOrdinal(value):
        """
        Returns the ordinal (trailing characters) for a given numerical value.
        """
        if 11 <= (value % 100) <= 13:
            return "th"

        else:
            return ["th", "st", "nd", "rd", "th"][min(value % 10, 4)]

    def getPlayerInitial():
        """
        Returns the first letter of the player's name.

        OUT:
            First letter of the player's name.
        """
        return list(store.player)[0]

    def getPlayerFinal(repeat_times=0):
        """
        Returns the last letter of the player's name.
        OUT:
            Last letter of the player's name
        """
        player_final = list(store.player)[len(store.player) - 1]
        for i in range(repeat_times):
            player_final += list(store.player)[len(store.player) - 1]

        return player_final

    def getStringContainsLabel(string):
        """
        Returns True if the given string contains a label pertaining to sexuality.
        Used for more stringent checks on items such as nicknames where such terms aren't appropriate.

        IN:
            - string - The string to test

        OUT:
            - True if string contains a label; otherwise False
        """
        return re.search(re.compile('|'.join({
            "qu[e3][e3]r",
            "s[e3]xu[a4]l",
            "(?!sus)s[e3]x$",
        }), re.IGNORECASE), string.lower())

    def getStringContainsProfanity(string):
        """
        Returns True if the given string contains a profanity, based on regex.
        Source courtesy of: https://github.com/RobertJGabriel/Google-profanity-words, with some additions by us

        IN:
            - string - The string to test

        OUT:
            - True if string contains profanity; otherwise False
        """
        return re.search(re.compile('|'.join({
            "(?<![blmprs])ass(?!i)",
            "(^d[il1]ck$|d[il1]ckhead)",
            "(^dink$|dirsa)",
            "^f[a4]g{1,2}$",
            "[s5]h[il1]t",
            "(a_s_s|a55)",
            "anu[s5]",
            "(ar5e|arrse|^arse$)",
            "((b|l3)[il1]a?[t+7]ch)",
            "(bolloc?k)",
            "([ck]ock|cok)",
            "([ck]um|cunil|kunil)",
            "(d[o0][o0]sh|duche)",
            "eja[ck]ul.*",
            "(f4nny|fanny|fanyy)",
            "([4f](uc?|oo|ec|cu)[kx]|f_u_c_k)",
            "g[o0]d-dam",
            "^(h[o0]are?|h[o0]er|h[o0]re)$",
            "(h[o0]rniest|h[o0]rny)",
            "jack-?[o0]ff",
            "j[il1][sz]m",
            "(m[a4][s5]t[eu]r-?b[a8][t+]?[e3]?|masochist)",
            "m[o0]-?f[o0]",
            "n[il1]gg",
            "[o0]rgas[il1]?m",
            "phuc?[kq]",
            "^(p[o0]rn|pr[o0]n)$",
            "puss[eiy]",
            "(r[il1]mjaw|r[il1]mming)",
            "(scr[o0]at|scr[o0]te|scr[o0]tum)",
            "(sh[i\!1][t+]e?|s_h_i_t)",
            "(test[il1]cal|test[il1]cle)",
            "(^t[il1]t$|t[il1]tt[il1]e[s5]|t[e3][e3]ts|t[e3][e3]tz)",
            "(tw[a4]t|twunt)",
            "(w[il1]ll[il1][e3]s|w[il1]lly)",
            "^balls$",
            "^bum$",
            "^c[o0][o0]n$",
            "^h[o0]$",
            "^h[o0][e3]$",
            "^n[o0]b$",
            "^t[il1]t$",
            "4r5e",
            "^a[il1]ds$",
            "^anal$",
            "b[il1]tch",
            "b[o0]+b(?!er|on)",
            "ballbag",
            "ballsack",
            "bastard",
            "b[e3]ll[e3]nd",
            "^b[e3]st[il1]al$",
            "b[e3]st[il1]ality",
            "^bl[o0][o0]dy$",
            "bl[o0]wj[o0]b",
            "b[o0]i[o0]las",
            "b[o0]ner",
            "br[e3]asts",
            "buceta",
            "bugger",
            "bunnyfucker",
            "butt(?!er|on)",
            "c[o0]ck",
            "c[o0]cksucker",
            "carpetmuncher",
            "cawk",
            "chink",
            "^cipa$",
            "^cl[il1]t$",
            "cnut",
            "crap",
            "^cunt$",
            "cyal[il1]s",
            "cyberfuc*",
            "^damn$",
            "dild[o0]",
            "d[o0]g-fucker",
            "d[o0]ggin",
            "d[o0]nkeyribber",
            "dyke",
            "fatass",
            "felching",
            "f[e3]llat",
            "^flang[e3]$",
            "fudg[e3]pack[e3]r",
            "gangbang",
            "gayl[o0]rd",
            "gays[e3]x",
            "g[o0]ats[e3]",
            "g[o0]ddamn",
            "hardc[o0]r[e3]s[e3]x",
            "(^h[e3]ll$|^h[e3]llspawn$)",
            "h[il1]tl[e3]r",
            "h[e3]sh[e3]",
            "^h[o0]m[o0]$",
            "h[o0]tsex",
            "^jap$",
            "j[e3]rk-[o0]ff",
            "kawk",
            "^kn[o0]b$",
            "k[o0]ndum",
            "lab[il1]a",
            "^l[e3]sb[o0]$",
            "^lust$",
            "^muff$",
            "mutha",
            "naz[il1]",
            "^n[il1]gg[e3]r",
            "^n[il1]gga$",
            "^n[e3]gr[o0]",
            "numbnuts",
            "nutsack",
            "p[o0]rn",
            "^pawn$",
            "^pecker$",
            "ped[o0]",
            "p[e3]nis",
            "ph[o0]nes[e3]x",
            "pigfucker",
            "pimpis",
            "p[il1]ss",
            "^(p[o0][o0]|p[o0][o0]p)$",
            "^pr[il1]ck$",
            "^pub[e3]$",
            "r[e3]ctum",
            "r[e3]tard",
            "s.[o0].b.",
            "sad[il1]st",
            "schl[o0]ng",
            "^scr[e3]w$",
            "s[e3]m[e3]n",
            "^[s5]ex$",
            "^[s5]exual$",
            "^shag$",
            "sh[e3]mal[e3]",
            "^skank|^scanc",
            "slut$",
            "slutty",
            "sm[e3]gma",
            "smut",
            "snatch",
            "s[o0]n-[o0]f-a-bitch|s[o0]n[o0]fabitch",
            "^spac$",
            "spunk",
            "t[o0]sser",
            "^turd$",
            "v14gra|v1gra",
            "vag[il1]na",
            "v[il1]agra",
            "vulva",
            "w[o0][o0]se",
            "wang",
            "wank$",
            "wh[o0]ar",
            "wh[o0]re",
            "xrat[e3]d",
            "xxx"
        }), re.IGNORECASE), string.lower())

    def getStringContainsInsult(string):
        """
        Returns True if the given string contains an insult, based on regex.

        IN:
            - string - The string to test

        OUT:
            - True if string contains an insult; otherwise False
        """
        return re.search(re.compile('|'.join({
            "arr[o0]gant",
            "^abr[o0]s[e3]xual$",
            "^as[e3]xual$",
            "^(b[e3]ast|b[e3]astly)$",
            "b[o0]n[e3]bag",
            "b[o0]n[e3]h[e3]ad",
            "^b[il1]sexual$",
            "^b[il1]$",
            "^brat$|bratty",
            "br[e3]adb[o0]ard",
            "^bully$",
            "^ch[e3]at[e3]r$",
            "^ch[il1]ld$",
            "^cl[o0]wn$",
            "cutt[il1]ngb[o0]ard",
            "^d[e3]m[o0]n$",
            "^d[e3]m[il1]s[e3]xual$",
            "d[il1]mw[il1]t",
            "^d[il1]rt$",
            "d[il1]sgust[il1]ng",
            "^d[o0]g$",
            "dumb|dumb[o0]",
            "dunc[e3]",
            "^dwarf$",
            "dw[e3][e3]b",
            "[e3]g[o0]ist|[e3]g[o0]tistical",
            "^[e3]vil$",
            "^(fa[il1]l|fa[il1]lur[e3])$",
            "fak[e3]",
            "(^fat$|fats[o0]|fatty|fatt[il1][e3])",
            "(flat|flats[o0]|flatty|flatt[il1][e3])",
            "^gay$",
            "^g[e3]nd[e3]rqu[e3][e3]r$",
            "^g[il1]lf$",
            "^(ghast|ghastly)$",
            "^gr[e3]mlin$",
            "^gr[o0]ss$",
            "halfl[il1]ng|halfp[il1]nt|half-p[il1]nt",
            "halfw[il1]t",
            "h[e3]artl[e3]ss",
            "h[e3]llspawn",
            "^h[e3]t[e3]r[o0]$",
            "^h[e3]t[e3]r[o0]s[e3]xual$",
            "hid[e3][o0]us",
            "h[o0]rrid|h[o0]rribl[e3]",
            "^h[o0]m[o0]s[e3]x$",
            "^h[o0]m[o0]s[e3]xual$",
            "hungry",
            "^idi[o0]t$",
            "ign[o0]ramus",
            "ign[o0]rant",
            "[il1]mb[e3]cil[e3]",
            "^[il1]mp$",
            "[il1]r[o0]ningb[o0]ard",
            "^[il1]nt[e3]rs[e3]x$",
            "(^k[il1]d$|k[il1]dd[o0]|k[il1]ddy|k[il1]dd[il1][e3])",
            "l[e3]sbian",
            "l[e3]sb[o0]",
            "^m[il1]dg[e3]t$",
            "m[o0]r[o0]n",
            "narc[il1]ss[il1]st",
            "(^nasty$|nasty-ass)",
            "n[e3]ckcrack|n[e3]ck-crack",
            "n[e3]cksnap|n[e3]ck-snap",
            "^n[il1]mr[o0]d$",
            "nu[il1]sanc[e3]",
            "^[o0]mn[il1]s[e3]xual$",
            "^p[e3]st$",
            "^path[e3]tic$",
            "^pans[e3]xual$",
            "playth[il1]ng",
            "^p[o0]lys[e3]xual$",
            "punchbag|punch-bag|punch[il1]ngbag|punch[il1]ng-bag",
            "^pupp[e3]t$",
            "putr[il1]d",
            "^sh[o0]rt$|sh[o0]rtstuff|sh[o0]rty",
            "^s[il1]ck$",
            "^s[il1]mp$",
            "s[il1]mpl[e3]t[o0]n",
            "^sk[il1]nny$",
            "slav[e3]",
            "sm[e3]lly",
            "^s[o0][il1]l$",
            "starv[e3]d|starv[il1]ng",
            "st[il1]nky",
            "^(stuckup|stuck-up)$",
            "^stup[il1]d$",
            "^t[e3]abag$",
            "^th[o0]t$",
            "^t[il1]ny$",
            "^t[o0]y$",
            "^tw[e3]rp$",
            "^tw[il1]t$",
            "^us[e3]l[e3]ss$",
            "^v[e3]ndingmachin[e3]$",
            "^(v[il1]rg[il1]n|turb[o0]virgin)$",
            "^v[o0]mit$",
            "^washb[o0]ard$",
            "^w[il1]tch$",
            "^wr[e3]tch$",
            "^z[o0]mbi[e3]$",
        }), re.IGNORECASE), string.lower())

    def getRandomTease():
        """
        Returns a random tease from Natsuki for the player from the list.
        Natsuki may use these at higher levels of affinity to tease her player with.
        """
        return random.choice([
            "dummy",
            "you big dummy",
            "silly",
            "stupid",
            "you dork",
            "you big dork",
            "you goof",
            "you goofball",
            "you numpty",
            "you donut",
            "you dope",
            "you big dork",
            "you big goof",
            "you big dope"
        ])

    def getRandomTeaseName():
        """
        Returns a random tease from Natsuki, avoiding any assignment of the term I.E "you" or descriptions I.E "silly".
        Natsuki may use these at higher levels of affinity to tease her player with.
        """
        return random.choice([
            "dummy",
            "dork",
            "goof",
            "donut",
            "dope"
        ])

    def getRandomEndearment():
        """
        Returns a random endearment from Natsuki for the player from the list.
        Natsuki may use these at the highest levels of affinity to refer to her player - she isn't that lovey-dovey, so use sparingly!
        """
        return random.choice([
            "babe",
            "darling",
            "dummy",
            "hun",
            "my love",
            "sweetheart",
            "sweetie"
        ])

    def getRandomDescriptor():
        """
        Returns a random positive descriptor from Natsuki for the player from the list.
        Natsuki may use these at the highest levels of affinity to describe her player when she is being sentimental.
        """
        return random.choice([
            "amazing",
            "awesome",
            "really awesome",
            "really great",
            "so sweet",
            "the best"
        ])

    def getRandomInsult():
        """
        Returns a random insult from Natsuki for the player from the list.
        Natsuki may use these at the lowest levels of affinity to insult her player with.
        """
        return random.choice([
            "jerk",
            "idiot",
            "moron",
            "stupid",
            "loser",
            "you ass"
        ])

    def getRandomHappyEmoticon():
        """
        Returns a random happy emoticon from Natsuki for the player from the list.
        """
        return random.choice([
            "^^",
            "^.^",
            "\.^-^./",
            ":)",
            ":]",
            ":3",
            "^-^",
            "^_^",
            ":]",
            ":D",
            "(*^▽^*)",
            "(^∇^)",
            "(＾▽＾)",
            "(=^▽^=)",
            "(^ｖ^)",
            "(^_^)"
        ])

    def getRandomAngryEmoticon():
        """
        Returns a random angry emoticon from Natsuki for the player from the list.
        """
        return random.choice([
            ">_>",
            "<_<",
            "-_-",
            "-.-",
            ">:T",
            ">:/",
            ">:(",
            "(;>_>)",
            "(-_-)",
            "||-_-"
        ])

    def getRandomSadEmoticon():
        """
        Returns a random sad emoticon from Natsuki for the player from the list.
        """
        return random.choice([
            ":(",
            ":'(",
            ":/",
            "._.",
            "(v_v”)",
            "( .. )",
            "( ;; )",
            "(|||;-;)",
            "(;v-v)",
            ":-(",
            "</3",
            "<|3",
            ":<",
            ">:",
        ])

    def getRandomTeaseEmoticon():
        """
        Returns a random teasing emoticon from Natsuki for the player from the list.
        """
        return random.choice([
            ">:3",
            ">:)",
            "^.^",
            "(^ｖ^)",
            ">:P",
            ">;P",
            ">;D",
            ">:D",
            ">;)"
        ])

    def getRandomConfusedEmoticon():
        """
        Returns a random confused emoticon from Natsuki for the player from the list.
        """
        return random.choice([
            "o.o",
            "o.o;",
            "O.O",
            "T.T",
            "T_T",
            "@_@",
            "@.@",
            "0.0?",
            "C-C",
            "C_C",
            "C.C"
        ])

    # Key setup
    key_path = os.path.join(renpy.config.basedir, "game/dev/key.txt").replace("\\", "/")
    if not os.path.exists(key_path):
        __KEY_VALID = False

    else:
        with open(name=key_path, mode="r") as key_file:
            __KEY_VALID = hashlib.sha256(key_file.read().encode("utf-8")).hexdigest() == __KEY_HASH

    def get_key_valid():
        """
        Returns the validation state of the key.
        """
        return __KEY_VALID

    def save_game():
        """
        Saves all game data.
        """

        # Save outfit data
        store.jn_outfits.JNOutfit.saveAll()

        # Save holiday data
        store.jn_events.JNHoliday.saveAll()

        # Save poem data
        store.jn_poems.JNPoem.saveAll()

        # Save joke data
        store.jn_jokes.JNJoke.saveAll()

        # Save desk item data
        store.jn_desk_items.JNDeskItem.saveAll()

        #Save topic data
        store.Topic._save_topic_data()

        #Save background data
        store.main_background.save()

        if store.persistent._affinity_daily_bypasses > 5:
            store.persistent._affinity_daily_bypasses = 5

        if store.persistent.affinity >= (store.persistent._jn_gs_aff + 250):
            store.persistent._jn_pic_aff = store.persistent.affinity
            store.persistent.affinity = store.persistent._jn_gs_aff
            jn_utils.log("434346".decode("hex"))
            store.persistent._jn_pic = True

        else:
            store.persistent._jn_gs_aff = store.persistent.affinity

# Generic transforms/animations
transform JN_TRANSFORM_FADE_IN:
    subpixel True
    alpha 0
    ease 0.5 alpha 1

transform JN_TRANSFORM_FADE_OUT:
    subpixel True
    alpha 1
    ease 0.5 alpha 0

transform JN_PULSE(time=1, wait=1.5):
    truecenter
    alpha 1
    parallel:
        0.144
        zoom 1.00 + 0.07 * time
        easein 0.250 zoom 1.00 + 0.04 * time
        easeout 0.269 zoom 1.00 + 0.07 * time
        zoom 1.00
        wait
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * time
        easeout_bounce 0.3 xalign 0.5 - 0.02 * time
    
    ease 0.15 alpha 0

# Vanilla resources from base DDLC
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)
define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

# JN resources

# Singleton sound effects
define audio.blow = "mod_assets/sfx/blow.ogg"
define audio.book_closing = "mod_assets/sfx/book_closing.ogg"
define audio.button_mashing_a = "mod_assets/sfx/button_mashing_a.ogg"
define audio.button_mashing_b = "mod_assets/sfx/button_mashing_b.ogg"
define audio.button_mashing_c = "mod_assets/sfx/button_mashing_c.ogg"
define audio.button_tap_a = "mod_assets/sfx/button_tap_a.ogg"
define audio.button_tap_b = "mod_assets/sfx/button_tap_b.ogg"
define audio.button_tap_c = "mod_assets/sfx/button_tap_c.ogg"
define audio.card_place = "mod_assets/sfx/card_place.ogg"
define audio.card_shuffle = "mod_assets/sfx/card_shuffle.ogg"
define audio.cassette_close = "mod_assets/sfx/cassette_close.ogg"
define audio.cassette_open = "mod_assets/sfx/cassette_open.ogg"
define audio.chair_in = "mod_assets/sfx/chair_in.ogg"
define audio.chair_out = "mod_assets/sfx/chair_out.ogg"
define audio.chair_out_fast = "mod_assets/sfx/chair_out_fast.ogg"
define audio.chair_out_in = "mod_assets/sfx/chair_out_in.ogg"
define audio.clothing_ruffle = "mod_assets/sfx/clothing_ruffle.ogg"
define audio.coin_flip = "mod_assets/sfx/coin_flip.ogg"
define audio.drawer = "mod_assets/sfx/drawer.ogg"
define audio.drink_pour = "mod_assets/sfx/drink_pour.ogg"
define audio.gift_close = "mod_assets/sfx/gift_close.ogg"
define audio.gift_open = "mod_assets/sfx/gift_open.ogg"
define audio.gift_rustle = "mod_assets/sfx/gift_rustle.ogg"
define audio.gift_slide = "mod_assets/sfx/gift_slide.ogg"
define audio.glass_move = "mod_assets/sfx/glass_move.ogg"
define audio.glasses_case_close = "mod_assets/sfx/glasses_case_close.ogg"
define audio.glasses_case_open = "mod_assets/sfx/glasses_case_open.ogg"
define audio.hair_brush = "mod_assets/sfx/hair_brush.ogg"
define audio.hair_clip = "mod_assets/sfx/hair_clip.ogg"
define audio.headpat = "mod_assets/sfx/headpat.ogg"
define audio.kettle_boil = "mod_assets/sfx/kettle_boil.ogg"
define audio.keyboard = "mod_assets/sfx/keyboard.ogg"
define audio.kiss = "mod_assets/sfx/kiss.ogg"
define audio.laptop_close = "mod_assets/sfx/laptop_close.ogg"
define audio.necklace_clip = "mod_assets/sfx/necklace_clip.ogg"
define audio.notification = "mod_assets/sfx/notification.ogg"
define audio.page_turn = "mod_assets/sfx/page_turn.ogg"
define audio.paper_crumple = "mod_assets/sfx/paper_crumple.ogg"
define audio.paper_throw = "mod_assets/sfx/paper_throw.ogg"
define audio.select_confirm = "mod_assets/sfx/select_confirm.ogg"
define audio.select_hover = "mod_assets/sfx/select_hover.ogg"
define audio.smack = "mod_assets/sfx/smack.ogg"
define audio.stationary_rustle_a = "mod_assets/sfx/stationary_rustle_a.ogg"
define audio.stationary_rustle_b = "mod_assets/sfx/stationary_rustle_a.ogg"
define audio.stationary_rustle_c = "mod_assets/sfx/stationary_rustle_a.ogg"
define audio.straw_sip = "mod_assets/sfx/straw_sip.ogg"
define audio.switch_flip = "mod_assets/sfx/switch_flip.ogg"
define audio.thump = "mod_assets/sfx/switch_flip.ogg"
define audio.twitch_die = "mod_assets/sfx/twitch_die.ogg"
define audio.twitch_you_lose = "mod_assets/sfx/twitch_you_lose.ogg"
define audio.zipper = "mod_assets/sfx/zipper.ogg"

# Glitch/spooky sound effects
define audio.glitch_a = "mod_assets/sfx/glitch_a.ogg"
define audio.glitch_b = "mod_assets/sfx/glitch_b.ogg"
define audio.glitch_c = "mod_assets/sfx/glitch_c.ogg"
define audio.glitch_d = "mod_assets/sfx/glitch_d.ogg"
define audio.glitch_e = "mod_assets/sfx/glitch_e.ogg"
define audio.interference = "mod_assets/sfx/interference.ogg"
define audio.ooo_creep = "mod_assets/sfx/ooo_creep.ogg"
define audio.static = "mod_assets/sfx/glitch_static.ogg"
define audio.thump = "mod_assets/sfx/thump.ogg"

# Looped sound effects
define audio.rain_muffled = "mod_assets/sfx/rain_muffled.ogg"

# Music, vanilla DDLC
define audio.space_classroom_bgm = "mod_assets/bgm/space_classroom.ogg"
define audio.holiday_bgm = "mod_assets/bgm/vacation.ogg"
define audio.dread = "mod_assets/bgm/dread.ogg"

# Music, JN exclusive
define audio.just_natsuki_bgm = "mod_assets/bgm/just_natsuki.ogg"
define audio.happy_birthday_bgm = "mod_assets/bgm/happy_birthday.ogg"
define audio.ikustan_tsuj = "mod_assets/bgm/ikustan_tsuj.ogg"
define audio.juuuuu_nnnnn = "mod_assets/bgm/juuuuu_nnnnn.ogg"
define audio.just = "mod_assets/bgm/just.ogg"
define audio.night_natsuki = "mod_assets/bgm/night_natsuki.ogg"

# Voicing - we disable TTS
define config.tts_voice = None

##Character Definitions
define mc = DynamicCharacter('player', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

init python:
    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    _dismiss_pause = config.developer

    #Each of the girls' names before the MC learns their name throughout ch0.
    s_name = "Sayori"
    m_name = "Monika"
    y_name = "Yuri"

    n_name = "Natsuki"
    player = persistent.playername

init -999 python:
    def labelCallback(name, abnormal):
        jn_globals.last_label = jn_globals.current_label
        jn_globals.current_label = name

    config.label_callback = labelCallback

    def quitInputCheck():
        """
        Checks to ensure that a screen/label isn't up that crashes the game, interferes or otherwise doesn't work with the force quit mechanics/dialogue.
        If so, then prevents the force quit process from continuing until that screen/label is hidden, or the player quits in a way we can't control (I.E spamming the close button or task manager).
        """
        for blocked_screen in (
            "input",
            "choice",
            "choice_centred",
            "choice_centred_mute",
            "categorized_menu",
            "scrollable_choice_menu",
            "poem_view",
            "preferences",
            "history",
            "hotkeys",
            "create_outfit",
            "snap_ui",
            "blackjack_ui"
        ):
            if renpy.get_screen(blocked_screen):
                Natsuki.setForceQuitAttempt(True)
                Natsuki.addApology(jn_apologies.ApologyTypes.sudden_leave)
                Natsuki.setQuitApology(jn_apologies.ApologyTypes.sudden_leave)
                return

        if jn_globals.current_label in (
            "try_force_quit"
        ):
            # Prevent the dialogue being called again if a force quit is already in progress
            return

        elif jn_globals.force_quit_enabled:
            renpy.call("try_force_quit")

    class JNEvent(object):
        """
        Pythonic equivalent of C#'s event type

        Events are added and removed via `+=` to add a listener, and `-=` to remove a listener.
        To call all handlers, simply call the instance of the event class
        """
        def __init__(self):
            self.__eventhandlers = []

        def __iadd__(self, handler):
            self.__eventhandlers.append(handler)
            return self

        def __isub__(self, handler):
            self.__eventhandlers.remove(handler)
            return self

        def __call__(self, *args, **keywargs):
            for eventhandler in self.__eventhandlers:
                eventhandler(*args, **keywargs)
