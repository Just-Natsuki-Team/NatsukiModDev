init python:
    import store
    from Enum import Enum

    JN_NATSUKI_ZORDER = 3

    _BASE_SPRITE_PATH = "mod_assets/natsuki/"


    class JNPose(Enum):
        sitting = 1

        def __str__(self):
            return self.name

    class JNBlush(Enum):
        full = 1
        light = 2

        def __str__(self):
            return self.name

    class JNMouth(Enum):
        agape = 1
        ajar = 2
        angry = 3
        awe = 4
        big = 5
        bigsmile = 6
        bored = 7
        caret = 8
        catty = 9
        devious = 10
        embarrassed = 11
        frown = 12
        furious = 13
        gasp = 14
        glub = 15
        grin = 16
        laugh = 17
        nervous = 18
        pout = 19
        pursed = 20
        scream = 21
        serious = 22
        shock = 23
        slant = 24
        small = 25
        smallfrown = 26
        smallsmile = 27
        smile = 28
        smirk = 29
        smug = 30
        tease = 31
        triange = 32
        uneasy = 33
        upset = 34
        worried = 35

        def __str__(self):
            return self.name

    class JNEyes(Enum):
        baka = 1
        circletears = 2
        closedhappy = 3
        closedsad = 4
        cute = 5
        normal = 6
        pleading = 7
        scared = 8
        shocked = 9
        smug = 10
        sparkle = 11
        squint = 12
        unamused = 13
        warm = 14
        wide = 15
        winkleft = 16
        winkright = 17

        def __str__(self):
            return self.name

    class JNEyebrows(Enum):
        normal = 1
        up = 2
        knit = 3
        furrowed = 4
        think = 5

        def __str__(self):
            return self.name

    class JNTears(Enum):
        heavy = 1
        light = 2

    def jn_generate_natsuki_sprite(
        pose,
        eyebrows,
        eyes,
        mouth,
        blush=None,
        tears=None
    ):
        """
        """
        lc_args = [
            (1280, 720), # Anchor
            (0, 0), _BASE_SPRITE_PATH + "desk/chair-normal.png", # Chair
            (0, 0), "{0}{1}/base/body.png".format(_BASE_SPRITE_PATH, pose), # Base
                (0, 0), "{0}{1}/clothes/[jn_globals.natsuki_current_outfit]/body.png".format(_BASE_SPRITE_PATH, pose), # Outfit, body
            (0, 0), "{0}{1}/hair/[jn_globals.natsuki_current_hairstyle]/back.png".format(_BASE_SPRITE_PATH, pose), # Hair back
        ]

        if blush:
            lc_args.extend([
                (0, 0), "{0}{1}/face/blush/{2}.png".format(_BASE_SPRITE_PATH, pose, blush)
            ])

        lc_args.extend([
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_BASE_SPRITE_PATH, pose, mouth), # Mouth
            (0, 0), "{0}{1}/face/nose/nose.png".format(_BASE_SPRITE_PATH, pose), # Nose
            (0, 0), "{0}{1}/hair/[jn_globals.natsuki_current_hairstyle]/bangs.png".format(_BASE_SPRITE_PATH, pose), # Hair front
        ])

        #TODO: Expand accessories and clothes into their own subsystems
        if store.jn_globals.natsuki_current_accessory is not None:
            lc_args.extend([
                (0, 0), "{0}{1}/accessories/[jn_globals.natsuki_current_accessory].png".format(_BASE_SPRITE_PATH, pose)
            ])

        lc_args.extend([
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_BASE_SPRITE_PATH, pose, eyes), # Eyes
        ])

        if tears:
            lc_args.extend([
                (0, 0), "{0}{1}/face/tears/{2}.png".format((_BASE_SPRITE_PATH, pose, blush))
            ])

        if store.jn_globals.natsuki_current_eyewear is not None:
            lc_args.extend([
                (0, 0), "{0}{1}/eyewear/[jn_globals.natsuki_current_eyewear].png".format(_BASE_SPRITE_PATH, pose)
            ])

        lc_args.extend([
            (0, 0), "{0}{1}/face/eyebrows/{2}.png".format(_BASE_SPRITE_PATH, pose, eyebrows), # Brows
            (0, 0), _BASE_SPRITE_PATH + "/desk/table-normal.png" # Table
        ])

        # Generate and return the sprite
        return renpy.display.layout.LiveComposite(
            *lc_args
        )

# Sprite code format:
# <pose><eyebrows><eyes><mouth><tears><blush>
#
# Sprite code values:
# <pose> - The current pose Natsuki is resting in
# 1 - upright
#
# <eyebrows> - The eyebrows Natsuki is currently showing
# n - normal
# u - up
# k - knit
# f - furrowed
# t - think
#
# <eyes> - The eyes Natsuki is currently showing
# bk - baka
# ct - circle/cartoon tears
# ch - closed happy
# cs - closed sad
# ct - cute
# nm - normal
# pl - pleading
# sc - scared
# sk - shocked
# sg - smug
# sp - sparkle
# sq - squint
# un - unamused
# wm - warm
# wd - wide
# wl - winking, left
# wr - winking, right
#
# <mouth> - The mouth shape Natsuki is currently making
# aj - ajar
# an - angry
# aw - awe
# bg - big
# bs - big smile
# bo - bored
# ca - caret
# ct - catty
# dv - devious
# em - embarrassed
# fr - frown
# fu - furious
# gs - gasp
# gn - grin
# lg - laugh
# nv - nervous
# po - pout
# pu - pursed
# sc - scream
# sr - serious
# sk - shock
# sl - slant
# sm - smile
# sf - small frown
# ss - small smile
# sg - smug
# ts - tease
# tr - triangle
# un - uneasy
# up - upset
# wr - worried
#
# <tears> - The tears Natsuki is currently showing
# h - heavy
# l - light
#
# <blush> - The amount of blush on Natsuki's face
# f - full
# l - light

# Sprite code listing
# Add your new sprite codes here
image natsuki sad = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.knit,
    eyes=JNEyes.pleading,
    mouth=JNMouth.serious
)


image natsuki 1unmbs = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.normal,
    mouth=JNMouth.bigsmile
)

##Placeholder redefs

#Boast
image natsuki 1ksqbs = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.knit,
    eyes=JNEyes.squint,
    mouth=JNMouth.bigsmile
)

#Neutral
image natsuki 1unmsm = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.normal,
    mouth=JNMouth.smile
)

#Pleading
image natsuki 1kwmsr = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.knit,
    eyes=JNEyes.warm,
    mouth=JNMouth.serious
)

#Pleased
image natsuki 1uchsm = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.closedhappy,
    mouth=JNMouth.smile
)

#Pleased (blush)
image natsuki 1uchsmf = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.closedhappy,
    mouth=JNMouth.smile,
    blush=JNBlush.full
)

#Sad
image natsuki 1kplsr = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.knit,
    eyes=JNEyes.pleading,
    mouth=JNMouth.serious
)

#Shy
image natsuki 1kchss = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.knit,
    eyes=JNEyes.closedhappy,
    mouth=JNMouth.smallsmile
)

#Smile
image natsuki 1uchbg = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.closedhappy,
    mouth=JNMouth.big
)

#Smile (blush)
image natsuki 1uchbgf = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.closedhappy,
    mouth=JNMouth.big,
    blush=JNBlush.full
)

#Smug
image natsuki 1fsqsm = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.furrowed,
    eyes=JNEyes.squint,
    mouth=JNMouth.smile
)

#Sparkle
image natsuki 1uspsm = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.sparkle,
    mouth=JNMouth.smile
)

#Tease
image natsuki 1fsqlg = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.furrowed,
    eyes=JNEyes.squint,
    mouth=JNMouth.laugh
)

#Unamused
image natsuki 1fsqsr = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.furrowed,
    eyes=JNEyes.squint,
    mouth=JNMouth.serious
)

#Wink (right)
image natsuki 1uwlgn = jn_generate_natsuki_sprite(
    pose=JNPose.sitting,
    eyebrows=JNEyebrows.up,
    eyes=JNEyes.winkright,
    mouth=JNMouth.grin
)

label emote_test:
    n sad "this is me sad"
    n 1unmsm "this is me smiling"
    n 1unmbs "This is me smiling big"
    n happy "This is me happy"
    return
