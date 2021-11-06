label ch30_autoload:
    #Start with black scene
    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False

    #Do all the things here for initial setup/flow hijacking

    #FALL THROUGH

label ch30_holiday_check:
    #Run holiday checks and push/setup holiday related things here

    #FALL THROUGH

label ch30_visual_setup:
    $ main_background.draw(True)

    #FALL THROUGH

label ch30_init:

    python:      
        # Determine if the player should get a prolonged leave greeting
        if (datetime.datetime.now() - persistent.jn_last_visited_date).total_seconds() / 604800 >= 1:
            persistent.last_apology_type = apologies.APOLOGY_TYPE_PROLONGED_LEAVE

        # Add to the total visits counter and set the last visit date
        persistent.jn_total_visit_count += 1
        persistent.jn_last_visited_date = datetime.datetime.now()

    # Let's pick a greeting
    $ push(greetings.select_greeting())

    # Draw background and placeholder sprites
    $ main_background.draw(full_redraw=True)

    if utils.get_current_hour() > 6 and utils.get_current_hour() < 18:
        show placeholder_sky_day zorder jn_placeholders.SKY_Z_INDEX
    else:
        hide placeholder_sky_day
    
    show screen hkb_overlay

    # Do all var-sets, resets, and sanity checks prior to entering the loop here

    # Reset the previous admission/apology, now that Natsuki will have picked a greeting
    $ persistent.jn_player_admission_type_on_quit = None
    $ persistent.jn_player_apology_type_on_quit = None

    #And finally, we head into the loop
    jump ch30_loop

#The main loop
label ch30_loop:

    #Run our checks
    python:
        _now = datetime.datetime.now()
        if LAST_MINUTE_CHECK.minute is not _now.minute:
            minute_check()
            LAST_MINUTE_CHECK = _now

        if LAST_HOUR_CHECK is not _now.hour:
            hour_check()
            LAST_HOUR_CHECK = _now.hour

        if LAST_DAY_CHECK is not _now.day:
            day_check()
            LAST_DAY_CHECK = _now.day

        #We'll also check if we need to redraw the room
        #main_background.check_redraw()

    #Now, as long as there's something in the queue, we should go for it
    while persistent._event_list:
        call call_next_topic

    #FALL THROUGH

label ch30_wait:
    window hide
    $ renpy.pause(delay=5.0, hard=True)
    jump ch30_loop

#Other labels
label call_next_topic:

    if persistent._event_list:
        $ _topic = persistent._event_list.pop(0)

        if renpy.has_label(_topic):
            
            if _topic in ["greeting_sudden_leave", "greeting_prolonged_leave"]:
                show placeholder_natsuki plead zorder jn_placeholders.NATSUKI_Z_INDEX

            elif "greeting_" in _topic:
                $ jn_placeholders.show_greeting_placeholder_natsuki()

            else:
                $ jn_placeholders.show_resting_placeholder_natsuki()
                
            call expression _topic

    python:
        #Collect our return keys here
        #NOTE: This is instance checked for safety
        return_keys = _return if isinstance(_return, dict) else dict()

        topic_obj = get_topic(_topic)

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

    jump ch30_loop

init python:
    LAST_MINUTE_CHECK = datetime.datetime.now()
    LAST_HOUR_CHECK = LAST_MINUTE_CHECK.hour
    LAST_DAY_CHECK = LAST_MINUTE_CHECK.day

    _NAT_SAYS = 0
    _PLAYER_SAYS = 1

    _SAYS_RANGE = [
        _NAT_SAYS,
        _PLAYER_SAYS
    ]

    def minute_check():
        """
        Runs every minute during breaks between topics
        """

        # Push a new topic every couple of minutes
        if datetime.datetime.now().minute % 2 is 0:
            topic_pool = Topic.filter_topics(
                topics.TOPIC_MAP.values(),
                unlocked=True,
                nat_says=True,
                location=main_background.location.id,
                affinity=jn_affinity.get_affinity_state(),
            )

            if topic_pool:
                queue(random.choice(topic_pool).label)
        pass

    def hour_check():
        """
        Runs ever hour during breaks between topics
        """
        pass

    def day_check():
        """
        Runs every day during breaks between topics
        """
        pass

label talk_menu:
    python:
        import pprint

        # Get the flavor text for the talk menu, based on affinity state
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_LOVE_ENAMORED)

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_AFFECTIONATE_NORMAL)

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_UPSET_DISTRESSED)

        else:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_BROKEN_RUINED)            

        # Ensure any variable references are substituted
        _talk_flavor_text = renpy.substitute(_talk_flavor_text)

    $ jn_placeholders.show_resting_placeholder_natsuki(offset=True)

    menu:
        n "[_talk_flavor_text]"

        "Let's talk about...":
            call player_select_topic

        "Tell me again about...":
            call player_select_topic(is_repeat_topics=True)

        "I feel..." if jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            jump player_admissions_start

        "I want to tell you something..." if jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            jump player_compliments_start

        "I want to apologize...":
            jump player_apologies_start

        "Goodbye.":
            jump farewell_start

        "Nevermind.":
            $ jn_placeholders.show_resting_placeholder_natsuki()
            jump ch30_loop
    return

label player_select_topic(is_repeat_topics=False):
    python:
        _topics = Topic.filter_topics(
            topics.TOPIC_MAP.values(),
            nat_says=is_repeat_topics,
            player_says=not is_repeat_topics,
            unlocked=True,
            location=main_background.location.id,
            affinity=jn_affinity.get_affinity_state()
        )

        # Sort the topics we can pick by prompt for a cleaner appearance
        _topics.sort(key=lambda topic: topic.prompt)

        # Present the topic options grouped by category to the player
        menu_items = menu_dict(_topics)

    call screen categorized_menu(menu_items,(1020, 70, 250, 572), (740, 70, 250, 572), len(_topics))

    $ _choice = _return
    $ utils.log("_choice is {0}".format(_choice))

    # We got a string, we should push
    if isinstance(_choice, unicode):

        $ push(str(_choice))
        $ jn_placeholders.show_resting_placeholder_natsuki()
        jump call_next_topic

    # -1 means go back
    elif _choice == -1:
        jump talk_menu

    # Clear _return
    $ _return = None
    $ jn_placeholders.show_resting_placeholder_natsuki()

    jump ch30_loop

label music_menu:
    n "This isn't done."
    jump ch30_loop

label extras_menu:
    n "This isn't done."
    jump ch30_loop
