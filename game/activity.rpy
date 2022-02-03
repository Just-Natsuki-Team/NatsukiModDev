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
        spotify = 3
        gaming  = 4
        youtube = 5
        github_jn = 6
        github_other = 6
        artwork = 7
        anime_streaming = 10
        work_applications = 11
        twitter = 14
        deviantart = 15
        manga = 16
        facebook = 17

        def __int__(self):
            return self.value

    WINDOW_NAME_REGEX_ACTIVITY_MAP = {
        "(visualstudio|notepad/+/+|atom|brackets|vim)": JNActivities.coding,
        "(discord)": JNActivities.discord,
        "(spotify)": JNActivities.spotify,
        "(steam|origin)": JNActivities.gaming,
        "(youtube)": JNActivities.youtube,
        "(natsukimoddev)": JNActivities.github_jn,
        "(github)": JNActivities.github_other,
        "(clipstudiopaint|photoshop|krita|gimp|paint.net)": JNActivities.artwork,
        "(crunchyroll)": JNActivities.anime_streaming,
        "(word|excel|powerpoint|openoffice|libreoffice)": JNActivities.work_applications,
        "(twitter)": JNActivities.twitter,
        "(deviantart)": JNActivities.deviantart,
        "(mangadex|mangasee)": JNActivities.manga,
        "(facebook)": JNActivities.facebook,
    }

    def get_current_window_name():
        """
        Gets the title of the currently active window.

        OUT:
            - str representing the title of the currently active window
        """
        if renpy.windows:
            return pygetwindow.getActiveWindow().title
            
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
            window_name = get_current_window_name().replace(" ", "").lower()
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
