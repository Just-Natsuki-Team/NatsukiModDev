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

    def set_outfit(outfit):
        """
        Sets Natsuki's appearance using the given outfit.
        """
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

        else:
            utils.log("Cannot dress Natsuki in outfit {0}; outfit is locked".format(outfit.name))

    def _set_outfit_for_time_of_day_low_affinity():
        """
        Sets Natsuki's outfit based on whether today is a weekday or the weekend.
        """
        # Weekdays
        if utils.get_is_weekday():
            set_outfit(DEFAULT_OUTFIT_UNIFORM)

        # Weekends
        else:
            set_outfit(DEFAULT_OUTFIT_CASUAL_WEEKDAY)

    def _set_outfit_for_time_of_day_medium_affinity():
        """
        Sets Natsuki's outfit based on the time of day (limited), and whether today is a weekday or the weekend.
        """
        # Weekdays
        if utils.get_is_weekday():
            # Evening Natsuki
            if utils.get_current_time_block() in (utils.TIME_BLOCK_EVENING, utils.TIME_BLOCK_NIGHT):
                set_outfit(DEFAULT_OUTFIT_CASUAL_WEEKDAY)

            # Schoolday Natsuki
            else:
                set_outfit(DEFAULT_OUTFIT_UNIFORM)

        # Weekends
        else:
            set_outfit(DEFAULT_OUTFIT_CASUAL_WEEKEND)

    def _set_outfit_for_time_of_day_high_affinity():
        """
        Sets Natsuki's outfit based on the time of day and whether today is a weekday or the weekend.
        """
        # Weekdays
        if utils.get_is_weekday():
            # Morning Natsuki
            if utils.get_current_time_block() in (utils.TIME_BLOCK_EARLY_MORNING, utils.TIME_BLOCK_MID_MORNING):
                set_outfit(DEFAULT_OUTFIT_MORNING)

            # Schoolday Natsuki
            elif utils.get_current_time_block() in (utils.TIME_BLOCK_LATE_MORNING, utils.TIME_BLOCK_AFTERNOON):
                set_outfit(DEFAULT_OUTFIT_UNIFORM)

            # Evening Natsuki
            elif utils.get_current_time_block() == utils.TIME_BLOCK_EVENING:
                set_outfit(DEFAULT_OUTFIT_CASUAL_WEEKDAY)

            # Night Natsuki
            else:
                set_outfit(DEFAULT_OUTFIT_NIGHT)
        
        # Weekends
        else:
            # Morning Natsuki
            if utils.get_current_time_block() in (
                utils.TIME_BLOCK_EARLY_MORNING,
                utils.TIME_BLOCK_MID_MORNING,
                utils.TIME_BLOCK_LATE_MORNING):
                set_outfit(DEFAULT_OUTFIT_MORNING)

            # Day Natsuki
            elif utils.get_current_time_block() == utils.TIME_BLOCK_AFTERNOON:
                if config.developer and random.choice(range(11)) == 10:
                    set_outfit(DEFAULT_OUTFIT_QEEB)

                else:
                    set_outfit(DEFAULT_OUTFIT_CASUAL_WEEKEND)

            # Night Natsuki
            else:
                set_outfit(DEFAULT_OUTFIT_NIGHT)

    def set_outfit_for_time_of_day():
        """
        Sets Natsuki's outfit based on the time of day, whether it is a weekday/weekend, and affinity.
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            _set_outfit_for_time_of_day_high_affinity()
        
        elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
            _set_outfit_for_time_of_day_medium_affinity()
        
        else:
            _set_outfit_for_time_of_day_low_affinity()

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
