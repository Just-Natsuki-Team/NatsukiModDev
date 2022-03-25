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
        triangle = 32
        uneasy = 33
        upset = 34
        worried = 35
        drink = 37

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
        lookleft = 18
        lookright = 19
        squintleft = 20
        squintright = 21

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

        def __str__(self):
            return self.name

    class JNEmote(Enum):
        affection = 1
        anger = 2
        dazzle = 3
        dread = 4
        exclamation = 5
        idea = 6
        merry = 7
        questionmark = 8
        sad = 9
        sigh = 10
        shock = 11
        sleepy = 12
        somber = 13
        speech = 14
        surprise = 15

        def __str__(self):
            return self.name

    def jn_generate_natsuki_sprite(
        pose,
        eyebrows,
        eyes,
        mouth,
        blush=None,
        tears=None,
        emote=None
    ):
        """
        """
        lc_args = [
            (1280, 740), # Anchor
            (0, 0), _BASE_SPRITE_PATH + "desk/chair-normal.png", # Chair
            (0, 0), "{0}{1}/hair/[persistent.jn_natsuki_current_hairstyle]/back.png".format(_BASE_SPRITE_PATH, pose), # Hair back
            (0, 0), "{0}{1}/base/body.png".format(_BASE_SPRITE_PATH, pose), # Body
            (0, 0), "{0}{1}/clothes/[persistent.jn_natsuki_current_outfit]/body.png".format(_BASE_SPRITE_PATH, pose), # Outfit, body
        ]

         #TODO: Fix this
        # if store.persistent.jn_natsuki_current_necklace is not None:
        #     lc_args.extend([
        #         (0, 0), "{0}{1}/necklace/[persistent.jn_natsuki_current_necklace].png".format(_BASE_SPRITE_PATH, pose)
        #     ])

        lc_args.extend([
            (0, 0), "{0}{1}/base/head.png".format(_BASE_SPRITE_PATH, pose), # Head
        ])

        if blush:
            lc_args.extend([
                (0, 0), "{0}{1}/face/blush/{2}.png".format(_BASE_SPRITE_PATH, pose, blush)
            ])

        lc_args.extend([
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_BASE_SPRITE_PATH, pose, mouth), # Mouth
            (0, 0), "{0}{1}/face/nose/nose.png".format(_BASE_SPRITE_PATH, pose), # Nose
            (0, 0), "{0}{1}/hair/[persistent.jn_natsuki_current_hairstyle]/bangs.png".format(_BASE_SPRITE_PATH, pose), # Hair front
        ])

        #TODO: Expand accessories and clothes into their own subsystems
        if store.persistent.jn_natsuki_current_accessory is not None:
            lc_args.extend([
                (0, 0), "{0}{1}/accessories/[persistent.jn_natsuki_current_accessory].png".format(_BASE_SPRITE_PATH, pose)
            ])

        lc_args.extend([
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_BASE_SPRITE_PATH, pose, eyes), # Eyes
        ])

        if tears:
            lc_args.extend([
                (0, 0), "{0}{1}/face/tears/{2}.png".format((_BASE_SPRITE_PATH, pose, blush))
            ])

        #TODO: Fix this
        # if store.persistent.jn_natsuki_current_headgear is not None:
        #     lc_args.extend([
        #         (0, 0), "{0}{1}/headgear/[persistent.jn_natsuki_current_headgear].png".format(_BASE_SPRITE_PATH, pose)
        #     ])

         #TODO: Fix this
        # if store.persistent.jn_natsuki_current_eyewear is not None:
        #     lc_args.extend([
        #         (0, 0), "{0}{1}/eyewear/[persistent.jn_natsuki_current_eyewear].png".format(_BASE_SPRITE_PATH, pose)
        #     ])

        if emote:
            lc_args.extend([
                (0, 0), "{0}{1}/emote/{2}.png".format(_BASE_SPRITE_PATH, pose, emote)
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
        "ll": JNEyes.lookleft,
        "lr": JNEyes.lookright,
        "nm": JNEyes.normal,
        "pl": JNEyes.pleading,
        "sc": JNEyes.scared,
        "sk": JNEyes.shocked,
        "sg": JNEyes.smug,
        "sp": JNEyes.sparkle,
        "sq": JNEyes.squint,
        "sl": JNEyes.squintleft,
        "sr": JNEyes.squintright,
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
        "dr": JNMouth.drink,
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
        "tr": JNMouth.triangle,
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

    EMOTE_MAP = {
        "f": JNEmote.affection,
        "n": JNEmote.anger,
        "z": JNEmote.dazzle,
        "d": JNEmote.dread,
        "e": JNEmote.exclamation,
        "i": JNEmote.idea,
        "m": JNEmote.merry,
        "q": JNEmote.questionmark,
        "s": JNEmote.sad,
        "h": JNEmote.sigh,
        "k": JNEmote.shock,
        "l": JNEmote.sleepy,
        "o": JNEmote.somber,
        "p": JNEmote.speech,
        "u": JNEmote.surprise
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
        emote = None

        #If we still have an expcode, we know we have either tears, blush, or both
        while exp_code:
            exp_part = exp_code[0]
            exp_code = exp_code[1:]

            #Check if part is a tear
            if exp_part in TEARS_MAP:
                tears = exp_part

            #Otherwise it might be a blush
            elif exp_part in BLUSH_MAP:
                blush = exp_part

            # Finally, emote
            elif exp_part in EMOTE_MAP:
                emote = exp_part

        return {
            "pose": POSE_MAP[pose],
            "eyebrows": EYEBROW_MAP[eyebrows],
            "eyes": EYE_MAP[eyes],
            "mouth": MOUTH_MAP[mouth],
            "tears": TEARS_MAP.get(tears),
            "blush": BLUSH_MAP.get(blush),
            "emote": EMOTE_MAP.get(emote)
        }

    def _generate_image(exp_code):
        """
        Internal function to generate the image from the given expression code
        """
        #Parse the expression code and generate the displayable
        disp = jn_generate_natsuki_sprite(**_parse_exp_code(exp_code))

        #Get existing attrs to append this one to the known attrs
        _existing_attr_list = renpy.display.image.image_attributes["natsuki"]

        #Now add the displayable
        renpy.display.image.images[("natsuki", exp_code)] = disp

        #And finally update the attributes
        if exp_code not in _existing_attr_list:
            _existing_attr_list.append(exp_code)

    def _find_target_override(self):
        """
        This method tries to find an image by its reference. It can be a displayable or tuple.
        If this method can't find an image and it follows the pattern of Natsuki's sprites, it'll try to generate one.

        Main change to this function is the ability to auto generate displayables
        """
        name = self.name

        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True

        if not isinstance(name, tuple):
            name = tuple(name.split())

        def error(msg):
            self.target = renpy.text.text.Text(msg, color=(255, 0, 0, 255), xanchor=0, xpos=0, yanchor=0, ypos=0)

            if renpy.config.debug:
                raise Exception(msg)

        args = [ ]

        while name:
            target = renpy.display.image.images.get(name, None)

            if target is not None:
                break

            args.insert(0, name[-1])
            name = name[:-1]

        if not name:
            if (
                isinstance(self.name, tuple)
                and len(self.name) == 2
                and self.name[0] == "natsuki"
            ):
                #Reset name
                name = self.name
                #Generate
                _generate_image(name[1])
                #Try to get the img again
                target = renpy.display.image.images[name]

            else:
                error("Image '%s' not found." % ' '.join(self.name))
                return False

        try:
            a = self._args.copy(name=name, args=args)
            self.target = target._duplicate(a)

        except Exception as e:
            if renpy.config.debug:
                raise

            error(str(e))

        #Copy the old transform over.
        new_transform = self.target._target()

        if isinstance(new_transform, renpy.display.transform.Transform):
            if self.old_transform is not None:
                new_transform.take_state(self.old_transform)

            self.old_transform = new_transform

        else:
            self.old_transform = None

        return True

    renpy.display.image.ImageReference.find_target = _find_target_override

# Sprite code format:
# <pose><eyebrows><eyes><mouth><tears><blush><emote>
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
# ll - lookleft
# lr - lookright
# nm - normal
# pl - pleading
# sc - scared
# sk - shocked
# sg - smug
# sp - sparkle
# sq - squint
# sl - squint, left
# sr - squint, right
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
#
# <emote> - Emotion effects around Natsuki, E.G lightbulb representing an idea, etc.
# f - affection
# n - anger
# z - dazzle
# d - dread
# e - exclamation
# i - idea
# m - merry
# q - questionmark
# s - sad
# h - sigh
# k - shock
# l - sleepy
# o - somber
# p - speech
# u - surprise

#TODO: Fix shows without expressions showing silhouettes. They should show the current exp as normal.
#Only then can we delete these hardcoded exps.
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

# This selects which idle image to show based on current affinity state
image natsuki idle = ConditionSwitch(
    "jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED", "natsuki idle max_affinity",
    "jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE", "natsuki idle high_affinity",
    "jn_affinity.get_affinity_state() >= jn_affinity.NORMAL", "natsuki idle medium_affinity",
    "jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED", "natsuki idle low_affinity",
    "True", "natsuki idle min_affinity",
    predict_all = True
)

# Idle images for ENAMORED+
image natsuki idle max_affinity:
    block:
        choice:
            "natsuki 1nchsmf"
        choice:
            "natsuki 1kwmsmf"
        choice:
            "natsuki 1kllsmf"
        choice:
            "natsuki 1klrsmf"
        choice:
            "natsuki 1knmsmf"
        choice:
            "natsuki 1kcssmf"
        choice:
            "natsuki 1kcssgf"

        pause 10
        repeat

# Idle images for AFFECTIONATE+
image natsuki idle high_affinity:
    block:
        choice:
            "natsuki 1ullsml"
        choice:
            "natsuki 1ulrsml"
        choice:
            "natsuki 1unmsml"
        choice:
            "natsuki 1nnmsgl"

        pause 10
        repeat

# Idle images for NORMAL+
image natsuki idle medium_affinity:
    block:
        choice:
            "natsuki 1nllbo"
        choice:
            "natsuki 1nlrbo"
        choice:
            "natsuki 1nllpu"
        choice:
            "natsuki 1nlrpu"
        choice:
            "natsuki 1nllca"
        choice:
            "natsuki 1nlrca"
        choice:
            "natsuki 1nnmca"

        pause 10
        repeat

# Idle images for DISTRESSED+
image natsuki idle low_affinity:
    block:
        choice:
            "natsuki 1fllsl"
        choice:
            "natsuki 1klrsl"
        choice:
            "natsuki 1kcssl"
        choice:
            "natsuki 1kcssf"
        choice:
            "natsuki 1fcssf"
        choice:
            "natsuki 1fllsf"
        choice:
            "natsuki 1flrsf"
        choice:
            "natsuki 1fsqca"

        pause 10
        repeat

# Idle images for RUINED+
image natsuki idle min_affinity:
    block:
        choice:
            "natsuki 1fcsun"
        choice:
            "natsuki 1kcssr"
        choice:
            "natsuki 1fsqup"
        choice:
            "natsuki 1fsqun"
        choice:
            "natsuki 1kcsup"
        choice:
            "natsuki 1fcsup"

        pause 10
        repeat

# Idle images for the introduction sequence, after Natsuki and the player are introduced
image natsuki idle introduction:
    block:
        choice:
            "natsuki 1kllsr"
        choice:
            "natsuki 1klrsr"
        choice:
            "natsuki 1klrpu"
        choice:
            "natsuki 1kllpu"
        choice:
            "natsuki 1kcspu"
        choice:
            "natsuki 1kcssr"
        choice:
            "natsuki 1kcsun"
        choice:
            "natsuki 1kllun"
        choice:
            "natsuki 1klrun"
        pause 10
        repeat

init python:
    def show_natsuki_talk_menu():
        """
        Hack to work around renpy issue where the sprite is not refreshed when showing again
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            renpy.show("natsuki talk_menu_max_affinity", at_list=[jn_left])

        elif jn_affinity.get_affinity_state() >= jn_affinity.AFFECTIONATE:
            renpy.show("natsuki talk_menu_high_affinity", at_list=[jn_left])

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            renpy.show("natsuki talk_menu_medium_affinity", at_list=[jn_left])

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            renpy.show("natsuki talk_menu_low_affinity", at_list=[jn_left])

        else:
            renpy.show("natsuki talk_menu_min_affinity", at_list=[jn_left])

# Menu images for ENAMORED+
image natsuki talk_menu_max_affinity:
    block:
        choice:
            "natsuki 1nchbgl"
        choice:
            "natsuki 1nnmbgl"
        choice:
            "natsuki 1uchssl"
        choice:
            "natsuki 1unmssl"
        choice:
            "natsuki 1uwltsl"

# Menu images for AFFECTIONATE+
image natsuki talk_menu_high_affinity:
    block:
        choice:
            "natsuki 1unmsm"
        choice:
            "natsuki 1unmbg"
        choice:
            "natsuki 1uchbg"
        choice:
            "natsuki 1nchbg"

# Menu images for NORMAL+
image natsuki talk_menu_medium_affinity:
    block:
        choice:
            "natsuki 1unmss"
        choice:
            "natsuki 1unmaj"
        choice:
            "natsuki 1ulraj"
        choice:
            "natsuki 1ullaj"
        choice:
            "natsuki 1unmca"

# Menu images for DISTRESSED+
image natsuki talk_menu_low_affinity:
    block:
        choice:
            "natsuki 1fnmaj"
        choice:
            "natsuki 1fslaj"
        choice:
            "natsuki 1fsrbo"
        choice:
            "natsuki 1fcsbo"
        choice:
            "natsuki 1fcsaj"

# Menu images for RUINED+
image natsuki talk_menu_min_affinity:
    block:
        choice:
            "natsuki 1fcsan"
        choice:
            "natsuki 1fslem"
        choice:
            "natsuki 1fsrsf"
        choice:
            "natsuki 1fcssf"
        choice:
            "natsuki 1kcsan"
