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
image glitch_garbled_n = "mod_assets/backgrounds/etc/youdidthis.png"
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
    import store.jn_utils as jn_utils

    # Draw Z indexes
    _DIM_Z_INDEX = 1
    _SKY_Z_INDEX = 0

    class JNWeatherTypes(Enum):
        """
        Identifiers for different weather objects, used for sanity checks when changing weather.
        """
        overcast = 1
        rain = 2
        sunny = 3
        thunder = 4
        glitch = 5

    class JNWeather():
        def __init__(
            self,
            weather_type,
            day_image,
            night_image=None,
            dim_image=None,
            weather_sfx=None
        ):
            """
            Initialises a new instance of JNWeather.

            IN:
                - weather_type - JNWeatherTypes type describing this weather
                - day_image - Name of the image to show for this weather during the day
                - night_image - Name of the image to show for this weather during the night
                - dim_image - Name of the dimming effect to use, or None
                - weather_sfx - File path of the weather sound effect to use, or None
            """
            self.weather_type = weather_type
            self.day_image = day_image
            self.night_image = night_image
            self.dim_image = dim_image
            self.weather_sfx = weather_sfx

    WEATHER_OVERCAST = JNWeather(
        weather_type=JNWeatherTypes.overcast,
        day_image="sky_day overcast",
        dim_image="dim light"
    )

    WEATHER_RAIN = JNWeather(
        weather_type=JNWeatherTypes.rain,
        day_image="sky_day rain",
        dim_image="dim medium",
        weather_sfx="mod_assets/sfx/rain_muffled.mp3"
    )

    WEATHER_THUNDER = JNWeather(
        weather_type=JNWeatherTypes.thunder,
        day_image="sky_day thunder",
        dim_image="dim heavy",
        weather_sfx="mod_assets/sfx/rain_muffled.mp3"
    )

    WEATHER_SUNNY = JNWeather(
        weather_type=JNWeatherTypes.sunny,
        day_image="sky_day sunny"
    )

    WEATHER_GLITCH = JNWeather(
        weather_type=JNWeatherTypes.glitch,
        day_image="glitch_fuzzy")

    __RANDOM_WEATHER_TYPES = [
        WEATHER_OVERCAST,
        WEATHER_RAIN,
        WEATHER_THUNDER,
        WEATHER_SUNNY
    ]

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

            elif not is_current_weather_sunny():
                show_sky(WEATHER_SUNNY, with_transition=with_transition)

    def show_random_sky(with_transition=True):
        """
        Shows a random sky with associated dimming effect

        IN:
            with_transition - If True, will visually fade in the new weather
        """
        # Select the sky
        weather = random.choice(__RANDOM_WEATHER_TYPES)

        # Show the sky
        renpy.show(name=weather.day_image, zorder=_SKY_Z_INDEX)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)

        # Add the dimming effect, if defined
        if weather.dim_image:
            renpy.show(name=weather.dim_image, zorder=_DIM_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)

        # Play rain sfx if the chosen weather is rainy
        if weather.weather_sfx:
            renpy.music.play(filenames=weather.weather_sfx, channel="weather_loop", fadein=3.0)

        else:
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        global current_weather
        current_weather = weather.weather_type

    def show_sky(weather, with_transition=True):
        """
        Shows the specified sky placeholder with associated dimming effect.

        IN:
            weather - JNWeather to set
            with_transition - If True, will visually fade in the new weather
        """
        if weather.weather_sfx:
            renpy.music.play(filenames=weather_sfx, channel="weather_loop", fadein=3.0)

        else:
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        renpy.show(name=weather.day_image, zorder=_SKY_Z_INDEX)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)

        if weather.dim_image:
            renpy.show(name=weather.dim_image, zorder=_DIM_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)

        global current_weather
        current_weather = weather.weather_type

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
