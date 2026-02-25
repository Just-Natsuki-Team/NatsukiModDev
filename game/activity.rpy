default persistent._jn_activity_used_programs = []

init python in jn_activity:
    from Enum import Enum
    from plyer import notification
    import sys
    import random
    import re
    import store
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    ACTIVITY_SYSTEM_ENABLED = True # Determines if the system supports activity detection
    LAST_ACTIVITY = None

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
        # macOS: enable, but do all osascript work off the main thread (to avoid UI stalls)
        import subprocess
        import time

        ACTIVITY_SYSTEM_ENABLED = True

        # Refresh frequency (seconds). Higher = less churn; lower = more responsive.
        _JN_MAC_CACHE_TTL = 0.75

        # Cached value returned instantly from getCurrentWindowName().
        _jn_mac_cached_value = ""
        _jn_mac_cached_at = 0.0
        _jn_mac_refresh_in_flight = False

        # Default to title mode (macOS user must have approved DDLC + JN system permissions)
        MAC_READ_WINDOW_TITLE = True

        # Tracks whether osascript appears usable. None = unknown (never tested yet).
        _jn_mac_osascript_ok = None

        def _jn_mac_run_osascript(script_text):
            """
            Runs osascript with a single -e script string.
            Returns stdout (str) or "" on failure.
            IMPORTANT: This may be slow; do NOT call it on the main thread.
            """
            try:
                p = subprocess.Popen(
                    ["/usr/bin/osascript", "-e", script_text],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                out, err = p.communicate()
                if out is None:
                    return ""
                return out.strip()
            except Exception:
                return ""

        def _jn_mac_get_frontmost_app_name():
            return _jn_mac_run_osascript(
                'tell application "System Events" to get name of first application process whose frontmost is true'
            )

        def _jn_mac_get_frontmost_window_title():
            return _jn_mac_run_osascript(
                'tell application "System Events" to tell (first application process whose frontmost is true) to get name of front window'
            )

        def _jn_mac_refresh_cache_worker():
            global _jn_mac_cached_value, _jn_mac_cached_at, _jn_mac_refresh_in_flight, _jn_mac_osascript_ok

            try:
                # First time: sanity-check osascript inside the worker thread.
                if _jn_mac_osascript_ok is None:
                    ok = _jn_mac_run_osascript('return "ok"')
                    _jn_mac_osascript_ok = (ok == "ok")

                if not _jn_mac_osascript_ok:
                    _jn_mac_cached_value = ""
                    _jn_mac_cached_at = time.time()
                    return

                app_name = _jn_mac_get_frontmost_app_name()
                win_title = ""
                url = ""

                # Transient blanks happen. Retry once quickly.
                if not app_name:
                    time.sleep(0.05)
                    app_name = _jn_mac_get_frontmost_app_name()

                # Prefer app-native browser info when possible.
                if MAC_READ_WINDOW_TITLE and app_name == "Safari":
                    win_title = _jn_mac_run_osascript('tell application "Safari" to get name of front document')
                    url = _jn_mac_run_osascript('tell application "Safari" to get URL of front document')

                    if (not win_title) or (not url):
                        time.sleep(0.05)
                        if not win_title:
                            win_title = _jn_mac_run_osascript('tell application "Safari" to get name of front document')
                        if not url:
                            url = _jn_mac_run_osascript('tell application "Safari" to get URL of front document')

                elif MAC_READ_WINDOW_TITLE:
                    # Generic fallback
                    win_title = _jn_mac_get_frontmost_window_title()

                if win_title and url and app_name:
                    # Include URL so regex matching can key off domains.
                    value = "{0} ({1}) - {2}".format(win_title, url, app_name)
                elif win_title and app_name:
                    value = "{0} - {1}".format(win_title, app_name)
                elif win_title:
                    value = win_title
                elif app_name:
                    value = app_name
                else:
                    value = ""

                _jn_mac_cached_value = value
                _jn_mac_cached_at = time.time()

            finally:
                _jn_mac_refresh_in_flight = False

        def _jn_mac_kick_refresh_if_needed(force=False):
            global _jn_mac_refresh_in_flight

            now = time.time()

            if _jn_mac_refresh_in_flight:
                return

            if (not force) and ((now - _jn_mac_cached_at) < _JN_MAC_CACHE_TTL):
                return

            _jn_mac_refresh_in_flight = True

            # Run refresh off the main thread so input never stalls.
            try:
                renpy.invoke_in_thread(_jn_mac_refresh_cache_worker)
            except Exception:
                _jn_mac_refresh_in_flight = False

        # Warm the cache once at boot, in the worker thread.
        _jn_mac_kick_refresh_if_needed(force=True)

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
        ddlc_moe = 13
        takeaway_food = 14
        instagram = 15
        music_creation = 16
        reddit = 17
        fourchan = 18
        monika_after_story = 19
        just_yuri = 20
        forever_and_ever = 21
        video_applications = 22
        e_commerce = 23
        recording_software = 24

        def __int__(self):
            return self.value

    class JNPlayerActivity:
        """
        This class represents some activity a player can be doing, outside of JN, to be used in notifications/dialogue.
        """
        def __init__(
            self,
            activity_type,
            window_name_regex=None,
            notify_text=None
        ):
            """
            Initialises a new instance of JNPlayerActivity.

            IN:
                - activity_type - The JNActivities type of this JNPlayerActivity
                - window_name_regex - The window regex that must be matched for this activity to be the current activity
                - notify_text - List of text Natsuki may react with via popup, if this activity is detected
            """
            self.activity_type = activity_type
            self.window_name_regex = window_name_regex
            self.notify_text = notify_text

        def getRandomNotifyText(self):
            """
            Returns the substituted reaction text for this activity.
            """
            if self.notify_text and len(self.notify_text) > 0:
                store.happy_emote = jn_utils.getRandomHappyEmoticon()
                store.angry_emote = jn_utils.getRandomAngryEmoticon()
                store.sad_emote = jn_utils.getRandomSadEmoticon()
                store.tease_emote = jn_utils.getRandomTeaseEmoticon()
                store.confused_emote = jn_utils.getRandomConfusedEmoticon()
                return renpy.substitute(random.choice(self.notify_text))

            return None

    class JNActivityManager:
        """
        Management class for handling activities.
        """
        def __init__(self):
            self.registered_activities = {}
            self.last_activity = JNPlayerActivity(
                activity_type=JNActivities.unknown
            )
            self.__enabled = False

        def setIsEnabled(self, state):
            """
            Sets the enabled state, determining if activity detection is active.

            IN:
                - state - bool enabled state to set
            """
            self.__enabled = state

        def getIsEnabled():
            """
            Gets the enabled state.
            """
            return self.__enabled

        def registerActivity(self, activity):
            self.registered_activities[activity.activity_type] = activity

        def getActivityFromType(self, activity_type):
            """
            Returns the activity corresponding to the given JNActivities activity type, or None if it doesn't exist
            """
            if activity_type in self.registered_activities:
                return self.registered_activities[activity_type]

            return None

        def getCurrentActivity(self, delay=0):
            """
            Returns the current JNActivities state of the player as determined by the currently active window,
            and if the activity is registered.

            IN:
                - delay - Force RenPy to sleep before running the check. This allows time to swap windows from JN for debugging.
            OUT:
                - JNPlayerActivity type for the active window, or None
            """
            if delay is not 0:
                store.jnPause(delay, hard=True)

            if not self.__enabled:
                return self.getActivityFromType(JNActivities.unknown)

            window_name = getCurrentWindowName()
            if window_name is not None:
                window_name = getCurrentWindowName().lower()
                for activity in self.registered_activities.values():
                    if activity.window_name_regex:
                        if re.search(activity.window_name_regex, window_name) is not None:

                            if not self.hasPlayerDoneActivity(int(activity.activity_type)):
                                store.persistent._jn_activity_used_programs.append(int(activity.activity_type))

                            return activity

            return self.getActivityFromType(JNActivities.unknown)

        def hasPlayerDoneActivity(self, activity_type):
            """
            Returns True if the player has previously partook in the given activity.

            IN:
                - activity - The JNActivities activity to check
            """
            return int(activity_type) in store.persistent._jn_activity_used_programs

    ACTIVITY_MANAGER = JNActivityManager()

    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.unknown
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.coding,
        window_name_regex="(- visual studio|- notepad/+/+|- atom|- brackets|vim|eclipse|^github desktop$|^sourcetree$|- scratch)",
        notify_text=[
            "You're seriously such a nerd, [player].",
            "You forgot a semicolon! [tease_emote]",
            "How do you even read all that stuff?!",
            "Well? Does it work? [tease_emote]",
            "What even IS that mumbo-jumbo...",
            "I don't even know where I'd start with coding stuff...",
            "More programming stuff?",
            "I see, I see. You're on nerd duty today! [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.discord,
        window_name_regex="(- discord)",
        notify_text=[
            "Someone's a social butterfly, huh?",
            "Yeah, yeah. Chat it up, [player]~",
            "Man... I wish I had some emotes... [sad_emote]",
            "Maybe I should start a server...",
            "Huh? Did someone message you?",
            "Eh? Did someone just ping you? [confused_emote]",
            "Don't just spend all day yapping away on there! [angry_emote]",
            "I'm not THAT boring to talk to, am I? [sad_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.music_applications,
        window_name_regex="(^spotify$|^spotify premium$|^groove$|^zune$|^itunes$|^musicbee$|^aimp$|^winamp$)",
        notify_text=[
            "You better play something good!",
            "New playlist, [player]?",
            "Play some tunes, [player]!",
            "When do I get to pick something, huh? [angry_emote]",
            "Hit it, [player]! [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.gaming,
        window_name_regex="(^steam$|^origin$|^battle.net$|- itch.io)",
        notify_text=[
            "You better not be spending all day on that! [angry_emote]",
            "Just... remember to take breaks, alright? [sad_emote]",
            "Gonna play something?",
            "You could have just said if you were bored... [sad_emote]",
            "You better not play anything weird...",
            "Game time, huh?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.youtube,
        window_name_regex="(- youtube)",
        notify_text=[
            "YouTube, huh? I think Sayori uploaded something once...",
            "Oh! Oh! Let me watch! [happy_emote]",
            "What's on, [player]?",
            "You better not be watching anything weird...",
            "Just... no reaction videos. Please. [angry_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.github_jn,
        window_name_regex="(just-natsuki-team/natsukimoddev)",
        notify_text=[
            "Hey! I know this place!",
            "I knew you'd help me out! Ehehe.",
            "Oh! Oh! It's my website!",
            "I heard only complete nerds come here... [tease_emote]",
            "Ehehe. Thanks for stopping by!",
            "Hey! It's geek-hub! [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.artwork,
        window_name_regex="(clip studio paint|photoshop|krita|gimp|paint.net|paint tool sai|medibang|- paint)",
        notify_text=[
            "Draw for me, [player]! Ehehe.",
            "I was never any good at artwork... [sad_emote]",
            "You're drawing? [confused_emote]",
            "Oh! Oh! What're you drawing?",
            "Eh? What're you drawing? [confused_emote]",
            "Draw me! Draw me!!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.anime_streaming,
        window_name_regex="(^crunchyroll$)",
        notify_text=[
            "What's the flavor of the month?",
            "So many options...",
            "I still don't see Parfait Girls anywhere...",
            "Infinite choices! Ehehe.",
            "I could waste DAYS here... [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.work_applications,
        window_name_regex="(- word| - excel| - powerpoint|openoffice|libreoffice)",
        notify_text=[
            "Ew... work...",
            "You're sure you gotta do this now, [player]? [confused_emote]",
            "Ugh... reminds me of my school assignments...",
            "Great... now I'm getting flashbacks of my group projects.",
            "Booo-ring! Ehehe.",
            "Reminds me of schoolwork... [angry_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.twitter,
        window_name_regex="(/ twitter)",
        notify_text=[
            "There's so much cool art here!",
            "I swear I could waste hours just scrolling here...",
            "Oh! Oh! Am I trending?",
            "I should probably check my Twitter, huh?",
            "Oh man! I gotta check on my feed! [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.deviantart,
        window_name_regex="(deviantart - |\| deviantart)",
        notify_text=[
            "So. Much. Art.",
            "Oh! Do you post here, [player]?",
            "Just... don't search up anything weird...",
            "I... know this place.",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.manga,
        window_name_regex="(- mangadex|- mangasee|- mangakot)",
        notify_text=[
            "What's the flavor of the month?",
            "No Parfait Girls here... [sad_emote]",
            "Oh! What're you reading? [happy_emote]",
            "Looking for an EXPERT opinion? Ehehe.",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.ddlc_moe,
        window_name_regex="(doki doki literature club! -)",
        notify_text=[
            "...",
            "I... don't like this website.",
            "Uuuuuu... do you HAVE to visit this place?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.takeaway_food,
        window_name_regex=(
            "((uber eats[a-zA-Z]*| food delivery)|( - uber eats)|(deliveroo - takeaway food delivery)"
            "|(\| domino's pizza)|(\| pizza hut)|(\| grubhub)|(doordash food delivery & takeout -))"
        ),
        notify_text=[
            "H-hey! Less of the junk! [angry_emote]",
            "Cooking isn't THAT hard, you know... [angry_emote]",
            "You better not be making a habit of that...",
            "[player]! Think of your wallet! Jeez... [confused_emote]",
            "[player]... come on... [sad_emote]",
            "Just... don't make a habit of this. [angry_emote] Please?",
            "Ew... junk food...",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.instagram,
        window_name_regex="(• instagram photos and videos)",
        notify_text=[
            "So who are YOU stalking, huh? [tease_emote]",
            "Huh? Do you post here, [player]?",
            "You post here much, [player]?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.music_creation,
        window_name_regex="(cubase|fl studio|reaper|mixcraft|studio one|logic pro|garageband|cakewalk|pro tools)",
        notify_text=[
            "Ooooh! You're making beats?",
            "Making some tunes? [confused_emote]",
            "...Should I start taking NOTES? Ehehe.",
            "Oh! Oh! I GOTTA listen to this!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.reddit,
        window_name_regex="(reddit - dive into anything)",
        notify_text=[
            "I hope you don't believe everything you read...",
            "Eh? What's in the news?",
            "Huh? Did something happen?",
            "You making a post, [player]? [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.fourchan,
        window_name_regex="(- 4chan|^4chan$)"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.monika_after_story,
        window_name_regex="^monika after story$"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.just_yuri,
        window_name_regex="(^just yuri$|^just yuri \(beta\)$)"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.forever_and_ever,
        window_name_regex="^forever & ever$"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.video_applications,
        window_name_regex="(- vlc media player)",
        notify_text=[
            "What're you watching, [player]? [confused_emote]",
            "You watching something, [player]? [confused_emote]",
            "Oh hey! Any funny video clips? [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.e_commerce,
        window_name_regex="(^amazon.[A-Za-z]{2,6}|\| ebay)",
        notify_text=[
            "Just... don't go overboard. [angry_emote]",
            "Shopping, huh? [tease_emote]",
            "Run out of something again? Ehehe.",
            "Oh? You gotta grab something? [confused_emote]",
            "Money to burn, huh?"
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.recording_software,
        window_name_regex="(^obs [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}|^bandicam [0-9]{4}|^fraps|^xsplit broadcaster$|- lightstream studio$)",
        notify_text=[
            "W-wait... what kind of app is that, [player]? [confused_emote]",
            "Wait a second... is that some kind of recorder?",
            "I-I hope you aren't recording me, [player]. [angry_emote]",
            "Huh? What kind of program is that, [player]? [confused_emote]",
            "What are you recording, [player]...? [confused_emote]"
        ]
    ))

    # macOS-only: extend detection coverage without changing Windows/Linux behavior
    if renpy.macintosh:
        def _jn__strip_outer_parens(s):
            if not s:
                return ""
            s = s.strip()
            if len(s) >= 2 and s[0] == "(" and s[-1] == ")":
                return s[1:-1]
            return s

        def _jn__extend_activity_regex(activity_type, extra_regex):
            try:
                act = ACTIVITY_MANAGER.getActivityFromType(activity_type)
            except Exception:
                act = None

            if act is None:
                return

            try:
                old = act.window_name_regex
            except Exception:
                old = None

            old_inner = _jn__strip_outer_parens(old)
            extra_inner = _jn__strip_outer_parens(extra_regex)

            if old_inner and extra_inner:
                act.window_name_regex = "(" + old_inner + "|" + extra_inner + ")"
            elif extra_inner:
                act.window_name_regex = "(" + extra_inner + ")"

        def _jn_patch_activity_entries_all():
            try:
                # Anime streaming: Crunchyroll, HiDive, RetroCrush
                # Suggestion: include HiDive, RetroCrush for Windows/Linux
                _jn__extend_activity_regex(
                    JNActivities.anime_streaming,
                    "(crunchyroll|crunchyroll\\.com|www\\.crunchyroll\\.com|hidive|hi\\s*dive|hidive\\.com|retrocrush|retrocrush\\.tv|retrocrush\\.com)"
                )

                # Work apps: Apple Pages, Numbers, Keynote
                _jn__extend_activity_regex(
                    JNActivities.work_applications,
                    "( - pages| - numbers| - keynote|^pages$|^numbers$|^keynote$)"
                )

                # Music players: Apple Music, Marvis Pro
                _jn__extend_activity_regex(
                    JNActivities.music_applications,
                    "(^music$| - music|marvis pro|^marvis$| - marvis|marvis)"
                )

                # Coding: TextEdit, Sublime Text, CotEditor, Xcode
                _jn__extend_activity_regex(
                    JNActivities.coding,
                    "(^textedit$| - textedit|textedit|^sublime text$| - sublime text|sublime text|^coteditor$| - coteditor|coteditor|^xcode$| - xcode|xcode)"
                )

                # Music creation: GarageBand (robust variants)
                _jn__extend_activity_regex(
                    JNActivities.music_creation,
                    "(^garageband$| - garageband|garageband)"
                )

                # Artwork: Pixelmator Pro
                _jn__extend_activity_regex(
                    JNActivities.artwork,
                    "(pixelmator pro|pixelmator)"
                )

                # Video applications: IINA, Infuse
                _jn__extend_activity_regex(
                    JNActivities.video_applications,
                    "(^iina$| - iina|iina|^infuse$| - infuse|infuse)"
                )

            except Exception:
                pass

        _jn_patch_activity_entries_all()

    def _getJNWindowHwnd():
        """
        Gets the hwnd of the JN game window (Windows only).

        OUT:
            - int representing the hwnd of the JN game window
        """
        def checkJNWindow(hwnd, ctx):
            """
            Returns JNWindowFoundException containing the hwnd of the JN game window.
            """
            if win32gui.GetWindowText(hwnd) == store.config.window_title:
                raise JNWindowFoundException(hwnd)

        try:
            # Iterate through all windows, comparing titles to find the JN game window
            win32gui.EnumWindows(checkJNWindow, None)

        except JNWindowFoundException as exception:
            return exception.hwnd

    def getJNWindowActive():
        """
        Returns True if the currently active window is the JN game window, otherwise False.
        """
        return getCurrentWindowName() == store.config.window_title

    def getCurrentWindowName(delay=0):
        """
        Gets the title of the currently active window.

        IN:
            - delay - int amount of seconds to wait before checking window

        OUT:
            - str representing the title of the currently active window
        """
        global ACTIVITY_SYSTEM_ENABLED
        if ACTIVITY_SYSTEM_ENABLED:
            if delay is not 0:
                store.jnPause(delay, hard=True)

            try:
                if renpy.windows and pygetwindow.getActiveWindow():
                    return pygetwindow.getActiveWindow().title

                elif renpy.linux:
                    # This is incredibly messy
                    focus = Xlib.display.Display().get_input_focus().focus

                    if not isinstance(focus, int):
                        # We have a window
                        wm_name = focus.get_wm_name()
                        wm_class = focus.get_wm_class()

                        if isinstance(wm_name, basestring) and wm_name != "":
                            # Window has a name, return it
                            return wm_name

                        elif wm_class is None and (wm_name is None or wm_name == ""):
                            # Try and get the parent of the window
                            focus = focus.query_tree().parent

                            if not isinstance(focus, int):
                                # Try and get the wm_name of the parent and return that instead
                                wm_name = focus.get_wm_name()
                                return wm_name if isinstance(wm_name, basestring) else ""

                        elif isinstance(wm_class, tuple):
                            # Just return the parent name
                            return str(wm_class[0])

                        # Fall through

                elif renpy.macintosh:
                    # macOS: never block UI; return cached and refresh in worker thread
                    ACTIVITY_SYSTEM_ENABLED = True
                    try:
                        _jn_mac_kick_refresh_if_needed()
                    except Exception:
                        pass
                    try:
                        return _jn_mac_cached_value
                    except Exception:
                        return ""

            except AttributeError as exception:
                ACTIVITY_SYSTEM_ENABLED = False
                jn_utils.log("Failed to identify activity: {0}; only x11 sessions are supported. Disabling activity system for session.".format(repr(exception)))
                return ""

            except Exception as exception:
                ACTIVITY_SYSTEM_ENABLED = False
                jn_utils.log("Failed to identify activity: {0}. Disabling activity system for session.".format(repr(exception)))
                return ""

        return ""

    def taskbarFlash(flash_count=2, flash_frequency_milliseconds=750):
        """
        Flashes the JN icon on the taskbar (Windows only).
        By default, the icon will flash twice with a healthy delay between each flash, before remaining lit.

        IN:
            - flash_count - The amount of times to flash the icon before the icon remains in a lit state
            - flash_frequency_milliseconds - The amount of time to wait between each flash, in milliseconds
        """
        if renpy.windows:
            win32gui.FlashWindowEx(_getJNWindowHwnd(), 6, flash_count, flash_frequency_milliseconds)

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
                timeout=7
            )
