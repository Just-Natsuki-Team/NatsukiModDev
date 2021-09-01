init -1 python in weather:
    import urllib2
    import json
    import time
    import store

    #TEST API key, feel free to use
    #2c2f369ad4987a01f5de4c149665c5fd

    def string_to_dict(string):
        """
        Converts a string in dictionary format into a dictionary

        IN:
            string
        OUT:
            dictionary

        note: This automaticaly converts types
            E.G.:
                IN: "{x : 100}"

                OUT: {"x" : 100} instead of {"x" : "100"}
        """
        return json.loads(string)

    def get_api_call_url(api_key, parameters=dict()):
        """
        Creates a valid url(string) for an API call

        IN:
            key - (string) a valid API key
            parameters - (dictionary<string, string>) parameters to pass on to the API call
        OUT:
            API call url
        """

        # Check if key is valid
        if not isinstance(api_key, basestring):
            raise Exception("API key is type {0} instead of string".format(type(api_key)))

        # Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise Exception("parameters is {0} instead of a dictionary".format(type(parameters)))

        # base API call url
        url = "https://api.openweathermap.org/data/2.5/weather?"

        # Iterate through parameters
        for key in parameters:
            # Check that parameter contains a string key and value
            if not (isinstance(key, basestring) and isinstance(parameters[key], basestring)):
                raise Exception("parameters contain a non-string key and/or value")
            # Append parameter to url
            url += "{0}={1}&".format(key, parameters[key])

        # And lastly append API key
        url += "appid={0}".format(api_key)

        return str(url)

    def make_request(url):
        """
        Makes a request to url

        IN:
            url - <string>
        OUT:
            raw html

        note:
            This is intended to be used with OpenWeatherMap API as such
            if an HTTP error occurs the error code is returned in format {"cod" : [error code]}
            because of this, refrain from using it for other purposes
        """
        # Default response is None
        response = None
        # try to make a request
        # if successful
        ## set response to it's raw html
        try:
            request = urllib2.urlopen(url)
            response = request.read()
        # else
        ## return HTTP error code in an acceptable format
        except urllib2.HTTPError, err:
            response = "{{\"cod\":{0}}}".format(err.code)

        return response

    def get_api_call_info(key, parameters=dict()):
        """
            Creates an API call and returns the response as a dictionary

            IN:
                key - <string> a valid API key
                parameters - <dict> parameters to pass on to the API call
            OUT:
                API response - <dict>

            note: API key should already be validated
        """

        # Create an API call url with a valid API key and parameters
        url = get_api_call_url(key, parameters)
        # Create a request
        html = make_request(url)

        # Find first open brace
        start_index = html.find('{')
        # Find last close brace
        end_index = html.rfind('}')
        # Strip raw html, leaving only the API response
        content = html[start_index:end_index+1]

        # Convert response from a string to a dictionary and return it
        return string_to_dict(content)

    def get_response_code(key, parameters=dict()):
        """
            Returns API's response code

            IN:
                same as get_api_call_info()
            OUT:
                API response code - <int>

            note: This should be used only when validating stuff like API keys, locations, etc.
                  As this function makes a NEW API call
        """
        # Make an API call and get it's response
        content = get_api_call_info(key, parameters)

        # Return response code
        return content["cod"]

    def is_api_key_valid(key):
        """
            Checks whether an API key is valid or not

            IN:
                API key - string
            OUT:
                True - if key is valid
                False - if key is invalid

            note: Use this only when a key ~needs~ to be validated
                  If an API key has been validated before, assume it will stay like that
                  (This function makes a new API call)
        """
        # Get response code of API call
        response_code = get_response_code(key)

        # Check if response isn't "invalid API key" error code
        if response_code != 401:
            return True
        #else
        return False

    def is_city_valid(key, city):
        #NOTE: Deprecated
        """
            Checks whether city can be found by the API

            IN:
                city - (string) city name
            OUT:
                True - if city was found
                False - if city wasn't found

            note: same as in function above but with location
        """
        # Create an API call url with our API key
        params = get_location_dict(city=city)
        # Get response code of API call
        response_code = get_response_code(key, params)


        # Check if response isn't "city not found" error code
        if response_code != 404:
            return True
        #else
        return False

    def handle_other_errors(response_code):
        """
            Handles other common error codes

            IN:
                response code from an API call - <int>
        """
        if response_code == 429:
            store.utils.log("ERROR: OpenWeatherMap error 429. Exceeded rate limit of 60 calls/min.", store.utils.SEVERITY_ERR)
            raise Exception("exceeded 60 calls per minute! This shouldn't happen under any circumstances, needs fix now!")
            # TODO: do not raise an exception in production. Should be resolved in testing.

        if response_code in [500, 502, 503, 504]:
            store.utils.log("ERROR: API call to OpenWeatherMap resulted in {0} response code".format(response_code), store.utils.SEVERITY_ERR)
            # Something went horribly, horribly wrong
            # Good news tho! It's not our fault, yay!
            #TODO: Log whole API response for debugging purposes
            #TODO: Have Natsuki handle the situation in a non-immersion-breaking way
            ###### Probably ask the player if they could contact us

    def get_location_dict(longitude=None, latitude=None):
        """
            Returns a dictionary with player's latitude and longitude
            in a format understandable by OWM API
            note: coordinates should be stored as a string to avoid constant conversion

            IN:
                longitude - <string> longitude coordinates
                latitude - <string> latitude coordinates
            OUT:
                location - <dictionary>
        """

        location=dict()

        if longitude:
            location["lon"] = store.persistent.longitude

        if latitude:
            location["lat"] = store.persistent.latitude

        return location

    def get_parameters_for_call():
        """
            returns merged preferences and location dictionaries

            IN:
                preferences - <dictionary> containing stuff like what units to use, language etc.
                location - <dictionary> containing location info
            OUT:
                merged dictionary
        """
        # combine the two dictionaries without modifying either of them
        params = preferences.copy()
        params.update(
            get_location_dict(
            store.persistent.latitude,
            store.persistent.longitude
            )
        )

        return params

    def set_next_weather_call_time(seconds):
        """
        Sets a time next OWM API call should be made

        IN:
            in how many seconds should it be called

        note: is a function solely for easier queuing in renpy dialogue
        """
        store.persistent.next_weather_call_time = time.time()+seconds

    #TODO: persist this
    preferences = {
        "units" : "metric"
    }

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
            params = get_parameters_for_call()
            try:
                response = get_api_call_info(store.persistent.weather_api_key, params)
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
                    drizzle : intensity of a drizzle (article correct?)
                    rain    : intensity of rain
                    snow    : intensity of snowing
                    clouds  : percentage of cloud sky coverage
                    clear   : True or False
                    special : special weather events (dust storm, tornado, volcanic ash etc.), can be None
                    "wind"  : wind speed in m/s
                    "temp"  : temperature in °C
            """
            params = get_parameters_for_call()

            # try to make an API call
            try:
                response = get_api_call_info(store.persistent.weather_api_key, params)
                store.utils.log("INFO: Made succesfull API call to OpenWeatherMap")
            except Exception as e:
                store.utils.log("ERROR: While making an API call to OpenWeatherMap an exception occured. {0}".format(e), store.utils.SEVERITY_ERR)

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

            return parsed_weather, weather_short

init -1 python:
    import webbrowser
    import os
    import subprocess
    import time

    def open_browser(url):
        """
            Opens a new tab/window in the default browser with the specified url

            IN:
                url - <string>
        """
        webbrowser.open(url)


    def open_maps(latitude, longitude):
        """
            Opens google maps in a new tab/window in the default browser with specified coordinates
        """
        url = "https://www.google.com/maps/place/{0},{1}".format(latitude, longitude)
        webbrowser.open(url)

    def open_txt(file):
        """
            Opens a txt file in default txt editor
        """
        os.startfile(file)

    def txt_input(pre_format_string=""):
        """
            Creates a new temporary txt file and opens it in default txt editor
            File will have pre_format_string written in it before opening the file
            Then it will wait until the user closes it
            Returns what the user typed in or None if file doesn't start with pre_format_string
            Deletes both the temporary text file and it's temporary folder parent

            note: should be used only when user is expected to need to paste something
                  otherwise use renpy.input()

            IN:
                pre_format_string - <string> a pre-formated string
            OUT:
                user's input<string> or <None>
        """
        #NOTE: might not be necessary to create a new folder for it
        ###### is done purely to avoid possible issue with overwriting an existing file
        if not os.path.exists(".temp_input"):
            os.makedirs(".temp_input")

        # Create a new file in our new folder
        file = open(".temp_input\\__temp_input__.txt", "w")
        # If for some reason the file already existed, delete it's content
        file.truncate(0)
        # Write our preformatted string into it
        file.write(pre_format_string)
        file.close()

        # Make a new proccess that opens our file (sorry for wrong terminology)
        process = subprocess.Popen(["notepad.exe", ".temp_input\\__temp_input__.txt"])
        # Wait until process is terminated
        process.wait()
        # When file is closed open it and read it's content
        file = open(".temp_input\\__temp_input__.txt", "r")
        content = file.read()
        #if file still starts with our preformatted string
        ## strip it's content of the pre-format string
        if content[:len(pre_format_string)] == pre_format_string:
            content = content[len(pre_format_string):]

        else:
            content = None
        # close file, delete it, delete it's parent folder
        file.close()
        os.remove(".temp_input\\__temp_input__.txt")
        os.rmdir(".temp_input")

        return content

init -1 python in location:
    import geocoder
    import store

    def get_coords_by_ip():
        """
            Returns coordinates tuple based on users ip adress
            note: for accuracy issues and possibility of VPN usage this should be used only if other methods fail

            OUT:
                (latitude, longitude) or None if fail
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
