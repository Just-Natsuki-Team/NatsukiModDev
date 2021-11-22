init -1 python in weather:
    import urllib2
    import datetime
    import store

    #TEST API key, feel free to use
    #2c2f369ad4987a01f5de4c149665c5fd
    #NOTE: remove in production

    PREFERENCES = {
        "units" : "metric"
    }

    @store.utils.coroutine_loop(datetime.timedelta(seconds=30))
    def testytesttest():
        store.utils.log("testiiiiiiiiiiiiiiiiiiiiiiiiiing")
    testytesttest.start()


    def get_json(response):
        """
            returns json part of response as a dictionary
        """
        html = response["html"]
        if html is None:
            return {"cod" : response["status"]}

        start = html.find('{')
        end = html.rfind('}')+1

        stripped = html[start:end]
        json = store.api.string_to_dict(stripped)

        return json

    def make_API_call():
        """

        """
        apikey = store.persistent.weather_api_key
        params = get_location_dict()
        params.update(store.weather.PREFERENCES)

        response = store.api.make_request("OpenWeatherMap", params, appid=apikey)

        #uhhh I probably shouldn't call it json
        json = get_json(response)

        other_API_response_codes(json["cod"])

        return json

    def is_api_key_valid(apikey):
        response = get_json(store.api.make_request("OpenWeatherMap", appid=apikey))

        if response["cod"] == 401:
            return False

        return True

    def other_API_response_codes(code):
        if code == 429:
            store.utils.log("[OpenWeatherMap] Exceeded 60 calls/min", store.utils.SEVERITY_ERR)

        if code == 404:
            #we messed up... F
            store.utils.log("[OpenWeatherMap] API request is most likely invalid", store.utils.SEVERITY_ERR)

        if code in {500, 502, 503, 504}:
            store.utils.log("[OpenWeatherMap] Something went wrong on API's side, we should contact OWM via email", store.utils.SEVERITY_ERR)

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
        longitude = store.persistent.longitude if longitude is None else longitude

        latitude = store.persistent.latitude if latitude is None else latitude

        location={
            "lon" : longitude,
            "lat" : latitude
        }

        return location



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

        @staticmethod
        def get_weather():
            """
                Returns a simple one-word description about current weather

                possible outputs:
                    Thunderstom
                    Drizzle
                    Rain
                    Snow
                    Mist/Smoke/Haze/Dust/Ash/Squall/Tornado
                    Clear
                    Clouds
            """
            try:
                response = make_API_call()
                store.utils.log("INFO: Made succesfull API call to OpenWeatherMap")
            except Exception as e:
                store.utils.log("ERROR: While making an API call to OpenWeatherMap an exception occured. {0}".format(e), store.utils.SEVERITY_ERR)

            # "weather" - weather info
            # [0] - primary weather info
            # "main" - one word description of current weather
            return response["weather"][0]["main"]

        @staticmethod
        def get_weather_detail():
            """
                Returns detailed information about current weather with intensity of each ~~element~~

                format:
                    {
                        "thunder" : <int>,
                        "drizzle" : <int>,
                        "rain" : <int>,
                        "snow" : <int>,
                        "clouds" : <int>,
                        "clear" : <bool>,
                        "special" : <string?>,
                        "wind" : <int>,
                        "temp" : <int>
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
            store.utils.log(response)

            # Get primary weather info
            weather_info = response["weather"][0]

            # Get one-word info about current weather
            weather_short = weather_info["main"]

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

            store.persistent.current_weather_long = parsed_weather
            store.persistent.current_weather_long = weather_short

            return parsed_weather, weather_short

# THis is here purely because of a bug in renpy extension, remove after it's fixed
init -1 python:
    pass

init -1 python in location:
    import geocoder
    import store

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

    # Currently not in use
    def get_coords_by_city(city, country=None):
        """
            Returns coordinates of a city from a lookup file

            IN:
                city - <string>
                country - <string?> (optional) two-letter code of a country
            OUT:
                0, (None, None) - if no occurance of city name in lookup
                1, (latitude, longitude) if a single of city name found
                2, (None, NOne) - if multiple occurances of city name found
        """
        # Open lookup file, read it's content and close it
        lookup_file = open("countries_lookup.txt", "r")
        lookup = lookup_file.read()
        lookup_file.close()

        # if country wasn't inputted search only by city name
        if not country:
            city_occurrences = lookup.count("\n{0},".format(city))
        # else search by city and country
        else:
            city_occurrences = lookup.count("\n{0},{1},".format(city, country))

        if city_occurrences == 0:
            return 0, (None, None)

        elif city_occurrences == 1:
            # find starting index of the line our city is on
            if not country:
                city_line_start = lookup.find("\n{0},".format(city))+1
            else:
                city_line_start = lookup.find("\n{0},{1},".format(city, country))+1

            # find ending index of the line (next new line after starting index)
            city_line_end = lookup.find('\n', city_line_start)
            # get only the line
            city_line = lookup[city_line_start:city_line_end]
            # split it by ','
            ## [city_name, country, latitude, longitude, region/state]
            city_line = city_line.split(',')

            return 1, (city_line[2], city_line[3])

        elif city_occurrences > 1:
            return 2, (None, None)
