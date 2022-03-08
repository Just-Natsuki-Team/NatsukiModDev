
default persistent.jn_natsuki_auto_outfit_change_enabled = True
default persistent.jn_outfits_list = {}

init python in jn_outfits:
    import json
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_utils as jn_utils

    _use_alt_outfit = random.choice(range(1, 3)) == 1

    class JNOutfit():
        """
        Describes a complete outfit for Natsuki to wear; including clothing, hairstyle, etc.
        At minimum, an outfit must consist of clothes and a hairstyle
        """
        def __init__(
            self,
            display_name,
            reference_name,
            select_quote,
            unlocked,
            selectable,
            clothes,
            hairstyle,
            accessory=None,
            eyewear=None,
            headgear=None,
            necklace=None
        ):
            if clothes is None:
                raise TypeError("Outfit clothing cannot be None")
                return

            if hairstyle is None:
                raise TypeError("Outfit hairstyle cannot be None")
                return

            self.display_name = display_name
            self.reference_name = reference_name
            self.select_quote = select_quote
            self.unlocked = unlocked
            self.selectable = selectable
            self.clothes = clothes
            self.hairstyle = hairstyle
            self.accessory = accessory
            self.eyewear = eyewear
            self.headgear = headgear
            self.necklace = necklace

        @classmethod
        def from_json(self, json):
            return JNOutfit(
                display_name=json["display_name"],
                reference_name=json["reference_name"],
                select_quote=json["select_quote"],
                unlocked=json["unlocked"],
                selectable=json["selectable"],
                clothes=json["clothes"],
                hairstyle=json["hairstyle"],
                accessory=json["accessory"],
                eyewear=json["eyewear"],
                headgear=json["headgear"],
                necklace=json["necklace"]
            )

        @staticmethod
        def load_all():
            """
            Loads all outfits from the persistent.
            """
            global ALL_OUTFITS
            ALL_OUTFITS = []
            for outfit in store.persistent.jn_outfits_list.itervalues():
                ALL_OUTFITS.append(JNOutfit.from_json(json.loads(outfit)))

        @staticmethod
        def save_all():
            """
            Saves all outfits to the persistent.
            """
            global ALL_OUTFITS
            for outfit in ALL_OUTFITS:
                outfit.__save()

        def as_dict(self):
            """
            Exports a dict representation of this outfit.

            OUT:
                dictionary representation of the outfit object
            """
            return {
                key:value
                for key, value in self.__dict__.iteritems()
            }

        def to_json(self):
            """
            Returns this outfit as a JSON object.

            OUT:
                - JSON string representing this outfit
            """
            return json.dumps(self.__dict__)

        def __save(self):
            """
            Saves this outfit to the persistent.
            """
            store.persistent.jn_outfits_list[self.reference_name] = self.to_json()

    # Default outfits
    DEFAULT_OUTFIT_UNIFORM = JNOutfit(
        display_name="School uniform",
        reference_name="jn_school_uniform",
        select_quote="Still fits, alright!",
        unlocked=True,
        selectable=True,
        clothes="uniform",
        hairstyle="default",
        accessory="hairbands/red"
    )

    DEFAULT_OUTFIT_CASUAL_WEEKDAY = JNOutfit(
        display_name="Casual clothes",
        reference_name="jn_casual_weekday",
        select_quote="Can't complain!",
        unlocked=True,
        selectable=True,
        clothes="casual",
        hairstyle="default",
        accessory="hairbands/red"
    )

    DEFAULT_OUTFIT_CASUAL_WEEKDAY_ALT = JNOutfit(
        display_name="Casual clothes",
        reference_name="jn_casual_weekday_alt",
        select_quote="Can't complain!",
        unlocked=True,
        selectable=True,
        clothes="casual",
        hairstyle="ponytail",
        accessory="hairbands/white"
    )

    DEFAULT_OUTFIT_CASUAL_WEEKEND = JNOutfit(
        display_name="Casual clothes",
        reference_name="jn_casual_weekend",
        select_quote="Can't complain!",
        unlocked=True,
        selectable=True,
        clothes="casual",
        hairstyle="bun",
        accessory="hairbands/red"
    )

    DEFAULT_OUTFIT_CASUAL_WEEKEND_ALT = JNOutfit(
        display_name="Casual clothes",
        reference_name="jn_casual_weekend_alt",
        select_quote="Can't complain!",
        unlocked=True,
        selectable=True,
        clothes="casual",
        hairstyle="messy_bun",
        accessory="hairbands/white"
    )

    DEFAULT_OUTFIT_NIGHT = JNOutfit(
        display_name="Pyjamas",
        reference_name="jn_pajamas_night",
        select_quote="Super comfy!",
        unlocked=True,
        selectable=True,
        clothes="star_pajamas",
        hairstyle="down",
        accessory="hairbands/red"
    )

    DEFAULT_OUTFIT_MORNING = JNOutfit(
        display_name="Pyjamas",
        reference_name="jn_pajamas_morning",
        select_quote="Super comfy!",
        unlocked=True,
        selectable=True,
        clothes="star_pajamas",
        hairstyle="bedhead",
        accessory="hairbands/red"
    )

    DEFAULT_OUTFIT_MORNING_ALT = JNOutfit(
        display_name="Pyjamas",
        reference_name="jn_pajamas_morning_alt",
        select_quote="Super comfy!",
        unlocked=True,
        selectable=True,
        clothes="star_pajamas",
        hairstyle="bedhead",
        accessory="hairbands/green"
    )

    DEFAULT_OUTFIT_CHRISTMAS = JNOutfit(
        display_name="Natsu claus outfit",
        reference_name="jn_natsu_claus",
        select_quote="You better watch out...",
        unlocked=False,
        selectable=False,
        clothes="casual",
        hairstyle="down",
        accessory="hairbands/green",
        headgear="natsu_claus_hat"
    )

    DEFAULT_OUTFIT_VALENTINE = JNOutfit(
        display_name="Valentine dress",
        reference_name="jn_valentine",
        select_quote="Am I stylish or what? Ehehe...",
        unlocked=False,
        selectable=False,
        clothes="red_rose_lace_dress",
        hairstyle="messy_bun",
        accessory="hairbands/white"
    )

    ALL_OUTFITS = []

    # Default outfit schedules
    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_MORNING_ALT if _use_alt_outfit else DEFAULT_OUTFIT_MORNING,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_CASUAL_WEEKDAY_ALT if _use_alt_outfit else DEFAULT_OUTFIT_CASUAL_WEEKDAY,
        store.JNTimeBlocks.night: DEFAULT_OUTFIT_NIGHT
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_MORNING_ALT if _use_alt_outfit else DEFAULT_OUTFIT_MORNING,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_MORNING_ALT if _use_alt_outfit else DEFAULT_OUTFIT_MORNING,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_MORNING_ALT if _use_alt_outfit else DEFAULT_OUTFIT_MORNING,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_CASUAL_WEEKEND_ALT if _use_alt_outfit else DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_CASUAL_WEEKEND_ALT if _use_alt_outfit else DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.night:DEFAULT_OUTFIT_NIGHT
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_CASUAL_WEEKDAY,
        store.JNTimeBlocks.night: DEFAULT_OUTFIT_CASUAL_WEEKDAY
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.night: DEFAULT_OUTFIT_CASUAL_WEEKEND
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_UNIFORM,
        store.JNTimeBlocks.night: DEFAULT_OUTFIT_UNIFORM
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY = {
        store.JNTimeBlocks.early_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.mid_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.late_morning: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.afternoon: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.evening: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        store.JNTimeBlocks.night: DEFAULT_OUTFIT_CASUAL_WEEKEND
    }

    def get_outfit_for_time_block():
        """
        Returns the outfit corresponding to affinity, the current time block and whether or not is is a weekday.
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            if store.jn_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY.get(store.jn_get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY.get(store.jn_get_current_time_block())
        
        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            if store.jn_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY.get(store.jn_get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY.get(store.jn_get_current_time_block())
        
        else:
            if store.jn_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY.get(store.jn_get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY.get(store.jn_get_current_time_block())

    def register_outfit(outfit):
        """
        Registers a new outfit in the list of all outfits, allowing it to be referred to in-game and later saved to persistent.
        IN:
            - outfit - the JNOutfit to register.
        """
        for registered_outfit in ALL_OUTFITS:
            if registered_outfit.reference_name == outfit.reference_name:
                jn_utils.log("Cannot register outfit name: {0}, as an outfit with that name already exists.".format(outfit.reference_name))
                return

        ALL_OUTFITS.append(outfit)

    if len(store.persistent.jn_outfits_list) == 0:
        register_outfit(DEFAULT_OUTFIT_UNIFORM)
        register_outfit(DEFAULT_OUTFIT_CASUAL_WEEKDAY)
        register_outfit(DEFAULT_OUTFIT_NIGHT)
        JNOutfit.save_all()

label outfits_time_of_day_change:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1uchbg "Oh!{w=0.2} I gotta change,{w=0.1} just give me a sec...{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1unmpu "Oh!{w=0.2} I should probably change,{w=0.1} one second..."
        n 1flrpol "A-{w=0.1}and no peeking,{w=0.1} got it?!{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmpu "Oh -{w=0.1} I gotta get changed.{w=0.2} I'll be back in a sec.{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmsl "Back in a second.{w=0.75}{nw}"

    else:
        n 1fsqsl "I'm changing.{w=0.75}{nw}"

    play audio clothing_ruffle
    $ JN_NATSUKI.set_outfit(jn_outfits.get_outfit_for_time_block())
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")
    
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1uchgn "Ta-da!{w=0.2} There we go!{w=0.2} Ehehe.{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1nchbg "Okaaay!{w=0.2} I'm back!{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1nnmsm "And...{w=0.3} all done.{w=0.75}{nw}"

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nllsl "I'm back.{w=0.75}{nw}"

    else:
        n 1fsqsl "...{w=0.75}{nw}"

    show natsuki idle
    return

label outfits_wear_outfit:
    n 1unmaj "Huh? You want me to put on another outfit?"
    n 1fchbg "Sure thing!"
    extend 1unmbg " What do you want me to wear?"
    show natsuki idle at jn_left

    python:
        available_outfits = []
        for outfit in jn_outfits.ALL_OUTFITS:
            if outfit.unlocked and outfit.selectable:
                available_outfits.append([outfit.display_name, outfit])
        available_outfits.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(available_outfits, ("Nevermind.", None))
    show natsuki at jn_center

    if isinstance(_return, jn_outfits.JNOutfit):
        n 1unmaj "Oh? You want me to wear my [_return.display_name]?"
        extend 1uchbg " Gotcha!"
        n 1nchsm "Just give me a second..."

        play audio clothing_ruffle
        $ JN_NATSUKI.set_outfit(_return)
        with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

        n 1nchbg "Okaaay!"
        n 1tnmsm "How do I look, [player]?"
        extend 1flldvl " Ehehe."

    else:
        n 1nnmbo "Oh."
        extend 1nllaj " Well, that's fine."
        n 1nsrpol "I didn't wanna change anyway."

    return

label outfits_suggest_outfit:

    return

label outfits_remove_outfit:

    return