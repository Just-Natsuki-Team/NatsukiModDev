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
    
    ACTIVITY_SYSTEM_ENABLED = True
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
        ddlc_moe = 13
        takeaway_food = 14
        instagram = 15
        music_creation = 16
        reddit = 17
        fourchan = 18
        monika_after_story = 19
        just_yuri = 20
        forever_and_ever = 21

        def __int__(self):
            return self.value

    __WINDOW_NAME_REGEX_ACTIVITY_MAP = {
        "(- visual studio|- notepad/+/+|- atom|- brackets|vim|eclipse|^github desktop$|^sourcetree$)": JNActivities.coding,
        "(- discord)": JNActivities.discord,
        "(^spotify$|^spotify premium$|^groove$|^zune$|^itunes$)": JNActivities.music_applications,
        "(^steam$|^origin$|^battle.net$)": JNActivities.gaming,
        "(- youtube)": JNActivities.youtube,
        "(just-natsuki-team/natsukimoddev)": JNActivities.github_jn,
        "(clip studio paint|photoshop|krita|gimp|paint.net|paint tool sai|medibang)": JNActivities.artwork,
        "(^crunchyroll$)": JNActivities.anime_streaming,
        "(- word| - excel| - powerpoint|openoffice|libreoffice)": JNActivities.work_applications,
        "(/ twitter)": JNActivities.twitter,
        "(deviantart - |\| deviantart)": JNActivities.deviantart,
        "(- mangadex|- mangasee|- mangakot)": JNActivities.manga,
        "(Doki Doki Literature Club! -)": JNActivities.ddlc_moe,
        (
            "((Uber Eats[a-zA-Z]*| Food delivery)|( - Uber Eats)|(Deliveroo - Takeaway Food Delivery)"
            "|(\| Domino's Pizza)|(\| Pizza Hut)|(\| GrubHub)|(DoorDash Food Delivery & Takeout -))"
        ): JNActivities.takeaway_food,
        "(• Instagram photos and videos)": JNActivities.instagram,
        "(cubase|fl studio|reaper|mixcraft|studio one|logic pro|garageband|cakewalk|pro tools)": JNActivities.music_creation,
        "(Reddit - Dive into anything)": JNActivities.reddit,
        "(- 4chan|^4chan$)": JNActivities.fourchan,
        "^monika after story$": JNActivities.monika_after_story,
        "(^just yuri$|^just yuri \(beta\)$)": JNActivities.just_yuri,
        "^forever & ever$": JNActivities.forever_and_ever,
    }

    __ACTIVITY_NOTIFY_MESSAGE_MAP = {
        JNActivities.coding: [
            "You're seriously such a nerd, [player].",
            "You forgot a semicolon! {0}".format(random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)),
            "How do you even read all that stuff?!",
            "Well? Does it work? {0}".format(random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)),
            "What even IS that mumbo jumbo...",
        ],
        JNActivities.discord: [
            "Someone's a social butterfly, huh?",
            "Yeah, yeah. Chat it up, [player]~",
            "Man... I wish I had some emotes... {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Maybe I should start a server...",
            "Huh? Did someone message you?",
        ],
        JNActivities.music_applications: [
            "You better play something good!",
            "New playlist, [player]?",
            "Play some tunes, [player]!",
            "When do I get to pick something, huh? {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
        ],
        JNActivities.gaming: [
            "You better not be spending all day on that! {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "Just... remember to take breaks, alright? {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Gonna play something?",
            "You could have just said if you were bored... {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "You better not play anything weird...",
        ],
        JNActivities.youtube: [
            "YouTube, huh? I think Sayori uploaded something once...",
            "Oh! Oh! Let me watch!".format(random.choice(jn_globals.DEFAULT_HAPPY_EMOTICONS)),
            "What's on, [player]?",
            "You better not be watching anything weird...",
            "Just... no reaction videos. Please. {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
        ],
        JNActivities.github_jn: [
            "Hey! I know this place!",
            "I knew you'd help me out! Ehehe.",
            "Oh! Oh! It's my website!",
            "I heard only complete nerds come here... {0}".format(random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)),
            "Ehehe. Thanks for stopping by!",
            "Hey! It's geek-hub! {0}".format(random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)),
        ],
        JNActivities.artwork: [
            "Draw for me, [player]! Ehehe.",
            "I was never any good at artwork... {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "You're drawing? {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
            "Oh! Oh! What're you drawing?",
            "Eh? What're you drawing? {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
            "Draw me! Draw me!!",
        ],
        JNActivities.anime_streaming: [
            "What's the flavor of the month?",
            "So many options...",
            "I still don't see Parfait Girls anywhere...",
            "Infinite choices! Ehehe.",
            "I could waste DAYS here... {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
        ],
        JNActivities.work_applications: [
            "Ew... work...",
            "You're sure you gotta do this now, [player]? {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
            "Ugh... reminds me of my school assignments...",
            "Great... now I'm getting flashbacks of my group projects.",
            "Booo-ring! Ehehe.",
            "Reminds me of schoolwork... {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
        ],
        JNActivities.twitter: [
            "There's so much cool art here!",
            "I swear I could waste hours just scrolling here...",
            "Oh! Oh! Am I trending?",
            "I should probably check my Twitter, huh?",
            "Oh man! I gotta check on my feed! {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
        ],
        JNActivities.deviantart: [
            "So. Much. Art.",
            "Oh! Do you post here, [player]?",
            "Just... don't search up anything weird...",
            "I... know this place.",
        ],
        JNActivities.manga: [
            "What's the flavor of the month?",
            "No Parfait Girls here... {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Oh! What're you reading? {0}".format(random.choice(jn_globals.DEFAULT_HAPPY_EMOTICONS)),
            "Looking for an EXPERT opinion? Ehehe.",
        ],
        JNActivities.ddlc_moe: [
            "...",
            "I... don't like this website.",
            "Uuuuuu... do you HAVE to visit this place?",
        ],
        JNActivities.takeaway_food: [
            "H-hey! Less of the junk! {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "Cooking isn't THAT hard, you know... {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "You better not be making a habit of that...",
            "[player]! Think of your wallet! Jeez... {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
            "[player]... come on... {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Just... don't make a habit of this. {0} Please?".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
        ],
        JNActivities.instagram: [
            "So who are YOU stalking, huh? {0}".format(random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)),
            "Huh? Do you post here, [player]?",
            "You post here much, [player]?",
        ],
        JNActivities.music_creation: [
            "Ooooh! You're making beats?",
            "Making some tunes? {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
            "...Should I start taking NOTES? Ehehe.",
            "Oh! Oh! I GOTTA listen to this!",
        ],
        JNActivities.reddit: [
            "I hope you don't believe everything you read...",
            "Eh? What's in the news?",
            "Huh? Did something happen?",
            "You making a post, [player]? {0}".format(random.choice(jn_globals.DEFAULT_CONFUSED_EMOTICONS)),
        ]
    }

    def __getJNWindowHwnd():
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

    def getCurrentWindowName():
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

    def getCurrentActivity(delay=0):
        """
        Returns the current JNActivities state of the player as determined by the currently active window,
        and if an entry exists in the __WINDOW_NAME_REGEX_ACTIVITY_MAP, or JNActivities.unknown if no match was found.
        IN:
            - delay - Force RenPy to sleep before running the check. This allows time to swap windows from JN for debugging.
        OUT:
            - JNActivities type for the active window, or JNActivities.unknown
        """
        if delay is not 0:
            renpy.pause(delay)

        window_name = getCurrentWindowName()
        if window_name is not None:
            window_name = getCurrentWindowName().lower()
            for regex, activity in __WINDOW_NAME_REGEX_ACTIVITY_MAP.items():
                if re.search(regex, window_name):
                    if not hasPlayerDoneActivity(int(activity)):
                        store.persistent._jn_activity_used_programs.append(int(activity))

                    return activity

        return JNActivities.unknown

    def hasPlayerDoneActivity(activity):
        """
        Returns True if the player has previously partook in the given activity.

        IN:
            - activity - The JNActivities activity to check
        """
        return int(activity) in store.persistent._jn_activity_used_programs

    def taskbarFlash(flash_count=2, flash_frequency_milliseconds=750):
        """
        Flashes the JN icon on the taskbar (Windows only).
        By default, the icon will flash twice with a healthy delay between each flash, before remaining lit.

        IN:
            - flash_count - The amount of times to flash the icon before the icon remains in a lit state
            - flash_frequency_milliseconds - The amount of time to wait between each flash, in milliseconds
        """
        if renpy.windows:
            win32gui.FlashWindowEx(__getJNWindowHwnd(), 6, flash_count, flash_frequency_milliseconds)

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

    def getActivityNotifyQuote(activity):
        """
        Gets a random quote related to the given JNActivities activity, or None if none are defined.

        IN:
            - activity - The JNActivities activity to get a corresponding quote for

        OUT:
            - Random quote matching the given activity, or None if the activity isn't defined
        """
        if activity in __ACTIVITY_NOTIFY_MESSAGE_MAP:
            return renpy.substitute(random.choice(__ACTIVITY_NOTIFY_MESSAGE_MAP.get(activity)))
        
        return None
