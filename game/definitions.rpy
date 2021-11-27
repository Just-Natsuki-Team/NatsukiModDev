default persistent.playername = ""
default player = persistent.playername

# Generic data
default persistent.jn_total_visit_count = 0
default persistent.jn_first_visited_date = datetime.datetime.now()
default persistent.jn_last_visited_date = datetime.datetime.now()

#Our main topic pool
default persistent._event_list = list()

#Early imports
init -990 python:
    import datetime

init 0 python:
    import store.jn_affinity as jn_aff
    from collections import OrderedDict

    #Constants for types. Add more here if we need more organizational areas
    TOPIC_TYPE_FAREWELL = "FAREWELL"
    TOPIC_TYPE_GREETING = "GREETING"
    TOPIC_TYPE_NORMAL = "NORMAL"
    TOPIC_TYPE_ADMISSION = "ADMISSION"
    TOPIC_TYPE_COMPLIMENT = "COMPLIMENT"
    TOPIC_TYPE_APOLOGY = "APOLOGY"

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
            if not store.jn_affinity.is_affinity_range_valid(affinity_range):
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
                for key, value in self.__dict__.iteritems()
                if key != "_m1_definitions__persistent_db"
            }

        def check_conditional(self):
            """
            Evaluates the topic's conditional
            """
            if self.conditional is not None:
                try:
                    return eval(self.conditional)

                except Exception as e:
                    store.utils.log(e.message, utils.SEVERITY_ERR)
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
                affinity_state = jn_affinity.get_affinity_state()

            return store.jn_affinity.is_state_within_range(affinity_state, self.affinity_range)

        def evaluate_trust_range(self, trust_state):
            """
            Checks if the current affinity is within this topic's affinity_range

            OUT:
                True if the current affinity is within range. False otherwise
            """
            return None #TODO: THIS

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
            for persist_key, value in self.as_dict().iteritems():
                if TOPIC_LOCKED_PROP_BASE_MAP[persist_key]:
                    self.__persistent_db[self.label][persist_key] = value

        @staticmethod
        def _save_topic_data():
            """
            Saves all topics
            """
            for topic in store.topic_handler.ALL_TOPIC_MAP.itervalues():
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


        def _filter_topic(
            self,
            unlocked=None,
            nat_says=None,
            player_says=None,
            is_seen=None,
            location=None,
            affinity=None,
            trust=None,
            conditional=None,
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

            if conditional and not self.check_conditional():
                return False

            if includes_categories and len(set(includes_categories).intersection(set(self.category))) != len(includes_categories):
                return False

            if excludes_categories and self.category and len(set(excludes_categories).intersection(set(self.category))) > 0:
                return False

            if self.conditional is not None and not eval(self.conditional):
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
            conditional=None,
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
                    conditional,
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
        Pushes a topic to the topic stack

        IN:
            topic_label - Topic.label of the topic you wish to push
        """
        persistent._event_list.insert(0, topic_label)

    def queue(topic_label):
        """
        Queues a topic to the topic stack

        IN:
            topic_label - Topic.label of the topic you wish you queue
        """
        persistent._event_list.append(topic_label)

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

    def get_custom_tracks():
        """
        return all .mp3 files from custom_music folder
        """
        all_files = renpy.list_files()
        tracks = []
        for file in all_files:
            if ".mp3" in file[-4:] and "custom_music" in file:
                name = file.split('.')
                name = name[-2].split('/')
                name = name[-1]
                track = "<loop 0.0>" + file
                tracks.append((name, track))

        return tracks

    def open_txt(file):
        """
            Opens a txt file in default txt editor
        """
        os.startfile(file)


# Variables with cross-script utility specific to Just Natsuki
init -990 python in jn_globals:
    import store

    # Tracking; use these for data we might refer to/modify mid-session, or anything time sensitive
    current_session_start_time = store.datetime.datetime.now()

    # Flags; use these to set/refer to binary states

    # Tracks whether the player opted to stay for longer when Natsuki asked them to when quitting; True if so, otherwise False
    player_already_stayed_on_farewell = False

    # Tracks whether the player is or is not currently playing a game
    player_is_ingame = False

    # Tracks whether the player is or is not currently in some topic flow
    player_is_in_conversation = False

    # Outfit handling; these should be persisted and in some kind of structure going forward for presets, etc.
    natsuki_current_pose = "sitting"
    natsuki_current_outfit = "uniform"
    natsuki_current_hairstyle = "default"
    natsuki_current_accessory = "hairbands/red"
    natsuki_current_eyewear = None

    # Constants; use these for anything we only want defined once and used in a read-only context

    # Endearments Natsuki may use at the highest levels of affinity to refer to her player
    # She isn't that lovey-dovey, so use sparingly!
    DEFAULT_PLAYER_ENDEARMENTS = [
        "babe",
        "darling",
        "dummy",
        "hun",
        "my love",
        "sweetheart",
        "sweetie"
    ]

    # Descriptors Natsuki may use at the higher levels of affinity to define her player
    DEFAULT_PLAYER_DESCRIPTORS = [
        "amazing",
        "awesome",
        "really awesome",
        "really great",
        "so sweet",
        "the best"
    ]

    # Names Natsuki may use at the higher levels of affinity to tease her player with
    DEFAULT_PLAYER_TEASE_NAMES = [
        "dummy",
        "silly",
        "stupid",
        "you dork",
        "you goof",
        "you numpty"
    ]

    # Links

    # OpenWeatherMap; used for setting up weather in-game
    LINK_OPEN_WEATHER_MAP_HOME = "https://openweathermap.org"
    LINK_OPEN_WEATHER_MAP_SIGN_UP = "https://home.openweathermap.org/users/sign_up"
    LINK_OPEN_WEATHER_MAP_API_KEYS = "https://home.openweathermap.org/api_keys"

    # LatLong.net; used for helping the player find their coordinates when setting up location manually
    LINK_LAT_LONG_HOME = "https://www.latlong.net"
    
    # Names Natsuki may use at the lowest levels of affinity to insult her player with
    DEFAULT_PLAYER_INSULT_NAMES = [
        "jerk",
        "idiot",
        "moron",
        "stupid"
    ]

    # Flavor text for the talk menu at high affinity
    DEFAULT_TALK_FLAVOR_TEXT_LOVE_ENAMORED = [
        "What's up,{w=0.1} [player]?",
        "What's on your mind,{w=0.1} [player]?",
        "Something up,{w=0.1} [player]?",
        "You wanna talk?{w=0.2} Ehehe.",
        "I'd love to talk!",
        "I always love talking to you,{w=0.1} [player]!",
        "[player]!{w=0.2} What's up?",
        "[player]!{w=0.2} What's on your mind?",
        "Ooh!{w=0.2} What did you wanna talk about?",
        "I'm all ears,{w=0.1} [player]!",
        "I've always got time for you,{w=0.1} [player]!"
    ]

    # Flavor text for the talk menu at medium affinity
    DEFAULT_TALK_FLAVOR_TEXT_AFFECTIONATE_NORMAL = [
        "What's up?",
        "What's on your mind?",
        "What's happening?",
        "Something on your mind?",
        "Oh?{w=0.2} You wanna talk to me?",
        "Huh?{w=0.2} What's up?",
        "You wanna share something?",
        "Hey!{w=0.2} What's up?",
        "What's new,{w=0.1} [player]?",
        "'Sup,{w=0.1} [player]?"
    ]

    # Flavor text for the talk menu at low affinity
    DEFAULT_TALK_FLAVOR_TEXT_UPSET_DISTRESSED = [
        "What do you want?",
        "What is it?",
        "Can I help you?",
        "Do you need me?",
        "Make it quick.",
        "What now?",
        "Yes?",
        "What do you want now?",
        "What is it this time?",
        "Yeah?{w=0.2} What?",
        "What is it now?",
        "This had better be good."
    ]

    # Flavor text for the talk menu at minimum affinity
    DEFAULT_TALK_FLAVOR_TEXT_BROKEN_RUINED = [
        "...",
        "...?",
        "What?",
        "Just talk already.",
        "Spit it out.",
        "Start talking."
    ]

    # Emoticon sets for where we can't express Natsuki's emotions directly (I.E modals)
    DEFAULT_HAPPY_EMOTICONS = [
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
    ]

    DEFAULT_ANGRY_EMOTICONS = [
        ">_>",
        "<_<",
        "-_-",
        "-.-",
        ">:T",
        ">:/",
        ">:(",
        "(;>_>)",
        "(-_-)"
    ]

    DEFAULT_SAD_EMOTICONS = [
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
        ":<"
    ]

    # Alphabetical (excluding numbers) values allowed for text input
    DEFAULT_ALPHABETICAL_ALLOW_VALUES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-' "

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
init -999 python in utils:
    import datetime
    import os
    import store
    import pprint

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

    def log(message, logseverity=SEVERITY_INFO):
        """
        Writes a message to the main log file (DDLC/log/log.txt)

        IN:
            message - message to write to the log file
            logseverity - Severity level of the log message (Default: INFO)
        """
        global __main_log
        __main_log.write(
            LOGSEVERITY_MAP.get(
                logseverity,
                LOGSEVERITY_MAP[SEVERITY_INFO]
            ).format(datetime.datetime.now(), message)
        )

    def pretty_print(object, indent=1, width=150):
        """
        Returns a PrettyPrint-formatted representation of an object as a dict.

        IN:
            object - the object to be converted
            indent - the level of indentation in the formatted string
            width - the maximum length of each line in the formatted string, before remaining content is shifted to next line

        OUT:
            Formatted string representation of object __dict__
        """
        return pprint.pformat(object.__dict__, indent, width)

init python in utils:
    def get_current_session_length():
        """
        Returns a timedelta object representing the length of the current game session.

        OUT:
            datetime.timedelta object representing the length of the current game session
        """
        return datetime.datetime.now() - store.jn_globals.current_session_start_time

    # Kinda obsessed with decorators right now, tell me in case I should stop using them everywhere
    def coroutine_loop(t):
        """
            a decorator used for calling a function periodically
            is not exact because function cannot be called while Natsuki is talking
            because of this you should always assume the function will be called later than it should be
            but never earlier

            IN:
                t - <datetime.timedelta> how often to call function

            also adds subfunctions to the function
                start() - starts looping and calls the function
                stop() - stops looping
                next_call(t) - set next call time to
                    t - <timedelta> this is a one time thing, regular loop time doesn't change
                        if function is continued to loop afterwards depends on if it's been started or not

            NOTE: loop times are not maintained in-between sessions
        """
        # check if we got timedelta as argument
        if not isinstance(t, datetime.timedelta):
            raise Exception("decorator coroutine_loop accepts only datetime.timedelta object ({0} given)".format(type(t)))

        # if not yet defined, create a dictionary with all functions to loop
        # and put it under .all attribute
        if not hasattr(coroutine_loop, "all"):
            coroutine_loop.all = dict()

        def register(func):
            def stop(self=func):
                coroutine_loop.all[self]["next"] = None
                coroutine_loop.all[self]["looping"] = False

            def start(self=func):
                coroutine_loop.all[self]["next"] = coroutine_loop.all[self]["loop_time"] + datetime.datetime.now()
                coroutine_loop.all[self]["looping"] = True
                func()

            def next_call(t, self=func):
                if not isinstance(t, datetime.timedelta):
                    raise Exception("{0}.next_call expected timedelta instead of {1}".format(func, type(t)))

                coroutine_loop.all[self]["next"] = datetime.datetime.now() + t

            setattr(func, "stop", stop)
            setattr(func, "start", start)
            setattr(func, "next_call", next_call)

            #NOTE: check might not be neccessary?
            if func not in coroutine_loop.all:
                coroutine_loop.all[func] = {"next":None,"loop_time":t, "looping" : False}

            return func
        return register

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

    def get_current_hour():
        """
        Gets the current hour (out of 24) of the day.
        
        OUT:
            Integer representing the current hour of the day.
        """
        return datetime.datetime.now().hour

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

# Single-play sound effects
define audio.camera_shutter = "mod_assets/sfx/camera_shutter.mp3"
define audio.select_hover = "mod_assets/sfx/select_hover.mp3"
define audio.select_confirm = "mod_assets/sfx/select_confirm.mp3"
define audio.coin_flip = "mod_assets/sfx/coin_flip.mp3"
define audio.card_shuffle = "mod_assets/sfx/card_shuffle.mp3"
define audio.card_place = "mod_assets/sfx/card_place.mp3"
define audio.drawer = "mod_assets/sfx/drawer.mp3"
define audio.smack = "mod_assets/sfx/smack.mp3"

# Looped sound effects
define audio.rain_muffled = "mod_assets/sfx/rain_muffled.mp3"

# Music
define audio.test_bgm = "mod_assets/bgm/background_test_music.ogg"

# Sprites
define body_a = "mod_assets/natsuki-assets/base.png"
define uniform_a = "mod_assets/natsuki-assets/uniform.png"
define face_a = "mod_assets/natsuki-assets/jnab.png"

##Character Definitions
define mc = DynamicCharacter('player', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define n2 = DynamicCharacter('Natsuki Test', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

init python:
    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    _dismiss_pause = config.developer

    #Each of the girls' names before the MC learns their name throughout ch0.
    s_name = "Sayori"
    m_name = "Monika"
    y_name = "Yuri"

    # Assign Natsuki the chosen nickname (defaulted to Natsuki)
    if persistent.jn_player_nicknames_current_nickname:
        n_name = persistent.jn_player_nicknames_current_nickname
    
    else:
        n_name = "Natsuki"

init -999 python:
    def label_callback(name, abnormal):
        jn_globals.last_label = jn_globals.current_label
        jn_globals.current_label = name

    config.label_callback = label_callback
