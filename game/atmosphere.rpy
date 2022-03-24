# Weather data
default persistent.jn_weather_api_key = None
default persistent.jn_weather_api_configured = False

# Location data
default persistent.jn_player_latitude = None
default persistent.jn_player_longitude = None
default persistent.jn_hemisphere_north_south = None
default persistent.jn_hemisphere_east_west = None

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
define weather_change_transition = Dissolve(1.5)
define dim_change_transition = Dissolve(0.25)

init 0 python in jn_atmosphere:
    from Enum import Enum
    import random
    import requests
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

    __WEATHER_CODE_REGEX_TYPE_MAP = {
        ("^2[0-9][0-9]$"): WEATHER_THUNDER, # Thunder
        ("^3[0-9][0-9]$"): WEATHER_RAIN, # Drizzle
        ("^5[0-9][0-9]$"): WEATHER_RAIN, # Rain
        ("^6[0-9][0-9]$"): WEATHER_OVERCAST, # Snow
        ("^7[0-9][0-9]$"): WEATHER_OVERCAST, # Misc (mist, tornado, sandstorms, etc.)
        ("(800|801|802)"): WEATHER_SUNNY, # Clear/light clouds
        ("(803|804)"): WEATHER_OVERCAST, # Clouds
    }

    __WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={WEATHER_LAT}&lon={WEATHER_LONG}&units=metric&exclude=current,minutely,daily,alerts&appid={WEATHER_API_KEY}"

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
        weather = random.choice([
            jn_atmosphere.WEATHER_OVERCAST,
            jn_atmosphere.WEATHER_RAIN,
            jn_atmosphere.WEATHER_THUNDER,
            jn_atmosphere.WEATHER_SUNNY
        ])

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

    def get_weather_from_api():
        """
        Gets the current weather from the OpenWeatherMap API, assuming it is set up.
        """
        # Get the response from the OpenWeatherMap api
        weather_response = requests.get(
            url="https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&units=metric&exclude=current,minutely,daily,alerts&appid={2}".format(
                persistent.jn_player_latitude,
                persistent.jn_player_longitude,
                persistent.jn_weather_api_key
            ),
            verify=os.environ['SSL_CERT_FILE'])

        if not weather_response.status_code == 200:
            # Invalid response, can't do anything here so log and return
            jn_utils.log("Unable to fetch weather from OpenWeatherMap; API response was: {0}".format(weather_response.status_code))
            return None
        
        # We got a response, so find out the weather and return if it exists in the map
        weather_data = weather_response.json()["hourly"][0]

        for regex, weather in WEATHER_CODE_REGEX_TYPE_MAP.items():
            if re.search(regex, str(weather_data["weather"][0]["id"])):
                return weather.weather_type

        # No map entries, fallback
        return None

    def get_latitude_longitude_by_ip_address():
        """
        Returns (latitude, longitude) tuple based on the player's IP address.
        Please note this will be affected by any VPNs, etc active on the host.

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

    def is_current_weather_glitch():
        """
        Returns True if the current weather is glitchy, otherwise False
        """
        return current_weather == JNWeatherTypes.glitch
