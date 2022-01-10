# Weather data
default persistent.jn_weather_api_key = None
default persistent.jn_weather_validate_apikey_in_time = None
default persistent.jn_weather_is_tracking_set_up = False
default persistent.jn_current_weather_type = jn_weather.TYPE_CLEAR
default persistent.jn_current_weather_long = dict()

# Location data
default persistent.jn_player_latitude = None
default persistent.jn_player_longitude = None
default persistent.jn_hemisphere_north_south = None
default persistent.jn_hemisphere_east_west = None

init -1 python in jn_weather:
    import datetime
    import store

    PREFERENCES = {
        "units" : "metric"
    }

    def make_API_call():
        """
            for making an API call after all checks and validations are done

            OUT:
                <dict> API json response
        """
        apikey = store.persistent.jn_weather_api_key
        params = get_location_dict()
        params.update(store.jn_weather.PREFERENCES)

        response = store.api.make_request("OpenWeatherMap", params, appid=apikey)

        #uhhh I probably shouldn't call it json
        json = response["json"]

        other_API_response_codes(json["cod"])

        return json

    def is_api_key_valid(apikey=None):
        """
            makes a new API call and returns True if apikey is valid

            IN:
                apikey - <string> if None, persisted apikey is used

            OUT:
                <bool>
        """
        if apikey is None:
            if store.persistent.jn_weather_api_key is None:
                return False

            apikey = store.persistent.jn_weather_api_key

        response = store.api.make_request("OpenWeatherMap", appid=apikey)["json"]

        if response["cod"] == 401:
            return False

        return True

    def other_API_response_codes(code):
        """
            logs based on what response we got from API call
        """
        if code == 429:
            store.jn_utils.log("[OpenWeatherMap] Exceeded 60 calls/min", store.jn_utils.SEVERITY_ERR)

        if code == 404:
            #we messed up... F
            store.jn_utils.log("[OpenWeatherMap] API request is most likely invalid", store.jn_utils.SEVERITY_ERR)

        if code in {500, 502, 503, 504}:
            store.jn_utils.log("[OpenWeatherMap] Something went wrong on API's side, we should contact OWM via email", store.jn_utils.SEVERITY_ERR)

    def get_location_dict(longitude=None, latitude=None):
        """
            Returns a dictionary with player's latitude and longitude
            in a format understandable by OpenWeatherMap API
            note: coordinates should be stored as a string to avoid constant conversion

            IN:
                longitude - <string> longitude coordinates
                latitude - <string> latitude coordinates
            OUT:
                location - <dictionary>
        """
        longitude = store.persistent.jn_player_longitude if longitude is None else longitude

        latitude = store.persistent.jn_player_latitude if latitude is None else latitude

        location={
            "lon" : longitude,
            "lat" : latitude
        }

        return location

    TYPE_THUNDER = 0
    TYPE_DRIZZLE = 1
    TYPE_RAIN = 2
    TYPE_SNOW = 3
    TYPE_MIST = 4
    TYPE_SMOKE = 5
    TYPE_HAZE = 6
    TYPE_DUST = 7
    TYPE_ASH = 8
    TYPE_SQUALL = 9
    TYPE_TORNADO = 10
    TYPE_CLEAR = 11
    TYPE_CLOUDS = 12

    class Weather():

        WEATHER_TABLE = {
            ##################### THUNDERSTORM ####################

            200 : {
                "thunder" : 2,
                "drizzle" : 0,
                "rain" : 1,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            201 : {
                "thunder" : 2,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            202 : {
                "thunder" : 2,
                "drizzle" : 0,
                "rain" : 3,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            210 : {
                "thunder" : 1,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            211 : {
                "thunder" : 2,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            212 : {
                "thunder" : 3,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            221 : {
                "thunder" : 2,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            230 : {
                "thunder" : 2,
                "drizzle" : 1,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            231 : {
                "thunder" : 2,
                "drizzle" : 2,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            232 : {
                "thunder" : 2,
                "drizzle" : 3,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },

            ##################### DRIZZLE ####################

            300: {
                "thunder" : 0,
                "drizzle" : 1,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            301: {
                "thunder" : 0,
                "drizzle" : 2,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            302: {
                "thunder" : 0,
                "drizzle" : 3,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            310: {
                "thunder" : 0,
                "drizzle" : 1,
                "rain" : 1,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            311: {
                "thunder" : 0,
                "drizzle" : 2,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            312: {
                "thunder" : 0,
                "drizzle" : 3,
                "rain" : 3,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            313: {
                "thunder" : 0,
                "drizzle" : 2,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            314: {
                "thunder" : 0,
                "drizzle" : 3,
                "rain" : 3,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            321: {
                "thunder" : 0,
                "drizzle" : 2,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },

            ##################### RAIN ####################

            500: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 1,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            501: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            502: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 3,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            503: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 4,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            504: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 5,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            511: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            520: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 1,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            521: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            522: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 3,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            531: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },

            ##################### SNOW ####################

            600: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 1,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            601: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            602: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 3,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            611: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            612: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 1,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            613: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            615: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 1,
                "snow" : 1,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            616: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 2,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            620: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 1,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            621: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 2,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            622: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 3,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },

            ##################### ATMOSPHERE ####################

            701: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "mist"
            },
            711: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "smoke"
            },
            721: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "haze"
            },
            731: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "dust"
            },
            741: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "fog"
            },
            751: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "sand"
            },
            761: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "dust"
            },
            762: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "ash"
            },
            771: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "squall"
            },
            781: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : "tornado"
            },

            ##################### CLEAR ####################

            800: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },

            ##################### CLOUDS ####################

            801: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            802: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            803: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            },
            804: {
                "thunder" : 0,
                "drizzle" : 0,
                "rain" : 0,
                "snow" : 0,
                "clouds" : 0,
                "clear" : False,
                "special" : None
            }
        }

        WEATHER_TYPES = {
            "Thunderstom" : TYPE_THUNDER,
            "Drizzle" : TYPE_DRIZZLE,
            "Rain" : TYPE_RAIN,
            "Snow" : TYPE_SNOW,
            "Mist" : TYPE_MIST,
            "Smoke" : TYPE_SMOKE,
            "Haze" : TYPE_HAZE,
            "Dust" : TYPE_DUST,
            "Ash" : TYPE_ASH,
            "Squall" : TYPE_SQUALL,
            "Tornado" : TYPE_TORNADO,
            "Clear" : TYPE_CLEAR,
            "Clouds" : TYPE_CLOUDS
        }

        @staticmethod
        def update_weather():
            """
                maps current weather type to currently supported weather
            """
            if store.persistent.jn_random_weather:
                return

            if store.persistent.jn_current_weather_type in {TYPE_THUNDER, TYPE_TORNADO}:
                store.jn_atmosphere.current_weather = store.jn_atmosphere.JNWeatherTypes.thunder

            elif store.persistent.jn_current_weather_type in {TYPE_RAIN, TYPE_DRIZZLE, TYPE_SNOW, TYPE_SQUALL, }:
                store.jn_atmosphere.current_weather = store.jn_atmosphere.JNWeatherTypes.rain

            elif store.persistent.jn_current_weather_type in {TYPE_MIST, TYPE_CLOUDS, TYPE_SMOKE, TYPE_HAZE, TYPE_ASH, TYPE_DUST}:
                store.jn_atmosphere.current_weather = store.jn_atmosphere.JNWeatherTypes.overcast

            else:
                store.jn_atmosphere.current_weather = store.jn_atmosphere.JNWeatherTypes.sunny

            store.jn_atmosphere.show_sky(store.jn_atmosphere.current_weather)

        @staticmethod
        def get_weather():
            """
                Returns current weather type from `WEATHER_TYPES`

                possible outputs:
                    TYPE_THUNDER
                    TYPE_DRIZZLE
                    TYPE_RAIN
                    TYPE_SNOW
                    TYPE_MIST
                    TYPE_SMOKE
                    TYPE_HAZE
                    TYPE_DUST
                    TYPE_ASH
                    TYPE_SQUALL
                    TYPE_TORNADO
                    TYPE_CLEAR
                    TYPE_CLOUDS
            """
            try:
                response = make_API_call()
                store.jn_utils.log("INFO: Made succesfull API call to OpenWeatherMap")
            except Exception as e:
                store.jn_utils.log("ERROR: While making an API call to OpenWeatherMap an exception occured. {0}".format(e), store.jn_utils.SEVERITY_ERR)

            # "weather" - weather info
            # [0] - primary weather info
            # "main" - one word description of current weather
            weather_type = Weather.WEATHER_TYPES[response["weather"][0]["main"]]
            store.persistent.jn_current_weather_type = weather_type

            # Update var for visualizing weather
            Weather.update_weather()
            return weather_type

        @staticmethod
        @store.jn_utils.coroutine_loop(datetime.timedelta(seconds=30))
        def get_weather_detail():
            """
                Returns detailed information about current weather with intensity of each ~~element~~
                and weather type as well (see get_weather above)

                OUT:
                    (detailed_description, weather_type)

                detail format:
                    {
                        "thunder" : <int>,
                        "drizzle" : <int>,
                        "rain" : <int>,
                        "snow" : <int>,
                        "clouds" : <int>,
                        "clear" : <bool>,
                        "special" : <string?>,
                        "wind" : <float>,
                        "temp" : <float>
                    }

                    thunder : intensity of a thunderstorm
                    drizzle : intensity of drizzle
                    rain    : intensity of rain
                    snow    : intensity of snowing
                    clouds  : percentage of cloud sky coverage
                    clear   : True or False
                    special : special weather events (dust storm, tornado, volcanic ash etc.), can be None
                    "wind"  : wind speed in m/s
                    "temp"  : temperature in Celsius
            """

            response = make_API_call()
            store.jn_utils.log(response)

            # Get primary weather info
            weather_info = response["weather"][0]

            # Get one-word info about current weather
            weather_type = Weather.WEATHER_TYPES[weather_info["main"]]

            # Get detailed weather info from look-up table WEATHER_TABLE by weather id
            parsed_weather = Weather.WEATHER_TABLE[weather_info["id"]]

            # If there is more detailed info on clouds in the API response
            ## Fetch that info
            ## overwrite clouds ~intensity~ with it's percentage
            if "clouds" in response:
                clouds_info = response["clouds"]["all"]
                parsed_weather["clouds"] = clouds_info

            # If there is wind info in APi response
            ## Fetch it
            ## add to our detailed weather report
            if "wind" in response:
                wind_info = response["wind"]["speed"]
                parsed_weather["wind"] = wind_info
            # else set it to 0
            else:
                parsed_weather["wind"] = 0

            store.persistent.jn_current_weather_long = parsed_weather
            store.persistent.jn_current_weather_type = weather_type

            # Update var for visualizing weather
            Weather.update_weather()
            return parsed_weather, weather_type

# THis is here purely because of a bug in renpy extension, remove after it's fixed
init -1 python:
    pass

init -1 python in location:
    import geocoder
    import store
    import webbrowser

    def open_maps(latitude, longitude):
        """
            Opens google maps in a new tab/window in the default browser with specified coordinates
        """
        url = "https://www.google.com/maps/place/{0},{1}".format(latitude, longitude)
        webbrowser.open(url)

    def get_coords_by_ip():
        """
            Returns coordinates tuple based on users ip adress
            note: for accuracy issues and a possibility of VPN usage this should be used only if other methods fail

            OUT:
                (latitude, longitude) or None if failed
        """
        #try to get coordinates
        try:
            g = geocoder.ip('me')

            # if no exception occured but something still went wrong return None
            if g.status != 'OK':
                return None

            return (str(g.lat), str(g.lng))
        #if an exception occurs, catch it and return None
        except:
            return None
