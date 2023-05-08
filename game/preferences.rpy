default persistent.jn_ui_style = "default"

init python in jn_preferences.weather:
    from Enum import Enum
    import store

    class JNWeatherSettings(Enum):
        disabled = 1
        random = 2
        real_time = 3

        def __int__(self):
            return self.value

init python in jn_preferences.random_topic_frequency:
    from Enum import Enum
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4

    _RANDOM_TOPIC_FREQUENCY_COOLDOWN_MAP = {
        0: 10000,
        1: 30,
        2: 15,
        3: 5,
        4: 2,
    }

    _RANDOM_TOPIC_FREQUENCY_DESC_MAP = {
        0: "Never",
        1: "Rarely",
        2: "Sometimes",
        3: "Frequent",
        4: "Often",
    }

    def get_random_topic_frequency_description():
        """
        Gets the descriptor for the random topic frequency, as given by the current frequency.
        """
        return _RANDOM_TOPIC_FREQUENCY_DESC_MAP.get(store.persistent.jn_natsuki_random_topic_frequency)

    def get_random_topic_cooldown():
        """
        Gets the cooldown (in minutes) between topics prompted by Natsuki, as given by the current frequency.
        """
        return _RANDOM_TOPIC_FREQUENCY_COOLDOWN_MAP.get(store.persistent.jn_natsuki_random_topic_frequency)

# This determines how often Natsuki should start a conversation by herself
default persistent.jn_natsuki_random_topic_frequency = jn_preferences.random_topic_frequency.SOMETIMES

# This determines if Natsuki should talk about topics randomly that she has already spoken about
default persistent.jn_natsuki_repeat_topics = True

# This determines if Natsuki will do her own thing in the downtime between topics
default persistent._jn_natsuki_idles_enabled = True

# This determines if the game should use realtime weather
default persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

# This determines if Natsuki should attempt to notify the user when starting a conversation
default persistent._jn_notify_conversations = True

# This determines if Natsuki should attempt to notify the user when she spots them doing something she's interested in
default persistent._jn_notify_activity = True

# RPY warning
default persistent._jn_scw = True

# This determines if Natsuki should warn the player whenever she runs out of unlocked things to say
default persistent._jn_natsuki_out_of_topics_remind = True
