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
        pooled = 2

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

init 1 python:
    POSE_MAP = {
        "1": JNPose.sitting,
    }

    EYEBROW_MAP = {
        "n": JNEyebrows.normal,
        "u": JNEyebrows.up,
        "k": JNEyebrows.knit,
        "f": JNEyebrows.furrowed,
        "t": JNEyebrows.think,
    }

    EYE_MAP = {
        "bk": JNEyes.baka,
        "ct": JNEyes.circletears,
        "ch": JNEyes.closedhappy,
        "cs": JNEyes.closedsad,
        "cu": JNEyes.cute,
        "nm": JNEyes.normal,
        "pl": JNEyes.pleading,
        "sc": JNEyes.scared,
        "sk": JNEyes.shocked,
        "sg": JNEyes.smug,
        "sp": JNEyes.sparkle,
        "sq": JNEyes.squint,
        "un": JNEyes.unamused,
        "wm": JNEyes.warm,
        "wd": JNEyes.wide,
        "wl": JNEyes.winkleft,
        "wr": JNEyes.winkright,
    }

    MOUTH_MAP = {
        "aj": JNMouth.ajar,
        "an": JNMouth.angry,
        "aw": JNMouth.awe,
        "bg": JNMouth.big,
        "bs": JNMouth.bigsmile,
        "bo": JNMouth.bored,
        "ca": JNMouth.caret,
        "ct": JNMouth.catty,
        "dv": JNMouth.devious,
        "em": JNMouth.embarrassed,
        "fr": JNMouth.frown,
        "fu": JNMouth.furious,
        "gs": JNMouth.gasp,
        "gn": JNMouth.grin,
        "lg": JNMouth.laugh,
        "nv": JNMouth.nervous,
        "po": JNMouth.pout,
        "pu": JNMouth.pursed,
        "sc": JNMouth.scream,
        "sr": JNMouth.serious,
        "sk": JNMouth.shock,
        "sl": JNMouth.slant,
        "sm": JNMouth.smile,
        "sf": JNMouth.smallfrown,
        "ss": JNMouth.smallsmile,
        "sg": JNMouth.smug,
        "ts": JNMouth.tease,
        "tr": JNMouth.triange,
        "un": JNMouth.uneasy,
        "up": JNMouth.upset,
        "wr": JNMouth.worried,
    }

    TEARS_MAP = {
        "h": JNTears.heavy,
        "p": JNTears.pooled,
    }

    BLUSH_MAP = {
        "f": JNBlush.full,
        "l": JNBlush.light,
    }

    def _parse_exp_code(exp_code):
        """
        Parses the given expression code and returns the **kwargs to create the sprite if it is valid

        THROWS:
            ValueError if the expression is invalid due to length (too short)
            KeyError if the expression is invalid due to invalid parts
        """
        #Check if the length is valid first
        if len(exp_code) < 6:
            raise ValueError("Invalid expression code: {0}".format(exp_code))

        #Left to right, first is the pose
        pose = exp_code[0]
        exp_code = exp_code[1:]

        #Next, eyebrows
        eyebrows = exp_code[0]
        exp_code = exp_code[1:]

        #Next, eyes
        eyes = exp_code[:2]
        exp_code = exp_code[2:]

        #Next, mouth
        mouth = exp_code[:2]
        exp_code = exp_code[2:]

        blush = None
        tears = None

        #If we still have an expcode, we know we have either tears, blush, or both
        while exp_code:
            exp_part = exp_code[0]
            exp_code = exp_code[1:]

            #Check if part is a tear
            if exp_part in TEARS_MAP:
                tears = TEARS_MAP[exp_part]

            #Otherwise it might be a blush
            elif exp_part in BLUSH_MAP:
                blush = BLUSH_MAP[exp_part]


        return {
            "pose": POSE_MAP[pose],
            "eyebrows": EYEBROW_MAP[eyebrows],
            "eyes": EYE_MAP[eyes],
            "mouth": MOUTH_MAP[mouth],
            "tears": TEARS_MAP.get(tears),
            "blush": BLUSH_MAP.get(blush),
        }

# Sprite code format:
# <pose><eyebrows><eyes><mouth><tears><blush>
#
# Some notes regarding lengths of each part:
#   pose: 1 character
#   eyebrows: 1 character
#   eyes: 2 characters
#   mouth: 2 characters
#   tears: 1 character
#   blush: 1 character
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
# cu - cute
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
# p - pooled
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
