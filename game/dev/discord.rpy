default persistent.jn_discord_user_id = None
default persistent.jn_discord_api_key = None

init python in jn_discord:
    import requests
    import random
    import store
    import store.utils as utils

    _API_URL = "https://xg8lifnd19.execute-api.eu-west-1.amazonaws.com/v1/send-message"

    def send_message(message):
        """
        Sends the given message to Discord, substituting any variables using renpy.substitute, using Blizzardsev's Ryo API.
        The message is delivered to the user as found by the user id specified under persistent.jn_discord_user_id.
        Response if not successful is delivered to the log.

        IN:
            - message - message to deliver to Discord
        """
        if store.persistent.jn_discord_user_id:
            response = requests.post(
                url=_API_URL,
                json={
                    "user_id": store.persistent.jn_discord_user_id,
                    "message": renpy.substitute(message)
                },
                headers={
                    "x-api-key": store.persistent.jn_discord_api_key                
                }
            )

            if response.status_code != 200:
                utils.log(message="Ryo API call for Discord DM failed; status code was: {0}".format(response.status_code), logseverity=utils.SEVERITY_ERR)

label test_discord:
    n 1fnmbg "Ooh!{w=0.2} Okay!{w=0.2} I'll send you a message..."
    n 1fchsm "...{nw}"
    $ tease_emote = random.choice(jn_globals.DEFAULT_TEASE_EMOTICONS)
    $ jn_discord.send_message("[player] is a beeg dum-dum~ [tease_emote]")
    n 1uchsm "...And there we go!{w=0.2} Did you get it,{w=0.1} [player]?"
    n 1fsqsm "Ehehe."
    jump ch30_loop
