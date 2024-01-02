default persistent._event_database = dict()
default persistent._jn_holiday_list = dict()
default persistent._jn_holiday_completed_list = []
default persistent._jn_holiday_deco_list_on_quit = []
default persistent._jn_event_completed_count = 0
default persistent._jn_event_attempt_count = 15

default persistent._jn_player_celebrates_christmas = None
default persistent._jn_player_love_halloween_seen = None

# Transforms for overlays
transform jn_glasses_pre_slide:
    subpixel True
    ypos 0

transform jn_glasses_slide_down:
    subpixel True
    ypos 0
    easeout 5 ypos 20

transform jn_glasses_slide_down_faster:
    subpixel True
    ypos 0
    easeout 3 ypos 20

transform jn_glasses_readjust:
    subpixel True
    ypos 20
    easein 0.75 ypos 0

transform jn_mistletoe_lift:
    subpixel True
    ypos 0
    easeout 2 ypos -54

transform jn_confetti_fall:
    subpixel True
    ypos 0
    easeout 2.25 alpha 0 ypos 90

# Foreground props are displayed on the desk, in front of Natsuki
image prop poetry_attempt = "mod_assets/props/poetry_attempt.png"
image prop math_attempt = "mod_assets/props/math_attempt.png"
image prop a_la_mode_manga_held = "mod_assets/props/a_la_mode_manga_held.png"
image prop strawberry_milkshake = "mod_assets/props/strawberry_milkshake.png"
image prop step_by_step_manga_held = "mod_assets/props/step_by_step_manga_held.png"
image prop glasses_case = "mod_assets/props/glasses_case.png"
image prop hot_chocolate hot = "mod_assets/props/hot_chocolate.png"
image prop hot_chocolate cold = "mod_assets/props/hot_chocolate_cold.png"
image prop cake lit = "mod_assets/props/cake_lit.png"
image prop cake unlit = "mod_assets/props/cake_unlit.png"
image prop watering_can = "mod_assets/props/watering_can.png"

image prop f14_heart give = "mod_assets/props/f14/give_heart.png"
image prop f14_heart hold = "mod_assets/props/f14/hold_heart.png"

image prop wintendo_twitch_held free = "mod_assets/props/twitch/held/wintendo_twitch_held_free.png"
image prop wintendo_twitch_held charging = "mod_assets/props/twitch/held/wintendo_twitch_held_charging.png"
image prop wintendo_twitch_playing free:
    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1

    choice:
        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat
image prop wintendo_twitch_playing charging:
    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1

    choice:
        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat
image prop wintendo_twitch_battery_low:
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_a.png"
    pause 1
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_b.png"
    pause 1
    repeat
image prop wintendo_twitch_dead:
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_a.png"
    pause 1
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_b.png"
    pause 1
    repeat

image prop music_notes:
    choice:
        "mod_assets/props/music/music_notes_a.png"
    choice:
        "mod_assets/props/music/music_notes_b.png"
    choice:
        "mod_assets/props/music/music_notes_c.png"
    choice:
        "mod_assets/props/music/music_notes_d.png"
    pause 1
    repeat

image confetti falling:
    "mod_assets/props/confetti/confetti_a.png"
    pause 0.75
    "mod_assets/props/confetti/confetti_b.png"
    pause 0.75
    "mod_assets/props/confetti/confetti_c.png"
    pause 0.75

image confetti desk:
    "mod_assets/props/confetti/confetti_desk.png"

# Background decorations are displayed in the room behind Natsuki
image deco balloons = "mod_assets/deco/balloons.png"
image deco garlands = "mod_assets/deco/garlands.png"
image deco tree day = "mod_assets/deco/tree_day.png"
image deco tree night = "mod_assets/deco/tree_night.png"
image deco hanging_lights lit = "mod_assets/deco/hanging_lights_lit.png"
image deco hanging_lights unlit = "mod_assets/deco/hanging_lights_unlit.png"
image deco wall_stocking day = "mod_assets/deco/wall_stocking_day.png"
image deco wall_stocking night = "mod_assets/deco/wall_stocking_night.png"
image deco d24 = "mod_assets/deco/d24.png"
image deco d25 = "mod_assets/deco/d25.png"
image deco o31 = "mod_assets/deco/o31.png"

# Overlays are displayed over the top of Natsuki, in front of any decorations but behind any props
image overlay slipping_glasses = "mod_assets/overlays/slipping_glasses.png"
image overlay mistletoe = "mod_assets/overlays/mistletoe.png"

init python in jn_events:
    import datetime
    from Enum import Enum
    import random
    import store
    import store.audio as audio
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils

    EVENT_MAP = dict()
    EVENT_RETURN_OUTFIT = None

    __ALL_HOLIDAYS = {}

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

        def __int__(self):
            return self.value

    class JNHoliday():
        """
        Describes a holiday event that a user can experience, once per year.
        """
        def __init__(
            self,
            label,
            holiday_type,
            affinity_range,
            natsuki_sprite_code,
            conditional=None,
            bgm=None,
            deco_list=[],
            prop_list=[],
            priority=0
        ):
            """
            Constructor.

            IN:
                - label - The name used to uniquely identify this holiday and refer to it internally
                - holiday_type - The JNHolidayTypes type of this holiday
                - affinity_range - The affinity range that must be satisfied for this holiday to be picked when filtering
                - natsuki_sprite_code - The sprite code to show for Natsuki when the holiday is revealed
                - conditional - Python statement that must evaluate to True for this holiday to be picked when filtering
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
            is_seen=None,
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
                - list of holidays matching the search criteria
            """
            return [
                _holiday
                for _holiday in holiday_list
                if _holiday.__filterHoliday(
                    is_seen,
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
            is_seen=None,
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
            if is_seen is not None and self.is_seen != is_seen:
                return False

            elif holiday_types is not None and not self.holiday_type in holiday_types:
                return False

            elif affinity is not None and not self.currAffinityInAffinityRange(affinity):
                return False

            elif (
                holiday_completion_state is not None
                and self.isCompleted()
            ):
                return False

            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False

            return True

        def run(self, suppress_visuals=False):
            """
            Sets up all visuals for this holiday, before revealing everything to the player.
            Any props or decorations left over from the previous holiday are tidied up before presentation.

            IN:
                - suppress_visuals - If True, prevents any props or deco from being displayed automatically
            """
            renpy.hide("prop")
            renpy.hide("deco")

            if not suppress_visuals:
                for prop in self.prop_list:
                    renpy.show(name="prop {0}".format(prop), zorder=store.JN_PROP_ZORDER)

            if not suppress_visuals:
                for deco in self.deco_list:
                    renpy.show(name="deco {0}".format(deco), zorder=store.JN_DECO_ZORDER)

            kwargs = {
                "natsuki_sprite_code": self.natsuki_sprite_code
            }
            if self.bgm:
                kwargs.update({"bgm": self.bgm})

            if not suppress_visuals:
                displayVisuals(**kwargs)

            else:
                jn_globals.force_quit_enabled = True

        def complete(self):
            """
            Marks this holiday as complete, preventing it from being seen again until reset.
            This should be run after a holiday has concluded, so a crash/quit after starting the holiday doesn't lock progression.
            We also mark the holiday type as completed for this year, so we can't cycle through all seasonal events in one year
            Lastly, set the persisted deco list so reloading the game without a day change shows the deco for this event.
            """
            store.persistent._jn_event_completed_count += 1
            self.is_seen = True
            self.__save()

            if not self.isCompleted():
                store.persistent._jn_holiday_completed_list.append(int(self.holiday_type))

            if self.deco_list:
                store.persistent._jn_holiday_deco_list_on_quit = self.deco_list

            store.Natsuki.resetLastTopicCall()
            store.Natsuki.resetLastIdleCall()

        def isCompleted(self):
            """
            Returns whether this holiday has been completed.

            OUT:
                - True if the holiday has been marked as completed, otherwise False
            """
            return int(self.holiday_type) in store.persistent._jn_holiday_completed_list

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

        if store.jnIsNewYearsDay(input_date):
            holidays.append(JNHolidayTypes.new_years_day)

        if store.jnIsValentinesDay(input_date):
            holidays.append(JNHolidayTypes.valentines_day)

        if store.jnIsEaster(input_date):
            holidays.append(JNHolidayTypes.easter)

        if store.jnIsHalloween(input_date):
            holidays.append(JNHolidayTypes.halloween)

        if store.jnIsChristmasEve(input_date):
            holidays.append(JNHolidayTypes.christmas_eve)

        if store.jnIsChristmasDay(input_date):
            holidays.append(JNHolidayTypes.christmas_day)

        if store.jnIsNewYearsEve(input_date):
            holidays.append(JNHolidayTypes.new_years_eve)

        if store.jnIsNatsukiBirthday(input_date):
            holidays.append(JNHolidayTypes.natsuki_birthday)

        if store.jnIsPlayerBirthday(input_date):
            holidays.append(JNHolidayTypes.player_birthday)

        if store.jnIsAnniversary(input_date):
            holidays.append(JNHolidayTypes.anniversary)

        return holidays

    def getAllHolidays():
        """
        Returns a list of all holidays.
        """
        return __ALL_HOLIDAYS.itervalues()

    def selectHolidays():
        """
        Returns a list of all uncompleted holidays that apply for the current date, or None if no holidays apply.
        Only one holiday of each type may be returned.
        """
        holiday_list = JNHoliday.filterHolidays(
            is_seen=False,
            holiday_list=getAllHolidays(),
            holiday_types=getHolidaysForDate(),
            affinity=store.Natsuki._getAffinityState(),
            holiday_completion_state=False
        )

        if len(holiday_list) > 0:
            holiday_types_added = []
            return_list = []
            for holiday in holiday_list:
                if holiday.holiday_type not in holiday_types_added:
                    holiday_types_added.append(holiday.holiday_type)
                    return_list.append(holiday)

            return return_list

        else:
            return None

    def resetHolidays():
        """
        Resets the is_seen state and corresponding completion state for all holidays.
        Also clears the deco.
        """
        for holiday in getAllHolidays():
            holiday.is_seen = False

        JNHoliday.saveAll()
        store.persistent._jn_holiday_completed_list = []
        store.persistent._jn_holiday_deco_list_on_quit = []

    def queueHolidays(holiday_list, is_day_check=False):
        """
        Given a list of holidays, will sort them according to priority and add them to the list of topics to run through.
        Interludes are used to perform pacing, so a holiday will not immediately transition into another.
        """
        store.persistent._event_list = list()
        holiday_list.sort(key = lambda holiday: holiday.priority)

        if is_day_check:
            store.queue("holiday_prelude")

        while len(holiday_list) > 0:
            store.queue(holiday_list.pop(0).label)

            if len(holiday_list) > 0:
                store.queue("holiday_interlude")

            else:
                store.queue("ch30_loop")

        renpy.jump("call_next_topic")

    def displayVisuals(
        natsuki_sprite_code,
        bgm="mod_assets/bgm/vacation.ogg"
    ):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
            - music_file_path - The str file path of the music to play upon revealing Natsuki; defaults to standard bgm
        """
        renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        store.jnPause(0.1)
        renpy.hide("black")
        renpy.show_screen("hkb_overlay")
        renpy.play(filename=audio.switch_flip, channel="audio")
        renpy.play(filename=bgm, channel="music")
        renpy.hide("black")

    # Holiday registration

    # Christmas eve
    __registerHoliday(JNHoliday(
        label="holiday_christmas_eve",
        holiday_type=JNHolidayTypes.christmas_eve,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchsm",
        deco_list=["d24"],
        priority=99
    ))

    # Christmas day
    __registerHoliday(JNHoliday(
        label="holiday_christmas_day",
        holiday_type=JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fspss",
        deco_list=["d25"],
        priority=99
    ))

    # New year's eve
    __registerHoliday(JNHoliday(
        label="holiday_new_years_eve",
        holiday_type=JNHolidayTypes.new_years_eve,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchgneme",
        priority=10
    ))

    # New year's day
    __registerHoliday(JNHoliday(
        label="holiday_new_years_day",
        holiday_type=JNHolidayTypes.new_years_day,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchgneme",
        deco_list=["balloons"],
        priority=10
    ))

    # Valentine's day
    __registerHoliday(JNHoliday(
        label="holiday_valentines_day",
        holiday_type=JNHolidayTypes.valentines_day,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        natsuki_sprite_code="1fsrunlsbr",
        prop_list=["f14_heart hold"],
        priority=10
    ))

    # Easter
    __registerHoliday(JNHoliday(
        label="holiday_easter",
        holiday_type=JNHolidayTypes.easter,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fsrunlsbr",
        priority=10
    ))

    # Halloween
    __registerHoliday(JNHoliday(
        label="holiday_halloween",
        holiday_type=JNHolidayTypes.halloween,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fsrunlsbr",
        deco_list=["o31"],
        priority=10
    ))

    # Player's birthday
    __registerHoliday(JNHoliday(
        label="holiday_player_birthday",
        holiday_type=JNHolidayTypes.player_birthday,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        natsuki_sprite_code="1uchgnl",
        bgm=audio.happy_birthday_bgm,
        deco_list=["balloons"],
        prop_list=["cake unlit"],
        priority=50
    ))

    # Natsuki's birthday
    __registerHoliday(JNHoliday(
        label="holiday_natsuki_birthday",
        holiday_type=JNHolidayTypes.natsuki_birthday,
        conditional="jn_gifts.getGiftFileExists('party_supplies')",
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1unmemlsbr",
        bgm=audio.happy_birthday_bgm,
        deco_list=["balloons"],
        prop_list=["cake unlit"],
        priority=50
    ))

# RANDOM INTRO EVENTS

# Natsuki is walked in on reading a new volume of Parfait Girls. She isn't impressed.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 2",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_reading_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ jnPause(2)
    n "W-{w=0.2}wait...{w=0.3} what?!"
    n "M-{w=0.2}Minori!{w=0.5}{nw}"
    extend " You {i}idiot{/i}!"
    n "I seriously can't believe...!"
    n "Ugh...{w=0.5}{nw}"
    extend " {i}this{/i} is what I had to look forward to?"
    n "Come on...{w=0.5}{nw}"
    extend " give me a break..."

    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    $ parfait_manga = jn_desk_items.getDeskItem('jn_parfait_manga_held')
    $ parfait_manga.unlock()
    $ manga_closed = jn_desk_items.getDeskItem("jn_parfait_manga_closed")
    $ manga_closed.unlock()
    $ Natsuki.setDeskItem(parfait_manga)
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    n 1uskeml "[player]!{w=0.5}{nw}"
    extend 1fcsan " C-{w=0.2}can you {i}believe{/i} this?"
    n 1fllfu "Parfait Girls got a new editor,{w=0.3}{nw}"
    extend 1fbkwr " and they have no {i}idea{/i} what they're doing!"
    n 1flrwr "I mean,{w=0.2} have you {i}seen{/i} this crap?!{w=0.5}{nw}"
    extend 1fcsfu " Have they even {i}read{/i} the series before?!"
    n 1fcsan "As {i}if{/i} Minori would ever stoop so low as to-!"
    n 1unmem "...!"
    n 1fllpol "..."
    n 1fcspo "Actually,{w=0.2} you know what?{w=0.5} It's fine."
    n 1fsrss "I didn't wanna spoil it for you anyway."
    n 1flldv "Ehehe..."
    n 1nllpol "I'll just...{w=0.5}{nw}"
    extend 1nlrss " put this away."

    show natsuki 1nsrca
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    $ Natsuki.clearDesk()
    show natsuki 4nlrbo
    $ jnPause(4)
    hide black with Dissolve(1)

    n 3ulraj "So..."
    n 3fchbgsbr "What's new,{w=0.2} [player]?"

    return

# Natsuki is walked in on getting frustrated with her poetry, and gets flustered.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_writing_poetry",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
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
    $ jnPause(7)

    n "..."
    n "Nnnnnn-!"
    n "I just can't {i}focus{/i}!{w=0.5}{nw}"
    extend " Why is this {i}so{/i} hard now?"

    play audio paper_crumple
    $ jnPause(7)

    n "Rrrrr...!"
    n "Oh,{w=0.2} {i}forget it!{/i}"

    play audio paper_crumple
    $ jnPause(3)
    play audio paper_throw
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    show prop poetry_attempt zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskuplesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 4uskgsf "[player_initial]-[player]?!{w=0.5}{nw}"
    extend 2fbkwrl " How long have you been there?!"
    n 2fllpol "..."
    n 4uskeml "H-{w=0.2}huh? This?{w=0.5}{nw}"
    extend 4fcswrl " I-{w=0.2}it's nothing!{w=0.5}{nw}"
    extend 2flrpol " Nothing at all!"

    show natsuki 4fcspol
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    hide prop poetry_attempt
    show natsuki 2nslbol
    $ jnPause(4)
    hide black with Dissolve(1)

    n 2nslpol "..."
    n 2fslsslsbr "S-{w=0.2}so...{w=0.5}{nw}"
    extend 4fcsbglsbr " what's up,{w=0.2} [player]?"

    return

# Natsuki is disillusioned with the relationship, and can't suppress her anger and frustration.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_relationship_doubts",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
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
    $ jnPause(5)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder JN_GLITCH_ZORDER with vpunch
        n "I {i}HATE{/i} IT!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ jnPause(5)

    menu:
        "Enter.":
            pass

    $ jn_events.displayVisuals(natsuki_sprite_code="1fcsupl", bgm="mod_assets/bgm/just_natsuki.ogg")
    $ jn_globals.force_quit_enabled = True

    n 1fsqunltsb "..."
    n 1fsqemtsb "...Oh.{w=1}{nw}"
    extend 2fsrsr " {i}You're{/i} here."
    n 2ncsem "{i}Great{/i}..."
    n 4fcsantsa "Yeah, that's {i}just{/i} what I need right now."

    return

# Natsuki tries fiddling with the game, it doesn't go well.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_code_fiddling",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_code_fiddling:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmm..."
    n "Aha!{w=0.5}{nw}"
    extend " I see,{w=0.2} I see."
    n "So,{w=0.3} I think...{w=1}{nw}"
    extend " if I just...{w=1.5}{nw}"
    extend " very...{w=2}{nw}"
    extend " carefully...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
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
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c

    n "Eek!"
    n "..."
    n "...Yeah,{w=0.3} no.{w=0.5} I think that's enough for now.{w=1}{nw}"
    extend " Yeesh..."
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.displayVisuals("1fslpo")
    $ jn_globals.force_quit_enabled = True

    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskemlesh "Ack-!"
    n 4fbkwrl "[player_initial]-{w=0.2}[player]!"
    extend 2fcseml " Are you {i}trying{/i} to give me a heart attack or something?"
    n 2fllpol "Jeez..."
    n 1fsrpo "Hello to you too,{w=0.2} dummy..."

    return

# Natsuki isn't quite ready for the day...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_not_ready_yet",
            unlocked=True,
            conditional=(
                "((jn_is_time_block_early_morning() or jn_is_time_block_mid_morning()) and jn_is_weekday())"
                " or (jn_is_time_block_late_morning and not jn_is_weekday())"
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
            jn_outfits.getWearable("jn_headgear_ahoge_curly"),
            jn_outfits.getWearable("jn_headgear_ahoge_small"),
            jn_outfits.getWearable("jn_headgear_ahoge_swoop")
        ]
        for ahoge in unlocked_ahoges:
            ahoge.unlock()

        # Unlock the super-messy hairstyle
        super_messy_hairstyle = jn_outfits.getWearable("jn_hair_super_messy").unlock()

        # Make note of the loaded outfit, then assign Natsuki a hidden one to show off hair/ahoge
        outfit_to_restore = Natsuki.getOutfitName()
        ahoge_outfit = jn_outfits.getOutfit("jn_ahoge_unlock")
        ahoge_outfit.headgear = random.choice(unlocked_ahoges)
        jn_outfits.saveTemporaryOutfit(ahoge_outfit)

    $ jnPause(5)
    n "Uuuuuu...{w=2}{nw}"
    extend " man..."
    $ jnPause(3)
    n "It's too {i}early{/i} for thiiis!"
    play audio chair_out_in
    $ jnPause(5)
    n "Ugh...{w=1}{nw}"
    extend " I gotta get to bed earlier..."
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    $ jn_events.displayVisuals("1uskeml")
    $ jn_globals.force_quit_enabled = True

    n 1uskemlesh "H-{w=0.3}huh?{w=1}{nw}"
    extend 1uskwrl " [player]?!{w=0.75}{nw}"
    extend 4klleml " You're here already?!"
    n 4flrunl "..."
    n 4uskemfeexsbr "I-{w=0.3}I gotta get ready!"

    show natsuki 1fslunlsbr
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio clothing_ruffle
    $ Natsuki.setOutfit(jn_outfits.getOutfit(outfit_to_restore))
    show natsuki 2fsrpol
    $ jnPause(4)
    hide black with Dissolve(1)

    n 2fcsem "Jeez...{w=1.5}{nw}"
    extend 2nslpo  " I really gotta get an alarm clock or something.{w=1}{nw}"
    extend 2nsrss " Heh."
    n 4flldv "So...{w=1}{nw}"
    extend 3fcsbgl " what's up,{w=0.2} [player]?"

    return

# Natsuki is having a hard time understanding Ren'Py (like all of us).
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_renpy_for_dummies",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_renpy_for_dummies:
    $ jn_globals.force_quit_enabled = False

    n "..."

    play audio page_turn
    $ jnPause(2)

    n "Labels...{w=1.5}{nw}"
    extend " labels exist as program points to be called or jumped to,{w=1.5}{nw}"
    extend " either from Ren'Py script,{w=0.3} Python functions,{w=0.3} or from screens."
    n "..."
    $ jnPause(1)
    n "...What?"
    $ jnPause(1)

    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(2)

    n "..."
    n "Labels can be local or global...{w=1.5}{nw}"
    play audio page_turn
    extend " can transfer control to a label using the jump statement..."
    n "..."
    n "I see!{w=1.5}{nw}"
    extend " I see."
    $ jnPause(5)

    n "..."
    n "Yep!{w=1.5}{nw}"
    extend " I have no idea what I'm doing!"
    n "Can't believe I thought {i}this{/i} would help me...{w=1.5}{nw}"
    extend " '{i}award winning{/i}',{w=0.2} my butt."
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_held"))
    $ jn_events.displayVisuals("1fcspo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "O-{w=0.3}oh!"
    extend 1fllbgl " H-{w=0.3}hey,{w=0.2} [player]!"
    n 1ullss "I was just...{w=1.5}{nw}"
    extend 1nslss " doing...{w=1.5}{nw}"
    n 1fsrun "..."
    n 1fcswr "N-{w=0.2}nevermind that!"
    extend 1fllpo " This book is trash anyway."

    show natsuki 1fcspo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 4nslsr
    $ jnPause(4)
    hide black with Dissolve(1)

    n 4nllaj "So...{w=1}{nw}"
    extend 2fchbgsbl " what's new,{w=0.2} [player]?"

    return

# Natsuki tries out a new fashion manga.
# Prop courtesy of Almay @ https://twitter.com/art_almay
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_reading_a_la_mode",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_reading_a_la_mode:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ jnPause(5)

    n "Oh man...{w=1}{nw}"
    extend " this artwork..."
    n "It's so {i}{cps=\7.5}pretty{/cps}{/i}!"
    n "How the hell do they get so good at this?!"

    $ jnPause(3)
    play audio page_turn
    $ jnPause(5)

    n "Pffffft-!"
    n "The heck is {i}that{/i}?{w=1}{nw}"
    extend " What were you {i}thinking{/i}?!"
    n "This is {i}exactly{/i} why you leave the outfit design to the pros!"

    $ jnPause(1)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    show prop a_la_mode_manga_held zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1fdwca")
    $ jn_globals.force_quit_enabled = True

    n 1unmgslesu "Oh!{w=1}{nw}"
    extend 1fllbgl " H-{w=0.2}hey,{w=0.2} [player]!"
    n 1nsrss "I was just catching up on some reading time..."
    n 1fspaj "Who'd have guessed slice of life and fashion go so well together?"
    n 1fchbg "I gotta continue this one later!{w=1}{nw}"
    extend 1fchsm " I'm just gonna mark my place real quick,{w=0.2} one sec..."

    show natsuki 1fcssm
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio page_turn
    $ jnPause(1.5)
    play audio drawer
    hide prop a_la_mode_manga_held
    $ jnPause(4)
    hide black with Dissolve(1)

    n 3nchbg "Aaaand we're good to go!{w=1}{nw}"
    extend 3fwlsm " What's new,{w=0.2} [player]?"

    return

# Natsuki treats herself to a strawberry milkshake.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_drinking_strawberry_milkshake",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_drinking_strawberry_milkshake:
    $ jn_globals.force_quit_enabled = False
    n "..."

    play audio straw_sip
    $ jnPause(3)

    n "Man...{w=1}{nw}"
    extend " {i}sho good{/i}!"

    play audio straw_sip
    $ jnPause(3)

    n "Wow,{w=0.3} I've missed these...{w=1}{nw}"
    extend " why didn't I think of this before?!"

    play audio straw_sip
    $ jnPause(2)
    play audio straw_sip
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    show prop strawberry_milkshake zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1nchdr")
    $ jn_globals.force_quit_enabled = True

    n 4nchdr "..."
    play audio straw_sip
    n 4nsqdr "..."
    n 4uskdrlesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 2fbkwrl "[player_initial]-{w=0.3}[player]!{w=1}{nw}"
    extend 2flleml " I wish you'd stop just {i}appearing{/i} like that..."
    n 1fcseml "Jeez...{w=1}{nw}"
    extend 4fsqpo " you almost made me spill it!"
    n 4flrpo "At least let me finish up here real quick..."

    show natsuki 2fcsdrl
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio glass_move
    hide prop strawberry_milkshake
    show natsuki 4ncssm
    $ jnPause(2)
    hide black with Dissolve(1)

    n 4ncsss "Ah..."
    n 1uchgn "Man,{w=0.2} that hit the spot!"
    n 4fsqbg "And now I'm all refreshed...{w=1}{nw}"
    extend 3tsqsm " what's happening, [player]?{w=1}{nw}"
    extend 3fchsm " Ehehe."

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
    $ jnPause(2)
    n "Jeez..."
    n "Who {i}drew{/i} this?!"
    n "I feel like I'm gonna vomit rainbows or something!"
    $ jnPause(3)
    play audio page_turn
    $ jnPause(2)
    play audio page_turn
    $ jnPause(1)
    n "Man..."
    n "A-{w=0.3}alright,{w=0.2} enough drooling over the art!{w=1.5}{nw}"
    extend " You got this thing for a reason,{w=0.2} Natsuki..."
    n "Step by step..."
    n "Improve my daily confidence,{w=0.3} huh?{w=1.5}{nw}"
    extend " Okaaay..."

    $ jnPause(1)
    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    show prop step_by_step_manga_held zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1uskemfesh")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fpawrf "[player_initial]-{w=0.3}[player]!{w=0.2} Again?!{w=1}{nw}"
    extend 1fbkwrf " D-{w=0.3}do you really have to barge in like that {i}every{/i} time?"
    n 1flrunfess "Yeesh...{w=1}{nw}"
    extend 1fsremfess " I swear you're gonna be the death of me one of these days..."
    n 1fslpol "..."
    n 1tsqsll "...Huh?"
    n 1tnmpul "What?{w=0.2} Is something on my face?"
    n 1tllpuleqm "..."
    n 1uskajlesu "O-{w=0.3}oh!{w=0.75}{nw}"
    extend 1fdwbgl " The book!"
    n 1fcsbglsbl "I was just..."
    n 1fllunl "I was..."
    n 1fcsunf "Nnnnnn-!"
    n 1fcswrl "I-{w=0.2}I just like the artwork!{w=1}{nw}"
    extend 1fllemlsbl " That's all it is!"
    n 1fcswrl "I'm {i}super{/i} confident already!"
    n 1fllunlsbl "..."
    n 1fcsemlsbr "A-{w=0.2}and besides,{w=1}{nw}"
    extend 1fllpol " even if I {i}was{/i} reading it for the self-{w=0.2}help stuff..."
    n 1kllsll "..."
    n 1kwmpul "...What'd be wrong with that?"
    n 1fcsbol "It takes real guts to admit to yourself that you can do better.{w=1}{nw}"
    extend 1fnmbol " Can {i}be{/i} better."
    n 1fsrbol "...And only a real jerk would tease someone for trying."
    n 1fcsajl "Never forget that."

    play audio drawer
    hide prop step_by_step_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 4nllpol "..."
    n 4ulrbol "So..."
    n 3tnmsslsbr "What's new,{w=0.2} [player]?{w=1}{nw}"
    extend 3fllsslsbl " Ahaha..."

    return

# Natsuki finds her glasses in her drawer! They don't fit as well as she remembers...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_eyewear_problems",
            unlocked=True,
            conditional="persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_eyewear_problems:
    python:
        import copy
        import random

        jn_globals.force_quit_enabled = False

        # Unlock the starter glasses
        unlocked_eyewear = [
            jn_outfits.getWearable("jn_eyewear_round_glasses_black"),
            jn_outfits.getWearable("jn_eyewear_round_glasses_red"),
            jn_outfits.getWearable("jn_eyewear_round_glasses_brown"),
            jn_outfits.getWearable("jn_eyewear_round_sunglasses"),
            jn_outfits.getWearable("jn_eyewear_rectangular_glasses_black"),
            jn_outfits.getWearable("jn_eyewear_rectangular_glasses_red"),
        ]
        for eyewear in unlocked_eyewear:
            eyewear.unlock()

        # Make note of the loaded outfit, then give Natsuki a copy without eyewear so we can show off the new ones!
        outfit_to_restore = Natsuki.getOutfitName()
        eyewear_outfit = copy.copy(jn_outfits.getOutfit(outfit_to_restore))
        eyewear_outfit.eyewear = jn_outfits.getWearable("jn_none")
        jn_outfits.saveTemporaryOutfit(eyewear_outfit)

    n "..."
    play audio drawer
    $ jnPause(2)

    n "Oh,{w=0.75}{nw}"
    extend " come {i}on{/i}!{w=1}{nw}"
    play audio stationary_rustle_c
    extend " I {i}know{/i} I left them here!"
    n "I just know it!"

    $ jnPause(3)
    play audio drawer
    $ jnPause(2.25)
    play audio drawer
    $ jnPause(1.5)
    play audio stationary_rustle_a
    $ jnPause(0.5)

    n "I just don't get it!{w=1}{nw}"
    extend " It's not like anyone's even {i}here{/i} to mess around with my things any more!"
    n "Ugh...{w=1.25}{nw}"
    extend " I {i}knew{/i} I shouldn't have let Sayori borrow my desk for all the club stuff..."
    n "Reeeeal smooth,{w=0.5} Natsuki..."

    $ jnPause(2.5)
    play audio paper_crumple
    $ jnPause(1)

    n "And are these...{w=1} {i}candy wrappers{/i}?!"
    n "That's funny..."
    n "I don't remember ever saying my desk was a{w=0.2}{nw}"
    extend " {b}trash{/b}{w=0.33}{nw}"
    extend " {b}basket!{/b}"

    play audio gift_rustle
    $ jnPause(3.5)

    n "...Great.{w=0.75} And now my drawer is all sticky."
    n "Gross..."

    play audio paper_crumple
    $ jnPause(2.5)
    play audio paper_throw
    $ jnPause(3)

    n "Come on..."

    play audio stationary_rustle_b
    $ jnPause(1.5)
    play audio stationary_rustle_c
    $ jnPause(1.75)
    play audio drawer

    n "I can...{w=0.5} just about...{w=0.5} reach the back...!"
    play audio chair_in
    $ jnPause(1.5)
    n "Nnnnnng-!"

    $ jnPause(2)
    play audio gift_close
    $ jnPause(0.25)

    n "...!"
    n "T-{w=0.2}they're here?!{w=1}{nw}"
    extend " They're here!"
    n "Man,{w=0.2} that's a relief..."
    n "..."
    play audio glasses_case_open
    n "...I wonder if they still..."
    $ jnPause(3.5)

    menu:
        "Enter...":
            pass

    show prop glasses_case zorder JN_PROP_ZORDER
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_pre_slide
    $ jn_events.displayVisuals("1fcssmesi")
    $ jn_globals.force_quit_enabled = True

    n 1uskgsesu "...!"
    n 1ullajl "O-{w=0.2}oh!{w=1}{nw}"
    extend 4fllbglsbl " [player]!"
    n 4fcssslsbl "Heh."
    n 1fcsbglsbr "Well,{w=0.5}{nw}"
    extend 2fsqsglsbr " didn't {i}you{/i} pick a fine time to show up."
    n 2fcssglsbr "..."
    n 2tsqsslsbr "...So,{w=0.3} [player]?{w=1}{nw}"
    extend 4fchgnledzsbr " Notice anything different?"
    n 1tsqsmledz "...Mmm?"
    n 2usqctleme "Oho?{w=1}{nw}"
    extend 2fcsctl " What's that?"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down
    n 4tllbgl "Did I do something with my hair?{w=1}{nw}"
    extend 4fcssml " Ehehe."
    n 2nchgnleme "Nope!{w=0.5}{nw}"
    extend 2fcsbgl " I-{w=0.75}{nw}"
    n 2nsqbol "..."

    show natsuki 1fsqbof at jn_center zorder JN_NATSUKI_ZORDER
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_readjust
    $ jnPause(1)

    n 4fcspol "..."
    n 4fcsemfsbl "Ahem!"
    n 2fcsbglsbl "N-{w=0.2}nope!{w=0.75}{nw}"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down
    extend 1fchbglsbr " I-{w=0.2}it's not my hair,{w=0.2} [player]!"
    n 2tsqsmlsbr "What else did you-{w=1}{nw}"
    n 1fsranlsbl "..."
    n 4fcsanf "Nnnnn...!"

    show natsuki 1fcsunf at jn_center zorder JN_NATSUKI_ZORDER
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_readjust
    $ jnPause(1.15)

    n 4fcsemlesi "..."
    n 2fcstrlsbr "So!"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down_faster
    extend 2fsqbglesssbr " What else did you noti-{w=1}{nw}"
    n 1fslanlsbl "Uuuuuuuuu-!"

    menu:
        "Natsuki...":
            pass

    n 1fbkwrlesssbl "Alright!{w=0.75}{nw}"
    extend 4flrwrlesssbl" Alright!"
    n 2fcsgslsbr "I know,{w=0.33} okay?!"
    extend 2fsremlsbr " The glasses don't fit properly!"
    n 2fslsrl "They {i}never{/i} have."
    n 1ksrbol "And to think I wasted all that time trying to find them,{w=0.2} too..."
    n 4kcsemlesi "..."

    menu:
        "I think glasses suit you, Natsuki!":
            $ Natsuki.calculatedAffinityGain()
            if Natsuki.isEnamored(higher=True):
                n 1knmsll "..."
                n 4kllpul "...You really think so,{w=0.75}{nw}"
                extend 4knmpul " [player]?"
                n 1ksrunlsbl "..."
                n 1fcssslsbl "Heh."
                n 1fsldvlsbr "...Then I guess that at least wasn't a {i}total{/i} waste of time."
                n 2fcsajlsbr "Not that I {i}don't{/i} think I look good in them too,{w=0.5}{nw}"
                extend 2fcssmfsbl " o-{w=0.2}obviously."

            elif Natsuki.isAffectionate(higher=True):
                n 4uskemfeshsbl "...!{w=0.5}{nw}"
                n 2fcsgsfsbl "W-{w=0.3}well,{w=0.2} of course they do,{w=0.2} [player]!{w=1}{nw}"
                extend 2flrpolsbl " I {i}did{/i} pick them,{w=0.2} a-{w=0.2}after all."
                n 4ksrsllsbl "..."

            else:
                n 1fcsgslsbl "W-{w=0.2}well,{w=0.5}{nw}"
                extend 4fllgslsbl " duh!"
                n 2fcsbglsbr "Of course they suit me,{w=0.2} [player]!"
                n 4fcsemlsbr "I mean,{w=0.75}{nw}"
                extend 2fllemlsbr " You didn't seriously think I'd pick something that {i}wouldn't{/i} show off my sense of style,{w=0.75}{nw}"
                extend 2fnmpolsbr " did you?"
                n 1fcsemlsbl "Yeesh..."

        "Yeah, that was a waste of time.":
            $ Natsuki.percentageAffinityLoss(2)
            if Natsuki.isAffectionate(higher=True):
                n 4fskemlesh "H-{w=0.3}hey!{w=1}{nw}"
                extend 1fsqwrl " And listening to you being so rude {i}isn't{/i}?"
                n 2flreml "Yeesh..."
                n 2fsreml "{i}Someone{/i} woke up on the wrong side of the bed..."
                n 2fsrsll "..."

            else:
                n 4fskwrlesh "H-{w=0.2}hey!{w=0.5}{nw}"
                extend 1fnmgsl " What was that for?!"
                n 2fnmwrl "And as if you acting like a jerk {i}isn't{/i}?"
                n 2fsrsllean "..."

        "...":
            n 1fllsll "..."
            n 4knmeml "...What?"
            extend 2fsqemlsbr " The silent act {i}definitely{/i} isn't helping,"
            extend 2fsrpolsbl " you jerk..."

    n 1fcsajl "Well,{w=0.3} whatever.{w=1}{nw}"
    extend 2fllsll " At least I know where they are now,"
    extend 2fslbol " I suppose."
    n 1fcseml "...And wearing them all high up like that was dorky,{w=0.5}{nw}"
    extend 2fcspol " a-{w=0.2}anyway."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    # Hide glasses overlay and restore old outfit
    hide prop
    hide overlay
    $ Natsuki.setOutfit(jn_outfits.getOutfit(outfit_to_restore))
    show natsuki 1fcsbol at jn_center zorder JN_NATSUKI_ZORDER
    play audio glasses_case_close
    $ jnPause(0.75)
    play audio drawer
    $ jnPause(3)
    hide black with Dissolve(2)

    n 4nsrcal "..."
    n 4nsrajl "I...{w=0.75}{nw}"
    extend 1nsrsslsbl " guess I should apologize for all of...{w=1.25}{nw}"
    extend 2nslsllsbl " that."
    n 2nsrpolsbl "Not exactly rolling out the red carpet here,{w=0.2} am I?{w=0.75}{nw}"
    extend 1nslsslsbl " Heh."
    n 4fcsajlsbr "A-{w=0.2}and besides."
    n 3fslsslsbr "I think that's about enough of that{w=0.75}{nw}"
    extend 3fsqbglsbr " {i}spectacle{/i},{w=1}{nw}"
    extend 3nsqbglsbr " huh?"
    n 1nsrsslsbr "So..."
    n 2kchsslesd "W-{w=0.2}what's new,{w=0.2} [player]?"

    return

# Natsuki learns why you should always have a charging cable on hand...
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_battery_dead",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_battery_dead:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_a
    n "..."
    n "...Ha!"
    play audio button_tap_b
    n "..."

    play audio button_mashing_b
    $ jnPause(3)
    play audio button_mashing_a

    n "Oh,{w=0.3} come {i}on{/i}!{w=1.25}{nw}"
    extend " As {i}if{/i} that hit me!"
    play audio button_mashing_c

    $ jnPause(2)
    play audio button_mashing_b

    n "Nnnng-!"
    n "G-{w=0.2}get OFF me!{w=0.5}{nw}"
    extend " Jeez!"
    play audio button_mashing_a
    n "I HATE these enemies!"
    n "Did they {i}have{/i} to add so many?!"

    $ jnPause(3)
    play audio button_mashing_b

    n "Get out of my way!{w=0.75}{nw}"
    play audio button_tap_b
    extend " It's right there!{w=0.75}{nw}"
    extend " I'm SO {i}close{/i}!"
    play audio button_tap_a
    n "Come on...{w=1}{nw}"
    play audio button_mashing_c
    extend " {i}come on{/i}...!"

    menu:
        "Enter...":
            pass

    show prop wintendo_twitch_playing free zorder JN_PROP_ZORDER
    show natsuki gaming at jn_center zorder JN_NATSUKI_ZORDER
    $ jn_events.displayVisuals("1fdwfol")
    $ jn_globals.force_quit_enabled = True
    $ jnPause(3)

    n 1fdwanl "Nnnnnn...!"
    play audio button_mashing_a
    n 1fdwpoless "Uuuuuuu-!"
    n 1fdwfo "..."
    play audio button_mashing_c
    n 1fdwfoesssbl "Mmmmmm...!"

    show prop wintendo_twitch_held free zorder JN_PROP_ZORDER

    n 1uchbsedz "YES!{w=1.25}{nw}"
    extend 1uchgnedz " FINALLY!"
    n 1kcsbgesisbl "Haah..."
    n 1fcsbgemesbr "Stick {i}that{/i} in your pipe and smoke it!"

    show prop wintendo_twitch_battery_low zorder JN_PROP_ZORDER

    n 1kcsssemesbr "..."
    n 1ksqsmsbl "...{w=0.75}{nw}"
    n 1uskemleshsbl "...!"
    n 1fllbglsbl "A-{w=0.2}ah!"
    extend 1fchbglsbr " H-{w=0.2}hey,{w=0.2} [player]!"
    extend 1tchbglsbr " What's up?"
    n 1kcssssbl "Man..."
    n 1fsldvsbl "Sorry,"
    extend 1fcsgssbl " but you have no {i}IDEA{/i} how long I was trying to beat that stage!"
    n 1fnmpol "Seriously!"
    n 1fcsajl "I mean,{w=1}{nw}"
    extend 1fsrajlsbl " it's not like I was getting {i}upset{/i} or anything..."
    n 1fcsbglsbr "I'm {i}way{/i} past getting vexed over games,{w=0.2} of all things."
    n 1fslbglsbr "T-{w=0.2}they're just lucky I {i}chose{/i} not to go all out.{w=1}{nw}"
    extend 1fcsajlsbr " That's all.{w=1}{nw}"
    extend 1nchgnl " Ehehe."
    n 1nchsmleme "..."
    n 1tnmbo "Eh?"
    extend 1klrbgesssbl " Oh,{w=0.2} right!{w=0.75}{nw}"
    extend 1fchbgesssbr " Sorry!{w=0.75}{nw}"
    extend 1flrdvlsbr " I'm almost done anyway."
    n 1ucssslsbr "All I gotta do is save,{w=0.5}{nw}"

    show prop wintendo_twitch_dead zorder JN_PROP_ZORDER

    extend " and I'll be right-{w=1.25}{nw}"
    n 1udwssl "..."
    n 1ndwbo "..."
    n 1fdwem "...But I..."
    n 1fdwwr "I-{w=0.2}I just...{w=0.5}{nw}"
    extend 1fdwun " charged..."
    n 1fdwanl "..."
    n 1fcsful "..."
    n 1fcsunl "..."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    play audio chair_out_in
    $ jnPause(5)
    hide black with Dissolve(2)

    n 4ndtbo "..."
    n 4nslbo "..."
    n 4ndtca "..."
    n 2fdteml "This stays between us."
    n 2fsqfrlsbl "Got it?"
    n 1nsrpolsbl "..."
    n 4nsrajlsbl "...So.{w=1}{nw}"
    extend 2tsqsllsbl " What's new,{w=0.2} [player]?"

    return

# Natsuki jumps at the player entering the room, right as she's about to win a game... uh oh.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_game_over",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_game_over:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_b
    n "..."
    n "Ehehe..."
    play audio button_mashing_a
    n "Oh yeah.{w=0.5} Uh huh."

    play audio button_mashing_b
    $ jnPause(2)
    play audio button_mashing_a
    $ jnPause(2)

    n "Ugh!{w=0.5}{nw}"
    play audio button_mashing_c
    extend " Get up!{w=0.75} Get UP!"
    n "Counter,{w=0.2} you idiot!"

    play audio button_mashing_b
    $ jnPause(1)

    n "Yeah!{w=0.75} Now THAT's what I'm talking about!"
    play audio button_mashing_c
    n "Three hits!{w=0.5}{nw}"
    extend " Four hits!{w=0.3}{nw}"
    extend " Five hits!"
    n "You're on {i}fire{/i},{w=0.2} Natsuki!"

    play audio button_mashing_b
    $ jnPause(3)
    play audio button_mashing_a

    n "Oh man,{w=0.2} I'm ACING this!"
    play audio button_tap_b
    n "Yeah!{w=0.75}{nw}"
    play audio button_tap_a
    extend " Yeah! Come on!"
    play audio button_mashing_c
    n "Just a few more hits...!"

    menu:
        "Enter...":
            pass

    show prop wintendo_twitch_held charging zorder JN_PROP_ZORDER
    show natsuki gaming at jn_center zorder JN_NATSUKI_ZORDER
    $ jn_events.displayVisuals("1unmpu")
    $ jn_globals.force_quit_enabled = True
    $ jnPause(0.5)

    n 1unmemesu "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fnmgs "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1fllemlsbr " H-{w=0.2}how many times do I gotta tell y-{w=0.25}{nw}"
    play audio twitch_die
    n 1nskemlsbr "...{w=0.5}{nw}"
    play audio twitch_you_lose
    n 1fdwemsbl "..."
    n 1fcsansbl "..."
    n 1fcsemsbl "Are.{w=0.75}{nw}"
    extend 1fcsfusbr " You.{w=0.75}{nw}"
    extend 1fbkwrleansbr " KIDDING ME?!"
    $ player_final = jn_utils.getPlayerFinal(repeat_times=2)
    n 1kbkwrlsbr "[player][player_final]!{w=1}{nw}"
    extend 1fllgslsbr " Come on!"
    n 1fcswrlsbr "Y-{w=0.2}you totally threw off my groove!{w=0.75}{nw}"
    extend 1fsqpolsbl " You big jerk!"
    n 1kcsemesisbl "..."
    n 1kdwwr "...And now I gotta do {i}that{/i} all over again?{w=1}{nw}"
    extend 1kcspu " Man..."
    n 1fslsl "..."
    n 1flrtr "I guess I'll just do that later."
    n 1fsqcal "{b}Again{/b}."
    n 1fcsajlsbl "You're just lucky I've done that part so many times {i}already{/i},{w=0.2} [player].{w=0.75}{nw}"
    extend 1fcscalesm " Trust me."
    n 1ccspol "A-{w=0.2}as if I'd seriously let some minor setback annoy me {i}that{/i} much."

    show natsuki 1csrpol
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    play audio chair_out_in
    show natsuki 4nsrbol
    $ jnPause(5)
    hide black with Dissolve(2)

    n 4nsrcal "..."
    n 2nnmtrl "Well,{w=0.2} [player].{w=0.75}{nw}"
    extend 2nsqtrl " Hope you're buckled up."
    n 2nsrpol "...'Cause now you owe me {i}twice{/i} as much fun today to make up for that."
    n 4nsqbol "..."
    n 4fsqajl "Well?{w=0.75}{nw}"
    extend 3fcspolesi " Get to it then,{w=0.2} [player]!{w=0.75}{nw}"
    extend 3fsqsml " Ehehe."

    return

# Natsuki shares tips how to stay warm at chilly days
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_warm_package",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7 and persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_warm_package:
    python:
        jn_globals.force_quit_enabled = False
        teddy_cardigan_outfit = jn_outfits.getOutfit("jn_cosy_cardigan_outfit")
        teddy_cardigan_outfit.unlock()
        Natsuki.setOutfit(teddy_cardigan_outfit)

    if jn_atmosphere.isCurrentWeatherRain() or jn_atmosphere.isCurrentWeatherThunder():
        n "..."
        n "Uuuuuuu-!"
        n "You've {w=0.2}{i}got{/i}{w=0.2} to be kidding me."
        n "Rain?!{w=0.75} {i}Again?!{/i}"
        n "It's always freezing here when it does that!{w=1} I don't even {i}have{/i} a radiator to turn on!"
        $ jnPause(3)
        n "Ugh..."
        n "You know what?{w=0.75} Screw this!"
        play audio chair_out
        n "Someone {i}had{/i} to have left a coat or...{w=0.75} {i}something{/i}{w=0.5} lying around..."
        $ jnPause(3)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "..."
        n "Jeez..."
        n "How is this not enough?{w=1} I'm {i}still{/i} freezing my butt off!"

        $ jnPause(3)
        play audio gift_slide
        $ jnPause(1)
        play audio gift_open

        n "Uuuuu..."
        n "You'd think the {i}star{/i} of the debate club would have at least {i}tried{/i} to talk our way into a warm clubroom."
        n "I can barely feel my toes..."

        $ jnPause(3)
        play audio gift_open

        n "...!"
        n "Oh man,{w=0.2} am I glad to see you {i}here{/i}!"
        n "...Wait.{w=1} How did {i}you{/i} survive being in a classroom with Sayori around...?"
        n "..."
        n "...Doesn't matter.{w=0.75} Too cold to question it.{w=1} Now where did they leave the kettle last time..."
        n "Aha!{w=0.75} Right!{w=0.3} Just gotta plug it in there,{w=0.2} and..."
        $ jnPause(2)

    elif jn_atmosphere.isCurrentWeatherSnow():
        n "..."
        n "Uuuuuuu...!"
        n "As if being stuck here wasn't enough of a cold shoulder..."
        n "Now the {i}weather{/i} is giving me one!{w=1} Literally!"
        n "Forget frostbite!{w=0.3} I'm getting frost-{w=0.5}{i}butt{/i}!{w=1} I am {i}so{/i} done with this..."
        n "..."
        n "Oh, screw it!{w=0.75} I'm a girl of action!"
        n "I don't have to stand for this!"

        play audio chair_out
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "Man...{w=0.75} I {i}really{/i} should've tidied all this up before..."
        n "Look at all this junk!{w=0.75} Sheesh..."
        n "...No wonder all my stuff kept getting lost in here."
        $ jnPause(3)
        n "..."
        n "...!"
        n "H-{w=0.2}how did {i}you{/i} end up here?{w=0.75} I thought you were gone forever!"

        play audio clothing_ruffle
        $ jnPause(3)

        n "Come on...{w=0.75} what else...{w=0.5} what else..."
        n "..."
        n "Ugh...{w=1} now my fingers are all numb..."

        $ jnPause(3)
        play audio gift_slide
        $ jnPause(2)

        n "...Eh?{w=0.75} What do we have here...?"
        play audio gift_open
        n "...!"
        n "SCORE!"
        n "Natsuki,{w=0.2} you've done it again!"
        n "Alright...{w=1.25} now,{w=0.2} where did she put the kettle..."
        play audio gift_slide
        $ jnPause(2)
        n "Aha!{w=0.75} There we go.{w=1} Come to mama..."

    else:
        n "..."
        n "Ugh...{w=0.75} I {i}seriously{/i} cannot believe my luck sometimes."
        n "Out of all the places I could have been stuck inside for {i}literally forever...{/i}"
        n "Did it {i}really{/i} have to be the one classroom {i}without{/i} central heating?!"
        n "Come {i}on{/i}..."

        $ jnPause(3)

        n "...Wait."
        n "..."
        n "Didn't I...?{w=1} I'm sure I did..."

        play audio chair_out
        $ jnPause(3)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "Man,{w=0.2} I honestly forgot just how much junk is back here..."
        n "No wonder the teacher got all antsy about my books."

        $ jnPause(2)
        play audio clothing_ruffle

        n "Yuri's...{w=0.75} Yuri's...{w=0.75} Yuri's..."
        play audio clothing_ruffle
        n "Monika's..."
        $ jnPause(2)
        play audio clothing_ruffle
        $ jnPause(3)
        n "..."
        n "...{b}Definitely{/b}{w=0.25} Yuri's."
        n "..."
        n "Aha!{w=0.2} I knew it!{w=1} Take {i}that{/i},{w=0.2} academy uniform guidelines!"
        play audio clothing_ruffle
        $ jnPause(3)
        play audio gift_open
        n "...Eh?{w=0.2} And is this...?"
        n "I-{w=0.2}it is!"
        n "Oh man...{w=1} JACKPOT!{w=0.75} Ehehe."

    play audio switch_flip
    $ jnPause(2)
    play audio kettle_boil
    $ jnPause(5)
    play audio drink_pour
    $ jnPause(7)
    play audio chair_in
    $ jnPause(3)

    menu:
        "Enter...":
            pass

    show prop hot_chocolate hot zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1fsqbl")
    $ jn_globals.force_quit_enabled = True

    n 1kcsbsesi "Haah...{w=1.5}{nw}"
    extend 1fchsmedz " perfecto!"
    n 2fcsbg "Who {i}needs{/i} working heating when you have hot chocolate?"
    n 2fcssmlesisbl "{i}And{/i} I didn't even burn my tongue this time!"

    n 2ndwsm "..."
    n 2uwdgseex "...!"
    n 4fllbglsbl "W-{w=0.2}well,{w=0.75}{nw}"
    extend 2fcsbglsbl " hello [player]!"
    n 2fllsmlsbl "..."
    n 2tsqsml "...?"
    n 2tsqctl "Oho?"
    n 4nchts "Is that a hint of {i}jealousy{/i} I spy there,{w=0.2} [player]?{w=1}{nw}"
    extend 1fsqsmleme " Ehehe."
    n 2uchgn "Well,{w=0.2} can't say I blame you!"
    n 2fllbg "I mean...{w=0.5}{nw}"
    extend 4fspgsedz " have you {i}seen{/i} this right here?"
    n 1ncsajsbl "...And no,{w=0.5}{nw}"
    extend 2fslpo " I don't care how unhealthy it is."
    n 1fsqcaesi "I {i}always{/i} make an exception for hot chocolate."
    n 4fcstr "Besides,{w=0.2} you know what they say."
    n 2fchgn "...Go big or go home,{w=0.3} right?{w=0.75}{nw}"
    extend 2fchsml " Ehehe."
    n 1fllgs "Seriously,{w=0.2} hot chocolate just wouldn't {i}be{/i} hot chocolate without {i}all{/i} the extras!"
    n 2fcsgs "Cream?{w=0.3} Check!{w=0.3} Marshmallows?{w=0.3} Check!"
    n 2fsqcal "...My special panda mug?{w=1.25}{nw}"
    extend 4fcssml " Check again!"
    n 1fchbgl "Perfection!{w=0.75}{nw}"
    extend 2fcstsl " If I do say so myself~."

    n 2ullss "Well,{w=0.5}{nw}"
    extend 4fsqss " as much as I'm sure you'd {i}love{/i} to share this with me,{w=0.2} [player]..."
    n 1fcscaesi "There's some things I just can't allow.{w=0.75}{nw}"
    extend 1fsqsm " Ehehe."
    n 2fsqbg "So!{w=0.5} Prepare yourself."
    n 2fchbg "...'Cause I'm gonna share some pretty {i}hot{/i} tips of my own instead!"
    n 4fsqbg "That's right,{w=0.2} [player].{w=1}{nw}"
    extend 2fchbledz " You've got front row seats to another lesson from yours truly~!"
    n 1fcsaj "As you can see,{w=0.75}{nw}"
    extend 2fcstr " it isn't exactly hard to stay nice and toasty if you know what you're doing..."
    n 2fchsm "...And it all begins with what you wear!"
    n 4fllpu "Think of it as a fight:{w=0.75}{nw}"
    extend 1flrem " the cold is your opponent,{w=1}{nw}"
    extend 2fcspoesi " and your clothing is your armor!"

    n 2ullaj "Now{w=0.2} -{w=0.2} obviously,{w=0.2} you're gonna want to start with layers.{w=0.75}{nw}"
    extend 2nsrss " You probably knew that much already."
    n 1fnmgs "But that doesn't mean you should just throw on {i}anything{/i} you can find!"
    n 4fcspo "You really gotta {i}think{/i} about what exactly you're putting on -{w=1}{nw}"
    extend 4unmaj " like the material!"
    n 2fslaj "If your clothes aren't breathable,{w=0.75}{nw}"
    extend 2fsqpu " then you'll just end up getting all sticky and sweaty under all that fabric..."
    n 1fcsan "...And wet clothes are useless at keeping the heat in!"
    n 4ksqup "The last thing you want is being freezing cold {i}and{/i} stinky..."
    n 2fcsaj "So pick your layers{w=0.75}{nw}"
    extend 2fslpu " -{w=0.5} and how many of them -{w=0.5}{nw}"
    extend 2fchsm " wisely!"

    n 2fcsgs "Next up: ditch the tight clothes!"
    n 1nsqem "You {i}really{/i} want stuff that gives you at least some kind of gap between your skin and the fabric."
    n 1ullaj "That way,{w=0.2} all the heat from your body stays trapped around you -{w=0.75}{nw}"
    extend 4fchgn " like a little toasty shield!"
    n 4flrsl "If you just wear something like leggings,{w=0.5}{nw}"
    extend 1fsqsl " then all that warmth goes straight from your body,{w=0.2} into the cloth..."
    n 2fllem  "...And then the air just snatches it away,{w=0.2} like a professional freeloader!{w=0.75}{nw}"
    extend 2fcswr " What a waste!"
    n 4fslss "Besides,{w=0.2} unless you're a professional cyclist or something,{w=1}{nw}"
    extend 2fsqss " I {i}highly{/i} doubt you need the aerodynamics..."
    n 2fchbg "So keep 'em nice and baggy,{w=0.2} [player]!{w=0.75}{nw}"
    extend 4nchgn " Easy peasy!"

    n 4uwdaj "Oh -{w=0.5}{nw}"
    extend 1nllaj " right,{w=0.2} and most of all?"
    n 1ncssr "..."
    n 2nsqaj "...Just don't be a dork about going outside,{w=0.2} alright?"
    n 4nslss "I mean,{w=0.2} I get it -{w=0.5}{nw}"
    extend 1ksqss " sometimes you just have things that {i}need{/i} to be done out there.{w=0.75}{nw}"
    extend 1ksrsm " It happens.{w=1}{nw}"
    extend 4ksrsl " But..."
    n 4ksqbo "...Just know your limits.{w=0.5}{nw}"
    extend 1ksqpo " Warm up {i}properly{/i} if you've spent ages in crappy weather,{w=0.5}{nw}"
    extend 1fslpo " or nasty old buildings..."
    n 2fcsaj "Decent shelter,{w=0.2} hot drinks,{w=0.5}{nw}"


    if Natsuki.isLove(higher=True):
        extend 2tslss " warm food..."
        n 1nsldvleafsbl "Some quality time with your favorite girl..."
        n 4fchsmlsbl "I-{w=0.2}it all counts!"

    elif Natsuki.isAffectionate(higher=True):
        extend 2tslss " warm food..."
        n 1fsrdvl "S-{w=0.2}some quality time with a certain someone..."
        n 4fcssslsbr "I-{w=0.2}it all counts!"

    else:
        extend 2tslss " warm food...{w=0.5}{nw}"
        extend 4unmaj " you'd be surprised how much a little baking can turn up the heat!"
        n 1fslslsbr "...Speaking from experience."
        n 1kslsl "..."
        n 2fcsbgsbr "B-{w=0.2}but yeah!"

    show prop hot_chocolate cold

    n 2nchsm "And that about {i}wraps{/i} things up!{w=0.75}"
    extend 2nllss " I-"
    n 1unmsf "..."
    n 4udwemeshsbl "...!"
    n 4uskemsbl "M-{w=0.2}my drink!{w=1}{nw}"
    extend 4kbkwresssbr " I-{w=0.2}it's getting all cold!{w=0.75}{nw}"

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1)
    hide prop hot_chocolate
    play audio straw_sip
    $ jnPause(2)
    play audio glass_move
    show natsuki 1kcsss at jn_center zorder JN_NATSUKI_ZORDER
    $ jnPause(3)
    hide black with Dissolve(2)

    n 1kcsbgesi "Haaah...{w=1.25}{nw}"
    extend 4nchtseme " much better!"
    n 3fsqsm "Now that's out of the way,{w=0.2} [player]..."
    n 3usqbg "...How about {i}you{/i} warm up that conversational muscle of yours?{w=1}{nw}"
    extend 1fsqsmeme " Ehehe."
    n 2tsqss "Well?{w=0.75}{nw}"
    extend 2fchbl " I'm waiting!"

    return

# Natsuki finds a new friend in the clubroom!
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_sanjo",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_sanjo:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Man...{w=1} is there seriously {i}nothing else{/i} to do in this dump?{w=0.75} I'm so {b}bored{/b}!"
    n "Would it actually have {i}killed them{/i} to keep some board games here or what?"
    n "Ugh..."

    $ jnPause(5)

    n "..."
    n "Oh,{w=0.2} screw this!{w=0.75} I'm done just sitting around.{w=0.75} {i}Again{/i}." 
    n "There's gotta be something I missed in the teacher's desk or...{w=1} something..."

    play audio chair_out
    $ jnPause(3)

    n "..."

    play audio drawer
    $ jnPause(3)
    n "Huh.{w=0.75} Since when did the teachers keep so much stationary around?{w=0.75} Neat."
    n "Pretty sure nobody would mind if I...{w=1} just..."
    play audio stationary_rustle_c
    $ jnPause(0.75)
    n "Yoink."
    $ jnPause(3)

    n "Alright...{w=1} now what have we got here..."
    $ jnPause(2)
    
    n "Trash..."
    play audio stationary_rustle_a
    extend " more trash..."
    play audio stationary_rustle_b
    n "..."
    play audio paper_crumple
    n "Huh?{w=0.75} What's...?"
    n "..."
    n "...Oh,{w=0.75} {i}yuck{/i}!{w=0.75} G-{w=0.2}gross!"
    play audio paper_throw
    $ jnPause(2)
    n "I-{w=0.2}I don't even {i}want{/i} to know what was in {i}that{/i}..."
    n "Almost makes me wanna hurl."

    play audio drawer
    $ jnPause(4)

    n "..."
    n "...Huh?" 
    n "Wait.{w=0.75} Is that...?"
    n "..."
    n "I-{w=0.2}it is!{w=0.75} What are {i}you{/i} still doing here?" 
    n "...And what kind of inconsiderate jerk just left you {i}there{/i}?"

    play audio gift_slide
    $ jnPause(1)
    play audio necklace_clip
    n "Ack!{w=0.5} My finger!{w=0.75} P-{w=0.2}pricked it..."
    $ jnPause(3)

    n "Man...{w=1} and you're all nasty and crusty now too."
    n "..."
    n "Alright.{w=0.75} I guess I better get you all fixed up..."

    $ jnPause(2)
    play audio drink_pour
    $ jnPause(2)
    play audio glasses_case_close
    $ jnPause(2)
    play audio chair_in
    $ jnPause(2)

    menu:
        "Enter...":
            pass
    
    $ sanjo = jn_desk_items.getDeskItem("jn_sanjo")
    $ Natsuki.setDeskItem(sanjo)
    $ jn_events.displayVisuals("2fcssm")
    $ jn_globals.force_quit_enabled = True

    n 2fcssmeme "...{w=0.75}{nw}"
    n 2ccssm "...{w=0.75}{nw}"
    n 2tsqbo "...?{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 2unmgslesh "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fbkwrl " Jeez!{w=0.75}{nw}"
    extend 4flrwrlsbl " Since when did {i}you{/i} get here?"
    n 4fsqemlsbl "Did you seriously just wait outside the room for all that time?!{w=0.75}{nw}"
    extend 4csqfllsbl " How long were you even {i}there{/i}?"
    n 4ccsemsbl "Ugh..."
    n 2flrflsbr "I really wish you'd stop doing that.{w=0.75}{nw}"
    extend 2fsqposbr " You big jerk.{w=0.75}{nw}"
    extend 2ccsposbr " You should know I hate being made to jump by now."
    n 4ccsemsbl "A-{w=0.2}and anyway,{w=0.2} [player].{w=0.75}{nw}"
    extend 4cllaj " Can't you see I'm {i}busy{/i} here already?{w=0.75}{nw}"
    extend 3cslbo " Yeesh."

    if Natsuki.isEnamored(higher=True):
        n 4ccsfl "I mean,{w=0.75}{nw}"
        extend 5cllfll " it's not that I mind {i}that{/i} much.{w=0.75}{nw}"
        extend 3ccspolsbr " B-{w=0.2}but still."
        n 3ccsajlsbr "A little notice would have been nice.{w=1}{nw}"
        extend 3nsrbolsbr " That's all I'm saying."
    
    else:
        n 3ccstr "Talk about inconsiderate.{w=0.75}{nw}"
        extend 3csrca " You could at least give me some kinda notice or something next time."
    
    n 4csrbo "..."
    n 4tsqbo "..."
    n 2tnmfl "...What?{w=0.75}{nw}"
    extend 2cnmflsbl " What's the deal with {i}that{/i} look,{w=0.5}{nw}"
    extend 2clrflsbl " all of a sudden?"

    show natsuki option_wait_sulky
    menu:
        n "If you've got something you gotta ask then just say it already,{w=0.2} [player]."

        "What's with the plant, [n_name]?":
            n 1csqfl "...Seriously,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2fsqem " 'What's with the plant'?"
            n 4fllem "And just what exactly is {i}that{/i} supposed to mean?{w=0.75}{nw}" 
            extend 4fnmaj " Huh?"
            n 3fcsgs "You trying to say he needs an {i}excuse{/i} to be here or something?{w=0.75}{nw}"
            extend 3fcspo " Sheesh."
            n 1csrbo "Talk about rolling out the red carpet."
            n 4ccsaj "Besides."
            n 2fslfl "{i}'The plant'{/i} has a name,{w=0.5}{nw}" 
            extend 2ccsaj " you know."
            n 2cllbo "..."
            n 2cslbolsbl "..."
            n 5csqcalsbl "...It's Sanjo."

        "Looks like you and the plant have something in common...":
            n 4fsqfl "...A-{w=0.2}and what exactly {i}is{/i} that,{w=0.5}{nw}"
            extend 4fsqem " [player]?"
            n 2fsqca "..."
            n 2fcsgs "No,{w=0.2} no.{w=0.75}{nw}"
            extend 4fnmaj " Go on.{w=1}{nw}"
            extend 3fsqca " I {i}insist{/i}."
            n 3fsqbo "..."
            n 3tsqfl "Well?"
            n 3ccsss "Don't start getting cold feet now,{w=0.2} [player].{w=0.75}{nw}"
            extend 3ccsfl " Spit it out!"
            n 4csqfs "..."
            n 4fcsfs "Heh.{w=0.75}{nw}"
            extend 2fcsfl " Yeah."
            n 2fcspoesm "That's about what Sanjo here and I thought."

        "...":
            n 5csrunsbr "..."
            n 5csqemsbr "W-{w=0.2}what?{w=0.75}{nw}"
            extend 4ccsajsbr " Don't look at me like that,{w=0.2} [player]."
            n 3ccsflsbr "Besides."
            n 3ccsposbr "...You'll annoy Sanjo here."
    
    n 1ccsajlsbr "A-{w=0.2}and no,{w=0.5}{nw}"
    extend 5cdlbosbr " I didn't name him myself."
    n 4tllpu "In fact...{w=0.75}{nw}"
    extend 7tllbo " come to think of it.{w=1}{nw}"
    extend 7tnmfl " I don't actually know {i}who{/i} did."
    n 3unmaj "One of the teachers just kinda brought him in one day and told the class to take care of him.{w=0.75}{nw}"
    extend 3clrpu " Then just never bothered taking him back."
    n 3tlraj "So...{w=1}{nw}"
    extend 7tnmbo " I guess we kinda just took to having him around,{w=0.2} I suppose."
    n 4cslfl "...Still doesn't explain why someone just decided to shove him underneath the teacher's desk though.{w=0.75}{nw}"
    extend 4fslem " Jerks."
    n 2ccsfl "Well,{w=0.2} whatever.{w=0.75}{nw}"
    extend 2ulrfl " He's been left around long enough,{w=0.5}{nw}"
    extend 1fcstr " so clearly {i}someone{/i} is gonna have to take care of Sanjo here."
    n 3fchgn "...And who better to step up to the plate than yours truly!"
    n 3fsqsm "Ehehe.{w=0.75}{nw}"
    extend 6fcsbg " Yep!"
    n 3fcssmesm "I think it's about time [n_name] finally got her green thumb going!"
    n 4clrbgsbl "Don't get me wrong -{w=0.5}{nw}"
    extend 4csrsssbl " I'm not saying I'm gonna be some professional gardener or anything like that.{w=0.75}{nw}"
    extend 7fcsss " But let's face it."
    n 7ullaj "If you're gonna take up a little horticulture..."
    n 6fchbg "Where better to start than a cactus,{w=0.2} right?"
    n 4tlrss "Think about it,{w=0.2} [player] -{w=0.5}{nw}" 
    extend 3fdlsm " this little guy was practically {i}made{/i} for a beginner.{w=0.75}{nw}"
    extend 6fcsbg " He basically already fends for himself!"
    n 7ulraj "Plus I mean...{w=0.75}{nw}"
    extend 7unmbo " it's not like I've really gotta go out of my way to take care of him either.{w=1}{nw}"
    extend 3cdlss " I think you can guess why."
    n 1ullss "Some sunlight here,{w=0.2} a couple splashes of water there...{w=1}{nw}"
    extend 2fcsbg " how hard could it {i}possibly{/i} be?"
    n 2fcssmesm "Ehehe."
    n 4fcsaj "So!"
    n 2flrss "You better keep your eyes and ears{w=0.5}{nw}" 
    extend 2fsqss " {i}pricked{/i},{w=0.75}{nw}" 
    extend 4fsqbg " [player]..."
    n 3nchgnl "'Cause I'm gonna get Sanjo here blooming before you know it!"

    $ sanjo.unlock()
    return

# Natsuki is walked in on reading a new volume of Parfait Girls. She isn't impressed.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_house_of_cards",
            unlocked=True,
            conditional="persistent.jn_snap_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_house_of_cards:
    $ jn_globals.force_quit_enabled = False
    play audio card_place
    $ jnPause(5)
    n "And...{w=1}{nw}" 
    play audio card_place
    extend " that's another one!{w=1} Yes!"
    n "Jeez...{w=1} why didn't I think of this before?{w=0.75} This is actually {i}way{/i} more fun than I thought!"
    n "Ehehe."

    $ jnPause(1)
    play audio card_place
    $ jnPause(2)

    n "..."
    n "..."
    n "Nnnnnnnn..."
    n "..."
    play audio card_place
    $ jnPause(1.5)
    n "Yes!{w=0.75} 'Kay...{w=1.25} another one..."
    n "I swear,{w=0.2} if this crappy desk wobbles again now..."

    $ jnPause(2)

    n "Mmmmm...!"
    n "..."
    play audio card_place
    $ jnPause(1.5)
    n "Alright!{w=0.75} Man...{w=1} [n_name], you are on a {i}roll{/i}!{w=0.75} This is the furthest I've gotten yet!"
    $ jnPause(1)
    n "...R-{w=0.2}right.{w=0.75} Next card..."

    $ jnPause(1.5)
    play audio card_place
    $ jnPause(3)

    n "E-{w=0.2}easy...{w=1} come on...{w=1} don't throw this one now..."
    n "..."
    n "So...{w=1.5} close..."
    play audio chair_in
    n "Just gotta...{w=1} balance it...{w=1} right...!"
    $ jnPause(1)

    menu:
        "Enter...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_house_of_cards"))
    $ jn_events.displayVisuals("4fdwpusbr")
    $ jn_globals.force_quit_enabled = True

    n 4fdwfosbr "..."
    n 4tsqpueqmsbr "...?{w=0.75}{nw}"
    n 4uskemleshsbl "...!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 4fbkwrlsbr "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fllwrlsbr " Jeez!{w=0.75}{nw}"
    extend 4fcsgslsbr " H-{w=0.2}how many times do I have to remind you?!"
    n 4ftlemlsbr "I swear it's like you're actually {i}trying{/i} to give me a heart attack!{w=0.75}{nw}"
    extend 4fcsgssbr " Come on!\n{w=0.75}{nw}"
    extend 4csqemsbl "Is knocking {i}seriously{/i} that hard?"
    n 2fcswrsbl "A-{w=0.2}and besides!{w=0.75}{nw}"
    extend 2fdwwrsbr " Look!{w=0.75}{nw}"
    extend 4fcsgssbr " Can't you {i}see{/i} I'm clearly busy right-{nw}"

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pile"))
    show natsuki 1uskemeexsbl
    play audio card_shuffle
    $ jnPause(1)
    show natsuki 1ndwflsbl
    $ jnPause(4)

    n 4ndwpusbl "...Now."
    show natsuki 1fdwbolsbl
    $ jnPause(2)
    show natsuki 1fdwunlsbl
    $ jnPause(3)
    n 1fsrunl "..."
    n 1fcsunl "..."
    n 1fcsfll "Are."
    n 1fcseml "You."
    n 4fcsanl "Freaking{w=1}{nw}" 
    extend 4fbkwrl " {i}KIDDING ME{/i}?!{w=0.75}{nw}"
    $ player_final = jn_utils.getPlayerFinal(3)
    extend 4knmwrl " [player_initial]-[player][player_final]!"
    n 4fcsanl "Uuuuuu-!"
    n 4cbkwrless "Y-{w=0.2}you completely threw me off!{w=0.75}{nw}"
    extend 2fcsful " You have no {i}idea{/i} how long it took for me to get that far!{w=0.75}{nw}"
    extend 4knmeml " I-{w=0.2}I totally {i}had{/i}{w=0.5}{nw}" 
    extend 4knmwrl " thaaat!"
    n 1kdweml "...And now I gotta do it all over again!"
    n 1kcsflesi "..."
    n 1csrem "Man...{w=1.25}{nw}"
    extend 2csrsl " and I didn't even get to take a picture or anything."
    n 2fsrbo "..."
    n 2csqbo "..."
    n 2ccsfl "..."
    n 1ccsaj "...Forget it.{w=0.75}{nw}"
    extend 1fcswrlsbl " Forget it!{w=1}{nw}"
    extend 4ftlfllsbl " I don't even care anymore."
    n 4ccsfllsbl "This was a total waste of time in the first place,{w=0.5}{nw}" 
    extend 4cslsllsbl " a-{w=0.2}anyway."
    
    show natsuki 1ccscasbl
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 2cslsl
    $ jnPause(1)
    hide black with Dissolve(1.25)

    n 2cslbo "..."
    n 2csqbo "..."
    n 2ccspo "Hmph."
    n 2fcsfl "Well,{w=0.5}{nw}"
    extend 4cnmaj " I hope you know what you're in for now,{w=0.2} [player]."
    n 5cllaj "Seeing as how you owe me big time for throwing off my groove and all."
    n 3cllsl "..."
    n 3cnmem "What?{w=0.75}{nw}"
    extend 3ccsgs " I'm being serious!{w=1}{nw}"
    extend 4ccsposbl " There's no {i}way{/i} I'm letting you off the hook {i}that{/i} easily."

    if Natsuki.isEnamored(higher=True):
        n 1ccssssbl "...Heh.{w=0.75}{nw}"
        extend 2fcsflsbl " A-{w=0.2}and besides,{w=0.2} [player]."
        extend 2ccsaj " You've seen enough cards by now."
        n 7ccsbgl "...S-{w=0.2}so don't you recognize a {i}queen{/i} when you see one?{w=0.75}{nw}"
        extend 5fsrdvl " Ehehe."
        n 3fsrfslsbl "..."
        n 3ccsajlsbr "Well?{w=0.75}{nw}"
        extend 3cllbglsbr " Get started already,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fsqsslsbr " After {i}that{/i} much of a screw up?"
        $ time_of_day = "today" if jn_is_day() else "tonight"
        n 3fcsbglsbr "Y-{w=0.2}you better {i}believe{/i} you're giving me the royal treatment [time_of_day]!"
        n 3fsqsmlsbr "Ehehe."

    else:
        n 1ccsss "...Heh.{w=0.75}{nw}"
        extend 2ccsaj " Sorry,{w=0.2} [player]."
        n 2flltr "I'm done with the cards already."
        extend 6fsqbg " But making this up to me is just the hand you've been dealt!"
        n 3fcssm "Ehehe."

    return

# Natsuki discovers a new card game she wants to try with the player!
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_blackjack_unlock",
            unlocked=True,
            conditional="persistent.jn_snap_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_blackjack_unlock:
    $ jn_globals.force_quit_enabled = False
    $ jnPause(3)
    play audio laptop_close
    $ jnPause(2)
    n "...Alright.{w=0.75} Let's try this out.{w=0.75} {i}Again{/i}."
    n "There {i}has{/i} to be some decent results this time..."
    $ jnPause(2)

    play audio keyboard
    n "Card games...{w=1.75}{nw}"
    play audio keyboard
    extend " two players..."
    n "..."
    play audio button_tap_c
    extend "Search."
    $ jnPause(3)

    n "..."
    play audio keyboard
    n "...Card games...{w=1} two players...{w=1.75}{nw}" 
    play audio keyboard
    extend " {i}easy{/i}."

    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(2)

    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(2)

    n "Oh,{w=0.2} for-!{w=0.5}{nw}"
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    extend " Search!{w=0.75} Jeez..."
    n "Why is this thing so {i}slow{/i}?{w=0.75} What's even the {i}point{/i} of updates if they always make things worse..."
    n "Ugh...{w=1} no wonder the school was literally giving these piles of junk away."
    n "Stupid budget cuts."
    $ jnPause(3)
    n "...Finally.{w=0.75} {i}Now{/i} you decide to load."
    n "Of course they just {i}had{/i} to install the worst browser they could find too." 
    n "Cut me a break."
    
    $ jnPause(1)
    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(0.75)
    n "Uuuuuuuuu-!"
    n "A-and for the last time,{w=0.2} I am {b}not{/b} looking for free spins!{w=0.75} Why do search results {i}stink{/i} so much now?!"
    n "If I {i}wanted{/i} to gamble all my savings away,{w=0.2} I'd have {i}done it{/i} already!"
    n "Sheesh..."

    $ jnPause(2)
    play audio button_tap_c
    $ jnPause(2)
    play audio keyboard
    $ jnPause(3)
    play audio button_tap_c
    $ jnPause(1)

    n "Nnnnnn-!"
    n "Come on!{w=0.75} Why does this have to be so {i}difficult{/i}?!"
    n "Just give me a game I can actually {i}play{/i} or I swear,{w=0.2} I'm gonna-!"
    n "..."
    n "...Huh."
    play audio button_tap_c
    $ jnPause(3)
    play audio button_tap_c
    $ jnPause(5)

    menu:
        "Enter...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_laptop"))
    $ jn_events.displayVisuals("1ndwpu")
    $ jn_globals.force_quit_enabled = True

    # Nat's body is obscured by the laptop, so don't need as much spritecode variation
    n 1ndwpu "..."
    n 1fdwpu "..."
    n 1fdwbo "..."
    n 1tnmboeqm "...?{w=0.75}{nw}"
    n 1unmfllesh "A-{w=0.2}ah!{w=0.75}{nw}"
    extend 2ullemlsbr " [player]!{w=0.75}{nw}"
    extend 2fcsgslsbr " W-{w=0.2}well,{w=0.2} finally!"
    n 2fcsajlsbr "You sure took your sweet time getting here.{w=0.75}{nw}"
    extend 1csqcasbl " {i}Again{/i}.{w=0.75}{nw}"
    extend 1tsqflsbl " Are you {i}trying{/i} to set some kind of lateness record or what?"
    n 1tllflsbl "Seriously...{w=1}{nw}"
    extend 1nsqem " you're gonna put Sayori's tardiness to shame at this rate."
    n 1ncsflesi "..."
    n 1nlraj "Well,{w=0.2} anyway.{w=0.75}{nw}"
    extend 7fcsaj " Lucky for you,{w=0.2} [player]."
    n 7fnmsl "There's at least {i}one{/i} thing you showed up on time for."
    n 3fsqsm "Ehehe."
    n 6fnmbg "...'Cause I've finally found a new game I wanna try!{w=0.75}{nw}"
    extend 3fchgn " I even memorized all the rules and everything!"
    n 1tsqbg "And the best thing about it?"
    n 6fnmbg "We don't even {i}need{/i} anything new to play it!"
    n 7fcscs "Yep!{w=0.75}{nw}"
    extend 7flrbg " No rooting around in that stinky old closet again for me today.\n{w=0.75}{nw}"
    extend 3fcssmesm " I got everything I need right here!"
    n 1fcsss "Heh.{w=0.75}{nw}"
    extend 1tsqsm " And thanks to you?{w=0.75}{nw}"
    extend 1fsqbg " That includes a second player!"
    n 1fchsm "..."
    n 1tsqpu "What?"
    n 7unmaj "Oh,{w=0.2} right.{w=0.75}{nw}"
    extend 7nnmss " You're probably wondering what all the fuss is about all of a sudden,{w=0.5}{nw}"
    extend 7nlrss " huh."
    n 7ulraj "So...{w=1}{nw}"
    
    if persistent._jn_snap_player_wins > 0 or persistent._jn_snap_player_wins > 0:
        extend 7nllaj " I know we've played a bunch of Snap before,{w=0.2} obviously.{w=0.75}{nw}"
        extend 3unmfl " And don't get me wrong -{w=0.5}{nw}"
        extend 3clrflsbl " I'm not saying I was getting {i}bored{/i} of it,{w=0.2} exactly."
        n 1nsraj "But...{w=1}{nw}"
        extend 1clrfl " it always felt like it was missing something.{w=0.75}{nw}"
        extend 7tnmbo " You know?"

    else:
        extend 7tlrbo " I'm pretty sure I mentioned Snap before.{w=0.75}{nw}"
        extend 7tnmfl " That card game where you gotta call out matching cards to win?"
        n 3nllfl "...Even if we never actually ended up {i}playing{/i} it,{w=0.5}{nw}" 
        extend 3nslsl " for whatever reason."
        n 3nllpu "But like...{w=1}{nw}"
        extend 7nsqcasbr " I guess it's fine if all you actually care about in a game is reaction times."

    n 1fllaj "I wouldn't exactly say it's a {i}skilled{/i} game or anything like that."
    n 1ccsss "So it's not like it takes some kind of mastermind to figure out what's missing here."
    n 3fsqsm "..."
    n 3tsqss "What?{w=0.75}{nw}"
    extend 3fnmsm " Wasn't it obvious already,{w=0.5}{nw}"  
    extend 3fsqsm " [player]?"
    n 6fcsbg "...Some actual strategy!{w=0.75}{nw}"
    extend 6fchgn " Duh!"
    n 1fnmbg "And what better way to make sure you're actually using your noggin than a game where you've gotta think for once about your moves?"
    n 7fcsbg "You guessed it!{w=0.75}{nw}"
    extend 1fsqbg " I'm talking about..."

    show natsuki 1fcssm
    $ jnPause(1)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
    play audio smack
    $ jnPause(1.25)

    n 3fchbs "...Blackjack!"
    n 3fchsm "..."
    n 3fcssmeme "Ehehe."
    n 7ullss "I know,{w=0.2} I know.{w=0.75}{nw}"
    extend 7ccsbgedz " Genius,{w=0.2} right?{w=0.75}{nw}"
    extend 6ccssm " Betcha' wish {i}you'd{/i} thought of it before,{w=0.2} huh?"
    n 7ulraj "I'd actually heard about it a while ago,{w=0.5}{nw}" 
    extend 7clrsssbl " but I never thought it was something that could actually be fun to play.{w=0.75}{nw}"
    extend 3cslsssbl " Especially with only two players."
    n 3tnmbo "So when I was looking for something else to do with the card pack,{w=0.2} I guess it just kinda came to mind."
    n 3tllss "Besides.{w=0.75}{nw}"
    extend 1cslsssbr " I {i}did{/i} say I didn't know a whole lot of card games before.{w=0.75}{nw}"
    extend 1ccsposbr " Studying up on another one was clearly way overdue."
    n 7unmaj "Seriously though -{w=0.5}{nw}"
    extend 3fchbg " it's perfect!{w=0.75}{nw}"
    extend 3fspbg " And it's {i}super{/i} easy to pick up too!"
    n 3ccsss "Trust me,{w=0.2} [player].{w=0.75}{nw}"
    extend 7tsqss " Give it a couple rounds?"
    n 7tsrss "Well.{w=0.75}{nw}"
    extend 6ccssmesm " You'll still be losing,{w=0.2} of course.{w=0.75}{nw}"
    extend 3fchgnelg " But at least you'll be having tons of fun while you do!"
    n 1csqsm "..."
    n 1csqbg "...Well?{w=0.75}{nw}"
    extend 1unmbg " What do you think about it,{w=0.2} [player]?{w=0.75}{nw}"
    extend 3fcsbg " Don't lie!"

    $ persistent._jn_blackjack_unlocked = True
    show natsuki option_wait_smug
    menu:
        n "I can tell you're just {i}itching{/i} to get started,{w=0.2} right?"

        "You bet I am!":
            n 1fcssm "Heh.{w=0.75}{nw}"
            extend 7fcsbg " Just as I thought.{w=0.75}{nw}"
            extend 3fchgn " I can read you like a book!"
            n 3unmaj "Oh -{w=0.5}{nw}"
            extend 3cdwss " let me just pack this thing up real quick first."

            show natsuki 1ccssmeme
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(1)
            play audio laptop_close
            $ jnPause(2)
            play audio drawer
            $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
            show natsuki 1cllsmeme
            $ jnPause(1)
            hide black with Dissolve(1)

            jump blackjack_explanation

        "Not right now,{w=0.2} [n_name].":
            n 1ccssl "Heh.{w=0.75}{nw}"
            extend 3clrfl " Say no more,{w=0.2} [player].{w=0.75}{nw}"
            extend 3clrsl " Say no more."
            n 3ccstr "I {i}totally{/i} get it."
            n 1csqbo "..."
            n 3fcsbg "...Totally get that you'll just come crawling back later instead when you finally get bored,{w=0.2} that is."
            n 3fsqsm "Ehehe."
            n 7ulrfl "Nah,{w=0.2} I guess that's fine.{w=0.75}{nw}"
            extend 3cnmbo " As if I'm gonna force you to play or anything like that.{w=0.75}{nw}"
            extend 3csrfll " I'm not {i}that{/i} entitled."
            n 1ullsl "But hey."
            extend 6nchgn " Not like there's any shortage of time for you to start learning and losing later,{w=0.2} right?"
            
            show natsuki 1ccssmeme
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(2)
            play audio laptop_close
            $ jnPause(2)
            play audio drawer
            $ Natsuki.clearDesk()
            show natsuki 1cllsmeme
            $ jnPause(2)
            hide black with Dissolve(1)

            n 2cllss "Well,{w=0.2} now that's finally out of the way..."
            $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
            n 7fchbgl "What's happening,{w=0.2} [chosen_descriptor]?"

    return

# HOLIDAYS

# Used to lead up to a holiday, but only if already in-game and the day changes
label holiday_prelude:
    n 1tllbo "..."
    n 1ullpu "...You know,{w=0.75}{nw}"
    extend 3fsrcaesp " it almost feels like I'm missing something."
    n 3fsrpu "...{w=1}{nw}"
    n 1uskemlesh "...!{w=0.5}{nw}"
    n 1fbkwrl "J-{w=0.3}just a second!{w=1}{nw}"
    extend 2flrpol " I-{w=0.2}I'll be right back!{w=1}{nw}"

    hide screen hkb_overlay
    show black zorder JN_BLACK_ZORDER
    stop music
    hide prop
    hide deco
    play audio switch_flip
    $ jnPause(5)

    return

# Used to handle multiple events in a single day by cleaning/setting up inbetween events
label holiday_interlude:
    n 1fllbo "..."
    n 1tllpu "You know..."
    n 4tnmpueqm "I feel like I'm forgetting something else."
    n 2fsrpu "...{w=1}{nw}"
    n 1uskemlesh "...!{w=0.5}{nw}"
    n 1fbkwrl "J-{w=0.3}just a second!{w=1}{nw}"
    extend 2flrpol " Don't go anywhere!{w=1}{nw}"

    hide screen hkb_overlay
    show black zorder JN_BLACK_ZORDER
    stop music
    hide prop
    hide deco
    play audio switch_flip
    $ jnPause(5)

    return

label holiday_new_years_day:
    python:
        import copy

        # Give Natsuki a new year headband, using whatever she's currently wearing as a base
        jn_outfits.getWearable("jn_headgear_new_year_headband").unlock()
        new_years_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        new_years_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_new_year_headband")
        new_years_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(new_years_hat_outfit)

        jn_events.getHoliday("holiday_new_years_day").run()

    n 1uchbs "FIVE!"
    n 1uchbg "FOUR!"
    n 1uchbs "THREE!"
    n 1uchbg "TWO!"
    n 1unmajesu "ON-"
    n 1fskemesh "...!"
    n 3fcsanless "Uuuuuuuu-!"
    n 3fcsemless "Are you{w=0.5}{nw}"
    extend 3fcswrl " {cps=\10}freaking{/cps}{w=0.5}{nw}"
    extend 1fbkwrlean " {i}kidding{/i} me?!"
    n 1kskem "I missed it?!{w=0.5}{nw}"
    extend 1kskwr " {b}AGAIN?!{/b}"
    n 3fcsfu "Ugh!{w=0.5}{nw}"
    n 1fbkwrlean "How do I {i}always{/i} miss something that only happens once a year?!{w=1.25}{nw}"
    extend 4kslfreso " I can't {i}believe{/i} I was so off with the timing!"

    if jn_is_day():
        n 4tnmpu "...Really off,{w=0.2} actually.{w=0.5} Now that I look at the time.{w=1}{nw}"
        extend 4nsrpo " Almost impressively."
        n 1kcsemedr "Jeez..."
        n 3fslajl "You could have at least woken me up sooner,{w=0.5}{nw}"
        extend 3fsqpol " you jerk."
        n 1nslpu "But...{w=1}{nw}"
        extend 1tsqsl " I suppose I can't give you too much of a hard time for it,{w=0.2} [player]."
        n 1fcsbg " Your hangover can do that for me.{w=0.5}{nw}"
        extend 1fcsajsbr " Anyway!"

    else:
        n 1kcsemedr "Man..."
        n 2fsrpu "Now that's gonna bug me from the rest of the day..."
        n 2fslsrl "Way to start the new year,{w=0.2} huh?"
        n 1fcspoesi "..."
        n 1fcsajsbr "Well,{w=0.2} whatever!"

    n 1fcsemlsbr "Missing the new year?{w=0.5}{nw}"
    extend 2flrbgsbl " M-{w=0.3}merely a minor setback!"
    n 1fcsajsbr "Besides,{w=0.5}{nw}"
    extend 3fllbgsbr " it's not like we're gonna run out of years to count!{w=1}{nw}"
    extend 3nsrsssbr " Probably."
    n 1nllpusbr "It's...{w=1}{nw}"
    extend 1nsqsssbl " kinda getting harder to tell these days, huh?"
    n 1kllbosbl "..."

    n 1unmsl "In all seriousness though,{w=0.2} [player]?"
    n 3nslss "I know I've already kinda trashed my clean start..."
    n 4fnmbol "But that doesn't mean you're off the hook."
    n 1fcsss "Yeah,{w=0.2} yeah.{w=0.5} I know."
    n 1fslss "I'm not gonna give you a whole lecture on fresh starts,{w=1}{nw}"
    extend 1tlrbo " hitting the gym{w=0.5}{nw}"
    extend 4tnmss " or anything like that."

    if jn_is_day():
        n 1fchgn "{i}Something{/i} tells me you wouldn't appreciate the extra headache!"

    n 1tllaj "But...{w=1}{nw}"
    extend 1tnmsl " there actually is one thing I wanna say."
    n 1ncssl "..."
    n 1ucspu "Just..."

    if Natsuki.isAffectionate(higher=True):
        extend 4fnmpul " promise me something,{w=0.2} [player].{w=0.5}{nw}"
        extend 4knmbol " Please?"

    else:
        extend 1fnmpu " do one thing for me.{w=0.5}{nw}"
        extend 4knmbol " Please?"

    n 2kslbol "..."
    n 2kplpulsbl "Reach out to someone today.{w=0.5}{nw}"

    if Natsuki.isEnamored(higher=True):
        extend 1fcsajfesssbl " A-{w=0.2}and I don't mean me.{w=0.5}{nw}"
        extend 1fslssfesssbl " This time."

    else:
        extend 1fcsajfesssbl " A-{w=0.2}and I don't mean me.{w=0.5}{nw}"

    n 1fcsun "Please...{w=1}{nw}"
    extend 1fcspul " hear me out,{w=0.2} alright?"
    n 2kllun "Not everyone has the luxury of friends or family.{w=1}{nw}"
    extend 4ksqpu " And trust me when I say not everyone looks forward to a new year..."
    n 1knmsl "But the right message really {i}can{/i} make all the difference."
    n 2klrsl "...And you never know if you'll always have the chance to send it."
    n 1ncspu "Some family you don't get along with,{w=1}{nw}"
    extend 1nllsr " a friend you've drifted away from..."
    n 4knmpu "They won't...{w=0.5}{nw}"
    extend 4kllpu " be there{w=0.5}{nw}"
    extend 4fslunl " forever."
    n 2kslunltsb "...Just like my friends,{w=0.3} [player]."
    n 1fcsajftsa "A-{w=0.2}and remembering the people around you is just as important as any stupid resolution."
    n 1fnmsrl "So I don't care {i}how{/i} you do it.{w=1}{nw}"
    extend 1fllpul " Text message,{w=0.35} phone call,{w=0.35} whatever."
    n 1fcspul "But please...{w=0.5}{nw}"
    extend 1kllsrl " do something,{w=0.2} alright?{w=1}{nw}"
    extend 4fnmbol " For yourself just as much as them."

    n 4nlrunl "..."
    n 1ncsajl "Oh,{w=0.5}{nw}"
    extend 2nsleml " jeez."
    $ current_year = datetime.date.today().year
    n 3fllunlsbr "We're barely into [current_year] and I'm already making things all serious..."
    n 1fslsslsbr "Heh.{w=0.5}{nw}"
    extend 1tsqpu " So much for a lighthearted celebration,{w=0.2} right?"
    n 4tnmpu "But [player]?"
    n 2kllsl "..."

    if Natsuki.isEnamored(higher=True):
        n 4knmsll "...Thank you."
        n 1kllssl "For this year,{w=0.2} I mean."
        n 2fcsemlesssbl "I-{w=0.2}I know I don't show it a lot!{w=0.5}{nw}"
        extend 2klrpul " But...{w=0.5}{nw}"
        extend 2knmpul " just taking time out of your day to visit me,{w=0.75}{nw}"
        extend 2kllssl " listening to all my nonsense,{w=0.75}{nw}"
        extend 2fsldvl " dealing with my crap sometimes..."
        n 1knmbol "...It matters."
        n 1kllssl "It really does,{w=0.2} heh.{w=1.25}{nw}"
        extend 4kllbofsbr " A lot."
        n 1kllajf "And...{w=1}{nw}"
        extend 4knmpufsbr " one last thing?"
        n 1fcsunfsbr "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5)

        if Natsuki.isLove(higher=True):
            show natsuki 1fsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
            play audio kiss
            $ jnPause(1.5)
            hide black with Dissolve(1.25)
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 4kwmsmf "...Happy new year,{w=0.2} [chosen_endearment].{w=1.25}{nw}"
            extend 4kllssfess " Ehehe."

        else:
            show natsuki 1nsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
            $ jnPause(1.5)
            hide black with Dissolve(1.25)
            $ chosen_tease = jn_utils.getRandomTease()
            n 4klrssf "Heh."
            n 1fchsmfess "...Happy new year,{w=0.2} [chosen_tease]."

    else:
        n 1knmsll "...Thanks.{w=0.75}{nw}"
        extend 3fcsemlsbl " F-{w=0.2}for this year,{w=0.2} I mean."
        n 1fslbolesssbl "I...{w=0.5}{nw}"
        extend 4knmboless " really appreciate that you've spent so much time with me already."
        n 1kllssless "Even if I {i}am{/i} just a grouchy girl stuck in some{w=0.5}{nw}"
        extend 2fsrssl " magical space classroom."
        n 1nlrunl "..."
        n 1kbkwrl "Seriously!{w=0.2} I do!"
        n 3fllanlsbl "It's..."
        n 1kcsemlesisbl "..."
        n 2ksrpol "I-{w=0.3}it just means a lot to me,{w=0.2} okay?"
        n 1ksrpul "And...{w=0.75}{nw}"
        extend 1knmssl " one last thing?"
        n 1ncsajl "..."
        n 1fcsunl "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        show natsuki 1fsldvlsbl at jn_center zorder JN_NATSUKI_ZORDER
        play audio clothing_ruffle
        $ jnPause(3.5)
        hide black with Dissolve(1.25)

        n 4fsqdvlesssbr "...H-{w=0.2}happy new year,{w=0.2} dummy."
        n 4nslsslesssbl "A-{w=0.2}and if anyone asks,{w=0.3} that never happened.{w=1}{nw}"
        extend 4fsldvlesssbl " Ehehe..."

    $ jn_events.getHoliday("holiday_new_years_day").complete()

    return

label holiday_valentines_day:
    $ valentine_outfit = jn_outfits.getOutfit("jn_ruffle_neck_sweater_outfit")
    $ valentine_outfit.unlock()
    $ jn_outfits.saveTemporaryOutfit(valentine_outfit)
    $ player_has_gifted_clothes = len(jn_outfits.JNWearable.filterWearables(jn_outfits.getAllWearables(), True, False)) > 0
    $ jn_events.getHoliday("holiday_valentines_day").run()

    n 1uskfllsbr "...!{w=0.75}{nw}"
    n 1uskwrlsbr "A-{w=0.2}ah!{w=0.75}{nw}"
    extend 1flrbglsbr " [player]!"
    n 1fcsajlsbl "Well,{w=1}{nw}"
    extend 1fcsgslsbl " didn't you take your sweet time showing up?{w=0.75}{nw}"
    extend 1fllemlsbl " Yeesh!"
    n 1fcsemlsbl "I mean,{w=0.75}{nw}"
    extend 1fcsgsl " come on!{w=1}{nw}"
    extend 1fnmpol " Did you totally forget what day it was or something?{w=1}{nw}"
    extend 1fsqpol " Do I {i}seriously{/i} have to remind you?"
    n 1fcswrl "I'm not your personal assistant,{w=0.2} you know!"
    n 1fsqpol "..."
    n 1fsqpul "...Huh?{w=0.75}{nw}"
    extend 1tsqfll " What?"
    n 1nlrfllsbl "What's that look for,{w=0.5}{nw}" 
    extend 1knmfllsbl " all of a sudden?"

    if Natsuki.isLove(higher=True):
        n 1knmbolsbl "..."
        n 1udweml "O-{w=0.2}oh!{w=0.75}{nw}"
        extend 1fcseml " Right.{w=1}{nw}"
        extend 1nsrbolsbl " T-{w=0.2}the chocolates."
        n 1ksrbolsbl "..."
        n 1ksqfllsbl "...Come on,{w=0.2} [player].{w=1}{nw}"
        extend 1knmfllsbl " Isn't it obvious?{w=1}{nw}"
        extend 1klrfllsbl " Why else do you think I'd {i}magically{/i} have a box of them ready?"
        n 1ksrslfsbl "...T-{w=0.2}they're yours."
        n 1fcsajlsbl "I-{w=0.2}I know I can't exactly give you them..."
        n 1nslpulsbl "Well.{w=1}{nw}"
        extend 1nslsslsbr " Unless you count smearing them all over the screen or something.{w=1}{nw}"
        extend 1kslbolsbr " But..."
        n 1kslunlsbr "..."
        n 1fcsunlsbr "I had to do something!{w=0.75}{nw}"
        extend 1flrfllsbr " A-{w=0.2}and not just because we're...{w=1.25}{nw}"
        extend 1ksrbof " y-{w=0.2}you know."
        n 1kcsfll "It's just..."
        n 1kslsll "..."
        n 1kslpul "You've...{w=0.75}{nw}"
        extend 1kllbol " really done so much for me already.{w=1}{nw}"
        extend 1knmbol " You know?"
        n 1knmfll "...And for a super long time now too."
        n 1ncsajl "Yeah,{w=0.2} you brought me back.{w=1.25}{nw}"
        extend 1nsrfsl " Obviously.{w=1}{nw}"
        extend 1knmbol " But it's all the small things I {i}really{/i} care about,{w=0.2} [player]."
        n 1kllbol "It's how many times you've come to visit me."
        n 1kllsslsbr "It's how you always let me talk your ears off about random stuff."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1klrajlsbr "It's all the new stuff you've just...{w=1}{nw}"
            extend 1klrsllsbr " given me.{w=1.25}{nw}"
            extend 1ksrpol " Even if I never asked for it."

        n 1kcspulesi "..."
        n 1ksqsll "...Look.{w=1}{nw}"
        extend 1klrsll " I've never been good at this kind of stuff.{w=1.25}{nw}"
        extend 1fcsunlsbl " I-{w=0.2}I always struggle with it."
        n 1fcspulsbl "Especially when it's all just...{w=0.75}{nw}" 
        extend 1ksrsllsbl " so new to me.{w=0.75}{nw}"
        extend 1kllsllsbl " Having someone who..."
        n 1kllsrlsbl "..."
        n 1kllfllsbl "...Who really cares about me."
        n 1knmpulsbl "S-{w=0.2}someone who{w=0.75}{nw}" 
        extend 1ksrpufsbr " loves{w=0.75}{nw}" 
        extend 1ksrbofsbr " me."
        n 1kcsajlsbr "But what I'm trying to say is..."
        n 1ksrbolsbr "..."
        n 1knmbolsbr "...It's appreciated,{w=0.2} [player].{w=0.75}{nw}"
        extend 1knmfllsbr " Really.{w=1}{nw}"
        extend 1kllbolsbl " A whole lot more than you think."
        n 1knmbofsbl "And...{w=0.5} I really wanted you to know that."
        n 1fcsemfsbl "Even if it means I gotta feel all awkward in the process."
        extend 1ksrbof " That's what {i}really{/i} matters."
        n 1ksrajf "So...{w=1.25}{nw}"
        extend 1ksrssf " yeah."
        n 1ksrfsf "..."
        n 1knmfsf "...And [player]?"
        n 1kslcafsbr "..."

        show natsuki 1fcscafsbr
        play audio chair_out
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(3)

        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle

        $ valentine_special_outfit = jn_outfits.getOutfit("jn_heart_sweater_outfit")
        $ valentine_special_outfit.unlock()
        $ jn_outfits.saveTemporaryOutfit(valentine_special_outfit)
        show natsuki 1nsrdvfess at jn_center

        $ jnPause(5)
        play audio chair_in
        $ jnPause(2)
        hide black with Dissolve(2)
        $ jnPause(1)

        n 1fsrssf "S-{w=0.2}surprise."
        show prop f14_heart give
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1fchbgfesssbl "H-{w=0.2}happy Valentine's day,{w=0.2} [chosen_endearment].{w=1.25}{nw}"
        extend 1fchsmfesssbl " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1uskwrlesh "A-{w=0.2}ah!{w=0.5}{nw}"
        extend 1udwfll " T-{w=0.2}this thing?"
        n 1fcsgslsbr "I mean,{w=0.2} it's obviously..."
        n 1fslunlsbr "..."
        n 1fcsemlsbr "I-{w=0.2}it's...!"
        n 1fcsanlsbr "Uuuuuuuu...!"
        n 1fbkwrlsbr "C-{w=0.2}come on,{w=0.2} [player]!{w=0.75}{nw}"
        extend 1fnmemlsbl " Can't you read the room by now?{w=1}{nw}"
        extend 1klrfllsbl " Who {i}else{/i} do you see around here?"
        n 1flrfllsbl "Jeez...{w=0.75}{nw}"
        extend 1ksremlsbl " as if this wasn't awkward enough..."
        n 1fcsunlsbl "..."
        n 1ncspulesi "..."
        n 1flrbol "...I made them for you,{w=0.75}{nw}"
        extend 1fnmbol " okay?{w=1}{nw}"
        extend 1fslcalsbl " You wouldn't {i}believe{/i} how hard it was to find all this stuff."
        n 1fcsemfsbl "I-{w=0.2}I know we're not like {i}that{/i}!{w=0.75}{nw}"
        extend 1flrslf " And I know I can't exactly just hand them over.{w=1}{nw}"
        extend 1klrbof " But that's not the point at all."
        n 1klrfll "It's just that..."
        n 1ksrsll "..."
        n 1ksrfll "Not doing {i}something{/i}...{w=0.75}{nw}"
        extend 1fllbol " it just wouldn't have felt right.{w=1}{nw}"
        extend 1kllbol " N-{w=0.2}not after everything you've done for me."
        n 1fcscal "...A-{w=0.2}and I don't just mean bringing me back,{w=0.2} [player]."
        n 1nlrsll "Hearing out all my random thoughts.{w=1}{nw}"
        extend 1ksrbol " Bothering to come visit me all the time."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1fsrsslsbl "E-{w=0.2}even the dumb surprise gifts you {i}insist{/i} on giving me."

        n 1kllajl "It's all..."
        n 1kslunl "..."
        n 1ksqbolsbr "...It's appreciated.{w=1}{nw}"
        extend 1knmbolsbr " Okay?{w=1.25}{nw}"
        extend 1klrbolsbr " Really."
        n 1ksrflf "...And I wanted to make sure you know that too."
        n 1ksrslf "..."
        n 1ksrajl "So...{w=1}{nw}"
        extend 1nsrssl " yeah.{w=1.25}{nw}"
        extend 1nsrcal " Here."
        show prop f14_heart give
        $ jnPause(3)
        n 1ksrcal "..."
        n 1nnmajl "...And [player]?"
        n 1fslunlsbl "..."

        show prop f14_heart hold
        show natsuki 1fcsunfsbl
        play audio chair_out
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)

        play audio clothing_ruffle
        $ jnPause(3)
        show natsuki 1nsrbofsbr at jn_center

        $ jnPause(3)
        play audio chair_in
        $ jnPause(1)
        hide black with Dissolve(2)
        $ jnPause(2)

        show prop f14_heart give
        n 1fsrfsfsbr "H-{w=0.2}happy Valentine's day."

    else:
        n 1uskflleshsbr "...!{w=0.5}{nw}"
        n 1fcsgslsbr "T-{w=0.2}this?!{w=0.75}{nw}"
        extend 1flrgslsbr " It's..."
        n 1fcsgslsbr "I-{w=0.2}it's...!"
        n 1fcsanlsbr "Nnnnnnnn...!"
        n 1fbkwrlsbr "W-{w=0.2}what do you {i}think{/i} it's for?!{w=0.75}{nw}"
        extend 1flrwrlsbr " I don't {i}really{/i} have to spell it all out,{w=0.2} do I?{w=0.75}{nw}"
        extend 1fcsemlsbr " Jeez!"
        n 1fllemlsbr "I-{w=0.2}It's just...!"
        n 1fslemlsbr "..."
        n 1kslsllsbr "..."
        n 1fcsemlsbr "...Okay,{w=0.75}{nw}"
        extend 1flrbolsbl " look.{w=1}{nw}"
        extend 1fsrsrlsbl " I'm not dumb."
        n 1fcsgslsbl "I know we're not like...{w=0.75}{nw}"
        extend 1fslunfsbl " that.{w=1.5}{nw}"
        extend 1kslbolsbl " But..."
        n 1kllbolsbl "..."
        n 1fcsbolsbr "It just didn't feel right not doing {i}something{/i}.{w=1}{nw}"
        extend 1fnmbolsbl " Think about it,{w=0.2} [player]."
        n 1fcsemfsbl "Y-{w=0.2}you don't have to be all lovey-dovey with someone to show them they matter!{w=0.75}{nw}"
        extend 1fsrcalsbl " Despite what all the corny adverts insist."
        n 1fsqcalsbl "...And yes [player],{w=0.2} before you say anything.{w=0.75}{nw}"
        extend 1fcscalsbl " Y-{w=0.2}you do matter."
        n 1flrcalsbl "B-{w=0.2}bringing me back,{w=0.75}{nw}"
        extend 1nllbol " listening to all my dumb thoughts..."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1kslbolsbr "All the new stuff you've given me."

        n 1ncsemlsbr "E-{w=0.2}even just...{w=1}{nw}"
        extend 1kslsllsbr " showing up."
        n 1ncsajlsbr "It's all..."
        n 1klrbolsbr "..."
        n 1kcsemlesisbr "..."
        n 1ksqcal "...It's appreciated,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fcseml " A-{w=0.2}and I had to make sure you knew that."
        n 1fcscal "W-{w=0.2}whether you wanted to or not."
        n 1nslajl "So..."
        n 1fslslf "..."
        show prop f14_heart give
        n 1fcsslfsbr "...Here."
        n 1fcsajfsbr "Just pretend you're taking it or something,{w=0.75}{nw}"
        extend 1flrcafsbr " I guess.{w=1.25}{nw}"
        extend 1fsrpolsbr " Before I change my mind."
        n 1nsrpolsbr "..."
        n 1nsrpulsbr "And..."
        n 1fcssslsbl "H...{w=0.75}{nw}"
        extend 1fcspolsbl "happy Valentine's day,{w=0.2} [player]."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio gift_close
    $ jnPause(3)
    play audio drawer
    hide prop f14_heart
    $ jnPause(3)

    if Natsuki.isLove(higher=True):
        play audio kiss
        $ jnPause(2.5)

    hide black with Dissolve(2)
    $ jnPause(2)

    $ jn_events.getHoliday("holiday_valentines_day").complete()

    return

label holiday_easter:
    python:
        persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)
        jn_atmosphere.showSky(jn_atmosphere.WEATHER_CHERRY_BLOSSOM)

        chick_outfit = jn_outfits.getOutfit("jn_chick_outfit")
        chick_outfit.unlock()
        jn_outfits.saveTemporaryOutfit(chick_outfit)

        jn_events.getHoliday("holiday_easter").run()

    n 1unmflleex "...!{w=1.25}{nw}"
    n 4unmbgl "[player]!{w=0.5}{nw}"
    extend 4uchbgl " [player]!{w=0.3} [player]!"
    n 2fcsfll "I-{w=0.2}I mean,{w=0.5}{nw}"
    extend 2fcsgslsbr " it's about time you got your butt in here!{w=1}{nw}"

    if jn_is_day():
        extend 4fcsgssbl " Do you even {i}know{/i} what day it is today?{w=0.75}{nw}"
        extend 2fcsposbl " Sheesh!"
        
    else:
        extend 4fsqgssbl " Do you even {i}know{/i} what day it is today?"
        n 2fsrslsbl "I guess not,{w=0.75}{nw}"
        extend 2fcspoesisbl " considering the time you got here."

    n 2fsqca "I don't {i}seriously{/i} have to remind you,{w=0.2} do I?"
    n 1fcstresi "..."
    n 4fcsaj "It's..."
    n 3fchbg "Easter,{w=0.75}{nw}"
    extend 3uchgn " duh!{w=1}{nw}"
    extend 4fsqbg " What else was it gonna be,{w=0.2} [player]?"
    n 1fcsbg "After all.{w=0.75}{nw}"
    extend 3fsqsm " You {i}do{/i} know what Easter means,{w=0.2} right?"
    n 3tsqsm "..."
    n 1fcssm "Heh."
    n 4fcsbg "Yeah,{w=0.2} you do.{w=0.75}{nw}"
    extend 1fcssmesm " I basically have a sixth sense for this kind of thing,{w=0.2} after all."
    n 1fcsss "It means..." 
    n 3fchbs "Cherry blossom season,{w=0.75}{nw}"
    extend 3uchgn " obviously!"
    n 4tnmbo "..."
    n 4tnmfl "What?{w=0.75}{nw}"
    extend 2fsrpo " I'm being serious,{w=0.2} [player]!{w=1}{nw}"
    extend 2fcsaj " Why wouldn't I be?"
    n 1fcsfl "It's...{w=1.25}{nw}"
    extend 3uchgnledz " {b}AWESOME{/b}!"
    n 4ullbg "Seeing all the cherry blossom trees just {i}explode{/i} into life like that?{w=0.75}{nw}"
    extend 4fspgs " It's {i}super{/i} pretty!"
    n 2fcsbs "What else can you think of that floods the place with color that well,{w=0.2} huh?"
    n 1ulrss "Plus with how the blossoms travel all the way up from south to north..."
    n 3uchgn "It's pretty much a rolling announcement for the summer!{w=0.2} I love it!"
    
    $ cherry_blossom_outfit = jn_outfits.getOutfit("jn_cherry_blossom_outfit")
    if not cherry_blossom_outfit.unlocked:
        $ cherry_blossom_outfit.unlock()
        n 4fslpu "I'm sure I had a super stylish dress themed around it somewhere..."

    n 3unmaj "But personally?{w=0.75}{nw}"
    extend 3fcsca " I like to think it's my reward for making it through all the gross winter months too."
    n 1fslem "Putting up with all the crappy weather,{w=0.2} getting up when it's dark -{w=0.5}{nw}"
    extend 1fsqsl " getting back when it's dark."
    n 2fcswr "Not to mention being basically stuck indoors all the time!"
    n 4ulrfl "So after all that,{w=0.75}{nw}"
    extend 4nsrss " seeing everywhere start looking like something out of a fairy tale,{w=0.5}{nw}"
    extend 2tnmbo " even if it's just for a couple of weeks?{w=0.75}{nw}"
    extend 2tllss " Well..."
    n 1fchsm "It {i}almost{/i} makes dealing with winter worth it!"
    n 4fsqss "...{i}Almost{/i}.{w=1}{nw}"
    extend 4fcssm " Ehehe."

    $ easter_poem = jn_poems.getPoem("jn_easter_sakura_in_bloom")
    if not easter_poem.unlocked:
        $ easter_poem.unlock()
        n 1fcsbg "In fact..."

        show natsuki 1fcssmeme
        play audio page_turn
        show prop poetry_attempt zorder JN_PROP_ZORDER at JN_TRANSFORM_FADE_IN
        $ jnPause(2)

        n 1fchbgeme "Ta-{w=0.2}da!{w=0.75}{nw}"
        extend 4uchgn " I even wrote a poem about it!{w=0.75}{nw}"
        extend 4fcsbg " How could I {i}not{/i}?"
        n 2flrfl "What kind of poet would just throw away such easy inspiration?"
        n 2fcsaj "I mean...{w=1}{nw}"
        extend 2fcssm " it practically wrote itself!"
        n 1fsqsm "..."
        n 4fsqss "Oh?{w=0.75}{nw}"
        extend 4fnmss " What's that,{w=0.2} [player]?"
        n 2fcsbgsbl "You're just {i}dying{/i} to see it?{w=0.75}{nw}"
        extend 2fnmbgsbl " Is that it?"
        n 2fsqcssbl "..."
        n 2fcsbglsbl "W-{w=0.2}well,{w=0.75}{nw}"
        extend 2fcssmlsbl " I don't see why not.{w=1.25}{nw}"
        extend 4fcsajlsbr " After all..."
        n 4fcssmlsbr "{i}Someone's{/i} gotta remind you what {i}real{/i} literature looks like from time to time!"
        show natsuki 1fsrsmlsbr

        call show_poem(easter_poem)
        show natsuki 1fsrbolsbr

        n 2fllsssbr "Well?{w=0.75}{nw}"
        extend 2fcssmsbr " I told you it basically wrote itself!"
        n 4fsqsm "I don't mean to brag,{w=0.2} [player].{w=1}{nw}"
        extend 4tnmaj " But unlike the trees?"
        n 2fcssmesm "My writing is {i}always{/i} in full bloom.{w=0.75}{nw}"
        extend 2fchsm " Ahaha."

        show natsuki 4fcssm
        play audio page_turn
        hide prop at JN_TRANSFORM_FADE_OUT
        $ jnPause(2)

    n 4tslbo "..."
    n 4unmaj "Oh,{w=0.2} right.{w=1}{nw}"
    extend 2ulraj " And all the chocolate stuff is cool too,{w=0.75}{nw}"
    extend 2tlrbo " I guess."
    n 1fsqsm "Ehehe."
    n 3fcsbs "Don't tell me {i}that's{/i} the part of Easter you were {i}really{/i} interested in,{w=0.2} [player]."
    n 3fcsbg "I can read you like a book!"
    n 3nlraj "Though...{w=1.25}{nw}"
    extend 1tnmbo " in all seriousness,{w=0.2} [player]?{w=0.75}{nw}"
    n 2ullfl "We never really covered that a whole lot in school,{w=0.2} to be honest.{w=0.5}{nw}"
    extend 2tnmsl " Easter."
    n 4fsran "Not like that stopped all the stupid adverts {i}trying{/i} to cover it for us."
    n 1unmca "But at least I get what it's supposed to represent.{w=1}{nw}"
    extend 2ullaj " Rebirth,{w=0.2} starting over -{w=0.75}{nw}"
    extend 2fcssm " that kind of thing."
    n 4fcsbg "Surpised,{w=0.2} [player]?{w=0.75}{nw}"
    extend 3fsqss " Where {i}else{/i} did you think I got the idea for the dress?"
    n 3fsrss "I don't know a whole lot about Easter..."
    n 3fchgnl "But it doesn't take a genius to know chicks are cuuuute!{w=0.75}{nw}"
    extend 4uchgnl " I love the little yellow puffballs!"
    n 1ncsssl "Man..."
    n 4fcstrl "I have {w=0.2}{i}got{/i}{w=0.2} to get some plushies or something..."
    n 4nslcalsbr "..."
    n 2fcstrlsbr "Well,{w=0.2} a-{w=0.2}anyway."

    if Natsuki.isEnamored(higher=True):
        n 2ulraj "Easter might be all about fresh starts,{w=0.75}{nw}"
        extend 2nlrpu " but...{w=1}{nw}" 
        extend 4tnmbo " honestly?"
        n 4nllssl "...Thanks to you?"
        n 1kllbol "..."
        n 1ncsssl "Heh."

        if Natsuki.isLove(higher=True):
            n 1ksrssl "I think I've already {i}had{/i} the best I could have gotten."
            n 4ksrbolsbl "..."

            show natsuki 4fcsbolsbl
            play audio chair_out
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(3)
            play audio kiss
            show natsuki 4nslfsl at jn_center
            $ jnPause(3)
            play audio chair_in
            $ jnPause(2)
            hide black with Dissolve(2)

            n 4nsldvl "...And I guess we ended up {i}blossoming{/i} too,{w=0.2} huh?{w=1.25}{nw}"
            extend 4fchsslsbl " E-{w=0.2}ehehe..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "H-{w=0.2}happy Easter,{w=0.2} [chosen_tease]!"

        else:
            n 3ksrssl "I think I've already had the best I could have gotten.{w=0.75}{nw}"
            extend 3nsrsmlsbl " Ehehe."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbgl "H-{w=0.2}happy Easter,{w=0.2} [chosen_tease]!"

    elif Natsuki.isAffectionate(higher=True):
        n 2ullaj "Easter might be all about fresh starts,{w=0.75}{nw}"
        extend 2tnmbo " but honestly?"
        n 4kslslsbr "..."
        n 4fllsslsbr "I...{w=1}{nw}"
        extend 1nsrsslsbr " think I can settle for the one you gave me too.{w=1}{nw}"
        extend 1fcssslsbr " Ehehe."
        n 2fcsbglsbl "H-{w=0.2}happy Easter,{w=0.2} [player]!"

    else:
        n 2ulrbo "They say Easter is all about fresh starts,{w=0.75}{nw}"
        extend 2tlrpu " but...{w=1}{nw}"
        extend 2fnmsm " honestly?"
        n 3fcsbg "...I like to think this one is juuust getting started.{w=1}{nw}"
        extend 3fsqsm " Ehehe."
        n 4nchgn "Happy Easter,{w=0.2} [player]!"

    $ jn_events.getHoliday("holiday_easter").complete()

    return

label holiday_halloween:
    if preferences.get_volume("music") < 0.25:
        $ preferences.set_volume("music", 0.75)

    if preferences.get_volume("sfx") < 0.25:
        $ preferences.set_volume("sfx", 0.75)

    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    hide natsuki
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    $ jn_events.getHoliday("holiday_halloween").run(suppress_visuals=True)
    hide black

    $ jnPause(3)
    show tense at JN_PULSE zorder JN_GLITCH_ZORDER
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)
    show tense at JN_PULSE zorder JN_GLITCH_ZORDER
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)
    show tense at JN_PULSE zorder JN_GLITCH_ZORDER
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)

    python:
        for i in range(1, 7):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(1.5)

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(1)

    python:
        for i in range(1, 5):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(1)

            if (random.randint(1,5) == 1):
                renpy.play(filename=audio.glitch_d, channel="audio")
                jnPause(0.25)

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a
    $ jnPause(0.5)
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    $ jnPause(0.3)

    python:
        for i in range(1, 3):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(0.75)

            if (random.randint(1,4) == 1):
                renpy.play(filename=audio.glitch_d, channel="audio")
                jnPause(0.25)
                renpy.show(
                    name="glitch_garbled_red",
                    at_list=[JN_PULSE],
                    zorder=JN_GLITCH_ZORDER)
                jnPause(0.15)
                renpy.hide("glitch_garbled_red")

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_b
    $ jnPause(0.25)

    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    $ jnPause(0.15)
    play audio glitch_d

    show black zorder JN_BLACK_ZORDER
    $ jnPause(0.25)
    play audio ooo_creep
    $ jnPause(6)
    hide desk
    hide chair
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_SUNNY)
    $ magical_girl_cosplay = jn_outfits.getOutfit("jn_magical_girl_cosplay")
    $ magical_girl_cosplay.unlock()
    $ Natsuki.setOutfit(outfit=magical_girl_cosplay, persist=False)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_closed"))
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_pumpkins"))
    show deco o31 zorder JN_DECO_ZORDER
    show natsuki 4fchgn at jn_center zorder JN_NATSUKI_ZORDER
    $ jnPause(0.15)
    play audio switch_flip
    hide black
    $ jnPause(1)

    # Have to proc manually here due to fake reveal for the prank
    $ renpy.play(filename="mod_assets/bgm/vacation.ogg", channel="music")
    $ renpy.show_screen("hkb_overlay")
    $ jn_globals.force_quit_enabled = True

    $ player_upper = player.upper()
    n 4fchbg "HAPPY HALLOWEEN,{w=0.75}{nw}" 
    extend 4fchbs " [player_upper]!"
    n 4fchsm "..."
    n 4fsqsm "..."
    n 2fsqss "Well?{w=0.75}{nw}"
    extend 2fcsgs " Don't just sit there!{w=0.75}{nw}"
    extend 4fchgn " Say something already!"
    n 3fnmbs "Did I get you?{w=0.2} Did I get you?{w=0.75}{nw}"
    extend 3fcsbs " Don't lie!{w=1}{nw}"
    extend 7fsqbg " I {i}totally{/i} got you this time!"
    n 3ccsbg "Jeez...{w=1}{nw}"
    extend 7fcsbs " I {i}knew{/i} this dumb old book would come in handy someday!\n{w=0.75}{nw}"
    extend 7fsqss "Not bad for a bunch of reused scripts,{w=0.2} huh?"
    n 3unmbg "And hey -{w=0.5}{nw}"
    extend 3tlrbg " I didn't even blow the classroom up or anything.{w=0.75}{nw}"
    extend 4fchbg " I'd call that a complete success!"
    n 2fchsm "Ahaha."
    n 2cllss "Well,{w=0.2} anyway.{w=0.75}{nw}"
    extend 2ccsbg " I think I'm about done screwing around now."
    n 4ullaj "So -{w=0.5}{nw}"
    extend 4csqbg " you like what I've done with the place?{w=0.75}{nw}"
    extend 3ccspo " You better appreciate all the effort I put into all this,{w=0.2} [player]."
    n 3fnmbg "Yep!{w=0.75}{nw}"
    extend 7fcsbg " As you can {i}clearly{/i} see -{w=0.5}{nw}"
    extend 6fchbg " I pulled out {i}all{/i} the stops this time!"
    n 7clrbg "Awesome hand-crafted decorations?{w=0.75}{nw}"
    extend 7ccsbg " Check!{w=1}{nw}"
    extend 6ckrsm " Fabulously made cosplay?{w=0.75}{nw}"
    extend 6fcsbs " Check again!"
    n 3fnmbg "Getting easily the best jump of the year on [player]?"
    n 7fsgsm "..."
    n 7fcssm "Ehehe.{w=0.75}{nw}"
    extend 3fchgnelg " You bet!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 1cllbg "Man..."
        n 2unmaj "You know,{w=0.2} I'm pretty sure I mentioned it before at some point.{w=0.75}{nw}"
        extend 5csrbosbl " About how I don't really like horror and all."
        n 4ccsfl "But let's be real here,{w=0.2} [player]."

    else:
        n 1cllbg "Man...{w=1}{nw}"
        extend 2tlraj " I know I told you I wasn't the biggest fan of horror already,{w=0.75}{nw}" 
        extend 4ccsfl " but let's be real."

    n 4tnmaj "When it really comes to bang for your buck?{w=0.75}{nw}"
    extend 7ccssmesm " You just can't beat a good old Halloween."
    n 3unmfl "No,{w=0.2} really!{w=0.75}{nw}"
    extend 3fcsbg " Think about it!"
    n 4fsqss "Not {i}only{/i} is it an excuse to break out my sewing kit and blow {i}everyone{/i} away with my needlework..."
    n 1ccsss "But come on.{w=0.75}{nw}"
    extend 2fchgn " What {i}other{/i} holidays give you the excuse to pig out on as much free candy as you can swipe,{w=0.2} huh?"
    n 2fsqsm "..."
    n 1fcssm "Ehehe.{w=0.75}{nw}"
    extend 4fcsbg " That's what I thought,{w=0.2} [player].{w=1.25}{nw}"
    extend 3fchbg " Halloween is the best!"

    # Not ideal conditioning; holidays should really have a shown_count - see: #813. Replace this check and delete persistent flag once this is done!
    # Will need to migrate other holidays for shown counts too... FML.
    if Natsuki.isLove(higher=True) and not persistent._jn_player_love_halloween_seen:
        n 3clrbo "..."
        n 4clrpu "Or...{w=1}{nw}"
        extend 4klrsl " I guess it would be."
        n 5csrslsbl "Not like I'd be the kind to know,{w=0.2} a-{w=0.2}after all."

        if "holiday_christmas_day" in persistent._seen_ever:
            n 5cnmsl "..."
            n 2knmfl "What?{w=0.75}{nw}"
            extend 2kllfll " Don't you remember,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1cllbol " It's like how I told you last Christmas."

        else:
            n 4fcsem "It's just that..."
            n 2kslsl "..."
            n 2kslfl "I-{w=0.2}it just sucks.{w=0.75}{nw}"
            extend 4knmbol " You know?{w=1}{nw}"
            extend 1klrsll " With my family and everything."
        
        n 1ksrsll "..."
        n 4ccspu "We...{w=1}{nw}"
        extend 4ccsfl " never...{w=1}{nw}"
        extend 4cllfl " really celebrated much.{w=1.25}{nw}"
        extend 2cdlsl " At all."
        n 2clrfl "...And Halloween was no exception.{w=0.75}{nw}"
        extend 2clrsl " Obviously.{w=0.75}{nw}"
        extend 4knmfl " Why would it be?"
        n 4cslfl "And the excuses.{w=0.75}{nw}"
        extend 1fcsan " Every year without fail."
        n 3flrwr "'It's not what we do here,{w=0.2} Natsuki!'{w=0.75}{nw}"
        extend 3fllem " 'It's just not right,{w=0.2} Natsuki!{w=0.2} What would our neighbors think?'"
        n 3fslan "As if almost everyone on our street {i}didn't{/i} have kids,{w=0.2} or put decorations up!"
        n 4fcsan "Cut me a break."
        n 4fsrsl "Heh.{w=0.75}{nw}"
        extend 2fnmsl " We all knew what the {i}real{/i} reasons were,{w=0.2} [player]."
        n 2flrbol "And they weren't just because it wasn't Japanese enough,{w=0.2} I'll tell you that much."
        n 1ksrbol "..."
        n 1ccsfllesi "..."
        n 4cnmfll "...Look.{w=0.75}{nw}"
        extend 4ccsajl " I'm not just annoyed about missing out literally every year."
        n 2cllsll "I don't care about some tacky outfits or a bunch of junk from the convenience store."
        n 2cslsll "It's not like that stuff just disappears or something the rest of the year."
        n 2cnmpul "I don't care about any of that."
        n 1clrgsl "I..."
        n 5clrunl "..."
        n 5fcsajl "I...{w=1}{nw}"
        extend 1fcsfll " just...{w=1}{nw}"
        extend 1fllfll " wanted to join in with what everyone else was doing.{w=1}{nw}"
        extend 4knmwrl " W-{w=0.2}with what my {i}friends{/i} invited me to do!{w=0.75}{nw}"
        extend 4clrunl " Is that {i}really{/i} such a crime?"
        n 4fcswrl "A-{w=0.2}and besides,{w=0.2} what right did {i}they{/i} have to...!"
        n 4fllunltsc "T-{w=0.2}to..."
        n 1fcsunltsa "..."
        n 1fcsanltsa "..."
        n 2fcsflltsa "..."
        n 2csrslltsb "...Forget it.{w=1.25}{nw}"
        extend 2ccsgsl " Forget it!{w=1}{nw}"
        extend 4cslunl " I don't even know {i}why{/i} it still annoys me so much."
        n 4fcseml "It was all just..."
        n 4cslbol "..."
        n 1kslbol "...So dumb."
        n 3ccseml "A-{w=0.2}and I know there's nothing stopping me doing what I want now.\n{w=0.75}{nw}"
        extend 3clrbol "As you can see."
        n 4klrfll "But that doesn't change all the wasted time.{w=1.25}{nw}"
        extend 5kdlbol " All the disappointment."
        n 1kslbol "And I don't think it ever will."
        n 2kslsslsbr "...E-{w=0.2}even if getting to spend Halloween with you instead {i}is{/i} pretty awesome."
        n 2kslsllsbr "..."
        n 4knmpulsbr "...I wrote you something too,{w=0.5}{nw}"
        extend 5klrbolsbr " you know."
        n 5clrcalsbr "..."

        $ halloween_poem = jn_poems.getPoem("jn_natsuki_hallows_end")
        $ halloween_poem.unlock()
        play audio page_turn
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_poem_on_desk"))
        $ jnPause(2)

        n 5csqcalsbr "..."
        n 4fnmfllsbl "H-{w=0.2}hey!{w=0.75}{nw}"
        extend 4fllfllsbl " Come on."
        n 2cdlbolsbl "Don't give me that look,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccsemlsbl " Just..."
        n 1ksrpulsbl "..."
        n 1ccsfll "...Just take it already.{w=1}{nw}"
        extend 4cnmcal " Before I change my mind about the whole thing."
        n 4cdrcal "..."

        show natsuki 4kdrcal
        $ jnPause(0.5)
        call show_poem(halloween_poem)
        show natsuki 1cnmcal

        n 1cnmajl "You..."
        n 4cllajl "You did actually read all of that..."
        n 5csgsll "Right?"
        n 2ccseml "Because you have no {i}idea{/i} how much of a pain that was at short notice.{w=0.75}{nw}" 
        extend 2clleml " Especially with you sneaking around all the time.{w=1}{nw}"
        extend 2ccspol " You dork."
        n 1clrbolsbl "..."
        n 4ksrpulsbl "But..."
        n 4ksgpulsbl "Seriously,{w=0.2} [player]?"
        n 1kslsllsbl "..."

        show natsuki 4ccsunlsbl at jn_center zorder JN_NATSUKI_ZORDER
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio clothing_ruffle
        $ jnPause(3.5)
        show natsuki 5cslbolsbr at jn_center zorder JN_NATSUKI_ZORDER
        hide black with Dissolve(1.25)

        n 5kslpul "...T-{w=0.2}thank you.{w=0.75}{nw}"
        extend 2knmbol " For being with me for Halloween,{w=0.2} I mean."
        n 4ccsfll "I know I never got to really dress up,{w=0.75}{nw}"
        extend 4cdrfll " or make tons of fancy decorations,{w=0.75}{nw}"
        extend 1ksrsll " or go partying or anything exciting like that."
        n 1nlrpul "But...{w=1.25}{nw}"
        extend 5nsrssfsbl " I-{w=0.2}I guess I can settle for treating myself to you instead."
        n 5nsrajlsbl "So..."
        n 1csrfslsbl "...Yeah."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4cchsmlsbl "H-{w=0.2}happy Halloween,{w=0.2} [chosen_endearment]."
        n 4cslsmlsbl "..."
        n 2ccsfllsbr "N-{w=0.2}now,{w=0.2} enough of all the lovey-dovey stuff.{w=0.75}{nw}"
        extend 2cllfllsbr " Jeez,{w=0.2} [player]."
        n 2csqpo "Have you {i}totally{/i} forgotten what today is meant to be for already or what?"
        n 4fsqsm "..."
        n 4fsqss "No?"
        n 2fcsss "Heh.{w=0.75}{nw}"
        extend 2ccsbg " Then you better start preparing,{w=0.2} [player]."
        n 4cslbgsbr "Being here with you might be a treat..."
        $ jn_stickers.stickerWindowPeekUp(at_right=True)
        n 4fsqbs "...But you bet I've still got a ton of {i}tricks{/i} up my sleeve!{w=0.75}{nw}"
        extend 2nchgn " Ehehe."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio drawer
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
        $ jnPause(2)
        hide black with Dissolve(0.5)

        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 2uchgnl "Now let's get spooky already,{w=0.2} you [chosen_tease]!"
        $ persistent._jn_player_love_halloween_seen = True

    else:
        n 3cslss "..."
        n 4cslfl "Or...{w=1}{nw}"
        extend 4cslsl " at least it would be.{w=0.75}{nw}"
        extend 2fsrem " If {i}some people{/i} didn't insist on being complete idiots about it."
        n 2fcsfl "Ugh."
        n 2clrfl "Like,{w=0.2} don't get me wrong -{w=0.5}{nw}"
        extend 4fcsaj " I'm always game for a good prank!{w=0.75}{nw}"
        extend 4ccspo " I'm not thin-skinned,{w=0.2} obviously."
        n 2fslan "But what I can't {i}stand{/i} is when some people take it all {i}way{/i} over the top!{w=0.75}{nw}"
        extend 1fsqem " Or they're just straight-up jerks about the whole thing."
        n 4fcsfl "Yeah.{w=0.75}{nw}"
        extend 4fsgfl " You know the type,{w=0.2} [player]."
        n 3ftrfl "{i}Pranksters{/i},{w=0.5}{nw}"
        extend 3fsran " my butt."
        n 4fnmgs "Seriously!"
        n 4fllem "I get that mischief night is a thing too."
        n 2fcswr "But what the hell kind of 'mischief' involves just pissing people off?!{w=0.75}{nw}"
        extend 2fnmfu " Or going around everywhere and making a total ass out of yourself?"
        n 2fcsan "Cut me a break."
        n 4csqan "And don't even get me {i}started{/i} on keeping everyone up all night with crappy music..."
        n 3fsrem "...Or trashing a bunch of other people's stuff on purpose."
        n 3fcsemesi "Ugh..."
        n 4cllsl "Forget the eggs and toilet paper."
        n 5fslsl "Just makes me wanna smack them right in their stupid faces.{w=0.75}{nw}"
        extend 2fcsgs " Who says that isn't just {i}my{/i} take on a 'prank'?"
        n 2fsrsl "Jerks."
        n 1fcsflesi "..."
        n 4ccsfl "W-{w=0.2}whatever.{w=0.75}{nw}"
        extend 4cnmaj " You know what,{w=0.2} [player]?"
        n 2flrfl "Who even has the time to care about a bunch of idiots ruining things for themselves?{w=0.75}{nw}"
        extend 2fcspo " I sure don't."
        n 1ccsaj "A-{w=0.2}and besides."

        if Natsuki.isLove(higher=True):
            n 3cllssl "We both know {i}you{/i} aren't like that.{w=0.75}{nw}"
            extend 5ccssslsbr " T-{w=0.2}that's all that matters."

        elif Natsuki.isAffectionate(higher=True):
            n 7cllsslsbr "I'm pretty sure {i}you{/i} aren't like that.{w=0.75}{nw}"
            extend 3ccssslsbr " Even if you are a dork."

        else:
            n 7csqss "I kinda doubt {i}you're{/i} one of those people."

        n 3clrss "And it's not like we have to worry about any of that here either,{w=0.2} at any rate."
        n 4fcsaw "So!"
        n 4fsqbg "I hope you prepared yourself,{w=0.2} [player]."
        n 2ccsbg "'Cause if you haven't prepared plenty of treats today for yours truly..."
        $ jn_stickers.stickerWindowPeekUp(at_right=True)
        n 2fchgn "...Then you better get ready for some more grade-A tricks instead!{w=0.75}{nw}"
        extend 1nchgn " Ehehe."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTeaseName()
            n 2fwlbgl "Love you too,{w=0.5}{nw}" 
            extend 2fchblleaf " you big [chosen_tease]!"

        elif Natsuki.isAffectionate(higher=True):
            $ random_tease = random.choice(["dork", "dope"])
            n 3fchbgl "Now let's get spooky already,{w=0.2} you [random_tease]!"

        else:
            n 3fnmbg "Now let's spook things up already!"

    $ jn_events.getHoliday("holiday_halloween").complete()
    return

label holiday_christmas_eve:
    python:
        import copy

        # Let it snow
        jn_atmosphere.showSky(jn_atmosphere.WEATHER_SNOW)

        # The Nat in the Hat
        jn_outfits.getWearable("jn_headgear_santa_hat").unlock()
        santa_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        santa_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_santa_hat")
        santa_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(santa_hat_outfit)

        # Let it go
        jn_events.getHoliday("holiday_christmas_eve").run()

    n 1uchbg "Heeeey!{w=0.75}{nw}"
    extend 4uchbs " [player]!{w=0.5} [player]!"
    n 1uchgnedz "Guess what day it is?"
    n 1tsqsm "..."
    n 1fsqsm "Ehehe.{w=0.5}{nw}"
    extend 1fchbl " As {i}if{/i} I needed to remind you!"
    n 3ulraj "Man..."
    n 3tnmsssbr "Hard to believe it's Christmas Eve {i}already{/i},{w=0.2} huh?"
    n 3nsrsssbr "It's actually almost spooky how quickly it rolls around.{w=1}{nw}"
    extend 1uwdajsbr " Seriously!"
    n 1fllem "I mean...{w=1}{nw}"
    extend 1nsqbo " the later part of the year mainly feels like just one big snooze-{w=0.2}fest."
    n 2nsrem "School starts again,{w=0.75}{nw}"
    extend 2fslem " it gets all cold and nasty outside,{w=0.75}{nw}"
    extend 2nsqpo " everyone gets stuck indoors..."
    n 1fnmem "But then before you know it?{w=1}{nw}"
    extend 1fcsgs " December rolls around,{w=0.75}{nw}"
    extend 1fbkwr " and it's like all hell breaks loose!"
    n 3fslan "Every time!{w=0.5} Like clockwork!"
    n 3fcsemsbr "Yeesh,{w=0.5}{nw}"
    extend 1tsqemsbr " you'd think with a whole {i}year{/i} to prepare,{w=1}{nw}"
    extend 1fslcasbr " people wouldn't {i}always{/i} leave things to the very last month."
    n 3flrem "Like...{w=0.75}{nw}"
    extend 3fcswr " who {i}does{/i} that to themselves?"
    n 1fcsajeansbr "Oh,{w=0.75}{nw}"
    extend 1fcsgs " and don't even get me {i}started{/i} on the music {i}every{w=0.3} single{w=0.3} store{/i}{w=0.3} feels the need to play..."
    n 1fslsl "Ugh..."
    n 1fcspoesi "I swear,{w=0.2} it's like some kind of coordinated earache."
    n 1fllca "..."
    n 1unmgslsbl "D-{w=0.3}don't get me wrong!{w=0.75}{nw}"
    extend 3fcsgslsbl " I'm no scrooge{nw}"
    extend 3fcspolsbr "!"
    n 1fcsbglsbr "...I{w=0.2}-I'm just not stuck in the {i}Christmas past{/i},{w=0.2} that's all!{w=0.75}{nw}"
    extend 4fchsml " Ehehe."
    n 1ullss "Well,{w=0.75}{nw}"
    extend 1nllbg " whatever.{w=1}{nw}"
    extend 1fchgn " At least {i}here{/i} we can change the record,{w=0.2} right?"
    n 1fsqbg "And speaking of which..."
    n 4uchsmedz "What do you think of my decoration skills,{w=0.2} [player]?{w=0.75}{nw}"
    extend 4fwlbgeme " Not bad for {i}just{/i} school supplies,{w=0.2} if I say so myself."
    n 1fchbl "Just don't ask me where I got the tree!"
    n 1usqsm "...{w=1}{nw}"
    n 4uwdajeex "Ah!{w=1}{nw}"
    n 3fnmbg "But what about you,{w=0.2} [player]?{w=1}{nw}"
    extend 3fsqsg " Huh?"
    n 1fcsbg "You didn't {i}seriously{/i} think {i}you{/i} were off the hook for decorating,{w=0.2} did you?"
    n 1fchbg "Sorry!{w=0.75}{nw}"
    extend 1uchgnelg " Not a chance!"
    n 4fcsbg "So...{w=1}{nw}"

    show natsuki 1tsqsm at jn_center

    menu:
        extend " are {i}you{/i} all good to go yet,{w=0.2} [player]?"

        "You bet I am!":
            n 1usqct "Oho?"
            n 1fchbg "Well,{w=0.2} no kidding!{w=1}{nw}"
            extend 2fcsbs " Now that's {i}exactly{/i} what I like to hear."
            n 1fchbs "This year is gonna be {b}awesome{/b}!{w=0.75}{nw}"
            extend 1uchgnedz " I just know it!"

            $ persistent._jn_player_celebrates_christmas = True

        "I haven't decorated yet.":
            n 1uskemlesh "H-{w=0.2}huh?!"
            n 1fbkwrl "T-{w=0.2}then what are you doing sitting around here,{w=0.2} you goof?!{w=0.75}{nw}"
            extend 3fcsajlsbl " Jeez..."
            n 3fcspolsbl "I'm not doing {i}your{/i} place too,{w=0.2} you know."
            n 1fchbl "...Not for {i}free{/i},{w=0.2} anyway."

            $ persistent._jn_player_celebrates_christmas = True

        "I don't really celebrate Christmas.":
            n 4kslpu "...Aww.{w=0.75}{nw}"
            extend 4knmbo " Really?"
            n 1kllsl "..."
            n 1fcstrlsbr "I-{w=0.2}I mean,{w=0.75}{nw}"
            extend 1fchsmlsbl " that's totally fine."
            n 2fsqsslsbl "...Just means I gotta celebrate for both of us!{w=0.75}{nw}"
            extend 2fchsmleme " Ahaha."

            $ persistent._jn_player_celebrates_christmas = False

    n 1kslsm "..."
    n 1kslpu "But...{w=1}{nw}"
    extend 4knmpu " in all seriousness,{w=0.2} [player]?"
    n 2ksrbosbl "..."

    if Natsuki.isEnamored(higher=True):
        n 1kcscalsbl "...Thanks."
        n 2ksrajlsbl "For coming to see me today,{w=0.2} I mean."
        n 4knmajl "It..."
        n 4kslpul "..."
        n 1kcsbolesi "It seriously means a lot.{w=1}{nw}"
        extend 4kwmbol " You being here right now."
        n 2ksrbol "...Probably more than you'd know."
        n 1klrbol "..."
        n 1kwmpuf "...I really should have been spending today with my friends,{w=0.2} [player].{w=1}{nw}"
        extend 1kllbol " But..."

        if Natsuki.isLove(higher=True):
            n 4kwmfsfsbr "I-{w=0.3}I think I can settle for just you."

        else:
            n 2nslfsfsbr "I-{w=0.3}I can probably settle for you this year."

        n 1kslbol "..."
        n 1kslpul "And...{w=0.75}{nw}"
        extend 4ksqbol " [player]?"
        n 2ksrfsfsbr "..."
        show natsuki 1fcscafsbr

    elif Natsuki.isAffectionate(higher=True):
        n 1kcscalsbl "...T-{w=0.2}thanks."
        n 1fcsemlsbl "F-{w=0.3}for being here today,{w=0.75}{nw}"
        extend 2kslbolsbl " I mean."
        n 1fcsbolsbr "I-{w=0.3}I know you didn't have to come visit at all.{w=0.75}{nw}"
        extend 2ksrpulsbl " And I'd be a real jerk to demand it..."
        n 1knmpulsbl "So just..."
        n 1kslunlsbl "..."
        n 1fcsunf "Just...{w=0.75} know it's appreciated.{w=1.25}{nw}"
        extend 4kwmunl " 'Kay?"
        n 2kslbol "Really.{w=1.25}{nw}"
        extend 4ksqbol " Thank you."
        n 1ksrcal "..."
        n 1ksrajlsbr "And...{w=1}{nw}"
        extend 4knmajlsbr " [player]?"
        n 1kcsunfsbr "..."
        show natsuki 2fcssrfsbr

    else:
        n 1kcscalsbl "...Thanks.{w=0.75}{nw}"
        extend 1fcsemlsbl " F-{w=0.3}for turning up today,{w=0.2} I mean."
        n 3fcsgslesssbr "I-{w=0.2}I knew you would,{w=0.2} of course!"
        n 3fcscal "A-{w=0.2}and besides."
        extend 3fsrcal " Only a real jerk would leave someone all alone here,{w=1}{nw}"
        extend 1klrcafsbr " of all nights."
        n 1fcsajlsbr "So I..."
        n 1fllajlsbr "I..."
        n 4kslsllsbr "..."
        n 1fcsunlsbr "I...{w=1.25}{nw}"
        extend 1kcspufesisbr " really appreciate it.{w=0.75}{nw}"
        extend 4kwmbolsbr " I do."
        n 4kslbolsbr "..."
        n 4kwmpulsbr "...A-{w=0.2}and [player]?"
        n 2fslunfsbl "..."
        show natsuki 1fcsunfesssbl

    play audio chair_out
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)

    if Natsuki.isEnamored(higher=True):
        play audio clothing_ruffle

        if Natsuki.isLove(higher=True):
            $ jnPause(2.5)
            play audio kiss

        show natsuki 1kcsfsf at jn_center

    else:
        play audio clothing_ruffle
        show natsuki 4kcsbol at jn_center

    $ jnPause(3)
    play audio chair_in
    $ jnPause(2)

    if Natsuki.isLove(higher=True):
        show overlay mistletoe zorder JN_OVERLAY_ZORDER at jn_mistletoe_lift

    hide black with Dissolve(1.25)

    if Natsuki.isLove(higher=True):
        n 4fchsmf "M-{w=0.2}mind the mistletoe!"
        n 4fchtsfeaf "Ehehe."
        hide overlay

    elif Natsuki.isEnamored(higher=True):
        n 2kslsmlsbl "S-{w=0.2}so..."
        n 4kwmsml "What did you wanna talk about,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fchsmlsbr " Ehehe."

    else:
        n 2kslfsl "..."
        n 1ncsajlsbl "N-{w=0.3}now,{w=1}{nw}"
        extend 4tsqsslsbl " where were we?"
        n 3fsrdvlsbr "Ehehe..."

    $ Natsuki.calculatedAffinityGain(5, bypass=True)
    $ jn_events.getHoliday("holiday_christmas_eve").complete()

    return

label holiday_christmas_day:
    python:
        # Let it snow
        jn_atmosphere.showSky(jn_atmosphere.WEATHER_SNOW)

        # Dress up Natsu
        christmas_outfit = jn_outfits.getOutfit("jn_christmas_outfit")
        christmas_outfit.unlock()
        jn_outfits.saveTemporaryOutfit(christmas_outfit)

        # Let it go
        jn_events.getHoliday("holiday_christmas_day").run()

    n 1uwdgsesu "Omigosh!{w=0.5}{nw}"
    extend 4uchbsl " Omigosh omigosh omigosh omigosh omigoooosh!"
    n 1unmbgleex "!{w=0.5}{nw}"
    n 4uwdbgl "[player]!{w=0.75}{nw}"
    extend 4uwdbsl " [player]!{w=0.2} [player]!"
    n 1uchbsl "It's here!{w=0.75}{nw}"
    extend 1uchbgl " It's actually,{w=0.5}{nw}"
    extend 1fchbsl " finally,{w=0.5}{nw}"
    extend 4uchgnleme " freaking{w=0.5} {i}HERE{/i}!"

    if jn_get_current_time_block in [JNTimeBlocks.early_morning, JNTimeBlocks.mid_morning, JNTimeBlocks.late_morning]:
        n 3fspgs "Come on!{w=0.75}{nw}"
        extend 1knmgs " Get the sleep out of your eyes already,{w=0.2} [player]!"
        n 1fcsss "Up and at 'em!{w=0.5}{nw}"
        extend 4fchbg " C'mon,{w=0.2} [player]!"

    else:
        n 3fspgs "What even {i}took{/i} you so long?{w=0.75}{nw}"
        extend 3fsqpoesi " Did you forget what day it was or something?{w=0.5}{nw}"
        extend 3fcsgs " It's time to celebrate!"
        n 1fcsbg "'Cause..."

    n 4uchbsleme "IT'S CHRISTMAAAAS!{w=1}{nw}"
    extend 1uchsmleme " Ehehe!"
    n 1kcssslesi "..."
    n 1kcsss "Man,{w=0.75}{nw}"
    extend 3fchsm " it feels so good to {i}finally{/i} say that..."
    n 1ullss "I mean...{w=0.75}{nw}"
    extend 2tllss " it isn't as if I had tons planned or anything.{w=1}{nw}"
    extend 2nsrss " ...Not like there's much {i}to{/i} plan here."
    n 1ncsss "But there's just something about Christmas that brings that sense of relief,{w=0.5}{nw}"
    extend 4ksqsm " you know?"
    n 1fcssm "Studies can take a hike,{w=0.75}{nw}"
    extend 1ullaj " everything's all arranged and ready to go for everyone..."
    n 1tnmss "And even if it's just for a couple days..."
    n 4fchbg "Just having all that weight and stress removed {i}rocks{/i}!{w=1}{nw}"
    extend 4uchgn " It's great!"
    n 1kcsssesi "Like I can just feel the stress of the year washing away from me..."
    n 4fwlbl "And I don't even have to cook anything here!{w=0.75}{nw}"
    extend 1fchsm " Ehehe..."
    n 2kslsm "..."
    n 1kslsr "..."
    n 1kcssr "..."
    n 1ncspu "It's...{w=0.75}{nw}"
    extend 2kslpu " rough sometimes,{w=1}{nw}"
    extend 2kslsl " you know."
    n 2ksqsl "Christmas,{w=0.2} I mean."
    n 2klrbo "..."
    n 1kcspuesi "..."
    n 4ksrslsbl "...How do I {i}even{/i} put this..."
    n 1fcsunsbl "..."
    n 1fcsaj "We..."
    n 2ksrsl "W-{w=0.2}we were always 'traditional',{w=0.2} my family.{w=1}{nw}"
    extend 1ksqsl " I-{w=0.2}if we were asked."
    n 2ncsss "...Heh.{w=1}{nw}"
    extend 4tsqbo " Why,{w=0.2} you wonder?"
    n 2kslbo "...Think about it,{w=0.2} [player]."
    n 1ksqsr "..."
    n 1fcssr "...You don't need to buy gifts,{w=0.2} if you're {i}traditional{/i}.{w=1.25}{nw}"
    extend 2fsrsl " You don't need to invite guests,{w=0.2} if you're {i}traditional{/i}."
    n 1ksqsl "..."
    n 1kllpu "You see where I'm going with this...{w=1}{nw}"
    extend 4ksqbo " right?"
    n 2fcsunl "N-{w=0.2}not celebrating it wasn't a {i}choice{/i} at my place,{w=0.2} [player]."
    n 1fcsbol "..."
    n 1ncspul "So..."
    n 1nnmbo "...I made my own.{w=0.75}{nw}"
    extend 2kllbo " I'd sneak out."
    n 2ncsss "Heh.{w=0.75}{nw}"
    extend 4nslss " I'd already gotten {i}real{/i} good at figuring out where the squeaky floorboards were,{w=0.5}{nw}"
    extend 1nslfs " I'll tell you that much."
    n 2kslsll "I'd just leave for a couple hours."
    n 1nsrssl "Sure,{w=0.3} it was cold,{w=0.75}{nw}"
    extend 1ksrsrl " but..."
    n 1fsrunl "At least seeing all the decorations up on people's houses gave me {i}some{/i} sense of cheer."
    n 1fslsll "Besides.{w=0.3} Not like {i}they{/i} particularly cared where I was..."
    n 1kslsll "..."
    n 4ksqbol "But my friends always did."
    n 4knmpul "...We'd already arranged something,{w=1}{nw}" 
    extend 4knmbolsbr " you know."
    n 1kllbolsbr "For Christmas.{w=1}{nw}"
    extend 2tnmbolsbr " Didn't I tell you,{w=0.2} [player]?"
    n 1nllss "I was {i}meant{/i} to meet up with everyone,{w=0.75}{nw}"
    extend 4nslfs " and we were supposed to head off to Yuri's together."
    n 2kslss "...Heh.{w=0.75}{nw}"
    extend 4knmbo " There was so much talk over where we'd all go."
    n 1klrsssbl "Sayori got so excited over hosting...{w=0.75}{nw}"
    extend 2nsrsssbl " but it would have been {i}way{/i} too cramped for all of us."
    n 1nlraj "Though...{w=1}{nw}" 
    extend 1tnmbo " seriously?"
    n 1kslbo "..."
    n 1kcsaj "I...{w=0.75}{nw}"
    extend 2kslfs " never really paid it much mind."
    n 1ucsaj "Sayori's place,{w=0.75}{nw}"
    extend 1nlraj " Monika's...{w=1}{nw}"
    extend 4ksrfs " It honestly didn't even matter."
    n 1knmbo "...Wherever I went?{w=1}{nw}"
    extend 4tnmpu " So long as we were all together?"
    n 1kllbol "..."
    n 2fcsunl "T-{w=0.3}that's where {i}my{/i} home was."
    n 2fcsunltsa "..."
    n 2fllunltsc "I didn't even care what I got."
    n 2fcsunl "It didn't matter.{w=1}{nw}"
    extend 4ksrsll " N-{w=0.2}not really."
    n 1kcsajl "Just...{w=1}{nw}"
    extend 2fcsunl " warmth.{w=0.5} P-{w=0.2}people who really {i}cared{/i}."
    n 2fcsemltsa "N-{w=0.2}not about money.{w=1}{nw}"
    extend 2ksrboltsb " About me.{w=1}{nw}"
    extend 1ksrpultsb " Even if I could never get them {i}anything{/i}..."
    n 1fcsunlsbl "...That was a gift enough to me."
    n 1fcsajlsbl "So that's why..."
    n 2flrajltscsbl "S-{w=0.3}so that's..."
    n 2klremltscsbl "...t-{w=0.3}that's...{w=1}{nw}"
    extend 2fcsemltsd " w-{w=0.3}why..."
    n 2kcsupltsd "..."
    n 2kcsanltsd "..."

    $ prompt = "Natsuki..." if Natsuki.isEnamored(higher=True) else "Natsuki?"
    menu:
        "[prompt]":
            pass

    n 2fcsunltsd "I-{w=0.3}I'm fine.{w=1}{nw}"
    extend 2fcsemltsa " I'm fine!"
    n 1kcsboltsa "..."
    n 1kcspultsa "I-{w=0.2}it's just that..."
    n 4kslpultsb "..."
    n 1kcspultsb "..."
    n 1kcsboltsb "..."
    n 4ksqboltsb "...They aren't here anymore,{w=0.2} [player].{w=1.25}{nw}"
    extend 1kslpultsb " They haven't been here a long time now."
    n 2kllboltdr "...T-they're gone."
    n 1kwmboltdr "But they never stopped being my friends.{w=1.25}{nw}"
    extend 1kcsbol " A-{w=0.2}and I guess that's why I'm still celebrating."
    n 3kslfsl "...For them."

    if Natsuki.isEnamored(higher=True):
        n 1ksqbol "..."
        n 3ksrfslsbl "...A-{w=0.3}and for you."

    n 4kslpul "So..."
    n 1knmpul "..."
    n 1kcspul "...Thanks,{w=0.2} [player].{w=1}{nw}"
    extend 2ksrpolsbl " Really."
    n 1kcssllsbl "I don't have {i}all{/i} my friends right now,{w=0.75}{nw}"
    extend 2ksrbol " but..."

    if Natsuki.isLove(higher=True):
        n 2ksqbol "...Just having you here,{w=0.2} [player]?"
        n 1kslfsl "Heh."
        n 1kllssl "...Yeah.{w=1}{nw}"
        extend 4kcssmfsbl " I {i}know{/i} I can manage."

    elif Natsuki.isEnamored():
        n 2kslsmlsbl "...I think I can manage with just you."

    elif Natsuki.isAffectionate():
        n 4nslsslsbl "...A-{w=0.2}at least I got my best one."

    else:
        n 1ncsbol "I think..."
        n 1ncspulesi "..."
        n 1ncscal "I-{w=0.2}I think even just the one here is enough right now."

    if persistent._jn_player_celebrates_christmas == False:
        n 2nslsslsbr "Even if you {i}don't{/i} really celebrate Christmas."

    $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
        poem_list=jn_poems.getAllPoems(),
        unlocked=False,
        holiday_types=[jn_events.JNHolidayTypes.christmas_day],
        affinity=Natsuki._getAffinityState()
    )
    $ unlocked_poem_pool.sort(key = lambda poem: poem.affinity_range[0])
    $ christmas_poem = unlocked_poem_pool.pop() if len(unlocked_poem_pool) > 0 else None

    if christmas_poem:
        $ christmas_poem.unlock()

        # We have a poem to give the player
        n 1nllsllsbl "..."
        n 4knmcalsbl "...I did get you something,{w=0.2} you know."
        n 1fsrunlsbl "..."
        n 3fnmajlsbl "H-{w=0.3}hey!{w=0.75}{nw}"
        extend 3fcspolsbr " Don't give me that look."
        n 1fcstrlsbr "You didn't {i}seriously{/i} think all I had to give you was a {i}story{/i},{w=0.2} did you?"
        n 1fcsemlsbr "I had to at least {i}try{/i},{w=0.75}{nw}"
        extend 4kllbolsbr " s-{w=0.2}so..."

        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1knmbofsbr "..."
            n 2fcscalsbr "...J-{w=0.2}just look at it already,{w=0.2} [chosen_tease]."
            show natsuki 1kcscalsbr at jn_center

        else:
            n 1nslunlsbr "..."
            n 2fcsunlsbl "Nnnnnnn-!"
            n 2fcsemlsbl "...J-{w=0.2}just...{w=1}{nw}"
            extend 2ksrsllsbl " read it already,{w=0.2} [player].{w=1.25}{nw}"
            extend 2fcssllsbl " {i}B-before{/i} I change my mind."
            show natsuki 1ksrsllsbl at jn_center

        call show_poem(christmas_poem)

        if Natsuki.isEnamored(higher=True):
            n 4ksqcalsbr "...Finished,{w=0.2} [player]?"
            n 1kslcalsbr "..."
            n 1kcsbolsbl "...Look.{w=1}{nw}"
            extend 1fcseml " I'm..."
            n 1kslbol "..."
            n 3ksqbol "I'm not gonna kid myself and say this was some {i}amazing{/i} gift."
            n 3nsrsssbl "...Not like I'm the {i}first{/i} one to hand you a poem."
            n 1ncsajsbl "I just..."
            n 1kslsllsbl "..."
            n 1kcssllsbl "I-{w=0.2}I just wanted to show some appreciation.{w=1}{nw}"
            extend 4ksqcal " F-{w=0.2}for everything."
            n 1kcsajl "It...{w=0.75}{nw}"
            extend 1kcssll " seriously...{w=0.75}{nw}"
            extend 4kwmsll " m-{w=0.2}means a lot to me,{w=0.2} [player]."
            n 1kslbol "I-{w=0.2}it really does."
            n 4kwmfsl "...Thank you."

        else:
            n 2nsqsllsbl "..."
            n 2tsqcalsbl "All done,{w=0.2} [player]?{w=1}{nw}"
            extend 2nslssl " Man..."
            n 1fcsajlsbl "A-{w=0.2}about time,{w=0.2} huh?{w=1}{nw}"
            extend 3flrajlsbl " I swear,{w=0.5}{nw}"
            extend 3fcspolsbl " sometimes it's like you {i}need{/i} things read out to you or something.{w=0.75}{nw}"
            extend 1fsrfslsbl " Heh."
            n 1ksrbol "..."
            n 1kcsbolesi "..."
            n 4fslbol "...I know it wasn't much.{w=0.75}{nw}"
            extend 1kslsll " I'm not going to kid myself."
            n 3fsrunlsbr "I-{w=0.2}I know I can't get you some {i}fancy gift{/i}.{w=0.75}{nw}"
            extend 3fsrajlsbr " It's just..."
            n 1ksrbolsbr "..."
            n 1fcsbofsbr "...Just know I appreciate what you've done.{w=1}{nw}"
            extend 4fsldvlsbl " Even if it is just listening to me ramble on sometimes."
            n 1nllpulsbl "It really..."
            n 1fcsunlsbl "..."
            n 1kcscalsbl "..."
            n 1ksqcalsbl "I-{w=0.2}It means a lot to me,{w=0.2} [player]."
            n 2ksrcafsbl "...T-thanks."

    else:
        n 2kllbol "..."

        if Natsuki.isEnamored(higher=True):
            n 4kwmfsl "...And [player]?"
            show natsuki 1fcscalsbl at jn_center

        else:
            n 1kllpul "...And...{w=1}"
            extend 4knmsll " [player]?"
            n 1ksrsllsbl "..."
            show natsuki 1fcsunlsbl at jn_center

    play audio chair_out
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)

    if Natsuki.isEnamored(higher=True):
        play audio clothing_ruffle
        $ jnPause(2.5)
        play audio kiss
        show natsuki 1kcsfsf at jn_center

    else:
        play audio clothing_ruffle
        show natsuki 1kcsbol at jn_center

    $ jnPause(3)
    play audio chair_in
    $ jnPause(1)
    hide black with Dissolve(2)
    $ jnPause(2)

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4kchfsfeaf "...Merry Christmas,{w=0.2} [chosen_endearment]."

    else:
        n 1fchsmfsbl "M-{w=0.3}merry Christmas."

    $ jn_events.getHoliday("holiday_christmas_day").complete()

    return

label holiday_new_years_eve:
    $ jn_events.getHoliday("holiday_new_years_eve").run()

    n 4nchbselg "[player]!{w=1}{nw}"
    n 4uchlgelg "[player]!{w=0.5} [player]!"
    n 1fspaj "Look at the date!{w=0.5}{nw}"
    extend 1unmbg " Do you even know what day it is?!{w=1}{nw}"
    extend 1fspgsedz " It's almost the new year!"
    n 3kcsss "Man...{w=1}{nw}"
    extend 3fchgn " and about time too,{w=0.2} huh?"
    n 4ullaj "I don't know about you,{w=0.2} [player]...{w=1}{nw}"
    $ current_year = datetime.date.today().year
    extend 1fchbleme " but I can't {i}WAIT{/i} to tell [current_year] where to stick it!"
    n 1fsqsm "And what better way to do that...{w=0.75}{nw}"
    extend 1fchgnedz " than a crap ton of explosions and snacks?"
    n 3fchsml "Ehehe.{w=0.5}{nw}"
    extend 3fchbglelg " It's gonna be great!"

    if Natsuki.isEnamored(higher=True):
        n 1kllsml "..."
        n 1kllpul "But...{w=0.75}{nw}"
        extend 4knmbol " in all seriousness,{w=0.2} [player]?"
        n 1klrbol "..."
        n 1fcspul "I'd...{w=1}{nw}"
        extend 2knmpol " really like to spend it with you."
        n 1kllpof "..."
        n 2kslunf "...I'd like that a lot."
        n 2fcsemf "I-{w=0.3}if you didn't have anything planned,{w=0.2} anyway.{w=1}{nw}"
        extend 2nwmpol " I'm not gonna be a jerk about it if you already had stuff to do."
        n 1nlrpul "Though...{w=1}{nw}"
        extend 1tnmpul " if you didn't?{w=0.75}{nw}"
        extend 1nslssl " Well..."
        n 4nsqsmfsbl "You know where to find me.{w=0.5}{nw}"
        extend 4flldvfsbl " Ehehe."

        if Natsuki.isLove(higher=True):
            n 1uchsmfeaf "Love you,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1kllsll "..."
        n 4knmsll "...I'm not gonna expect you to drop all your plans to come see me,{w=0.5}{nw}"
        extend 1klrbol " you know."
        n 2fcsemlesssbl "I-{w=0.3}I know you already have...{w=1}{nw}"
        extend 2fllsllsbl " a life.{w=0.75}{nw}"
        extend 1kslsllsbl " Out there."
        n 2fcspol "I'm not gonna be a complete jerk about it.{w=0.75}{nw}"
        extend 1fcsajlsbl " I'm {i}way{/i} better than that,{w=0.5}{nw}"
        extend 2fslpolsbr " a-{w=0.3}after all."
        n 1kslpulsbr "But...{w=1.25}{nw}"
        extend 4knmpulsbl " [player]?"
        n 1ksrunlsbl "..."
        n 3fcspolsbl "...It isn't like I'd say {i}no{/i} to your company,{w=0.2} you know.{w=1}{nw}"
        extend 3fllpofesssbl " S-{w=0.3}so long as you don't make it all gross,{w=0.2} anyway."
        n 1fsldvfesdsbr "Ehehe."

    else:
        n 1fnmssl "Just a word of warning though,{w=0.2} [player]..."
        n 1fsqbgl "I {i}fully{/i} expect to see you here for it.{w=1}{nw}"
        extend 1fcslgl " No excuses!"
        n 1fcsajl "A-{w=0.3}and besides,{w=0.5}{nw}"
        extend 2fsrpofsbl " you {i}did{/i} bring me back to experience things like this."
        n 2fsqpolsbr "It's the least you can do...{w=1}{nw}"
        extend 4kwmpolsbr " right?"

    $ jn_events.getHoliday("holiday_new_years_eve").complete()

    return

label holiday_natsuki_birthday:
    python:
        import copy

        # Give Natsuki a party hat, using whatever she's currently wearing as a base
        party_hat = jn_outfits.getWearable("jn_headgear_classic_party_hat")

        if not party_hat.unlocked:
            party_hat.unlock()

        birthday_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        birthday_outfit.headgear = party_hat
        birthday_outfit.hairstyle = jn_outfits.getWearable("jn_hair_ponytail")
        jn_outfits.saveTemporaryOutfit(birthday_outfit)

        # Delete the party supplies needed to proc this holiday
        jn_utils.deleteFileFromDirectory(os.path.join(renpy.config.basedir, "characters/party_supplies.nats").replace("\\", "/"))

        player_initial = jn_utils.getPlayerInitial()
        player_final = jn_utils.getPlayerFinal(3)
        already_celebrated_player_birthday = jn_events.getHoliday("holiday_player_birthday").is_seen
        jn_atmosphere.showSky(weather=jn_atmosphere.WEATHER_CHERRY_BLOSSOM, with_transition=False)
        
        jn_events.getHoliday("holiday_natsuki_birthday").run()

    $ jnPause(0.25)
    play audio smack
    show natsuki 1cchanlsbr
    show confetti falling at jn_confetti_fall zorder JN_PROP_ZORDER
    $ jnPause(2.25)
    hide confetti
    show confetti desk zorder JN_PROP_ZORDER

    if persistent._jn_natsuki_birthday_known:
        n 1uskgsleshsbr "...!{w=0.75}{nw}"
        n 4ccsemlsbr "W-{w=0.2}wait,{w=0.5}{nw}"
        extend 4cnmemlsbr " what?{w=0.75}{nw}"
        extend 4cllemlsbl " This is..."
        n 4clrwrlsbl "This is all...!{w=0.75}{nw}"
        extend 1unmemlsbl " H-{w=0.2}how...?!"

        show natsuki idle fluster
        menu:
            "Happy Birthday, [n_name]!":
                pass

        n 4fcsanlsbl "Nnnnnnn-!"
        n 4fbkwrf "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 2kbkwrl " What {i}is{/i} all thiiiis?!"
        n 2fcsgslsbl "Y-{w=0.2}you were supposed to {i}forget{/i} all about my birthday!{w=0.75}{nw}"
        extend 2fllgslsbl " And what do you go ahead and do?!"
        n 4fbkwrleansbl "You go and make me the front and center of {i}everything{/i}!"
        n 1fcsgsl "Then just to top it off,{w=0.5}{nw}"
        extend 4flrgslsbr " it's {i}easily{/i} the most embarrassing type of attention too!"
        extend 4ksrfllsbr " Man..."

    else:
        n 1uskgsleshsbr "...!{w=0.75}{nw}"
        n 4kllfllsbr "H-{w=0.2}huh?{w=0.75}{nw}"
        extend 4klrpulsbl " What the..."
        n 1clrfllsbl "W-{w=0.2}what even...?"
        n 1cllunlsbr "This...{w=1}{nw}"
        extend 4fsluplsbl " this is all..."
        n 4fcsuplsbl "..."
        n 4fcsanlsbl "Uuuuuuuu...!"
        n 2fbkwrf "[player_initial]-{w=0.2}[player][player_final]!{w=1}{nw}"
        extend 2knmwrl " What the {b}hell{/b} is all this?!{w=0.75}{nw}"
        extend 2fllwrl " Are you {i}kidding me{/i}?!"
        n 4fbkwrl "I didn't even {i}tell you{/i} my birthday!{w=0.75}{nw}"
        extend 1clreml " How did you even...!"

        show natsuki idle fluster
        menu:
            "Happy Birthday, [n_name]!":
                pass

        if Natsuki.isEnamored(higher=True):
            n 2ccsgslsbl "W-{w=0.2}well yeah!{w=0.75}{nw}"
            extend 2flremlsbl " No kidding!{w=0.75}{nw}"
            extend 2csrfllsbl " Sheesh..."
            n 4ksrbolsbl "You should know I hate being put on the spot like this by now..."
            n 1ccsbolesisbl "..."
            n 2ccsfll "I swear,{w=0.2} [player].{w=0.75}{nw}"
            extend 2csrfll " You are {i}such{/i} a jerk sometimes."
            extend 2csqpol " You know that?"

        else:
            n 1uskeml "...!{w=0.5}{nw}"
            n 4fcsanl "Uuuuuuu-!"
            n 2fcseml "[player],{w=0.2} I swear..."
            n 2cslsll "You are {i}such{/i} a jerk sometimes.{w=0.75}{nw}"
            extend 2csqsll " Really.{w=1}{nw}"
            extend 1csrcal " I hate being put on the spot like this..."

    if already_celebrated_player_birthday:
        show natsuki 1csrbol
        menu:
            "Just returning the favor.":
                pass

        n 1unmemlesh "...!{w=0.5}{nw}"
        n 4csrbol "..."
        n 2ccseml "...Yeah,{w=0.2} yeah.{w=0.75}{nw}"
        extend 2nslpol " Wise-ass."
        n 2ccsfll "But come{w=0.5}{nw}"
        extend 2ccsgsl " on!{w=0.75}{nw}"
    
    else:
        n 2ccsfllsbl "...And come on now.{w=0.75}{nw}"

    extend 2cdwfllsbr " Seriously?{w=0.75}{nw}"
    extend 2cupajlsbr " You just {i}had{/i} to get the cake and everything else too?"
    n 2csrsllsbr "..."
    n 2csrpulsbr "...And now that I think about it..."
    n 4csqtrl "Where did you even {i}find{/i} all this?"

    if already_celebrated_player_birthday:
        n 2fsqcal "...And why does the cake look {i}exactly{/i} like the one I made you?"
        n 2csrcal "..."
        n 4csrajl "I'm...{w=0.75}{nw}"
        extend 4csrbolsbl " just gonna pretend I've never seen it before."
    
    else:
        n 4unmemlsbr "I-{w=0.2}it's not that I don't like it or anything!{w=0.75}{nw}"
        extend 2fcsemlsbr " It's perfectly fine!{w=1}{nw}"
        extend 2clrsll " But..."
        n 1csrbol "..."

    n 1cdwbol "..."
    n 2cslfll "...You're gonna make me do the whole wish thing.{w=0.75}{nw}"
    extend 2ksqsll " Aren't you?"
    
    $ jnPause(2)
    show prop cake lit zorder JN_PROP_ZORDER
    play audio necklace_clip
    show natsuki 2cslcal
    $ jnPause(3)

    menu:
        "Make a wish, [n_name]!":
            pass

    show natsuki 2csqcal
    $ jnPause(3)
    
    n 2clrsll "..."
    n 2ccspulesi "..."
    n 2cslpol "...Fine.{w=1}{nw}"

    if Natsuki.isLove(higher=True):
        extend 1ccscaf " B-{w=0.2}but only because it's you.{w=0.75}{nw}"
        extend 4csqcaf " Got it?"

    elif Natsuki.isEnamored(higher=True):
        extend 1ccsajl " B-{w=0.2}but only because you did all of...{w=1}{nw}"
        extend 4ksrcal " this."

    elif Natsuki.isAffectionate(higher=True):
        extend 1ccsajl " B-{w=0.2}but only because you put in the effort.{w=0.75}{nw}"
        extend 4csqcal " Got it?"
    
    else:
        extend 1ccsajl " But {i}only{/i} because I'd look like a total jerk otherwise.{w=0.75}{nw}"
        extend 4fsqcal " Capiche?"

    show natsuki 1ncsca
    $ jnPause(5)
    show natsuki 1ccsaj
    show prop cake unlit zorder JN_PROP_ZORDER
    play audio blow
    $ jnPause(0.5)
    show natsuki 1ccsbo
    $ jnPause(4)

    if Natsuki.isEnamored(higher=True):
        n 1ncsss "...Heh.{w=1.25}{nw}"
        extend 2clrsm " I can't even {i}remember{/i} the last time I got to do that."
        n 2clrsl "..."
        n 2clrpu "But...{w=1}{nw}"
        extend 2cnmpu " [player]?"
        n 1kslsll "..."
        n 1klrsll "...Thank you.{w=1}{nw}"
        extend 1kcsfll " F-{w=0.2}for all of..."
        extend 4cslfll " this."
        n 4ccsfll "It..."
        n 4ksrcalsbl "..."
        n 2ksrajlsbl "...Really means a lot."
        n 2ccsajlsbl "A-{w=0.2}and not just because of the flashy decorations,{w=0.2} or the dumb cake.{w=0.75}{nw}"
        extend 2cllsllsbl " I can live without those.{w=1.25}{nw}"
        extend 2cslbol " I {i}have{/i} lived without those."
        n 1ksrcal "...Probably more times than you'd think."
        n 4ccspu "It's just that..."
        n 4clrun "..."
        n 1clrpul "Nobody's...{w=1}{nw}"
        extend 1csrpul " ever...{w=1}{nw}"
        extend 1ccsunl " actually...{w=1}{nw}" 
        extend 2cslunl " tried this hard before."
        n 2kslsllsbr "...For me."
        n 4kslbolsbr "And I'd just be lying if I said I wasn't still trying to get used to it."
        n 1cnmemlsbr "I-{w=0.2}it's not like {i}nobody{/i} would have cared enough!{w=0.75}{nw}"
        extend 1clrfll " I know the others would have done {i}something{/i}.{w=0.75}{nw}"
        extend 4clrajl " Sayori,{w=0.2} Monika..."
        n 4csrfsl "Heh.{w=0.75}{nw}"
        extend 4ksrsll " Even Yuri.{w=1}{nw}"
        extend 2ksrpul " But..."
        n 2kcssllesi "..."
        n 2cllsl "...They're not here.{w=0.75}{nw}"
        extend 4kslsl " N-{w=0.2}not anymore."
        n 4knmsl "...And they never will be again."
        n 1klrpu "So that's why..."
        n 1klrbol "..."
        n 1ccsunl "So...{w=0.75}{nw}"
        extend 4cslemltsb " t-{w=0.2}that's..."
        n 4cslunltsb "..."
        n 4fcsunltsa "..."
        n 4fcsupltsa "S-{w=0.4}so that's why I..."
        n 1ccsunltsa "..."
        n 2ksrslltsb "..."
        n 2ncspulesi "..."
        $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 2kslsll "...Thanks,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
        extend 2knmsll " Really.{w=0.75}{nw}"
        extend 2klrssl " Even {i}if{/i} all of this is just through a screen?"
        n 4klrfsl "..."
        n 4ncsssl "...Heh."
        n 2kslfsl "It's still...{w=0.3} way more than I could have hoped for."

        $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
            poem_list=jn_poems.getAllPoems(),
            unlocked=False,
            holiday_types=[jn_events.JNHolidayTypes.natsuki_birthday],
            affinity=Natsuki._getAffinityState()
        )
        $ unlocked_poem_pool.sort(key = lambda poem: poem.affinity_range[0])
        $ birthday_poem = unlocked_poem_pool.pop() if len(unlocked_poem_pool) > 0 else None

        if birthday_poem:
            $ birthday_poem.unlock()
        
            n 1kslsll "..."
            n 4knmbol "...I ended up writing something,{w=0.2} you know."
            n 4klrbolsbr "..."
            n 2knmfllsbr "What?{w=0.75}{nw}"
            extend 2ccscalsbr " Don't give me that look.{w=1}{nw}"
            extend 2ccsfllsbr " I-{w=0.2}I {i}know{/i} you're not meant to give other people stuff on your birthday.{w=1}{nw}"
            extend 2cslcalsbr " {i}Obviously{/i}."
            n 2cllsllsbr "But..."
            n 1kllbol "..."
            n 4ccsajl "It doesn't matter."
            n 4cslcal "J-{w=0.2}just take it.{w=0.5}{nw}"
            extend 2ccscalsbl " Before I change my mind."

            show natsuki 2cllsrlsbl
            call show_poem(birthday_poem)
            $ jnPause(3)

            n 2cllbol "..."
            n 2cllajl "Hey..."
            n 2kllsll "...You did read that,{w=0.75}{nw}"
            extend 4knmbol " right?"
            n 4klrbol "Because...{w=1}{nw}"
            extend 2ksrfll " I really {b}did{/b} mean all that,{w=0.2} [player].{w=0.75}{nw}"
            extend 2knmbol " You should really know I do by now."
            n 2ccsfllsbr "I-{w=0.2}I might not be any taller."
            n 4kllbolsbr "But...{w=0.3} being here with you?"
            n 4ncsssl "Heh."
            n 1nsrfsf "...I like to think I grew anyway.{w=0.75}{nw}"
            extend 2ccssml " J-{w=0.2}just a little."

        n 4kslbol "..."
        n 4knmbol "...And [player]?"
        n 4klrbolsbl "..."
        show natsuki 1ccsbol

    else:
        if Natsuki.isAffectionate(higher=True):
            n 1nslss "...Heh.{w=0.75}{nw}"
            extend 2tsqbol " Happy now,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2clrfll " Sheesh..."
            n 2clrsl "..."
            n 2nlraj "But..."
            n 4ksrslsbl "..."
            
        else:
            n 2csqfll "...Happy now?{w=0.75}{nw}"
            extend 2cllfllsbr " Jeez..."
            n 2ccsposbr "If I {i}wanted{/i} to be embarrassed I would have just asked,{w=0.2} you know."
            n 2csrpo "..."
            n 2nsrbo "But..."
            n 4ksrslsbl "..."

        n 1ksrbolsbr "...Thanks.{w=1}{nw}"
        extend 4ccspulsbr " F-{w=0.2}for all of this,{w=0.2} I mean."
        n 4cllpul "It's just that..."
        n 1kllsll "..."
        n 1fcssll "It's...{w=0.75}{nw}"
        extend 4fcsunl " a lot{w=0.75}{nw}"
        extend 4ksrsll " to get used to.{w=1}{nw}"
        extend 4knmbol " Actually celebrating it with anyone."
        n 2kslcal "...Let alone anyone who actually {i}cares{/i}."
        n 2fcsgslsbl "N-{w=0.2}not like the others {i}wouldn't{/i} have done anything!"
        extend 2ccsflsbl " Of course they would!{w=0.75}{nw}"
        extend 4clrss " Sayori,{w=0.2} Monika..."
        n 4ccsss "Heh."
        extend 2cslfs " Even Yuri.{w=1}{nw}"
        extend 2kslbo " It's just..."
        n 4ccsunl "..."
        n 4ccsfll "It's...{w=0.75}{nw}"
        extend 4clrbol " not like they're gonna show up any time soon.{w=0.75}{nw}"
        extend 2ksrbol " E-{w=0.2}especially not now."
        n 2ksrsll "..."
        n 2fcsfllsbl "S-{w=0.2}so!{w=0.75}{nw}"
        extend 2fcsajlsbl " That's why..."
        n 2fcsunlsbl "T-{w=0.2}that's..."
        n 2kslunl "..."
        n 4ccsunl "It's..."
        n 4ccsflf "I-{w=0.2}it's just a good thing you showed up today!{w=1}{nw}"
        extend 2fcsfll " That's all I'm saying.{w=1}{nw}"
        extend 2nsrbol " So..."
        n 1ksrsll "...Yeah."
        n 1ksrbol "..."
        n 4ksqbol "...And [player]?"
        n 4cslunl "..."
        show natsuki 4ccsunf

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio glass_move
    hide prop
    hide confetti
    $ jnPause(2)
    play audio chair_out
    $ jnPause(3)
    play audio clothing_ruffle

    if Natsuki.isLove(higher=True):
        $ jnPause(1)
        n "...L-{w=0.2}love you."
        $ jnPause(3)
        play audio kiss
        $ jnPause(3)
        show natsuki 1nsrfsf
        $ jnPause(5)

    elif Natsuki.isEnamored(higher=True):
        show natsuki 1nsrbof
        $ jnPause(4)

    elif Natsuki.isAffectionate(higher=True):
        show natsuki 1csrbof
        $ jnPause(3)

    else:
        show natsuki 1csrunfsbr
        $ jnPause(3)

    $ jnPause(1.25)
    hide black with Dissolve(1.25)
    $ jnPause(3)
    
    $ gold_star_hairpin = jn_outfits.getWearable("jn_accessory_gold_star_hairpin")
    $ pink_star_hairpin = jn_outfits.getWearable("jn_accessory_pink_star_hairpin")
    
    if (
        persistent.jn_custom_outfits_unlocked 
        and (not gold_star_hairpin.unlocked or not pink_star_hairpin.unlocked)
    ):
        $ hairpin_to_gift = gold_star_hairpin if not gold_star_hairpin.unlocked else pink_star_hairpin
        $ hairpin_to_gift.unlock()
        n 2ksrbol "..."
        n 2nsrajl "So...{w=1}{nw}"
        extend 4tnmbol " what's...{w=0.5}{nw}"

        show natsuki 1tnmboltsbeqm
        $ jn_gifts.GIFT_BLUE.present()
        $ jnPause(0.5)
        show natsuki 4udwfll

        if Natsuki.isEnamored(higher=True):
            $ jnPause(3)
            n 4knmpul "...[player]...{w=1.25}{nw}"
            extend 2ksrpul " come on..."
            n 2knmsll "You haven't embarrassed me enough already?{w=0.75}{nw}"
            extend 2ksrpol " Man..."
            n 2cllsll "..."
            n 2kcspulesi "..."
            n 4kslbol "...Fine.{w=1}{nw}"
            extend 4nslsslsbr " I guess it's the least I could do,{w=0.2} huh?"
        
        else:
            $ jnPause(1.5)
            n 4unmfll "...!{w=0.5}{nw}"
            n 2fslunlsbr "..."
            n 2fsqunlsbr "T-{w=0.2}this better not be some kind of prank,{w=0.2} [player]."
            n 2nsrsllsbl "..."
            n 2ccsemlsbl "F-{w=0.2}fine."
            extend 4ksrbolsbr " I suppose it's the least I should do."
        
        show natsuki 4cdwbolsbr
        $ jn_gifts.GIFT_BLUE.open()
        $ jnPause(3)
        show natsuki 1udwfllsbr
        play audio gift_rustle
        $ jn_gifts.GIFT_BLUE.empty()
        $ jnPause(3)

        if Natsuki.isEnamored(higher=True):
            show natsuki 4ksrfsltsb

        else:
            show natsuki 4csrboltsb

        $ jnPause(3)
        play audio necklace_clip
        $ birthday_outfit.accessory = hairpin_to_gift
        $ jn_outfits.saveTemporaryOutfit(birthday_outfit)

        if Natsuki.isEnamored(higher=True):
            show natsuki 2ksrsml

        else:
            show natsuki 2nsrbol

        $ jnPause(3)
        
        if Natsuki.isEnamored(higher=True):
            n 2nsrssl "...Heh."
            n 4nsrfsl "It...{w=1}{nw}" 
            extend 1ksrfsl " really {i}does{/i} feel like my birthday now."
            $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove() else jn_utils.getRandomTease()
            n 1ksqbol "...Thanks,{w=0.2} [player].{w=0.75}{nw}"
            extend 1kllssl " It's..."
            n 2kslfslsbr "..."
            n 2kslssfsbr "...I-{w=0.2}I love it.{w=1}{nw}"
            extend 4kslfslsbr " T-{w=0.2}thank you.{w=1}{nw}" 
            extend 4cslsslsbr " You big dope."
            show natsuki 4cslsml

        else:
            n 2nsrbol "..."
            n 2nsrajlsbl "...I-{w=0.2}I guess that's one way to make it feel like a birthday.{w=0.75}{nw}"
            extend 2nsrsslsbl " Heh."
            n 4ksrbolsbl "..."
            n 4knmbolsbr "...Thanks,{w=0.2} [player].{w=1}{nw}"
            extend 4klrbolsbr " It's..."
            n 1ksrsllsbr "..."
            n 2ncssslsbr "...It's awesome.{w=1}{nw}"
            extend 2cslsslsbl " E-{w=0.2}even if it {i}did{/i} come from a dummy."
            show natsuki 2nslfsl

        $ jn_gifts.GIFT_BLUE.close()
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        $ jn_gifts.GIFT_BLUE.hide()
        hide black with Dissolve(1.5)
        $ jnPause(3)

    if Natsuki.isEnamored(higher=True):
        n 1nsrbol "..."
        n 1nsrssl "So..."
        $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 3tnmssl "What did you wanna do today,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3csldvlsbr " Ehehe..."

    elif Natsuki.isAffectionate(higher=True):
        n 2nsrbol "..."
        n 2nsrajl "So..."
        n 2ccssslsbr "W-{w=0.2}what's happening,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2cslsslsbr " Ehehe..."

    else:
        n 2nsrbol "..."
        n 2nsrajl "S-{w=0.2}so..."
        n 2ccssssbl "What else is new,{w=0.2} [player]?"

    $ persistent._jn_natsuki_birthday_known = True
    $ Natsuki.calculatedAffinityGain(base=2.5, bypass=True)
    $ jn_events.getHoliday("holiday_natsuki_birthday").complete()

    return

label holiday_player_birthday:
    python:
        import copy
        import datetime

        today_day_month = (datetime.date.today().day, datetime.date.today().month)

        # Give Natsuki a party hat, using whatever she's currently wearing as a base
        jn_outfits.getWearable("jn_headgear_classic_party_hat").unlock()
        birthday_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        birthday_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_classic_party_hat")
        birthday_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(birthday_hat_outfit)

        jn_events.getHoliday("holiday_player_birthday").run()
        player_name_capitalized = player.upper()

    n 1uchlgl "HAPPY BIRTHDAY,{w=0.2} [player_name_capitalized]!"

    if (
        persistent._jn_player_birthday_is_leap_day
        and today_day_month == (28, 2)
    ):
        # Actual birthday check already handled, so just need to check leap flag and day
        n 4nsldvlsbr "...Or close enough anyway this year,{w=0.2} right?"

    n 1fcsbg "Betcha' didn't think I had something planned all along,{w=0.2} did you?{w=0.5}{nw}"
    extend 1nchsml " Ehehe."
    n 1fnmaj "Don't lie!{w=1}{nw}"
    extend 4fchbl " I know I got you {i}real{/i} good this time."
    n 1ullss "Well,{w=0.2} whatever.{w=1}{nw}"
    extend 1tsqsm " We both know what {i}you're{/i} waiting for,{w=0.2} huh?"
    n 2fcsss "Yeah,{w=0.2} yeah.{w=0.5}{nw}"
    extend 2fchsm " I got you covered,{w=0.2} [player]."

    show prop cake lit zorder JN_PROP_ZORDER
    play audio necklace_clip

    n 1uchgn "Ta-{w=0.3}da!"
    $ jnPause(3)
    n 1fnmpu "..."
    n 1fbkwr "What?!{w=1}{nw}"
    extend 2fllpol " You don't {i}seriously{/i} expect me to sing all by myself?{w=1}{nw}"
    extend 2fcseml " No way!"
    n 2nlrpol "..."
    n 1nlrpu "But..."
    n 1nchbs "Yeah!{w=0.2} Here you go!{w=0.5}{nw}"
    extend 1nchsml " Ehehe."
    n 1tsqsm "So,{w=0.2} [player]?{w=1}{nw}"
    extend 1tsqss " Aren't you gonna make a wish?"
    n 4tlrpu "...Better come up with one soon,{w=0.2} actually.{w=1}{nw}"
    extend 4uskemlesh " I gotta put this out before the wax ruins all the icing!"
    n 2nllpo "..."
    n 1tsqpu "All set?{w=0.5}{nw}"
    extend 2fsrpo " About time.{w=1}{nw}"
    extend 1fchbg " Let's put these out already!"

    n 1ncsaj "...{w=0.5}{nw}"
    show prop cake unlit zorder JN_PROP_ZORDER
    play audio blow

    n 1nchsm "..."
    n 2tsgss "Well?{w=0.75}{nw}"
    extend 2tnmaj " What're you waiting for,{w=0.2} [player]?{w=1}{nw}"
    extend 2flrcal " Dig in already!"
    n 2nsqsll "Don't tell me I went all out on this for nothing."
    n 2fsqsr "..."
    n 1uskajesu "...Oh.{w=0.5}{nw}"
    extend 1fllssl " Ehehe.{w=1}{nw}"
    extend 1fslssl " Right."
    n 4flrssl "I...{w=1.5}{nw}"
    extend 4fsrdvl " kinda forgot about {i}that{/i} aspect."
    n 2fslpol "And I don't really feel like smearing cake all over your screen.{w=1}{nw}"
    extend 2ullaj " So..."
    n 1nsrss "I'm just gonna just save this for later."
    n 4fnmajl "Hey!{w=0.5}{nw}"
    extend 4fllbgl " It's the thought that counts,{w=0.2} right?"
    show natsuki 4fsldvl

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
            n 1knmpul "...I wrote you something too,{w=0.2} you know."
            n 2fcseml "I-{w=0.2}I know it's not some {i}fancy{/i} gift,{w=1}{nw}"
            extend 2klrsrl " but..."
            n 4fsrsrl "..."
            n 4fcsunl "Uuuuu..."
            n 1fcspul "Just...{w=1}{nw}"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 2klrpol " read it already,{w=0.2} [chosen_tease]."

        else:
            n 1fllunl "..."
            n 3fnmcal "I-{w=0.2}I hope you didn't think I'd just leave you with nothing."
            n 3nsrpol "I'm not {i}that{/i} much of a jerk."
            n 1nsrajl "So...{w=1}{nw}"
            extend 4fnmcal " here you go."
            n 1fcsemf "J-{w=0.2}just hurry up and read it.{w=1}{nw}"
            extend 2fslbof " I'm not gonna read it to you."

        call show_poem(birthday_poem)

        if Natsuki.isEnamored(higher=True):
            n 1knmbol "Hey...{w=1}{nw}"
            extend 1knmpul " you {i}did{/i} read it,{w=0.2} right?"
            n 2fslbol "I worked a lot on that,{w=0.2} you know."
            n 1fcseml "A-{w=0.2}and I meant every word,{w=1}{nw}"
            extend 4kllbof " so..."
            n 1klrssf "...Yeah."
            n 4flldvl "I'll..."
            extend 4fslssl " just put that poem back in my desk for now."

        else:
            n 1nsqpul "All done?{w=1}{nw}"
            extend 2fcseml " {i}Finally{/i}.{w=1}{nw}"
            extend 2fslcal " Jeez..."
            n 1fslunl "..."
            n 1fcsajl "I guess I'll just keep it in my desk for now.{w=1}{nw}"
            extend 4fsrssl " I-{w=0.2}in case you wanted to reference my writing skills later,{w=0.2} {i}obviously{/i}."

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    if Natsuki.isLove(higher=True):
        n 1klrssl "And...{w=1.5}{nw}"
        extend 4knmsml " [player]?"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        play audio kiss
        $ jnPause(0.25)
        hide black with Dissolve(1.25)

        n 4kwmssf "H-{w=0.2}happy birthday.{w=1}{nw}"
        extend 1kchsmf " Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 4kwmssf "H-{w=0.2}happy birthday."

    else:
        n 1fcsbgf "You're welcome!"

    if birthday_poem:
        $ birthday_poem.unlock()

    $ jn_events.getHoliday("holiday_player_birthday").complete()

    return

label holiday_anniversary:
    #TODO: writing
    $ jn_events.getHoliday("holiday_anniversary").run()
    $ jn_events.getHoliday("holiday_anniversary").complete()

    return
