init 0 python in jn_sprites:
    import store
    from Enum import Enum

    _BASE_SPRITE_PATH = "mod_assets/natsuki/"
    _NATSUKI_Z_INDEX = 3

    class Pose(Enum):
        sitting = 1

        def __str__(self):
            return self.name
    
    class Blush(Enum):
        full = 1
        light = 2

        def __str__(self):
            return self.name

    class Mouth(Enum):
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

    class Eyes(Enum):
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

    class Eyebrows(Enum):
        normal = 1
        up = 2
        knit = 3
        furrowed = 4
        think = 5

        def __str__(self):
            return self.name

    class Tears(Enum):
        heavy = 1
        light = 2

    def generate_natsuki_sprite(
        pose,
        eyebrows,
        eyes,
        mouth,
        blush=None,
        tears=None
    ):
        """
        """

        # Handle required args
        if not pose:
            raise Exception("Parameter 'pose' cannot be None")

        if not mouth:
            raise Exception("Parameter 'mouth' cannot be None")

        if not eyes:
            raise Exception("Parameter 'eyes' cannot be None")

        if not eyebrows:
            raise Exception("Parameter 'eyebrows' cannot be None")
        
        # Handle optional args
        blush_args = ((0, 0), "{0}{1}/etc/empty.png".format(_BASE_SPRITE_PATH, pose.__str__()))
        if blush:
            blush_args = ((0, 0), "{0}{1}/face/blush/{2}.png".format((_BASE_SPRITE_PATH, pose.__str__(), blush.__str__())))

        tears_args = ((0, 0), "{0}{1}/etc/empty.png".format(_BASE_SPRITE_PATH, pose.__str__()))
        if tears:
            tears_args = ((0, 0), "{0}{1}/face/tears/{2}.png".format((_BASE_SPRITE_PATH, pose.__str__(), blush.__str__())))

        hairclip_args = ((0, 0), "{0}{1}/etc/empty.png".format(_BASE_SPRITE_PATH, pose.__str__()))
        if store.jn_globals.natsuki_current_accessory is not None:
            hairclip_args = ((0, 0), "{0}{1}/accessories/{2}.png".format(_BASE_SPRITE_PATH, pose.__str__(), store.jn_globals.natsuki_current_accessory))

        eyewear_args = ((0, 0), "{0}{1}/etc/empty.png".format(_BASE_SPRITE_PATH, pose.__str__()))
        if store.jn_globals.natsuki_current_eyewear is not None:
            eyewear_args = ((0, 0), "{0}{1}/eyewear/{2}.png".format(_BASE_SPRITE_PATH, pose.__str__(), store.jn_globals.natsuki_current_eyewear))

        # Generate and return the sprite
        return renpy.display.layout.LiveComposite(
            (1280, 720), # Anchor
            (0, 0), "{0}{1}/table/chair-normal.png".format(_BASE_SPRITE_PATH, pose.__str__()), # Chair
            (0, 0), "{0}{1}/base/body.png".format(_BASE_SPRITE_PATH, pose.__str__()), # Base
            (0, 0), "{0}{1}/clothes/{2}/body.png".format(_BASE_SPRITE_PATH, pose.__str__(), store.jn_globals.natsuki_current_outfit), # Outfit, body
            (0, 0), "{0}{1}/hair/{2}/back.png".format(_BASE_SPRITE_PATH, pose.__str__(), store.jn_globals.natsuki_current_hairstyle), # Hair back
            blush_args[0], blush_args[1], #Blush
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_BASE_SPRITE_PATH, pose.__str__(), mouth.__str__()), # Mouth
            (0, 0), "{0}{1}/face/nose/nose.png".format(_BASE_SPRITE_PATH, pose.__str__()), # Nose
            (0, 0), "{0}{1}/hair/{2}/bangs.png".format(_BASE_SPRITE_PATH, pose.__str__(), store.jn_globals.natsuki_current_hairstyle), # Hair front
            hairclip_args[0], hairclip_args[1], # Hairclip
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_BASE_SPRITE_PATH, pose.__str__(), eyes.__str__()), # Eyes
            tears_args[0], tears_args[1], # Tears
            eyewear_args[0], eyewear_args[1], # Eyewear
            (0, 0), "{0}{1}/face/eyebrows/{2}.png".format(_BASE_SPRITE_PATH, pose.__str__(), eyebrows.__str__()), # Brows
            (0, 0), "{0}{1}/table/table-normal.png".format(_BASE_SPRITE_PATH, pose.__str__()) # Table
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
image natsuki happy = jn_sprites.generate_natsuki_sprite(pose=jn_sprites.Pose.sitting, eyebrows=jn_sprites.Eyebrows.up, eyes=jn_sprites.Eyes.closedhappy, mouth=jn_sprites.Mouth.smile)
image natsuki sad = jn_sprites.generate_natsuki_sprite(pose=jn_sprites.Pose.sitting, eyebrows=jn_sprites.Eyebrows.knit, eyes=jn_sprites.Eyes.pleading, mouth=jn_sprites.Mouth.serious)
