default persistent._jn_blackjack_unlocked = False
default persistent._jn_blackjack_explanation_given = False

# Win records
default persistent._jn_blackjack_player_wins = 0
default persistent._jn_blackjack_natsuki_wins = 0

# NOTES ON BLACKJACK
# Natsuki starts off with 2, but 1st card hidden
# Player starts off with 2
# Player can stay or hit each round, max 4 cards in hand
# Nat will stay or hit based on probability and her own risk level
# If player or Nat goes over 21, they bust and lose
# If player or Nat gets 21 exactly, they win automatically on the turn they get 21
# Otherwise, win goes to whoever gets closest to 21 after drawing all cards
# Aces are considered as having value of 11, unless they'd cause a player to bust immediately on getting their hand (in which case, they equal 1)

init 0 python in jn_blackjack:
    from Enum import Enum
    import random
    import store
    import time

    # In-game tracking
    _controls_enabled = False
    _is_player_turn = None
    _player_win_streak = 0
    _natsuki_win_streak = 0
    _last_game_result = None

    _natsuki_staying = False
    _player_staying = False

    # Collections of cards involved in the game
    _deck = []
    _natsuki_hand = []
    _player_hand = []

    class JNBlackjackEndings(Enum):
        """
        Identifiers for the different ways a blackjack game can end.
        """
        draw = 1
        forfeit = 2
        natsuki_bust = 3
        natsuki_blackjack = 4
        natsuki_closest = 5
        player_bust = 6
        player_blackjack = 6
        player_closest = 7

    def _getHandSum(is_player):
        """
        """
        return sum(card[1] for card in _player_hand) if is_player else sum(card[1] for card in _natsuki_hand)

    def _clear():
        """
        Resets all background data for blackjack, including the deck, hands and tracking.
        """
        del _deck[:]
        del _player_hand[:]
        del _natsuki_hand[:]

        global _is_player_turn
        global _controls_enabled
        global _last_game_result
        _is_player_turn = None
        _controls_enabled = None
        _last_game_result = None

    def _setup():
        """
        Performs initial setup for blackjack.
        The player and Natsuki are assigned two cards each to begin from a deck of shuffled cards.
        """
        _clear()

        # Generate all possible card combinations based on suits and values; unlike Snap this should include K/Q/J
        for card_suit in [
            "clubs",
            "diamonds",
            "hearts",
            "spades"
        ]:
            for card_number in range(1, 14):
                card_value = card_number

                if card_value == 1:
                    # Aces are considered eleven unless it would cause an instant loss
                    card_value = 11

                else:
                    # All face cards are considered to have a value of ten, so we cap
                    card_value = 10 if card_value > 10 else card_value

                _deck.append(("mod_assets/games/cards/{0}/{1}.png".format(card_suit, card_number), card_value))

        random.shuffle(_deck)

        # Assign each player their starting hand
        _player_hand.append(_deck.pop(0))
        _player_hand.append(_deck.pop(0))
        _natsuki_hand.append(_deck.pop(0))
        _natsuki_hand.append(_deck.pop(0))

        # Set aces to one if they would result in an instant bust for Natsuki
        if _getHandSum(is_player=False) > 21:
            for card in _natsuki_hand:
                card[1] = 1 if card[1] == 11 else card[1]

        # Set aces to one if they would result in an instant bust for the player
        if _getHandSum(is_player=True) > 21:
            for card in _player_hand:
                card[1] = 1 if card[1] == 11 else card[1]

        # Value adjustments so neither Natsuki or the player can instantly bust: an Ace will be set to a value of one 

        global _is_player_turn
        _is_player_turn = True

    def _stayOrHit(is_player, is_hit):
        """
        Handles the action/display for the player or Natsuki staying or hitting during a game.
        Staying refers to passing the turn.
        Hitting refers to pulling another card, adding it to the hand.
        """
        global _is_player_turn

        if is_player:
            # Player's turn
            if is_hit:
                _player_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_place.ogg")

            _is_player_turn = False
            global _player_staying
            _player_staying = not is_hit

        else:
            # Natsuki's turn
            if is_hit:
                _natsuki_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_place.ogg")

            _is_player_turn = True
            global _natsuki_staying
            _natsuki_staying = not is_hit

        _checkWinConditions()

    def _checkWinConditions():
        """
        """
        natsuki_hand_sum = _getHandSum(is_player=False)
        player_hand_sum = _getHandSum(is_player=True)
        natsuki_wins = False
        player_wins = False

        global _last_game_result

        # Win via blackjack or bust
        if natsuki_hand_sum == 21 and player_hand_sum != 21:
            natsuki_wins = True
            _last_game_result = JNBlackjackEndings.natsuki_blackjack

        elif natsuki_hand_sum > 21:
            player_wins = True
            _last_game_result = JNBlackjackEndings.natsuki_bust

        elif player_hand_sum == 21 and natsuki_hand_sum != 21:
            player_wins = True
            _last_game_result = JNBlackjackEndings.player_blackjack

        elif player_hand_sum > 21:
            natsuki_wins = True
            _last_game_result = JNBlackjackEndings.player_bust

        elif player_hand_sum == 21 and natsuki_hand_sum == 21:
            _last_game_result = JNBlackjackEndings.draw

        # Win via proximity
        elif (len(_natsuki_hand) == 4 and len(_natsuki_hand) == 4) or (_player_staying and _natsuki_staying):
            if 21 - natsuki_hand_sum < 21 - player_hand_sum:
                natsuki_wins = True
                _last_game_result = JNBlackjackEndings.natsuki_closest

            elif 21 - player_hand_sum < 21 - natsuki_hand_sum:
                player_wins = True
                _last_game_result = JNBlackjackEndings.player_closest

            else:
                # Draw somehow
                _last_game_result = JNBlackjackEndings.draw

        if natsuki_wins:
            store.persistent._jn_blackjack_natsuki_wins += 1

        if player_wins:
            store.persistent._jn_blackjack_player_wins += 1

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the blackjack UI.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _is_player_turn is None:
            return "Nobody!"

        return "Yours!" if _is_player_turn else "[n_name]"

    def _getCardDisplayable():
        pass

    def _getCardSprite(is_player, index):
        """
        Returns the sprite path for a card in a hand for blackjack.
        Note that Nat's first card is always hidden unless the game is over.
        
        IN:
            - is_player - bool flag for whether to get a sprite for the player's or Natsuki's hand
            - index - int value for the card in the hand to get the sprite for
        
        OUT:
            - str sprite path for the card at the given index, a hidden placeholder for Nat's first card if game ongoing, or empty it is doesn't exist.
        """
        if is_player:
            return _player_hand[index][0] if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"

        else:
            if _last_game_result is None and index == 0:
                return "mod_assets/games/cards/hide.png"
            
            return _natsuki_hand[index][0] if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"

label blackjack_intro:
    # TODO: Writing
    n "Alright! Let's play some blackjack!"

    if not persistent._jn_blackjack_explanation_given:
        n "Oh, right. Did you need an explanation on how it all works, or...?"

        show natsuki option_wait_curious
        menu:
            n "Need me to run through the rules real quick?"

            "Yes, please!":
                jump blackjack_explanation

            "No, I'm ready.":
                n "Let's go already then!"
                $ persistent._jn_blackjack_explanation_given = True

    jump blackjack_start

label blackjack_explanation:
    # TODO: Writing
    n "Here's how it works..."
    n "And that's that!"

    show natsuki option_wait_curious
    menu:
        n "Did that all make sense to you?"

        "Can you go over the rules again?":
            n 1tsqpueqm "Huh?{w=0.75}{nw}" 
            extend 1tllca " Well,{w=0.2} okay..."

            jump blackjack_explanation

        "Got it. Let's play!":
            n "Finally! Now let's play!"

            $ persistent._jn_blackjack_explanation_given = True
            jump blackjack_start

        "Thanks, [n_name]. I'll play later.":
            n "Wow... really? Fine."

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

label blackjack_start:
    # TODO: Writing

    $ HKBHideButtons()
    show screen blackjack_ui
    play audio card_shuffle
    $ jn_blackjack._setup()
    $ Natsuki.setInGame(True)
    $ jn_blackjack._controls_enabled = True

    jump blackjack_main_loop

label blackjack_main_loop:
    if jn_blackjack._last_game_result is not None:
        jump blackjack_end

    # Natsuki's hit/stay logic
    if not jn_blackjack._is_player_turn:
        $ natsuki_hand_sum = jn_blackjack._getHandSum(is_player=False)
        if natsuki_hand_sum == 20:
            $ jnPause(delay=random.randint(2, 3), hard=True)
            $ jn_blackjack._stayOrHit(is_player=False, is_hit=False)

        else:
            python:
                hit_percent = 0.50
                deck_used_high_cards = 0
                deck_used_low_cards = 0
                needed_to_blackjack = 21 - natsuki_hand_sum

                for card in jn_snap._natsuki_hand:
                    if card[1] > 6:
                        deck_used_high_cards += 1
                    else:
                        deck_used_low_cards +=1

                if (
                    deck_used_high_cards > deck_used_low_cards and needed_to_blackjack <= 6
                    or deck_used_low_cards > deck_used_high_cards and needed_to_blackjack > 6
                ):
                    hit_percent += 0.35
                elif (
                    deck_used_high_cards == deck_used_low_cards and needed_to_blackjack <= 6
                    or deck_used_high_cards == deck_used_low_cards and needed_to_blackjack > 6
                ):
                    hit_percent += 0.20

                if hit_percent == 0.50 and needed_to_blackjack <= 6:
                    hit_percent -= 35

                risk_percent = jn_snap._natsuki_win_streak / 100 if jn_snap._natsuki_win_streak > 0 else 0
                risk_percent = 0.05 if risk_percent > 0.05 else risk_percent

                hit_percent += risk_percent
                hit_percent = 0.85 if hit_percent > 0.85 else hit_percent

                will_hit = random.randint(0, 100) / 100 <= hit_percent
                jnPause(delay=random.randint(2, 3), hard=True)
                jn_blackjack._stayOrHit(is_player=False, is_hit=will_hit)

    $ jnPause(1)
    jump blackjack_main_loop

label blackjack_end:
    $ jn_blackjack._controls_enabled = False
    $ jnPause(delay=5, hard=True)
    hide screen blackjack_ui

    #TODO: Writing
    if jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.draw:
        n 1tsrpu "We drew? Weird."

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.natsuki_bust:
        n 1fupem "I bust? Are you kidding me?! Ugh..."

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.natsuki_blackjack:
        n 1nchgnl "Yes! blackjack! blackjack! Ehehe."

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.natsuki_closest:
        n 1nchgnl "Yes! I win! I win!"

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.player_bust:
        n 1fchgn "Ha! You bust that one, [player]!"

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.player_blackjack:
        n 1cslpo "Uuuuu...! Are you kidding me?! You got a blackjack? Man..."

    elif jn_blackjack._last_game_result == jn_blackjack.JNBlackjackEndings.player_closest:
        n 1ccspo "Hmph. You just got lucky again, [player]."

    n 1ulraj "So..."
    show natsuki option_wait_curious
    menu:
        n "Up for another game?"

        "You're on!":
            n "You bet!"

            jump blackjack_start

        "I'll pass.":
            n "Thanks for playing!"

            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            jump ch30_loop

label blackjack_forfeit:
    # TODO: writing
    n "Giving up?"
    menu:

        "Yes":
            n "continuing"

            jump blackjack_main_loop

        "No":
            n "ending"

            $ jn_blackjack._last_game_result = jn_blackjack.JNBlackjackEndings.forfeit
            jump blackjack_end

    return

style blackjack_card_scale:
    xysize(178, 250)

style blackjack_note_text:
    font gui.interface_font
    size gui.interface_text_size
    color "#000000"
    outlines []

    line_overlap_split 8
    line_spacing 8
    line_leading 8

transform blackjack_card_scale_down:
    zoom 0.75

screen blackjack_ui:
    zorder 5

    add "mod_assets/natsuki/desk/table/topdown/table.png" anchor(0, 0) pos(0, 0)
    add "mod_assets/natsuki/desk/table/topdown/sticky.png" anchor(0, 0) pos(0, 0)

    # Natsuki's hand
    vbox:
        pos(60, 60)
        text "[n_name]" style "categorized_menu_button"
        null height 10

        grid 4 1:
            spacing 20
            style "blackjack_card_scale"
            add jn_blackjack._getCardSprite(is_player=False, index=0) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=False, index=1) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=False, index=2) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=False, index=3) anchor(0,0) at blackjack_card_scale_down
    
    # Player's hand
    vbox:
        pos(60, 372)
        text "[player]" style "categorized_menu_button"
        null height 10

        grid 4 1:
            spacing 20
            style "blackjack_card_scale"
            add jn_blackjack._getCardSprite(is_player=True, index=0) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=True, index=1) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=True, index=2) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardSprite(is_player=True, index=3) anchor(0,0) at blackjack_card_scale_down

    # Information and controls
    vbox:
        xpos 960 ypos 230

        grid 1 3:
            spacing 20

            text "Your wins: {0}".format(persistent._jn_blackjack_player_wins) style "blackjack_note_text"
            text "[n_name]'s wins: {0}".format(persistent._jn_blackjack_natsuki_wins) style "blackjack_note_text"
            text "Turn: {0}".format(jn_blackjack._getCurrentTurnLabel()) style "blackjack_note_text"

        null height 120

        # Controls
        style_prefix "hkb"
        
        # Hit
        key "1" action [
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled, Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        textbutton _("Hit!"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, True),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]

        # Stay
        key "2" action [
            # Stay hotkey
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled, Function(jn_blackjack._stayOrHit, True, False))
        ]
        textbutton _("Stay"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, False),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]

        null height 20

        # Forfeit
        textbutton _("Forfeit"):
            style "hkbd_option"
            action [
                Function(renpy.jump, "blackjack_forfeit"),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]
