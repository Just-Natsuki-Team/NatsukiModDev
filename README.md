## DDLC Mod Template

These `.rpy` files are copies of important script files found in DDLC's `script.rpa` archive that are necessary to change for most basic modding projects.

As written, each of these files is similar to those included in DDLC but with story specific game flow removed. This will allow you to tell the story you want to tell instead. The original code has been included in commented blocks, however, if you want to reproduce portions of the original game.

**Interested in a community server or chatting with the devs? Consider joining our Discord server! We'd love to have you!**
<div style="text-align:center">
    <a href=https://discord.gg/B7GcUsK>
        <img src="https://discordapp.com/api/guilds/441438764049629185/widget.png?style=banner4"/>
    </a>
</div>

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

#### `script-ch30.rpy`

This is the MAIN script for everything in Natsuki's room. Dialogue and code.

#### `script-menus.rpy`

This is for every in game menu used in JN. Like dialogue and extras and dates. This ISNT every menu OUTSIDE of normal gameplay like settings or the like.

#### `Any of the script-(blank)date.rpys`

These are for each of the dates you can go to in JN. They don't each need their own explanation.

#### `zz_hotkey_buttons.rpy`

This one is in advanced scripts. It controlls the buttons and overall interface of JN beyond the normal game's.
