default persistent.jn_natsuki_current_pose = "sitting"
default persistent.jn_natsuki_current_outfit = "uniform"
default persistent.jn_natsuki_current_hairstyle = "default"
default persistent.jn_natsuki_current_accessory = "hairbands/red"
default persistent.jn_natsuki_current_eyewear = None

init python in jn_outfits:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.utils as utils

    current_outfit_name = None

    class Outfit():
        """
        Describes a complete outfit for Natsuki to wear; including clothing, hairstyle, etc.
        """
        def __init__(
            self,
            name,
            unlocked,
            clothes,
            hairstyle,
            accessory,
            eyewear
        ):
            self.name = name
            self.unlocked = unlocked
            self.clothes = clothes
            self.hairstyle = hairstyle
            self.accessory = accessory
            self.eyewear = eyewear

    # Default outfits
    DEFAULT_OUTFIT_UNIFORM = Outfit(
        name="School uniform",
        unlocked=True,
        clothes="uniform",
        hairstyle="default",
        accessory="hairbands/red",
        eyewear=None
    )

    DEFAULT_OUTFIT_CASUAL_WEEKDAY = Outfit(
        name="Casual clothes",
        unlocked=True,
        clothes="casual",
        hairstyle="default",
        accessory="hairbands/red",
        eyewear=None
    )

    DEFAULT_OUTFIT_CASUAL_WEEKEND = Outfit(
        name="Casual clothes",
        unlocked=True,
        clothes="casual",
        hairstyle="bun",
        accessory="hairbands/white",
        eyewear=None
    )

    DEFAULT_OUTFIT_MORNING = Outfit(
        name="Pyjamas, night",
        unlocked=True,
        clothes="star_pajamas",
        hairstyle="bedhead",
        accessory="hairbands/red",
        eyewear=None
    )

    DEFAULT_OUTFIT_NIGHT = Outfit(
        name="Pyjamas, day",
        unlocked=True,
        clothes="star_pajamas",
        hairstyle="down",
        accessory="hairbands/red",
        eyewear=None
    )

    # Default outfit schedules
    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_MORNING,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_CASUAL_WEEKDAY,
        utils.TIME_BLOCK_NIGHT: DEFAULT_OUTFIT_NIGHT
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_MORNING,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_MORNING,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_MORNING,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_NIGHT:DEFAULT_OUTFIT_NIGHT
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_CASUAL_WEEKDAY,
        utils.TIME_BLOCK_NIGHT: DEFAULT_OUTFIT_CASUAL_WEEKDAY
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_NIGHT: DEFAULT_OUTFIT_CASUAL_WEEKEND
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_UNIFORM,
        utils.TIME_BLOCK_NIGHT: DEFAULT_OUTFIT_UNIFORM
    }

    DEFAULT_OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY = {
        utils.TIME_BLOCK_EARLY_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_MID_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_LATE_MORNING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_AFTERNOON: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_EVENING: DEFAULT_OUTFIT_CASUAL_WEEKEND,
        utils.TIME_BLOCK_NIGHT: DEFAULT_OUTFIT_CASUAL_WEEKEND
    }

    def set_outfit(outfit):
        """
        Sets Natsuki's appearance using the given outfit.
        """
        global current_outfit_name
        
        if not isinstance(outfit, Outfit):
            raise Exception("Outfit given is not an Outfit-class object")
            return

        if outfit.clothes is None:
            raise Exception("Outfit clothing cannot be None")
            return

        if outfit.hairstyle is None:
            raise Exception("Outfit hairstyle cannot be None")
            return

        if outfit.unlocked:
            store.persistent.jn_natsuki_current_outfit = outfit.clothes
            store.persistent.jn_natsuki_current_hairstyle = outfit.hairstyle
            store.persistent.jn_natsuki_current_accessory = outfit.accessory
            store.persistent.jn_natsuki_current_eyewear = outfit.eyewear
            current_outfit_name = outfit.name

        else:
            utils.log("Cannot dress Natsuki in outfit {0}; outfit is locked".format(outfit.name))

    def get_outfit_for_time_block():
        """
        Returns the outfit corresponding to affinity, the current time block and whether or not is is a weekday.
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            if utils.get_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY.get(utils.get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY.get(utils.get_current_time_block())
        
        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            if utils.get_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY.get(utils.get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY.get(utils.get_current_time_block())
        
        else:
            if utils.get_is_weekday():
                return DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY.get(utils.get_current_time_block())

            else:
                return DEFAULT_OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY.get(utils.get_current_time_block())

    def set_outfit_for_time_block():
        """
        Sets Natsuki's outfit based on the time of day, whether it is a weekday/weekend, and affinity.
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            if utils.get_is_weekday():
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY.get(utils.get_current_time_block()))

            else:
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY.get(utils.get_current_time_block()))
        
        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            if utils.get_is_weekday():
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY.get(utils.get_current_time_block()))

            else:
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY.get(utils.get_current_time_block()))
        
        else:
            if utils.get_is_weekday():
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY.get(utils.get_current_time_block()))

            else:
                set_outfit(DEFAULT_OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY.get(utils.get_current_time_block()))
            
label outfits_time_of_day_change:
    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1uchbg "Oh!{w=0.2} I gotta change,{w=0.1} just give me a sec..."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1unmpu "Oh!{w=0.2} I should probably change,{w=0.1} one second..."
        n 1flrpol "A-{w=0.1}and no peeking,{w=0.1} got it?!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1unmpu "Oh -{w=0.1} I gotta get changed.{w=0.2} I'll be back in a sec."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nnmsl "Back in a second."

    else:
        n 1fsqsl "I'm changing."

    play audio drawer
    with Fade(out_time=0.5, hold_time=1, in_time=0.5, color="#181212")
    $ renpy.pause(delay=0.33, hard=True)
    $ jn_outfits.set_outfit_for_time_block()

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        n 1uchgn "Ta-da!{w=0.2} There we go!{w=0.2} Ehehe."

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        n 1nchbg "Okaaay!{w=0.2} I'm back!"

    elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
        n 1nnmsm "And...{w=0.3} all done."

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1nllsl "I'm back."

    else:
        n 1fsqsl "..."

    return
