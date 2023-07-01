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

    # Collections of cards involved in the game
    _deck = []
    _natsuki_hand = []
    _player_hand = []

    class JNBlackjackEndings(Enum):
        """
        Identifiers for the different ways a Blackjack game can end.
        """
        draw = 1
        forfeit = 2
        natsuki_bust = 3
        natsuki_blackjack = 4
        natsuki_closest = 5
        player_bust = 6
        player_blackjack = 6
        player_closest = 7

    def _clear():
        """
        Resets all background data for Blackjack, including the deck, hands and tracking.
        """
        del _deck[:]
        del _player_hand[:]
        del _natsuki_hand[:]

        global _is_player_turn
        global _controls_enabled
        _is_player_turn = None
        _controls_enabled = None

    def _setup():
        """
        Performs initial setup for Blackjack.
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
            for card_value in range(1, 14):
                #TODO: this might as well be image path! (given we don't use suit apart from that)
                _deck.append((card_suit, card_value))

        random.shuffle(_deck)

        # Assign each player their starting hand
        _player_hand.append(_deck.pop())
        _natsuki_hand.append(_deck.pop())

        _player_hand.append(_deck.pop())
        _natsuki_hand.append(_deck.pop())

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
                _player_hand.append(_desk.pop(0))
                renpy.play("mod_assets/sfx/card_place.ogg")

            _is_player_turn = False

        else:
            # Natsuki's turn
            if is_hit:
                _natsuki_hand.append(_desk.pop(0))
                renpy.play("mod_assets/sfx/card_place.ogg")

            _is_player_turn = True

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the blackjack UI.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _player_turn is None:
            return "Nobody!"

        return "Yours!" if _is_player_turn else "[n_name]"

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
            return "mod_assets/games/cards/{0}/{1}.png".format(_player_hand[index][0], _player_hand[index][1]) if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"

        else:
            if _last_game_result is not None and index == 0:
                return "mod_assets/games/cards/blank.png"
            
            return "mod_assets/games/cards/{0}/{1}.png".format(_natsuki_hand[index][0], _natsuki_hand[index][1]) if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"

label blackjack_intro:
    # TODO: Writing
    n "Alright! Let's play some Blackjack!"

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
    show screen blackjack_ui
    play audio card_shuffle
    $ jn_blackjack._setup()

    # TODO: Writing
    n "Start"

    $ Natsuki.setInGame(True)
    $ jn_blackjack._controls_enabled = True
    jump blackjack_main_loop

label blackjack_main_loop:
    # Setup to check for winners
    python:
        natsuki_hand_sum = 0
        player_hand_sum = 0
        natsuki_wins = False
        player_wins = False

        for card in jn_blackjack._natsuki_hand:
            natsuki_hand_sum += card[0]

        for card in jn_blackjack._player_hand:
            player_hand_sum += card[0]

    # Win via Blackjack or bust
    if natsuki_hand_sum == 21 or player_hand_sum > 21:
        $ natsuki_wins = True
        $ jn_blackjack._last_game_result = jn_blackjack.JNBlackjackEndings.natsuki_blackjack if natsuki_hand_sum == 21 else jn_blackjack.JNBlackjackEndings.player_bust

    elif player_hand_sum == 21 or natsuki_hand_sum > 21:
        $ player_wins = True
        $ jn_blackjack._last_game_result = jn_blackjack.JNBlackjackEndings.player_blackjack if player_hand_sum == 21 else jn_blackjack.JNBlackjackEndings.natsuki_bust

    # Win via proximity
    elif len(jn_blackjack._natsuki_hand) == 4 and len(jn_blackjack._natsuki_hand) == 4:
        if 21 - natsuki_hand_sum < 21 - player_hand_sum:
            $ natsuki_wins = True
            $ jn_blackjack._last_game_result = jn_blackjack.JNBlackjackEndings.natsuki_closest

        else:
            $ player_wins = True
            $ jn_blackjack._last_game_result = jn_blackjack.JNBlackjackEndings.player_closest

    if natsuki_wins:
        $ persistent._jn_blackjack_natsuki_wins += 0
        jump blackjack_end

    if player_wins:
        $ persistent._jn_blackjack_player_wins += 0
        jump blackjack_end

    $ jnPause(delay=random.randint(2, 3), hard=True)

    # Natsuki's Blackjack logic
    if not jn_blackjack._is_player_turn:
        # TODO - need to weight this somehow. Current card values + probability of getting high/low card. Risk level? 

    jump blackjack_main_loop

label blackjack_end:
    $ jn_blackjack._controls_enabled = False

    #TODO: end route conditions/handling

    # Reset the ingame flag, then hop back to ch30 as getting here has lost context
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

        "No:"
            n "ending"
            jump blackjack_end

    return

screen blackjack_ui:
    zorder 5

    add "mod_assets/natsuki/desk/table/topdown/table.png" anchor(0, 0) pos(0, 0)

    # Natsuki's hand
    add jn_blackjack._getCardSprite(is_player=False, index=0) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=False, index=1) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=False, index=2) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=False, index=3) anchor(0,0) pos (0, 0)

    # Player's hand
    add jn_blackjack._getCardSprite(is_player=True, index=0) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=True, index=1) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=True, index=2) anchor(0,0) pos (0, 0)
    add jn_blackjack._getCardSprite(is_player=True, index=3) anchor(0,0) pos (0, 0)

    # Information
    text "Your wins" size 32 xpos 1000 ypos 50 style "categorized_menu_button"
    text "[n_name]'s wins" size 32 xpos 1000 ypos 50 style "categorized_menu_button"
    
    text "Turn: {0}".format(jn_blackjack._current_turn) size 22 xpos 750 ypos 265 style "categorized_menu_button"

    # Controls
    style_prefix "hkb"
    vbox:
        xpos 1012
        ypos 420

        # Hotkeys

        key "1" action [
            # Hit
            If(
                jn_blackjack._is_player_turn and jn_blackjack._controls_enabled,
                Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        key "2" action [
            # Stay
            If(
                jn_blackjack._is_player_turn and jn_blackjack._controls_enabled,
                Function(jn_blackjack._stayOrHit, True, False))
        ]

        # Buttons

        # Hit
        textbutton _("Hit!"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, True),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]

        # Stay
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
