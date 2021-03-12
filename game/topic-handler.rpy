init python in topic_handler:
    import store

    normal_topic_map = dict()

    #Add to this as needed for more databases
    TOPIC_CODE_MAP = {
        store.TOPIC_TYPE_GREETING: store.greetings.GREETING_MAP,
        store.TOPIC_TYPE_FAREWELL: store.farewells.FAREWELL_MAP,
        store.TOPIC_TYPE_NORMAL: store.topics.TOPIC_MAP
    }

init 6 python in topic_handler:
    ALL_TOPIC_MAP = dict()

    #Add everything to the all-in-one map
    for topic_map in TOPIC_CODE_MAP.itervalues():
        ALL_TOPIC_MAP.update(topic_map)

init 6 python:
    import random
    #Now let's define some utility functions
    def get_topic(topic_label):
        """
        Gets a Topic object by its label

        IN:
            topic_label - Topic.label representing the label of the topic we wish to get

        OUT:
            Topic if a topic with the
        """
        return store.topic_handler.ALL_TOPIC_MAP.get(topic_label, None)

    def pick_random_topic():
        """
        Picks a random topic

        TODO: Build filters and such
        """
        #For now, return a random topic
        return random.choice(topics.TOPIC_MAP.keys())

label call_next_topic:
    if persistent._event_list:
        $ topic = persistent._event_list.pop(0)

        if renpy.has_label(topic):
            call expression topic

    python:
        #Collect our return keys here
        return_keys = _return if _return else dict()

        topic_obj = pick_random_topic()

        #Handle all things which act on topic objects here, since we can't access attributes of Nonetypes
        if topic_obj is not None:
            #Increment shown count
            topic_obj.shown_count += 1

            #Now manage return keys
            if "derandom" in return_keys:
                topic_obj.random = False

    #This topic might quit
    if "quit" in return_keys:
        jump _quit

    return
