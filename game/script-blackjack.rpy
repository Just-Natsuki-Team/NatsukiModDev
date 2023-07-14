default persistent._jn_blackjack_unlocked = False
default persistent._jn_blackjack_explanation_given = False

# Win records
default persistent._jn_blackjack_player_wins = 0
default persistent._jn_blackjack_natsuki_wins = 0
default persistent._jn_blackjack_player_streak = 0
default persistent._jn_blackjack_natsuki_streak = 0
default persistent._jn_blackjack_player_best_streak = 0

# NOTES ON BLACKJACK
# Natsuki starts off with 2, but 1st card hidden
# Player starts off with 2
# Player can stay or hit each round, max 5 cards in hand (3 hits)
# Nat will stay or hit based on probability and her own risk level
# If player or Nat goes over 21, they bust and lose
# If player or Nat gets 21 exactly, they win automatically on the turn they get 21
# Otherwise, win goes to whoever gets closest to 21 after drawing all cards, or if both players stay on the same turn
# Aces are considered as having value of 11, unless they'd cause a player to bust immediately on getting their hand (in which case, they equal 1)

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

    _splash_sprite = "draw"

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

    def _clear():
        """
        Resets all background data for blackjack, including the deck, hands and tracking.
        """
        del _deck[:]
        del _player_hand[:]
        del _natsuki_hand[:]

        global _is_player_turn
        global _is_player_committed
        global _controls_enabled
        global _game_state
        global _player_staying
        global _natsuki_staying

        _is_player_turn = None
        _is_player_committed = False
        _controls_enabled = None
        _game_state = None
        _player_staying = False
        _natsuki_staying = False

        return

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
            store.persistent._jn_blackjack_natsuki_streak = 0
            store.persistent._jn_blackjack_player_streak += 1

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
        Returns the turn text to display on the blackjack UI.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _game_state == JNBlackjackStates.draw:
            return  "Draw!"

        if (
            _game_state == JNBlackjackStates.natsuki_bust
            or _game_state == JNBlackjackStates.player_blackjack
            or _game_state == JNBlackjackStates.player_closest
        ):
            return  "You win!"

        if (
            _game_state == JNBlackjackStates.natsuki_blackjack
            or _game_state == JNBlackjackStates.natsuki_closest
            or _game_state == JNBlackjackStates.player_bust
        ):
            return  "You lost!"

        if _is_player_turn is None:
            return  "Nobody!"

        return  "Yours!" if _is_player_turn else "[n_name]"

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

    # TODO: Remove this!
    jn_plugins.registerExtrasOption(
        option_name="Blackjack Test",
        visible_if="store.persistent._jn_blackjack_unlocked",
        jump_label="blackjack_intro"
    )

label blackjack_intro:
    # TODO: Writing
    n 2fnmbg "Alright!{w=0.75}{nw}" 
    extend 4fchgn  " Let's play some blackjack!"

    if not persistent._jn_blackjack_explanation_given:
        n  "Oh, right."
        extend " I almost forgot."
        n  "So before I get {i}too{/i} ahead of myself here..."

        show natsuki option_wait_curious
        menu:
            n  "Did you need an explanation on how it all works, or...?"

            "Yes, please!":
                jump blackjack_explanation

            "No, I'm ready.":
                    $ dialogue_choice = random.randint(1, 3)
                    if dialogue_choice == 1:
                        n "Heh."
                        n "You're ready,"
                        extend " are you?"
                        n "Ready to get a grade A butt kicking!"
                        extend " Let's go, [player]!"

                    elif dialogue_choice == 2:
                        n "Hmm..."
                        n "Yeah,"
                        extend " I'd say you're about ready too."
                        n "...Ready for the bitter taste of defeat!"
                        extend " Now let's go already!"

                    else:
                        n  "Ehehe."
                        extend " Oh?"
                        extend " You're ready, huh?"
                        n "...Ready for a total thrashing!"
                        extend " Bring it, [player]!"

                $ persistent._jn_blackjack_explanation_given = True

    jump blackjack_start

label blackjack_explanation:
    if persistent._jn_blackjack_explanation_given:
        n  "So like I was saying before,"
        extend  " Blackjack is pretty simple once you've got your head around the rules."

    else:
        n  "So!"
        extend  " Blackjack is actually pretty simple, once you've got your head around the rules."

    n  "There's a bunch of different ways people play it,"
    extend  " so..." 
    extend  " we'll just go with something that works with only the two of us here."

    n  "To start off, we both get a couple random cards each from the deck."
    n  "Then, we both take it in turns to either {i}hit{/i} -" 
    extend  " draw another card," 
    extend  " or {i}stay{/i} -" 
    extend  " which is pretty much just skipping our turn."
    n  "So what's the goal, you ask?"
    n  "Well..." 
    extend  " we're basically trying to get the total value of our cards as close to twenty one as we can -"
    extend  " a blackjack!"

    n  "As for how the cards are gonna work..."
    n  "You remember Snap,"  
    extend  " right?"
    n  "Well, each card has a value -"
    extend  " obviously -"
    extend  " but don't worry about the actual {i}suit{/i}:" 
    extend  " diamonds or spades or whatever."
    extend  " We only care about the {i}numbers{/i}!"

    n  "The {i}face cards{/i} work a bit differently to the normal ones."
    n  "If you get a {i}king, queen or jack{/i},"
    extend  " then those just count as being worth {i}ten{/i}."
    n  "As for aces..."
    extend  " depends when you draw them!"
    extend  " But as a rule..."
    n  "Aces are worth {i}eleven{/i}, {i}unless you got one to start with that would make you bust instantly{/i}."
    extend  " Even I'm not that cruel!"
    n  "But yeah -"
    extend  " if the ace would make you {i}bust on your first turn{/i},"
    extend  " then it's just worth {i}one{/i} instead."

    n  "So..."
    n  "The general idea is that we keep taking it in turns until one of us hits twenty one, we both decide to {i}stay{/i} -"
    extend  " or one of us ends up with a hand that goes over twenty one."
    n  "...That means you bust!"
    n  "If neither of us end up busting,"
    extend  " then whoever got {i}closest{/i} to twenty one wins the round!"
    extend  " Simple, right?"

    n  "Oh -"
    extend  " and don't worry about keeping tabs on the score or anything."
    extend  " I've got it all covered!"
    extend  " Ehehe."
    n  "But yeah!"
    extend  " I think that's pretty much everything I had."
    n  "So..."
    extend  " how about it, [player]?"

    show natsuki option_wait_curious
    menu:
        #TODO: finish off script here
        n  "Did that all make sense to you?"

        "Can you go over the rules again?":
            n 1tsqpueqm "Huh?{w=0.75}{nw}" 
            extend 1tllca " Well,{w=0.2} okay..."

            jump blackjack_explanation

        "Got it. Let's play!":
            n  "Finally! Now let's play!"

            $ persistent._jn_blackjack_explanation_given = True
            jump blackjack_start

        "Thanks, [n_name]. I'll play later.":
            n  "Wow... really? Fine."

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
    #$ jn_utils.fireAndForgetFunction(jn_blackjack._showSplashImage)
    $ jn_blackjack._controls_enabled = False
    $ jn_blackjack._rounds += 1
    $ jnPause(delay=1, hard=True)
    $ chosen_response = ""

    if persistent._jn_blackjack_natsuki_streak in [3, 5, 10]:
        $ natsuki_streak_milestone_map = {
            3: [
                "Oh?{w=0.75} What's this?{w=0.75} Looks like {i}someone's{/i} got the makings of a streak going!",
                "Yes!{w=0.75} That makes three in a row!{w=0.75} Ehehe.",
                "Three wins and counting,{w=0.2} [player]!{w=0.75} Ehehe."
            ],
            5: [
                "Ha!{w=0.75} That makes five in a row now,{w=0.2} [player]!",
                "Yes!{w=0.75} Five in a row!{w=1} Top that,{w=0.2} {i}[player]{/i}.",
                "Aaaand that makes five!{w=0.75} Didn't I {i}say{/i} I was good?"
            ],
            10: [
                "Oh yeah!{w=0.75} Ten!{w=0.75} Now {i}that's{/i} what it means to be a pro,{w=0.2} [player]!",
                "Man...{w=1} ten in a row?{w=0.75} I am on {i}fire{/i} today!{w=0.75} Ehehe.",
                "Ha!{w=0.75} The big ten!{w=0.75} What have you got to say to that,{w=0.2} [player]?"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(natsuki_streak_milestone_map[persistent._jn_blackjack_natsuki_streak]))

    elif persistent._jn_blackjack_player_streak in [3, 5, 10]:
        $ player_streak_milestone_map = {
            3: [
                "L-{w=0.2}lucky break,{w=0.2} [player].{w=0.75} Anyone can luck out three times in a row!",
                "Yeah, yeah.{w=0.75} T-{w=0.2}three in a row is nothing anyway!",
                "B-{w=0.2}bet you can't make that four in a row,{w=0.2} [player]!"
            ],
            5: [
                "Uuuuuu...!{w=0.75} Y-{w=0.2}you can stop getting so lucky now,{w=0.2} [player]!{w=0.75} Jeez...",
                "F-{w=0.2}five in a row now?{w=0.75} Are you kidding me?!",
                "Seriously?{w=0.75} That's five times in a row?!{w=0.75} Ugh..."
            ],
            10: [
                "A-{w=0.2}are you reading my cards or what?!{w=0.75} {i}Ten{/i}?!{w=0.75} Jeez...",
                "Oh{w=0.2},{w=0.75} come {b}on{/b}!{w=0.75} There's no {i}way{/i} you just got ten in a row!{w=0.75} Ugh...",
                "T-{w=0.2}this is just getting ridiculous!{w=0.75} Ten in a row?!{w=0.75} I {i}swear{/i} these cards are rigged..."
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
                "Come on,{w=0.2} [player]...{w=1} you gotta lose some time!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_bust: [
                "I bust?{w=0.75} Are you kidding me?!{w=0.75} Ugh...",
                "Oh,{w=0.2} come on!{w=0.75} I bust {i}again{/i}?!{w=0.75} Yeesh...",
                "Oh,{w=0.2} for-!{w=0.75} {i}Another{/i} bust?!{w=0.75} Seriously...",
                "A-{w=0.2}as {i}if{/i} I bust!{w=0.75} Man...",
                "Are you joking?!{w=0.75} I bust again?!",
                "You have {i}got{/i} to be joking.{w=0.75} Again?!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_blackjack: [
                "Yes!{w=0.5} Yes!{w=0.5} Blackjack!{w=0.75} Ehehe.",
                "Blackjack!{w=0.5} Blackjack!{w=0.5} Ehehe.",
                "Blackjack!{w=0.5} Yes!{w=0.5} Now {i}that's{/i} how it's done!",
                "Yes!{w=0.5} Now {i}that's{/i} more like it!{w=0.75} Ahaha.",
                "Better be taking notes,{w=0.2} [player]!{w=0.75} Ehehe."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_closest: [
                "Yes!{w=0.5} I win!{w=0.3} I win!{w=0.75} Ehehe.",
                "Yes!{w=0.5} I win again!",
                "I was closer!{w=0.5} I win!{w=0.3} I win!",
                "Yes!{w=0.5} Take that,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Oh yeah!{w=0.75} Now {i}that's{/i} more like it!"
            ],
            jn_blackjack.JNBlackjackStates.player_bust: [
                "Pfft-!{w=0.75} Nice bust there,{w=0.2} [player]!{w=0.75} Ehehe.",
                "Yep.{w=0.5} Total misplay,{w=0.2} [player]!",
                "Now that's what I call a bust!{w=0.75} Ehehe.",
                "Ahaha.{w=0.75} Sucks to be you,{w=0.2} [player]!",
                "Pffft!{w=0.75} You {i}sure{/i} you know how to play,{w=0.2} [player]?"
            ],
            jn_blackjack.JNBlackjackStates.player_blackjack: [
                "Seriously?{w=0.75} You got a blackjack?!{w=0.75} Ugh...",
                "Yeah,{w=0.2} yeah.{w=0.75} Enjoy your luck while it lasts,{w=0.2} [player].",
                "Hmph.{w=0.75} You just lucked out this time.",
                "Oh,{w=0.2} come {i}on{/i}!{w=0.75} Again?{w=0.75} Seriously...",
                "N-{w=0.2}now that one was just pure luck!{w=0.75} Ugh..."
            ],
            jn_blackjack.JNBlackjackStates.player_closest: [
                "Heh.{w=0.75} Enjoy the luck while it lasts,{w=0.2} [player].",
                "{i}Seriously{/i}?{w=0.75} Ugh...",
                "Come on!{w=0.75} Really?{w=0.75} Man...",
                "Yeah,{w=0.2} yeah.{w=0.75} Laugh it up,{w=0.2} [player].{w=0.75} Just you wait...",
                "Hmph.{w=1} Lucky break,{w=0.2} [player].{w=0.75} That's all I'm saying."
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
        n  "Eh?{w=0.75}{nw}"
        extend  " You're done playing,{w=0.2} [player]?"
        
        if jn_blackjack._rounds == 0:
            n  "...W-{w=0.2}wait.{w=0.75}{nw}"
            extend  " Hang on just a second here,{w=0.2} [player]!{w=0.75}{nw}"
            extend  " What do you mean?"
            n  "We literally only just started {i}playing{/i}!"
            extend " Jeez..."
            n  "Y-{w=0.2}you better not be pulling my leg again,{w=0.2} [player]."

            $ natsuki_prompt = "Do you actually {i}want{/i} to play blackjack or not?"
            show natsuki option_wait_sulky

        elif jn_blackjack._rounds < 6:
            n  "Man...{w=1}{nw}"
            extend  " really?{w=0.75}{nw}"
            extend  " Come on,{w=0.2} [player]!{w=0.75}{nw}"
            extend  " You can't be done this soon {i}already{/i}."
            n  "Seriously -{w=0.5}{nw}"
            extend  " it's only been like [jn_blackjack._rounds] rounds!{w=0.75}{nw}"
            extend  " We've barely even started!"
            
            $ natsuki_prompt = "You can {i}easily{/i} play at least a couple more games...{w=0.3} right?"
            show natsuki option_wait_sulky

        else:
            n  "..."
            n  "Well...{w=1}{nw}"
            extend  " you have been playing a while.{w=0.75}{nw}"
            extend  " I {i}guess{/i}."
            n  "...Even if you {i}are{/i} calling it quits right in the middle of a game."
            n  "So..."

            $ natsuki_prompt = "You're sure you don't wanna keep playing,{w=0.2} [player]?"
            show natsuki option_wait_curious

    else:
        n  "Oh?{w=0.75}{nw}"
        extend  " What's this,{w=0.2} [player]?{w=0.75}{nw}"
        extend  " Why the cold feet all of a sudden?"
        n  "Ehehe."
        n  "Come on!{w=0.75}{nw}"
        extend  " Don't tell me you're giving up {i}that{/i} easily!"
        
        $ natsuki_prompt = "You can at {i}least{/i} stick it out to the end of this one,{w=0.2} right?"
        show natsuki option_wait_smug
        
    menu:
        n  "[natsuki_prompt]"

        "No, I'm done playing for now.":
            if jn_blackjack._is_player_committed:
                n  "...Man.{w=0.75}{nw}"
                extend  " For real,{w=0.2} [player]?"
                n  "..."
                n  "Well...{w=1}{nw}"
                extend  " I can't say I'm not at least a little disappointed.{w=0.75}{nw}"
                extend  " But I guess that's fine."
                n  "After all..."

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n  "Just means another win for me!{w=0.75}{nw}"

                elif dialogue_choice == 2:
                    n  "As if I'm turning down an easy win!{w=0.75}{nw}"

                else:
                    n  "I'm taking this as a win for me!{w=0.75}{nw}"

                extend  " Ehehe."

            else:
                n  "...Wow.{w=0.75}{nw}"
                extend  " And you didn't even end up making a single move!{w=0.75}{nw}"
                extend  " Huh."
                n  "..."
                n  "Well,{w=0.5}{nw}"
                extend  " looks like {i}you{/i} know what they say at least,{w=0.5}{nw}" 
                extend  " [player]."
                n  "I guess the only winning move for you was not to play!{w=0.75}{nw}"
                extend  " Ehehe."

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
                n  "Y-{w=0.2}yeah!{w=0.75}{nw}"
                extend  " Now that's more like it!{w=0.75}{nw}"
                extend  " Some fighting spirit!"
                n  "Bring it on already,{w=0.2} [player]!"
            
            elif jn_blackjack._rounds == 0:
                n  "Yeah!{w=0.75}{nw}"
                extend  " See?{w=0.75}{nw}"
                extend  " I knew you had some kind of fight left in you!"
                n  "Besides..."
                n  "Only a real sore loser would just chicken out before they've even {i}lost{/i}.{w=0.75}{nw}"
                extend  " Ehehe."
                n  "Prove me wrong,{w=0.2} [player]!"
                
            else:
                n  "Ehehe.{w=0.75}{nw}"
                extend  " Now {i}that's{/i} what I'm talking about!"
                n  "..."
                n  "Well?{w=0.75}{nw}"
                extend  " What're you waiting for?"
                n  "Make your move already,{w=0.2} [player]!"
            
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
