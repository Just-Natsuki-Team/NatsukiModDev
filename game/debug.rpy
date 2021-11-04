default persistent.jn_debug_tracked_watch_items = [
    "store.persistent.affinity",
    "store.jn_affinity.get_affinity_tier_name()",
    "store.persistent.trust",
    "store.jn_trust.get_trust_tier_name()"
]

init python in jn_debug:
    import store

    _view_tracked_items_enabled = False

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
                global _view_tracked_items_enabled
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
                global _view_tracked_items_enabled
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
