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

image sky glitch_fuzzy:
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
# Credit for rain, snow graphics goes to Monika After Story @ https://github.com/Monika-After-Story/MonikaModDev
# Thanks for allowing us to use these!
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
    _DIM_Z_INDEX = 6
    _PARTICLES_Z_INDEX = -3
    _CLOUDS_Z_INDEX = -6
    _SKY_Z_INDEX = -8

    _OPENWEATHERMAP_API_BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

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
            notify_text=list(),
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
                - notify_text - The text to show via popup if the weather changes, and Natsuki decides to react
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
            self.notify_text = notify_text
            self.dim_image = dim_image
            self.day_clouds_image = day_clouds_image
            self.night_clouds_image = night_clouds_image
            self.day_particles_image = day_particles_image
            self.night_particles_image = night_particles_image
            self.weather_sfx = weather_sfx

        
        def getNotifyText(self):
            """
            Gets a random notification string for this weather to be used in a popup
            """
            if self.notify_text and len(self.notify_text) > 0:
                store.happy_emote = jn_utils.getRandomHappyEmoticon()
                store.angry_emote = jn_utils.getRandomAngryEmoticon()
                store.sad_emote = jn_utils.getRandomSadEmoticon()
                store.tease_emote = jn_utils.getRandomTeaseEmoticon()
                store.confused_emote = jn_utils.getRandomConfusedEmoticon()
                return renpy.substitute(random.choice(self.notify_text))

            return None

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
        notify_text=[
            "Ugh... raining again. [angry_emote]",
            "Ew. Rain. [angry_emote]",
            "Man... why does it have to rain so much?",
            "Huh? It's raining? Gross... [angry_emote]",
        ],
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
        notify_text=[
            "Those clouds look really dark, huh? :<",
            "It was a dark and stormy night...",
            "Ugh... I hate storms... [angry_emote]",
            "Hey... is it stormy over there too? :/",
        ],
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
        notify_text=[
            "[player]! [player]! It's snowing! [happy_emote]",
            "It's snowing! It's snowing! [happy_emote]",
            "[player]! Is it snowing for you too?! [happy_emote]",
        ],
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
        day_sky_image="sky glitch_fuzzy",
        night_sky_image="sky glitch_fuzzy")

    # Weather code -> JNWeather map
    # key: Regex matching the weather code as a string, allowing ranged captures (returned from OpenWeatherMap)
    # value: JNWeather associated with the weather code range
    __WEATHER_CODE_REGEX_TYPE_MAP = {
        ("^2\d{2}$"): WEATHER_THUNDER, # Thunder
        ("^3\d{2}$"): WEATHER_RAIN, # Drizzle
        ("^5\d{2}$"): WEATHER_RAIN, # Rain
        ("^6\d{2}$"): WEATHER_SNOW, # Snow
        ("^7\d{2}$"): WEATHER_OVERCAST, # Misc (mist, tornado, sandstorms, etc.)
        ("(800|801|802|803)"): WEATHER_SUNNY, # Clear/light clouds
        ("(804)"): WEATHER_OVERCAST, # Clouds
    }

    current_weather = None

    def updateSky(with_transition=True):
        """
        Shows the sky based on the sunrise/sunset times specified under the persistent, and affinity.

        IN:
            with_transition - If True, will visually fade in the new weather
        """
        # API-based weather
        if store.persistent._jn_weather_setting == int(jn_preferences.weather.JNWeatherSettings.real_time):

            # Attempt to display weather based on API, otherwise default
            api_weather_result = getWeatherFromApi()
            if not api_weather_result:
                jn_utils.log("Unable to retrieve weather from API; defaulting to Sunny.")
                renpy.notify("Failed to update weather; please check log for more information.")
                showSky(WEATHER_SUNNY, with_transition=with_transition)

            else:
                showSky(weather=api_weather_result, with_transition=with_transition)

        # Random weather
        elif store.persistent._jn_weather_setting == int(jn_preferences.weather.JNWeatherSettings.random):

            # Flex based on affinity. An upset Natsuki will result in more rain, etc.
            if store.Natsuki.isEnamored(higher=True):
                showSky(random.choice([
                    WEATHER_OVERCAST,
                    WEATHER_RAIN,
                    WEATHER_THUNDER,
                    WEATHER_SUNNY,
                    WEATHER_SUNNY,
                    WEATHER_SUNNY,
                    WEATHER_SNOW,
                    WEATHER_SNOW
                ]),
                with_transition=with_transition)

            elif store.Natsuki.isAffectionate(higher=True):
                showSky(random.choice([
                    WEATHER_OVERCAST,
                    WEATHER_RAIN,
                    WEATHER_THUNDER,
                    WEATHER_SUNNY,
                    WEATHER_SUNNY,
                    WEATHER_SUNNY,
                    WEATHER_SNOW
                ]),
                with_transition=with_transition)

            elif store.Natsuki.isNormal(higher=True):
                showSky(random.choice([
                    WEATHER_OVERCAST,
                    WEATHER_RAIN,
                    WEATHER_THUNDER,
                    WEATHER_SUNNY,
                    WEATHER_SNOW
                ]),
                with_transition=with_transition)

            elif store.Natsuki.isDistressed(higher=True):
                showSky(random.choice([
                    WEATHER_OVERCAST,
                    WEATHER_OVERCAST,
                    WEATHER_RAIN,
                    WEATHER_RAIN,
                    WEATHER_RAIN,
                    WEATHER_THUNDER
                ]),
                with_transition=with_transition)

            else:
                showSky(random.choice([
                    WEATHER_OVERCAST,
                    WEATHER_RAIN,
                    WEATHER_RAIN,
                    WEATHER_THUNDER,
                    WEATHER_THUNDER,
                    WEATHER_THUNDER
                ]),
                with_transition=with_transition)

        # Default weather
        else:
            if store.Natsuki.isNormal(higher=True):
                showSky(WEATHER_SUNNY, with_transition=with_transition)

            elif store.Natsuki.isDistressed(higher=True):
                showSky(WEATHER_OVERCAST, with_transition=with_transition)

            else:
                showSky(WEATHER_RAIN, with_transition=with_transition)

    def showSky(weather, with_transition=True):
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
        current_weather = weather

    def getWeatherApiUrl(latitude, longitude, units, app_id, exclude=[]):
        """
        Builds the OpenWeatherMap API URL, given parameters.

        IN:
            - latitude - The latitude to use for the request URL
            - longitude - The longitude to use for the request URL
            - units - The str units of measurement (metric/imperial) to use for the request URL
            - app_id - The API key to use
            - exclude - Optional str list of units to exclude
        """
        exclude_string = "" if len(exclude) == 0 else "&exclude={0}".format(",".join(exclude))
        return "{0}?lat={1}&lon={2}&units={3}{4}&appid={5}".format(
            _OPENWEATHERMAP_API_BASE_URL,
            latitude,
            longitude,
            units,
            exclude_string,
            app_id
        )

    def getWeatherFromApi():
        """
        Gets the current weather from the OpenWeatherMap API, assuming it is set up.
        """
        # Get the response from the OpenWeatherMap api
        try:
            weather_response = requests.get(
                url=getWeatherApiUrl(
                    latitude=store.persistent._jn_player_latitude_longitude[0],
                    longitude=store.persistent._jn_player_latitude_longitude[1],
                    units="metric",
                    app_id=store.persistent._jn_weather_api_key,
                    exclude=["current", "minutely", "daily", "alerts"]
                ),
                verify=os.environ['SSL_CERT_FILE'])

        except Exception as exception:
            # Something went wrong that meant no response was returned at all; so log and return
            jn_utils.log("Unable to fetch weather from OpenWeatherMap as an exception occurred; {0}".format(exception.message))
            return None

        if weather_response.status_code != 200:
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

    def getLatitudeLongitudeByIpAddress():
        """
        Returns (latitude, longitude) tuple based on the player's IP address.
        Please note this will be affected by any VPNs, etc. in use by the host computer/network.

        OUT:
            - Tuple of (latitude, longitude), or None
        """
        try:
            # Attempt to fetch the player's latitude and longitude, then return both
            response = requests.get("http://ipinfo.io/json", verify=os.environ['SSL_CERT_FILE'])
            if response.status_code != 200:
                return None

            return (response.json()["loc"].split(','))

        except Exception as exception:
            jn_utils.log("Failed to retrieve user latitude, longitude via IP address: {}".format(exception))
            return None

    def isCurrentWeatherOvercast():
        """
        Returns True if the current weather is overcast, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.overcast

    def isCurrentWeatherRain():
        """
        Returns True if the current weather is rain, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.rain

    def isCurrentWeatherSunny():
        """
        Returns True if the current weather is sunny, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.sunny

    def isCurrentWeatherThunder():
        """
        Returns True if the current weather is thunder, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.thunder

    def isCurrentWeatherSnow():
        """
        Returns True if the current weather is snow, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.snow

    def isCurrentWeatherGlitch():
        """
        Returns True if the current weather is glitchy, otherwise False
        """
        return current_weather.weather_type == JNWeatherTypes.glitch

label weather_change:
    $ previous_weather = jn_atmosphere.current_weather
    $ jn_atmosphere.updateSky()

    if (
        Natsuki.isAffectionate(higher=True) 
        and random.randint(1, 4) == 1
        and previous_weather.weather_type != jn_atmosphere.current_weather.weather_type
    ):
        # Check for window react
        if persistent._jn_notify_activity and not jn_activity.getJNWindowActive() and jn_atmosphere.current_weather.getNotifyText():
            $ jn_activity.notifyPopup(renpy.substitute(jn_atmosphere.current_weather.getNotifyText()))
            return

        # Check for in-game dialogue
        else:
            $ alt_dialogue = random.choice([True, False])
            if jn_atmosphere.isCurrentWeatherSunny():
                if previous_weather.weather_type == jn_atmosphere.JNWeatherTypes.rain:
                    n 1fcsaj "Well,{w=1}{nw}"
                    extend 1fllgs " about time all that rain buzzed off!{w=1}{nw}"
                    n 1nchgn "Much better.{w=3}{nw}"

                elif previous_weather.weather_type == jn_atmosphere.JNWeatherTypes.thunder:
                    n 1tllpu "Huh?{w=1.25}{nw}"
                    extend 1ullajeex "Oh,{w=0.2} the storm passed.{w=1}{nw}"
                    n 1fcsajsbl "Good riddance.{w=3}{nw}"

                elif previous_weather.weather_type == jn_atmosphere.JNWeatherTypes.snow:
                    n 1kllpu "Aww...{w=1.5}{nw}"
                    extend 1kllpol " it stopped snowing...{w=3}{nw}"

                else:
                    n 1ulraj "Oh,{w=0.2} hey.{w=1}{nw}"
                    extend 1ulrbo " It just cleared up outside.{w=3}{nw}"

            if jn_atmosphere.isCurrentWeatherRain():
                # Rain
                if alt_dialogue:
                    n 1kcsemesi "Man...{w=1.25}{nw}"
                    extend 1kllsl " rain {i}again{/i}?{w=1}{nw}"
                    extend 1fsrbo " Lame...{w=3}{nw}"

                else:
                    n 1fcsem "Ugh...{w=1.5}{nw}"
                    extend 1fslpol " I'll never {i}not{/i} find rain gross.{w=3}{nw}"
                
            elif jn_atmosphere.isCurrentWeatherThunder():
                # Thunder
                if alt_dialogue:
                    n 1unmboesu "...{w=1}{nw}"
                    n 1nllem "I gotta say,{w=0.75}{nw}"
                    extend 1ksqsr " I am {i}not{/i} liking the look of those clouds.{w=1}{nw}"
                    extend 1nsrupesd " Yeesh...{w=3}{nw}"

                else:
                    n 1ulremesu "Woah...{w=1}{nw}"
                    extend 1ullpu " now those are some clouds,{w=0.5}{nw}"
                    extend 1tnmbo " huh?{w=3}{nw}"

            elif jn_atmosphere.isCurrentWeatherSnow():
                # Snow
                if alt_dialogue:
                    n 1uwdajeex "Woah!{w=1}{nw}"
                    n 1ullgs "[player],{w=0.2} look!{w=0.5}{nw}"
                    extend 1uchbgledz " It's snowing!{w=3}{nw}"

                else:
                    n 1uwdajeex "...!{w=1}{nw}"
                    n 1ullbg "Heeey!{w=0.75}{nw}"
                    extend 1uchgnledz " It's snowing!{w=3}{nw}"

            return
