init 0 python:
    from datetime import datetime as dt
    from enum import Enum
    import random

    # Check and create the screenshot directory
    _screenshot_dir = os.path.join(renpy.config.basedir, "screenshots")
    if not os.path.exists(_screenshot_dir):
        os.makedirs(_screenshot_dir)

    # Tracking
    _bad_screenshot_streak = 0

    # Prevent the player from taking screenshots within the screenshot dialogue tree
    _player_screenshot_in_progress = False

    # Prevent the player from taking screenshots completely
    _player_screenshots_blocked = False

    # Reaction/response permutations so Natsuki feels more dynamic
    surprised_reactions = [
        "{0}... you remember what I said about pictures, right?".format(persistent.playername),
        "{0}... did you forget what I said?".format(persistent.playername),
        "{0}... I think you forgot something.".format(persistent.playername),
        "Hey... do you remember when we talked about taking pictures?",
        "{0}, come on. We talked about this...".format(persistent.playername)
    ]

    surprised_responses = [
        "I really don't like being surprised with pictures when I don't expect it.",
        "I really don't like having pictures taken without my permission.",
        "I really don't like having pictures taken without my consent.",
        "Surprise pictures make me feel uneasy.",
        "I want to know when you're going to take a picture of me."
    ]

    annoyed_reactions = [
        "{0}! What're you doing?!".format(persistent.playername),
        "A-ah! {0}!".format(persistent.playername),
        "H-hey! {0}!".format(persistent.playername),
        "E-excuse me!",
        "Hey!",
        "W-what?!"]

    annoyed_responses = [
        "You didn't say you were going to take a picture!",
        "I thought I told you to ask if you wanted pictures?",
        "I don't like surprise pictures, remember?!"
    ]   

    angry_reactions = [
        "Hey! Cut it out!",
        "{0}! Knock it off!".format(persistent.playername),
        "{0}! Stop it!".format(persistent.playername),
        "{0}! Quit it already!".format(persistent.playername),
        "Okay, enough already!".format(persistent.playername),
        "Alright, that's enough!",
        "Ugh! Give it a rest, {0}!".format(persistent.playername),
        "{0}! Can you stop?!".format(persistent.playername)]    

    angry_responses = [
        "If I didn't give you permission, it means I don't want you to do it!",
        "I told you to ask if you wanted pictures!",
        "Don't you listen?! I said you should ask if you want pictures of me!"
    ]

    # Add the keymap for screenshots
    jn_register_label_keymap("attempt_screenshot", "screenshot_dialogue", "s")

# Attempt to produce a screenshot, render associated effects
label take_screenshot:
    python:
        if persistent.affinity > -50:
            renpy.screenshot("{0}/screenshot_{1}.png".format(_screenshot_dir, dt.now().strftime(r"%d-%m-%Y_%H-%M-%S"))) # WIP; pictures will need to go to a sensible (local!) location
            utils.log("Screenshot taken by player at {0}".format(dt.now().strftime(r"%d/%m/%Y, %H:%M")))
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

    if persistent.jn_first_screenshot_taken == None or type(persistent.jn_first_screenshot_taken) is str:
        # Set the date for the first ever screenshot, play the camera effects
        $ persistent.jn_first_screenshot_taken = dt.now()
        call take_screenshot

        n "H-huh? What was that flash I just saw?"
        n "Don't tell me... was that a camera?! There's a camera here?!"
        n "..."
        n "[player]... d-did you do that...?"
        menu:
            "Yes, I did.":
                n "O-oh! Aha! W-well, at least you admit it."
            "No, I didn't.":
                n "Huh? But then... who...?"
                n "..."
            "I'm not sure.":
                n "That's... a little worrying..."
                n "..."
        n "Well, anyway. The truth is, I've never been very comfortable with having my picture taken without my permission."
        n "I just... really, really don't like it."
        n "So for the future, could you please just let me know if you want to take pictures?"
        n "I'd really appreciate it, [player]."

    # Positive screenshot route, as we have Natsuki's permission
    elif persistent.jn_screenshot_has_permission:
        python:
            # Update tracking and take the shot
            persistent.jn_screenshot_good_shots_total += 1
        n "Huh? You're taking that picture now?"

        if persistent.affinity >= 700:
            n "Ahaha! Sure!"
            call take_screenshot
        elif persistent.affinity < 700 and persistent.affinity > 300:
            n "Well... alright."
            call take_screenshot
        else:
            n "...Fine. Just be quick."
            call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        if persistent.affinity > 300:
            n "Okaaay! Just ask me again if you wanna take another, alright?"
        else:
            n "All done? Just ask me again if you wanna take another, alright?"
        $ persistent.jn_screenshot_has_permission = False

    # Too many bad screenshots in a row; Natsuki is upset
    elif _bad_screenshot_streak >= 3 and persistent.affinity < 700:
        python:
            _player_screenshots_blocked = True
        call take_screenshot
        n "Okay, I think I've had enough. I'm just gonna turn this off for now."
        return

    # Negative screenshot route; Natsuki is upset
    elif not _player_screenshots_blocked:
        python:
            # Update tracking and take the shot
            persistent.jn_screenshot_bad_shots_total += 1
            _bad_screenshot_streak += 1

        call take_screenshot
        if persistent.affinity >= 700:
            python:
                chosen_reaction = surprised_reactions[random.randint(0, len(surprised_reactions) - 1)]
                chosen_response = surprised_responses[random.randint(0, len(surprised_responses) - 1)]
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "So... just please remember to ask next time, alright?"
            n "I won't bite... Ahaha..."
            n "Now, where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")

        elif persistent.affinity < 700 and persistent.affinity > 300:
            python:
                chosen_reaction = annoyed_reactions[random.randint(0, len(annoyed_reactions) - 1)]
                chosen_response = annoyed_responses[random.randint(0, len(annoyed_responses) - 1)]
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Hmph... could you at least give me some warning next time?"
            n "Thanks..."
            n "Now, where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")
        elif persistent.affinity > -50:
            python:
                chosen_reaction = angry_reactions[random.randint(0, len(angry_reactions) - 1)]
                chosen_response = angry_responses[random.randint(0, len(angry_responses) - 1)]
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Don't do that again."
            n "Now, where were we?"
            python:
                relationship("affinity-")
                relationship("trust-")
        else:
            n "You know what, [player]? No. We're not doing this."
            n "I'm just gonna turn this off. Not like you'd listen to me if I complained again."
            python:
                relationship("affinity-")
                relationship("trust-")
                _player_screenshots_blocked = True

    python:
        _player_screenshot_in_progress = False
    return