init -1 python:
    import urllib2
    import json

    #TEST API key, feel free to use
    #2c2f369ad4987a01f5de4c149665c5fd

    def string_to_dict(string):
        """
        Converts a string in dictionary format into a dictionary

        IN:
            string
        OUT:
            dictionary
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
            raise Exception("API key not string")

        # Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise Exception("argument isn't a dictionary")

        # base API call url
        url = "https://api.openweathermap.org/data/2.5/weather?"

        # Iterate through parameters
        for key in parameters:
            # Check that parameter contains a string key and value
            if not (isinstance(key, basestring) and isinstance(parameters[key], basestring)):
                raise Exception("parameters contain a non-string key or value")
            # Append parameter to url
            url += "{0}={1}&".format(key, parameters[key])

        # And lastly append API key
        url += "appid={0}".format(api_key)

        return url

    def get_api_call_info(key, parameters):
        url = get_api_call_url(key, parameters)
        # Convert response from a string to a dictionary

        request = urllib2.urlopen(url)
        html = request.read()
        start_index = html.find('{')
        end_index = html.rfind('}')
        content = html[start_index:end_index+1]
        request.close()

        return string_to_dict(content)

    def get_response_code(key, parameters=dict):
        url = get_api_call_url(key, parameters)
        # Convert response from a string to a dictionary

        request = urllib2.urlopen(url)
        html = request.read()
        start_index = html.find('{')
        end_index = html.rfind('}')
        content = html[start_index:end_index+1]
        request.close()

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
        """
        # Get response code of API call
        response_code = get_response_code(key)

        # Check if response isn't "invalid API key" error code
        if response_code != 401:
            return True
        #else
        return False

    def is_city_valid(key, city):
        """
            Checks whether city can be found by the API

            IN:
                city - (string) city name
            OUT:
                True - if city was found
                False - if city wasn't found
        """
        # Create an API call url with our API key
        params = {
            "q" : city
        }
        # Get response code of API call
        response_code = get_response_code(key, params)


        # Check if response isn't "city not found" error code
        if response_code != 404:
            return True
        #else
        return False

    def handle_other_errors(response_code):
        if response_code == 429:
            raise Exception("exceeded 60 calls per minute! This shouldn't happend under any circumstances, needs fix now!")
            # we are exceeding rate limit of 60 calls/min
            # needs to be fixed ASAP!

        if response_code in [500, 502, 503, 504]:
            pass
            # Something went horribly, horribly wrong
            # Good news tho! It's not our fault, yay!
            #TODO: Have Natsuki handle the situation in a non-immersion-breaking way
            #      Probably ask the player if they could contact us

    def get_new_location(city=None, country=None, zip_code=None, longitude=None, latitude=None):
            location=dict()

            if city:
                location["q"] = city

            if country:
                location["country"] = country

                if zip_code:
                    location["zip"] = zip_code

            if longitude:
                location["lon"] = longitude

            if latitude:
                location["lat"] = latitude

            return location

    def get_parameters_for_call():
        params = preferences.copy()
        params.update(location)

        return params

    city = "london"
    longitude = None
    latitude = None
    country = None
    zip_code = None
    api_key = "2c2f369ad4987a01f5de4c149665c5fd"

    preferences = {
        "units" : "metric"
    }

    location = get_new_location(city, country, zip_code, longitude, latitude)

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
            params = get_parameters_for_call()

            response = get_api_call_info(api_key, params)
            pass
            return response["weather"][0]["main"]

        @staticmethod
        def get_weather_detail():
            params = get_parameters_for_call()

            response = get_api_call_info(api_key, params)

            weather_info = response["weather"][0]
            clouds_info = response["clouds"]["all"]

            parsed_weather = Weather.WEATHER_TABLE[weather_info["id"]]

            parsed_weather["clouds"] = clouds_info

            return parsed_weather

    Weather.get_weather()
    Weather.get_weather_detail()
