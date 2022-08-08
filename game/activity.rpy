default persistent.jn_activity_used_programs = []

init python in jn_activity:
    from Enum import Enum
    from plyer import notification
    import sys
    import re
    import store
    import store.jn_utils as jn_utils
    
    ACTIVITY_SYSTEM_ENABLED = True

    if renpy.windows:
        from plyer import notification
        import pygetwindow
        sys.path.append(renpy.config.gamedir + '\\python-packages\\')
        import win32api
        import win32gui

    elif renpy.linux:
        import os

        #NOTE: On linux, there are different types of desktop sessions. Xlib will ONLY work with X11 sessions.
        if (os.environ.get('DISPLAY') is None) or (os.environ.get('DISPLAY') == ''):
            store.jn_utils.log("DISPLAY is not set. Cannot use Xlib.")
            #Set a flag indicating this should be disabled.
            ACTIVITY_SYSTEM_ENABLED = False

        else:
            import Xlib
            import Xlib.display

    elif renpy.macintosh:
        ACTIVITY_SYSTEM_ENABLED = False

    class JNWindowFoundException(Exception):
        """
        Custom exception; used to break out of the win32gui.EnumWindows method while still returning a value,
        as only that and returning False are valid means of termination.
        """
        def __init__(self, hwnd):
            self.hwnd = hwnd

        def __str__(self):
            return self.hwnd

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
        "(deviantart - |\| deviantart)": JNActivities.deviantart,
        "(- mangadex|- mangasee|- mangakot)": JNActivities.manga
    }

    def __get_jn_window_hwnd():
        """
        Gets the hwnd of the JN game window (Windows only).

        OUT:
            - int representing the hwnd of the JN game window
        """
        def check_jn_window(hwnd, ctx):
            """
            Returns JNWindowFoundException containing the hwnd of the JN game window.
            """
            if win32gui.GetWindowText(hwnd) == store.config.window_title:
                raise JNWindowFoundException(hwnd)

        try:
            # Iterate through all windows, comparing titles to find the JN game window
            win32gui.EnumWindows(check_jn_window, None)

        except JNWindowFoundException as exception:
            return exception.hwnd

    def get_jn_window_active():
        """
        Returns True if the currently active window is the JN game window, otherwise False.
        """
        return get_current_window_name() == store.config.window_title

    def get_current_window_name():
        """
        Gets the title of the currently active window.

        OUT:
            - str representing the title of the currently active window
        """
        if ACTIVITY_SYSTEM_ENABLED:
            if renpy.windows and pygetwindow.getActiveWindow():
                return pygetwindow.getActiveWindow().title

            elif renpy.linux:
                return Xlib.display.Display().get_input_focus().focus.get_wm_name()

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
            for regex, activity in WINDOW_NAME_REGEX_ACTIVITY_MAP.items():
                if re.search(regex, window_name):
                    if not has_player_done_activity(int(activity)):
                        store.persistent.jn_activity_used_programs.append(int(activity))

                    return activity

        return JNActivities.unknown

    def has_player_done_activity(activity):
        """
        Returns True if the player has previously partook in the given activity.

        IN:
            - activity - The JNActivities activity to check
        """
        return int(activity) in store.persistent.jn_activity_used_programs

    def taskbar_flash(flash_count=2, flash_frequency_milliseconds=750):
        """
        Flashes the JN icon on the taskbar (Windows only).
        By default, the icon will flash twice with a healthy delay between each flash, before remaining lit.

        IN:
            - flash_count - The amount of times to flash the icon before the icon remains in a lit state
            - flash_frequency_milliseconds - The amount of time to wait between each flash, in milliseconds
        """
        if renpy.windows:
            win32gui.FlashWindowEx(__get_jn_window_hwnd(), 6, flash_count, flash_frequency_milliseconds)

    def notifyPopup(message):
        """
        Displays a toast-style popup (Windows and Linux only).

        IN:
            - title - The title to display on the window
            - message - The message to display in the window
        """
        if renpy.windows or renpy.linux:
            notification.notify(
                title="Natsuki",
                message=message,
                app_name=store.config.window_title,
                app_icon=(renpy.config.gamedir + '/mod_assets/jnlogo.ico'),
                timeout=5
            )
