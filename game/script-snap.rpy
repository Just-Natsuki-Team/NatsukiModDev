default persistent.jn_snap_explanation_given = False

init 0 python in jn_snap:
    import random
    import store

    # Card config
    _card_values = range(1, 11)
    _card_suits = [
        "clubs",
        "diamonds",
        "hearts",
        "spades"
    ]

    _current_table_card_image = "mod_assets/games/snap/cards/blank.png"
    _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_none.png"

    _SNAP_Z_INDEX = 4

    # Quips
    _player_correct_snap_quips = [
        "Nnnnn-!",
        "Ugh!{w=0.2} Come on!",
        "Y-{w=0.1}You're fast!",
        "But I was just about to call ittt!",
        "Just you wait,{w=0.1} [player]...",
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

    _natsuki_correct_snap_quips = [
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

    _player_incorrect_snap_quips = [
        "Oh?{w=0.2} Someone's impatient,{w=0.1} huh?",
        "Oopsie daisy,{w=0.1} [player]~.{w=0.2} Ehehe.",
        "Nice one,{w=0.1} dummy.{w=0.2} Ahaha!",
        "Real smooth,{w=0.1} [player].{w=0.2} Ehehe.",
        "Ahaha!{w=0.2} What was that,{w=0.1} [player]?",
        "Hey,{w=0.1} [player] -{w=0.1} you're meant to read the cards!{w=0.2} Ehehe.",
        "Great play,{w=0.1} dummy!{w=0.2} Ahaha!"
    ]

    _natsuki_incorrect_snap_quips = [
        "Sn-...{w=0.3} oh.",
        "Snap!{w=0.2} Wait...",
        "SNAP!{w=0.2} Huh...?{w=0.2} O-{w=0.1}oh.",
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
        _card_fan_image_player = "mod_assets/games/snap/ui/card_fan_icon_alt.png"

    else:
        _card_fan_image_player = "mod_assets/games/snap/ui/card_fan_icon.png"

    _card_fan_image_natsuki = "mod_assets/games/snap/ui/card_fan_icon.png"

    def _reset(complete_reset=False):
        """
        Resets the in-game variables associated with Snap

        IN:
            - true_reset - boolean flag; if True will also reset Natsuki's skill level, etc.
        """
        _is_player_turn = None
        _player_forfeit = False
        _player_is_snapping = False
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
        for card_suit in _card_suits:
            for card_value in _card_values:
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
            renpy.play("mod_assets/sfx/card_shuffle.mp3")

            draw_card_onscreen()

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
            _current_table_card_image = "mod_assets/games/snap/cards/{0}/{1}.png".format(_cards_on_table[-1][0], _cards_on_table[-1][1])
            
        else:
            _current_table_card_image = "mod_assets/games/snap/cards/blank.png"

        renpy.show(name="current_table_card", zorder=_SNAP_Z_INDEX)

    def update_turn_indicator():
        """
        Updates the turn indicator graphic to display who's turn it is to move
        """
        global _turn_indicator_image

        if _is_player_turn is None:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_none.png"

        elif _is_player_turn:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_player.png"

        else:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_natsuki.png"

        renpy.show(name="turn_indicator_icon", zorder=_SNAP_Z_INDEX)

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
    n "Alright!{w=0.2} So the rules are dead simple,{w=0.1} like I was saying before."
    n "Basically,{w=0.1} we each get half a deck of cards."
    n "Then,{w=0.1} we take it in turns placing a card face up on the table -{w=0.1} we don't get to {i}pick or see{/i} the card before,{w=0.1} though!"
    n "Following me so far,{w=0.1} [player]?{w=0.2} Ehehe."
    n "If the card just placed down on the table matches either the {i}value or suit{/i} of the card that was there before..."
    n "Then we gotta call Snap!"
    n "Whoever calls it first gets the cards on the table."
    n "Oh -{w=0.1} but you gotta be careful,{w=0.2} [player]."
    n "When you call snap,{w=0.2} it becomes the other player's turn..."
    n "So don't shout unless you know you got it,{w=0.1} 'kay?"
    n "The winner is whoever ends up with all the cards first!"
    n "Which is usually me,{w=0.1} obviously."
    n "You also lose if you run out of cards to play,{w=0.1} so you should keep that in mind too."
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

        "Thanks, [n_name]. I'll play later.":
            n "Ehehe.{w=0.2} No worries,{w=0.1} [player]!"
            jump ch30_loop

label snap_start:
    # Reset everything ready for a fresh game
    play audio card_shuffle
    n "..."
    $ jn_snap._reset()
    $ jn_snap._generate_hands()

    # Reset the UI
    $ jn_placeholders.show_resting_placeholder_natsuki(True)
    $ jn_snap.draw_card_onscreen()
    $ jn_snap.update_turn_indicator()

    show player_hand_icon zorder jn_snap._SNAP_Z_INDEX
    show natsuki_hand_icon zorder jn_snap._SNAP_Z_INDEX
    show turn_indicator_icon zorder jn_snap._SNAP_Z_INDEX
    show screen snap_ui

    n "Okaaay!{w=0.2} That's the deck shuffled!"
    n "Let's see who's going first..."

    play audio coin_flip
    n "..."
    $ jn_snap._is_player_turn = random.choice([True, False])
    $ jn_snap.update_turn_indicator()

    if jn_snap._is_player_turn:
        n "Ehehe.{w=0.2} Bad luck,{w=0.1} [player].{w=0.2} Looks like you're up first!"
        
    else:
        n "Hmph...{w=0.3} you got lucky this time.{w=0.2} Looks like I'm first,{w=0.1} [player]."

    $ jn_globals.player_is_ingame = True
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
        $ jn_snap.last_game_result = jn_snap.RESULT_NATSUKI_WIN
        jump snap_end

    elif len(jn_snap._natsuki_hand) == 0:
        # Natsuki has lost; end the game
        $ jn_snap._player_win_streak += 1
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_PLAYER_WIN
        jump snap_end

    $ renpy.pause(delay=max(0.25, (3.0 - jn_snap._natsuki_skill_level * 0.25)))

    # Natsuki's snap logic

    # If a correct snap is possible, and the player isn't snapping already, Natsuki will try to call it: the higher the difficulty, the quicker Natsuki will be.
    if not jn_snap._player_is_snapping:
        if (jn_snap._get_snap_result()):  
            $ jn_snap._call_snap()

        # She may also snap by mistake, assuming it makes sense to do so: the higher the difficulty, the less she'll accidentally jn_snap.
        elif random.choice(range(0,10 + jn_snap._natsuki_skill_level)) == 1 and len(jn_snap._cards_on_table) >= 2 and jn_snap._natsuki_can_fake_snap:
            $ jn_snap._call_snap()
            $ jn_snap._natsuki_can_fake_snap = False

    if not jn_snap._is_player_turn:
        # Natsuki gets to place a card
        $ jn_snap._place_card_on_table(False)
        $ jn_snap._is_player_turn = True
        $ jn_snap._natsuki_can_fake_snap = True

    jump snap_main_loop

label snap_quip(is_player_snap, is_correct_snap):
    
    # Generate the quip based on what just happened
    if is_player_snap:
        
        # Player snapped, and was correct
        if is_correct_snap:
            $ quip = renpy.substitute(random.choice(jn_snap._player_correct_snap_quips))
            show placeholder_natsuki plead zorder jn_placeholders.NATSUKI_Z_INDEX

        # Player snapped, and was incorrect
        else:
            $ quip = renpy.substitute(random.choice(jn_snap._player_incorrect_snap_quips))
            show placeholder_natsuki smug zorder jn_placeholders.NATSUKI_Z_INDEX

    else:

        # Natsuki snapped, and was correct
        if is_correct_snap:
            $ quip = renpy.substitute(random.choice(jn_snap._natsuki_correct_snap_quips))
            show placeholder_natsuki smile zorder jn_placeholders.NATSUKI_Z_INDEX

        # Natsuki snapped, and was incorrect
        else:
            $ quip = renpy.substitute(random.choice(jn_snap._natsuki_incorrect_snap_quips))
            show placeholder_natsuki unamused zorder jn_placeholders.NATSUKI_Z_INDEX

    # Natsuki quips; disable controls so player can't skip dialogue
    $ jn_snap._controls_enabled = False
    n "[quip]"
    $ jn_placeholders.show_resting_placeholder_natsuki(True)
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

    $ jn_snap._controls_enabled = False

    # Player won, Natsuki amger
    if jn_snap.last_game_result == jn_snap.RESULT_PLAYER_WIN:

        if jn_snap._player_win_streak > 10:
            n "Yeah,{w=0.1} yeah.{w=0.2} You won again."
            n "...Nerd.{w=0.2} Ehehe."

        elif jn_snap._player_win_streak == 10:
            n "Nnnnnnnnnn-!!"
            n "W-what even is this,{w=0.1} [player]?"
            n "How are you so good at this?!"
            n "Ugh..."

        elif jn_snap._player_win_streak == 5:
            n "Okay!{w=0.2} Alright!{w=0.2} I get it!"
            n "You're good at Snap,{w=0.1} okay?!"
            n "Jeez..."
            n "Now...{w=0.3} how about letting up a little?"
            n "Ehehe..."

        elif jn_snap._player_win_streak == 3:
            n "Oho!{w=0.2} Someone's been practicing,{w=0.1} huh?"
            n "Or maybe you're just on a lucky streak,{w=0.1} [player]."

        else:
            n "Well,{w=0.1} heck.{w=0.2} I guess that's it,{w=0.1} huh?"
            n "Well played though,{w=0.1} [player]!"

    # Natsuki won, Natsuki happ
    elif jn_snap.last_game_result == jn_snap.RESULT_NATSUKI_WIN:

        if jn_snap._natsuki_win_streak > 10:
            n "Man,{w=0.1} this is just too easy!{w=0.2} I almost feel bad..."
            n "...Almost.{w=0.2} Ehehe."

        if jn_snap._natsuki_win_streak == 10:
            n "Jeez,{w=0.1} [player]...{w=0.3} are you having a bad day or what?"
            n "Ahaha!"
            n "So long as you're having fun though,{w=0.1} right?"

        elif jn_snap._natsuki_win_streak == 5:
            n "Oh?{w=0.2} This?{w=0.2} This skill?"
            n "Don't worry about it."
            n "It's all natural,{w=0.1} [player]~."
            n "What did you expect,{w=0.1} challenging a pro like that?" 
            n "Ehehe."

        elif jn_snap._natsuki_win_streak == 3:
            n "Yes!{w=0.2} I win again!"
            n "Ehehe."
            
        else:
            n "I won!{w=0.2} I won! Yesss!"
            n "Just as predicted,{w=0.1} right?{w=0.2} Ahaha."

    # What
    elif jn_snap.last_game_result == jn_snap.RESULT_DRAW:
        n "...Huh.{w=0.2} We actually tied?"
        n "That's...{w=0.3} almost impressive,{w=0.1} actually.{w=0.2} Weird."
        n "Well,{w=0.1} whatever,{w=0.1} I guess!"

    else:
        # Assume forfeit
        n "Oh?{w=0.2} You're giving up?"
        n "Well,{w=0.1} I guess that's fine.{w=0.2} Let me just chalk up another win for me,{w=0.1} then.{w=0.2} Ehehe."

    # Award affinity for playing to completion with best girl
    $ relationship("affinity+")

    if jn_snap._player_win_streak >= 3:
        n "Uuuuuu-!"
        n "I-{w=0.1}I demand a rematch!{w=0.2} I'm not going down like this!"
 
    elif jn_snap._natsuki_win_streak >= 3:
        n "Ehehe.{w=0.2} That can't be {i}all{/i} you've got,{w=0.1} [player].{w=0.2} Rematch!"

    else:
        n "So..." 

    menu:
        n "Let's play again!"

        "You're on!":
            n "Yeah,{w=0.1} you bet you are,{w=0.1} [player]!"
            $ jn_snap._natsuki_skill_level += 1
            jump snap_start

        "I'll pass.":
            n "Awww...{w=0.3} well,{w=0.1} okay."
            n "Thanks for playing,{w=0.1} [player]~."

            if jn_snap._player_win_streak >= 3:
                n "...Even if you did kick my butt."

            elif jn_snap._natsuki_win_streak >= 3:
                n "I wanna see more fight in you next time, though. Ahaha!"

            # Hide all the UI
            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer 
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ jn_globals.player_is_ingame = False
            jump ch30_loop

label snap_forfeit:
    $ jn_snap._controls_enabled = False
    n "Awww...{w=0.3} you're not giving up already are you,{w=0.1} [player]?"
    menu:
        n "...Are you?"

        "Yes, I give up.":
            n "Oh...{w=0.3} well,{w=0.1} okay."
            n "But just so you know..."
            n "I'm chalking this up as a win for me!{w=0.2} Ehehe."

            # Hit the streaks
            $ jn_snap._player_win_streak = 0
            $ jn_snap._natsuki_win_streak += 1

            # Hide all the UI
            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer 
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ jn_globals.player_is_ingame = False
            jump ch30_loop

        "In your dreams!":
            n "Pffffft!{w=0.2} Oh really?"
            n "Game on then,{w=0.1} [player]!"
            $ jn_snap._controls_enabled = True
            $ jn_snap._natsuki_skill_level += 1
            jump snap_main_loop

# This is the card currently on the top of the pile being shown
image current_table_card:
    anchor(0, 0)
    pos(1000, 100)
    jn_snap._current_table_card_image

# Icons representing each player's hand
image player_hand_icon:
    anchor(0,0)  
    pos (675, 110)
    jn_snap._card_fan_image_player

image natsuki_hand_icon:
    anchor(0,0)  
    pos (675, 180)
    jn_snap._card_fan_image_natsuki

# Icon representing who's turn it is
image turn_indicator_icon:
    anchor(0,0)
    pos(675, 250)
    jn_snap._turn_indicator_image

# Game UI
screen snap_ui:
    zorder jn_snap._SNAP_Z_INDEX

    # Game information
    text "Cards down: {0}".format(len(jn_snap._cards_on_table)) size 22 xpos 1000 ypos 50 style "categorized_menu_button"
    text "[player]'s hand: {0}".format(len(jn_snap._player_hand)) size 22 xpos 750 ypos 125 style "categorized_menu_button"
    text "[n_name]'s hand: {0}".format(len(jn_snap._natsuki_hand)) size 22 xpos 750 ypos 195 style "categorized_menu_button"
    text "Turn: {0}".format(jn_snap.get_turn_label_to_display()) size 22 xpos 750 ypos 265 style "categorized_menu_button"

    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440
    
        # Place card, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Place"):
            style "hkbd_button"
            action [ 
                Function(jn_snap._place_card_on_table, True),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        # Forfeit, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Forfeit"):
            style "hkbd_button"
            action [ 
                Function(renpy.jump, "snap_forfeit"),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        # Snap, but only selectable if there's enough cards down on the table, and both players are still capable of playing
        textbutton _("Snap!"):
            style "hkbd_button"
            action [ 
                Function(jn_snap._call_snap, True),
                SensitiveIf(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]
