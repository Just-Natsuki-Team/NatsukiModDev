## DDLC Mod Template

These `.rpy` files are copies of important script files found in DDLC's `script.rpa` archive that are necessary to change for most basic modding projects.

As written, each of these files is similar to those included in DDLC but with story specific game flow removed. This will allow you to tell the story you want to tell instead. The original code has been included in commented blocks, however, if you want to reproduce portions of the original game.

## Explanation of scripts

#### `options.rpy`

This file contains options that can be changed to customize your game. This file also includes the build options used when exporting your game for others to download.

#### `overrides.rpy`

This file is for overriding specific declarations from DDLC. You can use this to change images and other variables without having to directly edit the files in `/advanced_scripts`.

#### `script_example.rpy`

This is an example scene that teaches you a little about making mods, and is also a code example itself!

#### `script.rpy`

This is used for top-level game structure, and should not include any actual events or scripting; only logic and calling other labels. **This is the place to start for building your mod.**

#### `splash.rpy`

This splash screen is the first thing that Renpy will show the player. Also defines a lot of the behavior when first loading the game, such as checking for character files and jumping to scenes currently in progress.
