init -1 python in jn_plugins:
    from Enum import Enum
    import store
    import store.jn_globals as jn_globals

    class JNRegisteredActionType(Enum):
        minute = 1
        hour = 2
        day = 3

    class JNRegisteredAction():
        def __init__(self, statement, priority):
            self.statement = statement
            self.priority = priority

    def register_time_check_action(action_type, statement, priority=0):
        """
        Registers an action to take place each minute/hour/day, when not in conversation or gameplay with Natsuki.

        IN:
            - action_type - JNRegisteredActionType determining if the statement is be run every minute, hour or day
            - statement - python statement to be executed, to be given as a string literal via eval
            - priority - integer order in which the statement should be executed
        """

        if not isinstance(statement, basestring):
            raise Exception("statement for registered action must be of type str; type given was {0}".format(type(statement)))

        if not isinstance(priority, int):
            raise Exception("priority for registered action must be of type int; type given was {0}".format(type(priority)))

        if not isinstance(action_type, JNRegisteredActionType):
            raise Exception("action_type for registered action must be of type JNRegisteredActionType; type given was {0}".format(type(action_type)))
        
        if action_type == JNRegisteredActionType.minute:
            jn_globals.minute_check_calls.append(JNRegisteredAction(statement, priority))
            jn_globals.minute_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.hour:
            jn_globals.hour_check_calls.append(JNRegisteredAction(statement, priority))
            jn_globals.hour_check_calls.sort(key = lambda action: action.priority)

        elif action_type == JNRegisteredActionType.day:
            jn_globals.hour_check_calls.append(JNRegisteredAction(statement, priority))
            jn_globals.hour_check_calls.sort(key = lambda action: action.priority)
