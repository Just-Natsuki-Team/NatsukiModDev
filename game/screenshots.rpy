init -50 python:
    from datetime import datetime as dt
    from enum import Enum

    # Possible types for a screenshot, based on how it was received
    class ScreenshotReceptionTypes(Enum):
        NEUTRAL = 1
        GOOD = 2
        BAD = 3

    last_screenshot_type = ScreenshotReceptionTypes.NEUTRAL

    # Add the keymap for screenshots
    jn_register_label_keymap("attempt_screenshot", "screenshot_dialogue", "s")

    # Screenshot code; TODO
    def take_screenshot():
        return

# Handles dialogue and mechanics related to screenshots
label screenshot_dialogue:
    $utils.log('Screenshot taken by player at {0}'.format(dt.now().strftime(r"%d/%m/%Y, %H:%M")))
    if persistent._jn_first_screenshot_taken == None or type(persistent._jn_first_screenshot_taken) is str:
        # Set the date for the first ever screenshot
        python:
            persistent._jn_first_screenshot_taken = dt.now()
        n "H-huh? What was that flash I just saw?"
        n "Don't tell me... was that a camera?! There's a camera here?!"
        n "..."
        n "[player]... d-did you do that...?"
        # TODO - This should unlock the screenshot permission topic!

    if persistent._jn_screenshot_has_permission:
        # Positive screenshot route, as we have Natsuki's permission
        python:
            persistent._jn_screenshot_good_shots_total += 1
            last_screenshot_type = ScreenshotReceptionTypes.GOOD
            utils.log('Last screenshot reception is now {0}'.format(last_screenshot_type))
        n 'Huh? You wanna take a picture?'
        # TODO - Response tree based on pos. aff

    else:
        # Negative screenshot route; Natsuki is upset
        python:
            persistent._jn_screenshot_bad_shots_total += 1
            last_screenshot_type = ScreenshotReceptionTypes.BAD
            utils.log('Last screenshot reception is now {0}'.format(last_screenshot_type))
        n 'I thought I said no pictures? :('
        # TODO - Response tree based on neg. aff
    return