# This basically sorts out the pathing that requests needs to use certifi, in order to perform requests to HTTPS URLs.
# Credit and big thanks to Booplicate @ https://github.com/Booplicate for their kind assistance!

init -999:
    python:
        import os
        os.environ['SSL_CERT_FILE'] = renpy.config.gamedir + "/python-packages/certifi/cacert.pem"
