# Natsuki's placeholder sprites; we use these in leiu of a full sprite system for now
image placeholder_natsuki boast = "mod_assets/natsuki/placeholder_boast.png"
image placeholder_natsuki neutral = "mod_assets/natsuki/placeholder_neutral.png"
image placeholder_natsuki plead = "mod_assets/natsuki/placeholder_plead.png"
image placeholder_natsuki pleased = "mod_assets/natsuki/placeholder_pleased.png"
image placeholder_natsuki sad = "mod_assets/natsuki/placeholder_sad.png"
image placeholder_natsuki shy = "mod_assets/natsuki/placeholder_shy.png"
image placeholder_natsuki smile = "mod_assets/natsuki/placeholder_smile.png"
image placeholder_natsuki smug = "mod_assets/natsuki/placeholder_smug.png"
image placeholder_natsuki sparkle = "mod_assets/natsuki/placeholder_sparkle.png"
image placeholder_natsuki tease = "mod_assets/natsuki/placeholder_tease.png"
image placeholder_natsuki unamused = "mod_assets/natsuki/placeholder_unamused.png"
image placeholder_natsuki wink = "mod_assets/natsuki/placeholder_wink.png"

image placeholder_hairclip rabbit = "mod_assets/natsuki/accessories/placeholder_rabbit_hairclip.png"

# Placeholder sky types for the classroom
image placeholder_sky_day overcast = "mod_assets/backgrounds/classroom/placeholder_sky_day_overcast.png"
image placeholder_sky_day rain = "mod_assets/backgrounds/classroom/placeholder_sky_day_rain.png"
image placeholder_sky_day sunny = "mod_assets/backgrounds/classroom/placeholder_sky_day_sunny.png"
image placeholder_sky_day thunder = "mod_assets/backgrounds/classroom/placeholder_sky_day_thunder.png"

# Placeholder vignettes; used with various weather conditions
image placeholder_dim light = "mod_assets/backgrounds/classroom/placeholder_dim_light.png"
image placeholder_dim medium = "mod_assets/backgrounds/classroom/placeholder_dim_medium.png"
image placeholder_dim heavy = "mod_assets/backgrounds/classroom/placeholder_dim_heavy.png"

define natsuki_desk_move_transition = MoveTransition(0.1)
define weather_change_transition = Dissolve(1.5)
define dim_change_transition = Dissolve(0.25)

init 0 python in jn_placeholders:
    import random
    import store

    # Draw Z indexes for main placeholders
    NATSUKI_Z_INDEX = 3
    DIM_Z_INDEX = 1
    SKY_Z_INDEX = 0

    # Weather types when calling show_placeholder_sky
    WEATHER_OVERCAST = 1
    WEATHER_RAIN = 2
    WEATHER_SUNNY = 3
    WEATHER_THUNDER = 4

    ALL_PLACEHOLDER_NATSUKI_SPRITES = {
        "placeholder_natsuki boast",
        "placeholder_natsuki neutral",
        "placeholder_natsuki plead",
        "placeholder_natsuki pleased",
        "placeholder_natsuki sad",
        "placeholder_natsuki shy",
        "placeholder_natsuki smile",
        "placeholder_natsuki smug",
        "placeholder_natsuki sparkle",
        "placeholder_natsuki tease",
        "placeholder_natsuki unamused",
        "placeholder_natsuki wink"
    }

    _PLACEHOLDER_SKY_AND_DIM_MAP = {
        "placeholder_sky_day overcast" : "placeholder_dim light",
        "placeholder_sky_day rain" : "placeholder_dim medium",
        "placeholder_sky_day sunny" : None,
        "placeholder_sky_day thunder" : "placeholder_dim heavy"
    }

    def show_greeting_placeholder_natsuki():
        """
        Shows a resting Natsuki placeholder sprite based on current affinity.
        """
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            renpy.show(name="placeholder_natsuki smile", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.natsuki_desk_move_transition)

        elif store.jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            renpy.show(name="placeholder_natsuki neutral", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.natsuki_desk_move_transition)

        elif store.jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            renpy.show(name="placeholder_natsuki unamused", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.natsuki_desk_move_transition)

        else:
            renpy.show(name="placeholder_natsuki sad", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.natsuki_desk_move_transition)

    def show_resting_placeholder_natsuki(offset=False):
        """
        Shows the default resting Natsuki placeholder sprite, changing based on affinity level.

        IN:
            offset - Whether Natsuki should be drawn off to the left to account for menus, etc.

        """
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            if offset:
                renpy.show(name="placeholder_natsuki neutral", at_list=[store.left], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.natsuki_desk_move_transition)

            else:
                renpy.show(name="placeholder_natsuki neutral", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.natsuki_desk_move_transition)

        else:
            if offset:
                renpy.show(name="placeholder_natsuki sad", at_list=[store.left], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.natsuki_desk_move_transition)

            else:
                renpy.show(name="placeholder_natsuki sad", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.natsuki_desk_move_transition)

    def show_random_placeholder_sky():
        """
        Shows a randomised sky placeholder with associated dimming effect.
        """
        
        # Select the sky and dimming effect
        sky, dim = random.choice(list(_PLACEHOLDER_SKY_AND_DIM_MAP.items()))

        # Show the sky
        renpy.show(name=sky, zorder=SKY_Z_INDEX)
        renpy.with_statement(trans=store.weather_change_transition)

        # Add the dimming effect matching the sky, if it exists
        if dim:
            renpy.show(name=dim, zorder=DIM_Z_INDEX)
            renpy.with_statement(trans=store.dim_change_transition)

    def show_placeholder_sky(weather_type):
        """
        Shows the specified sky placeholder with associated dimming effect.

        IN:
            weather_type - int; WEATHER_OVERCAST, WEATHER_RAIN, WEATHER_THUNDER or WEATHER_SUNNY
        """
        if (isinstance(weather_type, int)):
            if weather_type == WEATHER_OVERCAST:
                renpy.show(name="placeholder_sky_day overcast", zorder=SKY_Z_INDEX)
                renpy.with_statement(trans=store.weather_change_transition)

                renpy.show(name="placeholder_dim light", zorder=DIM_Z_INDEX)
                renpy.with_statement(trans=store.dim_change_transition)

            elif weather_type == WEATHER_RAIN:
                renpy.show(name="placeholder_sky_day rain", zorder=SKY_Z_INDEX)
                renpy.with_statement(trans=store.weather_change_transition)

                renpy.show(name="placeholder_dim medium", zorder=DIM_Z_INDEX)
                renpy.with_statement(trans=store.dim_change_transition)

            elif weather_type == WEATHER_THUNDER:
                renpy.show(name="placeholder_sky_day thunder", zorder=SKY_Z_INDEX)
                renpy.with_statement(trans=store.weather_change_transition)

                renpy.show(name="placeholder_dim heavy", zorder=DIM_Z_INDEX)
                renpy.with_statement(trans=store.dim_change_transition)

            else:
                renpy.show(name="placeholder_sky_day sunny", zorder=SKY_Z_INDEX)
                renpy.with_statement(trans=store.weather_change_transition)
                renpy.hide(name="placeholder_dim")
        
        else:
            raise Exception("Supplied param weather_type {weather_type} is not a valid type.".format(weather_type))
