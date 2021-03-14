default persistent._farewell_database = dict()

init python in farewells:
    import random
    FAREWELL_MAP = dict()

    def select_farewell():
        """
        Picks a random greeting
        """
        #TODO: ME (for now this just returns a random)
        return random.choice(FAREWELL_MAP.keys())

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_see_ya",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_see_ya:
    n "See you soon!"
    $ renpy.quit()
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_bye",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_bye:
    n "Byee!"
    $ renpy.quit()
    return
