init -50 python:
    def register_keymap(keymap_name, keymap_action, *keys):
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
            utils.log("ERROR: Attemptd to register a new keymap under an existing name. Ignoring.", utils.SEVERITY_WARN);
            return

        #Validate the keymap is indeed callable
        if not callable(keymap_action):
            utils.log("ERROR: keymap action provided is not callable. Ignoring.", utils.SEVERITY_WARN)
            return

        #Checks passed, add the keymap
        config.keymap[keymap_name] = keys
        config.underlay.append(renpy.Keymap(**{keymap_name: keymap_action}))
