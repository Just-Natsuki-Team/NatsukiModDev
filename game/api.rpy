init -2 python in api:
    import json
    import urllib2
    import store

    #NOTE: I don't really like having a dictionary like this, but I can't think of a better way
    # except of maybe using the base_url itself instead of just the API name, that just seems annoying though
    APIs = {
        "OpenWeatherMap" : "https://api.openweathermap.org/data/2.5/weather"
    }

    def make_request(api, parameters=None, **kwargs):
        """
            Makes a request to an API

            IN:
                api - <string>
            OUT:
                <dict> {"status" : response_code, "html" : raw_html, "custom": ...}
                    custom - whatever is returned by a function defined with API_on_status_code decorator
        """
        if parameters is None: parameters = dict()

        if not api in store.api.APIs:
            raise Exception("API {0} not found".format(api))

        url = get_api_call_url(api, parameters, **kwargs)

        # this feels very janky
        response = {
            "status" : None,
            "html" : None,
            "custom" : None
        }

        # make a request and get response code
        try:
            request = urllib2.urlopen(url)
            code = request.getcode()
            response["html"] = request.read()
        except urllib2.HTTPError as err:
            code = err.code

        # if status OK read html
        if code == 200:
            store.utils.log("API call to {0} resulted in response 200".format(api))

        else:
            store.utils.log("API call to {0} resulted in response {1}".format(api, code), store.utils.SEVERITY_WARN)

        response["status"] = code
        response["custom"] = API_respond_2_code(api, code, response["html"])

        return response

    def get_api_call_url(api, parameters=None, **kwargs):
        """
        Creates a valid url for an API call

        IN:
            api - <string> api from APIs dictionary
            parameters - <dict> parameters to pass on to the API call
            kwargs - keyword arguments also passed to the url (merged with `parameters`)
        OUT:
            url - <string>
        """
        if parameters is None: parameters = dict()

        # check if base_url is a string
        if api not in store.api.APIs:
            raise Exception("API {0} not found".format(api))

        # Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise Exception("parameters is {0}, dictionary was expected".format(type(parameters)))

        # add quarry separator to url
        url = store.api.APIs[api] + '?'
        # merge parameters and kwargs
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
    def API_on_status_code(API, codes=None):
        """
            decorator used for calling functions based on HTTP response codes

            IN:
                API - <string> with which this function is associated
                codes - <int/list(range)/set> response codes on which this function should be called
                        if None, function will be called if API call results in a code that isn't in registry
            NOTE:
                function can accept `code` and `html` keyword arguments
                function should not accept any positional arguments
        """
        # if this is the first time the decorator is used we first instantiate the registry
        if not hasattr(API_on_status_code, "all"):
            API_on_status_code.all = dict()

        # if API is not yet in registry, add it
        if not API in API_on_status_code.all:
            API_on_status_code.all[API] = dict()

        # make codes an iterable if it isn't yet
        if not isinstance(codes, (list, set)):
            codes = [codes]

        def registered(func):
            for code in codes:
                # check if code is an integer
                if code is not None and not isinstance(code, int):
                    raise Exception("API_on_status_code accepts only integers for response codes")

                # Now we wrap our function based on what keyword args it accepts
                # Wrapper always accepts the same arguments to avoid possible integrity issues
                ## First we check what keyword arguments it accepts
                ## we try to pass it those args
                ## if it still for some reason fails we call it without any args

                func_args = func.func_code.co_varnames
                # Both code and html
                if "code" in func_args and "html" in func_args:
                    def wrapper(code=code, html=None):
                        try:
                            return func(code=code, html=html)
                        except TypeError:
                            return func()
                    # add wrapped function to our dictionary
                    API_on_status_code.all[API][code] = wrapper
                    continue

                # Only code
                if "code" in func_args:
                    def wrapper(code=code, html=None):
                        try:
                            return func(code=code)
                        except TypeError:
                            return func()
                    # add wrapped function to our dictionary
                    API_on_status_code.all[API][code] = wrapper
                    continue

                # Only html
                if "html" in func_args:
                    def wrapper(code=code, html=None):
                        try:
                            return func(html=html)
                        except TypeError:
                            return func()
                    # add wrapped function to our dictionary
                    API_on_status_code.all[API][code] = wrapper
                    continue

                # not html nor code
                def wrapper(code=code, html=None):
                    return func()
                # add wrapped function to our dictionary
                API_on_status_code.all[API][code] = wrapper

            return func

        return registered

    def API_respond_2_code(API, code, html=None):
        """
            calls a function from registry of callback funcs for APIs
        """
        # No function with decorator defined
        if not hasattr(API_on_status_code, "all"):
            return

        # API is not in registry so return None
        if API not in API_on_status_code.all:
            return

        if code not in API_on_status_code.all[API]:
            # code was not found in registry but registry contains a generic fallback
            if None in API_on_status_code.all[API]:
                return API_on_status_code.all[API][None](code=code, html=html)
            # no generic nor code specific callback, return None
            return

        # both API and code in registry so we call that function
        return API_on_status_code.all[API][code](code=code, html=html)

    def open_browser(url):
        """
            Opens a new tab/window in the default browser with the specified url

            IN:
                url - <string>
        """
        webbrowser.open(url)
