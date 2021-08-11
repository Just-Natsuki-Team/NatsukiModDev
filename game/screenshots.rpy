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
    surprised_reactions = [
        "[player]...{w=0.3} you remember what I said about pictures, right?",
        "[player]...{w=0.3} did you forget what I said?",
        "[player]...{w=0.3} I think you forgot something.",
        "Hey...{w=0.3} do you remember when we talked about taking pictures?",
        "[player],{w=0.1} come on. We talked about this..."
    ]

    surprised_responses = [
        "I really don't like being surprised with pictures when I don't expect it.",
        "I really don't like having pictures taken without my permission.",
        "I really don't like having pictures taken without my consent.",
        "Surprise pictures make me feel uneasy.",
        "I want to know when you're going to take a picture of me."
    ]

    annoyed_reactions = [
        "[player]!{w=0.2} What're you doing?!",
        "A-ah!{w=0.2} [player]!",
        "H-hey!{w=0.2} [player]!",
        "E-excuse me!",
        "Hey!",
        "W-what?!"]

    annoyed_responses = [
        "You didn't say you were going to take a picture!",
        "I thought I told you to ask if you wanted pictures?",
        "I don't like surprise pictures,{w=0.1} remember?!"
    ]   

    angry_reactions = [
        "Hey! Cut it out!",
        "[player]!{w=0.2} Knock it off!",
        "[player]!{w=0.2} Stop it!",
        "[player]!{w=0.2} Quit it already!",
        "Okay, enough already!",
        "Alright, that's enough!",
        "Ugh! Give it a rest,{w=0.1} [player]!",
        "[player]!{w=0.2} Can you stop?!"]    

    angry_responses = [
        "If I didn't give you permission,{w=0.1} it means I don't want you to do it!",
        "I told you to ask if you wanted pictures!",
        "Don't you listen?!{w=0.2} I said you should ask if you want pictures of me!"
    ]

    # Add the keymap for screenshots
    jn_register_label_keymap("attempt_screenshot", "screenshot_dialogue", "s")

# Attempt to produce a screenshot, render associated effects
label take_screenshot:
    hide window
    python:
        if persistent.affinity > -50:
            renpy.screenshot("{0}/screenshot_{1}.png".format(_screenshot_dir, datetime.datetime.now().strftime(r"%d-%m-%Y_%H-%M-%S"))) # WIP; pictures will need to go to a sensible (local!) location
            utils.log("Screenshot taken by player at {0}".format(datetime.datetime.now().strftime(r"%d/%m/%Y, %H:%M")))
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

    # Positive screenshot route, as we have Natsuki's permission
    elif player_screenshots_permission:
        python:
            # Update tracking and take the shot
            persistent.jn_screenshot_good_shots_total += 1
        n "Huh?{w=0.2} You're taking that picture now?"

        if persistent.affinity >= 700:
            n "Ahaha!{w=0.2} Sure!"
            call take_screenshot
        elif persistent.affinity < 700 and persistent.affinity > 300:
            n "Well...{w=0.2} alright."
            call take_screenshot
        else:
            n "...Fine.{w=0.1} Just be quick."
            call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        if persistent.affinity > 300:
            n "Okaaay!{w=0.2} Just ask me again if you wanna take another,{w=0.1} alright?"
        else:
            n "All done?{w=0.2} Just ask me again if you wanna take another,{w=0.1} okay?"
        $ player_screenshots_permission = False

    # Too many bad screenshots in a row; Natsuki is upset
    elif bad_screenshot_streak >= 3 and persistent.affinity < 700:
        $ player_screenshots_blocked = True
        call take_screenshot
        n "Okay,{w=0.1} I think I've had enough!{w=0.2} I'm just gonna turn this off for now."
        return

    # Negative screenshot route; Natsuki is upset
    elif not player_screenshots_blocked:
        python:
            # Update tracking and take the shot
            persistent.jn_screenshot_bad_shots_total += 1
            bad_screenshot_streak += 1

        call take_screenshot
        if persistent.affinity >= 700:
            python:
                chosen_reaction = renpy.substitute(renpy.random.choice(surprised_reactions))
                chosen_response = renpy.substitute(renpy.random.choice(surprised_responses))
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "So...{w=0.3} just please remember to ask next time,{w=0.1} alright?"
            n "I won't bite...{w=0.3} Ahaha..."
            n "Now,{w=0.2} where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")
        elif persistent.affinity < 700 and persistent.affinity > 300:
            python:
                chosen_reaction = renpy.substitute(renpy.random.choice(annoyed_reactions))
                chosen_response = renpy.substitute(renpy.random.choice(annoyed_responses))
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Hmph...{w=0.3} could you at least give me some warning next time?"
            n "Thanks..."
            n "Now,{w=0.2} where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")
        elif persistent.affinity > -50:
            python:
                chosen_reaction = renpy.substitute(renpy.random.choice(angry_reactions))
                chosen_response = renpy.substitute(renpy.random.choice(angry_responses))
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Don't do that again."
            n "Now,{w=0.2} where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")
        else:
            n "You know what,{w=0.1} [player]?{w=0.2} No.{w=0.1} We're not doing this."
            n "I'm just gonna turn this off.{w=0.1} {i}Not like you'd listen to me if I complained again.{/i}"
            python:
                relationship("affinity-")
                relationship("trust-")
                player_screenshots_blocked = True

    $ _player_screenshot_in_progress = False
    return