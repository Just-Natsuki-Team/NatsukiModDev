init -1 python in jn_sprites:
    from Enum import Enum

    _BASE_SPRITE_PATH = "mod_assets/natsuki/"
    _NATSUKI_Z_INDEX = 3

# Base images - these sandwich the individual code to help prevent repetition

# Natsuki's chair, body, outfit and hair behind her face
image natsuki_base_a = LiveComposite(
    (0, 0), # Anchor
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/table/chair-normal.png", # Chair
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/base/body.png", # Base
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/clothes/[jn_globals.natsuki_current_outfit]/body.png", # Outfit, body
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/hair/[jn_globals.natsuki_current_hairstyle]/back.png", # Hair back
)

# Natsuki's nose and hair in front of her face
image natsuki_base_b = LiveComposite(
    (0, 0), # Anchor
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/face/nose/nose.png", # Nose
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/hair/[jn_globals.natsuki_current_hairstyle]/bangs.png", # Hair front
    (0, 0), ConditionSwitch( # Hair clips 
        "jn_globals.natsuki_current_accessory is not None", "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/accessories/[jn_globals.natsuki_current_accessory].png",
        "True", "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/etc/empty.png"
    )
)

# Natsuki's desk and any decorations/props
image natsuki_base_c = LiveComposite(
    (0, 0), # Anchor
    (0, 0), "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/table/table-normal.png" # Table
)

init 0 python in jn_sprites:
    import store
    
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

    def generate_natsuki_sprite(
        mouth,
        eyes,
        eyebrows,
        blush=Blush.light,
    ):
        if not mouth:
            raise Exception("Parameter 'mouth' cannot be None")

        if not eyes:
            raise Exception("Parameter 'eyes' cannot be None")

        if not eyebrows:
            raise Exception("Parameter 'eyebrows' cannot be None")

        return renpy.display.layout.LiveComposite(
            (1280, 720), # Anchor
            (0, 0), "natsuki_base_a",
            (0, 0), "{0}{1}/face/blush/{2}.png".format(_BASE_SPRITE_PATH, store.jn_globals.natsuki_current_pose, blush.__str__()), # Blush
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_BASE_SPRITE_PATH, store.jn_globals.natsuki_current_pose, mouth.__str__()), # Mouth
            (0, 0), "natsuki_base_b",
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_BASE_SPRITE_PATH, store.jn_globals.natsuki_current_pose, eyes.__str__()), # Eyes
            (0, 0), renpy.display.layout.ConditionSwitch( # Glasses
                "jn_globals.natsuki_current_eyewear is not None", "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/eyewear/[jn_globals.natsuki_current_eyewear].png",
                "True", "[jn_sprites._BASE_SPRITE_PATH][jn_globals.natsuki_current_pose]/etc/empty.png"
            ),
            (0, 0), "{0}{1}/face/eyebrows/{2}.png".format(_BASE_SPRITE_PATH, store.jn_globals.natsuki_current_pose, eyebrows.__str__()), # Brows
            (0, 0), "natsuki_base_c"
        )

# Sprite code generation - we'll need a lot of these setting up and with a common code convention
image natsuki happy = jn_sprites.generate_natsuki_sprite(mouth=jn_sprites.Mouth.smile, eyes=jn_sprites.Eyes.closedhappy, eyebrows=jn_sprites.Eyebrows.up)
image natsuki sad = jn_sprites.generate_natsuki_sprite(mouth=jn_sprites.Mouth.serious, eyes=jn_sprites.Eyes.pleading, eyebrows=jn_sprites.Eyebrows.knit)