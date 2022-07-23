default persistent._event_database = dict()
default persistent._jn_holiday_list = dict()
default persistent._jn_holiday_completion_states = dict()

# Background decorations
image deco balloons = "mod_assets/deco/balloons.png"

# Foreground props
image prop poetry_attempt = "mod_assets/props/poetry_attempt.png"
image prop parfait_manga_held = "mod_assets/props/parfait_manga_held.png"
image prop renpy_for_dummies_book_held = "mod_assets/props/renpy_for_dummies_book_held.png"
image prop a_la_mode_manga_held = "mod_assets/props/a_la_mode_manga_held.png"
image prop strawberry_milkshake = "mod_assets/props/strawberry_milkshake.png"
image prop step_by_step_manga_held = "mod_assets/props/step_by_step_manga_held.png"
image prop cake lit = "mod_assets/props/cake_lit.png"
image prop cake unlit = "mod_assets/props/cake_unlit.png"

init python in jn_events:
    import datetime
    from Enum import Enum
    import random
    import store
    import store.audio as audio
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    JN_EVENT_DECO_ZORDER = 2
    JN_EVENT_PROP_ZORDER = 4
    JN_EVENT_FADE_ZORDER = 10

    EVENT_MAP = dict()

    __ALL_HOLIDAYS = {}

    class JNHolidayTypes(Enum):
        new_years_day = 1
        easter = 2
        halloween = 3
        christmas_eve = 4
        christmas_day = 5
        new_years_eve = 6
        natsuki_birthday = 7
        player_birthday = 8
        anniversary = 9
        valentines_day = 10

        def __str__(self):
            return self.name

    class JNHoliday():
        """
        Describes a holiday event that a user can experience, once per year.
        """
        def __init__(
            self,
            label,
            holiday_type,
            conditional,
            affinity_range,
            natsuki_sprite_code,
            bgm=None,
            deco_list=[],
            prop_list=[],
            priority=0
        ):
            """
            Constructor.

            IN:
                - label - The name used to uniquely identify this wearable and refer to it internally
                - holiday_type - The JNHolidayTypes type of this holiday
                - conditional - Python statement that must evaluate to True for this holiday to be picked when filtering
                - affinity_range - The affinity range that must be satisfied for this holiday to be picked when filtering
                - natsuki_sprite_code - The sprite code to show for Natsuki when the holiday is revealed
                - bgm - The optional music to play when the holiday is revealed 
                - deco_list - Optional list of deco images to show when setting up
                - prop_list - Optional list of prop images to show when setting up
                - priority - Optional priority value; holidays with lower values are shown first
            """
            self.label = label
            self.is_seen = False
            self.holiday_type = holiday_type
            self.conditional = conditional
            self.affinity_range = affinity_range
            self.natsuki_sprite_code = natsuki_sprite_code
            self.bgm = bgm
            self.deco_list = deco_list
            self.prop_list = prop_list
            self.priority = priority

        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each holiday from the persistent.
            """
            global __ALL_HOLIDAYS
            for holiday in __ALL_HOLIDAYS.itervalues():
                holiday.__load()

        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each holiday to the persistent.
            """
            global __ALL_HOLIDAYS
            for holiday in __ALL_HOLIDAYS.itervalues():
                holiday.__save()

        @staticmethod
        def filterHolidays(
            holiday_list,
            holiday_types=None,
            affinity=None,
            holiday_completion_state=None
        ):
            """
            Returns a filtered list of holidays, given an holiday list and filter criteria.

            IN:
                - holiday_list - the list of JNHoliday objects to query
                - holiday_types - list of JNHolidayTypes the holiday must be in
                - affinity - minimum affinity state the holiday must have
                - holiday_completion_state - boolean state the completion state corresponding to each holiday must be

            OUT:
                - list of JNWearable child wearables matching the search criteria
            """
            return [
                _holiday
                for _holiday in holiday_list
                if _holiday.__filterHoliday(
                    holiday_types,
                    affinity,
                    holiday_completion_state
                )
            ]

        def asDict(self):
            """
            Exports a dict representation of this holiday; this is for data we want to persist.

            OUT:
                dictionary representation of the holiday object
            """
            return {
                "is_seen": self.is_seen
            }

        def currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this holidays's affinity_range

            IN:
                affinity_state - Affinity state to test if the holidays can be shown in. If None, the current affinity state is used.
                    (Default: None)
            OUT:
                True if the current affinity is within range. False otherwise
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()

            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)

        def __load(self):
            """
            Loads the persisted data for this holiday from the persistent.
            """
            if store.persistent._jn_holiday_list[self.label]:
                self.is_seen = store.persistent._jn_holiday_list[self.label]["is_seen"]

        def __save(self):
            """
            Saves the persistable data for this holiday to the persistent.
            """
            store.persistent._jn_holiday_list[self.label] = self.asDict()

        def __filterHoliday(
            self,
            holiday_types=None,
            affinity=None,
            holiday_completion_state=None
        ):
            """
            Returns True, if the holiday meets the filter criteria. Otherwise False.

            IN:
                - holiday_types - list of JNHolidayTypes the holiday must be in
                - affinity - minimum affinity state the holiday must have

            OUT:
                - True, if the holiday meets the filter criteria. Otherwise False
            """
            if self.is_seen:
                return False

            elif holiday_types and not self.holiday_type in holiday_types:
                return False

            elif affinity and not self.currAffinityInAffinityRange(affinity):
                return False

            elif (
                holiday_completion_state
                and store.persistent._jn_holiday_completion_states[str(self.holiday_type)]
            ):
                return False

            elif not eval(self.conditional):
                return False

            return True

        def run(self):
            """
            Sets up all visuals for this holiday, before revealing everything to the player.
            """
            for prop in self.prop_list:
                renpy.show(name="prop {0}".format(prop), zorder=JN_EVENT_PROP_ZORDER)

            for deco in self.deco_list:
                renpy.show(name="deco {0}".format(deco), zorder=JN_EVENT_DECO_ZORDER)

            kwargs = {
                "natsuki_sprite_code": self.natsuki_sprite_code
            }
            if self.bgm:
                kwargs.update({"bgm": self.bgm})

            jn_globals.force_quit_enabled = True
            displayVisuals(**kwargs)

        def complete(self):
            """
            Marks this holiday as complete, preventing it from being seen again until marked as unseen again.
            This should be run after a holiday has concluded, so a crash/quit after starting the holiday doesn't lock progression.
            """
            self.is_seen = True
            self.__save()
            store.persistent._jn_holiday_completion_states[str(self.holiday_type)]

    def __registerHoliday(holiday):
        """
        Registers a new holiday in the list of all holidays, allowing in-game access and persistency.
        """
        if holiday.label in __ALL_HOLIDAYS:
            jn_utils.log("Cannot register holiday name: {0}, as a holiday with that name already exists.".format(holiday.reference_name))

        else:
            __ALL_HOLIDAYS[holiday.label] = holiday
            if holiday.label not in store.persistent._jn_holiday_list:
                holiday.__save()

            else:
                holiday.__load()

    def getHoliday(holiday_name):
        """
        Returns the holiday for the given name, if it exists.

        IN:
            - holiday_name - str outfit name to fetch

        OUT: Corresponding JNHoliday if the holiday exists, otherwise None 
        """
        if holiday_name in __ALL_HOLIDAYS:
            return __ALL_HOLIDAYS[holiday_name]

        return None

    def isNewYearsDay(input_date=None):
        """
        Returns True if the input_date is New Year's Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_NEW_YEARS_DAY

    def isValentinesDay(input_date=None):
        """
        Returns True if the input_date is Valentine's Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_VALENTINES_DAY

    def isEaster(input_date=None):
        """
        Returns True if the input_date is Easter; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_EASTER

    def isHalloween(input_date=None):
        """
        Returns True if the input_date is Halloween; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_HALLOWEEN

    def isChristmasEve(input_date=None):
        """
        Returns True if the input_date is Christmas Eve; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_CHRISTMAS_EVE

    def isChristmasDay(input_date=None):
        """
        Returns True if the input_date is Christmas Day; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_CHRISTMAS_DAY

    def isNewYearsEve(input_date=None):
        """
        Returns True if the input_date is New Year's Eve; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_NEW_YEARS_EVE

    def isNatsukiBirthday(input_date=None):
        """
        Returns True if the input_date is Natsuki's birthday; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.JN_NATSUKI_BIRTHDAY

    def isPlayerBirthday(input_date=None):
        """
        Returns True if the input_date is the player's birthday; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if not store.persistent._jn_player_birthday_day_month:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        player_birthday = datetime.date(
            2020, # We use 2020 as it is a leap year
            store.persistent._jn_player_birthday_day_month[1],
            store.persistent._jn_player_birthday_day_month[0]
        )

        return (input_date.month == player_birthday.month and input_date.day == player_birthday.day)

    def isAnniversary(input_date=None):
        """
        Returns True if the input_date is the player and Natsuki's anniversary; otherwise False

        IN:
            - input_date - datetime object to test against. Defaults to the current date.
        """
        if not store.persistent._jn_player_anniversary_day_month:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        anniversary_date = datetime.date(
            2020, # We use 2020 as it is a leap year
            store.persistent._jn_player_anniversary_day_month[1],
            store.persistent._jn_player_anniversary_day_month[0]
        )

        return (input_date.month == anniversary_date.month and input_date.day == anniversary_date.day)

    def getHolidaysForDate(input_date=None):
        """
        Gets the holidays - if any - corresponding to the supplied date, or the current date by default.

        IN:
            - input_date - datetime object to test against. Defaults to the current date.

        OUT:
            - JNHoliday representing the holiday for the supplied date.
        """

        if input_date is None:
            input_date = datetime.datetime.today()

        elif not isinstance(input_date, datetime.date):
            raise TypeError("input_date for holiday check must be of type date; type given was {0}".format(type(input_date)))

        holidays = []

        if isNewYearsDay(input_date):
            holidays.append(JNHolidayTypes.new_years_day)

        if isValentinesDay(input_date):
            holidays.append(JNHolidayTypes.valentines_day)

        if isEaster(input_date):
            holidays.append(JNHolidayTypes.easter)

        if isHalloween(input_date):
            holidays.append(JNHolidayTypes.halloween)

        if isChristmasEve(input_date):
            holidays.append(JNHolidayTypes.christmas_eve)

        if isChristmasDay(input_date):
            holidays.append(JNHolidayTypes.christmas_day)

        if isChristmasEve(input_date):
            holidays.append(JNHolidayTypes.new_years_eve)

        if isNatsukiBirthday(input_date):
            holidays.append(JNHolidayTypes.natsuki_birthday)

        if isPlayerBirthday(input_date):
            holidays.append(JNHolidayTypes.player_birthday)

        if isAnniversary(input_date):
            holidays.append(JNHolidayTypes.anniversary)

        return holidays

    def getAllHolidays():
        """
        Returns a list of all holidays.
        """
        return __ALL_HOLIDAYS.itervalues()

    def selectEvent():
        """
        Picks and returns a single random event, or None if no events are left.
        """
        kwargs = dict()
        event_list = store.Topic.filter_topics(
            EVENT_MAP.values(),
            unlocked=True,
            affinity=store.Natsuki._getAffinityState(),
            is_seen=False,
            **kwargs
        )

        # Events are one-time only, so we sanity check here
        if len(event_list) > 0:
            return random.choice(event_list).label

        else:
            return None

    def selectHolidays():
        """
        Returns a list of all holidays with a corresponding incomplete persistent entry that apply for the current date, or None if no holidays apply
        """
        holiday_list = JNHoliday.filterHolidays(
            holiday_list=getAllHolidays(),
            holiday_types=getHolidaysForDate(),
            affinity=store.Natsuki._getAffinityState(),
            holiday_completion_state=False
        )

        if len(holiday_list) > 0:
            return holiday_list

        else:
            return None

    def resetHolidays():
        """
        Resets the is_seen state and corresponding completion state for all holidays.
        """
        for holiday in getAllHolidays():
            holiday.is_seen = False

        for holiday_type in JNHolidayTypes:
            if str(holiday_type) in store.persistent._jn_holiday_completion_states:
                store.persistent._jn_holiday_completion_states[str(holiday_type)] = False

    def displayVisuals(
        natsuki_sprite_code,
        bgm="mod_assets/bgm/just_natsuki.ogg"
    ):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
            - music_file_path - The str file path of the music to play upon revealing Natsuki; defaults to standard bgm
        """
        renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        renpy.hide("black")
        renpy.show_screen("hkb_overlay")
        renpy.play(filename=audio.light_switch, channel="audio")
        renpy.play(filename=bgm, channel="music")

        # Reveal
        renpy.hide("black")

    # Handle the holiday completion states on the persistent
    for holiday_type in JNHolidayTypes:
        if not str(holiday_type) in store.persistent._jn_holiday_completion_states:
            store.persistent._jn_holiday_completion_states[str(holiday_type)] = False

    # Holiday registration

    # Player's birthday
    __registerHoliday(JNHoliday(
        label="event_player_birthday",
        holiday_type=JNHolidayTypes.player_birthday,
        conditional="store.jn_events.isPlayerBirthday()",
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        natsuki_sprite_code="1uchgnl",
        bgm=audio.happy_birthday_bgm,
        deco_list=["balloons"],
        prop_list=["cake unlit"],
        priority=99
    ))

    # New year's day
    __registerHoliday(JNHoliday(
        label="event_new_years_day",
        holiday_type=JNHolidayTypes.new_years_day,
        conditional="store.jn_events.isNewYearsDay()",
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchgneme",
        deco_list=["balloons"],
        priority=1
    ))

# Used to handle multiple events in a single day by cleaning/setting up inbetween events
label event_interlude:
    n 1fllpueqm "...I feel like I'm forgetting something else."
    n 1fsrpu "...{w=1}{nw}"
    n 1uskemlesh "...!{w=0.5}{nw}"
    n 1fbkwrl "J-{w=0.3}just a second!{w=1}{nw}"
    extend 1flrpol " Don't go anywhere!{w=1}{nw}"

    hide screen hkb_overlay
    show black zorder 99
    stop music
    hide prop
    hide deco
    play audio light_switch

    $ renpy.pause(3)

    return

# RANDOM INTRO EVENTS

# Natsuki is walked in on reading a new volume of Parfait Girls. She isn't impressed.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 2",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_reading_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(2)
    n "W-{w=0.1}wait...{w=0.3} what?!"
    n "M-{w=0.1}Minori!{w=0.5}{nw}"
    extend " You {i}idiot{/i}!"
    n "I seriously can't believe...!"
    n "Ugh...{w=0.5}{nw}"
    extend " {i}this{/i} is what I had to look forward to?"
    n "Come on...{w=0.5}{nw}"
    extend " give me a break..."

    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop parfait_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    n 1uskeml "[player]!{w=0.5}{nw}"
    extend 1fcsan " C-{w=0.1}can you {i}believe{/i} this?"
    n 1fllfu "Parfait Girls got a new editor,{w=0.3}{nw}"
    extend 1fbkwr " and they have no {i}idea{/i} what they're doing!"
    n 1flrwr "I mean,{w=0.1} have you {i}seen{/i} this crap?!{w=0.5}{nw}"
    extend 1fcsfu " Have they even read the series before?!"
    n 1fcsan "As {i}if{/i} Minori would ever stoop so low as to-!"
    n 1unmem "...!"
    n 1fllpol "..."
    n 1fcspo "Actually,{w=0.1} you know what?{w=0.2} It's fine."
    n 1fsrss "I didn't wanna spoil it for you anyway."
    n 1flldv "Ehehe..."
    n 1nllpol "I'll just...{w=0.5}{nw}"
    extend 1nlrss " put this away."

    play audio drawer
    hide prop parfait_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ulraj "So..."
    n 1fchbg "What's new,{w=0.1} [player]?"

    return

# Natsuki is walked in on getting frustrated with her poetry, and gets flustered.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_writing_poetry",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_writing_poetry:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmmm...{w=0.5}{nw}"
    extend " ugh!"

    play audio paper_crumple
    $ renpy.pause(7)

    n "..."
    n "Nnnnnn-!"
    n "I just can't {i}focus{/i}!{w=0.5}{nw}"
    extend " Why is this {i}so{/i} hard now?"

    play audio paper_crumple
    $ renpy.pause(7)

    n "Rrrrr...!"
    n "Oh,{w=0.1} {i}forget it!{/i}"

    play audio paper_crumple
    $ renpy.pause(3)
    play audio paper_throw
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop poetry_attempt zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskuplesh "...!"
    $ player_initial = jn_utils.get_player_initial()
    n 1uskgsf "[player_initial]-[player]?!{w=0.5}{nw}"
    extend 1fbkwrl " How long have you been there?!"
    n 1fllpol "..."
    n 1uskeml "H-{w=0.1}huh? This?{w=0.5}{nw}"
    extend 1fcswrl " I-{w=0.1}it's nothing!{w=0.5}{nw}"
    extend 1flrpol " Nothing at all!"

    play audio drawer
    hide prop poetry_attempt
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nslpol "..."
    n 1kslss "S-{w=0.1}so...{w=0.5}{nw}"
    extend 1flldv " what's up,{w=0.1} [player]?"

    return

# Natsuki is disillusioned with the relationship, and can't suppress her anger and frustration.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_relationship_doubts",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 5",
            affinity_range=(None, jn_affinity.DISTRESSED)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_relationship_doubts:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    n "What is even the {i}point{/i} of this..."
    n "Just..."
    n "..."

    if Natsuki.isDistressed(higher=True):
        n "I {w=2}{i}hate{/i}{w=2} this."

    else:
        n "I {w=2}{i}HATE{/i}{w=2} this."

    n "I hate it.{w=1} I hate it.{w=1} I hate it.{w=1} I hate it.{w=1} I {w=2}{i}hate{/i}{w=2} it."
    $ renpy.pause(5)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with vpunch
        n "I {i}HATE{/i} IT!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ renpy.pause(5)

    menu:
        "Enter.":
            pass

    $ jn_events.displayVisuals("1fcsupl")
    $ jn_globals.force_quit_enabled = True

    n 1fsqunltsb "..."
    n 1fsqemtsb "...Oh.{w=1}{nw}"
    extend 1fsrsr " {i}You're{/i} here."
    n 1ncsem "{i}Great{/i}..."
    n 1fcsantsa "Yeah, that's {i}just{/i} what I need right now."

    return

# Natsuki tries fiddling with the game, it doesn't go well.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_code_fiddling",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 3",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_code_fiddling:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmm..."
    n "Aha!{w=0.5}{nw}"
    extend " I see,{w=0.1} I see."
    n "So,{w=0.3} I think...{w=1}{nw}"
    extend " if I just...{w=1.5}{nw}"
    extend " very...{w=2}{nw}"
    extend " carefully...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n "Ack-!{w=2}{nw}"
    extend " Crap,{w=0.3} that {i}hurt{/i}!"
    n "Ugh..."
    n "How the hell did Monika manage this all the time?"
    extend " This code {i}sucks{/i}!"
    n "..."
    n "..."
    n "But...{w=1} what if I-{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    n "Eek!"
    n "..."
    n "...Yeah,{w=0.3} no.{w=0.5} I think that's enough for now.{w=1}{nw}"
    extend " Yeesh..."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.displayVisuals("1fslpo")
    $ jn_globals.force_quit_enabled = True

    $ player_initial = jn_utils.get_player_initial()
    n 1uskemlesh "Ack-!"
    n 1fbkwrl "[player_initial]-{w=0.1}[player]!"
    extend 1fcseml " Are you {i}trying{/i} to give me a heart attack or something?"
    n 1fllpol "Jeez..."
    n 1fsrpo "Hello to you too,{w=0.1} dummy..."

    return

# Natsuki isn't quite ready for the day...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_not_ready_yet",
            unlocked=True,
            conditional=(
                "((is_time_block_early_morning() or is_time_block_mid_morning()) and is_weekday())"
                " or (is_time_block_late_morning and not is_weekday())"
            ),
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_not_ready_yet:
    python:
        import random
        jn_globals.force_quit_enabled = False

        # Unlock the starter ahoges
        unlocked_ahoges = [
            jn_outfits.get_wearable("jn_headgear_ahoge_curly"),
            jn_outfits.get_wearable("jn_headgear_ahoge_small"),
            jn_outfits.get_wearable("jn_headgear_ahoge_swoop")
        ]
        for ahoge in unlocked_ahoges:
            ahoge.unlock()

        # Unlock the super-messy hairstyle
        super_messy_hairstyle = jn_outfits.get_wearable("jn_hair_super_messy").unlock()

        # Make note of the loaded outfit, then assign Natsuki a hidden one to show off hair/ahoge
        outfit_to_restore = Natsuki.getOutfitName()
        ahoge_outfit = jn_outfits.get_outfit("jn_ahoge_unlock")
        ahoge_outfit.headgear = random.choice(unlocked_ahoges)
        Natsuki.setOutfit(ahoge_outfit)

    $ renpy.pause(5)
    n "Uuuuuu...{w=2}{nw}"
    extend " man..."
    $ renpy.pause(3)
    n "It's too {i}early{/i} for thiiis!"
    play audio chair_out_in
    $ renpy.pause(5)
    n "Ugh...{w=1}{nw}"
    extend " I gotta get to bed earlier..."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.displayVisuals("1uskeml")
    $ jn_globals.force_quit_enabled = True

    n 1uskemlesh "H-{w=0.3}huh?{w=1.5}{nw}"
    extend 1uskwrl " [player]?!{w=1}{nw}"
    extend 1klleml " You're here already?!"
    n 1flrunl "..."
    n 1uskemf "I-{w=0.3}I gotta get ready!"

    play audio clothing_ruffle
    $ Natsuki.setOutfit(jn_outfits.get_outfit(outfit_to_restore))
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    n 1fcsem "Jeez...{w=1.5}{nw}"
    extend 1nslpo  " I really gotta get an alarm clock or something.{w=1}{nw}"
    extend 1nsrss " Heh."
    n 1flldv "So...{w=1}{nw}"
    extend 1fcsbgl " what's up,{w=0.1} [player]?"

    return

# Natsuki is having a hard time understanding Ren'Py (like all of us).
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_renpy_for_dummies",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 5",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_renpy_for_dummies:
    $ jn_globals.force_quit_enabled = False

    n "..."

    play audio page_turn
    $ renpy.pause(2)

    n "Labels...{w=1.5}{nw}"
    extend " labels exist as program points to be called or jumped to,{w=1.5}{nw}"
    extend " either from Ren'Py script,{w=0.3} Python functions,{w=0.3} or from screens."
    n "..."
    $ renpy.pause(1)
    n "...What?"
    $ renpy.pause(1)

    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(2)

    n "..."
    n "Labels can be local or global...{w=1.5}{nw}"
    play audio page_turn
    extend " can transfer control to a label using the jump statement..."
    n "..."
    n "I see!{w=1.5}{nw}"
    extend " I see."
    $ renpy.pause(5)

    n "..."
    n "Yep!{w=1.5}{nw}"
    extend " I have no idea what I'm doing!"
    n "Can't believe I thought {i}this{/i} would help me...{w=1.5}{nw}"
    extend " '{i}award winning{/i}',{w=0.1} my butt."
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop renpy_for_dummies_book_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.displayVisuals("1fcspo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "O-{w=0.3}oh!"
    extend 1fllbgl " H-{w=0.3}hey,{w=0.1} [player]!"
    n 1ullss "I was just...{w=1.5}{nw}"
    extend 1nslss " doing...{w=1.5}{nw}"
    n 1fsrun "..."
    n 1fcswr "N-{w=0.1}nevermind that!"
    extend 1fllpo " This book is trash anyway."

    play audio drawer
    hide prop renpy_for_dummies_book_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nllaj "So...{w=1}{nw}"
    extend 1kchbg " what's new,{w=0.1} [player]?"

    return

# Natsuki tries out a new fashion manga.
# Prop courtesy of Almay @ https://twitter.com/art_almay
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_reading_a_la_mode",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_reading_a_la_mode:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(5)

    n "Oh man...{w=1}{nw}"
    extend " this artwork..."
    n "It's so {i}{cps=\7.5}pretty{/cps}{/i}!"
    n "How the hell do they get so good at this?!"

    $ renpy.pause(3)
    play audio page_turn
    $ renpy.pause(5)

    n "Pffffft-!"
    n "The heck is {i}that{/i}?{w=1}{nw}"
    extend " What were you {i}thinking{/i}?!"
    n "This is {i}exactly{/i} why you leave the outfit design to the pros!"

    $ renpy.pause(1)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass
    
    show prop a_la_mode_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.displayVisuals("1unmajl")
    $ jn_globals.force_quit_enabled = True

    n 1unmgslesu "Oh!{w=1}{nw}"
    extend 1fllbgl " H-{w=0.1}hey,{w=0.1} [player]!"
    n 1nsrss "I was just catching up on some reading time..."
    n 1fspaj "Who'd have guessed slice of life and fashion go so well together?"
    n 1fchbg "I gotta continue this one later!{w=1}{nw}"
    extend 1fchsm " I'm just gonna mark my place real quick,{w=0.1} one sec..."

    play audio drawer
    hide prop a_la_mode_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nchbg "Aaaand we're good to go!{w=1}{nw}"
    extend 1fwlsm " What's new,{w=0.1} [player]?"

    return

# Natsuki treats herself to a strawberry milkshake.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_drinking_strawberry_milkshake",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_drinking_strawberry_milkshake:
    $ jn_globals.force_quit_enabled = False
    n "..."

    play audio straw_sip
    $ renpy.pause(3)

    n "Man...{w=1}{nw}"
    extend " {i}sho good{/i}!"

    play audio straw_sip
    $ renpy.pause(3)

    n "Wow,{w=0.3} I've missed these...{w=1}{nw}"
    extend " why didn't I think of this before?!"

    play audio straw_sip
    $ renpy.pause(2)
    play audio straw_sip
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop strawberry_milkshake zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.displayVisuals("1nchdr")
    $ jn_globals.force_quit_enabled = True

    n 1nchdr "..."
    play audio straw_sip
    n 1nsqdr "..."
    n 1uskdrlesh "...!"
    $ player_initial = jn_utils.get_player_initial()
    n 1fbkwrl "[player_initial]-{w=0.3}[player]!{w=1}{nw}"
    extend 1flleml " I wish you'd stop just {i}appearing{/i} like that..."
    n 1fcseml "Jeez...{w=1}{nw}"
    extend 1fsqpo " you almost made me spill it!"
    n 1flrpo "At least let me finish up here real quick..."

    play audio glass_move
    hide prop strawberry_milkshake
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ncsss "Ah..."
    n 1uchgn "Man,{w=0.1} that hit the spot!"
    n 1fsqbg "And now I'm all refreshed...{w=1}{nw}"
    extend 1tsqsm " what's happening, [player]?{w=1}{nw}"
    extend 1fchsm " Ehehe."

    return

# Natsuki is walked in on reading a manga aimed at/themed around self-help. She *totally* didn't need the self-help, -obviously-.
# Prop courtesy of TheShunBun @ https://twitter.com/TheShunBun
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_step_by_step_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_step_by_step_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(2)
    n "Jeez..."
    n "Who {i}drew{/i} this?!"
    n "I feel like I'm gonna vomit rainbows or something!"
    $ renpy.pause(3)
    play audio page_turn
    $ renpy.pause(2)
    play audio page_turn
    $ renpy.pause(1)
    n "Man..."
    n "A-{w=0.3}alright,{w=0.1} enough drooling over the art!{w=1.5}{nw}"
    extend " You got this thing for a reason,{w=0.1} Natsuki..."
    n "Step by step..."
    n "Improve my daily confidence,{w=0.3} huh?{w=1.5}{nw}"
    extend " Okaaay..."

    $ renpy.pause(1)
    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Enter...":
            pass

    show prop step_by_step_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_events.display_visuals("1uskemfesh")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    $ player_initial = jn_utils.get_player_initial()
    n 1fbkwrf "[player_initial]-{w=0.3}[player]!{w=0.2} Again?!{w=1}{nw}"
    extend 1fbkwrf " D-{w=0.3}do you really have to barge in like that {i}every{/i} time?"
    n 1flrunfess "Yeesh...{w=1}{nw}"
    extend 1fsremfess " I swear you're gonna be the death of me one of these days..."
    n 1fslpol "..."
    n 1tsqsll "...Huh?"
    n 1tnmpul "What?{w=0.2} Is something on my face?"
    n 1tllpuleqm "..."
    n 1uskajlesu "O-{w=0.3}oh!{w=0.75}{nw}"
    extend 1flrbgl " The book!"
    n 1fcsbglsbl "I was just..."
    n 1fllunl "I was..."
    n 1fcsunf "Nnnnnn-!"
    n 1fcswrl "I-{w=0.2}I just like the artwork!{w=1}{nw}"
    extend 1fllemlsbl " That's all it is!"
    n 1fcswrl "I'm {i}super{/i} confident already!"
    n 1fllunlsbl "..."
    n 1fcsemlsbr "A-{w=0.2}and besides,{w=1}{nw}"
    extend 1fllpol " even if I {i}was{/i} reading it for the self-{w=0.1}help stuff..."
    n 1kllsll "..."
    n 1kwmpul "...What'd be wrong with that?"
    n 1fcsbol "It takes real guts to admit to yourself that you can do better.{w=1}{nw}"
    extend 1fnmbol " Can {i}be{/i} better."
    n 1fsrbol "...And only a real jerk would tease someone for trying."
    n 1fcsajl "Never forget that."

    play audio drawer
    hide prop step_by_step_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nllpol "..."
    n 1ulrbol "So..."
    n 1tnmsslsbr "What's new,{w=0.1} [player]?{w=1}{nw}"
    extend 1fllsslsbl " Ahaha..."

    return

# HOLIDAY EVENTS

label event_new_years_day:
    python:
        import copy
        # Give Natsuki a party hat, using whatever she's currently wearing as a base
        previous_outfit = Natsuki.getOutfitName()
        new_years_hat_outfit = copy.copy(jn_outfits.get_outfit(Natsuki.getOutfitName()))
        new_years_hat_outfit.headgear = jn_outfits.get_wearable("jn_headgear_classic_party_hat")
        Natsuki.setOutfit(new_years_hat_outfit)
        jn_events.getHoliday("event_new_years_day").run()
    
    n 1uchbs "FIVE!"
    n 1uchbg "FOUR!"
    n 1uchbs "THREE!"
    n 1uchbg "TWO!"
    n 1unmajesu "ON-"
    n 1fskemesh "...!"
    n 1fcsanless "Uuuuuuuu-!"
    n 1fcsemless "Are you{w=0.5}{nw}"
    extend 1fcswrl " {cps=\10}freaking{/cps}{w=0.5}{nw}"
    extend 1fbkwrlean " {i}kidding{/i} me?!{w=0.5}{nw}"
    n 1kskem "I missed it?!{w=0.5}{nw}"
    extend 1kskwr " {b}AGAIN?!{/b}"
    n 1fcsfu "Ugh!{w=0.5}{nw}"
    extend 1kslfreso " I can't {i}believe{/i} I was so off with the timing!"

    if jn_is_day():
        n 1tnmpu "...Really off,{w=0.1} actually.{w=0.5} Now that I look at the time.{w=1}{nw}"
        extend 1nsrpo " Almost impressively."
        n 1kcsemedr "Jeez..."
        n 1fslajl "You could have at least woken me up sooner,{w=0.5}{nw}"
        extend 1fsqpol " you jerk."
        n 1nslpu "But...{w=1}{nw}"
        extend 1tsqsl " I suppose I can't give you too much of a hard time for it,{w=0.1} [player]."
        n 1fcsbg " Your hangover can do that for me.{w=0.5}{nw}"
        extend 1fcsajsbr " Anyway!"

        play audio page_turn
        $ Natsuki.setOutfit(previous_outfit)
        with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    else:
        n 1kcsemedr "Man..."
        n 1fsrpu "Now that's gonna bug me from the rest of the day...{w=0.5}{nw}"
        extend 1tsqss " way to start the year,{w=0.1} huh?"
        n 1fcspo "..."
        n 1fcsajsbr "Well,{w=0.1} whatever!"

    n 1flldvlsbr "Missing the new year?{w=0.5}{nw}"
    extend 1flrbgsbl " M-{w=0.3}merely a minor setback!"
    n 1fcsajsbr "Besides,{w=0.5}{nw}"
    extend 1flrbgsbr " it's not like we're gonna run out of years to count!{w=1}{nw}"
    extend 1nsrsssbr " Probably."

    n 1unmsl "In all seriousness though,{w=0.1} [player]?"
    n 1nslss "I know I've kinda already trashed my clean start..."
    n 1fnmbol "But that doesn't mean you're off the hook."
    n 1fcsss "Yeah,{w=0.1} yeah.{w=0.5} I know."
    n 1fslss "I'm not gonna give you a whole lecture on fresh starts,{w=1}{nw}"
    extend 1tlrbo " hitting the gym{w=0.5}{nw}"
    extend 1tnmss " or anything like that."

    if jn_is_day():
        n 1fchgn "{i}Something{/i} tells me you wouldn't appreciate the extra headache!"

    n 1tllaj "But...{w=1}{nw}" 
    extend 1tnmsl " there actually is one thing I wanna say."
    n 1ncssl "..."
    n 1ucspu "Just..."

    if Natsuku.isAffectionate(higher=True):
        extend 1fnmpul " promise me something,{w=0.1} [player].{w=0.5}{nw}"
        extend 1knmbol " Please?"
    
    else:
        extend 1fnmpu " do one thing for me.{w=0.5}{nw}"
        extend 1knmbol " Please?"

    n 1kslbol "..."
    n 1kplpulsbl "Reach out to someone today.{w=0.5}{nw}"

    if Natsuki.isEnamored(higher=True):
        extend 1fcsajfesssbl " A-{w=0.2}and I don't mean me.{w=0.5}{nw}"
        extend 1fslssfesssbl " This time."

    else:
        extend 1fcsajfesssbl " A-{w=0.2}and I don't mean me.{w=0.5}{nw}"
    
    n 1fcsun "Just...{w=1}{nw}" 
    extend 1fcspul " hear me out,{w=0.1} alright?"
    n 1kllun "Not everyone has the luxury of friends or family.{w=0.5}{nw}"
    extend 1ksqpu " And trust me when I say not everyone looks forward to a new year..."
    n 1knmsl "But the right message really {i}can{/i} make all the difference."
    n 1klrsl "...And you never know if you'll always have the chance to send it."
    n 1ncspu "Some family you don't get along with,{w=1}{nw}"
    extend 1nllsr " a friend you've drifted away from..."
    n 1knmpu "They won't...{w=0.5}{nw}"
    extend 1kllpu " be there{w=0.5}{nw}"
    extend 1fslunl " forever."
    n 1fcsajl "And remembering the people around you is just as important as any stupid resolution."
    n 1fnmsrl "So I don't care {i}how{/i} you do it.{w=1}{nw}"
    extend 1fllpul "Text message,{w=0.1} phone call,{w=0.1} whatever."
    n 1fcspul "Just...{w=0.5}{nw}"
    extend 1kllsrl " do something,{w=0.1} alright?{w=1}{nw}"
    extend 1fnmbol " For yourself just as much as them."

    n 1nlrunl "..."
    n 1ncsajl "Oh,{w=0.5}{nw}"
    extend 1nsleml " jeez."
    $ current_year = datetime.date.today().year
    n 1fllunlsbr "We're barely into [current_year] and I'm already making things all serious..."
    n 1fslsslsbr "Heh.{w=0.5}{nw}"
    extend 1tsqpu " So much for a lighthearted celebration,{w=0.1} huh?"
    n 1tnmpu "But [player]?"
    n 1kllsl "..."

    if Natsuki.isEnamored(higher=True):
        n 1knmsll "...Thank you."
        n 1kllssl "For this year,{w=0.1} I mean."
        n 1fcsemlesssbl "I-{w=0.2}I know I don't show it a lot!{w=0.5}{nw}"
        extend 1klrpul " But...{w=0.5}{nw}" 
        extend 1knmpul " just taking time out of your day to visit me,{w=0.75}{nw}"
        extend 1kllssl " listening to all my nonsense,{w=0.75}{nw}"
        extend 1fsldvl " dealing with my crap sometimes..."
        n 1knmbol "...It matters."
        n 1kllssl "It really does,{w=0.1} heh.{w=1.25}{nw}"
        extend 1kllbofsbr " A lot."
        n 1kllajf "And...{w=1}{nw}"
        extend 1knmpufsbr " one last thing?"
        n 1fcsunfsbr "..."

        show black zorder 4 with Dissolve(0.5)
        play audio clothing_ruffle
        pause 5

        if Natsuki.isLove(higher=True):
            show natsuki 1fsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
            play audio kiss
            pause 3
            hide black with Dissolve(1.25)
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1kwmsmf "...Happy new year,{w=0.1} [chosen_endearment].{w=1.25}{nw}"
            extend 1kllssfess " Ehehe."

        else:
            show natsuki 1nsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1klrssf "Heh."
            n 1fchsmfess "...Happy new year,{w=0.1} [chosen_tease]."

    else:
        n 1knmsll "...Thanks.{w=0.75}{nw}"
        extend 1fcsemlsbl " F-{w=0.2}for this year,{w=0.1} I mean."
        n 1fslbolesssbl "I...{w=0.5}{nw}"
        extend 1knmboless " really appreciate that you've spent so much time with me already."
        n 1kllssless "Even if I {i}am{/i} just a grouchy girl stuck in some{w=0.5}{nw}" 
        extend 1fsrssl " magical space classroom."
        n 1nlrunl "..."
        n 1kbkwrl "Seriously!{w=0.2} I do!"
        n 1fllanlsbl "It's..."
        n 1kcsemlesisbl "..."
        n 1ksrpol "I-{w=0.3}it just means a lot to me,{w=0.1} okay?"
        n 1ksrpul "And...{w=0.75}{nw}"
        extend 1knmssl " one last thing?"
        n 1ncsajl "..."
        n 1fcsunl "..."

        show black zorder 4 with Dissolve(0.5)
        show natsuki 1fsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
        play audio clothing_ruffle
        pause 5
        hide black with Dissolve(1.25)

        n 1fsqdvlesssbr "...H-{w=0.2}happy new year,{w=0.1} dummy."
        n 1nslsslesssbl "A-{w=0.2}and if anyone asks,{w=0.3} that never happened.{w=1}{nw}"
        extend 1fsldvlesssbl " Ehehe..."

    $ jn_events.getHoliday("event_new_years_day").complete()

    return

label event_valentines_day:
    #TODO: writing
    $ jn_events.getHoliday("event_valentines_day").run()

    $ jn_events.getHoliday("event_valentines_day").complete()

    return

label event_easter:
    #TODO: writing
    $ jn_events.getHoliday("event_easter").run()
    $ jn_events.getHoliday("event_easter").complete()

    return

label event_halloween:
    #TODO: writing
    $ jn_events.getHoliday("event_halloween").run()

    $ jn_events.getHoliday("event_halloween").complete()

    return

label event_christmas_eve:
    #TODO: writing
    $ jn_events.getHoliday("event_christmas_eve").run()

    $ jn_events.getHoliday("event_christmas_eve").complete()

    return

label event_christmas_day:
    #TODO: writing
    $ jn_events.getHoliday("event_christmas_day").run()

    $ jn_events.getHoliday("event_christmas_day").complete()

    return

label event_new_years_eve:
    #TODO: writing
    $ jn_events.getHoliday("event_new_years_eve").run()

    $ jn_events.getHoliday("event_new_years_eve").complete()

    return

# Natsuki wishes the player a happy birthday!
label event_player_birthday():
    $ jn_events.getHoliday("event_player_birthday").run()
    $ player_name_capitalized = persistent.playername.upper()
    n 1uchlgl "HAPPY BIRTHDAY,{w=0.1} [player_name_capitalized]!"
    n 1fcsbg "Betcha' didn't think I had something planned all along,{w=0.1} did you?{w=0.5}{nw}"
    extend 1nchsml " Ehehe."
    n 1fnmaj "Don't lie!{w=1}{nw}"
    extend 1fchbl " I know I got you {i}real{/i} good this time."
    n 1ullss "Well,{w=0.1} whatever.{w=1}{nw}"
    extend 1tsqsm " We both know what {i}you're{/i} waiting for,{w=0.1} huh?"
    n 1fcsss "Yeah,{w=0.1} yeah.{w=0.5}{nw}"
    extend 1fchsm " I got you covered,{w=0.1} [player]."

    show prop cake lit zorder jn_events.JN_EVENT_PROP_ZORDER
    play audio necklace_clip

    n 1uchgn "Ta-{w=0.3}da!"
    $ renpy.pause(3)
    n 1fnmpu "..."
    n 1fbkwr "What?!{w=1}{nw}"
    extend 1fllpol " You don't {i}seriously{/i} expect me to sing all by myself?{w=1}{nw}"
    extend 1fcseml " No way!"
    n 1nlrpol "..."
    n 1nlrpu "But..."
    n 1nchbs "Yeah!{w=0.2} Here you go!{w=0.5}{nw}"
    extend 1nchsml " Ehehe."
    n 1tsqsm "So,{w=0.1} [player]?{w=1}{nw}"
    extend 1tsqss " Aren't you gonna make a wish?"
    n 1tlrpu "...Better come up with one soon,{w=0.1} actually.{w=1}{nw}"
    extend 1uskemlesh " I gotta put this out before the wax ruins all the icing!"
    n 1nllpo "..."
    n 1tsqpu "All set?{w=0.5}{nw}"
    extend 1fsrpo " About time.{w=1}{nw}"
    extend 1fchbg " Let's put these out already!"

    n 1ncsaj "...{w=0.5}{nw}"
    show prop cake unlit zorder jn_events.JN_EVENT_PROP_ZORDER
    play audio blow

    n 1nchsm "..."
    n 1tsgss "Well?{w=0.75}{nw}"
    extend 1tnmaj " What're you waiting for,{w=0.1} [player]?{w=1}{nw}"
    extend 1flrcal " Dig in already!"
    n 1nsqsll "Don't tell me I went all out on this for nothing."
    n 1fsqsr "..."
    n 1uskajesu "...Oh.{w=0.5}{nw}"
    extend 1fllssl " Ehehe.{w=1}{nw}"
    extend 1fslssl " Right."
    n 1flrssl "I...{w=1.5}{nw}"
    extend 1fsrdvl " kinda forgot about {i}that{/i} aspect."
    n 1fslpol "And I don't really feel like smearing cake all over your screen.{w=1}{nw}"
    extend 1ullaj " So..."
    n 1nsrss "I'm just gonna just save this for later."
    n 1fnmajl "Hey!{w=0.5}{nw}"
    extend 1fllbgl " It's the thought that counts,{w=0.1} right?"

    play audio glass_move
    hide prop cake unlit
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
        poem_list=jn_poems.getAllPoems(),
        unlocked=False,
        holiday_types=[jn_events.JNHolidayTypes.player_birthday],
        affinity=Natsuki._getAffinityState()
    )
    $ birthday_poem = random.choice(unlocked_poem_pool) if len(unlocked_poem_pool) > 0 else None   

    if birthday_poem:
        if Natsuki.isEnamored(higher=True):
            n 1kllcal "..."
            n 1knmpul "...I wrote you something too,{w=0.1} you know."
            n 1fcseml "I-{w=0.2}I know it's not some {i}fancy{/i} gift,{w=1}{nw}" 
            extend 1klrsrl " but..."
            n 1fsrsrl "..."
            n 1fcsunl "Uuuuu..."
            n 1fcspul "Just...{w=1}{nw}"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            extend 1klrpol " read it already,{w=0.1} [chosen_tease]."

        else:
            n 1fllunl "..."
            n 1fnmcal "I-{w=0.2}I hope you didn't think I'd just leave you with nothing."
            n 1nsrpol "I'm not {i}that{/i} much of a jerk."
            n 1nsrajl "So...{w=1}{nw}"
            extend 1fnmcal " here you go."
            n 1fcsemf "J-{w=0.2}just hurry up and read it.{w=1}{nw}"
            extend 1fslbof " I'm not gonna read it to you."

        call show_poem(birthday_poem)

        if Natsuki.isEnamored(higher=True):
            n 1knmbol "Hey...{w=1}{nw}"
            extend 1knmpul " you {i}did{/i} read it,{w=0.1} right?"
            n 1fslbol "I worked a lot on that,{w=0.1} you know."
            n 1fcseml "A-{w=0.2}and I meant every word,{w=1}{nw}" 
            extend 1kllbof " so..."
            n 1klrssf "...Yeah."
            n 1flldvl "I'll..."
            extend 1fslssl " just put that poem back in my desk for now."

        else:
            n 1nsqpul "All done?{w=1}{nw}"
            extend 1fcseml " {i}Finally{/i}.{w=1}{nw}"
            extend 1fslcal " Jeez..."
            n 1fslunl "..."
            n 1fcsajl "I guess I'll just keep it in my desk for now.{w=1}{nw}"
            extend 1fsrssl " I-{w=0.2}in case you wanted to reference my writing skills later,{w=0.1} {i}obviously{/i}."

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    if Natsuki.isLove(higher=True):
        n 1klrssl "And...{w=1.5}{nw}"
        extend 1knmsml " [player]?"

        show black zorder jn_events.JN_EVENT_FADE_ZORDER with Dissolve(0.5)
        $ renpy.pause(0.5)
        play audio kiss
        $ renpy.pause(0.25)
        hide black with Dissolve(1.25) 

        n 1kwmssf "H-{w=0.2}happy birthday.{w=1}{nw}"
        extend 1kchsmf " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1kwmssf "H-{w=0.2}happy birthday."

    else:
        n 1fcsbgf "You're welcome!"

    if birthday_poem:
        $ birthday_poem.unlock()

    $ jn_events.getHoliday("event_player_birthday").complete()

    return

label event_anniversary:
    #TODO: writing
    $ jn_events.getHoliday("event_anniversary").run()
    n "This isn't done yet, but happy anniversary!"
    
    $ jn_events.getHoliday("event_anniversary").complete()
    
    return
