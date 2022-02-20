# Sky types for the classroom
image sky_day overcast = "mod_assets/backgrounds/classroom/sky_day_overcast.png"
image sky_day rain = "mod_assets/backgrounds/classroom/sky_day_rain.png"
image sky_day sunny = "mod_assets/backgrounds/classroom/sky_day_sunny.png"
image sky_day thunder = "mod_assets/backgrounds/classroom/sky_day_thunder.png"

# Dimming effects; used with various weather conditions
image dim light = "mod_assets/backgrounds/classroom/dim_light.png"
image dim medium = "mod_assets/backgrounds/classroom/dim_medium.png"
image dim heavy = "mod_assets/backgrounds/classroom/dim_heavy.png"

# Glitch effects
image glitch_garbled_a = "mod_assets/backgrounds/etc/glitch_garbled_a.png"
image glitch_garbled_b = "mod_assets/backgrounds/etc/glitch_garbled_b.png"
image glitch_garbled_c = "mod_assets/backgrounds/etc/glitch_garbled_c.png"
image glitch_garbled_red = "mod_assets/backgrounds/etc/glitch_garbled_red.png"

image glitch_fuzzy:
    "mod_assets/backgrounds/etc/glitch_fuzzy_a.png"
    pause 0.25
    "mod_assets/backgrounds/etc/glitch_fuzzy_b.png"
    pause 0.25
    "mod_assets/backgrounds/etc/glitch_fuzzy_c.png"
    pause 0.25
    repeat

# Transitions
define natsuki_desk_move_transition = MoveTransition(0.1)
define weather_change_transition = Dissolve(1.5)
define dim_change_transition = Dissolve(0.25)

init 0 python in jn_atmosphere:
    from Enum import Enum
    import random
    import store

    # Draw Z indexes
    _DIM_Z_INDEX = 1
    _SKY_Z_INDEX = 0

    class JNWeatherTypes(Enum):
        overcast = 1
        rain = 2
        sunny = 3
        thunder = 4
        glitch = 5

    # Maps a sky type to a given vignette/dimming effect
    __WEATHER_EFFECT_MAP = {
        JNWeatherTypes.overcast: ("sky_day overcast", "dim light"),
        JNWeatherTypes.rain: ("sky_day rain", "dim medium"),
        JNWeatherTypes.sunny: ("sky_day sunny", None),
        JNWeatherTypes.thunder: ("sky_day thunder", "dim heavy"),
        JNWeatherTypes.glitch: ("glitch_fuzzy", None)
    }

    __MUFFLED_RAIN_PATH = "mod_assets/sfx/rain_muffled.mp3"

    current_weather = None

    def show_current_sky(with_transition=True):
        """
        Shows the sky based on the sunrise/sunset times specified under the persistent.

        IN:
            with_transition - If True, will visually fade in the new weather
        """
        if (store.jn_get_current_hour() > store.persistent.jn_sunrise_hour 
            and store.jn_get_current_hour() <= store.persistent.jn_sunset_hour ):
            if store.persistent.jn_random_weather:
                show_random_sky(with_transition=with_transition)

            elif not jn_atmosphere.is_current_weather_sunny():
                show_sky(JNWeatherTypes.sunny, with_transition=with_transition)

    def show_random_sky(with_transition=True):
        """
        Shows a random sky with associated dimming effect

        IN:
            with_transition - If True, will visually fade in the new weather
        """

        # Select the sky and dimming effect
        weather_map = random.choice(list(__WEATHER_EFFECT_MAP.items()))
        weather_type = weather_map[0]
        sky, dim = weather_map[1]

        # Show the sky
        renpy.show(name=sky, zorder=_SKY_Z_INDEX)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)

        # Add the dimming effect matching the sky, if it exists
        if dim:
            renpy.show(name=dim, zorder=_DIM_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)

        # Play rain sfx if the chosen weather is rainy
        if weather_type in (JNWeatherTypes.rain, JNWeatherTypes.thunder):
            renpy.music.play(filenames=__MUFFLED_RAIN_PATH, channel="weather_loop", fadein=3.0)

        global current_weather
        current_weather = weather_type

    def show_sky(weather_type, with_transition=True):
        """
        Shows the specified sky placeholder with associated dimming effect.

        IN:
            weather_type - JNWeatherTypes value for the weather to set
            with_transition - If True, will visually fade in the new weather
        """
        sky, dim = __WEATHER_EFFECT_MAP.get(weather_type)
        if weather_type in (JNWeatherTypes.rain, JNWeatherTypes.thunder):
            renpy.music.play(filenames=__MUFFLED_RAIN_PATH, channel="weather_loop", fadein=3.0)
        
        else:
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        renpy.show(name=sky, zorder=_SKY_Z_INDEX)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)

        if dim:
            renpy.show(name=dim, zorder=_DIM_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)

        global current_weather
        current_weather = weather_type

    def is_current_weather_overcast():
        """
        Returns True if the current weather is overcast, otherwise False
        """
        return current_weather == JNWeatherTypes.overcast

    def is_current_weather_rain():
        """
        Returns True if the current weather is rain, otherwise False
        """
        return current_weather == JNWeatherTypes.rain

    def is_current_weather_sunny():
        """
        Returns True if the current weather is sunny, otherwise False
        """
        return current_weather == JNWeatherTypes.sunny

    def is_current_weather_thunder():
        """
        Returns True if the current weather is thunder, otherwise False
        """
        return current_weather == JNWeatherTypes.thunder

    def is_current_weather_glitch():
        """
        Returns True if the current weather is glitchy, otherwise False
        """
        return current_weather == JNWeatherTypes.glitch
