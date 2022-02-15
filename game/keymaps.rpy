init -50 python:
    def jn_register_label_keymap(keymap_name, keymap_label, *keys):
        """
        Registers a new keymap for labels to be called on the keys pressed

        IN:
            keymap_name - name of the keymap (used to reference it internally in renpy).
            keymap_label - label (no args) which contains the action/dialogue used in the keymap action.
            *keys - individual arguments (or a list) of keys to use as a trigger

        NOTE: See https://www.renpy.org/doc/html/keymap.html for details on creating keymap combos
        NOTE: labels are always called in new context to formally interrupt flow without issues
        """
        if not renpy.has_label(keymap_label):
            jn_utils.log("[ERROR]: Attempted to register label keymap for label that doesn't exist", jn_utils.SEVERITY_WARN)

        jn_register_keymap(
            keymap_name,
            lambda: renpy.call_in_new_context(keymap_label),
            *keys
        )

    def jn_register_keymap(keymap_name, keymap_action, *keys):
        """
        Registers a new keymap with the specified name and action, linked to the given keys

        IN:
            keymap_name - name of the keymap (used to reference it internally in renpy)
            keymap_action - function (no args/return) which performs the action for this.
            *keys - individual arguments (or a list) of keys to use as a trigger.

        NOTE: See https://www.renpy.org/doc/html/keymap.html for details on creating keymap combos
        NOTE: it is best to call things in new context for keymaps to formally interrupt flow without issues
        """
        #If a kemap already exists, we simply log and return
        if keymap_name in config.keymap:
            jn_utils.log("ERROR: Attempted to register a new keymap under an existing name. Ignoring.", jn_utils.SEVERITY_WARN);
            return

        #Validate the keymap is indeed callable
        if not callable(keymap_action):
            jn_utils.log("ERROR: keymap action provided is not callable. Ignoring.", jn_utils.SEVERITY_WARN)
            return

        #Checks passed, add the keymap
        config.keymap[keymap_name] = keys
        config.underlay.append(renpy.Keymap(**{keymap_name: keymap_action}))
