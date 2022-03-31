# Weather data
default persistent._jn_weather_api_key = None
default persistent._jn_weather_api_configured = False

# Location data
default persistent._jn_player_latitude_longitude = None
default persistent._jn_hemisphere_north_south = None
default persistent._jn_hemisphere_east_west = None

# Sky types
image sky day overcast = "mod_assets/backgrounds/atmosphere/sky/sky_day_overcast.png"
image sky day rain = "mod_assets/backgrounds/atmosphere/sky/sky_day_rain.png"
image sky day sunny = "mod_assets/backgrounds/atmosphere/sky/sky_day_sunny.png"
image sky day thunder = "mod_assets/backgrounds/atmosphere/sky/sky_day_thunder.png"
image sky day snow = "mod_assets/backgrounds/atmosphere/sky/sky_day_snow.png"

image sky night overcast = "mod_assets/backgrounds/atmosphere/sky/sky_night_overcast.png"
image sky night rain = "mod_assets/backgrounds/atmosphere/sky/sky_night_rain.png"
image sky night sunny = "mod_assets/backgrounds/atmosphere/sky/sky_night_sunny.png"
image sky night thunder = "mod_assets/backgrounds/atmosphere/sky/sky_night_thunder.png"

# Dimming effects; used with various weather conditions
image dim light = "mod_assets/backgrounds/atmosphere/dim/dim_light.png"
image dim medium = "mod_assets/backgrounds/atmosphere/dim/dim_medium.png"
image dim heavy = "mod_assets/backgrounds/atmosphere/dim/dim_heavy.png"

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

# Clouds
image clouds day light:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_light.png"
    cloud_scroll

image clouds day heavy:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_heavy.png"
    cloud_scroll

image clouds day thunder:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_day_thunder.png"
    cloud_scroll

image clouds night light:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_night_light.png"
    cloud_scroll

image clouds night heavy:
    "mod_assets/backgrounds/atmosphere/clouds/clouds_night_heavy.png"
    cloud_scroll

# Particles
image particles rain:
    "mod_assets/backgrounds/atmosphere/particles/rain.png"
    rain_scroll

image particles snow:
    "mod_assets/backgrounds/atmosphere/particles/snow.png"
    snow_scroll

# Transforms
transform cloud_scroll:
    # Clouds shift from left to right
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 30 xoffset -1280
        repeat

transform snow_scroll:
    subpixel True
    right
    parallel:
        xoffset 0 yoffset 0
        linear 60 xoffset 220  yoffset 1280
        repeat

transform rain_scroll:
    subpixel True
    right
    parallel:
        xoffset 0 yoffset 0
        linear 2 xoffset 220  yoffset 1280
        repeat

# Transitions
define weather_change_transition = Dissolve(0.75)
define dim_change_transition = Dissolve(0.25)

init 0 python in jn_atmosphere:
    from Enum import Enum
    import os
    import random
    import re
    import requests
    import store
    import store.jn_preferences as jn_preferences
    import store.jn_utils as jn_utils

    # Zorder indexes
    # Complete order is:
    # v PROPS 
    # v NATSUKI
    # v BACKGROUND
    # v DIM
    # v PARTICLES
    # v CLOUDS
    #   SKY
    _DIM_Z_INDEX = 2
    _PARTICLES_Z_INDEX = -1
    _CLOUDS_Z_INDEX = -2
    _SKY_Z_INDEX = -3

    class JNWeatherTypes(Enum):
        """
        Identifiers for different weather objects, used for sanity checks when changing weather.
        """
        overcast = 1
        rain = 2
        sunny = 3
        thunder = 4
        glitch = 5
        snow = 6

    class JNWeather():
        def __init__(
            self,
            weather_type,
            day_sky_image,
            night_sky_image,
            dim_image=None,
            day_clouds_image=None,
            night_clouds_image=None,
            day_particles_image=None,
            night_particles_image=None,
            weather_sfx=None
        ):
            """
            Initialises a new instance of JNWeather.

            IN:
                - weather_type - JNWeatherTypes type describing this weather
                - day_sky_image - Name of the image to show for this weather during the day
                - night_sky_image - Name of the image to show for this weather during the night
                - dim_image - Name of the dimming effect to use, or None
                - day_clouds_image - Name of the clouds to use for this weather during the day, or None
                - night_clouds_image - Name of the clouds to use for this weather during the night, or None
                - day_particles_image - Name of the particles to use for this weather during the day, or None
                - night_particles_image - Name of the particles to use for this weather during the night, or None
                - weather_sfx - File path of the weather sound effect to use, or None
            """
            self.weather_type = weather_type
            self.day_sky_image = day_sky_image
            self.night_sky_image = night_sky_image
            self.dim_image = dim_image
            self.day_clouds_image = day_clouds_image
            self.night_clouds_image = night_clouds_image
            self.day_particles_image = day_particles_image
            self.night_particles_image = night_particles_image
            self.weather_sfx = weather_sfx

    WEATHER_OVERCAST = JNWeather(
        weather_type=JNWeatherTypes.overcast,
        day_sky_image="sky day overcast",
        night_sky_image="sky night overcast",
        dim_image="dim light",
        day_clouds_image="clouds day heavy",
        night_clouds_image="clouds night heavy",
    )

    WEATHER_RAIN = JNWeather(
        weather_type=JNWeatherTypes.rain,
        day_sky_image="sky day rain",
        night_sky_image="sky night rain",
        dim_image="dim medium",
        day_clouds_image="clouds day heavy",
        night_clouds_image="clouds night heavy",
        day_particles_image="particles rain",
        night_particles_image="particles rain",
        weather_sfx="mod_assets/sfx/rain_muffled.mp3"
    )

    WEATHER_THUNDER = JNWeather(
        weather_type=JNWeatherTypes.thunder,
        day_sky_image="sky day thunder",
        night_sky_image="sky night thunder",
        dim_image="dim heavy",
        day_clouds_image="clouds day thunder",
        night_clouds_image="clouds night heavy",
        day_particles_image="particles rain",
        night_particles_image="particles rain",
        weather_sfx="mod_assets/sfx/rain_muffled.mp3"
    )

    WEATHER_SNOW = JNWeather(
        weather_type=JNWeatherTypes.snow,
        day_sky_image="sky day snow",
        night_sky_image="sky night overcast",
        dim_image="dim light",
        day_clouds_image="clouds day light",
        night_clouds_image="clouds night light",
        day_particles_image="particles snow",
        night_particles_image="particles snow",
    )

    WEATHER_SUNNY = JNWeather(
        weather_type=JNWeatherTypes.sunny,
        day_sky_image="sky day sunny",
        night_sky_image="sky night sunny",
        day_clouds_image="clouds day light",
        night_clouds_image="clouds night light"
    )

    WEATHER_GLITCH = JNWeather(
        weather_type=JNWeatherTypes.glitch,
        day_sky_image="glitch_fuzzy",
        night_sky_image="glitch_fuzzy")

    # Weather code -> JNWeather map
    # key: Regex matching the weather code as a string, allowing ranged captures (returned from OpenWeatherMap)
    # value: JNWeather associated with the weather code range
    __WEATHER_CODE_REGEX_TYPE_MAP = {
        ("^2[0-9][0-9]$"): WEATHER_THUNDER, # Thunder
        ("^3[0-9][0-9]$"): WEATHER_RAIN, # Drizzle
        ("^5[0-9][0-9]$"): WEATHER_RAIN, # Rain
        ("^6[0-9][0-9]$"): WEATHER_SNOW, # Snow
        ("^7[0-9][0-9]$"): WEATHER_OVERCAST, # Misc (mist, tornado, sandstorms, etc.)
        ("(800|801|802)"): WEATHER_SUNNY, # Clear/light clouds
        ("(803|804)"): WEATHER_OVERCAST, # Clouds
    }

    current_weather = None

    def update_sky(with_transition=True):
        """
        Shows the sky based on the sunrise/sunset times specified under the persistent.

        IN:
            with_transition - If True, will visually fade in the new weather
        """
        # API-based weather
        if store.persistent._jn_weather_setting == int(jn_preferences.weather.JNWeatherSettings.real_time):

            # Attempt to display weather based on API, otherwise default
            api_weather_result = get_weather_from_api()
            if not api_weather_result:
                jn_utils.log("Unable to retrieve weather from API; defaulting to Sunny.")
                show_sky(WEATHER_SUNNY, with_transition=with_transition)

            else:
                show_sky(weather=api_weather_result, with_transition=with_transition)

        # Random weather
        elif store.persistent._jn_weather_setting == int(jn_preferences.weather.JNWeatherSettings.random):
            weather = show_sky(random.choice([
                WEATHER_OVERCAST,
                WEATHER_RAIN,
                WEATHER_THUNDER,
                WEATHER_SUNNY,
                WEATHER_SNOW
            ]),
            with_transition=with_transition)

        # Default weather
        else:
            show_sky(WEATHER_SUNNY, with_transition=with_transition)

    def show_sky(weather, with_transition=True):
        """
        Shows the specified sky with related clouds and dimming effect (if defined), based on time of day.

        IN:
            weather - JNWeather to set
            with_transition - If True, will visually fade in the new weather
        """
        # Play rain sfx if the chosen weather is rainy
        if weather.weather_sfx:
            renpy.music.play(filenames=weather.weather_sfx, channel="weather_loop", fadein=3.0)

        else:
            renpy.music.stop(channel="weather_loop", fadeout=5.0)

        # Get images to show based on day/night state
        sky_to_show = weather.day_sky_image if store.jn_is_day() else weather.night_sky_image
        clouds_to_show = weather.day_clouds_image if store.jn_is_day() else weather.night_clouds_image

        # Show the selected sky
        renpy.show(name=sky_to_show, zorder=_SKY_Z_INDEX)
        if with_transition:
            renpy.with_statement(trans=store.weather_change_transition)

        # Add the clouds, if defined
        if clouds_to_show:
            renpy.show(name=clouds_to_show, zorder=_CLOUDS_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.weather_change_transition)

        else:
            renpy.hide("clouds")

        # Add the particles, if defined
        if weather.day_particles_image or weather.night_particles_image:
            if store.jn_is_day() and weather.day_particles_image:
                renpy.show(name=weather.day_particles_image, zorder=_PARTICLES_Z_INDEX)

            elif weather.night_particles_image:
                renpy.show(name=weather.night_particles_image, zorder=_PARTICLES_Z_INDEX)

            if with_transition:
                renpy.with_statement(trans=store.weather_change_transition)

        else:
            renpy.hide("particles")

        # Add the dimming effect, if defined
        if weather.dim_image:
            renpy.show(name=weather.dim_image, zorder=_DIM_Z_INDEX)
            if with_transition:
                renpy.with_statement(trans=store.dim_change_transition)

        else:
            renpy.hide("dim")

        global current_weather
        current_weather = weather.weather_type

    def get_weather_from_api():
        """
        Gets the current weather from the OpenWeatherMap API, assuming it is set up.
        """
        # Get the response from the OpenWeatherMap api
        weather_response = requests.get(
            url="https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&units=metric&exclude=current,minutely,daily,alerts&appid={2}".format(
                store.persistent._jn_player_latitude_longitude[0],
                store.persistent._jn_player_latitude_longitude[1],
                store.persistent._jn_weather_api_key
            ),
            verify=os.environ['SSL_CERT_FILE'])

        if not weather_response.status_code == 200:
            # Invalid response, can't do anything here so log and return
            jn_utils.log("Unable to fetch weather from OpenWeatherMap; API response was: {0}".format(weather_response.status_code))
            return None

        # We got a response, so find out the weather and return if it exists in the map
        weather_data = weather_response.json()["hourly"][0]

        for regex, weather in __WEATHER_CODE_REGEX_TYPE_MAP.items():
            if re.search(regex, str(weather_data["weather"][0]["id"])):
                return weather

        # No map entries, fallback
        return None

    def get_latitude_longitude_by_ip_address():
        """
        Returns (latitude, longitude) tuple based on the player's IP address.
        Please note this will be affected by any VPNs, etc. in use by the host computer/network.

        OUT:
            - Tuple of (latitude, longitude), or None
        """
        try:
            # Attempt to fetch the player's latitude and longitude, then return both
            response = requests.get("http://ipinfo.io/json", verify=os.environ['SSL_CERT_FILE'])
            if not response.status_code == 200:
                return None

            return (response.json()["loc"].split(','))

        except Exception as exception:
            jn_utils.log("Failed to retrieve user latitude, longitude via IP address: {}".format(exception))
            return None

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

    def is_current_weather_snow():
        """
        Returns True if the current weather is snow, otherwise False
        """
        return current_weather == JNWeatherTypes.snow

    def is_current_weather_glitch():
        """
        Returns True if the current weather is glitchy, otherwise False
        """
        return current_weather == JNWeatherTypes.glitch
