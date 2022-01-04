# Sky types for the classroom
image sky_day overcast = "mod_assets/backgrounds/classroom/sky_day_overcast.png"
image sky_day rain = "mod_assets/backgrounds/classroom/sky_day_rain.png"
image sky_day sunny = "mod_assets/backgrounds/classroom/sky_day_sunny.png"
image sky_day thunder = "mod_assets/backgrounds/classroom/sky_day_thunder.png"

# Dimming effects; used with various weather conditions
image dim light = "mod_assets/backgrounds/classroom/dim_light.png"
image dim medium = "mod_assets/backgrounds/classroom/dim_medium.png"
image dim heavy = "mod_assets/backgrounds/classroom/dim_heavy.png"

# Transitions
define natsuki_desk_move_transition = MoveTransition(0.1)
define weather_change_transition = Dissolve(1.5)
define dim_change_transition = Dissolve(0.25)

init 0 python in jn_atmosphere:
    import random
    import store

    # Draw Z indexes
    _DIM_Z_INDEX = 1
    _SKY_Z_INDEX = 0

    # Weather types when calling show_sky
    WEATHER_OVERCAST = 1
    WEATHER_RAIN = 2
    WEATHER_SUNNY = 3
    WEATHER_THUNDER = 4

    # Maps a sky type to a given vignette/dimming effect
    _SKY_AND_DIM_MAP = {
        "sky_day overcast" : "dim light",
        "sky_day rain" : "dim medium",
        "sky_day sunny" : None,
        "sky_day thunder" : "dim heavy"
    }

    _MUFFLED_RAIN_PATH = "mod_assets/sfx/rain_muffled.mp3"

    def show_random_sky():
        """
        Shows a randomised sky placeholder with associated dimming effect.
        """

        # Select the sky and dimming effect
        sky, dim = random.choice(list(_SKY_AND_DIM_MAP.items()))

        # Show the sky
        renpy.show(name=sky, zorder=_SKY_Z_INDEX)
        renpy.with_statement(trans=store.weather_change_transition)

        # Add the dimming effect matching the sky, if it exists
        if dim:
            renpy.show(name=dim, zorder=_DIM_Z_INDEX)
            renpy.with_statement(trans=store.dim_change_transition)

        # Play rain sfx if the chosen weather is rainy
        if sky in ("rain", "thunder"):
            renpy.music.play(filenames=_MUFFLED_RAIN_PATH, channel="weather_loop", fadein=3.0)

    def show_sky(weather_type):
        """
        Shows the specified sky placeholder with associated dimming effect.

        IN:
            weather_type - int; WEATHER_OVERCAST, WEATHER_RAIN, WEATHER_THUNDER or WEATHER_SUNNY
        """
        if weather_type == WEATHER_OVERCAST:
            sky = "sky_day overcast"
            dim = "dim light"
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        elif weather_type == WEATHER_RAIN:
            sky = "sky_day rain"
            dim = "dim medium"
            renpy.music.play(filenames=_MUFFLED_RAIN_PATH, channel="weather_loop", fadein=3.0)

        elif weather_type == WEATHER_THUNDER:
            sky = "sky_day thunder"
            dim = "dim heavy"
            renpy.music.play(filenames=_MUFFLED_RAIN_PATH, channel="weather_loop", fadein=3.0)

        else:
            sky = "sky_day sunny"
            dim = None
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        renpy.show(name=sky, zorder=_SKY_Z_INDEX)
        renpy.with_statement(trans=store.weather_change_transition)

        if dim:
            renpy.show(name=dim, zorder=_DIM_Z_INDEX)
            renpy.with_statement(trans=store.dim_change_transition)
