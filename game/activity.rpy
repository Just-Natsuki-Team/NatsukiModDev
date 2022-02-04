default persistent.jn_activity_used_programs = []

init python in jn_activity:
    from Enum import Enum
    if renpy.windows:
        import pygetwindow
    else:
        import Xlib
        import Xlib.display
    import re
    import store
    import store.jn_utils as jn_utils

    class JNActivities(Enum):
        unknown = 0
        coding = 1
        discord = 2
        music_applications = 3
        gaming  = 4
        youtube = 5
        github_jn = 6
        artwork = 7
        anime_streaming = 8
        work_applications = 9
        twitter = 10
        deviantart = 11
        manga = 12

        def __int__(self):
            return self.value

    WINDOW_NAME_REGEX_ACTIVITY_MAP = {
        "(- visual studio|- notepad/+/+|- atom|- brackets|vim|eclipse)": JNActivities.coding,
        "(- discord)": JNActivities.discord,
        "(spotify|groove|zune|itunes)": JNActivities.music_applications,
        "(steam|origin|battle.net)": JNActivities.gaming,
        "(- youtube)": JNActivities.youtube,
        "(just-natsuki-team/natsukimoddev)": JNActivities.github_jn,
        "(clip studio paint|photoshop|krita|gimp|paint.net)": JNActivities.artwork,
        "(crunchyroll)": JNActivities.anime_streaming,
        "(word|excel|powerpoint|openoffice|libreoffice)": JNActivities.work_applications,
        "(/ twitter)": JNActivities.twitter,
        "(deviantart - |/|deviantart)": JNActivities.deviantart,
        "(- mangadex|- mangasee|- mangakot)": JNActivities.manga
    }

    def get_current_window_name():
        """
        Gets the title of the currently active window.

        OUT:
            - str representing the title of the currently active window
        """
        if renpy.windows:
            if pygetwindow.getActiveWindow():
                return pygetwindow.getActiveWindow().title

            return ""
            
        elif renpy.linux:
            return Xlib.display.Display().get_input_focus().focus.get_wm_name()

        else:
            return ""

    def get_current_activity(delay=0):
        """
        Returns the current JNActivities state of the player as determined by the currently active window,
        and if an entry exists in the WINDOW_NAME_REGEX_ACTIVITY_MAP, or JNActivities.unknown if no match was found.
        IN:
            - delay - Force RenPy to sleep before running the check. This allows time to swap windows from JN for debugging.
        OUT:
            - JNActivities type for the active window, or JNActivities.unknown
        """
        if delay is not 0:
            renpy.pause(delay)

        window_name = get_current_window_name()
        if window_name is not None:
            window_name = get_current_window_name().lower()
            for entry in WINDOW_NAME_REGEX_ACTIVITY_MAP.items():
                if re.search(entry[0], window_name):
                    if not has_player_done_activity(int(entry[1])):
                        store.persistent.jn_activity_used_programs.append(int(entry[1]))
                    
                    return entry[1]

        return JNActivities.unknown

    def has_player_done_activity(activity):
        """
        Returns True if the player has previously partook in the given activity.

        IN:
            - activity - The JNActivities activity to check
        """
        return int(activity) in store.persistent.jn_activity_used_programs
