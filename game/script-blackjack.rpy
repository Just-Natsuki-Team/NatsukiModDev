default persistent._jn_blackjack_unlocked = False
default persistent._jn_blackjack_explanation_given = False

# Win records
default persistent._jn_blackjack_player_wins = 0
default persistent._jn_blackjack_natsuki_wins = 0
default persistent._jn_blackjack_player_streak = 0
default persistent._jn_blackjack_natsuki_streak = 0
default persistent._jn_blackjack_player_best_streak = 0

# How JN blackjack works:
# ---
# Both Natsuki and the player start with a hand of two random cards; Natsuki's first card is always hidden until the game ends
# Player can stay or hit each round, with up to 5 cards in hand (3 total hits maximum)
# Natsuki will stay or hit based on probability and her own risk level
# If player or Nat goes over 21, they bust and lose
# If player or Nat gets 21 exactly, they win automatically on the turn they get 21 (Blackjack)
# Otherwise, win goes to whoever gets closest to 21 after drawing all cards, or if both players stay on the same turn
# Aces are considered as having value of 11, unless they'd cause Natsuki/the player to bust immediately on getting their hand (in which case, they equal 1)
# ---

init 0 python in jn_blackjack:
    from Enum import Enum
    import random
    import store
    import store.jn_plugins as jn_plugins
    import time

    # In-game tracking
    _controls_enabled = False
    _is_player_turn = None
    _is_player_committed = False
    _game_state = None

    _natsuki_staying = False
    _player_staying = False
    _rounds = 0

    # Collections of cards involved in the game
    _deck = []
    _natsuki_hand = []
    _player_hand = []

    class JNBlackjackStates(Enum):
        """
        Identifiers for the different ways a blackjack game can end.
        """
        draw = 1
        forfeit = 2
        natsuki_bust = 3
        natsuki_blackjack = 4
        natsuki_closest = 5
        player_bust = 6
        player_blackjack = 7
        player_closest = 8

    def _getHandSum(is_player):
        """
        Returns the total card value of a hand in blackjack.

        IN:
            - is_player - bool flag for whether to retrieve the sum from the players hand.

        OUT:
            - Total card value of the player's hand if is_player is True, otherwise total card value of Natsuki's hand.
        """
        return sum(card[1] for card in _player_hand) if is_player else sum(card[1] for card in _natsuki_hand)

    def _setup():
        """
        Performs initial setup for blackjack.
        The player and Natsuki are assigned two cards each to begin from a deck of shuffled cards.
        """
        del _deck[:]
        del _player_hand[:]
        del _natsuki_hand[:]

        global _is_player_committed
        global _controls_enabled
        global _game_state
        global _player_staying
        global _natsuki_staying

        _is_player_committed = False
        _controls_enabled = None
        _game_state = None
        _player_staying = False
        _natsuki_staying = False

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

                _deck.append(["mod_assets/games/cards/{0}/{1}.png".format(card_suit, card_number), card_value])

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

        # Player always moves first
        global _is_player_turn
        _is_player_turn = True

        return

    def _stayOrHit(is_player, is_hit):
        """
        Handles the action/display for the player or Natsuki staying or hitting during a game, then checks win conditions post-turn.
        Staying refers to passing the turn.
        Hitting refers to pulling another card, adding it to the hand.

        IN:
            - is_player - bool flag for whether it is the player making the move. If False, it is Natsuki's move.
            - is_hit - bool flag for whether the move is a hit (drawing a card). If False, it is a stay.
        """
        global _is_player_turn

        if is_player:
            # Player's turn
            if is_hit:
                _player_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))

            _is_player_turn = False
            global _player_staying
            global _is_player_committed
            _player_staying = not is_hit
            _is_player_committed = True

        else:
            # Natsuki's turn
            if is_hit:
                _natsuki_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))

            _is_player_turn = True
            global _natsuki_staying
            _natsuki_staying = not is_hit

        _checkWinConditions()

        return

    def _checkWinConditions():
        """
        Checks the current game conditions to determine if either the player or Natsuki has won.
        """
        natsuki_hand_sum = _getHandSum(is_player=False)
        player_hand_sum = _getHandSum(is_player=True)

        natsuki_wins = False
        player_wins = False

        global _game_state

        # Win via blackjack or bust
        if natsuki_hand_sum == 21 and player_hand_sum != 21:
            natsuki_wins = True
            _game_state = JNBlackjackStates.natsuki_blackjack

        elif player_hand_sum == 21 and natsuki_hand_sum != 21:
            player_wins = True
            _game_state = JNBlackjackStates.player_blackjack

        elif player_hand_sum == 21 and natsuki_hand_sum == 21:
            _game_state = JNBlackjackStates.draw

        elif natsuki_hand_sum > 21 and player_hand_sum < 21:
            player_wins = True
            _game_state = JNBlackjackStates.natsuki_bust

        elif player_hand_sum > 21 and natsuki_hand_sum < 21:
            natsuki_wins = True
            _game_state = JNBlackjackStates.player_bust

        elif player_hand_sum > 21 and natsuki_hand_sum > 21:
            _game_state = JNBlackjackStates.draw

        # Win via proximity
        elif (len(_natsuki_hand) == 5 and len(_natsuki_hand) == 5) or (_player_staying and _natsuki_staying):
            if natsuki_hand_sum > player_hand_sum:
                natsuki_wins = True
                _game_state = JNBlackjackStates.natsuki_closest

            elif player_hand_sum > natsuki_hand_sum:
                player_wins = True
                _game_state = JNBlackjackStates.player_closest

            else:
                # Draw somehow
                _game_state = JNBlackjackStates.draw

        if _game_state is not None:
            _controls_enabled = False

        if natsuki_wins:
            renpy.play("mod_assets/sfx/pencil_scribble.ogg")
            store.persistent._jn_blackjack_natsuki_wins += 1
            store.persistent._jn_blackjack_natsuki_streak += 1
            store.persistent._jn_blackjack_player_streak = 0

        if player_wins:
            renpy.play("mod_assets/sfx/pencil_scribble.ogg")
            store.persistent._jn_blackjack_player_wins += 1
            store.persistent._jn_blackjack_player_streak += 1
            store.persistent._jn_blackjack_natsuki_streak = 0

            if store.persistent._jn_blackjack_player_streak > store.persistent._jn_blackjack_player_best_streak:
                store.persistent._jn_blackjack_player_best_streak = store.persistent._jn_blackjack_player_streak

        return

    def _showSplashImage():
        """
        Shows a splash image corresponding to the current game state.
        """
        image_state_map = {
            JNBlackjackStates.natsuki_blackjack: "blackjack",
            JNBlackjackStates.player_blackjack: "blackjack",
            JNBlackjackStates.natsuki_bust: "bust",
            JNBlackjackStates.player_bust: "bust",
            JNBlackjackStates.natsuki_closest: "game",
            JNBlackjackStates.player_closest: "game",
            JNBlackjackStates.draw: "draw"
        }
        if _game_state in image_state_map:
            renpy.show(
                name="blackjack_popup",
                at_list=[store.blackjack_popup],
                layer="overlay",
                what=store.Image("mod_assets/games/blackjack/{0}.png".format(image_state_map[_game_state])),
                zorder=10)

        return

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the blackjack UI, including win/lose states.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _game_state == JNBlackjackStates.draw:
            return "It's a draw!"

        if (
            _game_state == JNBlackjackStates.natsuki_bust
            or _game_state == JNBlackjackStates.player_blackjack
            or _game_state == JNBlackjackStates.player_closest
        ):
            return "You win!"

        if (
            _game_state == JNBlackjackStates.natsuki_blackjack
            or _game_state == JNBlackjackStates.natsuki_closest
            or _game_state == JNBlackjackStates.player_bust
        ):
            return "You lose!"

        if _is_player_turn is None:
            return "Nobody!"

        return "Yours!" if _is_player_turn else "[n_name]"

    def __getQuitOrForfeitLabel():
        """
        Returns text for the quit/forfeit button, based on if the player has committed to the game by making a move.

        OUT:
            - str "Forfeit" if the player has made any move, otherwise "Quit"
        """
        return "Forfeit" if _is_player_committed else "Quit"

    def _getCardDisplayable(is_player, index):
        """
        Returns a layered displayable for a card in a hand for blackjack, consisting of the card face and a shadow (or nothing if no card exists for the index).
        Note that Nat's first card is always hidden/obfuscated unless the game is over.
        
        IN:
            - is_player - bool flag for whether to get a displayable for the player's or Natsuki's hand
            - index - int value for the card in the hand to get the displayable for
        
        OUT:
            - Displayable for the card at the given index

        """
        top_sprite = ""
        bottom_sprite = ""

        if is_player:
            top_sprite = _player_hand[index][0] if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"
            bottom_sprite = "mod_assets/games/cards/card_shadow.png" if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"

        else:
            if _game_state is None and index == 0:
                # Natsuki's first card is always obfuscated unless the game is concluded
                top_sprite =  "mod_assets/games/cards/hide.png"
                bottom_sprite =  "mod_assets/natsuki/etc/empty.png"
            
            else:
                top_sprite = _natsuki_hand[index][0] if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"
                bottom_sprite = "mod_assets/games/cards/card_shadow.png" if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"

        return renpy.display.layout.LiveComposite(
            (223, 312), # Displayable size; this needs to match the pixel size of the card asset
            (5, 5), bottom_sprite, # Shadow is offset to the right bottom
            (0, 0), top_sprite
        )

label blackjack_intro:
    n 2fnmbg "Alright!{w=0.75}{nw}" 
    extend 4fchgn " Let's play some blackjack!"

    if not persistent._jn_blackjack_explanation_given:
        n 4unmajeex "Oh,{w=0.2} right.{w=0.75}{nw}"
        extend 4flrsssbl " I almost forgot."
        n 2nsrsssbl "So before I get {i}too{/i} ahead of myself here..."

        show natsuki option_wait_curious
        menu:
            n "Did you need an explanation on how it all works,{w=0.2} or...?"

            "Yes please!":
                jump blackjack_explanation

            "No, I'm ready.":
                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 2fcssm "Heh."
                    n 2fnmss "You're ready,{w=0.5}{nw}"
                    extend  4fsqbg " are you?"
                    n 6fchgn "Ready to get a grade A butt kicking!{w=0.75}{nw}"
                    extend 4fnmbgedz " Let's go,{w=0.2} [player]!"

                elif dialogue_choice == 2:
                    n 7ttrbo "Hmm..."
                    n 7ulraj "Yeah,{w=0.5}{nw}"
                    extend  3unmbo " I'd say you're about ready too."
                    n 4fcsbg "...Ready for the bitter taste of defeat!{w=0.75}{nw}"
                    extend  4fchbgedz " Now let's go already!"

                else:
                    n 1fcssm "Ehehe.{w=0.75}{nw}"
                    extend 2tsqss  " Oh?{w=0.75}{nw}"
                    extend 2fsqbg " You're ready,{w=0.2} huh?"
                    n 4fnmbg "...Ready for a total thrashing!{w=0.75}{nw}"
                    extend 4nchgnedz " Bring it,{w=0.2} [player]!"

                $ persistent._jn_blackjack_explanation_given = True

    jump blackjack_start

label blackjack_explanation:
    if persistent._jn_blackjack_explanation_given:
        n 7ulraj "So like I was saying before,{w=0.5}{nw}"
        extend 7unmbo " Blackjack is pretty simple once you've got your head around the rules."

    else:
        n 4fcsbg "So!{w=0.75}{nw}"
        extend 7ullss " Blackjack is actually pretty simple,{w=0.5}{nw}" 
        extend 3unmaj " once you've got your head around the rules."

    n 5nsrsssbl "There's a bunch of different ways people play it,{w=0.5}{nw}"
    extend 4ulraj " so...{w=1}{nw}" 
    extend 6ccssm " we'll just go with something that works with only the two of us here."
    n 3ullaj "To start off,{w=0.2} we both get a couple random cards each from the deck."

    if not persistent._jn_blackjack_explanation_given:
        n 4fcsss "Yeah,{w=0.2} yeah.{w=0.75}{nw}"
        extend 2fsqsm " Don't worry,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fcsbgeme " I {i}always{/i} shuffle."

    n 3unmaj "Next,{w=0.2} we both take it in turns to either {i}hit{/i} -{w=0.5}{nw}" 
    extend 3clrss " draw another card,{w=0.5}{nw}" 
    extend 6unmbo " or {i}stay{/i} -{w=0.5}{nw}" 
    extend 3cllsm " which is just skipping our turn."
    n 4tnmss "What's the goal,{w=0.2} you ask?"
    n 7tlrss "Well...{w=1}{nw}" 
    extend 3fnmsm " we're basically trying to get the total value of our cards as close to twenty one as we can.{w=0.75}{nw}"
    extend 3fcsbg " That's called a {i}blackjack{/i}!"
    
    if not persistent._jn_blackjack_explanation_given:
        n 7cllss "As for how the cards are gonna work..."

        if persistent.jn_snap_explanation_given:
            n 7tnmbo "You remember Snap,{w=0.2} right?"

        else:
            n 3tnmbo "You've at least seen playing cards before,{w=0.2} right?"

        n 6ullaj "Well each card has a value -{w=0.5}{nw}"
        extend 3ccssm " obviously -{w=0.5}{nw}"
        extend 4nnmfl " but don't worry about the actual {i}suit{/i}:{w=0.75}{nw}" 
        extend 1tlrbo " diamonds or spades or whatever.{w=0.75}{nw}"
        extend 2fcssmesm " We only care about the {i}numbers{/i}!"

    else:
        n 3clrss "Like I said last time:{w=0.5}{nw}"
        extend 4tlraj " the suits of the cards don't matter here,{w=0.5}{nw}"
        extend 2fnmsm " so it's just the numbers you gotta keep an eye on."

    n 4clrss "The {i}face cards{/i} work kinda differently to the normal ones."
    n 6tnmaj "If you get a {i}king,{w=0.2} queen,{w=0.2} or jack{/i},{w=0.5}{nw}"
    extend 3ccssm " then those just count as being worth {i}ten{/i}."
    n 7tllfl "As for aces...{w=1}{nw}"
    extend 3nchgn " depends when you draw them!{w=0.75}{nw}"
    n 3ulrss "We'll say aces are worth {i}eleven{/i},{w=0.2} {i}unless{/i} you got one to start with that would make you bust instantly.{w=0.75}{nw}"
    extend 3fcssm " I'm not {i}that{/i} mean."
    n 4cllbg "But yeah -{w=0.5}{nw}"
    extend 2ullpu " if the ace would make you {i}lose on your first turn{/i},{w=0.5}{nw}"
    extend 2nnmbo " then it's just worth {i}one{/i} instead."
    n 7ulraj "We keep taking it in turns until one of us hits twenty one,{w=0.2} we both decide to {i}stay{/i} -{w=0.5}{nw}"
    extend 7unmbo " or one of us ends up with a hand that goes over twenty one."
    n 6fchbl "...That means you bust!"
    n 1cllss "Otherwise if neither of us end up busting,{w=0.5}{nw}"
    extend 2ccssm " then whoever got {i}closest{/i} to twenty one wins the round.{w=0.75}{nw}"
    extend 2fchbg "Easy peasy!"
    n 4unmaj "Oh,{w=0.2} yeah -{w=0.5}{nw}"
    extend 7clrss " and don't worry about keeping tabs on the score or anything.{w=0.75}{nw}"
    extend 6fcsbg " I've got it all covered!"
    n 3fchsm "Ehehe."
    n 4fnmsm "But yeah!{w=0.75}{nw}"
    extend 1ullss " I think that's pretty much everything I had."
    n 3ullaj "So...{w=1}{nw}"
    extend 7unmbo " how about it,{w=0.2} [player]?"

    $ persistent._jn_blackjack_explanation_given = True
    show natsuki option_wait_curious
    menu:
        n "Did you catch all that,{w=0.2} or...?"

        "Can you go over the rules again?":
            n 7tsqpueqm "Huh?{w=0.75}{nw}"
            extend 7tsqfl " You need me to go over that stuff again?"
            n 7cllfl "Well...{w=1}{nw}"
            extend 3nslbo " fine."
            n 3ccspoesi "But you better be listening this time,{w=0.2} [player]."

            jump blackjack_explanation

        "Got it. Let's play!":
            n 7tnmaj "Oh?{w=0.75}{nw}"
            extend 7tnmfl " You got all that?{w=0.75}{nw}"
            extend 3tsqsm " You sure,{w=0.2} [player]?"
            n 1fcssm "Ehehe."
            n 2fcsbg "Well then."
            n 2fnmbg "...Guess it's about time we put that to the test!{w=0.75}{nw}"
            extend 4fchgn " Let's do this,{w=0.2} [player]!"
            
            jump blackjack_start

        "Thanks, [n_name]. I'll play later.":
            n 1ccsemesi "..."
            n 2ccsfl "...Really,{w=0.5}{nw}"
            extend 2csqfl " [player]?"
            n 4fcsgs "I went through all that just for you to say you're gonna play{w=0.5}{nw}" 
            extend 4ftlem " {i}later{/i}?"
            n 1fsqca "..."
            n 3fchgn "Well,{w=0.75} your loss!{w=0.75}{nw}"
            extend 6fcssmesm " Just a word of warning though,{w=0.2} [player]..."

            if Natsuki.isLove(higher=True):
                n 3fcsbg "Don't think I'm gonna go any easier on you later either!"
                n 3fchbllsbr "You aren't gonna sweet-talk your way out of losing!"
            
            else:
                n 3fcsbg "Don't think I'm gonna go any easier on you later either!{w=0.75}{nw}"
                extend 3nchgnl " Ahaha."

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
    $ HKBHideButtons()
    show screen blackjack_ui
    play audio card_place
    $ jn_blackjack._setup()
    $ Natsuki.setInGame(True)
    $ jn_blackjack._controls_enabled = True

    jump blackjack_main_loop

label blackjack_main_loop:
    if jn_blackjack._game_state is not None:
        $ jn_utils.fireAndForgetFunction(jn_blackjack._showSplashImage)
        jump blackjack_end

    # Natsuki's hit/stay logic
    elif not jn_blackjack._is_player_turn:
        $ jn_blackjack._controls_enabled = False
        $ natsuki_hand_sum = jn_blackjack._getHandSum(is_player=False)

        if natsuki_hand_sum == 20 or len(jn_blackjack._natsuki_hand) == 5:
            $ jnPause(delay=random.randint(1, 3), hard=True)
            $ jn_blackjack._stayOrHit(is_player=False, is_hit=False)

        else:
            python:
                hit_percent = 0.50
                deck_used_high_cards = 0
                deck_used_low_cards = 0
                needed_to_blackjack = 21 - natsuki_hand_sum

                for card in jn_blackjack._natsuki_hand:
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

                risk_percent = jn_blackjack.store.persistent._jn_blackjack_natsuki_streak / 100 if jn_blackjack.store.persistent._jn_blackjack_natsuki_streak > 0 else 0
                risk_percent = 0.05 if risk_percent > 0.05 else risk_percent

                hit_percent += risk_percent
                hit_percent = 0.85 if hit_percent > 0.85 else hit_percent

                will_hit = random.randint(0, 100) / 100 <= hit_percent
                jnPause(delay=random.randint(2, 3), hard=True)
                jn_blackjack._stayOrHit(is_player=False, is_hit=will_hit)
    
    if jn_blackjack._game_state is None:
        $ jn_blackjack._controls_enabled = True

    $ jnPause(1)
    jump blackjack_main_loop

label blackjack_end:
    $ jn_blackjack._controls_enabled = False
    $ jn_blackjack._rounds += 1
    $ jnPause(delay=1, hard=True)
    $ chosen_response = ""

    if persistent._jn_blackjack_natsuki_streak in [3, 5, 10]:
        $ natsuki_streak_milestone_map = {
            3: [
                "Oh?{w=0.75} Three wins now?{w=0.75} Looks like {i}someone's{/i} got the makings of a streak going!",
                "Yes!{w=0.75} That makes three in a row!{w=0.75} Ehehe.",
                "Three wins and counting,{w=0.2} [player]!{w=0.75} Ehehe.",
                "What's that?{w=0.75} Three wins now?{w=0.75} Sounds like a streak to me!",
                "Oh yeah!{w=0.75} Three in a row!"
            ],
            5: [
                "Ha!{w=0.75} That makes five in a row now,{w=0.2} [player]!",
                "Yes!{w=0.75} Five in a row!{w=1} Top that,{w=0.2} {i}[player]{/i}.",
                "Aaaand that makes five!{w=0.75} Didn't I {i}say{/i} I was good?",
                "Yes!{w=0.75} That's five wins and counting!",
                "Yeah!{w=0.75} Five in a row!{w=0.75} Ehehe."
            ],
            10: [
                "Oh yeah!{w=0.75} Ten!{w=0.75} Now {i}that's{/i} what it means to be a pro,{w=0.2} [player]!",
                "Man...{w=1} ten in a row?{w=0.75} I am on {i}fire{/i} today!{w=0.75} Ehehe.",
                "Ha!{w=0.75} The big ten!{w=0.75} What have you got to say to that,{w=0.2} [player]?",
                "Yes!{w=0.75} Ten in a row!{w=0.75} Man...{w=1} I'm unstoppable!",
                "Jeez...{w=1} what is that now?{w=0.75} Ten?{w=0.75} At least {i}try{/i} to keep up,{w=0.2} [player]!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(natsuki_streak_milestone_map[persistent._jn_blackjack_natsuki_streak]))

    elif persistent._jn_blackjack_player_streak in [3, 5, 10]:
        $ player_streak_milestone_map = {
            3: [
                "L-{w=0.2}lucky break,{w=0.2} [player].{w=0.75} Anyone can luck out three times in a row!",
                "Yeah,{w=0.2} yeah.{w=0.75} T-{w=0.2}three in a row is nothing anyway!",
                "B-{w=0.2}bet you can't make that four in a row,{w=0.2} [player]!",
                "Y-{w=0.2}you better not be getting cocky.{w=0.75} Three in a row is nothing,{w=0.2} [player]!",
                "T-{w=0.2}three losses in a row is nothing!{w=0.75} I'm seriously just getting started!"
            ],
            5: [
                "Uuuuuu...!{w=0.75} Y-{w=0.2}you can stop getting so lucky now,{w=0.2} [player]!{w=0.75} Jeez...",
                "F-{w=0.2}five in a row now?{w=0.75} Are you kidding me?!",
                "Seriously?{w=0.75} That's five times in a row?!{w=0.75} Ugh...",
                "Nnnnnn-!{w=0.75} T-{w=0.2}there's no way you just got five in a row!{w=0.75} Cut me a break...",
                "Y-{w=0.2}you've got to be kidding me!{w=0.75} Five times?!{w=0.75} T-{w=0.2}there's no way this is anything but luck!"
            ],
            10: [
                "A-{w=0.2}are you reading my cards or what?!{w=0.75} {i}Ten{/i}?!{w=0.75} Jeez...",
                "Oh{w=0.2},{w=0.75} come {b}on{/b}!{w=0.75} There's no {i}way{/i} you just got ten in a row!{w=0.75} Ugh...",
                "T-{w=0.2}this is just getting ridiculous!{w=0.75} Ten in a row?!{w=0.75} I {i}swear{/i} these cards are rigged...",
                "Okay!{w=0.75} Okay!{w=0.75} You've made your point...{w=1} now can you go back to losing already? Yeesh...",
                "Nnnnnnnn-!{w=0.75} J-{w=0.2}just lose already,{w=0.2} [player]!{w=0.75} It's my turn to win something!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(player_streak_milestone_map[persistent._jn_blackjack_player_streak]))

    else:
        $ response_map = {
            jn_blackjack.JNBlackjackStates.draw: [
                "We drew?{w=0.75} Huh.",
                "Huh.{w=0.75} We drew?{w=0.75} Weird.",
                "Wait,{w=0.2} we tied?{w=0.75} Huh.",
                "A tie?{w=0.75} Weird.",
                "Come on,{w=0.2} [player]...{w=1} you gotta lose some time!",
                "Huh.{w=0.75} Another tie.",
                "Another draw,{w=0.2} huh?{w=0.75} Weird."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_bust: [
                "I bust?{w=0.75} Are you kidding me?!{w=0.75} Ugh...",
                "Oh,{w=0.2} come on!{w=0.75} I bust {i}again{/i}?!{w=0.75} Yeesh...",
                "Oh,{w=0.2} for-!{w=0.75} {i}Another{/i} bust?!{w=0.75} Seriously...",
                "A-{w=0.2}as {i}if{/i} I bust!{w=0.75} Man...",
                "Are you joking?!{w=0.75} I bust again?!",
                "You have {i}got{/i} to be joking.{w=0.75} Again?!",
                "Come on,{w=0.5} [n_name]...{w=1} get it together!",
                "Uuuuuuu...!{w=0.75} I {i}knew{/i} that was a crappy move!{w=0.75} Ugh..."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_blackjack: [
                "Yes!{w=0.5} Yes!{w=0.5} Blackjack!{w=0.75} Ehehe.",
                "Blackjack!{w=0.5} Blackjack!{w=0.5} Ehehe.",
                "Blackjack!{w=0.5} Yes!{w=0.5} Now {i}that's{/i} how it's done!",
                "Yes!{w=0.5} Now {i}that's{/i} more like it!{w=0.75} Ahaha.",
                "Better be taking notes,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Oh yeah!{w=0.75} Blackjack!",
                "Blackjack!{w=0.75} Blackjack!{w=0.75} Yes!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_closest: [
                "Yes!{w=0.5} I win!{w=0.3} I win!{w=0.75} Ehehe.",
                "Yes!{w=0.5} I win again!",
                "I was closer!{w=0.5} I win!{w=0.3} I win!",
                "Yes!{w=0.5} Take that,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Oh yeah!{w=0.75} Now {i}that's{/i} more like it!",
                "Yes!{w=0.75} Tough luck,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Ehehe.{w=0.75} Now {i}that's{/i} how it's played,{w=0.2} [player]!"
            ],
            jn_blackjack.JNBlackjackStates.player_bust: [
                "Pfft-!{w=0.75} Nice bust there,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Yep.{w=0.5} Total misplay,{w=0.2} [player]!",
                "Now that's what I call a bust!{w=0.75} Ehehe.",
                "Ahaha.{w=0.75} Sucks to be you,{w=0.2} [player]!",
                "Pffft!{w=0.75} You {i}sure{/i} you know how to play,{w=0.2} [player]?",
                "{i}Real{/i} smooth there,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Hey,{w=0.2} [player] -{w=0.5} you're meant to count up the cards!{w=0.75} Ehehe."
            ],s
            jn_blackjack.JNBlackjackStates.player_blackjack: [
                "Seriously?{w=0.75} You got a blackjack?!{w=0.75} Ugh...",
                "Yeah,{w=0.2} yeah.{w=0.75} Enjoy your luck while it lasts,{w=0.2} [player].",
                "Hmph.{w=0.75} You just lucked out this time.",
                "Oh,{w=0.2} come {i}on{/i}!{w=0.75} Again?{w=0.75} Seriously...",
                "N-{w=0.2}now that one was just pure luck!{w=0.75} Ugh...",
                "T-{w=0.2}that one was just pure chance!{w=0.75} Come on...",
                "Ugh...{w=1} for real?{w=0.75} You got another blackjack?"
            ],
            jn_blackjack.JNBlackjackStates.player_closest: [
                "Heh.{w=0.75} Enjoy the luck while it lasts,{w=0.2} [player].",
                "{i}Seriously{/i}?{w=0.75} Ugh...",
                "Come on!{w=0.75} Really?{w=0.75} Man...",
                "Yeah,{w=0.2} yeah.{w=0.75} Laugh it up,{w=0.2} [player].{w=0.75} Just you wait...",
                "Hmph.{w=1} Lucky break,{w=0.2} [player].{w=0.75} That's all I'm saying.",
                "Uuuuuu-!{w=0.75} You totally just got the better hand!{w=0.75} Ugh...",
                "Y-{w=0.2}you totally just got lucky this time,{w=0.2} [player].{w=0.75} That's all this is."
            ],
        }
        $ chosen_response = renpy.substitute(random.choice(response_map[jn_blackjack._game_state]))

    n "[chosen_response]"
    $ jnPause(0.5)
    jump blackjack_start

label blackjack_quit_forfeit:
    hide screen blackjack_ui
    $ natsuki_prompt = ""

    if jn_blackjack._is_player_committed:
        n 1tnmpueqm "Eh?{w=0.75}{nw}"
        extend 2tnmsleqm " You're done playing,{w=0.2} [player]?"
        
        if jn_blackjack._rounds == 0:
            n 4ccsflsbr "...W-{w=0.2}wait.{w=0.75}{nw}"
            extend 3fcsgssbr " Hang on just a second here,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3fnmgs " What do you mean?"
            n 4fcswr "We literally only just started {i}playing{/i}!{w=0.75}{nw}"
            extend 2flrem " Jeez..."
            n 2csqcasbl "You better not be pulling my leg again,{w=0.2} [player]."

            $ natsuki_prompt = "Do you actually {i}want{/i} to play blackjack or not?"
            show natsuki option_wait_sulky

        elif jn_blackjack._rounds < 6:
            n 1kslfl "Man...{w=1}{nw}"
            extend 4cnmem " really?{w=0.75}{nw}"
            extend 4ccsgssbl " Come on,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3ccsposbl " You can't be done this soon {i}already{/i}."
            n 3flrflsbr "Seriously -{w=0.5}{nw}"
            extend 3tnmfl " it's only been like [jn_blackjack._rounds] rounds!{w=0.75}{nw}"
            extend 4cnmaj " We've barely even started!"
            
            $ natsuki_prompt = "You can {i}easily{/i} play at least a couple more games...{w=0.3} right?"
            show natsuki option_wait_sulky

        else:
            n 2tdrsl "..."
            n 2tdrfl "Well...{w=1}{nw}"
            extend 2tlrbo " you have been playing a while.{w=0.75}{nw}"
            extend 4csrpo " I {i}guess{/i}."
            n 2nsqca "...Even if you {i}are{/i} calling it quits right in the middle of a game."
            n 2nllaj "So..."

            $ natsuki_prompt = "You're sure you don't wanna keep playing,{w=0.2} [player]?"
            show natsuki option_wait_curious

    else:
        n 4ccsss "Oh?{w=0.75}{nw}"
        extend 4fllss " What's this,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqbg " Why the cold feet all of a sudden?"
        n 1fsqsm "Ehehe."
        n 2fnmbg "Come on!{w=0.75}{nw}"
        extend 2fcsbs " Don't tell me you're giving up {i}that{/i} easily!"
        
        $ natsuki_prompt = "You can at {i}least{/i} stick it out to the end of this one,{w=0.2} right?"
        show natsuki option_wait_smug
        
    menu:
        n  "[natsuki_prompt]"

        "No, I'm done playing for now.":
            if jn_blackjack._is_player_committed:
                n 1kcsflesi "...Man.{w=0.75}{nw}"
                extend 4ksqfl " For real,{w=0.2} [player]?"
                n 2cslbo "..."
                n 2nslaj "Well...{w=1}{nw}"
                extend 5cdrca " I can't say I'm not at least a little disappointed.{w=0.75}{nw}"
                extend 5nlraj " But I guess that's fine."
                n 4ccsss "After all..."

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 3fcsbg "Just means another win for me!{w=0.75}{nw}"

                elif dialogue_choice == 2:
                    n 3fcssmesm "As if I'm turning down an easy win!{w=0.75}{nw}"

                else:
                    n 3nchgn "That's still a win for me!{w=0.75}{nw}"

                extend 3fcssmeme " Ehehe."

            else:
                n 1nsqpu "...Wow.{w=0.75}{nw}"
                extend 4tnmfl " And you didn't even end up making a single move!{w=0.75}{nw}"
                extend 4tlrbo " Huh."
                n 2tlrsl "..."
                n 2ulrfl "Well.{w=0.75}{nw}"
                extend 2fcsss " looks like {i}you{/i} know what they say at least,{w=0.5}{nw}" 
                extend 2fsqbg " [player]."
                n 6fcsbs "Guess the only winning move for you was not to play!{w=0.75}{nw}"
                extend 7fchsmeme " Ehehe."

            show natsuki 1fcssm
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(1)
            play audio drawer
            $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
            $ jnPause(1)
            hide black with Dissolve(1.25)

            $ jn_blackjack._rounds = 0
            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            $ HKBShowButtons()

            jump ch30_loop 

        "You're on!":
            if not jn_blackjack._is_player_committed:
                n 4fcsbgsbr "Y-{w=0.2}yeah!{w=0.75}{nw}"
                extend 2fcsbssbr " Now that's more like it!{w=0.75}{nw}"
                extend 2fsqbg " Some fighting spirit!"
                n 4fnmgsedz "Bring it on already,{w=0.2} [player]!"
            
            elif jn_blackjack._rounds == 0:
                n 1fspgs "Yeah!{w=0.75}{nw}"
                extend 3fcsbg " See?{w=0.75}{nw}"
                extend 3fchgn " I knew you had some kind of fight left in you!"
                n 1ccsbg "Besides..."
                n 2fsqbg "Only a real sore loser would just chicken out before they've even {i}lost{/i}.{w=0.75}{nw}"
                extend 2fsqsm " Ehehe."
                n 4fnmbs "Prove me wrong,{w=0.2} [player]!"
                
            else:
                n 1fsqsm "Ehehe.{w=0.75}{nw}"
                extend 3fcsbs " Now {i}that's{/i} what I'm talking about!"
                n 3fnmsm "..."
                n 3fsqbg "Well?{w=0.75}{nw}"
                extend 4fcsbg " What're you waiting for?"
                n 4fchgn "Make your move already,{w=0.2} [player]!"
            
            show screen blackjack_ui
            jump blackjack_main_loop

    return

style blackjack_note_text:
    font gui.interface_font
    size gui.interface_text_size
    color "#000000"
    outlines []

    line_overlap_split 8
    line_spacing 8
    line_leading 8

transform blackjack_card_scale_down:
    zoom 0.675

transform blackjack_popup:
    parallel:
        ease 0.33 alpha 1.0 yoffset -30
        easeout 0.75 alpha 0

screen blackjack_ui:
    zorder 5

    add "mod_assets/natsuki/desk/table/topdown/table.png" anchor(0, 0) pos(0, 0)
    add "mod_assets/natsuki/desk/table/topdown/accessories.png" anchor(0, 0) pos(0, 0)
    add "mod_assets/natsuki/desk/table/topdown/nameplates.png" anchor(0, 0) pos(0, 0)

    # Natsuki's hand
    vbox:
        pos(40, 60)
        text "[n_name]" style "categorized_menu_button" size 24 outlines [(3, "#2E1503EF", 0, 0)]
        null height 10

        grid 5 1:
            spacing 10
            #style "blackjack_card_scale"
            add jn_blackjack._getCardDisplayable(is_player=False, index=0) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=1) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=2) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=3) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=4) anchor(0,0) at blackjack_card_scale_down

    # Player's hand
    vbox:
        pos(40, 342)
        if persistent._jn_blackjack_show_hand_value:
            text "[player]: {0}".format(jn_blackjack._getHandSum(True)) style "categorized_menu_button" size 24 outlines [(3, "#2E1503EF", 0, 0)]

        else:
            text "[player]" style "categorized_menu_button" size 24 outlines [(3, "#2E1503EF", 0, 0)]

        null height 10

        grid 5 1:
            spacing 10
            add jn_blackjack._getCardDisplayable(is_player=True, index=0) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=1) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=2) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=3) anchor(0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=4) anchor(0,0) at blackjack_card_scale_down

    # Information and controls
    vbox:
        xpos 960 ypos 230

        grid 1 3:
            spacing 10
            text "[player]: {0}".format(persistent._jn_blackjack_player_wins) style "blackjack_note_text"
            text "[n_name]: {0}".format(persistent._jn_blackjack_natsuki_wins) style "blackjack_note_text"
            text "Turn: {0}".format(jn_blackjack._getCurrentTurnLabel()) style "blackjack_note_text"

        null height 120

        # Controls
        style_prefix "hkb"
        
        # Hit
        key "1" action [
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 5, Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        textbutton _("Hit!"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, True),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 5)]

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

        # Quit/Forfeit
        textbutton _(jn_blackjack.__getQuitOrForfeitLabel()):
            style "hkbd_option"
            action [
                Function(renpy.jump, "blackjack_quit_forfeit"),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]
