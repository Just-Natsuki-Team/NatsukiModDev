## Just Natsuki
An After Story style mod for Natsuki.

### Disclaimer:
For those who clone this repository to try the mod, please note that Just Natsuki is in heavy development.
As such, a lot of what you may see may be removed as more changes happen, they may wind up locked behind other features, or they may be removed entirely.

Therefore, if you're interested in really getting to know Natsuki, we recommend you wait until we're in a position to release, as there can be major issues with your persistent as development continues and our code changes.

If you're just interested in seeing what we're up to, or hunting for bugs, please open an issue if you come across one and there isn't an existing issue open for it.

#### TL;DR:
- Don't install the source code expecting a complete, polished Just Natsuki yet
- There likely will be data integrity issues if you play through enough of the commits
- There **will** be bugs

**Interested in a community server or chatting with the devs? Consider joining our Discord server! We'd love to have you!**
<p align="center">
    <a href=https://discord.gg/B7GcUsK>
        <img src="https://discordapp.com/api/guilds/441438764049629185/widget.png?style=banner4"/>
    </a>
</p>

## Explanation of scripts
These `.rpy` files are copies of important script files found in DDLC's `script.rpa` archive that are necessary to change for most basic modding projects.

As written, each of these files is similar to those included in DDLC but with story specific game flow removed. This will allow you to tell the story you want to tell instead. The original code has been included in commented blocks, however, if you want to reproduce portions of the original game.
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
