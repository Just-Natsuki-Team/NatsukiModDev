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
    import store.jn_plugins as jn_plugins
    import time

    # In-game tracking
    _controls_enabled = False
    _is_player_turn = None
    _game_state = None

    _natsuki_staying = False
    _player_staying = False
    _natsuki_win_streak = 0

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
        global _controls_enabled
        global _game_state
        _is_player_turn = None
        _controls_enabled = None
        _game_state = None

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
        elif (len(_natsuki_hand) == 4 and len(_natsuki_hand) == 4) or (_player_staying and _natsuki_staying):
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
            _showSplashImage()

        global _natsuki_win_streak

        if natsuki_wins:
            store.persistent._jn_blackjack_natsuki_wins += 1
            _natsuki_win_streak += 1

        if player_wins:
            store.persistent._jn_blackjack_player_wins += 1
            _natsuki_win_streak = 0

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
            JNBlackjackStates.draw: "draw",
        }
        if _game_state in image_state_map:
            global _splash_sprite
            _splash_sprite = image_state_map[_game_state]
            renpy.show(name="blackjack_splash", zorder=10, layer="overlay")

        return

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the blackjack UI.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _game_state == JNBlackjackStates.draw:
            return "Draw!"

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
            return "You lost!"

        if _is_player_turn is None:
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
            return _player_hand[index][0] if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"

        else:
            if _game_state is None and index == 0:
                return "mod_assets/games/cards/hide.png"
            
            return _natsuki_hand[index][0] if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"

    # TODO: Remove this!
    jn_plugins.registerExtrasOption(
        option_name="Blackjack Test",
        visible_if="store.persistent._jn_blackjack_unlocked",
        jump_label="blackjack_intro"
    )

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
    if jn_blackjack._game_state is not None:
        jump blackjack_end

    # Natsuki's hit/stay logic
    elif not jn_blackjack._is_player_turn:
        $ jn_blackjack._controls_enabled = False
        $ natsuki_hand_sum = jn_blackjack._getHandSum(is_player=False)

        if natsuki_hand_sum == 20 or len(jn_blackjack._natsuki_hand) == 4:
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

                risk_percent = jn_blackjack._natsuki_win_streak / 100 if jn_blackjack._natsuki_win_streak > 0 else 0
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
    $ jnPause(delay=3, hard=True)

    if persistent._jn_blackjack_quick_mode:
        # Quick mode is restricted to a single line response before play continues, without hiding any UI
        $ response_map = {
            JNBlackjackStates.draw: {
                "We drew? Huh.",
                "Huh. We drew? Weird.",
                "Wait, we tied? Huh.",
                "A tie? Weird."
            },
            JNBlackjackStates.natsuki_bust: {
                "I bust? Are you kidding me?! Ugh...",
                "Oh, come on! I bust {i}again{/i}?! Yeesh...",
                "Oh, for-! {i}Another{/i} bust?!",
                "A-as {i}if{/i} I bust! Man..."
            },
            JNBlackjackStates.natsuki_blackjack: {
                "Yes! Yes! Blackjack! Ehehe.",
                "Blackjack! Blackjack! Ehehe.",
                "Blackjack! Yes! Now {i}that's{/i} how it's done!",
                "Yes! Now {i}that's{/i} more like it! Ahaha."
            },
            JNBlackjackStates.natsuki_closest: {
                "Yes! I win! I win! Ehehe.",
                "Yes! I win again!",
                "I was closer! I win! I win!",
                "Yes! Take that, [player]! Ehehe."
            },
            JNBlackjackStates.player_bust: {
                "Pfft-! Nice bust there, [player]!",
                "Yep. Total misplay, [player]!",
                "Now that's what I call a bust! Ehehe.",
                "Ahaha. Sucks to be you, [player]!"  
            },
            JNBlackjackStates.player_blackjack: {
                "Seriously? You got a blackjack?! Ugh...",
                "Yeah, yeah. Enjoy your luck while it lasts, [player].",
                "Hmph. You just lucked out this time.",
                "Oh, come {i}on{/i}! Again? Seriously..."
            },
            JNBlackjackStates.player_closest: {
                "Heh. Enjoy the luck while it lasts, [player].",
                "{i}Seriously{/i}? Ugh...",
                "Come on! Really? Man...",
                "Yeah, yeah. Laugh it up, [player]. Just you wait..."
            },
        }
        $ chosen_response = renpy.substitute(random.choice(response_map[jn_blackjack._game_state]))
        n "[chosen_response]"

        $ jnPause(1)
        jump blackjack_start

    else:
        # Standard dialogue flow
        $ dialogue_choice = random.randint(1, 3)
        $ rematch_prompt = ""
        hide screen blackjack_ui

        if jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.draw:
            if dialogue_choice == 1:
                n "...Huh."
                extend " We drew?"
                extend " Weird."
                n "Well, anyway -"
                extend " not like it really matters."
                extend " A-as if I plan on tying next time!"

            elif dialogue_choice == 2:
                n "Eh?"
                extend " We drew?"
                extend " How did that happen?"
                n "Well, whatever."
                extend " Y-you can't luck out of losing forever, [player]!"

            else:
                n "What?"
                extend " We actually drew?"
                extend " Man..."
                n "Admit it, [player] -"
                extend " I totally had you on the ropes!"

            n "Come on, [player]!"
            extend " We're {i}totally{/i} doing this again!"

            $ rematch_prompt = renpy.substitute(random.choice({
                "Rematch! Rematch!",
                "Come on! Rematch!",
                "Rematch!",
                "We're doing a rematch!"
            }))
            show natsuki option_wait_sulky

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.natsuki_bust:
            if dialogue_choice == 1:
                n "Uuuuuuu-!"
                extend " A-as if I bust!"
                extend " Come on..."
                n "..."

            elif dialogue_choice == 2:
                n "Oh,"
                extend " come"
                extend " {i}on{/i}!"
                n "Ugh..."
                extend " I {i}knew{/i} it was a crappy hand..."

            else:
                n "Yeah, yeah."
                extend " I get it."
                extend " I bust."
                n "Yeesh..."

            n "W-wipe that smile off your face already!"
            extend " There's no way I'm taking this lying down!"

            $ rematch_prompt = renpy.substitute(random.choice({
                "I-I demand a rematch!",
                "We're rematching!",
                "We're totally having a rematch!",
                "Rematch! Now!"
            }))
            show natsuki option_wait_sulky

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.natsuki_blackjack:
            if dialogue_choice == 1:
                n "Yes!"
                extend " Blackjack! Blackjack!"
                extend " Ehehe."
                n "See, [player]?"
                extend " Now {i}that's{/i} how it's done!"

            elif dialogue_choice == 2:
                n "Aha!"
                extend " Blackjack! Blackjack!"
                extend " Yes!"
                n "Ehehe."
                n "Now that's what I call some professional plays!"

            else:
                n "Blackjack! Blackjack!"
                extend " Yes!"
                n "Well, what can I say?"
                extend " Guess it just comes to me naturally!"
                extend " Ahaha."

            n "Well, [player]?"
            extend " What do you say?"

            $ rematch_prompt = renpy.substitute(random.choice([
                "Ready to challenge the master again?",
                "Think you can take on a real pro?",
                "Betcha I can pull that off again!",
                "Feeling lucky this time, [player]?"
            ]))
            show natsuki option_wait_smug

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.natsuki_closest:
            n 1nchgnl "Yes! I win! I win!"

            if dialogue_choice == 1:
                n "Yes! Yes!"
                extend " I win! I win!"
                n "Ahaha."
                n "Sorry, [player] -"
                extend " that's just the luck of the draw for you!"

            elif dialogue_choice == 2:
                n "Ha!"
                extend " Yes!"
                extend " I win again!"
                n "Don't worry, [player]."
                extend " That's just what you have to expect!"

            else:
                n "Ehehe."
                extend " Tough luck, [player]."
                extend " Looks like this one belongs to [n_name]!"

            n "So..."

            $ rematch_prompt = renpy.substitute(random.choice([
                "Wanna try your luck again, [player]?",
                "Think you can win this time, [player]?",
                "Finished blaming the cards? You wanna try again?",
                "Feeling lucky this time, [player]?"
            ]))
            show natsuki option_wait_smug

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.player_bust:
            if dialogue_choice == 1:
                n "Ha!"
                extend " I knew it!"
                extend " You sure bust that one, [player]!"

            elif dialogue_choice == 2:
                n "Ehehe."
                extend " What can I say, [player]?"
                extend " Total misplay!"

            else:
                n "Yep!"
                extend " Just as I expected."
                extend " Bust wide open!"

            b "..."
            n "Well?"

            $ rematch_prompt = renpy.substitute(random.choice([
                "Wanna try your luck again, [player]?",
                "Think you can win this time, [player]?",
                "Finished blaming the cards? You wanna try again?",
                "Feeling lucky this time, [player]?"
            ]))
            show natsuki option_wait_smug

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.player_blackjack:
            n 1cslpo "Uuuuu...! Are you kidding me?! You got a blackjack? Man..."

            if dialogue_choice == 1:
                n "Uuuuu...!"
                n "Are you kidding me?"
                extend " You got a blackjack?"
                extend " Man..."

            elif dialogue_choice == 2:
                n ""

            else:
                n ""

            $ rematch_prompt = renpy.substitute(random.choice([
                "Wanna try your luck again, [player]?",
                "Think you can win this time, [player]?",
                "Finished blaming the cards? You wanna try again?",
                "Feeling lucky this time, [player]?"
            ]))
            show natsuki option_wait_sulky

        elif jn_blackjack._game_state == jn_blackjack.JNBlackjackStates.player_closest:
            n 1ccspo "Hmph. You just got lucky again, [player]."

            if dialogue_choice == 1:
                pass

            elif dialogue_choice == 2:
                pass

            else:
                pass

            $ rematch_prompt = renpy.substitute(random.choice([
                "Wanna try your luck again, [player]?",
                "Think you can win this time, [player]?",
                "Finished blaming the cards? You wanna try again?",
                "Feeling lucky this time, [player]?"
            ]))
            show natsuki option_wait_sulky

        menu:
            n "[rematch_prompt]"

            "You're on!":
                n "You bet!"

                jump blackjack_start

            "I'll pass.":
                n "Thanks for playing!"

                hide screen blackjack_ui
                $ Natsuki.setInGame(False)
                $ Natsuki.resetLastTopicCall()
                $ Natsuki.resetLastIdleCall()
                $ HKBShowButtons()
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

            $ jn_blackjack._game_state = jn_blackjack.JNBlackjackStates.forfeit
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

transform blackjack_popup:
    easeout 0.75 alpha 0

image blackjack_splash:
    "mod_assets/games/blackjack/[jn_blackjack._splash_sprite].png"
    ease 0.33 alpha 1.0 yoffset -30
    blackjack_popup

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
            spacing 10

            text "Your wins: {0}".format(persistent._jn_blackjack_player_wins) style "blackjack_note_text"
            text "[n_name]'s wins: {0}".format(persistent._jn_blackjack_natsuki_wins) style "blackjack_note_text"
            text "Turn: {0}".format(jn_blackjack._getCurrentTurnLabel()) style "blackjack_note_text"

        null height 120

        # Controls
        style_prefix "hkb"
        
        # Hit
        key "1" action [
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 4, Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        textbutton _("Hit!"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, True),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 4)]

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
