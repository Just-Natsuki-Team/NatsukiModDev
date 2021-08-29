init python in topic_handler:
    import store

    normal_topic_map = dict()

    #Add to this as needed for more databases
    TOPIC_CODE_MAP = {
        store.TOPIC_TYPE_GREETING: store.greetings.GREETING_MAP,
        store.TOPIC_TYPE_FAREWELL: store.farewells.FAREWELL_MAP,
        store.TOPIC_TYPE_NORMAL: store.topics.TOPIC_MAP,
        store.TOPIC_TYPE_ADMISSION: store.admissions.ADMISSION_MAP
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

    def pick_random_topic(
        label=None,
        prompt=None,
        conditional=None,
        category=None,
        unlocked=None,
        nat_says=None,
        player_says=None,
        affinity=None,
        trust=None,
        location=None,
        additional_properties=None
    ):
        """
        Picks a random topic with optional filters

        IN(optional):
                label - renpy label (as string) this topic corresponds to
                prompt - string representing the prompt to use for this topic in menus
                conditional - condition under which this topic should be allowed to be shown
                category - list of strings representing categories to group this topic under.
                unlocked - whether or not this topic is displayed to the user in menus
                nat_says - whether or not this topic will be brought up by Natsuki
                player_says - whether or not this topic is to be prompted by the player
                location - location this topic is bound to. If None, it can be shown in all locations
                additional_properties - dictionary representing additional properties which don't directly affect the topic itself.
        OUT:
            random topic passing all filters
        """
        filtered_topics = Topic.filter_topics(
            topics.TOPIC_MAP.values(),
            unlocked=None,
            nat_says=None,
            player_says=None,
            affinity=None,
            trust=None,
            location=None
        )

        return random.choice(filtered_topics).label if filtered_topics else None

    #TODO: Remove this once the new menus are implemented
    def get_all_topics(
        label=None,
        prompt=None,
        conditional=None,
        category=None,
        unlocked=None,
        nat_says=None,
        player_says=None,
        affinity=None,
        trust=None,
        location=None,
        additional_properties=None
    ):
        """
        return all topics passing optional filters

        IN(optional):
            label - renpy label (as string) this topic corresponds to
            prompt - string representing the prompt to use for this topic in menus
            conditional - condition under which this topic should be allowed to be shown
            category - list of strings representing categories to group this topic under.
            unlocked - whether or not this topic is displayed to the user in menus
            nat_says - whether or not this topic will be brought up by Natsuki
            player_says - whether or not this topic is to be prompted by the player
            location - location this topic is bound to. If None, it can be shown in all locations
            additional_properties - dictionary representing additional properties which don't directly affect the topic itself.
        OUT:
            topics passing all filters
        """

        filters = {
            "label" : label,
            "label" : prompt,
            "conditional" : conditional,
            "category" : category,
            "unlocked" : unlocked,
            "nat_says" : nat_says,
            "player_says" : player_says,
            "affinity_range" : affinity,
            "trust_range" : trust,
            "location" : location,
            "additional_properties" : additional_properties
        }
        filtered_topics = []
        passed = True

        for topic in topics.TOPIC_MAP.values():
            #TODO: Same comment as above
            for filter_ in filters:
                if filters[filter_] == None:
                    continue
                elif (
                    filter_ != 'affinity_range'
                    and filter_ != 'trust_range'
                ):
                        if getattr(topic, filter_) != filters[filter_]:
                            passed = False
                            break
                else:
                    range_ = getattr(topic, filter_)
                    if range_ == None:
                        continue
                    elif range_[0] != None and range_[1] == None:
                        if range_[0] <= filters[filter_]:
                            continue
                    elif range_[0] == None and range_[1] != None:
                        if filters[filter_] <= range_[1]:
                            continue
                    elif range_[0] <= filters[filter_] <= range_[1]:
                        continue
                    else:
                        passed = False
                        break


            if passed:
                filtered_topics.append(topic)
            passed = True
        return filtered_topics
