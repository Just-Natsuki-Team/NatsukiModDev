init python in jn_idles:
    import datetime
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils
    
    __ALL_IDLES = {}

    _last_idle_label = None

    def selectIdle():
        """
        Picks and returns a single random idle, or None if no idles are available.
        The same idle cannot be returned two times in a row.
        """
        global _last_idle_label
        not_label = [_last_idle_label] if _last_idle_label is not None else []

        idle_list = JNIdle.filterIdles(
            idle_list=getAllIdles(),
            affinity=store.Natsuki._getAffinityState(),
            not_label=not_label
        )
        return_idle = random.choice(idle_list).label if len(idle_list) > 0 else None
        _last_idle_label = return_idle

        return return_idle

    def getAllIdles():
        """
        Returns a list of all idles.
        """
        return __ALL_IDLES.values()

    class JNIdleTypes(Enum):
        reading = 1
        gaming = 2
        resting = 3
        vibing = 4
        working = 5

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
            not_label=None
        ):
            """
            Returns True if the idle meets the filter criteria, otherwise False.

            IN:
                - affinity - The affinity the idle must match in its affinity_range.
                - not_label - List of labels the idle must not match

            OUT:
                - True if all filter criteria has been passed; otherwise False.
            """
            if affinity is not None and not self.__currAffinityInAffinityRange(affinity):
                return False

            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False

            elif not_label is not None and self.label in not_label:
                return False

            return True

        @staticmethod
        def filterIdles(
            idle_list,
            affinity=None,
            not_label=None
        ):
            """
            Returns a filtered list of idles, given an idle list and filter criteria.

            IN:
                - affinity - The affinity the idle must match in its affinity_range.
                - not_label - List of labels the idle must not match

            OUT:
                - list of idles matching the search criteria
            """
            return [
                _idle
                for _idle in idle_list
                if _idle.__filterIdle(
                    affinity,
                    not_label
                )
            ]

    def __registerIdle(idle):
        """
        Registers a new idle in the list of idles, allowing it to be selected randomly between topics.
        
        IN:
            - idle - JNIdle to register.
        """
        if idle.label in __ALL_IDLES:
            jn_utils.log("Cannot register idle name: {0}, as an idle with that name already exists.".format(idle.label))

        else:
            __ALL_IDLES[idle.label] = idle

    def _concludeIdle():
        """
        Wraps up an idle by setting the last idle call time and jumping to the talk menu.
        This is necessary as we can't call the menu and then return like a topic.
        """
        store.LAST_IDLE_CALL = datetime.datetime.now()
        renpy.jump("talk_menu")

    __registerIdle(JNIdle(
        label="idle_twitch_playing",
        idle_type=JNIdleTypes.gaming,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional=(
            "get_topic('event_wintendo_twitch_battery_dead').shown_count > 0"
            " or get_topic('event_wintendo_twitch_game_over').shown_count > 0"
        )
    ))

    __registerIdle(JNIdle(
        label="idle_reading_parfait_girls",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_caught_reading_manga').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_reading_renpy_for_dummies",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_renpy_for_dummies').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_reading_a_la_mode",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional="get_topic('event_reading_a_la_mode').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_reading_step_by_step",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        conditional="get_topic('event_step_by_step_manga').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_naptime",
        idle_type=JNIdleTypes.resting,
        affinity_range=(jn_affinity.AFFECTIONATE, None)
    ))

    __registerIdle(JNIdle(
        label="idle_daydreaming",
        idle_type=JNIdleTypes.resting,
        affinity_range=(jn_affinity.NORMAL, None)
    ))

    __registerIdle(JNIdle(
        label="idle_poetry_attempts",
        idle_type=JNIdleTypes.working,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_caught_writing_poetry').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_vibing_headphones",
        idle_type=JNIdleTypes.vibing,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional="persistent.jn_custom_music_unlocked"
    ))

    __registerIdle(JNIdle(
        label="idle_whistling",
        idle_type=JNIdleTypes.vibing,
        affinity_range=(jn_affinity.NORMAL, None)
    ))

    __registerIdle(JNIdle(
        label="idle_laptop",
        idle_type=JNIdleTypes.gaming,
        affinity_range=(jn_affinity.HAPPY, None)
    ))

    __registerIdle(JNIdle(
        label="idle_math_attempts",
        idle_type=JNIdleTypes.working,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('talk_favorite_subject').shown_count > 0"
    ))

    __registerIdle(JNIdle(
        label="idle_plantcare",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        conditional="jn_desk_items.getDeskItem('jn_sanjo').unlocked"
    ))

label idle_twitch_playing:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop wintendo_twitch_playing free zorder JN_PROP_ZORDER
    show natsuki gaming
    hide black with Dissolve(0.5)
    $ jnPause(0.5)
    $ jnClickToContinue(silent=False)

    n 1tnmpueqm "...?{w=1}{nw}"
    show prop wintendo_twitch_held free
    n 1unmflesu "Oh!{w=1}{nw}"
    extend 1fchbgsbr " What's up,{w=0.2} [player]?"

    if random.choice([True, False]):
        n 1fllsssbr "Just gotta save real quick..."
    
    else:
        n 1fsrsssbr "Just give me a second here..."

    show natsuki gaming
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_parfait_girls:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_parfait_manga_closed":
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_parfait_manga_held"))
    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    n 1tlrbo "...{w=1}{nw}"
    n 1tnmboeqm "...?{w=1}{nw}"
    n 1unmflesu "Oh!{w=0.75}{nw}"
    extend 1fchbgsbl " Hey!"

    if random.choice([True, False]):
        n 1fslsssbl "Let me just bookmark this real quick..."
    
    else:
        n 1fcssssbl "Just gotta find a good stopping point here..."

    show natsuki reading
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)

    if random.choice([True, False]):
        play audio drawer
        $ jnPause(1.3)
    
    else:
        play audio book_closing
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_parfait_manga_closed"))
        $ jnPause(0.3)

    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_renpy_for_dummies:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.left) == "jn_renpy_for_dummies_closed":
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.left)

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_held"))
    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    n 1fdwbo "...{w=1}{nw}"
    n 1tnmboeqm "...?{w=1}{nw}"
    n 1unmflesu "Oh!{w=0.75}{nw}"
    extend 1nlrsssbr " Hey.{w=1}{nw}"
    extend 1nsrsssbr " Just let me finish up here real quick."

    if random.choice([True, False]):
        n 1nsrbosbr "..."
        n 1nnmaj "...And no.{w=1}{nw}" 
        extend 1fslpo " The book still sucks."

    else:
        n 1fcsflsbr "None of this crap was making any sense,{w=0.2} a-{w=0.2}anyway."

    show natsuki 1fcspo
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fcssmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)

    if random.choice([True, False]):
        play audio drawer
        $ jnPause(1.3)
    
    else:
        play audio book_closing
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_closed"))
        $ jnPause(0.3)

    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_a_la_mode:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop a_la_mode_manga_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ Natsuki.setIsReadingToRight(False)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1unmaj "Ah!{w=1}{nw}"
        extend 1unmbg " [player]!{w=1}{nw}"
        extend 1fcsbg " Perfect timing."
        n 1fsqsm "I {i}juuuust{/i} finished that chapter~.{w=1.25}{nw}"
        extend 1fchsm " Ehehe."

    else:
        n 1tnmpu "Huh?{w=1}{nw}"
        extend 1unmajl " Oh!{w=0.75}{nw}"
        extend 1nlrsslsbl " Heh."
        n 1nsrsssbl "I...{w=1}{nw}"
        extend 1nslsssbl " kinda got distracted.{w=0.75}{nw}"
        extend 1fspgs " But man,{w=0.2} this is a good read!"
        n 1fcsbg "You have no {w=0.3}{i}idea{/i}{w=0.3} what you're missing out on,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fsqsm " Ehehe."

    show natsuki 1fcssm
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_step_by_step:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop step_by_step_manga_held zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ Natsuki.setIsReadingToRight(False)
    $ jnClickToContinue(silent=False)

    n 1tnmpu "Eh?{w=1.25}{nw}"
    extend 1unmfllesu " Oh!{w=0.75}{nw}"
    extend 1ullfllsbl " [player]!"

    if random.choice([True, False]):
        n 1nslbolsbl "..."
        n 1nslajl "Just...{w=1}{nw}"
        extend 1nslssl " give me a sec.{w=1}{nw}"
        extend 1nsrcal " I was only just getting into that..."

    else:
        n 1fcsbglsbr "W-{w=0.2}what's up?{w=1}{nw}"
        extend 1nsrsslsbr " I'll just...{w=1}{nw}" 
        extend 1nsrcal " bookmark this real quick."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_naptime:
    $ jn_globals.force_quit_enabled = False
    show natsuki sleeping
    $ jnPause(7.1)
    $ jnClickToContinue(silent=False)
    
    n 3kcsslesl "...Mmmnnn...{w=2}{nw}"
    n 3kwlpuesl "...Nnnn?{w=1}{nw}"
    extend 3ksqpul " Wha...?{w=2}{nw}"
    n 3unmpulesu "...!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    $ jn_globals.force_quit_enabled = True
    n 4unmfllsbr "[player_initial]-[player]!{w=1}{nw}"
    extend 4nsrunlsbr " Jeez..."
    n 2nsrpol "What's up?"

    $ jn_idles._concludeIdle()

label idle_daydreaming:
    show natsuki thinking
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 3flrpu "...{w=1.5}{nw}"
        n 3tnmpueqm "...?{w=1}{nw}"
        n 4unmfleex "Oh!{w=0.75}{nw}"
        extend 4fllsslsbr " H-{w=0.2}hey."
        n 2fcsajlsbr "I-{w=0.2}I {i}totally{/i} wasn't spacing out or anything like that.{w=1}{nw}"
        extend 2fsrposbr " In case you were wondering."
        n 1fcsajsbr "A-{w=0.2}anyway."

    else:
        n 3tlrca "...{w=1.5}{nw}"
        n 3tnmpueqm "Huh?{w=1}{nw}"
        extend 4unmemeex " Oh!{w=1}{nw}"
        extend 4nllfllsbr " [player]."
        n 2fcspolsbr "Y-{w=0.2}you should {i}really{/i} know better than to interrupt someone thinking,{w=0.75}{nw}"
        extend 2flrposbr " you know."
        n 2fcsajsbr "Anyhow..."

    $ jn_idles._concludeIdle()

label idle_poetry_attempts:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop poetry_attempt zorder JN_PROP_ZORDER
    show natsuki working_on_papers
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=1.25}{nw}"
        n 1unmajesu "Oh!{w=0.75}{nw}"
        extend 1fchbgsbl " Hey,{w=0.2} [player]."
        n 1tnmsm "..."
        n 1tnmpu "...What?{w=0.75}{nw}"
        extend 1klrflsbl " What's that look for,{w=0.5}{nw}" 
        extend 1knmbosbl " all of a sudden?"
        n 1udwfll "..."
        n 1udwemleex "A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1flremlsbl " T-{w=0.2}this?{w=0.75}{nw}"
        extend 1fcsemlsbl " It's nothing!{w=1}{nw}"
        extend 1fcscalsbl " N-{w=0.2}nothing at all."

    else:
        n 1tlrca "...{w=1.25}{nw}"
        n 1tnmcaeqm "...?{w=0.75}{nw}"
        n 1unmeml "A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1ulreml " [player]!"
        n 1fcsajlsbr "J-{w=0.2}just a second!{w=1}{nw}"
        extend 1fsrcalsbr " Jeez..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1nsrcasbl
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_vibing_headphones:
    python:
        import copy

        outfit_to_restore = jn_outfits.getOutfit(Natsuki.getOutfitName())
        headphones = jn_outfits.getWearable("jn_headgear_cat_headphones")
        if not headphones.unlocked:
            headphones.unlock()

        headphones_outfit = copy.copy(outfit_to_restore)
        headphones_outfit.headgear = headphones

    show natsuki 1ncsca
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show prop music_notes zorder JN_PROP_ZORDER
    $ jn_outfits.saveTemporaryOutfit(headphones_outfit)
    show natsuki vibing
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 4tslboeqm "...{w=1}{nw}"
        n 4tnmboeqm "...?{w=0.75}{nw}"
        hide prop
        n 1unmfllesh "O-{w=0.2}oh!{w=0.75}{nw}"
        extend 1flrsslsbl " [player]!{w=0.75}{nw}"
        extend 2fsrdvlsbl " Heh."
        n 2fcsfllsbl "J-{w=0.2}just give me a second here."

    else:
        n 1tsqcaeqm "...?{w=1}{nw}"
        n 1uskemlesh "...!{w=0.75}{nw}"
        hide prop
        $ player_initial = jn_utils.getPlayerInitial()
        n 4fbkwrl "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 4fnmemlsbr " How long have you just been {i}sitting there{/i}?!{w=1.25}{nw}"
        extend 2fslfllsbr " Jeez..."
        n 2fcsposbr "At {i}least{/i} let me put these on charge first..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ jnPause(1.3)
    $ Natsuki.setOutfit(outfit_to_restore)
    show natsuki 2nsrcasbl
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_whistling:
    show natsuki whistling
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=0.75}{nw}"
        n 4unmfllesh "O-{w=0.2}oh!{w=0.75}{nw}"
        extend 4cllssl " H-{w=0.2}hey [player]."
        n 4tnmbo "What's up?"

    else:
        n 4tllbo "...{w=0.75}{nw}"
        n 4tnmboeqm "...?{w=0.75}{nw}"
        n 4unmfllesh "A-{w=0.2}ah!{w=0.75}{nw}"
        extend 2nlrsslsbl " Heh.{w=0.75}{nw}"
        extend 2nllbolsbl " Hey."
        n 2tnmbo "What's happening,{w=0.2} [player]?"

    $ jn_idles._concludeIdle()

label idle_laptop:
    show natsuki 4udwbo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if random.choice([True, False]):
        show natsuki reading

    else:
        show natsuki gaming

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_laptop"))
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 4tdwbo "...{w=0.75}{nw}"
        n 4tnmfleqm "Eh?{w=0.75}{nw}"
        n 4unmaj "Oh.{w=0.75}{nw}"
        extend 4ulraj " Hey [player].{w=0.75}{nw}"
        extend 4cllsssbl " Let me just finish up here real quick..."
        show natsuki gaming

    else:
        n 4cdwpu "...{w=0.75}{nw}"
        n 4cnmpueqm "...?{w=0.75}{nw}"
        n 4unmfllesh "Huh?{w=0.75}{nw}"
        extend 4unmgslesh " O-{w=0.2}oh!{w=0.75}{nw}"
        extend 4fllbglsbr " [player]!"
        n 4cslsssbr "Heh."
        n 4ccsajsbr "I...{w=1}{nw}"
        extend 4clrcasbr " kinda got distracted.{w=0.75}{nw}"
        extend 4ccstrsbr " J-{w=0.2}just give me a sec to power down,{w=0.2} alright?"
        show natsuki 4ccscasbr

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio laptop_close
    $ jnPause(0.75)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    $ jnPause(1.3)
    show natsuki 3ullbo
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_math_attempts:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop math_attempt zorder JN_PROP_ZORDER
    show natsuki working_on_papers
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=1.25}{nw}"
        n 1uwdajesu "Oh!{w=0.75}{nw}"
        extend 1fchbgsbl " H-{w=0.2}hey [player]."
        n 2fslsssbl "I-{w=0.2}I was just..."
        n 2fslunsbl "..."
        n 2ccsfl "Ugh.{w=0.5} Nevermind.{w=0.75}{nw}"
        extend 2fcsposbr " Math is such a dumb subject anyway."

    else:
        n 1tlrca "...{w=1.25}{nw}"
        n 1tnmcaeqm "...?{w=0.75}{nw}"
        n 1uwdwrlesh "A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1cdrbol " [player]!"
        n 2fcsajlsbr "Y-{w=0.2}you {i}seriously{/i} need to learn how to speak up!{w=0.75}{nw}"
        extend 2fcsfllsbr " Yeesh..."
        n 2cslbosbr "At least let me clean up this mess..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 4nsrbosbl
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_plantcare:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_sanjo"))
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_plant_care_book_held"))
    $ Natsuki.setIsReadingToRight(True)
    show prop watering_can zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)
    $ dialogue_choice = random.randint(1, 3)

    if dialogue_choice == 1:
        n 1cdwbo "...{w=0.75}{nw}"
        n 1tnmboeqm "...?{w=0.75}{nw}"
        n 1uwdflesu "Oh!{w=0.75}{nw}"
        extend 1fllbgsbr " H-{w=0.2}hey,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fchbgsbr " What's happening?"
        n 1unmaj "Let me just finish up here real quick.{w=0.75}{nw}"
        extend 1ccsss " Besides."
        n 1cdltr "I gotta do right by Sanjo after all,{w=0.5}{nw}" 
        extend 1fcscaesi " you know."
        show natsuki 1fcsca

    elif dialogue_choice == 2:
        n 1clrpu "...{w=0.75}{nw}"
        n 1tnmpu "...Huh?{w=0.75}{nw}"
        n 1unmpuesu "Oh!{w=0.75}{nw}"
        extend 1cllsssbr " Heh.{w=0.75}{nw}"
        extend 1ccssssbr " What's up,{w=0.2} [player]?"
        n 1clraj "Just give me a minute.{w=0.75}{nw}"
        extend 1nsrpo " I was getting tired of all the plant mumbo-jumbo anyway."
        show natsuki 1ccspo

    else:
        n 1cdwpu "...{w=0.75}{nw}"
        n 1cnmpueqm "Eh?{w=0.75}{nw}"
        extend 1unmaj " Oh.{w=0.75}{nw}"
        extend 1ullbo " Hey,{w=0.2} [player]."
        n 1clrss "Don't mind me.{w=0.75}{nw}"
        extend 1fcsss " Don't mind me at all."
        n 1fcssmesm "Juuuust making sure I'm keeping Sanjo here in tip-top shape!"
        show natsuki 1fchsmeme

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()
