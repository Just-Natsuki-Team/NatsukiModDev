init python in jn_idles:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils
    
    __ALL_IDLES = {}

    def selectIdle():
        """
        Picks and returns a single random idle, or None if no idles are available.
        """
        idle_list = JNIdle.filterIdles(
            idle_list=getAllIdles(),
            affinity=store.Natsuki._getAffinityState()
        )
        return random.choice(idle_list).label if len(idle_list) > 0 else None

    def getAllIdles():
        """
        Returns a list of all idles.
        """
        return __ALL_IDLES.values()

    class JNIdleTypes(Enum):
        reading = 1
        gaming = 2
        resting = 3

    class JNIdle:
        """
        Describes an idle that Natsuki can initiate in the gaps between topics randomly.
        """
        def __init__(
            self,
            label,
            idle_type,
            affinity_range=None,
            conditional=None
        ):
            """
            Constructor.

            IN:
                - label - The name used to uniquely identify this idle and refer to it internally
                - idle_type - The category of the idle
                - affinity_range - The affinity range that must be satisfied for this idle to be picked when filtering
                - conditional - Python statement that must evaluate to True for this idle to be picked when filtering
            """
            self.label = label
            self.idle_type = idle_type
            self.affinity_range = affinity_range
            self.conditional = conditional

        def __currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this idle's affinity_range.

            IN:
                - affinity_state - Affinity state to test if the holidays can be shown in. If None, the current affinity state is used.
            
            OUT:
                - True if the current affinity is within range; otherwise False.
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()

            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)

        def __filterIdle(
            self,
            affinity=None,
            conditional=None
        ):
            """
            Returns True if the idle meets the filter criteria, otherwise False.

            IN:
                - affinity - The affinity the idle must match in its affinity_range.

            OUT:
                - True if all filter criteria has been passed; otherwise False.
            """
            if affinity is not None and not self.__currAffinityInAffinityRange(affinity):
                return False

            elif conditional is not None and not eval(self.conditional, globals=store.__dict__):
                return False

            return True

        @staticmethod
        def filterIdles(
            idle_list,
            affinity
        ):
            """
            Returns a filtered list of idles, given an idle list and filter criteria.

            IN:
                - affinity - minimum affinity state the idle must have

            OUT:
                - list of idles matching the search criteria
            """
            return [
                _idle
                for _idle in idle_list
                if _idle.__filterIdle(
                    affinity
                )
            ]

    def __registerIdle(idle):
        if idle.label in __ALL_IDLES:
            jn_utils.log("Cannot register idle name: {0}, as an idle with that name already exists.".format(idle.label))

        else:
            __ALL_IDLES[idle.label] = idle
    
    __registerIdle(JNIdle(
        label="idle_twitch_playing",
        idle_type=JNIdleTypes.gaming,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional=(
            """get_topic("talk_thoughts_on_vegetarianism").shown_count > 0"""
            """ or get_topic("talk_thoughts_on_vegetarianism").shown_count > 0"""
        )
    ))

    __registerIdle(JNIdle(
        label="idle_reading_parfait_girls",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="""get_topic("event_caught_reading_manga").shown_count > 0"""
    ))

    __registerIdle(JNIdle(
        label="idle_reading_renpy_for_dummies",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="""get_topic("event_renpy_for_dummies").shown_count > 0"""
    ))

    __registerIdle(JNIdle(
        label="idle_reading_a_la_mode",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional="""get_topic("event_reading_a_la_mode").shown_count > 0"""
    ))

    __registerIdle(JNIdle(
        label="idle_reading_step_by_step",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        conditional="""get_topic("event_step_by_step_manga").shown_count > 0"""
    ))

    __registerIdle(JNIdle(
        label="idle_naptime",
        idle_type=JNIdleTypes.resting,
        affinity_range=(jn_affinity.AFFECTIONATE, None)
    ))

label idle_twitch_playing:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop wintendo_twitch_playing free zorder JN_PROP_ZORDER
    show natsuki gaming
    hide black with Dissolve(0.5)
    $ jnPause(0.5)
    $ jnClickToContinue()

    n 1tnmpueqm "...?{w=1}{nw}"
    show prop wintendo_twitch_held free
    n 1unmflesu "Oh!{w=1}{nw}"
    extend 1fchbgsbr " What's up,{w=0.2} [player]?"
    n 1fsrsssbr "Just give me a second here..."

    show natsuki gaming
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    jump talk_menu

label idle_reading_parfait_girls:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop parfait_manga_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue()

    n 1tlrbo "...{w=1}{nw}"
    n 1tnmboeqm "...?{w=1}{nw}"
    n 1unmflesu "Oh!{w=0.75}{nw}"
    extend 1fchbgsbl " Hey!"
    n 1fslsssbl "Let me just bookmark this real quick..."

    show natsuki reading
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    jump talk_menu

label idle_reading_renpy_for_dummies:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop renpy_for_dummies_book_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue()

    # TODO: writing

    show natsuki reading
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    jump talk_menu

label idle_reading_a_la_mode:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop a_la_mode_manga_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue()

    # TODO: writing

    show natsuki reading
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    jump talk_menu

label idle_reading_step_by_step:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop step_by_step_manga_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue()

    # TODO: writing

    show natsuki reading
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    jump talk_menu

label idle_naptime:
    $ jn_globals.force_quit_enabled = False
    show natsuki sleeping
    $ jnPause(7.1)
    $ jnClickToContinue()
    
    n 3kcsslesl "...Mmmnnn...{w=2}{nw}"
    n 3kwlpuesl "...Nnnn?{w=1}{nw}"
    extend 3ksqpul " Wha...?{w=2}{nw}"
    n 3unmpulesu "...!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    $ jn_globals.force_quit_enabled = True
    n 4unmfllsbr "[player_initial]-[player]!{w=1}{nw}"
    extend 4nsrunlsbr " Jeez..."
    n 2nsrpol "What's up?"

    jump talk_menu
