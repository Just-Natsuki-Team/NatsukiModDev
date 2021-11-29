#Datetime of when the first screenshot was taken
default persistent.jn_first_screenshot_taken = None

#Amount of good screenshots taken (permission granted)
default persistent.jn_screenshot_good_shots_total = 0

#Amount of bad screenshots taken (no perms granted)
default persistent.jn_screenshot_bad_shots_total = 0

init python in jn_screenshots:
    import os
    import random
    import store

    # Check and create the screenshot directory
    _screenshot_dir = os.path.join(renpy.config.basedir, "screenshots")
    if not os.path.exists(_screenshot_dir):
        os.makedirs(_screenshot_dir)

    # Are screenshots enabled
    __screenshots_enabled = True

    ## Tracking
    # Amount of bad screenshot taken in succession
    bad_screenshot_streak = 0

    #Does the player have permission to take screenshots?
    __has_screenshot_permission = False

    # Prevent the player from taking screenshots completely
    __screenshots_blocked = False

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

    def enable_screenshots():
        """
        Enables screenshots.
        """
        global __screenshots_enabled
        __screenshots_enabled = True

    def disable_screenshots():
        """
        Disables screenshots.
        """
        global __screenshots_enabled
        __screenshots_enabled = False

    def are_screenshots_enabled():
        """
        Returns True if screenshots are enabled.
        """
        return __screenshots_enabled

    def are_screenshots_blocked():
        """
        Returns True if screenshots are blocked.
        """
        return __screenshots_blocked

    def is_allowed_to_take_screenshot():
        """
        Checks if the player is allowed to take a screenshot.

        OUT:
            boolean - True if the player is allowed to take a screenshot, False otherwise.
        """
        return not __screenshots_blocked and __has_screenshot_permission

    def revoke_screenshot_permission(block=False):
        """
        Revokes the player's permission to take a screenshot.

        IN:
            block - If True, the player will also be blocked from taking screenshots.
        """
        global __has_screenshot_permission

        __has_screenshot_permission = False
        if block:
            block_screenshots()

    def grant_screenshot_permission(unblock=False):
        """
        Grants the player permission to take a screenshot.

        IN:
            unblock - If True, the player will also be unblocked from taking screenshots.
        """
        global __has_screenshot_permission

        __has_screenshot_permission = True

        if unblock:
            unblock_screenshots()

    def block_screenshots():
        """
        Blocks the player from taking screenshots.
        """
        global __screenshots_blocked
        __screenshots_blocked = True

    def unblock_screenshots():
        """
        Unblocks the player from taking screenshots.
        """
        global __screenshots_blocked
        __screenshots_blocked = False

    def take_screenshot():
        """
        Checks if screenshots are enabled, and if so will start the screenshot flow
        """
        if __screenshots_enabled and not __screenshots_blocked:
            renpy.call("screenshot_dialogue")

    #Register this as the new screenshot hotkey
    store.jn_register_keymap("attempt_screenshot", take_screenshot, "s")

# Attempt to produce a screenshot, render associated effects
label take_screenshot:
    if jn_affinity.get_affinity_state() >= jn_affinity.BROKEN:
        $ renpy.screenshot("{0}/screenshot_{1}.png".format(jn_screenshots._screenshot_dir, datetime.datetime.now().strftime(r"%d-%m-%Y_%H-%M-%S")))
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
    $ jn_screenshots.disable_screenshots()

    if persistent.jn_first_screenshot_taken is None:
        # Set the date for the first ever screenshot, play the camera effects
        $ persistent.jn_first_screenshot_taken = datetime.datetime.now()
        call take_screenshot

        jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            n 1uskajl "H-huh?{w=0.2} What was that flash I just saw?"
            n 1fskanl "Don't tell me...{w=0.3} was that a camera?!{w=0.2} There's a camera here?!"
            n 1fcssr "..."
            n 1kplpu "[player]...{w=0.3} d-did you do that...?"
            menu:
                "Yes, I did.":
                    n 1fcsbgl "O-oh!{w=0.2} Aha!{w=0.2} W-well,{w=0.1} at least you admit it."
                "No, I didn't.":
                    n 1tnmpu "Huh?{w=0.2} But then...{w=0.3} who...?"
                    n 1tllpu "..."
                "I'm not sure.":
                    n 1tllpu "That's...{w=0.3} a little worrying..."
                    n 1tnmpu "..."
            n 1nnmpu "Well...{w=0.3} anyway.{w=0.1} The truth is,{w=0.1} I've never been very comfortable with having my picture taken without my permission."
            n 1klrbol "I just...{w=0.3} really,{w=0.1} really don't like it."
            n 1klraj "So for the future,{w=0.1} could you please just let me know if you want to take pictures?"
            n 1klrbo "I'd really appreciate it,{w=0.1} [player]."

        jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            n 1fskpu "..."
            n 1fsqpu "You're taking pictures of me,{w=0.1} aren't you?"
            menu:
                "Yes.":
                    n 1fsqaj "Yeah...{w=0.3} no.{w=0.1} I'm not doing this."
                    n 1fsqsl "I'm turning that off."

                "No.":
                    n 1fcsan "..."
                    n 1fsqpu "There's nobody here but you and I,{w=0.1} [player]."
                    n 1fsqan "...{w=0.3}So why would you lie to me?"
                    n 1fcssr "Whatever.{w=0.1} I don't care.{w=0.1} I'm turning that off."

            $ jn_screenshots.unblock_screenshots()
            $ relationship("affinity-")
            $ relationship("trust-")

        else:
            n 1fscem "..."
            n 1fscanl "C-{w=0.1}camera...?"
            n 1kcsfrl "...No.{w=0.2} I-{w=0.1}I can't.{w=0.2} No."
            n 1fcsunl "I don't give a crap.{w=0.2} It's going off."
            $ jn_screenshots.unblock_screenshots()
            $ relationship("affinity-")
            $ relationship("trust-")

    # Positive screenshot route, as we have Natsuki's permission
    elif jn_screenshots.is_allowed_to_take_screenshot():
        $ persistent.jn_screenshot_good_shots_total += 1
        n 1unmaj "Huh?{w=0.2} You're taking that picture now?"

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uchbg "Ahaha!{w=0.2} Sure!"

        elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
            n 1kllpu "Well...{w=0.2} alright."

        else:
            n 1nlrsl "...Fine.{w=0.1} Just be quick."

        call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            n 1uchsml "Okaaay!{w=0.2} Just ask me again if you wanna take another,{w=0.1} alright?"

        else:
            n 1knmbo "All done?{w=0.2} Just make sure you ask again if you wanna take another."

        $ jn_screenshots.revoke_screenshot_permission()

    # Too many bad screenshots in a row; Natsuki is upset
    elif jn_screenshots.bad_screenshot_streak >= 3 and jn_affinity.get_affinity_state() < jn_affinity.ENAMORED:

        show natsuki 1fsqsr

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(store.jn_apologies.TYPE_SCREENSHOT)

        # Update tracking and block further screenshots
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ jn_screenshots.revoke_screenshot_permission(block=True)

        call take_screenshot
        n 1fcswr "Okay,{w=0.1} I think I've had enough!{w=0.2} I'm just gonna turn this off for now."
        return

    elif jn_screenshots.is_allowed_to_take_screenshot():
        # Update tracking and take shot
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ jn_screenshots.bad_screenshot_streak += 1

        call take_screenshot
        $ utils.log("Curr aff state: {0}".format(jn_affinity.get_affinity_state()))

        show natsuki 1fsqsr zorder 3

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(store.jn_apologies.TYPE_SCREENSHOT)

        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:

            # Pick the reaction and response; Natsuki is surprised but not angry
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.love_enamored_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.love_enamored_responses))

            n 1kwmpu "[chosen_reaction]"
            n 1kllpu "[chosen_response]"
            n 1knmbo "So...{w=0.3} just please remember to ask next time,{w=0.1} alright?"
            n 1klrbg "I won't bite...{w=0.3} Ahaha..."
            n 1klrsl "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        if jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            # Pick the reaction and response; Natsuki is irritated
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.affectionate_normal_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.affectionate_normal_responses))

            n 1fbkwrl "[chosen_reaction]"
            n 1fnmeml "[chosen_response]"
            n 1fllem "Hmph...{w=0.3} could you at least give me some warning next time?"
            n 1fllsl "Thanks..."
            n 1fnmsl "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        elif jn_affinity.is_state_within_range(
            affinity_state=jn_affinity.get_affinity_state(),
            affinity_range=(jn_affinity.UPSET, jn_affinity.DISTRESSED)
        ):

            # Pick the reaction and response; Natsuki is clearly upset
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.upset_minus_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.upset_minus_responses))

            n 1fcsan "[chosen_reaction]"
            n 1fnmfu "[chosen_response]"
            n 1fsqan "Don't do that again."
            n 1fcssr "Now,{w=0.2} where were we?"
            $ relationship("affinity-")
            $ relationship("trust-")

        else:
            # Natsuki isn't putting up with this
            n 1fcsan "You know what,{w=0.1} [player]?{w=0.2} No.{w=0.1} We're not doing this."
            n 1fcssr "I'm just gonna turn this off.{w=0.1} {i}Not like you'd listen to me if I complained again.{/i}"
            $ relationship("affinity-")
            $ relationship("trust-")
            $ jn_screenshots.revoke_screenshot_permission(block=True)

    #Enable screenshots again
    $ jn_screenshots.enable_screenshots()
    return

# Ask Natsuki for permission to take a picture of her, or have her call out the player if permission already given!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_get_picture_permission",
            unlocked=True,
            prompt="Can I take a picture of you?",
            conditional="persistent._jn_first_screenshot_taken != None",
            category=["You", "Photography"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_get_picture_permission:
    # The player was warned!
    if jn_screenshots.are_screenshots_blocked():
        n 1fsqpu "Uh...{w=0.3} no,{w=0.1} I'm not turning the camera back on,{w=0.1} [player]."
        return

    if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1uchgn "Ahaha!{w=0.2} I already said you could,{w=0.1} dummy!"
            n 1unmbg "I'm ready,{w=0.1} so take one whenever!"

        else:
            n 1unmbg "Eh?{w=0.2} A picture?{w=0.2} Of course!"
            $ jn_screenshots.grant_screenshot_permission()

    elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1tnmpu "Huh?{w=0.2} Didn't you ask me that already?"
            n 1fllpol "It's fine,{w=0.1} so go ahead!"

        else:
            n 1nllss "Oh?{w=0.2} You wanna take a picture?{w=0.2} Alright!"
            $ jn_screenshots.grant_screenshot_permission()

    elif jn_affinity.get_affinity_state() >= jn_affinity.HAPPY:
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1nllss "Hmm?{w=0.2} A picture?{w=0.2} Well,{w=0.1} okay."
            $ jn_screenshots.grant_screenshot_permission()

        else:
            n 1fcspol "Uuuu...{w=0.3} I just said you could,{w=0.1} [player]."
            n 1knmpo "Just take it soon,{w=0.1} alright?"

    elif jn_affinity.get_affinity_state() >= jn_affinity.UPSET:
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1fnmpu "I {i}already{/i} said you could,{w=0.1} [player]."

        else:
            # Indecisive; this lets lower affinity players have a chance at screenshots without upsetting Natsuki
            n 1fnmpu "You want a picture?"
            n 1fcspu "...{w=0.3} let me think about it."
            n 1fcsbo "..."
            # We take into account the player's behaviour with pictures so far
            $ natsuki_approves = random.randint(1, 100) <= (100 - (jn_screenshots.bad_screenshot_streak * 25))
            if natsuki_approves:
                n 1fllbo "Fine,{w=0.1} I guess.{w=0.1} Take it soon."
                $ jn_screenshots.grant_screenshot_permission()

            else:
                n 1fcsbo "Sorry.{w=0.2} I don't want my picture taken right now."
                $ jn_screenshots.revoke_screenshot_permission()

    elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
        n 1fsqfr "No.{w=0.1} I {b}don't{/b} want my picture taken."
        $ jn_screenshots.revoke_screenshot_permission()

    else:
        n 1fsqan "..."
        $ jn_screenshots.revoke_screenshot_permission()
    return
