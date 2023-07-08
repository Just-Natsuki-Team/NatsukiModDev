# General tracking; the player unlocks Snap by admitting boredom to Natsuki at least once
default persistent.jn_snap_unlocked = False
default persistent.jn_snap_explanation_given = False

# Natsuki will refuse to play with a cheater
default persistent.jn_snap_player_is_cheater = False

# Win records
default persistent._jn_snap_player_wins = 0
default persistent._jn_snap_natsuki_wins = 0

init 0 python in jn_snap:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import time

    # Card config
    _CARD_VALUES = range(1, 11)
    _CARD_SUITS = [
        "clubs",
        "diamonds",
        "hearts",
        "spades"
    ]

    _current_table_card_image = "mod_assets/games/cards/blank.png"
    _turn_indicator_image = "mod_assets/games/snap/turn_indicator_none.png"

    _SNAP_UI_Z_INDEX = 4
    _SNAP_POPUP_Z_INDEX = 5

    # Quips
    _PLAYER_CORRECT_SNAP_QUIPS = [
        "Nnnnn-!",
        "Ugh!{w=0.2} Come on!",
        "Y-{w=0.2}You're fast!",
        "But I was just about to call ittt!",
        "Just you wait,{w=0.2} [player]...",
        "Uuuuuu-!",
        "Not again!{w=0.2} Grrr...",
        "Damn it...",
        "Fudge...",
        "So dumb...",
        "Again?{w=0.2} Really?",
        "Ugh...",
        "So ridiculous...",
        "So dumb...",
        "Jeez! Whatever...",
        "Jeez!",
        "Jeeeeeez!",
        "Oh come on,{w=0.2} [player]!",
        "How are you {i}that{/i} fast?!"
    ]

    _NATSUKI_CORRECT_SNAP_QUIPS = [
        "SNAP!{w=0.2} Ahaha!",
        "Snap!{w=0.2} Ahaha!",
        "SNAP!{w=0.2} Ehehe.",
        "SNAP!",
        "Snap!",
        "Snap~!",
        "Snap!{w=0.2} Snap snap snap!",
        "Snappy snap!",
        "Boom!{w=0.2} Snap!",
        "Snap!{w=0.2} Snap!",
        "Snap!{w=0.2} Snap!{w=0.2} Snap!",
        "Yes!{w=0.2} SNAP!",
        "Yeah!{w=0.2} SNAP!",
        "Yeah!{w=0.2} Snap!{w=0.2} Snap!",
        "Snap snap freaking snap!",
        "SNAAAP!{w=0.2} Ehehe.",
        "Bam!{w=0.2} Snap!"
    ]

    _PLAYER_INCORRECT_SNAP_QUIPS = [
        "Oh?{w=0.2} Someone's impatient,{w=0.2} huh?",
        "Oopsie daisy,{w=0.2} [player]~.{w=0.2} Ehehe.",
        "Nice one,{w=0.2} dummy.{w=0.2} Ahaha!",
        "Real smooth,{w=0.2} [player].{w=0.2} Ehehe.",
        "Ahaha!{w=0.2} What was that,{w=0.2} [player]?",
        "Hey,{w=0.2} [player] -{w=0.2} you're meant to read the cards!{w=0.2} Ehehe.",
        "Great play,{w=0.2} dummy!{w=0.2} Ahaha!"
    ]

    _NATSUKI_INCORRECT_SNAP_QUIPS = [
        "Sn-...{w=0.3} oh.",
        "Snap!{w=0.2} Wait...",
        "SNAP!{w=0.2} Huh...?{w=0.2} O-{w=0.2}oh.",
        "Snap sna-...{w=0.3} grrr."
    ]

    # Out of game tracking
    _player_win_streak = 0
    _natsuki_win_streak = 0
    last_game_result = None

    # Game outcomes
    RESULT_PLAYER_WIN = 0
    RESULT_NATSUKI_WIN = 1
    RESULT_DRAW = 3
    RESULT_FORFEIT = 4

    # In-game tracking
    _is_player_turn = None
    _player_forfeit = False
    _player_is_snapping = False
    _player_failed_snap_streak = 0
    _natsuki_can_fake_snap = False
    _natsuki_skill_level = 0
    _controls_enabled = False

    # Collections of cards involved in the game
    _cards_in_deck = []
    _cards_on_table = []
    _natsuki_hand = []
    _player_hand = []

    # A little something extra
    if random.choice(range(1, 100)) == 1:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/card_fan_icon_alt.png"

    else:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/card_fan_icon.png"

    _CARD_FAN_IMAGE_NATSUKI = "mod_assets/games/snap/card_fan_icon.png"

    _SNAP_POPUP_SPRITES = [
        "mod_assets/games/snap/snap_a.png",
        "mod_assets/games/snap/snap_b.png",
        "mod_assets/games/snap/snap_c.png",
        "mod_assets/games/snap/snap_d.png"
    ]

    def _reset(complete_reset=False):
        """
        Resets the in-game variables associated with Snap

        IN:
            - true_reset - boolean flag; if True will also reset Natsuki's skill level, etc.
        """
        global _is_player_turn
        global _player_forfeit
        global _player_is_snapping
        global _player_failed_snap_streak
        global _natsuki_can_fake_snap

        _is_player_turn = None
        _player_forfeit = False
        _player_is_snapping = False
        _player_failed_snap_streak = 0
        _natsuki_can_fake_snap = False
        del _cards_in_deck[:]
        del _cards_on_table[:]

        if complete_reset:
            _natsuki_skill_level = 1

    def _generate_hands():
        """
        Generates a deck of cards based on the card configuration
        Deck is then shuffled, and the players are then assigned their hands
        Finally, the deck is cleared
        """
        # Clear the old hands
        del _player_hand[:]
        del _natsuki_hand[:]

        # Generate all possible card combinations based on suits and values
        for card_suit in _CARD_SUITS:
            for card_value in _CARD_VALUES:
                _cards_in_deck.append((card_suit, card_value))

        # Assign each player their deck
        random.shuffle(_cards_in_deck)
        switch = False
        for card in _cards_in_deck:
            # We alternate between Natsuki and the player's hands when giving cards out
            if switch:
                switch = False
                _player_hand.append(card)

            else:
                switch = True
                _natsuki_hand.append(card)

        # Finally clear here, since we can't remove elements while iterating through
        del _cards_in_deck[:]

    def _place_card_on_table(is_player=False):
        """
        Takes the top-most card from the player's hand and places it on the table pile

        IN:
            - is_player boolean value representing if the player or Natsuki is the one placing their card down.
        """
        global _is_player_turn
        if is_player:
            if (len(_player_hand) > 0):
                new_card = _player_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.ogg")
                _is_player_turn = False

        else:
            if (len(_natsuki_hand) > 0):
                new_card = _natsuki_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.ogg")
                _is_player_turn = True

        update_turn_indicator()
        draw_card_onscreen()

    def _get_card_label_to_display():
        """
        Returns a string representing the uppermost card on the table pile
        """
        if len(_cards_on_table) >= 1:
            return "{0} of {1}".format(_cards_on_table[-1][0], _cards_on_table[-1][1])

        else:
            return "None!"

    def _get_snap_result():
        """
        Compares the last two cards placed on the table pile, and returns True if either:
            - The suits on both cards match
            - The values on both cards match
        Otherwise, returns False
        Used by Natsuki's logic to determine if she should "spot" the snap opportunity
        """
        if len(_cards_on_table) >= 2:
            return _cards_on_table[-1][0] == _cards_on_table[-2][0] or _cards_on_table[-1][1] == _cards_on_table[-2][1]

        else:
            return False

    def _call_snap(is_player=False):
        """
        Attempts to call snap and award cards for the player or Natsuki, based on who made the call

        IN:
            - is_player boolean value representing if the player or Natsuki was the one who made the call
        """
        global _is_player_turn
        global _player_is_snapping

        # We set this here so Natsuki can't try to snap while the player is snapping
        if is_player:
            _player_is_snapping = True

        # If the suit/value on the last placed card matches the preceding card, the snap is valid
        if _get_snap_result():

            if is_player:
                # Player called snap successfully; give them the cards on the table
                for card in _cards_on_table:
                    _player_hand.append(card)

            else:
                # Natsuki called snap successfully; give her the cards on the table
                for card in _cards_on_table:
                    _natsuki_hand.append(card)

            # Clear the cards on the table
            del _cards_on_table[:]
            renpy.play("mod_assets/sfx/card_shuffle.ogg")
            draw_card_onscreen()

            # Use of renpy.call here is a stopgap and will be reworked, as renpy.call risks breaking label flow if not carefully applied.
            # Please use renpy.jump instead of this approach

            # Natsuki comments on the correct snap
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=True)

        else:
            # Natsuki comments on the incorrect snap
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=False)

    def draw_card_onscreen():
        """
        Shows the card currently on top of the table pile, or nothing if no cards are on the pile
        """
        global _current_table_card_image

        if len(_cards_on_table) is not 0:
            _current_table_card_image = "mod_assets/games/cards/{0}/{1}.png".format(_cards_on_table[-1][0], _cards_on_table[-1][1])

        else:
            _current_table_card_image = "mod_assets/games/cards/blank.png"

    def update_turn_indicator():
        """
        Updates the turn indicator graphic to display who's turn it is to move
        """
        global _turn_indicator_image

        if _is_player_turn is None:
            _turn_indicator_image = "mod_assets/games/snap/turn_indicator_none.png"

        elif _is_player_turn:
            _turn_indicator_image = "mod_assets/games/snap/turn_indicator_player.png"

        else:
            _turn_indicator_image = "mod_assets/games/snap/turn_indicator_natsuki.png"

    def get_turn_label_to_display():
        """
        Returns a turn descriptor label based on who's turn it is to move
        """
        if _is_player_turn is None:
            return "Nobody!"

        elif _is_player_turn:
            return "Yours!"

        else:
            return renpy.substitute("[n_name]")

label snap_intro:
    n 1nchbs "Alriiiight!{w=0.75}{nw}" 
    extend 1fcsbg " Let's play some Snap!"

    if not persistent.jn_snap_explanation_given:
        n 1nnmaj "Oh -{w=0.3} before we start,{w=0.2} did you want an explanation?{w=0.5}{nw}" 
        extend 4tllca " You know,{w=0.2} on how it works?"
        n 4nchsm "It's a super simple game,{w=0.2} but I thought I'd better ask."
        n 2fcsbg "I don't wanna win just because you didn't know what you were doing!"
        n 2usqfs "So...{w=1}{nw}"
        extend 4fchss " how about it?"

        show natsuki 4fchsm
        menu:
            n "Need me to run through the rules real quick?"

            "Yes, please!":
                jump snap_explanation

            "No, I'm ready.":
                n 4tsqss "Oh?{w=0.75}{nw}" 
                extend 4flrbg " You're ready,{w=0.5}{nw}" 
                extend 4fsqbg " huh?"
                n 2fchgn "Ready to get your butt kicked!{w=0.75}{nw}" 
                extend 2fchbs " Let's go,{w=0.2} [player]!"
                $ persistent.jn_snap_explanation_given = True

    jump snap_start

label snap_explanation:
    n 1nnmss "Alright!{w=0.2} So the rules are dead simple,{w=0.5}{nw}" 
    extend 4nslsm " like I was saying before."
    n 4unmaj "Basically,{w=0.2} we each get half a deck of cards."
    n 2nchss "Then,{w=0.2} we take it in turns placing a card face up on the table -{w=0.5}{nw}"
    extend 2fsrdv " we don't get to {i}pick or see{/i} the card before,{w=0.2} though!"
    n 4fsgbg "Following me so far,{w=0.2} [player]?{w=0.2} Ehehe."
    n 1nnmbg "If the card just placed down on the table matches either the {i}value or suit{/i} of the card that was there before..."
    n 4usqsm "Then we gotta call{w=0.5}{nw}"
    extend 4fchbs " Snap!"
    n 1nnmsm "Whoever calls it first gets the cards on the table."
    n 1unmaj "Oh -{w=0.5}{nw}"
    extend 2tsqss " but you gotta be careful,{w=0.2} [player]."
    n 4fllsg "When you call snap,{w=0.2} it becomes the other player's turn..."
    n 2fsqsm "So don't shout unless you know you got it,{w=0.5}{nw}"
    extend 2nchgn " 'kay?"
    n 1uchbg "The winner is whoever ends up with all the cards first!"
    n 4tsqsm "Which is usually me,{w=0.75}{nw}"
    extend 2fsldv " obviously."
    n 4uwdaj "Oh,{w=0.2} right -{w=0.5}{nw}"
    extend 1nnmsm " you also lose if you run out of cards to play,{w=0.2} so you should keep that in mind too."
    n 4tsqss "So...{w=0.3} how about it,{w=0.2} [player]?{w=0.2} You got all that?"

    show natsuki 4unmbo
    menu:
        n "Did that all make sense to you?"

        "Can you go over the rules again?":
            n 1tsqpueqm "Huh?{w=0.75}{nw}" 
            extend 1tllca " Well,{w=0.2} okay..."

            jump snap_explanation

        "Got it. Let's play!":
            n 1fcsbg "Now {i}that's{/i} what I'm talking about.{w=0.75}{nw}" 
            extend 1fchgn " Some fighting spirit!"
            n 2fsqbg "I should warn you though,{w=0.2} [player]..."
            n 2fcsbs "I'm not gonna hold back!{w=0.75}{nw}" 
            extend 2uchgn " Let's do this!"

            $ persistent.jn_snap_explanation_given = True
            jump snap_start

        "Thanks, [n_name]. I'll play later.":
            n 1tsqpueqm "Huh?{w=0.75}{nw}"
            extend 2nsqflsbl " Seriously?"
            n 2nslpo "..."
            n 4nllfl "Well...{w=1.25}{nw}" 
            extend 4nslca " fine."
            n 2flrpo "...Spoilsport."

            if not Natsuki.getDeskSlotClear(jn_desk_items.JNDeskSlots.centre):
                show natsuki 2ccspo
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
                show natsuki 2nlrbo
                $ jnPause(1)
                hide black with Dissolve(1.25)

            jump ch30_loop

label snap_start:
    # Reset everything ready for a fresh game
    play audio card_shuffle
    $ jn_snap._reset()
    $ jn_snap._generate_hands()

    # Reset the UI
    $ jn_snap.draw_card_onscreen()
    $ jn_snap.update_turn_indicator()

    show natsuki 1uchsm at jn_left
    show screen snap_ui
    $ jnPause(1)

    n 1nchbg "'Kay!{w=0.75}{nw}" 
    extend 1fchsm " That's the deck shuffled!"
    n 4fsqsm "Let's see who's up first..."

    play audio coin_flip

    n 4fnmpu "..."
    $ jn_snap._is_player_turn = random.choice([True, False])
    $ jn_snap.update_turn_indicator()

    if jn_snap._is_player_turn:
        n 1fcssm "Ehehe.{w=0.5}{nw}" 
        extend 1fcsbg " Bad luck,{w=0.2} [player].{w=0.75}{nw}" 
        extend 1fchgn " Looks like you're up first!"

    else:
        n 2nsqsl "..."
        n 2fslpo "Hmph.{w=0.5}{nw}" 
        extend 2fcsaj " You just got lucky this time.{w=0.75}{nw}" 
        extend 2fcsca " I guess I'll go first then,{w=0.2} [player]."

    show natsuki snap
    $ Natsuki.setInGame(True)
    $ jn_snap._controls_enabled = True
    jump snap_main_loop

label snap_main_loop:

    # First, let's check to see if anyone has won yet
    if len(jn_snap._player_hand) == 0 and len(jn_snap._natsuki_hand) == 0:
        # We tied somehow? End the game
        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_DRAW
        jump snap_end

    elif len(jn_snap._player_hand) == 0:
        # Player has lost; end the game
        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak += 1
        $ persistent._jn_snap_natsuki_wins += 1 
        $ jn_snap.last_game_result = jn_snap.RESULT_NATSUKI_WIN
        jump snap_end

    elif len(jn_snap._natsuki_hand) == 0:
        # Natsuki has lost; end the game
        $ jn_snap._player_win_streak += 1
        $ persistent._jn_snap_player_wins += 1
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_PLAYER_WIN
        jump snap_end

    $ jnPause(delay=max(0.33, (3.0 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)

    # Natsuki's snap logic

    # If a correct snap is possible, and the player isn't snapping already, Natsuki will try to call it: the higher the difficulty, the quicker Natsuki will be.
    if not jn_snap._player_is_snapping:
        if jn_snap._get_snap_result():
            $ jn_snap._call_snap()

        # She may also snap by mistake, assuming it makes sense to do so: the higher the difficulty, the less she'll accidentally jn_snap.
        elif (
            random.choice(range(0,10 + jn_snap._natsuki_skill_level)) == 1
            and len(jn_snap._cards_on_table) >= 2
            and jn_snap._natsuki_can_fake_snap
            and not _player_failed_snap_streak
        ):
            $ jn_snap._call_snap()
            $ jn_snap._natsuki_can_fake_snap = False

    if not jn_snap._is_player_turn:
        # Natsuki gets to place a card
        $ jn_snap._place_card_on_table(False)

        # If Natsuki only has one card left, she'll try to see if she can snap before admitting defeat
        if len(jn_snap._natsuki_hand) == 0:
            $ jnPause(delay=max(0.33, (1.25 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)

            if jn_snap._get_snap_result():
                $ jn_snap._call_snap()

        $ jn_snap._is_player_turn = True
        $ jn_snap._natsuki_can_fake_snap = True

    jump snap_main_loop

label snap_quip(is_player_snap, is_correct_snap):

    $ cheat_check = False

    # Generate the quip based on what just happened
    if is_player_snap:

        # Player snapped, and was correct
        if is_correct_snap:
            $ jn_snap._player_failed_snap_streak = 0
            $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_CORRECT_SNAP_QUIPS))
            show natsuki 4klrca zorder JN_NATSUKI_ZORDER

            # Some UE things to make it fun
            play audio smack
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            $ jnPause(0.75)
            hide snap_popup

        # Player snapped, and was incorrect
        else:
            $ jn_snap._player_failed_snap_streak += 1

            # Cheating warning
            if jn_snap._player_failed_snap_streak == 3 and not persistent.jn_snap_player_is_cheater:
                $ cheat_check = True
                n 4fnmaj "[player]!{w=0.5}{nw}"
                extend 2fnmsf " You're just calling Snap whenever it's your turn!{w=0.5}{nw}"
                extend 2fsqaj " That's not how you play at all!"
                n 2fllca "I hope you aren't trying to cheat,{w=0.2} [player].{w=0.75}{nw}"
                extend 2fsqsl " I can't stand playing with cheaters."

            # Natsuki calls off the game
            elif jn_snap._player_failed_snap_streak == 6 and not persistent.jn_snap_player_is_cheater:
                $ jn_snap_controls_enabled = False
                n 2fupfl "Ugh...{w=1.25}{nw}" 
                extend 2fcsfl " look,{w=0.2} [player]."
                n 2fcsaj "If you aren't gonna play fairly,{w=0.5}{nw}" 
                extend 2flrem " then why should I bother playing at all?"
                n 4fllfl "I even {i}warned{/i} you before,{w=0.5}{nw}" 
                extend 4fnmfl " too!"
                n 4fcsemesi "..."
                n 4fcssl "You know what?{w=0.75}{nw}"
                extend 2fcsfl " Fine."
                n 2fsrbo "We're done with this game,{w=0.2} [player]."

                $ _player_win_streak = 0
                $ persistent.jn_snap_player_is_cheater = True
                $ Natsuki.percentageAffinityLoss(1)
                $ Natsuki.addApology(jn_apologies.ApologyTypes.cheated_game)

                # Hide all the UI
                hide screen snap_ui

                show natsuki 2fcsbo
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
                show natsuki 2cslbo
                $ jnPause(1)
                hide black with Dissolve(1.25)

                # Reset the ingame flag, then hop back to ch30 as getting here has lost context
                $ Natsuki.setInGame(False)
                $ Natsuki.resetLastTopicCall()
                $ Natsuki.resetLastIdleCall()
                jump ch30_loop

            # Generic incorrect quip/tease
            else:
                $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_INCORRECT_SNAP_QUIPS))
                show natsuki 2fsqsm zorder JN_NATSUKI_ZORDER

    else:

        # Natsuki snapped, and was correct
        if is_correct_snap:
            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_CORRECT_SNAP_QUIPS))
            show natsuki 4uchbg zorder JN_NATSUKI_ZORDER

            # Some UE things to make it fun

            play audio smack
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            $ jnPause(0.75)
            hide snap_popup

        # Natsuki snapped, and was incorrect
        else:
            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_INCORRECT_SNAP_QUIPS))
            show natsuki 2fsqsr zorder JN_NATSUKI_ZORDER

    # Natsuki quips; disable controls so player can't skip dialogue
    $ jn_snap._controls_enabled = False

    if not cheat_check:
        n "[quip]"

    show natsuki snap at jn_left
    $ jn_snap._controls_enabled = True

    # Now we reset the flags so nothing can happen before the quip has completed
    if is_player_snap:
        $ jn_snap._player_is_snapping = False
        $ jn_snap._is_player_turn = False

    else:
        $ jn_snap._is_player_turn = True

    $ jn_snap.update_turn_indicator()

    return

label snap_end:
    hide screen snap_ui
    $ jn_snap._controls_enabled = False

    # Player won, Natsuki amger
    if jn_snap.last_game_result == jn_snap.RESULT_PLAYER_WIN:

        if jn_snap._player_win_streak > 10:
            n 2csltr "Yeah,{w=0.3} yeah.{w=1}{nw}" 
            extend 2cslpo " You won again."
            n 2csrsssbr "...You nerd."

        elif jn_snap._player_win_streak == 10:
            n 2fcsaj "Oh,{w=0.5}{nw}"
            extend 2fcsan " come{w=0.75}{nw}"
            extend 2fbkwrl " {b}on{/b}!"
            n 4fllgs "Seriously?!{w=0.75}{nw}"
            extend 4fnmgs " Ten in a row?!{w=0.75}{nw}"
            extend 2clremsbl " Man..."
            n 2ccsfl "If you had a point to make,{w=0.2} you've made it,{w=0.75}{nw}"
            extend 2csqpo " okay?{w=1}{nw}"
            extend 2cslcasbr " Jeez..."

        elif jn_snap._player_win_streak == 5:
            n 4fcsem "J-{w=0.2}jeez!{w=0.5}{nw}"
            extend 4flrgs " Five {i}already{/i}?!{w=0.75}{nw}"
            extend 2cslca " Come on."
            n 2fcsajsbl "I never {i}said{/i} I was a professional,{w=0.5}{nw}" 
            extend 2fcsposbl " you know."

        elif jn_snap._player_win_streak == 3:
            n 1fcsss "Heh.{w=0.75}{nw}"
            extend 1fllsssbr " Better gloat while you can,{w=0.2} [player]."
            n 1fcsbgsbr "'Cause that lucky streak won't last forever!"

        else:
            n 2nllpo "Well,{w=0.2} heck.{w=0.5}{nw}" 
            extend 2nslsssbr " I guess that's it,{w=0.2} huh?"
            n 2fcssssbr "W-{w=0.2}well played,{w=0.2} [player].{w=0.75}{nw}"
            extend 2csrposbr " I guess."

    # Natsuki won, Natsuki happ
    elif jn_snap.last_game_result == jn_snap.RESULT_NATSUKI_WIN:

        if jn_snap._natsuki_win_streak > 10:
            n 1fcsss "Man,{w=0.5}{nw}" 
            extend 4fcsbg " this is just too{w=0.25}{nw}" 
            extend 4fchgn " {i}easy{/i}!{w=0.75}{nw}" 
            extend 4fcsbg " I {i}almost{/i} feel bad."
            n 2fsqsm "...Almost.{w=0.75}{nw}" 
            extend 2fchsmeme " Ehehe."

        if jn_snap._natsuki_win_streak == 10:
            n 2cllss "Wow...{w=1}{nw}"
            extend 2fchgn " is {i}someone{/i} having a bad day or what?"
            n 4fsqbg "...Or am I just {i}that{/i} good?{w=0.75}{nw}"
            extend 2fsqsmeme " Ehehe."

        elif jn_snap._natsuki_win_streak == 5:
            n 2fcsbg "Oh?{w=0.75}{nw}"
            extend 2fsqbg " What's that?"
            n 4fchgn "The sound of five in a row {i}already{/i}?{w=0.75}{nw}"
            extend 1nchgn " Ehehe."
            n 2fcscs "Well don't you worry,{w=0.2} [player].{w=0.75}{nw}"
            extend 2fcsbgeme " There's plenty more where {i}that{/i} came from!"

        elif jn_snap._natsuki_win_streak == 3:
            n 1fcssm "Ehehe.{w=0.75}{nw}"
            extend 2fchbg " Yep!{w=0.75}{nw}"
            extend 2fcssmesm " Yet another one for Team [n_name]!"

        else:
            n 1unmbs "Yes!{w=0.5}{nw}"
            extend 1uchbg " I win!{w=0.75}{nw}"
            extend 1fcsbgsbl " A-{w=0.2}as if it was gonna go any other way."
            n 1fsqsmeme "Ehehe."

    # What
    elif jn_snap.last_game_result == jn_snap.RESULT_DRAW:
        n 1csrfl "...Huh.{w=0.75}{nw}" 
        extend 1tnmfl " We {i}actually{/i} tied?"
        n 2tslpu "..."
        n 2tslaj "That's...{w=1}{nw}"
        extend 4tllsl " almost impressive,{w=0.2} actually.{w=1}{nw}" 
        extend 2cllsssbr " Weird."
        n 2ccssssbr "Well,{w=0.2} whatever."

    else:
        # Assume forfeit
        n 4tnmpu "Huh?{w=0.5}{nw}" 
        extend 4tnmbo " You're giving up?"
        n 1ullaj "Well,{w=0.2} I guess that's fine.{w=0.75}{nw}"
        extend 1fchgn " I'm taking that as a win for me!"

    # Award affinity for playing to completion with best girl
    $ Natsuki.calculatedAffinityGain()
    $ play_again_prompt = "Let's play again!"

    if jn_snap._player_win_streak >= 3:
        n 2fcsan "Uuuuuu-!"
        n 4fcsgsl "I-{w=0.2}I demand a rematch!{w=0.75}{nw}" 
        extend 2fcspol " I'm not going down like this!"

        show natsuki 2fcsgsl
        $ play_again_prompt = "We're playing again!"

    elif jn_snap._natsuki_win_streak >= 3:
        n 4fnmaj "Come on,{w=0.2} [player]!{w=0.75}{nw}"
        extend 2fcsbs " That {i}can't{/i} be all you've got!"
        n 2fchbs "Rematch!{w=0.3} Rematch!"

        show natsuki 2fchbg
        $ play_again_prompt = "Again!"

    else:
        n 2nsqsm "So..."

        show natsuki 2fchbg

    menu:
        n "[play_again_prompt]"

        "You're on!":
            n 2fcsbg "You bet you are,{w=0.2} [player]!"

            $ jn_snap._natsuki_skill_level += 1
            jump snap_start

        "I'll pass.":
            n 1cllsl "Awww..."
            n 2fsqss "...Spoilsport.{w=0.75}{nw}"
            extend 2fchsm " Ehehe."
            n 4ullss "Nah,{w=0.5}{nw}"
            extend 4nslss " I guess that's fine.{w=0.75}{nw}"

            if jn_snap._player_win_streak >= 3:
                extend 4fchsm " And thanks for playing."
                n 2csrpo "...Even if you did kick my butt."
                show natsuki 2nsrpo

            elif jn_snap._natsuki_win_streak >= 3:
                extend 4fchsm " And thanks for playing."
                n 2fsqcs "...Just bring more fight with you next time."
                extend 2fcssm " Ahaha."
                show natsuki 1fcssm

            else:
                extend 2fchsm " Thanks for playing~!"
                show natsuki 1fcssm

            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(1)
            play audio drawer
            $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
            $ jnPause(1)
            hide black with Dissolve(1.25)

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            jump ch30_loop

label snap_forfeit:
    hide screen snap_ui

    $ jn_snap._controls_enabled = False
    n 4ccsflsbr "W-{w=0.2}wait,{w=0.5}{nw}"
    extend 4cnmfl " what?{w=0.75}{nw}"
    extend 2knmfl " Come on,{w=0.2} [player]!"
    n 2cslaj "You aren't {i}seriously{/i} giving up already...{w=0.5}{nw}"

    show natsuki 2csqca
    menu:
        n "Are you?"

        "Yes, I give up.":
            n 2ccscaesm "..."
            n 2nllsl "Well,{w=0.2} I guess that's fine.{w=0.75}{nw}"
            extend 2fcsbg " But I'm taking that as a win for me!"

            # Hit the streaks
            $ jn_snap._player_win_streak = 0
            $ jn_snap._natsuki_win_streak += 1
            $ persistent._jn_snap_natsuki_wins += 1

            show natsuki 1fcssm
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(1)
            play audio drawer
            $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
            $ jnPause(1)
            hide black with Dissolve(1.25)

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            jump ch30_loop

        "In your dreams!":
            n 4fcsaj "Oh,{w=0.5}{nw}"
            extend 4fcsbg " {b}now{/b} it's on,{w=0.2} [player]!"
            show natsuki 4fsqsm

            $ jn_snap._controls_enabled = True
            $ jn_snap._natsuki_skill_level += 1
    
            show screen snap_ui
            jump snap_main_loop

# Animation for the Snap! popup fading out; we use this because Ren'Py sucks at image prediction
transform snap_popup_fadeout:
    easeout 0.75 alpha 0

# Self-explanatory, you dummy
image snap_popup:
    block:
        choice:
            "mod_assets/games/snap/snap_a.png"
        choice:
            "mod_assets/games/snap/snap_b.png"
        choice:
            "mod_assets/games/snap/snap_c.png"
        choice:
            "mod_assets/games/snap/snap_d.png"

    snap_popup_fadeout

# Game UI
screen snap_ui:
    zorder jn_snap._SNAP_UI_Z_INDEX

    # This is the card currently on the top of the pile being shown
    add jn_snap._current_table_card_image anchor(0, 0) pos(1000, 100)
    
    # Icons representing each player's hand
    add jn_snap._CARD_FAN_IMAGE_PLAYER anchor(0,0) pos (675, 110)
    add jn_snap._CARD_FAN_IMAGE_NATSUKI anchor(0,0) pos (675, 180)

    # Icon representing who's turn it is
    add jn_snap._turn_indicator_image anchor(0,0) pos(675, 250)

    # Game information
    text "Cards down: {0}".format(len(jn_snap._cards_on_table)) size 32 xpos 1000 ypos 50 style "categorized_menu_button"
    text "Your hand: {0}".format(len(jn_snap._player_hand)) size 22 xpos 750 ypos 125 style "categorized_menu_button"
    text "[n_name]'s hand: {0}".format(len(jn_snap._natsuki_hand)) size 22 xpos 750 ypos 195 style "categorized_menu_button"
    text "Turn: {0}".format(jn_snap.get_turn_label_to_display()) size 22 xpos 750 ypos 265 style "categorized_menu_button"

    # Options
    style_prefix "hkb"
    vbox:
        xpos 1012
        ypos 420

        # Hotkeys
        key "1" action [
            # Place
            If(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled, Function(jn_snap._place_card_on_table, True)) 
        ]
        key "2" action [
            # Snap
            If(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled, Function(jn_snap._call_snap, True))
        ]

        # Place card, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Place"):
            style "hkbd_option"
            action [
                Function(jn_snap._place_card_on_table, True),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        # Snap, but only selectable if there's enough cards down on the table, and both players are still capable of playing
        textbutton _("Snap!"):
            style "hkbd_option"
            action [
                Function(jn_snap._call_snap, True),
                SensitiveIf(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        null height 20

        # Forfeit, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Forfeit"):
            style "hkbd_option"
            action [
                Function(renpy.jump, "snap_forfeit"),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]
