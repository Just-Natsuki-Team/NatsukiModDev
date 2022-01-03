default persistent.jn_ui_style = "default"

init python in jn_preferences.random_topic_frequency:
    import store

    OFTEN = 0
    FREQUENT = 1
    SOMETIMES = 2
    RARELY = 3
    NEVER = 4

    _RANDOM_TOPIC_FREQUENCY_COOLDOWN_MAP = {
        0: 5,
        1: 10,
        2: 30,
        3: 60,
        4: 999
    }

    _RANDOM_TOPIC_FREQUENCY_DESC_MAP = {
        0: "Often",
        1: "Frequent",
        2: "Sometimes",
        3: "Rarely",
        4: "Never"
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

# This determines whether the weather must be randomly weathered by the player
# Wether you can deal with this depends on how well you can weather this joke
default persistent.jn_random_weather = True
