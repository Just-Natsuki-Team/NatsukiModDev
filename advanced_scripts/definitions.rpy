#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.
#Also maybe don't break anything. Natsuki will be angry!

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = True #Change this flag to True to enable dev tools
define natsuki_love = False #Don't touch this is usually breaks stuff.

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.tdokidoki = "mod_assets/bgm/dokidoki.ogg"
define audio.tpoems = "mod_assets/bgm/poems.ogg"
define audio.custom1 = "custom-music/01.mp3"
define audio.custom2 = "custom-music/02.mp3"
define audio.custom3 = "custom-music/03.mp3"
define audio.battle = "custom-music/battle.mp3"
define audio.spooky1 = "mod_assets/bgm/spooky1.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)(No, it doesn't have to.) -Edgar

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
define audio.tbeach = "mod_assets/sfx/beachsfx.ogg"
define audio.tsmoshsong = "mod_assets/bgm/smoshsong.ogg"
define audio.tattack = "mod_assets/bgm/attack.ogg"
define audio.tattack2 = "mod_assets/bgm/mallattack.ogg"
define audio.tchase = "mod_assets/bgm/chase.ogg"
define audio.tmonikafight = "<loop 14.0>mod_assets/bgm/monikafight.ogg"
define audio.theend = "mod_assets/bgm/theend.ogg"
define audio.rewind = "mod_assets/bgm/rewind.ogg"
define audio.tbeach_night = "<loop 5.0>mod_assets/bgm/beachnight.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

image splash_glitch_2 = "images/bg/splash-glitch2.png"

# Backgrounds
image black = "#000000"
#image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image chocolate = "mod_assets/JustNatsuki/chocolate.png"


image nb1:
    "mod_assets/nb1.png"
image nb2:
    "mod_assets/natsukidrink.png"
image nb3:
    "mod_assets/nb2.png"
image smoshscreen:
    "mod_assets/easter_eggs/smosheastereggscreen.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image residential_night = "mod_assets/locations/residential/residential_night.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image house_night = "mod_assets/locations/residential/house_night.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bm2 = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1bl2.png", (0, 0), "mod_assets/natsuki/1br2.png", (0, 0), "mod_assets/natsuki/m2.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

image natsuki 1ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/a.png")
image natsuki 1cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/b.png")
image natsuki 1cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/c.png")
image natsuki 1cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/d.png")
image natsuki 1ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/e.png")
image natsuki 1cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/f.png")
image natsuki 1cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/g.png")
image natsuki 1ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/h.png")
image natsuki 1ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/i.png")
image natsuki 1cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/j.png")
image natsuki 1ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/k.png")
image natsuki 1cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/l.png")
image natsuki 1cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/m.png")
image natsuki 1cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/n.png")
image natsuki 1co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/o.png")
image natsuki 1cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/p.png")
image natsuki 1cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/q.png")
image natsuki 1cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/r.png")
image natsuki 1cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/s.png")
image natsuki 1ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/t.png")
image natsuki 1cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/u.png")
image natsuki 1cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/v.png")
image natsuki 1cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/w.png")
image natsuki 1cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/x.png")
image natsuki 1cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/y.png")
image natsuki 1cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/z.png")

image natsuki 2ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/a.png")
image natsuki 2cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/b.png")
image natsuki 2cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/c.png")
image natsuki 2cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/d.png")
image natsuki 2ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/e.png")
image natsuki 2cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/f.png")
image natsuki 2cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/g.png")
image natsuki 2ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/h.png")
image natsuki 2ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/i.png")
image natsuki 2cj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/j.png")
image natsuki 2ck = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/k.png")
image natsuki 2cl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/l.png")
image natsuki 2cm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/m.png")
image natsuki 2cn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/n.png")
image natsuki 2co = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/o.png")
image natsuki 2cp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/p.png")
image natsuki 2cq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/q.png")
image natsuki 2cr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/r.png")
image natsuki 2cs = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/s.png")
image natsuki 2ct = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/t.png")
image natsuki 2cu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/u.png")
image natsuki 2cv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/v.png")
image natsuki 2cw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/w.png")
image natsuki 2cx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/x.png")
image natsuki 2cy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/y.png")
image natsuki 2cz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/z.png")

image natsuki 12ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2bta.png")
image natsuki 12cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2bte.png")
image natsuki 12cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2btc.png")
image natsuki 12cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2btd.png")
image natsuki 12ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2bte.png")
image natsuki 12cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2btf.png")
image natsuki 12cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2btg.png")
image natsuki 12ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2bth.png")
image natsuki 12ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1cl.png", (0, 0), "mod_assets/natsuki/1cr.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ca = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2bta.png")
image natsuki 42cb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2bte.png")
image natsuki 42cc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2btc.png")
image natsuki 42cd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2btd.png")
image natsuki 42ce = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2bte.png")
image natsuki 42cf = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2btf.png")
image natsuki 42cg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2btg.png")
image natsuki 42ch = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2bth.png")
image natsuki 42ci = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2cl.png", (0, 0), "mod_assets/natsuki/2cr.png", (0, 0), "natsuki/2bti.png")

# Normal Beach Outfit, Used at lower \"romance\" levels.

image natsuki 1da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/a.png")
image natsuki 1db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/b.png")
image natsuki 1dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/c.png")
image natsuki 1dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/d.png")
image natsuki 1de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/e.png")
image natsuki 1df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/f.png")
image natsuki 1dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/g.png")
image natsuki 1dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/h.png")
image natsuki 1di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/i.png")
image natsuki 1dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/j.png")
image natsuki 1dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/k.png")
image natsuki 1dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/l.png")
image natsuki 1dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/m.png")
image natsuki 1dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/n.png")
image natsuki 1do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/o.png")
image natsuki 1dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/p.png")
image natsuki 1dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/q.png")
image natsuki 1dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/r.png")
image natsuki 1ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/s.png")
image natsuki 1dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/t.png")
image natsuki 1du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/u.png")
image natsuki 1dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/v.png")
image natsuki 1dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/w.png")
image natsuki 1dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/x.png")
image natsuki 1dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/y.png")
image natsuki 1dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1dl.png", (0, 0), "mod_assets/natsuki/1dr.png", (0, 0), "natsuki/z.png")

image natsuki 2da = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/a.png")
image natsuki 2db = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/b.png")
image natsuki 2dc = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/c.png")
image natsuki 2dd = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/d.png")
image natsuki 2de = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/e.png")
image natsuki 2df = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/f.png")
image natsuki 2dg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/g.png")
image natsuki 2dh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/h.png")
image natsuki 2di = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/i.png")
image natsuki 2dj = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/j.png")
image natsuki 2dk = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/k.png")
image natsuki 2dl = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/l.png")
image natsuki 2dm = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/m.png")
image natsuki 2dn = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/n.png")
image natsuki 2do = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/o.png")
image natsuki 2dp = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/p.png")
image natsuki 2dq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/q.png")
image natsuki 2dr = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/r.png")
image natsuki 2ds = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/s.png")
image natsuki 2dt = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/t.png")
image natsuki 2du = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/u.png")
image natsuki 2dv = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/v.png")
image natsuki 2dw = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/w.png")
image natsuki 2dx = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/x.png")
image natsuki 2dy = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/y.png")
image natsuki 2dz = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2dl.png", (0, 0), "mod_assets/natsuki/2dr.png", (0, 0), "natsuki/z.png")

# Bikini Outfit, Natsuki's Swim outfit at higher "Romance" level.

image natsuki 1ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/a.png")
image natsuki 1eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/b.png")
image natsuki 1ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/c.png")
image natsuki 1ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/d.png")
image natsuki 1ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/e.png")
image natsuki 1ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/f.png")
image natsuki 1eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/g.png")
image natsuki 1eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/h.png")
image natsuki 1ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/i.png")
image natsuki 1ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/j.png")
image natsuki 1ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/k.png")
image natsuki 1el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/l.png")
image natsuki 1em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/m.png")
image natsuki 1en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/n.png")
image natsuki 1eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/o.png")
image natsuki 1ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/p.png")
image natsuki 1eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/q.png")
image natsuki 1er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/r.png")
image natsuki 1es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/s.png")
image natsuki 1et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/t.png")
image natsuki 1eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/u.png")
image natsuki 1ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/v.png")
image natsuki 1ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/w.png")
image natsuki 1ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/x.png")
image natsuki 1ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/y.png")
image natsuki 1ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/z.png")

image natsuki 2ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/a.png")
image natsuki 2eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/b.png")
image natsuki 2ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/c.png")
image natsuki 2ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/d.png")
image natsuki 2ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/e.png")
image natsuki 2ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/f.png")
image natsuki 2eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/g.png")
image natsuki 2eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/h.png")
image natsuki 2ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/i.png")
image natsuki 2ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/j.png")
image natsuki 2ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/k.png")
image natsuki 2el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/l.png")
image natsuki 2em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/m.png")
image natsuki 2en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/n.png")
image natsuki 2eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/o.png")
image natsuki 2ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/p.png")
image natsuki 2eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/q.png")
image natsuki 2er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/r.png")
image natsuki 2es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/s.png")
image natsuki 2et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/t.png")
image natsuki 2eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/u.png")
image natsuki 2ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/v.png")
image natsuki 2ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/w.png")
image natsuki 2ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/x.png")
image natsuki 2ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/y.png")
image natsuki 2ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/z.png")

image natsuki 3ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/a.png")
image natsuki 3eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/b.png")
image natsuki 3ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/c.png")
image natsuki 3ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/d.png")
image natsuki 3ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/e.png")
image natsuki 3ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/f.png")
image natsuki 3eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/g.png")
image natsuki 3eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/h.png")
image natsuki 3ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/i.png")
image natsuki 3ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/j.png")
image natsuki 3ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/k.png")
image natsuki 3el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/l.png")
image natsuki 3em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/m.png")
image natsuki 3en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/n.png")
image natsuki 3eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/o.png")
image natsuki 3ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/p.png")
image natsuki 3eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/q.png")
image natsuki 3er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/r.png")
image natsuki 3es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/s.png")
image natsuki 3et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/t.png")
image natsuki 3eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/u.png")
image natsuki 3ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/v.png")
image natsuki 3ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/w.png")
image natsuki 3ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/x.png")
image natsuki 3ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/y.png")
image natsuki 3ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/z.png")

image natsuki 4ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/a.png")
image natsuki 4eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/b.png")
image natsuki 4ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/c.png")
image natsuki 4ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/d.png")
image natsuki 4ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/e.png")
image natsuki 4ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/f.png")
image natsuki 4eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/g.png")
image natsuki 4eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/h.png")
image natsuki 4ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/i.png")
image natsuki 4ej = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/j.png")
image natsuki 4ek = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/k.png")
image natsuki 4el = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/l.png")
image natsuki 4em = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/m.png")
image natsuki 4en = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/n.png")
image natsuki 4eo = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/o.png")
image natsuki 4ep = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/p.png")
image natsuki 4eq = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/q.png")
image natsuki 4er = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/r.png")
image natsuki 4es = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/s.png")
image natsuki 4et = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/t.png")
image natsuki 4eu = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/u.png")
image natsuki 4ev = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/v.png")
image natsuki 4ew = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/w.png")
image natsuki 4ex = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/x.png")
image natsuki 4ey = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/y.png")
image natsuki 4ez = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/z.png")

image natsuki 12ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2bta.png")
image natsuki 12eb = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2bte.png")
image natsuki 12ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2btc.png")
image natsuki 12ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2btd.png")
image natsuki 12ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2bte.png")
image natsuki 12ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2btf.png")
image natsuki 12eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2btg.png")
image natsuki 12eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2bth.png")
image natsuki 12ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/1el.png", (0, 0), "mod_assets/natsuki/1er.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ea = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2bta.png")
image natsuki 42ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2bte.png")
image natsuki 42ec = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2btc.png")
image natsuki 42ed = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2btd.png")
image natsuki 42ee = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2bte.png")
image natsuki 42ef = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2btf.png")
image natsuki 42eg = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2btg.png")
image natsuki 42eh = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2bth.png")
image natsuki 42ei = im.Composite((960, 960), (0, 0), "mod_assets/natsuki/2el.png", (0, 0), "mod_assets/natsuki/2er.png", (0, 0), "natsuki/2bti.png")


# These are expression definitions! They go like J(Emotion)(Number). N = Normal/Nuetral, H = Happy, S = Sad, A = Angry.

image natsuki jn = "/mod_assets/JustNatsuki/jnbase.png"
image natsuki jha = "/mod_assets/JustNatsuki/jnha.png"
image natsuki jha_idle:
    "/mod_assets/JustNatsuki/jnha.png"
    5.0
    "/mod_assets/JustNatsuki/jnha2.png"
    0.4
    repeat
image natsuki jhb = "/mod_assets/JustNatsuki/jnhb.png"
image natsuki jhb_idle:
    "/mod_assets/JustNatsuki/jnhb.png"
    5.0
    "/mod_assets/JustNatsuki/jnna2.png"
    0.4
    repeat
image natsuki jaa = "/mod_assets/JustNatsuki/jnaa.png"
image natsuki jaa_idle:
    "/mod_assets/JustNatsuki/jnaa.png"
    5.0
    "/mod_assets/JustNatsuki/jnaa2.png"
    0.4
    repeat
image natsuki jab = "/mod_assets/JustNatsuki/jnab.png"
image natsuki jac = "/mod_assets/JustNatsuki/jnac.png"
image natsuki jad = "/mod_assets/JustNatsuki/jnad.png"
image natsuki jsa = "/mod_assets/JustNatsuki/jnsa.png"
image natsuki jsa_idle:
    "/mod_assets/JustNatsuki/jnsa.png"
    5.0
    "/mod_assets/JustNatsuki/jnsa2.png"
    0.4
    repeat
image natsuki jnb = "/mod_assets/JustNatsuki/jnnb.png"
image natsuki jhc = "/mod_assets/JustNatsuki/jnhc.png"
image natsuki jhd = "/mod_assets/JustNatsuki/jnhd.png"
image natsuki jsb = "/mod_assets/JustNatsuki/jnsb.png"
image natsuki jyan = "/mod_assets/JustNatsuki/jnyan.png"
image natsuki jp = "/mod_assets/JustNatsuki/jnp.png"
image natsuki jba = "/mod_assets/JustNatsuki/jnba.png"


image natsuki beach = "mod_assets/nb1.png"

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")


image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

#---------------------------------------------------THE MC (Don't trust him)--------------------------------------------

image mc 1a = "mod_assets/mc.png"
image mc 1b = "mod_assets/mc/mcangry.png"
image mc 1c = "mod_assets/mc/mcsad.png"

############### Natsuki's dad ########################

### Base poses ###

image natsukidad 1a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 1b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 1c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 1d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 1e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 1f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 1g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 1h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 1i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 1j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 1k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 1l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 1m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 1n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 1o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 1p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 1q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 1r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 1s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 1t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 1u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 1v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 1w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 1x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/aB.png")

image natsukidad 2a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 2b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 2c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 2d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 2e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 2f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 2g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 2h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 2i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 2j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 2k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 2l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 2m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 2n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 2o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 2p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 2q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 2r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 2s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 2t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 2u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 2v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 2w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 2x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/aB.png")

image natsukidad 3a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 3b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 3c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 3d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 3e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 3f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 3g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 3h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 3i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 3j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 3k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 3l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 3m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 3n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 3o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 3p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 3q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 3r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 3s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 3t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 3u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 3v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 3w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 3x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/aB.png")

image natsukidad 4a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 4b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 4c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 4d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 4e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 4f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 4g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 4h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 4i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 4j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 4k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 4l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 4m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 4n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 4o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 4p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 4q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 4r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 4s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 4t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 4u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 4v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 4w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 4x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/aB.png")

image natsukidad 5a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/3a.png")
image natsukidad 5x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/3a.png")

### Base poses (With drunk blush) ###

image natsukidad 1ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 1xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image natsukidad 2ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 2xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image natsukidad 3ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 3xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image natsukidad 4ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 4xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2l.png", (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image natsukidad 5ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 5xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/3a.png", (0, 0), "mod_assets/natsukidad/db.png")

### Bottle Poses ###

image natsukidad 6a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 6b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 6c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 6d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 6e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 6f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 6g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 6h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 6i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 6j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 6k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 6l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 6m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 6n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 6o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 6p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 6q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 6r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 6s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 6t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 6u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 6v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 6w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 6x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/aB.png")

image natsukidad 7a = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a.png")
image natsukidad 7b = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/b.png")
image natsukidad 7c = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/c.png")
image natsukidad 7d = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/d.png")
image natsukidad 7e = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/e.png")
image natsukidad 7f = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/f.png")
image natsukidad 7g = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/g.png")
image natsukidad 7h = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/h.png")
image natsukidad 7i = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/i.png")
image natsukidad 7j = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/j.png")
image natsukidad 7k = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/k.png")
image natsukidad 7l = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/l.png")
image natsukidad 7m = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/m.png")
image natsukidad 7n = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/n.png")
image natsukidad 7o = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/o.png")
image natsukidad 7p = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/p.png")
image natsukidad 7q = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/q.png")
image natsukidad 7r = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/r.png")
image natsukidad 7s = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/s.png")
image natsukidad 7t = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/t.png")
image natsukidad 7u = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/u.png")
image natsukidad 7v = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/v.png")
image natsukidad 7w = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a2.png")
image natsukidad 7x = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/aB.png")

### Bottle Poses (With drunk blush) ###

image natsukidad 6ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 6xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/1r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image natsukidad 7ad = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7bd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/b.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7cd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/c.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7dd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/d.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7ed = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/e.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7fd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/f.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7gd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/g.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7hd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/h.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7id = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/i.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7jd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/j.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7kd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/k.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7ld = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/l.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7md = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/m.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7nd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/n.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7od = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/o.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7pd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/p.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7qd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/q.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7rd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/r.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7sd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/s.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7td = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/t.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7ud = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/u.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7vd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/v.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7wd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/a2.png", (0, 0), "mod_assets/natsukidad/db.png")
image natsukidad 7xd = im.Composite((960, 960), (0, 0), "mod_assets/natsukidad/2r.png", (0, 0), "mod_assets/natsukidad/4l.png", (0, 0), "mod_assets/natsukidad/aB.png", (0, 0), "mod_assets/natsukidad/db.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define base = DynamicCharacter('base_name', image='n_base', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define clothes = DynamicCharacter('clothes_name', image='n_cloth', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define flag = DynamicCharacter('flag_name', image='n_flag', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define p = Character('Player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nd = DynamicCharacter('nd_name', image='natsukidad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default nd_name = "Dad"

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.blah = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default in_skipable = False

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default clothes_name = "Clothes"
default base_name = "Base"
default flag_name = "Flag"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori'] #Seems rigged...

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None
#Who's the "we", Dan?

#Code for Natsuki. Update: Damn a lot of these variables are messy and unused, might need to do some cleaning here...
default allow_dialogue = None
default allow_dialogue2 = None
default beach = None
default mall = None
default park = None
default club = None
default anime_like = None
default sayori_cutscene = False
default natsuki_lovescene = False
default penis_scene = False #What the fuck is this?
default yuri_cutscene = False
default yuri_hidebutton_loop = False
default normal_dialogue = True
default seen_age_ask = False
default seen_park_ask = False
default monika_return = False

# Music options. Update: Man this is outdated....
default persistent.music_daijoubu = None
default persistent.music_natsuki = None
default persistent.music_dokidoki = None
default persistent.music_room = None


# Open a multi-game persistent file to share with other mods
#Why the hell would you want that?! Unless you're making a squeal I guess...
init 1 python:
    mp = MultiPersistent("ddlc_mods")

    # This persistent simply tracks which mods have been played
    if mp.played is None:
        mp.played = {}
    mp.played[config.name] = True

    #Be sure to save the multipersistent after any changes
    mp.save()
