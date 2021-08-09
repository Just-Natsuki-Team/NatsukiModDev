## Advanced scripts

These `.rpy` files are copies of important script files found in DDLC's `script.rpa` archive that are not necessary to change for basic modding projects, but may need to be replaced by more advanced projects.

As written, each of these files is functionally identical to the one included in DDLC, but with additional comments added to help you understand what they do. To override these files in your release simply make any changes needed there.

## Explanation of scripts

#### `cgs.rpy`

Defines the CG images for DDLC and some transforms that can be applied to them.

#### `console.rpy`

Defines the "fake console" effect that is used in a few scenes, including the background of Sayori's death. It's modeled on the console/error view in Renpy.

#### `credits.rpy`

Plays the ending credits scroll, with images being colored/deleted based on cg completion. If you do include credits for your game, be sure to acknowledge the original creators of DDLC!

#### `effects.rpy`

Defines most of the special effects used in the game, including the cool glitchy effects like screen color inversions, static, and screen tearing.

#### `glitchtext.rpy`

Defines a function that replace all letters in a string with random non-unicode characters (garbage).

#### `gui.rpy`

Defines the look of basic GUI elements like text, buttons, scrollbars, etc. Not to be confused with `screens.rpy`.

#### `poems_special.rpy`

Defines how "special poems" are displayed, which are poems stored as image assets, rather than text.

#### `poems.rpy`

Everything for poems in DDLC. It has the poems written by the club members shown to the player in normal gameplay written as plaintext. This also defines the function `showpoem()` which is used to call poems in game and the screen `poem` which handles the UI for the poem.

#### `poemwords.txt`

A comma separated list of words for the poem game, with the point values for each of the three girls.

#### `screens.rpy`

Defines all of the major screen objects in the game, like the say screen, menu screens, dialogue and input boxes, etc. Note that this gives both the appearance and the *functionality* of those objects.

#### `script-poemgame.rpy`

The entirety of the poem mini-game, including its appearance, functionality, and all of the weird glitchy things it can do in later acts.

#### `script-poemresponses.rpy`

This is the scene where the Main Character talks to each girl about his poem and reads theirs. It's a good example of how to use the results from the poem mini-game.

#### `transforms.rpy`

Defines character animations, screen transitions, and the special effects that can be applied to displayables in the game.
