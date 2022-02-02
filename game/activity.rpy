default persistent.jn_activity_used_programs = []

init python in jn_activity:
    from Enum import Enum
    import pygetwindow
    import store
    import store.jn_utils as jn_utils

    class JNActivities(Enum):
        unknown = 0
        visual_studio = 1
        discord = 2
        spotify = 3
        steam  = 4
        youtube = 5
        github_jn = 6
        github_other = 6
        clip_studio_paint = 7
        photoshop = 8
        krita = 9
        crunchyroll = 10
        word = 11
        excel = 12
        powerpoint = 13
        twitter = 14
        deviantart = 15
        gimp = 16
        open_office = 17
        libre_office = 18

        def __int__(self):
            return self.value

    WINDOW_NAME_ACTIVITY_MAP = {
        "visualstudio": JNActivities.visual_studio,
        "discord": JNActivities.discord,
        "spotify": JNActivities.spotify,
        "steam": JNActivities.steam,
        "youtube": JNActivities.youtube,
        "natsukimoddev": JNActivities.github_jn,
        "github": JNActivities.github_other,
        "clipstudiopaint": JNActivities.clip_studio_paint,
        "photoshop": JNActivities.photoshop,
        "krita": JNActivities.krita,
        "crunchyroll": JNActivities.crunchyroll,
        "word": JNActivities.word,
        "excel": JNActivities.excel,
        "powerpoint": JNActivities.powerpoint,
        "twitter": JNActivities.twitter,
        "deviantart": JNActivities.deviantart,
        "gimp": JNActivities.gimp,
        "openoffice": JNActivities.open_office,
        "libreoffice": JNActivities.libre_office,
    }

    def get_current_window_name():
        """
        Gets the title of the currently active window.

        OUT:
            - str representing the title of the currently active window
        """
        return pygetwindow.getActiveWindow().title

    def get_current_activity():
        """
        Returns the current JNActivities state of the player as determined by the currently active window,
        and if an entry exists in the WINDOW_NAME_ACTIVITY_MAP, or JNActivities.unknown if no match was found.
        
        OUT:
            - JNActivities type for the active window, or JNActivities.unknown
        """
        renpy.pause(2.0)
        window_name = get_current_window_name().replace(" ", "").lower()
        for entry in WINDOW_NAME_ACTIVITY_MAP.items():
            if entry[0] in window_name:
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
