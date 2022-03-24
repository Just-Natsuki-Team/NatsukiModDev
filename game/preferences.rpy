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
        0: 999,
        1: 60,
        2: 30,
        3: 10,
        4: 5,
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

# This determines if the game should use realtime weather
default persistent.jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

# These determine when the sun rises/sets
default persistent.jn_sunrise_hour = 6
default persistent.jn_sunset_hour = 18

# This determines if Natsuki should attempt to notify the user when starting a conversation
default persistent.jn_notify_conversations = True
