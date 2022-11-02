python early in jn_data_migrations:
    from enum import Enum
    import re
    import store

    # dict mapping a from_version -> to_version, including the function used to migrate between those versions
    # form:
    # "x.y.z": {
    #    MigrationRuntimes.INIT: (callable, "x.y.z"),
    #    MigrationRuntimes.RUNTIME: (callable, "x.y.z")
    #},
    UPDATE_FUNCS = dict()

    # list containing the late (during runtime) migrations we need to run. These will simply be run in order.
    LATE_UPDATES = []

    #Parses x.x.x.x (suffix) to a regex match with two groups:
    # ver and suffix
    VER_STR_PARSER = re.compile(r"^(?P<ver>\d+\.\d+\.\d+)(?P<suffix>.*)$")

    class MigrationRuntimes(Enum):
        """
        Enum for the times to run migration scripts.
        """
        INIT = 1
        RUNTIME = 2

    def migration(from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Decorator function to register a data migration function

        IN:
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)

        OUT:
            the wrapper function
        """
        def wrap(_function):
            registerUpdateFunction(
                _callable=_function,
                from_versions=from_versions,
                to_version=to_version,
                runtime=runtime
            )
            return _function
        return wrap

    def registerUpdateFunction(_callable, from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Register a function to be called when the program is updated.

        IN:
            _callable: the function to run (Must take no arguments)
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)
        """
        for from_version in from_versions:
            if from_version not in UPDATE_FUNCS:
                UPDATE_FUNCS[from_version] = dict()

            UPDATE_FUNCS[from_version][runtime] = (_callable, to_version)

    def verStrToVerList(ver_str):
        """
        Converts a version string to a list of integers representing the version.
        """
        match = VER_STR_PARSER.match(ver_str)
        if not match:
            raise ValueError("Invalid version string.")

        ver_list = match.group("ver").split(".")
        return [int(x) for x in ver_list]

    def compareVersions(ver_str1, ver_str2):
        """
        Compares two version strings.
        """
        match1 = VER_STR_PARSER.match(ver_str1)
        match2 = VER_STR_PARSER.match(ver_str2)

        if not match1 or not match2:
            raise ValueError("Invalid version string.")

        ver1 = verStrToVerList(match1.group("ver"))
        ver2 = verStrToVerList(match2.group("ver"))

        #Check the lengths of the versions, we'll pad the shorter one with zeros
        if len(ver1) > len(ver2):
            ver2 += [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))

        #Now directly compare from left to right
        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1

        #If we got here, the versions are equal
        return 0

    def runInitMigrations():
        """
        Runs init time migration functions. Must be run after init 0
        """
        #We do nothing here if the version isn't in the dict
        if store.persistent._jn_version not in UPDATE_FUNCS:
            return

        #Set from_version to the version we're migrating from
        from_version = store.persistent._jn_version

        #If the current version (config.version) is greater than the version we've got stored (or migrating from)
        #We should loop until we've caught up
        while compareVersions(from_version, renpy.config.version) < 0:
            #First, check if there's a late migration we need to run
            if MigrationRuntimes.RUNTIME in UPDATE_FUNCS[store.persistent._jn_version]:
                LATE_UPDATES.append(UPDATE_FUNCS[store.persistent._jn_version][MigrationRuntimes.RUNTIME])

            #We're below the latest version, so we need to migrate to the next one in the chain
            _callable, from_version = UPDATE_FUNCS[from_version][MigrationRuntimes.INIT]

            #Migrate
            _callable()

    def runRuntimeMigrations():
        """
        Runs the runtime migration functions.
        """
        for _callable in LATE_UPDATES:
            _callable()

#Init time migrations are run at init 10
init 10 python:
    jn_data_migrations.runInitMigrations()


#All migration scripts go here
init python in jn_data_migrations:
    import store.jn_utils as jn_utils

    #This runs a migration from version 0.0.0 to 0.0.1
    #This script serves an example and hence, does nothing. All arguments are present however "runtime" is not necessary
    @migration(["0.0.0"], "0.0.1", runtime=MigrationRuntimes.INIT)
    def to_0_0_1():
        pass

    @migration(["0.0.0", "0.0.1", "0.0.2"], "1.0.0", runtime=MigrationRuntimes.INIT)
    def to_1_0_0():
        # Nickname persistent migration
        if (
            persistent.jn_player_nicknames_allowed is not None
            and not persistent.jn_player_nicknames_allowed
        ):
            persistent._jn_nicknames_natsuki_allowed = False

        # Natsuki nickname variable was renamed; migrate
        if (
            persistent.jn_player_nicknames_current_nickname is not None
            and persistent.jn_player_nicknames_current_nickname != "Natsuki"
            and persistent._jn_nicknames_natsuki_allowed
        ):
            persistent._jn_nicknames_natsuki_current_nickname = persistent.jn_player_nicknames_current_nickname

        if (
            persistent.jn_player_nicknames_bad_given_total is not None
            and persistent.jn_player_nicknames_bad_given_total > 0
        ):
            persistent._jn_nicknames_natsuki_bad_given_total = persistent.jn_player_nicknames_bad_given_total

        # Allow players who haven't told Natsuki they love her yet to confess
        if Natsuki.isLove(higher=True) and persistent.jn_player_love_you_count == 0:
            persistent.affinity = jn_affinity.AFF_THRESHOLD_LOVE -1

        # Topic conditional migrations
        persistent._apology_database = dict()
        persistent._topic_database["talk_i_love_you"]["conditional"] = None
        persistent._topic_database["talk_mod_contributions"]["conditional"] = (
            "not jn_activity.ACTIVITY_SYSTEM_ENABLED "
            "or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
        )

        # Misc migrations
        if (
            persistent.jn_activity_used_programs is not None
            and len(persistent.jn_activity_used_programs) > len(persistent._jn_activity_used_programs)
        ):
            persistent._jn_activity_used_programs = persistent.jn_activity_used_programs

        if persistent.jn_notify_conversations is not None:
            persistent._jn_notify_conversations = persistent.jn_notify_conversations
        
        jn_utils.save_game()
