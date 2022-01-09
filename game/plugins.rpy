init -1 python in jn_plugins:
    from Enum import Enum
    import store
    import store.jn_globals as jn_globals

    # Plugins for minute/hour/day checks
    minute_check_calls = []
    quarter_hour_check_calls = []
    half_hour_check_calls = []
    hour_check_calls = []
    day_check_calls = []

    # Plugins for the extras menu options
    extras_options = []

    class JNRegisteredActionType(Enum):
        minute = 0
        quarter_hour = 1
        half_hour = 2
        hour = 3
        day = 4

    class JNRegisteredAction():
        def __init__(self, statement, priority):
            self.statement = statement
            self.priority = priority

    class JNRegisteredExtraOption():
        def __init__(self, option_name, visible_if, jump_label):
            self.option_name = option_name
            self.visible_if = visible_if
            self.jump_label = jump_label

    def register_time_check_action(action_type, statement, priority=0):
        """
        Registers an action to take place each minute/hour/day, when not in conversation or gameplay with Natsuki.

        IN:
            - action_type - JNRegisteredActionType determining if the statement is be run every minute, hour or day
            - statement - python statement to be executed, to be given as a string literal via eval
            - priority - integer order in which the statement should be executed
        """
        if action_type == JNRegisteredActionType.minute:
            # Add action to minute roster
            global minute_check_calls
            minute_check_calls.append(JNRegisteredAction(statement, priority))
            minute_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.quarter_hour:
            # Add action to quarter-hour roster
            global quarter_hour_check_calls
            quarter_hour_check_calls.append(JNRegisteredAction(statement, priority))
            quarter_hour_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.half_hour:
            # Add action to half-hour roster
            global half_hour_check_calls
            half_hour_check_calls.append(JNRegisteredAction(statement, priority))
            half_hour_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.hour:
            # Add action to hourly roster
            global hour_check_calls
            hour_check_calls.append(JNRegisteredAction(statement, priority))
            hour_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.day:
            # Add action to daily roster
            global day_check_calls
            day_check_calls.append(JNRegisteredAction(statement, priority))
            day_check_calls.sort(key = lambda action: action.priority)

    def register_extras_option(option_name, visible_if, jump_label):
        """
        Registers an option that can be selected under the Extras menu.

        IN:
            - option_name - string; the text displayed for this option that the user will see
            - visible_if - string; python statement that must return True for this option to be visible and selectable 
            - jump_label - string; the renpy label to jump to when this option is selected, assuming this option is visible and selectable
        """        
        global extras_options
        extras_options.append(JNRegisteredExtraOption(
            option_name,
            visible_if,
            jump_label
        ))
