init -2 python in api:
    import json
    import urllib2
    import store

    #NOTE: I don't really like having a dictionary like this, but I can't think of a better way
    # except of maybe using the base_url itself instead of just the API name, that just seems annoying though
    APIs = {
        "OpenWeatherMap" : "https://api.openweathermap.org/data/2.5/weather"
    }
    def make_request(api):
        """
            Makes a request to an API, this should only be used with an API

            IN:
                api - <string>
            OUT:
                <dict> {"status" : response_code, "html" : raw_html, "custom": ...}
                    custom - whatever is returned by a function defined with API_on_status_code decorator
        """
        if not api in store.api.APIs:
            raise Exception("API {0} not found".format(api))

        base_url = store.api.APIs[api]

        # this feels very janky
        response = {
            "status" : None,
            "html" : None,
            "custom" : None
        }

        # make a request and get response code
        request = urllib2.urlopen(url)
        code = request.getcode()

        # if status OK read html
        if code == 200:
            response["html"] = request.read()

        response["status"] = code
        response["custom"] = API_respond_2_code(api, code)

        """TODO:remove this, just keeping it here for reference
        except urllib2.HTTPError, err:
            response = "{{\"cod\":{0}}}".format(err.code)
        """

        return response

    def get_api_call_url(base_url, parameters=dict(), **kwargs):
        """
        Creates a valid url for an API call

        IN:
            base_url - <string> example: https://www.google.com/
            parameters - <dict> parameters to pass on to the API call
            kwargs - keyword arguments also passed to the url
        OUT:
            url - <string>
        """
        # check if base_url is a string
        if not isinstance(base_url, str):
            raise Exception("base_url is {0}, string was expected".format(type(base_url)))

        # Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise Exception("parameters is {0}, dictionary was expected".format(type(parameters)))

        # base API call url
        # merge parameters and kwargs
        url = base_url + '?'
        parameters.update(kwargs)

        # Iterate through parameters and append them to url
        for key, value in parameters.items():

            url += "{0}={1}&".format(key, value)

        return url

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


    #I think this is what you meant Multi?
    #also just realized API might be a bad arg name because it suggests it's a constant?
    #also the more I look at this the more confused and less confident that this is correct I get... oh well
    def API_on_status_code(API, codes):
        """
            decorator used for calling functions based on HTTP response codes

            IN:
                API - <string> with which API is this function associated
                codes - <int/list/set/range> response codes on which this function should be called
            NOTE: function should not accept any positional arguments
        """
        # if this is the first time the decorator is used we first instantiate the registry
        if not hasattr(API_on_status_code, "all"):
            API_on_status_code.all = dict()

        # if API is not yet in registry, add it
        if not API in API_on_status_code.all:
            API_on_status_code.all[API] = dict()

        # make codes an iterable if it isn't yet
        if not isinstance(codes, (list, set, range)):
            codes = [codes]

        def registered(func):
            for code in codes:
                # check if code is an integer
                if not isinstance(codes, int):
                    raise Exception("API_on_status_code accepts only integers for response codes")

                #TODO: this can be optimized using `func.func_code.co_varnames`
                def wrapper(code=code):
                    # try to pass `code` to the function
                    # if this fails call it without any arguments
                    try:
                        return func(code)
                    except TypeError:
                        return func()

                # add wrapped function to our dictionary
                API_on_status_code.all[API][code] = wrapper

            return func

        return registered

    def API_respond_2_code(API, code):
        if API not in API_on_status_code.all:
            return

        if code not in API_on_status_code.all[API]:
            return

        return API_on_status_code.all[API][code]()

    def open_browser(url):
        """
            Opens a new tab/window in the default browser with the specified url

            IN:
                url - <string>
        """
        webbrowser.open(url)
