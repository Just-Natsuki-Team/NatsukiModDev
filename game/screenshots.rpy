init 0 python:
    from datetime import datetime as dt
    from enum import Enum
    import random

    # Possible types for a screenshot, based on how it was received
    class ScreenshotReceptionTypes(Enum):
        NEUTRAL = 1
        GOOD = 2
        BAD = 3

    # Handling variables for when we're processing screenshots
    last_screenshot_type = ScreenshotReceptionTypes.NEUTRAL
    player_screenshots_blocked = False
    player_screenshot_in_progress = False
    bad_screenshot_streak = 0

    # Reaction/response permutations so Natsuki feels more dynamic
    surprised_reactions = [
        "{0}... you remember what I said about pictures, right?".format(persistent.playername),
        "{0}... did you forget what I said?".format(persistent.playername),
        "{0}... I think you forgot something.".format(persistent.playername),
        "Hey... do you remember when we talked about taking pictures?"
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
            renpy.screenshot("screenshot_{0}.png".format(dt.now().strftime(r"%d-%m-%Y_%H-%M-%S"))) # WIP; pictures will need to go to a sensible (local!) location
            utils.log("Screenshot taken by player at {0}".format(dt.now().strftime(r"%d/%m/%Y, %H:%M")))
    play audio camera_shutter
    with Fade(.15, 0, .50, color="#fff")
    return

# Handles dialogue and mechanics related to screenshots
label screenshot_dialogue:
    if player_screenshot_in_progress:
        # Don't take a screenshot if we're already going through the dialogue!
        return
    else:
        $ player_screenshot_in_progress = True

    if persistent._jn_first_screenshot_taken == None or type(persistent._jn_first_screenshot_taken) is str:
        # Set the date for the first ever screenshot, play the camera effects
        $ persistent._jn_first_screenshot_taken = dt.now()
        call take_screenshot

        n "H-huh? What was that flash I just saw?"
        n "Don't tell me... was that a camera?! There's a camera here?!"
        n "..."
        n "[player]... d-did you do that...?"
        menu:
            "Yes, I did.":
                n "TODO"
            "No, I didn't.":
                n "TODO"
            "I'm not sure.":
                n "TODO"
    if persistent._jn_screenshot_has_permission:
        # Positive screenshot route, as we have Natsuki's permission
        python:
            # Update tracking and take the shot
            persistent._jn_screenshot_good_shots_total += 1
            last_screenshot_type = ScreenshotReceptionTypes.GOOD
        n "Huh? You're taking that picture now?"

        if persistent.affinity >= 700:
            n "Ahaha! Sure!"
            call take_screenshot
        elif persistent.affinity < 700 and persistent.affinity > 300:
            n "Well... alright."
            call take_screenshot
        else:
            n "...Fine. Just be quick, alright?"
            call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        n "Okaaay! Just ask me again if you wanna take another, alright?"
        $ persistent._jn_screenshot_has_permission = False

    elif not player_screenshots_blocked:
        # Negative screenshot route; Natsuki is upset
        python:
            # Update tracking and take the shot
            persistent._jn_screenshot_bad_shots_total += 1
            last_screenshot_type = ScreenshotReceptionTypes.BAD
            bad_screenshot_streak += 1

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
            #python:
                #relationship.affinity_decrease("affinity-")
                #relationship.trust_decrease("trust-")

        elif persistent.affinity < 700 and persistent.affinity > 300:
            python:
                chosen_reaction = annoyed_reactions[random.randint(0, len(annoyed_reactions) - 1)]
                chosen_response = annoyed_responses[random.randint(0, len(annoyed_responses) - 1)]
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Hmph... could you at least give me some warning next time?"
            n "Thanks..."
            n "Now, where were we?"
            #python:
                #relationship.affinity_decrease("affinity-")
                #relationship.trust_decrease("trust-")
        elif persistent.affinity > -50:
            python:
                chosen_reaction = angry_reactions[random.randint(0, len(angry_reactions) - 1)]
                chosen_response = angry_responses[random.randint(0, len(angry_responses) - 1)]
            n "[chosen_reaction]"
            n "[chosen_response]"
            n "Don't do that again."
            n "Now, where were we?"
            #python:
                #relationship.affinity_decrease("affinity-")
                #relationship.trust_decrease("trust-")
        else:
            n "You know what, [player]? No. We're not doing this."
            n "I'm just gonna turn this off. Not like you'd listen to me if I complained again."
            python:
                #relationship.affinity_decrease("affinity-")
                #relationship.trust_decrease("trust-")
                player_screenshots_blocked = True

    python:
        utils.log('Last screenshot reception is now {0}'.format(last_screenshot_type))
        player_screenshot_in_progress = False
    return