label ch30_autoload:
    #Do all the things here for initial setup/flow hijacking

    #FALL THROUGH

label ch30_holiday_check:
    #Run holiday checks and push/setup holiday related things here

    #FALL THROUGH

label ch30_visual_setup:
    $ main_background.draw(True)

    #FALL THROUGH

label ch30_init:
    #Do all var-sets, resets, and sanity checks prior to entering the loop here

    #And finally, we head into the loop
    jump ch30_loop

#The main loop
label ch30_loop:
    #Do topic selection here
    #TODO: jump pick_random_topic

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
        main_background.check_redraw()

    #Now, as long as there's something in the queue, we should go for it
    while persistent._event_list:
        call call_next_topic

    #FALL THROUGH

label ch30_wait:
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
