init -50 python:
    import store
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils
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
        big_smile = 6
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
        small_frown = 26
        small_smile = 27
        smile = 28
        smirk = 29
        smug = 30
        tease = 31
        triangle = 32
        uneasy = 33
        upset = 34
        worried = 35
        blep = 36
        drink = 37

        def __str__(self):
            return self.name

    class JNEyes(Enum):
        baka = 1
        circle_tears = 2
        closed_happy = 3
        closed_sad = 4
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
        wink_left = 16
        wink_right = 17
        look_left = 18
        look_right = 19
        squint_left = 20
        squint_right = 21

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
        double_stream_closed = 1
        double_stream_narrow = 2
        double_stream_regular = 3
        dried = 4
        single_pooled_closed = 5
        single_pooled_narrow = 6
        single_pooled_regular = 7
        single_stream_closed = 8
        single_stream_narrow = 9
        single_stream_regular = 10
        spritz = 11
        wink_pooled_left = 12
        wink_pooled_right = 13

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
        question_mark = 8
        sad = 9
        sigh = 10
        shock = 11
        sleepy = 12
        somber = 13
        speech = 14
        surprise = 15
        laughter = 16
        sweat_drop = 17
        sweat_spritz = 18
        sweat_small = 19

        def __str__(self):
            return self.name

    class JNSweat(Enum):
        bead_left = 1
        bead_right = 2

        def __str__(self):
            return self.name

    def jn_generate_natsuki_sprite(
        pose,
        eyebrows,
        eyes,
        mouth,
        blush=None,
        tears=None,
        emote=None,
        sweat=None
    ):
        """
        Generates sprites for Natsuki based on outfit, expression, pose, etc.
        """
        lc_args = [
            (1280, 740), # Anchor
            (0, 0), _BASE_SPRITE_PATH + "desk/chair-normal.png", # Chair
            (0, 0), "{0}{1}/hair/[Natsuki._outfit.hairstyle.reference_name]/back.png".format(_BASE_SPRITE_PATH, pose), # Hair back
            (0, 0), "{0}{1}/base/body.png".format(_BASE_SPRITE_PATH, pose), # Body
            (0, 0), "{0}{1}/clothes/[Natsuki._outfit.clothes.reference_name]/body.png".format(_BASE_SPRITE_PATH, pose), # Outfit, body
        ]

        # Necklace
        necklace = Null() if not Natsuki._outfit.necklace else "{0}{1}/necklace/[Natsuki._outfit.necklace.reference_name]/{1}.png".format(_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), necklace
        ])

        # Head
        lc_args.extend([
            (0, 0), "{0}{1}/base/head.png".format(_BASE_SPRITE_PATH, pose),
        ])

        # Blush
        if blush:
            lc_args.extend([
                (0, 0), "{0}{1}/face/blush/{2}.png".format(_BASE_SPRITE_PATH, pose, blush)
            ])

        # Mouth, nose, hair (front)
        lc_args.extend([
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_BASE_SPRITE_PATH, pose, mouth),
            (0, 0), "{0}{1}/face/nose/nose.png".format(_BASE_SPRITE_PATH, pose),
            (0, 0), "{0}{1}/hair/[Natsuki._outfit.hairstyle.reference_name]/bangs.png".format(_BASE_SPRITE_PATH, pose),
        ])

        # Accessory
        accessory = Null() if not Natsuki._outfit.accessory else "{0}{1}/accessory/[Natsuki._outfit.accessory.reference_name]/{1}.png".format(_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), accessory
        ])

        # Eyes
        lc_args.extend([
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_BASE_SPRITE_PATH, pose, eyes), 
        ])

        # Tears
        if tears:
            lc_args.extend([
                (0, 0), "{0}{1}/face/tears/{2}.png".format(_BASE_SPRITE_PATH, pose, tears)
            ])

        # Sweat
        if sweat:
            renpy.notify("hit")
            lc_args.extend([
                (0, 0), "{0}{1}/face/sweat/{2}.png".format(_BASE_SPRITE_PATH, pose, sweat)
            ])

        # Headgear
        headgear = Null() if not Natsuki._outfit.headgear else "{0}{1}/headgear/[Natsuki._outfit.headgear.reference_name]/{1}.png".format(_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), headgear
        ])

        # Eyewear
        eyewear = Null() if not Natsuki._outfit.eyewear else "{0}{1}/eyewear/[Natsuki._outfit.eyewear.reference_name]/{1}.png".format(_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), eyewear
        ])

        # Emotes
        if emote:
            lc_args.extend([
                (0, 0), "{0}{1}/emote/{2}.png".format(_BASE_SPRITE_PATH, pose, emote)
            ])

        # Brows
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
        "1": JNPose.sitting
    }

    EYEBROW_MAP = {
        "n": JNEyebrows.normal,
        "u": JNEyebrows.up,
        "k": JNEyebrows.knit,
        "f": JNEyebrows.furrowed,
        "t": JNEyebrows.think
    }

    EYE_MAP = {
        "bk": JNEyes.baka,
        "ct": JNEyes.circle_tears,
        "ch": JNEyes.closed_happy,
        "cs": JNEyes.closed_sad,
        "cu": JNEyes.cute,
        "ll": JNEyes.look_left,
        "lr": JNEyes.look_right,
        "nm": JNEyes.normal,
        "pl": JNEyes.pleading,
        "sc": JNEyes.scared,
        "sk": JNEyes.shocked,
        "sg": JNEyes.smug,
        "sp": JNEyes.sparkle,
        "sq": JNEyes.squint,
        "sl": JNEyes.squint_left,
        "sr": JNEyes.squint_right,
        "un": JNEyes.unamused,
        "wm": JNEyes.warm,
        "wd": JNEyes.wide,
        "wl": JNEyes.wink_left,
        "wr": JNEyes.wink_right
    }

    MOUTH_MAP = {
        "aj": JNMouth.ajar,
        "an": JNMouth.angry,
        "aw": JNMouth.awe,
        "bg": JNMouth.big,
        "bs": JNMouth.big_smile,
        "bl": JNMouth.blep,
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
        "sf": JNMouth.small_frown,
        "ss": JNMouth.small_smile,
        "sg": JNMouth.smug,
        "ts": JNMouth.tease,
        "tr": JNMouth.triangle,
        "un": JNMouth.uneasy,
        "up": JNMouth.upset,
        "wr": JNMouth.worried
    }

    BLUSH_MAP = {
        "f": JNBlush.full,
        "l": JNBlush.light
    }

    TEARS_MAP = {
        "tda": JNTears.double_stream_closed,
        "tdb": JNTears.double_stream_narrow,
        "tdc": JNTears.double_stream_regular,
        "tdr": JNTears.dried,
        "tsa": JNTears.single_pooled_closed,
        "tsb": JNTears.single_pooled_narrow,
        "tsc": JNTears.single_pooled_regular,
        "tsd": JNTears.single_stream_closed,
        "tse": JNTears.single_stream_narrow,
        "tsf": JNTears.single_stream_regular,
        "tsz": JNTears.spritz,
        "twl": JNTears.wink_pooled_left,
        "twr": JNTears.wink_pooled_right
    }

    EMOTE_MAP = {
        "eaf": JNEmote.affection,
        "ean": JNEmote.anger,
        "edz": JNEmote.dazzle,
        "edr": JNEmote.dread,
        "eex": JNEmote.exclamation,
        "eid": JNEmote.idea,
        "elg": JNEmote.laughter,
        "eme": JNEmote.merry,
        "eqm": JNEmote.question_mark,
        "esd": JNEmote.sad,
        "esi": JNEmote.sigh,
        "esh": JNEmote.shock,
        "esl": JNEmote.sleepy,
        "eso": JNEmote.somber,
        "esp": JNEmote.speech,
        "esu": JNEmote.surprise,
        "esd": JNEmote.sweat_drop,
        "esz": JNEmote.sweat_spritz,
        "ess": JNEmote.sweat_small
    }

    SWEAT_MAP = {
        "sbl": JNSweat.bead_left,
        "sbr": JNSweat.bead_right
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
        sweat = None

        #If we still have an expcode, we know we have optional portions to process
        while exp_code:
            if exp_code[0] in BLUSH_MAP:
                exp_part = exp_code[0]
                exp_code = exp_code[1:]
                blush = exp_part

            else:
                if exp_code[:3] in TEARS_MAP:
                    tears = exp_code[:3]
                    exp_code = exp_code[3:]

                elif exp_code[:3] in EMOTE_MAP:
                    emote = exp_code[:3]
                    exp_code = exp_code[3:]

                elif exp_code[:3] in SWEAT_MAP:
                    sweat = exp_code[:3]
                    exp_code = exp_code[3:] 

                #To avoid an infinite loop, we'll raise another ValueError to note this format is invalid
                else:
                    raise ValueError(
                        "Invalid optional expression part: '{0}'. (All optional parts must follow mandatory ones)".format(exp_code)
                    )

        return {
            "pose": POSE_MAP[pose],
            "eyebrows": EYEBROW_MAP[eyebrows],
            "eyes": EYE_MAP[eyes],
            "mouth": MOUTH_MAP[mouth],
            "blush": BLUSH_MAP.get(blush),
            "tears": TEARS_MAP.get(tears),
            "emote": EMOTE_MAP.get(emote),
            "sweat": SWEAT_MAP.get(sweat)
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

        IN:
            - self - Reference to the calling narration statement, so we can access its args (name and spritecode)
        """
        name = self.name

        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True

        # Name is a tuple of (character_name, spritecode); we use these to determine displayable
        if not isinstance(name, tuple):
            name = tuple(name.split())

        def error(msg):
            """
            Sets the image target to a displayable (text) for a missing image.

            IN:
                - msg - The message to display for the fallback displayable
            """
            self.target = renpy.text.text.Text(
                msg,
                color=(255, 0, 0, 255),
                xanchor=0,
                xpos=0,
                yanchor=0,
                ypos=0
            )

            if renpy.config.debug:
                raise Exception(msg)

        args = [ ]

        while name:
            # Here, we are iterating through the characters of the spritecode and trying to find a 
            # pre-existing image for it to save generating every time, stopping if we find one.
            #
            # This also lets us check to make sure the narration isn't trying to use a hardcoded image
            target = renpy.display.image.images.get(name, None)

            if target is not None:
                break

            args.insert(0, name[-1])
            name = name[:-1]

        if not name:
            # We didn't find an image corresponding to the spritecode, or a hardcoded image, so we generate a new one
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
                # Image couldn't be generated
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

    # Finally, feed back to Ren'Py the image we actually want to display for the narration
    renpy.display.image.ImageReference.find_target = _find_target_override

# Sprite code format:
# <pose><eyebrows><eyes><mouth><blush><tears><emote><sweat>
#
# Pose, eyebrows, eyes and mouth are compulsary. Any others are optional.
#
# Some notes regarding lengths of each part:
#   pose: 1 character
#   eyebrows: 1 character
#   eyes: 2 characters
#   mouth: 2 characters
#   blush: 1 character
#   tears: 3 characters, t-prefix
#   emote: 3 characters, e-prefix
#   sweat: 3 characters, s-prefix
#
# For spritecode construction, use the previewer @ https://just-natsuki-team.github.io/Expression-Previewer/

# This selects which idle image to show based on current affinity state
image natsuki idle = ConditionSwitch(
    "Natsuki.isEnamored(higher=True)", "natsuki idle max_affinity",
    "Natsuki.isAffectionate(higher=True)", "natsuki idle high_affinity",
    "Natsuki.isNormal(higher=True)", "natsuki idle medium_affinity",
    "Natsuki.isDistressed(higher=True)", "natsuki idle low_affinity",
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
            "natsuki 1fcsuntsa"
        choice:
            "natsuki 1fcsantsa"
        choice:
            "natsuki 1fslantsb"
        choice:
            "natsuki 1fcssrtsa"
        choice:
            "natsuki 1kcssrtsa"
        choice:
            "natsuki 1ksrsrtsb"
        choice:
            "natsuki 1fsrantse"

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
        if Natsuki.isEnamored(higher=True):
            renpy.show("natsuki talk_menu_max_affinity", at_list=[jn_left])

        elif Natsuki.isAffectionate(higher=True):
            renpy.show("natsuki talk_menu_high_affinity", at_list=[jn_left])

        elif Natsuki.isNormal(higher=True):
            renpy.show("natsuki talk_menu_medium_affinity", at_list=[jn_left])

        elif Natsuki.isDistressed(higher=True):
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
            "natsuki 1fcsun"
        choice:
            "natsuki 1fslun"
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
            "natsuki 1fcsantsb"
        choice:
            "natsuki 1fsluntse"
        choice:
            "natsuki 1fcssrtse"
        choice:
            "natsuki 1fnmantdr"
