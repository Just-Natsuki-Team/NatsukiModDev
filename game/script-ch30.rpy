#Aaa this code is so clean!!!!! I really need to learn how to write like this! -Daisy

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
    #Let's pick a greeting
    $ push(greetings.select_greeting())

    show mask_2 zorder 1
    show mask_3 zorder 1
    show monika_room zorder 2
    show natsuki a zorder 3
    show screen hkb_overlay
    #Do all var-sets, resets, and sanity checks prior to entering the loop here

    #And finally, we head into the loop
    jump ch30_loop

#The main loop
label ch30_loop:
    #Do topic selection here
    $ queue(pick_random_topic(unlocked=True, player_says=False))

    #Run our checks
    python:
        _now = datetime.datetime.now()
        if LAST_MINUTE_CHECK.minute < _now.minute < LAST_MINUTE_CHECK.minute:
            minute_check()
            LAST_MINUTE_CHECK = _now

        if LAST_HOUR_CHECK < _now.hour < LAST_HOUR_CHECK:
            hour_check()
            LAST_HOUR_CHECK = _now.hour

        if LAST_DAY_CHECK < _now.day < LAST_DAY_CHECK:
            day_check()
            LAST_DAY_CHECK = _now.day

        #We'll also check if we need to redraw the room
        #no day/night room images yet
        #main_background.check_redraw()

    #Now, as long as there's something in the queue, we should go for it
    while persistent._event_list:
        call call_next_topic

    jump ch30_loop
    

label ch30_wait:
    window hide
    $ renpy.pause(delay=5.0, hard=True)
    jump ch30_loop


init python:
    LAST_MINUTE_CHECK = datetime.datetime.now()
    LAST_HOUR_CHECK = LAST_MINUTE_CHECK.hour
    LAST_DAY_CHECK = LAST_MINUTE_CHECK.day

    def minute_check():
        """
        Runs every minute during breaks between topics
        """
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

#Other labels
label call_next_topic:
    if persistent._event_list:
        $ topic = persistent._event_list.pop(0)

        if renpy.has_label(topic):
            call expression topic

    python:
        #Collect our return keys here
        return_keys = _return if _return else dict()

        topic_obj = get_topic(topic)

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



label ch30_talk:
    python:
        choice=None
        menu_items=[]
        for topic in topics.TOPIC_MAP.values():
            if topic.unlocked and topic.player_says == True:
                menu_items.append((topic.prompt, topic.label))

        menu_items.append(("Nevermind", "ch30_loop"))
        menu_items.append(("Goodbye", farewells.select_farewell()))
        choice = menu(menu_items)
        push(choice)
    jump ch30_loop