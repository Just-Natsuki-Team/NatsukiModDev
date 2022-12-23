default persistent.jn_poem_list = dict()

image paper default = "mod_assets/poems/default.png"
image paper pink_floral = "mod_assets/poems/pink_floral.png"
image paper festive = "mod_assets/poems/festive.png"

init python in jn_poems:
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    __ALL_POEMS = {}

    class JNPoem:
        """
        Describes a poem object that players can unlock and read.
        """
        def __init__(
            self,
            reference_name,
            display_name,
            holiday_type,
            affinity_range,
            poem,
            paper="default",
            font_size=28,
            text_align=0.0
        ):
            """
            Constructor.

            IN:
                reference_name - The name used to uniquely identify this poem and refer to it internally
                display_name - The name displayed to the user
                holiday_type - The JNHoliday type associated with this player, allowing a poem to be associated with a holiday
                affinity_range - The affinity range that must be satisfied for this holiday to be picked when filtering
                poem - The actual poem content
                paper - The paper image that is associated with this poem. Defaults to a standard notepad page
                font_size - The int font size for the main body of the poem. Must be within a range of 16-28.
                text_align - The decimal alignment for the main body of the poem, where:
                    0.0: LEFT
                    0.5: CENTRE
                    1.0: RIGHT
            """
            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = False
            self.holiday_type = holiday_type
            self.affinity_range = affinity_range
            self.poem = poem
            self.paper = paper
            self.font_size = font_size if 16 <= font_size <= 24 else 24 
            self.text_align = text_align if text_align in (0.0, 0.5, 1.0) else 0.0

        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each poem from the persistent.
            """
            global __ALL_POEMS
            for poem in __ALL_POEMS.itervalues():
                poem.__load()

        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each poem to the persistent.
            """
            global __ALL_POEMS
            for poem in __ALL_POEMS.itervalues():
                poem.__save()

        @staticmethod
        def filterPoems(
            poem_list,
            unlocked=None,
            reference_name=None,
            holiday_types=None,
            affinity=None
        ):
            """
            Returns a filtered list of poems, given an poem list and filter criteria.

            IN:
                - poem_list - the list of JNpoem child poems to query. Defaults to all poems
                - unlocked - the boolean unlocked state to filter for
                - reference_name - list of reference_names the poem must have 
                - holiday_types - list of the JNHolidayTypes the poem must be in
                - affinity - minimum affinity state the poem must have

            OUT:
                - list of poems matching the search criteria
            """
            return [
                _poem
                for _poem in poem_list
                if _poem.__filterPoem(
                    unlocked,
                    reference_name,
                    holiday_types,
                    affinity
                )
            ]

        def asDict(self):
            """
            Exports a dict representation of this poem; this is for data we want to persist.

            OUT:
                dictionary representation of the poem object
            """
            return {
                "unlocked": self.unlocked
            }

        def currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this poem's affinity_range

            IN:
                affinity_state - Affinity state to test if the poems can be shown in. If None, the current affinity state is used.
                    (Default: None)
            OUT:
                True if the current affinity is within range. False otherwise
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()

            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)

        def lock(self):
            """
            Locks this poem, making it unavailable to the player.
            """
            self.unlocked = False
            self.__save()

        def unlock(self):
            """
            Unlocks this poem, making it available to the player.
            """
            self.unlocked = True
            self.__save()

        def __load(self):
            """
            Loads the persisted data for this poem from the persistent.
            """
            if store.persistent.jn_poem_list[self.reference_name]:
                self.unlocked = store.persistent.jn_poem_list[self.reference_name]["unlocked"]

        def __save(self):
            """
            Saves the persistable data for this poem to the persistent.
            """
            store.persistent.jn_poem_list[self.reference_name] = self.asDict()

        def __filterPoem(
            self,
            unlocked=None,
            reference_name=None,
            holiday_types=None,
            affinity=None
        ):
            """
            Returns True, if the poem meets the filter criteria. Otherwise False.

            IN:
                - poem_list - the list of JNpoem child poems to query
                - unlocked - the boolean unlocked state to filter for
                - reference_name - list of reference_names the poem must have 
                - holiday_types - list of the JNHolidayTypes the poem must be in
                - affinity - minimum affinity state the poem must have

            OUT:
                - True, if the poem meets the filter criteria. Otherwise False
            """
            if unlocked is not None and self.unlocked != unlocked:
                return False

            elif reference_name is not None and not self.reference_name in reference_name:
                return False

            elif holiday_types is not None and not self.holiday_type in holiday_types:
                return False

            elif affinity and not self.currAffinityInAffinityRange(affinity):
                return False

            return True

    def __registerPoem(poem):
        """
        Registers a new poem in the list of all poems, allowing in-game access and persistency.
        If the poem has no existing corresponding persistent entry, it is saved.

        IN:
            - poem - the JNPoem to register.
        """
        if poem.reference_name in __ALL_POEMS:
            jn_utils.log("Cannot register poem name: {0}, as an poem with that name already exists.".format(poem.reference_name))

        else:
            __ALL_POEMS[poem.reference_name] = poem
            if poem.reference_name not in store.persistent.jn_poem_list:
                poem.__save()

    def getPoem(poem_name):
        """
        Returns the poem for the given name, if it exists.

        IN:
            - poem_name - str poem name to fetch

        OUT: Corresponding JNPoem if the poem exists, otherwise None 
        """
        if poem_name in __ALL_POEMS:
            return __ALL_POEMS[poem_name]

        return None

    def getAllPoems():
        """
        Returns a list of all poems.
        """
        return __ALL_POEMS.itervalues()

    __registerPoem(JNPoem(
        reference_name="jn_birthday_cakes_candles",
        display_name="Cakes and Candles",
        holiday_type=jn_events.JNHolidayTypes.player_birthday,
        affinity_range=(jn_affinity.HAPPY, None),
        poem=(
            "Another cake, another candle\n"
            "Another year that you've just handled\n"
            "Some people dread this special day\n"
            "And push the thought so far away\n"
            "But I don't think it's bad!\n"
            "\n"
            "Another gift, another guest\n"
            "Another year you've tried your best\n"
            "Some people cherish this special day\n"
            "Talk, dance, party and play\n"
            "How could you think that's sad?\n"
            "\n"
            "No more doubts, no more fears\n"
            "Ignore the numbers, forget the years\n"
            "This poem is your birthday cheers\n"
            "\n"
            "Now grab yourself a plate!\n"
        ),
        paper="pink_floral"
    ))

    __registerPoem(JNPoem(
        reference_name="jn_christmas_evergreen",
        display_name="Evergreen",
        holiday_type=jn_events.JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.ENAMORED, None),
        poem=(
            "It's\n" 
            "Chilly and\n" 
            "Cold outside\n" 
            "But warm inside\n" 
            "With you by my side.\n" 
            "Listening to the cozy fire\n" 
            "Sitting side by side together.\n" 
            "Talking to one another, making\n" 
            "New memories that shine brightly.\n" 
            "Illuminating even the darkest of nights\n" 
            "To allow weary travelers a guiding light\n" 
            "A star guided path ahead in a stressful life.\n" 
            "Previous troubles melt away in the hot cocoa\n" 
            "That I hold tight as I tease you to find your own.\n" 
            "Was always my favorite, but now, so more than ever\n" 
            "As it tastes more sweet with new and fresh ingredients.\n" 
            "The warmth I feel inside will outlast any amount of winter\n" 
            "Because with you by my side\n" 
            "I'm always ready for another.\n" 
        ),
        paper="festive",
        font_size=18,
        text_align=0.5
    ))

    __registerPoem(JNPoem(
        reference_name="jn_christmas_gingerbread_house",
        display_name="Gingerbread House",
        holiday_type=jn_events.JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.HAPPY, None),
        poem=(
            "From a brittle gingerbread household Amy came\n"
            "Disguised by colorful icing and confectionaries\n" 
            "One that hid the shouts and all the arguments\n"
            "One that hid in plain sight, opposed to spotlight\n"
            "\n"
            "But where we come from doesn't define\n"
            "Who we truly are deep on the inside\n"
            "And sometimes all it takes is someone.\n"
            "Someone new to remind you of more.\n"
            "\n"
            "A new friend to help decorate a tree.\n"
            "An evergreen free for decoration\n"
            "Eagerly awaiting two people\n"
            "To coat it with ornaments and lights.\n"
            "\n"
            "That tree a template of what's to come\n"
            "A place where new memories can form\n"
            "Where gingerbread can appear brittle\n"
            "Without needing to lie, with honesty.\n"
            "\n"
            "Being welcomed without all the bells and whistles\n"
            "As acceptance provides warmth in the coldest of winters\n"
        ),
        paper="festive",
        font_size=20
    ))

label show_poem(poem):
    play audio page_turn
    show screen poem_view(poem)
    with Dissolve(1)
    $ renpy.pause(hard=True)
    $ renpy.pause(2)
    return

screen poem_view(poem):
    vbox:
        xalign 0.5
        add "paper [poem.paper]"

    # Scrolling poem view
    viewport id "poem_viewport":
        child_size (710, None)
        xysize(600,600)
        mousewheel True
        draggable True
        xanchor 0
        ypos 100
        xpos 360
        has vbox
        text "[poem.display_name]" style "poem_title" text_align 0.5
        null height 50
        hbox:
            xsize 600
            box_wrap True
            null height 60
            text "[poem.poem]" style "poem_text" size poem.font_size text_align poem.text_align
            null height 50

    vbar value YScrollValue(viewport="poem_viewport") style "poem_vbar"

    # Menu
    vbox:
        xpos 1056
        ypos 10
        textbutton _("Done"):
            style "hkbd_button"
            action [
                Hide(
                    screen="poem_view",
                    transition=Dissolve(1)
                ),
                Return()
            ]

style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    ysize 700

style poem_title:
    font "mod_assets/fonts/natsuki.ttf"
    size 30
    color "#000"
    outlines []
    line_leading 5
    xalign 0.5

style poem_text:
    font "mod_assets/fonts/natsuki.ttf"
    color "#000"
    outlines []
    xalign 0.5
    line_leading 5
