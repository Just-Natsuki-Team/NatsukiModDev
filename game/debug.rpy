default persistent.jn_debug_tracked_watch_items = [
    "store.persistent.affinity",
    "store.jn_affinity.get_affinity_tier_name()",
    "store.persistent.trust",
    "store.jn_trust.get_trust_tier_name()"
]

init python in jn_debug:

    # This is the basic set of watched data we reset to
    _default_tracked_watch_items = [
        "store.persistent.affinity\n",
        "store.jn_affinity.get_affinity_tier_name()\n",
        "store.persistent.trust\n",
        "store.jn_trust.get_trust_tier_name()"
    ]

    import os
    import store
    import traceback

    _view_tracked_items_enabled = False

    # Tracking states for when attempting to load a file from disk for use on returns
    LOAD_FROM_DISK_SUCCESS = 1
    LOAD_FROM_DISK_NEW_FILE_CREATED = 2
    LOAD_FROM_DISK_FAILED = 3

    def _watch_all_tracked_items():
        """
        Calls renpy.watch() on all items in the tracked watch items list, displaying them onscreen.
        """
        for item in store.persistent.jn_debug_tracked_watch_items:
            try:
                renpy.watch(item)

            except:
                store.utils.log(message="Failed to watch expression {0}".format(item), logseverity=SEVERITY_WARN)
        
    def _unwatch_all_tracked_items():
        """
        Calls renpy.unwatch() on all items in the tracked watch items list, hiding them.
        """
        for item in store.persistent.jn_debug_tracked_watch_items:
            try:
                renpy.unwatch(item)

            except:
                store.utils.log(message="Failed to unwatch expression {0}".format(item), logseverity=SEVERITY_WARN)

    def toggle_show_tracked_watch_items(force_show_state=None):
        """
        Toggles the view state of the tracked items on/off, or forces the view state if force_show_state given.

        IN:
            - force_show_state - bool representing whether to force display on/off regardless of current toggle.
                (Default: None)
        """
        global _view_tracked_items_enabled

        if force_show_state is not None and isinstance(force_show_state, bool):
            if force_show_state:
                _view_tracked_items_enabled = True
                _watch_all_tracked_items()

            else:
                _view_tracked_items_enabled = False
                _unwatch_all_tracked_items()

        else:
            if _view_tracked_items_enabled:
                _view_tracked_items_enabled = False
                _unwatch_all_tracked_items()

            else:
                _view_tracked_items_enabled = True
                _watch_all_tracked_items()

    def add_tracked_watch_item(expression):
        """
        Adds the given expression to the list of items to watch and display

        IN:
            - expression - python statement in string format to watch
        """
        if isinstance(expression, str):
            if expression in store.persistent.jn_debug_tracked_watch_items:
                store.utils.log(
                    message="{0} already in watched variables; ignoring addition call.".format(expression),
                    logseverity=store.utils.SEVERITY_WARN
                )

            else:
                _unwatch_all_tracked_items()
                store.persistent.jn_debug_tracked_watch_items.append(expression)

                if _view_tracked_items_enabled:
                    _watch_all_tracked_items()
        
        else:
            raise Exception("Expression provided is not of type str")
        
    def remove_tracked_watch_item(expression):
        """
        Adds the given expression to the list of items to watch and display

        IN:
            - expression - python statement in string format to watch
        """
        if isinstance(expression, str):
            if expression in store.persistent.jn_debug_tracked_watch_items:
                _unwatch_all_tracked_items()
                store.persistent.jn_debug_tracked_watch_items.remove(expression)

                if _view_tracked_items_enabled:
                    _watch_all_tracked_items()

            else:
                store.utils.log(
                    message="{0} not found in watched variables; ignoring removal call.".format(expression),
                    logseverity=store.utils.SEVERITY_WARN
                )

        else:
            raise Exception("Expression provided is not of type str")

    def load_tracked_watch_items_from_disk():
        """
        Loads the expressions configured under debug/watch_items.txt into memory to be watched.
        """
        try:
            if not os.path.exists(".\\debug"):
                # The folder doesn't exist; create the folder and file from the default ready for use
                os.makedirs(".\\debug")
                items_setup_file = open(".\\debug\\watch_items.txt", "a")
                items_setup_file.writelines(_default_tracked_watch_items)
                items_setup_file.close()
                return LOAD_FROM_DISK_NEW_FILE_CREATED

            else:
                # The folder exists; let's try and read it into memory!
                items_setup_file = open(".\\debug\\watch_items.txt", "r")
                _unwatch_all_tracked_items()
                items_from_file = items_setup_file.readlines()
                items_setup_file.close()

                # Get rid of any whitespace/newline chars, then assign to persistent
                store.persistent.jn_debug_tracked_watch_items = []
                for item_from_file in items_from_file:
                    store.persistent.jn_debug_tracked_watch_items.append(item_from_file.strip('\n'))
                
                # Finally redisplay if the view was open
                if _view_tracked_items_enabled:
                    _watch_all_tracked_items()

                return LOAD_FROM_DISK_SUCCESS

        except:
            # Oh, fiddlesticks
            store.utils.log(
                message="Failed to load the tracked watch item file from disk; are file permissions correctly set?\nTraceback: {0}".format(traceback.format_exc()),
                logseverity=store.utils.SEVERITY_ERR
            )
            return LOAD_FROM_DISK_FAILED
        
    def reset_tracked_watch_items():
        """
        Completely resets the tracked watch item list to the default configuration
        """
        _unwatch_all_tracked_items()
        store.persistent.jn_debug_tracked_watch_items = _default_tracked_watch_items

        if _view_tracked_items_enabled:
            _watch_all_tracked_items()
