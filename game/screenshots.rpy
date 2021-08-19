init 0 python:
    #from datetime import datetime
    from enum import Enum
    import random

    # Check and create the screenshot directory
    _screenshot_dir = os.path.join(renpy.config.basedir, "screenshots")
    if not os.path.exists(_screenshot_dir):
        os.makedirs(_screenshot_dir)

    # Prevent the player from taking screenshots within the screenshot dialogue tree
    _player_screenshot_in_progress = False

    # Tracking
    bad_screenshot_streak = 0
    player_screenshots_permission = False

    # Prevent the player from taking screenshots completely
    player_screenshots_blocked = False

    # Reaction/response permutations so Natsuki feels more dynamic

    # LOVE - ENAMORED
    love_enamored_reactions = [
        "[player]...{w=0.3} you remember what I said about pictures, right?",
        "[player]...{w=0.3} did you forget what I said?",
        "[player]...{w=0.3} I think you forgot something.",
        "Hey...{w=0.3} do you remember when we talked about taking pictures?",
        "[player],{w=0.1} come on. We talked about this..."
    ]

    love_enamored_responses = [
        "I really don't like being surprised with pictures when I don't expect it.",
        "I really don't like having pictures taken without my permission.",
        "I really don't like having pictures taken without my consent.",
        "Surprise pictures make me feel uneasy.",
        "I want to know when you're going to take a picture of me."
    ]

    # AFFECTIONATE - NORMAL
    affectionate_normal_reactions = [
        "[player]!{w=0.2} What're you doing?!",
        "A-ah!{w=0.2} [player]!",
        "H-hey!{w=0.2} [player]!",
        "E-excuse me!",
        "Hey!",
        "W-what?! [player]!",
        "Kyaaahh!{w=0.2} Why?!"]

    affectionate_normal_responses = [
        "You didn't say you were going to take a picture!",
        "I thought I told you to ask if you wanted pictures?",
        "I don't like surprise pictures,{w=0.1} remember?!"
    ]   

    # UPSET-
    upset_minus_reactions = [
        "Would you stop?!",
        "Okay, okay! Stop!",
        "Hey! Cut it out!",
        "[player]!{w=0.2} Knock it off!",
        "[player]!{w=0.2} Stop it!",
        "[player]!{w=0.2} Quit it already!",
        "Okay, enough already!",
        "Alright, that's enough!",
        "Ugh! Give it a rest,{w=0.1} [player]!",
        "[player]!{w=0.2} Can you stop?!",
        "I'm getting real tired of that,{w=0.1} [player]!"]    

    upset_minus_responses = [
        "If I didn't give you permission,{w=0.1} it means I don't want you to do it!",
        "I told you to ask if you wanted pictures!",
        "Don't you listen?!{w=0.2} I said you should ask if you want pictures of me!",
        "I thought I made it clear I don't want surprise pictures!"
    ]

    # Add the keymap for screenshots
    jn_register_label_keymap("attempt_screenshot", "screenshot_dialogue", "s")

# Attempt to produce a screenshot, render associated effects
label take_screenshot:
    
    if store.jn_affinity.get_affinity_state() >= store.jn_affinity.BROKEN:
        $ renpy.screenshot("{0}/screenshot_{1}.png".format(_screenshot_dir, datetime.datetime.now().strftime(r"%d-%m-%Y_%H-%M-%S"))) # WIP; pictures will need to go to a sensible (local!) location
        $ utils.log("Screenshot taken by player at {0}".format(datetime.datetime.now().strftime(r"%d/%m/%Y, %H:%M")))
    
    else:
        n "No, [player].{w=0.1} I'm keeping that turned off."
        return
    
    hide window
    play audio camera_shutter
    with Fade(.15, 0, .50, color="#fff")
    return

# Handles dialogue and mechanics related to screenshots
label screenshot_dialogue:

    if _player_screenshot_in_progress:
        # Don't take a screenshot if we're already going through the dialogue!
        return

    else:
        $ _player_screenshot_in_progress = True

    if persistent.jn_first_screenshot_taken is None:

        # Set the date for the first ever screenshot, play the camera effects
        $ persistent.jn_first_screenshot_taken = datetime.datetime.now()
        call take_screenshot

        if store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.NORMAL, store.jn_affinity.LOVE)
        ): 

            n "H-huh?{w=0.2} What was that flash I just saw?"
            n "Don't tell me...{w=0.3} was that a camera?!{w=0.2} There's a camera here?!"
            n "..."
            n "[player]...{w=0.3} d-did you do that...?"
            menu:
                "Yes, I did.":
                    n "O-oh!{w=0.2} Aha!{w=0.2} W-well,{w=0.1} at least you admit it."
                "No, I didn't.":
                    n "Huh?{w=0.2} But then...{w=0.3} who...?"
                    n "..."
                "I'm not sure.":
                    n "That's...{w=0.3} a little worrying..."
                    n "..."
            n "Well, anyway.{w=0.1} The truth is,{w=0.1} I've never been very comfortable with having my picture taken without my permission."
            n "I just...{w=0.3} really,{w=0.1} really don't like it."
            n "So for the future,{w=0.1} could you please just let me know if you want to take pictures?"
            n "I'd really appreciate it,{w=0.1} [player]."

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.UPSET, store.jn_affinity.RUINED)
        ): 

            n "..."
            n "You're taking pictures of me,{w=0.1} aren't you?"
            menu:
                "Yes.":
                    n "Yeah...{w=0.3} no.{w=0.1} I'm not doing this."
                    n "I'm turning that off."

                "No.":
                    n "..."
                    n "There's nobody here but you and I,{w=0.1} [player]."
                    n "...{w=0.3}So why would you lie to me?"
                    n "Whatever.{w=0.1} I don't care.{w=0.1} I'm turning that off."

            $ player_screenshots_blocked = False
            $ relationship("affinity-")
            $ relationship("trust-")

        else:

            n "..."
            n "C-{w=0.1}camera...?"
            n "No.{w=0.2} I-{w=0.1}I can't.{w=0.2} No."
            n "I don't give a crap.{w=0.2} It's going off."
            $ player_screenshots_blocked = False
            $ relationship("affinity-")
            $ relationship("trust-")

    # Positive screenshot route, as we have Natsuki's permission
    elif player_screenshots_permission:
        
        $ persistent.jn_screenshot_good_shots_total += 1
        n "Huh?{w=0.2} You're taking that picture now?"

        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            n "Ahaha!{w=0.2} Sure!"

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.NORMAL, store.jn_affinity.AFFECTIONATE)
        ): 
            n "Well...{w=0.2} alright."

        else:
            n "...Fine.{w=0.1} Just be quick."

        call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.AFFECTIONATE:
            n "Okaaay!{w=0.2} Just ask me again if you wanna take another,{w=0.1} alright?"

        else:
            n "All done?{w=0.2} Just ask me again if you wanna take another,{w=0.1} okay?"
        
        $ player_screenshots_permission = False

    # Too many bad screenshots in a row; Natsuki is upset
    elif bad_screenshot_streak >= 3 and store.jn_affinity.get_affinity_state() < store.jn_affinity.ENAMORED:
        
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ player_screenshots_blocked = True
        call take_screenshot
        n "Okay,{w=0.1} I think I've had enough!{w=0.2} I'm just gonna turn this off for now."
        return

    # Negative screenshot route; Natsuki is upset
    elif not player_screenshots_blocked:

        # Update tracking and take shot
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ bad_screenshot_streak += 1
        call take_screenshot
        $ store.utils.log("Curr aff state: {0}".format(store.jn_affinity.get_affinity_state()))
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:

            # Pick the reaction and response; Natsuki is surprised but not angry
            $ chosen_reaction = renpy.substitute(renpy.random.choice(love_enamored_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(love_enamored_responses))

            n "[chosen_reaction]"
            n "[chosen_response]"
            n "So...{w=0.3} just please remember to ask next time,{w=0.1} alright?"
            n "I won't bite...{w=0.3} Ahaha..."
            n "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.NORMAL, store.jn_affinity.AFFECTIONATE)
        ): 

            # Pick the reaction and response; Natsuki is irritated
            $ chosen_reaction = renpy.substitute(renpy.random.choice(affectionate_normal_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(affectionate_normal_responses))

            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Hmph...{w=0.3} could you at least give me some warning next time?"
            n "Thanks..."
            n "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        elif store.jn_affinity.is_state_within_range(
            affinity_state=store.jn_globals.current_affinity_state,
            affinity_range=(store.jn_affinity.NORMAL, store.jn_affinity.AFFECTIONATE)
        ): 

            # Pick the reaction and response; Natsuki is clearly upset
            $ chosen_reaction = renpy.substitute(renpy.random.choice(upset_minus_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(upset_minus_responses))

            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Don't do that again."
            n "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        else:

            # Natsuki isn't putting up with this
            n "You know what,{w=0.1} [player]?{w=0.2} No.{w=0.1} We're not doing this."
            n "I'm just gonna turn this off.{w=0.1} {i}Not like you'd listen to me if I complained again.{/i}"
            $ relationship("affinity-")
            $ relationship("trust-")
            $ player_screenshots_blocked = True

    $ _player_screenshot_in_progress = False
    return