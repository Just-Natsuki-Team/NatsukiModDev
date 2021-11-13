default persistent.jn_snap_explanation_given = False

init 0 python in snap:
    import random
    import store

    # Card config
    _card_values = range(1, 11)
    _card_suits = [
        "Hearts", # Sayori
        "Spades", # Yuri
        "Clubs", # Natsuki
        "Diamonds" # Monika
    ]

    # Quips
    _player_correct_snap_quips = [
        "Nnnnn-!",
        "Ugh!{w=0.2} Come on!",
        "You're fast!",
        "But I was just about to call ittt!",
        "Just you wait,{w=0.1} [player]..."
        "Uuuuuu-!"
    ]

    _natsuki_correct_snap_quips = [
        "SNAP!{w=0.2} Aha!",
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
    ]

    _player_wrong_snap_quips = [
        "Oh?{w=0.2} Someone's impatient,{w=0.1} huh?",
        "Oopsie daisy,{w=0.1} [player]~.{w=0.2} Ehehe.",
        "Nice one,{w=0.1} dummy.{w=0.2} Ahaha!",
        "Real smooth,{w=0.1} [player].{w=0.2} Ehehe.",
        "Ahaha!{w=0.2} What was that,{w=0.1} [player]?",
        "Hey,{w=0.1} [player] -{w=0.1} you're meant to read the cards!{w=0.2} Ehehe."
    ]

    _natsuki_wrong_snap_quips = [
        "Sn-...{w=0.3} oh.",
        "Snap!{w=0.2} Wait...",
        "SNAP!{w=0.2} Wait...",
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
    _is_player_turn = False
    _player_forfeit = False
    _natsuki_skill_level = 1

    # Collections of cards involved in the game
    _cards_in_deck = []
    _cards_on_table = []
    _natsuki_hand = []
    _player_hand = []

    # A little something extra
    if random.choice(range(1, 100)) == 1:
        _card_fan_image = "mod_assets/games/snap/ui/card_fan_dual_alt_a.png"

    elif random.choice(range(1, 100)) == 99:
        _card_fan_image = "mod_assets/games/snap/ui/card_fan_dual_alt_b.png"

    else:
        _card_fan_image = "mod_assets/games/snap/ui/card_fan_dual.png"

    def _reset(complete_reset=False):
        """
        Resets the in-game variables associated with Snap

        IN:
            - true_reset - boolean flag; if True will also reset Natsuki's skill level, etc.
        """
        _is_player_turn = False
        _player_forfeit = False

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
        for card_suit in _card_values:
            for card_value in _card_suits:
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
                new_card = _player_hand.pop()
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.mp3")
                _is_player_turn = False

        else:
            if (len(_natsuki_hand) > 0):
                new_card = _natsuki_hand.pop()
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.mp3")

    def _get_card_to_display():
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
        if len(_cards_on_table) > 1:
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

        # If the suit/value on the last placed card matches the preceding card, the snap is valid
        if len(_cards_on_table) >= 2:

            if _get_snap_result():

                if is_player:
                    # Player called snap successfully; give them the cards on the table
                    for card in _cards_on_table:
                        _player_hand.append(card)

                    renpy.say(store.n, renpy.substitute(random.choice(_player_correct_snap_quips)))

                else:
                    # Natsuki called snap successfully; give her the cards on the table
                    for card in _cards_on_table:
                        _natsuki_hand.append(card)

                    renpy.say(store.n, renpy.substitute(random.choice(_natsuki_correct_snap_quips)))

                del _cards_on_table[:]
                renpy.play("mod_assets/sfx/card_shuffle.mp3")

        else:
            # Natsuki taunts the player for a bad snap
            if is_player:
                renpy.say(store.n, renpy.substitute(random.choice(_player_wrong_snap_quips)))

            # Natsuki is frustrated at herself for a bad snap
            else:
                renpy.say(store.n, renpy.substitute(random.choice(_natsuki_wrong_snap_quips)))

        # Finally switch turns
        _is_player_turn = not _is_player_turn

label snap_intro:
    n "Alriiiight!{w=0.2} Let's play some Snap!"
    if not persistent.jn_snap_explanation_given:
        n "Oh -{w=0.1} before we start,{w=0.1} did you want an explanation?{w=0.2} You know,{w=0.1} on how it works?"
        n "It's a super simple game,{w=0.1} but I thought I'd better ask."
        n "I don't wanna win just because you didn't know what you were doing!"
        n "So..."
        n "How about it?" 
        menu:
            n "Want me to run through the rules real quick?"

            "Yes please!":
                jump snap_explanation

            "No,{w=0.1} I'm ready.":
                n "Oh?{w=0.2} You're ready,{w=0.1} huh?"
                n "Ready to get your butt kicked!{w=0.2} Let's go,{w=0.1} [player]!"
                
    jump snap_start

label snap_explanation:
    n "Alright!{w=0.2} So the rules are dead simple,{w=0.1} like I was saying."
    n "Basically,{w=0.1} we each get half a deck of cards."
    n "Then,{w=0.1} we take it in turns placing a card face up on the table -{w=0.1} we don't get to {i}pick or see{/i} the card before,{w=0.1} though!"
    n "Following me so far,{w=0.1} [player]?{w=0.2} Ehehe."
    n "If the card just placed down on the table matches either the {i}value or suit{/i} of the card that was there before..."
    n "Then we gotta call Snap!"
    n "Whoever calls it first gets the cards on the table."
    n "The winner is whoever ends up with all the cards first!"
    n "Which will clearly be me,{w=0.1} obviously.{w=0.2} Ahaha."
    n "So...{w=0.3} how about it,{w=0.1} [player]?{w=0.2} You got all that?"
    menu:
        n "Do the rules all make sense to you?"
        "Could you go over them again,{w=0.1} please?":
            n "Huh?{w=0.2} Well,{w=0.1} okay..."
            jump snap_explanation

        "Got it.{w=0.2} Let's play!":
            n "That's what I'm talking about!{w=0.2} Some fighting spirit!"
            n "I should warn you though,{w=0.1} [player]..."
            n "I'm not gonna hold back!{w=0.2} Let's do this!"
            $ persistent.jn_snap_explanation_given = True
            jump snap_start

label snap_start:
    play audio card_shuffle
    n "..."
    $ snap._reset()
    $ snap._generate_hands()
    show player_natsuki_hands zorder 20
    show screen snap_ui
    $ utils.log("player's hand: {0}".format(str(snap._player_hand)))
    $ utils.log("natsuki's hand: {0}".format(str(snap._natsuki_hand)))
    n "Okaaay!{w=0.2} That's the deck shuffled!"
    n "I'm just gonna flip a coin to see who goes first.{w=0.2} No peeking,{w=0.1} [player]!"
    play audio coin_flip
    n "..."
    $ snap._is_player_turn = random.choice([True, False])

    if snap._is_player_turn:
        n "Ehehe.{w=0.2} Bad luck,{w=0.1} [player].{w=0.2} Looks like you're up first!"
        
    else:
        n "Hmph...{w=0.3} you got lucky this time.{w=0.2} Looks like I'm first,{w=0.1} [player]."
        n "N-{w=0.1}not like that changes anything!" 
        n "I'm still {i}totally{/i} gonna win,{w=0.1} of course."

    jump snap_main_loop

label snap_main_loop:
    $ global _is_player_turn
    # First, let's check to see if anyone has won yet
    if len(snap._cards_on_table) == 0:

        if len(snap._player_hand) == 0 and len(snap._natsuki_hand) == 0:
            # We tied somehow? End the game
            $ snap._player_win_streak = 0
            $ snap._natsuki_win_streak = 0
            $ snap.last_game_result = snap.RESULT_DRAW
            jump snap_end

        if len(snap._player_hand) == 0:
            # Player has lost; end the game
            $ snap._player_win_streak = 0
            $ snap._natsuki_win_streak += 1
            $ snap.last_game_result = snap.RESULT_NATSUKI_WIN
            jump snap_end
            
        elif len(snap._natsuki_hand) == 0:
            # Natsuki has lost; end the game
            $ snap._player_win_streak += 1
            $ snap._natsuki_win_streak = 0
            $ snap.last_game_result = snap.RESULT_PLAYER_WIN
            jump snap_end

    elif snap._player_forfeit:
        # Player gave up
        $ snap._player_win_streak = 0
        $ snap.last_game_result = snap.RESULT_FORFEIT
        jump snap_end

    if not snap._is_player_turn:
        # Natsuki gets to place a card
        $ snap._place_card_on_table(False)
        $ snap._is_player_turn = True

    $ renpy.pause(delay=3.0)

    # Natsuki's snap logic
    if (snap._get_snap_result()):
        # If a correct snap is possible, Natsuki will try to call it.
        # The higher the difficulty, the quicker Natsuki will be.
        $ snap._call_snap()
        pass

    else:
        # If a snap isn't possible, Natsuki may snap by mistake.
        # The lower the difficulty, the more frequently Natsuki will mess up.
        pass

    jump snap_main_loop

label snap_end:
    # Player won,{w=0.1} Natsuki amger
    if snap.last_game_result == snap.RESULT_PLAYER_WIN:
        if snap._player_win_streak >= 10:
            n "Nnnnnnnnnn-!!"
            n "W-what even is this,{w=0.1} [player]?"
            n "How are you so good at this?!"
            n "Ugh..."

        elif snap._player_win_streak >= 5:
            n "Okay!{w=0.2} Alright!{w=0.2} I get it!"
            n "You're good at Snap,{w=0.1} okay?!"
            n "Jeez..."
            n "Now...{w=0.3} how about letting up a little?"
            n "Ehehe..."

        elif snap._player_win_streak >= 3:
            n "Oho!{w=0.2} Someone's been practicing,{w=0.1} huh?"
            n "Or maybe you're just on a lucky streak,{w=0.1} [player]."

        else:
            n "Well,{w=0.1} heck.{w=0.2} I guess that's it,{w=0.1} huh?"
            n "Well played though,{w=0.1} [player]!"

    # Natsuki won,{w=0.1} Natsuki happ
    elif snap.last_game_result == snap.RESULT_NATSUKI_WIN:
        if snap._natsuki_win_streak >= 10:
            n "Jeez,{w=0.1} [player]...{w=0.3} are you having a bad day or what?"
            n "Ahaha!"
            n "So long as you're having fun though,{w=0.1} right?"

        elif snap._natsuki_win_streak >= 5:
            n "Oh?{w=0.2} This?{w=0.2} This skill?"
            n "Don't worry about it."
            n "It's all natural,{w=0.1} [player]~."
            n "What did you expect,{w=0.1} challenging a pro like that?" 
            n "Ehehe."

        elif snap._natsuki_win_streak >= 3:
            n "Yes!{w=0.2} I win again!"
            n "Ehehe."
            
        else:
            n "I won!{w=0.2} I won!"
            n "Just as predicted,{w=0.1} right?{w=0.2} Ahaha."

    # What
    elif snap.last_game_result == snap.RESULT_DRAW:
        n "...Huh.{w=0.2} We actually tied?"
        n "That's...{w=0.3} almost impressive,{w=0.1} actually.{w=0.2} Weird."
        n "Well,{w=0.1} whatever,{w=0.1} I guess!"

    else:
        # Assume forfeit
        n "Oh?{w=0.2} You're giving up?"
        n "Well,{w=0.1} I guess that's fine.{w=0.2} Let me just chalk up another win for me,{w=0.1} then.{w=0.2} Ehehe."

    n "So..." 
    menu:
        n "How 'bout another game?"

        "You're on!":
            n "Yeah,{w=0.1} you bet you are,{w=0.1} [player]!"
            jump snap_start

        "I'll pass.":
            n "Awww...{w=0.3} well,{w=0.1} okay."
            n "Thanks for playing,{w=0.1} [player]~."
            hide player_natsuki_hands
            hide screen snap_ui
            jump ch30_loop

image player_natsuki_hands:  
    pos (100, 215)
    snap._card_fan_image

screen snap_ui:
    zorder 20
    text "[player]'s hand: {0}".format(len(snap._player_hand)) size 22 xpos 175 ypos 55 style "categorized_menu_button"
    text "[n_name]'s hand: {0}".format(len(snap._natsuki_hand)) size 22 xpos 175 ypos 170 style "categorized_menu_button"
    text "Current card: {0}".format(snap._get_card_to_display()) size 22 xpos 175 ypos 425 style "categorized_menu_button"

    style_prefix "hkb"

    vbox:
        xpos 100
        ypos 230
    
        # Place card, but only selectable if player's turn
        textbutton _("Place"):
            style "hkbd_button"
            action [ Function(snap._place_card_on_table, True), SensitiveIf(snap._is_player_turn) ]

        # Forfeit, but only selectable if player's turn
        textbutton _("Forfeit"):
            style "hkbd_button"
            action [ SetField(snap, "_player_forfeit", True), SensitiveIf(snap._is_player_turn) ]

        # Snap, but only selectable if there's enough cards down on the table
        textbutton _("Snap!"):
            style "hkbd_button"
            action [ Function(snap._call_snap, True), SensitiveIf(len(snap._cards_on_table) >= 2) ]
