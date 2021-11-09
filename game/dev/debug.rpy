default persistent.jn_debug_open_watch_on_load = False

init 10 python:
    # Enable some QoL things
    config.console = True
    config.allow_skipping = True

default persistent.jn_debug_tracked_watch_items = [
    "store.persistent.affinity",
    "store.jn_affinity.get_affinity_tier_name()",
    "store.persistent.trust",
    "store.jn_trust.get_trust_tier_name()"
]

init python in jn_debug:

    import os
    import store
    import traceback

    # This is the basic set of watched data we reset to
    _default_tracked_watch_items = [
        "store.persistent.affinity\n",
        "store.jn_affinity.get_affinity_tier_name()\n",
        "store.persistent.trust\n",
        "store.jn_trust.get_trust_tier_name()"
    ]

    _view_tracked_items_enabled = False

    # Tracking states for when attempting to load a file from disk for use on returns
    LOAD_FROM_DISK_SUCCESS = 1
    LOAD_FROM_DISK_NEW_FILE_CREATED = 2
    LOAD_FROM_DISK_FAILED = 3

    # Let us call the Talk menu whenever to back out of dialogue
    #store.jn_register_label_keymap("force_talk_menu", talk_menu, "ctrl_t")

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

# Debugging topics

# This topic allows us to set the affinity state
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_affinity",
            unlocked=True,
            prompt="Can you change my affinity state?",
            conditional="config.console",
            category=["Debug (Affinity/Trust)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_affinity:
    n "Okaaay! Just tell me what affinity state you want!"
    menu:
        "High affinity...":
            call set_affinity_options_high

        "Low affinity...":
            call set_affinity_options_low

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."

    return

label set_affinity_options_high:
    menu:
        "LOVE":
            $ persistent.affinity = jn_affinity.THRESHOLD_LOVE
            n "Alright! Your affinity state is now LOVE!"

        "ENAMORED":
            $ persistent.affinity = jn_affinity.THRESHOLD_ENAMORED
            n "Alright! Your affinity state is now ENAMORED!"

        "AFFECTIONATE":
            $ persistent.affinity = jn_affinity.THRESHOLD_AFFECTIONATE
            n "Alright! Your affinity state is now AFFECTIONATE!"

        "HAPPY":
            $ persistent.affinity = jn_affinity.THRESHOLD_HAPPY
            n "Alright! Your affinity state is now HAPPY!"

        "NORMAL":
            $ persistent.affinity = jn_affinity.THRESHOLD_NORMAL
            n "Alright! Your affinity state is now NORMAL!"

        "Low affinity options...":
            call set_affinity_options_low

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."

    return

label set_affinity_options_low:
    menu:
        "UPSET":
            $ persistent.affinity = jn_affinity.THRESHOLD_UPSET
            n "Alright! Your affinity state is now UPSET!"

        "DISTRESSED":
            $ persistent.affinity = jn_affinity.THRESHOLD_DISTRESSED
            n "Alright! Your affinity state is now DISTRESSED!"

        "BROKEN":
            $ persistent.affinity = jn_affinity.THRESHOLD_BROKEN
            n "Alright! Your affinity state is now BROKEN!"

        "RUINED":
            $ persistent.affinity = jn_affinity.THRESHOLD_RUINED
            n "Alright! Your affinity state is now RUINED!"

        "High affinity options...":
            call set_affinity_options_high

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."

    return

# This topic allows us to set the trust state
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_set_trust",
            unlocked=True,
            prompt="Can you change my trust state?",
            conditional="config.console",
            category=["Debug (Affinity/Trust)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_set_trust:
    n "Sure! Just tell me what trust state you want!"
    menu:
        "High trust...":
            call set_trust_options_high

        "Low trust...":
            call set_trust_options_low

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."
    
    return

label set_trust_options_high:
    menu:
        "ABSOLUTE":
            $ persistent.trust = jn_trust.TRUST_ABSOLUTE
            n "Alright!{w=0.2} Your trust state is now ABSOLUTE!"

        "COMPLETE":
            $ persistent.trust = jn_trust.TRUST_COMPLETE
            n "Alright!{w=0.2} Your trust state is now COMPLETE!"

        "FULL":
            $ persistent.trust = jn_trust.TRUST_FULL
            n "Alright!{w=0.2} Your trust state is now FULL!"

        "PARTIAL":
            $ persistent.trust = jn_trust.TRUST_PARTIAL
            n "Alright!{w=0.2} Your trust state is now PARTIAL!"

        "NEUTRAL":
            $ persistent.trust = jn_trust.TRUST_NEUTRAL
            n "Alright!{w=0.2} Your trust state is now NEUTRAL!"

        "Low trust options...":
            call set_trust_options_low

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."

    return

label set_trust_options_low:
    menu:
        "SCEPTICAL":
            $ persistent.trust = jn_trust.TRUST_SCEPTICAL
            n "Alright!{w=0.2} Your trust state is now SCEPTICAL!"

        "DIMINISHED":
            $ persistent.trust = jn_trust.TRUST_DIMINISHED
            n "Alright!{w=0.2} Your trust state is now DIMINISHED!"

        "DISBELIEF":
            $ persistent.trust = jn_trust.TRUST_DISBELIEF
            n "Alright!{w=0.2} Your trust state is now DISBELIEF!"

        "SHATTERED":
            $ persistent.trust = jn_trust.TRUST_SHATTERED
            n "Alright!{w=0.2} Your trust state is now SHATTERED!"

        "High trust options...":
            call set_trust_options_high

        "Nevermind.":
            n "Oh...{w=0.3} well,{w=0.1} okay then."

    return

# This topic allows us to print all persistent data to the log, in a readable format
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_print_persistent",
            unlocked=True,
            prompt="Can you print my persistent data?",
            conditional=None,
            category=["Debug (Data)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_print_persistent:
    n "No problem, [player]!{w=0.1} Just give me a second..."
    $ utils.log(utils.pretty_print(persistent))
    n "And we're done!{w=0.2} Ehehe."
    return

# This topic allows us to print all config data to the log
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_print_config",
            unlocked=True,
            prompt="Can you print the config?",
            conditional=None,
            category=["Debug (Data)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_print_config:
    n "Leave it to me,{w=0.1} [player]!{w=0.2} One second..."
    $ utils.log(utils.pretty_print(config))
    n "And...{w=0.3} done!{w=0.2} You're welcome,{w=0.1} [player]~!{w=0.2} Ehehe."
    return

# This topic allows us to toggle on/off a list of core watched items for easy reference
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_toggle_watched_items",
            unlocked=True,
            prompt="Can you toggle the watched item list view?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_toggle_watched_items:
    n "Sure!{w=0.2} Just give me a sec here..."
    n "..."
    $ jn_debug.toggle_show_tracked_watch_items()
    n "There you go, [player]!"
    return

# This topic allows us to add an item to the watched item list
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_add_watched_item",
            unlocked=True,
            prompt="Can you add an item to the watched item list?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_add_watched_item:
    n "No sweat, [player]! Just tell me what you want to add."
    $ player_input = renpy.input("Enter an expression, or enter 'nevermind' to cancel:")
    if (player_input.lower().strip() in {"nevermind", ""}):
        n "Oh. Okay then."

    else:
        n "Right-o!"
        n "..."
        $ jn_debug.add_tracked_watch_item(str(player_input))
        n "Okaaay!{w=0.2} There you go, [player]!"
    
    return

# This topic allows us to remove an item from the watched item list
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remove_watched_item",
            unlocked=True,
            prompt="Can you remove an item from the watched item list?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remove_watched_item:
    n "No worries, [player]! Just tell me what you want to remove."
    $ player_input = renpy.input("Enter an expression, or enter 'nevermind' to cancel:")
    if (player_input.lower().strip() in {"nevermind", ""}):
        n "Oh.{w=0.2} Alright then."

    else:
        n "Leave it to me!"
        n  "..."
        $ jn_debug.remove_tracked_watch_item(str(player_input))
        n "Gotcha!{w=0.2} There you go,{w=0.1} [player]!"
    
    return

# This topic allows us to set the watched item list from file
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_load_watched_items_from_disk",
            unlocked=True,
            prompt="Can you load the watched item list from disk?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_load_watched_items_from_disk:
    n "No problemo,{w=0.1} [player]!{w=0.2} Uno momento..."
    n "..."
    $ load_outcome = jn_debug.load_tracked_watch_items_from_disk()

    if load_outcome == jn_debug.LOAD_FROM_DISK_NEW_FILE_CREATED:
        n "...Huh.{w=0.2} Hey,{w=0.1} [player]..."
        n "It looks like the file I needed didn't exist,{w=0.1} so I went ahead and created it for you."
        $ import os
        $ file_created_directory = os.getcwd()
        n "It's called {i}watch_items.txt{/i},{w=0.1} and you should be able to find it in the {i}debug{/i} folder under {i}[file_created_directory]{/i}."
        n "Remember though -{w=0.1} only one statement per line in the file,{w=0.1} 'kay?{w=0.2} Ehehe."

    elif load_outcome == jn_debug.LOAD_FROM_DISK_SUCCESS:
        n "And...{w=0.3} presto -{w=0.1} job done!"

    else:
        n "Uhmm...{w=0.3} [player]?{w=0.2} It looks like something went wrong."
        n "Are you sure the file is actually there, and isn't blank or anything dumb like that?"
        n "Just let me know when you've checked it out,{w=0.1} 'kay?"
        n "Thanks,{w=0.1} [player]~!"

    return

# This topic allows us to reset the watched item list to its basic configuration
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_reset_watched_items",
            unlocked=True,
            prompt="Can you reset the watched item list?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_reset_watched_items:
    n "Oh?{w=0.2} You want to reset the watched item list?"
    if len(persistent.jn_debug_tracked_watch_items) > 10:
        n "Uhmm...{w=0.3} [player]?{w=0.2} It looks like you're watching a lot of stuff..."
        menu:
            n "Are you sure you want to reset the list?"
            "Yes, please reset it.":
                pass
            "No, not just yet.":
                n "Oh...{w=0.3} well,{w=0.1} alright.{w=0.2} Just let me know whenever then,{w=0.1} 'kay?"
                return

    n "Okaaay!{w=0.2} Just give me a second..."
    n "..."
    $ jn_debug.reset_tracked_watch_items()
    n "And...{w=0.3} gone -{w=0.1} it should be back to basics now!{w=0.2} Ehehe."
    return

# This topic allows us to ensure the watched item list is always shown on loading up, to save toggling for frequent use
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_toggle_watched_items_on_load",
            unlocked=True,
            prompt="Can you toggle the watched item list on load state?",
            conditional="config.console",
            category=["Debug (Watch)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_toggle_watched_items_on_load:
    n "Can do,{w=0.1} [player]!{w=0.2} Just let me know what you wanna do here."
    menu:
        "Enable the watched item list on load.":
            $ persistent.jn_debug_open_watch_on_load = True
            n "Okaaay!{w=0.2} That's all done for you."

            if not jn_debug._view_tracked_items_enabled:
                n "Oh!{w=0.2} It looks like you don't have the view up right now,{w=0.1} by the way."

                menu:
                    n "Do you want me to bring that back up?"

                    "Yes please!":
                        n "Gotcha!{w=0.2} Give me a sec..."
                        n "..."
                        $ jn_debug.toggle_show_tracked_watch_items(True)
                        n "There you go~!"

                    "No thanks!":
                        n "Alrighty!"

        "Disable the watched item list on load.":
            $ persistent.jn_debug_open_watch_on_load = False
            n "Alright -{w=0.1} all done!"

            if jn_debug._view_tracked_items_enabled:
                n "Huh...{w=0.3} it looks like you still have the view up,{w=0.1} by the way."

                menu:
                    n "Do you want me to hide that for you?"

                    "Yes please!":
                        n "Loud and clear,{w=0.1} [player]!{w=0.2} Just a second..."
                        n "..."
                        $ jn_debug.toggle_show_tracked_watch_items(False)
                        n "Ta-{w=0.1}da!{w=0.2} Ehehe."

                    "No thanks!":
                        "Okaaay~."

    return

# This topic allows us to have Natsuki say whatever we like with any expression we choose
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_say",
            unlocked=True,
            prompt="Can you say something for me?",
            conditional=None,
            category=["Debug (Dialogue)"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_say:
    n "Oooh!{w=0.2} Are we pranking someone,{w=0.1} [player]?{w=0.2} I'm for it!"
    $ player_input = renpy.input("What do you want me to say?")
    menu:
        n "Alright!{w=0.2} Now how do you want me to say it?"

        "Neutrally":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki neutral zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Pleading":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki plead zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Sadly":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki sad zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Happily":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki smile zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Sparkly":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki sparkle zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Unamused":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki unamused zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"

        "Mischievously":
            n "Okaaay!{w=0.2} Here goes!"
            show placeholder_natsuki wink zorder jn_placeholders.NATSUKI_Z_INDEX
            n "[player_input]"
    
    n "..."
    show placeholder_natsuki smile zorder jn_placeholders.NATSUKI_Z_INDEX
    n "...And we're done here!{w=0.2} You're welcome,{w=0.1} [player]!"