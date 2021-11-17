init -2 python in api:
    def make_request(url):
        """
            Makes a request to url

            IN:
                url - <string>
            OUT:
                <dict> {"status" : response_code, "html" : raw_html}
        """
        # Default response is None
        response = {
            "status" : 200,
            "html" : None
        }
        # try to make a request
        # if successful
        ## set response to it's raw html
        try:
            request = urllib2.urlopen(url)
            response["html"] = request.read()
        # else
        ## return HTTP error code in an acceptable format
        except urllib2.HTTPError as err:
            response["status" : err]
        """
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
