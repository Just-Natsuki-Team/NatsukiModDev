default persistent.playername = ""
default player = persistent.playername

#Screenshot data
default persistent.jn_first_screenshot_taken = None
default persistent.jn_screenshot_good_shots_total = 0
default persistent.jn_screenshot_bad_shots_total = 0

#Our main topic pool
default persistent._event_list = list()

#Early imports
init -990 python:
    import datetime

init 0 python:
    import store.jn_affinity as jn_aff

    #Constants for types. Add more here if we need more organizational areas
    TOPIC_TYPE_FAREWELL = "FAREWELL"
    TOPIC_TYPE_GREETING = "GREETING"
    TOPIC_TYPE_NORMAL = "NORMAL"

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
            persistent_db[label] = self.as_dict()

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

        def evaluate_affinity_range(self):
            """
            Checks if the topic's action should be run
            """
            return store.jn_affinity.is_state_within_range(jn_globals.current_affinity_state, self.affinity_range)

        def __load(self):
            """
            Internal load funtion

            IN:
                persist_data - the as_dict representation of this topic
            """
            self.__dict__.update(self.__persistent_db[self.label])

        def __save(self):
            """
            Saves this topic object to persistent
            """
            self.__persistent_db[self.label] = self.as_dict()

        @staticmethod
        def _save_topic_data():
            """
            Saves all topics
            """
            for topic in store.topic_handler.ALL_TOPIC_MAP.itervalues():
                topic.__save()

        def get_player_affinity_in_topic_range(self):
            """
            Returns whether the player's affinity is in the affinity_range of this topic.
            """
            return affinity.affinity_is_between_bounds(
                lower_bound=self.affinity_range[0],
                affinity=store.persistent.affinity,
                upper_bound=self.affinity_range[1]
            )

        def get_player_trust_in_topic_range(self):
            """
            Returns whether the player's trust is in trust_range of this topic.
            """
            return trust.trust_is_between_bounds(
                lower_bound=self.trust_range[0],
                trust=store.persistent.trust,
                upper_bound=self.trust_range[1]
            )

        def get_topic_has_additional_property_with_value(self, property_key, property_value):
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
            try:
                return self.additional_properties[property_key] is property_value
            except:
                # This isn't ideal, and will need to be handled more gracefully!
                raise Exception("additional_property '{0}' is not defined for topic label: {1}".format(property_key, self.label))

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
            menu_topics - array of topics. Recommended input of get_all_topics()
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
        return menu_items

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

# Variables with cross-script utility specific to Just Natsuki
init -990 python in jn_globals:
    import store

    # Tracking; use these for data we might refer to/modify mid-session, or anything time sensitive
    current_session_start_time = store.datetime.datetime.now()

    # Flags; use these to set/refer to binary states

    # Tracks whether the player opted to stay for longer when Natsuki asked them to when quitting; True if so, otherwise False
    player_already_stayed_on_farewell = False

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
        "really great",
        "so sweet",
        "the best"
    ]

init 10 python in jn_globals:
    # The current affection state. We default this to 5 (NORMAL)
    current_affinity_state = store.jn_affinity.NORMAL

#Stuff that's really early, which should be usable basically anywhere
init -999 python in utils:
    import datetime
    import os
    import store

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

    def get_current_session_length():
        """
        Returns a timedelta object representing the length of the current game session.

        OUT:
            datetime.timedelta object representing the length of the current game session
        """
        return datetime.datetime.now() - store.jn_globals.current_session_start_time

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
define audio.tdokidoki = "mod_assets/bgm/dokidoki.ogg"
define audio.tpoems = "mod_assets/bgm/poems.ogg"
define audio.custom1 = "custom-music/01.mp3"
define audio.custom2 = "custom-music/02.mp3"
define audio.custom3 = "custom-music/03.mp3"
define audio.battle = "custom-music/battle.mp3"
define audio.spooky1 = "mod_assets/bgm/spooky1.ogg"
define audio.camera_shutter = "mod_assets/sfx/camera_shutter.mp3"

define body_a = "mod_assets/natsuki-assets/base.png"
define uniform_a = "mod_assets/natsuki-assets/uniform.png"
define face_a = "mod_assets/natsuki-assets/jnab.png"

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
    n_name = "Natsuki"
    y_name = "Yuri"
