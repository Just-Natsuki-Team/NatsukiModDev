init -1 python in jn_plugins:
    from Enum import Enum
    import store
    import store.jn_globals as jn_globals

    # Plugins for minute/hour/day checks
    minute_check_calls = []
    hour_check_calls = []
    day_check_calls = []

    # Plugins for the extras menu options
    extras_options = []

    class JNRegisteredActionType(Enum):
        minute = 1
        hour = 2
        day = 3

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

        if not isinstance(statement, basestring):
            raise TypeError("statement for registered action must be of type basestring; type given was {0}".format(type(statement)))

        if not isinstance(priority, int):
            raise TypeError("priority for registered action must be of type int; type given was {0}".format(type(priority)))

        if not isinstance(action_type, JNRegisteredActionType):
            raise TypeError("action_type for registered action must be of type JNRegisteredActionType; type given was {0}".format(type(action_type)))
        
        if action_type == JNRegisteredActionType.minute:
            global minute_check_calls
            minute_check_calls.append(JNRegisteredAction(statement, priority))
            minute_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.hour:
            global hour_check_calls
            hour_check_calls.append(JNRegisteredAction(statement, priority))
            hour_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.day:
            global day_check_calls
            hour_check_calls.append(JNRegisteredAction(statement, priority))
            hour_check_calls.sort(key = lambda action: action.priority)

    def register_extras_option(option_name, visible_if, jump_label):
        """
        Registers an option that can be selected under the Extras menu.

        IN:
            - option_name - the text displayed for this option that the user will see
            - visible_if - python statement that must return True for this option to be visible and selectable 
            - jump_label - the renpy label to jump to when this option is selected, assuming this option is visible and selectable
        """

        if not isinstance(option_name, basestring):
            raise TypeError("option_name must be of type basestring; type given was {0}".format(type(option_name)))

        if not isinstance(visible_if, basestring):
            raise TypeError("visible_if must be of type basestring; type given was {0}".format(type(visible_if)))

        if not isinstance(jump_label, basestring):
            raise TypeError("jump_label must be of type basestring; type given was {0}".format(type(jump_label)))
        
        global extras_options
        extras_options.append(JNRegisteredExtraOption(
            option_name,
            visible_if,
            jump_label
        ))
