init -50 python:
    import store
    import store.jn_desk_items as jn_desk_items
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils
    from Enum import Enum

    _JN_NATSUKI_BASE_SPRITE_PATH = "mod_assets/natsuki/"
    _JN_TABLE_SPRITE = None

    class JNPose(Enum):
        sitting = 1
        arms_crossed_body = 2
        arms_crossed_desk = 3
        fingers_on_desk = 4
        finger_touching = 5
        pointy_finger = 6
        hand_on_chin = 7

        def __str__(self):
            return self.name

        def __int__(self):
            return self.value

    class JNBlush(Enum):
        full = 1
        light = 2
        ill = 3

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
        focus = 38
        flat_smile = 39
        cat_smug = 40
        flustered = 41
        grit_teeth = 42

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
        doubt = 22
        down = 23
        pained = 24
        up = 25
        think_left = 26
        think_right = 27
        down_left = 28
        down_right = 29
        peek_left = 30
        peek_right = 31

        def __str__(self):
            return self.name

    class JNEyebrows(Enum):
        normal = 1
        up = 2
        knit = 3
        furrowed = 4
        think = 5
        concerned = 6

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
        smug = 20

        def __str__(self):
            return self.name

    class JNSweat(Enum):
        bead_left = 1
        bead_right = 2

        def __str__(self):
            return self.name

    # These are poses with arms rendered under the desk
    _JN_BEFORE_DESK_POSES = [
        JNPose.sitting,
        JNPose.arms_crossed_body,
        JNPose.finger_touching
    ]

    # These are poses with arms rendered on top of the desk
    _JN_AFTER_DESK_POSES = [
        JNPose.arms_crossed_desk,
        JNPose.fingers_on_desk,
        JNPose.pointy_finger,
        JNPose.hand_on_chin
    ]

    def jnGenerateNatsukiSprite(
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

        # Base
        lc_args = [
            (1280, 740), # Anchor
            (0, 0), _JN_NATSUKI_BASE_SPRITE_PATH + "desk/chair/chair_normal.png", # Chair
            (0, 0), "{0}/hair/[Natsuki._outfit.hairstyle.reference_name]/sitting/back.png".format(_JN_NATSUKI_BASE_SPRITE_PATH), # Hair back
        ]

        # Back item
        back = "{0}/back/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.back else "{0}/back/[Natsuki._outfit.back.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), back
        ])

        # Base, clothes
        lc_args.extend([
            (0, 0), "{0}/base/{1}/body.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose), # Body
            (0, 0), "{0}/clothes/[Natsuki._outfit.clothes.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose), # Outfit, body
        ])

        # Necklace
        necklace = "{0}/necklace/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.necklace else "{0}/necklace/[Natsuki._outfit.necklace.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), necklace
        ])

        # Head
        lc_args.extend([
            (0, 0), "{0}/base/{1}/head.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
        ])

        # Blush
        if blush:
            lc_args.extend([
                (0, 0), "{0}/face/blush/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, blush)
            ])

        # Mouth, nose, hair (front)
        lc_args.extend([
            (0, 0), "{0}/face/mouth/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, mouth),
            (0, 0), "{0}/face/nose/sitting/nose.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        ])

        # Sweat
        if sweat:
            lc_args.extend([
                (0, 0), "{0}/face/sweat/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, sweat)
            ])

        # Hair (front)
        lc_args.extend([
            (0, 0), "{0}/hair/[Natsuki._outfit.hairstyle.reference_name]/sitting/bangs.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        ])

        # Accessory
        accessory = "{0}/accessory/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.accessory else "{0}/accessory/[Natsuki._outfit.accessory.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), accessory
        ])

        # Eyes
        lc_args.extend([
            (0, 0), "{0}/face/eyes/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, eyes), 
        ])

        # Tears
        if tears:
            lc_args.extend([
                (0, 0), "{0}/face/tears/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, tears)
            ])

        # Headgear
        headgear = "{0}/headgear/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.headgear else "{0}/headgear/[Natsuki._outfit.headgear.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), headgear
        ])

        # Facewear
        facewear = "{0}/facewear/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.facewear else "{0}/facewear/[Natsuki._outfit.facewear.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), facewear
        ])

        # Eyewear
        eyewear = "{0}/eyewear/jn_none/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH) if not Natsuki._outfit.eyewear else "{0}/eyewear/[Natsuki._outfit.eyewear.reference_name]/sitting.png".format(_JN_NATSUKI_BASE_SPRITE_PATH)
        lc_args.extend([
            (0, 0), eyewear
        ])

        # Brows
        lc_args.extend([
            (0, 0), "{0}/face/eyebrows/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, eyebrows)
        ])

        if pose in _JN_BEFORE_DESK_POSES:
            # Arms, sleeves
            lc_args.extend([
                (0, 0), "{0}/arms/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
                (0, 0), "{0}/sleeves/[Natsuki._outfit.clothes.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
            ])

        # Desk
        lc_args.extend([
            (0, 0), _JN_NATSUKI_BASE_SPRITE_PATH + "/desk/table/{0}.png".format(_JN_TABLE_SPRITE)           
        ])

        if pose in _JN_AFTER_DESK_POSES:
            # Arms, sleeves
            lc_args.extend([
                (0, 0), "{0}/desk/table_shadow/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
                (0, 0), "{0}/arms/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
                (0, 0), "{0}/sleeves/[Natsuki._outfit.clothes.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
            ])

        # Left desk item
        lc_args.extend([
            (0, 0), DynamicDisplayable(Natsuki.getDeskItemDisplayable, desk_slot=jn_desk_items.JNDeskSlots.left)
        ])
        # Centre desk item
        lc_args.extend([
            (0, 0), DynamicDisplayable(Natsuki.getDeskItemDisplayable, desk_slot=jn_desk_items.JNDeskSlots.centre)
        ])
        # Right desk item
        lc_args.extend([
            (0, 0), DynamicDisplayable(Natsuki.getDeskItemDisplayable, desk_slot=jn_desk_items.JNDeskSlots.right)
        ])

        # Emotes
        if emote:
            lc_args.extend([
                (0, 0), "{0}/emote/sitting/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, emote)
            ])

        # Generate and return the sprite
        return renpy.display.layout.LiveComposite(
            *lc_args
        )

init 1 python:
    import store

    POSE_MAP = {
        "1": JNPose.sitting,
        "2": JNPose.arms_crossed_body,
        "3": JNPose.arms_crossed_desk,
        "4": JNPose.fingers_on_desk,
        "5": JNPose.finger_touching,
        "6": JNPose.pointy_finger,
        "7": JNPose.hand_on_chin
    }

    EYEBROW_MAP = {
        "n": JNEyebrows.normal,
        "u": JNEyebrows.up,
        "k": JNEyebrows.knit,
        "f": JNEyebrows.furrowed,
        "t": JNEyebrows.think,
        "c": JNEyebrows.concerned
    }

    EYE_MAP = {
        "bk": JNEyes.baka,
        "ct": JNEyes.circle_tears,
        "ch": JNEyes.closed_happy,
        "cs": JNEyes.closed_sad,
        "cu": JNEyes.cute,
        "dt": JNEyes.doubt,
        "dw": JNEyes.down,
        "dl": JNEyes.down_left,
        "dr": JNEyes.down_right,
        "kl": JNEyes.peek_left,
        "kr": JNEyes.peek_right,
        "ll": JNEyes.look_left,
        "lr": JNEyes.look_right,
        "nm": JNEyes.normal,
        "pa": JNEyes.pained,
        "pl": JNEyes.pleading,
        "sc": JNEyes.scared,
        "sk": JNEyes.shocked,
        "sg": JNEyes.smug,
        "sp": JNEyes.sparkle,
        "sq": JNEyes.squint,
        "sl": JNEyes.squint_left,
        "sr": JNEyes.squint_right,
        "tl": JNEyes.think_left,
        "tr": JNEyes.think_right,
        "un": JNEyes.unamused,
        "up": JNEyes.up,
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
        "cs": JNMouth.cat_smug,
        "ct": JNMouth.catty,
        "dr": JNMouth.drink,
        "dv": JNMouth.devious,
        "em": JNMouth.embarrassed,
        "fl": JNMouth.flustered,
        "fo": JNMouth.focus,
        "fr": JNMouth.frown,
        "fs": JNMouth.flat_smile,
        "fu": JNMouth.furious,
        "gn": JNMouth.grin,
        "gs": JNMouth.gasp,
        "gt": JNMouth.grit_teeth,
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
        "l": JNBlush.light,
        "i": JNBlush.ill
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
        "esm": JNEmote.smug,
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
        disp = jnGenerateNatsukiSprite(**_parse_exp_code(exp_code))

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

    if Natsuki.isLove(higher=True):
        _JN_TABLE_SPRITE = "table_love"
        
    elif Natsuki.isEnamored(higher=True):
        _JN_TABLE_SPRITE = "table_enamored"

    elif Natsuki.isAffectionate(higher=True):
        _JN_TABLE_SPRITE = "table_affectionate"

    elif Natsuki.isUpset(higher=True):
        _JN_TABLE_SPRITE = "table_normal"

    elif Natsuki.isDistressed(higher=True):
        _JN_TABLE_SPRITE = "table_distressed"

    elif Natsuki.isBroken(higher=True):
        _JN_TABLE_SPRITE = "table_broken"

    elif Natsuki.isRuined(higher=True):
        _JN_TABLE_SPRITE = "table_ruined"

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

# Idle images for Natsuki playing her Twitch
image natsuki gaming:
    block:
        choice:
            "natsuki 1fdwfosbl"
            pause 3
            "natsuki 1fcsfosbl"
            pause 0.1

        choice:
            "natsuki 1fdwpusbr"
            pause 3

        choice:
            "natsuki 1fdwslsbl"
            pause 3
            "natsuki 1fcsslsbl"
            pause 0.1

        choice:
            "natsuki 1fdwcaesssbr"
            pause 3
            
        choice:
            "natsuki 1fdwsssbl"
            pause 3
            "natsuki 1fcssssbl"
            pause 0.1

    repeat

# Idle images for Natsuki falling - then remaining - asleep
image natsuki sleeping:
    # Falling asleep (4.1s)
    "natsuki 3nnmpu"
    pause 1
    "natsuki 3nsqpu"
    pause 2
    "natsuki 3ncspu"
    pause 0.2
    "natsuki 3nsqsl"
    pause 2
    "natsuki 3ncssl"
    pause 2

    # Sleeping loop
    block:
        "natsuki 3ncsflesl"
        pause 2
        "natsuki 3ncsemesl"
        pause 4
        "natsuki 3ncspuesl"
        pause 1

        repeat

# Idle images for Natsuki reading something
image natsuki reading:
    block:
        choice:
            "natsuki 1ndwbo"
            pause 3
            "natsuki 1ndwbo"
            pause 0.1
            "natsuki 1ndwbo"
            pause 4

        choice:
            "natsuki 1ndwpu"
            pause 3
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1ndwpu"
            pause 4

        choice:
            "natsuki 1udwsm"
            pause 3
            "natsuki 1ucssm"
            pause 0.1
            "natsuki 1udwsm"
            pause 2

        choice:
            "natsuki 1fdwpu"
            pause 3
            "natsuki 1fcspu"
            pause 0.1
            "natsuki 1fdwpu"
            pause 4

        choice:
            "natsuki 1ndwfs"
            pause 3
            "natsuki 1ncsfs"
            pause 0.1
            "natsuki 1ndwfs"
            pause 4

        choice:
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1cdrbo", "True", "natsuki 1cdlbo", predict_all=True)
            pause 3
            "natsuki 1cdwbo"
            pause 3
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1cdlbo", "True", "natsuki 1cdrbo", predict_all=True)
            pause 3
            "natsuki 1ccsbo"
            pause 0.1
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1cdlbo", "True", "natsuki 1cdrbo", predict_all=True)
            pause 3
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1cdrbo", "True", "natsuki 1cdlbo", predict_all=True)
            pause 3
            "natsuki 1cdwbo"
            pause 3
            "natsuki 1ccsbo"
            pause 0.1

        choice:
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1udrsm", "True", "natsuki 1udlsm", predict_all=True)
            pause 3
            "natsuki 1udwsm"
            pause 3
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1udlsm", "True", "natsuki 1udrsm", predict_all=True)
            pause 3
            "natsuki 1ucssm"
            pause 0.1
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1udlsm", "True", "natsuki 1udrsm", predict_all=True)
            pause 3
            ConditionSwitch("Natsuki.getIsReadingToRight()", "natsuki 1udrsm", "True", "natsuki 1udlsm", predict_all=True)
            pause 3
            "natsuki 1udwsm"
            pause 3
            "natsuki 1ucssm"
            pause 0.1

    repeat

# Idle images for Natsuki daydreaming/in thought
image natsuki thinking:
    block:
        choice:
            "natsuki 7tupbo"
            pause 4
            "natsuki 7tcsbo"
            pause 0.1
            "natsuki 7tupbo"
            pause 1
            "natsuki 7tcsbo"
            pause 0.1
            "natsuki 7tupbo"
            pause 4
            "natsuki 7tcsbo"
            pause 0.1

        choice:
            "natsuki 2tllbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1
            "natsuki 2tllbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1

        choice:
            "natsuki 4tlrbo"
            pause 4
            "natsuki 4tcsbo"
            pause 0.1
            "natsuki 4tlrbo"
            pause 4
            "natsuki 4tcsbo"
            pause 0.1
    
        choice:
            "natsuki 7tsrpu"
            pause 4
            "natsuki 7tcspu"
            pause 0.1
            "natsuki 7tsrpu"
            pause 3
            "natsuki 7fsrpu"
            pause 3
            "natsuki 7fcspu"
            pause 0.1
            "natsuki 7tsrsl"
            pause 5
            "natsuki 7tcssl"
            pause 0.1

    repeat

# Idle images for Natsuki vibing/listening to music
image natsuki vibing:
    block:
        choice:
            "natsuki 1ncssm"
        choice:
            "natsuki 2fcssm"
        choice:
            "natsuki 4fcssm"
        choice:
            "natsuki 2fchsm"
        choice:
            "natsuki 4fchsm"
        choice:
            "natsuki 2fcsss"
            pause 0.75
            "natsuki 2fcsaj"
            pause 0.75
            "natsuki 2fcsbs"
            pause 0.75
            "natsuki 2fcsss"
            pause 0.75
            "natsuki 2fchsm"
        choice:
            "natsuki 1fcspu"
        choice:
            "natsuki 1fcssl"
        choice:
            "natsuki 1fcsca"
        choice:
            "natsuki 1fcssl"
            pause 0.75
            "natsuki 1fcsaj"
            pause 0.75
            "natsuki 1fcssl"
            pause 0.75
            "natsuki 1fcsaj"
            pause 0.75
            "natsuki 1fcsca"
    pause 8
    repeat

image natsuki whistling:
    block:
        choice:
            "natsuki 3nllpueme"
            pause 0.75
            "natsuki 3nllajeme"
            pause 0.75
            "natsuki 3nllpueme"
            pause 0.75
            "natsuki 3nllajeme"
            pause 0.75
            "natsuki 3nllboeme"
            pause 0.75
            "natsuki 3ncsboeme"
            pause 0.1
            "natsuki 3nllajeme"
            pause 0.75
            "natsuki 3nllpueme"
            pause 0.75
            "natsuki 3ullbo"
            pause 4
            "natsuki 3ucsboeme"
            pause 0.1
        choice:
            "natsuki 3nlrpueme"
            pause 0.75
            "natsuki 3nlrajeme"
            pause 0.75
            "natsuki 3nlrpueme"
            pause 0.75
            "natsuki 3nlrajeme"
            pause 0.75
            "natsuki 3nlrboeme"
            pause 0.75
            "natsuki 3ncsboeme"
            pause 0.1
            "natsuki 3nlrajeme"
            pause 0.75
            "natsuki 3nlrpueme"
            pause 0.75
            "natsuki 3ulrbo"
            pause 4
            "natsuki 3ucsboeme"
            pause 0.1
        choice:
            "natsuki 3utlajeme"
            pause 0.75
            "natsuki 3utlpueme"
            pause 0.75
            "natsuki 3ucspueme"
            pause 0.1
            "natsuki 3utlajeme"
            pause 0.75
            "natsuki 3utlsl"
            pause 4
        choice:
            "natsuki 3utrpueme"
            pause 0.75
            "natsuki 3utrajeme"
            pause 0.75
            "natsuki 3ucsajeme"
            pause 0.1
            "natsuki 3utrpueme"
            pause 0.75
            "natsuki 3utrsl"
            pause 4
    repeat

# Idle images for Natsuki working_on_papers
image natsuki working_on_papers:
    block:
        choice:
            "natsuki 2tupbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1
            "natsuki 2tupbo"
            pause 1
            "natsuki 2tcsbo"
            pause 0.1
            "natsuki 2tupbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1

        choice:
            "natsuki 2tllbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1
            "natsuki 2tllbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1

        choice:
            "natsuki 4tlrbo"
            pause 4
            "natsuki 4tcsbo"
            pause 0.1
            "natsuki 4tlrbo"
            pause 4
            "natsuki 4tcsbo"
            pause 0.1
    
        choice:
            "natsuki 2tsrpu"
            pause 4
            "natsuki 2tcspu"
            pause 0.1
            "natsuki 2tsrpu"
            pause 3
            "natsuki 2fsrpu"
            pause 3
            "natsuki 2fcspu"
            pause 0.1
            "natsuki 2tsrsl"
            pause 5
            "natsuki 2tcssl"
            pause 0.1

    repeat

image natsuki snap:
    block:
        choice:
            "natsuki 4csqsm"
            pause 4
            "natsuki 4ccssm"
            pause 0.1
            "natsuki 4csqsm"
            pause 4
            "natsuki 4ccssm"
            pause 0.1
        choice:
            "natsuki 7fsqsm"
            pause 4
            "natsuki 7fcssm"
            pause 0.1
            "natsuki 7fsqsm"
            pause 4
            "natsuki 7fcssm"
            pause 0.1
        choice:
            "natsuki 1flrss"
            pause 4
            "natsuki 1fcsss"
            pause 0.1
            "natsuki 1flrss"
            pause 4
            "natsuki 1fcsss"
            pause 0.1
        choice:
            "natsuki 1flrpu"
            pause 4
            "natsuki 1fcspu"
            pause 0.1
            "natsuki 1flrpu"
            pause 4
            "natsuki 1fcspu"
            pause 0.1
        choice:
            "natsuki 4flrpu"
            pause 4
            "natsuki 4fcspu"
            pause 0.1
            "natsuki 4flrpu"
            pause 4
            "natsuki 4fcspu"
            pause 0.1

    repeat

image natsuki option_wait_excited:
    block:
        choice:
            "natsuki 4unmbg"
            pause 4
            "natsuki 4ucsbg"
            pause 0.1
            "natsuki 4unmbg"
            pause 4
            "natsuki 4ucsbg"
            pause 0.1

        choice:
            "natsuki 4unmsm"
            pause 4
            "natsuki 4ucssm"
            pause 0.1
            "natsuki 4unmsm"
            pause 4
            "natsuki 4ucssm"
            pause 0.1

        choice:
            "natsuki 4unmss"
            pause 4
            "natsuki 4ucsss"
            pause 0.1
            "natsuki 4unmss"
            pause 4
            "natsuki 4ucsss"
            pause 0.1

    repeat

image natsuki option_wait_curious:
    block:
        choice:
            "natsuki 2tnmbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1
            "natsuki 2tnmbo"
            pause 4
            "natsuki 2tcsbo"
            pause 0.1

        choice:
            "natsuki 2unmbo"
            pause 4
            "natsuki 2ucsbo"
            pause 0.1
            "natsuki 2unmbo"
            pause 4
            "natsuki 2ucsbo"
            pause 0.1

        choice:
            "natsuki 7unmbo"
            pause 4
            "natsuki 7ucsbo"
            pause 0.1
            "natsuki 7unmbo"
            pause 4
            "natsuki 7ucsbo"
            pause 0.1

    repeat

image natsuki option_wait_smug:
    block:
        choice:
            "natsuki 2tsqsm"
            pause 4
            "natsuki 2tcssm"
            pause 0.1
            "natsuki 2tsqsm"
            pause 4
            "natsuki 2tcssm"
            pause 0.1

        choice:
            "natsuki 4tsqcs"
            pause 4
            "natsuki 4tcscs"
            pause 0.1
            "natsuki 2tsqcs"
            pause 4
            "natsuki 2tcscs"
            pause 0.1

        choice:
            "natsuki 7tsqsm"
            pause 4
            "natsuki 7tcssm"
            pause 0.1
            "natsuki 7tsqsm"
            pause 4
            "natsuki 7tcssm"
            pause 0.1

        choice:
            "natsuki 7csqcs"
            pause 4
            "natsuki 7ccscs"
            pause 0.1
            "natsuki 7csqcs"
            pause 4
            "natsuki 7ccscs"

    repeat

image natsuki option_wait_holding:
    block:
        choice:
            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1

        choice:
            "natsuki 1tlrbo"
            pause 4
            "natsuki 1tcsbo"
            pause 0.1
            "natsuki 1tlrbo"
            pause 4
            "natsuki 1tcsbo"
            pause 0.1

        choice:
            "natsuki 1tnmbo"
            pause 4
            "natsuki 1tcsbo"
            pause 0.1
            "natsuki 1tnmbo"
            pause 4
            "natsuki 1tcsbo"
            pause 0.1

        choice:
            "natsuki 1unmbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1unmbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1unmbo"
            pause 1
            "natsuki 1ucsbo"
            pause 0.1

    repeat

image natsuki option_wait_sulky:
    block:
        choice:
            "natsuki 2csqca"
            pause 4
            "natsuki 2ccsca"
            pause 0.1
            "natsuki 2csqca"
            pause 4
            "natsuki 2ccsca"
            pause 0.1

        choice:
            "natsuki 5cslca"
            pause 4
            "natsuki 5ccsca"
            pause 0.1
            "natsuki 5cslca"
            pause 4
            "natsuki 5ccsca"
            pause 0.1

        choice:
            "natsuki 2ccspo"
            pause 4
            "natsuki 2fcspo"
            pause 4

        choice:
            "natsuki 2ccsca"
            pause 6

        choice:
            "natsuki 2csrbo"
            pause 4
            "natsuki 2ccsbo"
            pause 0.1
            "natsuki 2csrbo"
            pause 4
            "natsuki 2ccsbo"
            pause 0.1

    repeat

image natsuki idle = Natsuki.getIdleImageTagsForAffinity()

# Idle images for ENAMORED+
image natsuki idle enamored:
    block:
        choice:
            "natsuki 5csqsml"
            pause 1
            "natsuki 5ccssml"
            pause 0.1
            "natsuki 5csqsml"
            pause 3
            "natsuki 3fchbll"
            pause 1
            "natsuki 3fchsml"
            pause 3

        choice:
            "natsuki 7tsqsml"
            pause 1
            "natsuki 7tcssml"
            pause 0.1
            "natsuki 7tsqsml"
            pause 3
            "natsuki 7fchsml"
            pause 3

        choice:
            "natsuki 1nchsmf"
            pause 10

        choice:
            "natsuki 4kwmsmf"
            pause 5
            "natsuki 4kcssmf"
            pause 0.1
            "natsuki 4kwmsmf"
            pause 5
            "natsuki 4kcssmf"
            pause 0.1

        choice:
            "natsuki 3kllsmf"
            pause 5
            "natsuki 3kcssmf"
            pause 0.1
            "natsuki 3kllsmf"
            pause 5
            "natsuki 3kcssmf"
            pause 0.1

        choice:
            "natsuki 4klrsmf"
            pause 5
            "natsuki 4kcssmf"
            pause 0.1
            "natsuki 4klrsmf"
            pause 5
            "natsuki 4kcssmf"
            pause 0.1

        choice:
            "natsuki 1knmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1knmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1

        choice:
            "natsuki 1kcssmf"
            pause 10

        choice:
            "natsuki 2kcssgf"
            pause 10

        choice:
            "natsuki 1kllsmf"
            pause 2
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1knmsmf"
            pause 3
            "natsuki 4fsqsmf"
            pause 3
            "natsuki 4fchblf"
            pause 1
            "natsuki 2fchgnf"
            pause 2
            "natsuki 2klrsmf"
            pause 2
            "natsuki 2kcssmf"
            pause 0.1

        choice:
            "natsuki 2kcssmf"
            pause 3
            "natsuki 2kcsssf"
            pause 3
            "natsuki 2kcssmf"
            pause 5

        choice:
            "natsuki 1nlrpul"
            pause 3
            "natsuki 1ncspul"
            pause 0.1
            "natsuki 3flrpul"
            pause 3
            "natsuki 3ncspul"
            pause 0.1
            "natsuki 3tnmpul"
            pause 1
            "natsuki 3unmpulesu"
            pause 1.5
            "natsuki 3fcspul"
            pause 0.1
            "natsuki 5fllcsfsbl"
            pause 4
            "natsuki 5fcscsf"
            pause 0.1

        choice:
            "natsuki 3uchsmfedz"
            pause 7

        choice:
            "natsuki 3nchsmfeme"
            pause 7

        repeat

# Idle images for AFFECTIONATE+
image natsuki idle affectionate:
    block:
        choice:
            "natsuki 3unmcsl"
            pause 1
            "natsuki 3ucscsl"
            pause 0.1
            "natsuki 3unmcsl"
            pause 3
            "natsuki 3ucscsl"
            pause 0.1
            "natsuki 4cslfslsbr"
            pause 4
            "natsuki 4ccsfslsbr"
            pause 0.1

        choice:
            "natsuki 3ullcsl"
            pause 5
            "natsuki 3ucscsl"
            pause 0.1
            "natsuki 3ullcsl"
            pause 5
            "natsuki 3ucscsl"
            pause 0.1

        choice:
            "natsuki 3ullsml"
            pause 5
            "natsuki 3ucssml"
            pause 0.1
            "natsuki 3ullsml"
            pause 5
            "natsuki 3ucssml"
            pause 0.1

        choice:
            "natsuki 4ulrsml"
            pause 5
            "natsuki 4ucssml"
            pause 0.1
            "natsuki 4ulrsml"
            pause 0.25
            "natsuki 4ucssml"
            pause 0.1
            "natsuki 4ulrsml"
            pause 5
            "natsuki 4ucssml"
            pause 0.1

        choice:
            "natsuki 1unmsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
            "natsuki 1unmsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1

        choice:
            "natsuki 1nllbol"
            pause 4
            "natsuki 2fllbol"
            pause 4
            "natsuki 2fcsbol"
            pause 0.1
            "natsuki 2tnmbol"
            pause 4
            "natsuki 2tcsbol"
            pause 0.1
            "natsuki 4fsqsml"
            pause 4
            "natsuki 4fwlsml"
            pause 0.5
            "natsuki 4flldvl"
            pause 2
            "natsuki 4fcsdvl"
            pause 0.1

        choice:
            "natsuki 7nllpul"
            pause 3
            "natsuki 7ncspul"
            pause 0.1
            "natsuki 7fllpul"
            pause 5
            "natsuki 7ncspul"
            pause 0.1
            "natsuki 7tnmpul"
            pause 4
            "natsuki 7tcspul"
            pause 0.1
            "natsuki 4flrdvless"
            pause 4
            "natsuki 4fcsdvl"
            pause 0.1

        repeat

# Idle images for HAPPY+
image natsuki idle happy:
    block:
        choice:
            "natsuki 3unmbo"
            pause 1
            "natsuki 3ucsbo"
            pause 0.1
            "natsuki 3unmbo"
            pause 3
            "natsuki 3ucsbo"
            pause 0.1
            "natsuki 4csrcalsbr"
            pause 4
            "natsuki 4ccscalsbr"
            pause 0.1

        choice:
            "natsuki 3ullbo"
            pause 4
            "natsuki 3ucsbo"
            pause 0.1
            "natsuki 3ullbo"
            pause 4
            "natsuki 3ucsbo"
            pause 0.1

        choice:
            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1

        choice:
            "natsuki 2ullfs"
            pause 4
            "natsuki 2ucsfs"
            pause 0.1
            "natsuki 2ullfs"
            pause 4
            "natsuki 2ucsfs"
            pause 0.1

        choice:
            "natsuki 4ulrfs"
            pause 4
            "natsuki 4ucsfs"
            pause 0.1
            "natsuki 4ulrfs"
            pause 4
            "natsuki 4ucsfs"
            pause 0.1

        choice:
            "natsuki 1ullca"
            pause 4
            "natsuki 1ucsca"
            pause 0.1
            "natsuki 1tllca"
            pause 4
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tllca"
            pause 2
            "natsuki 1tnmpu"
            pause 2
            "natsuki 1tcspu"
            pause 0.1
            "natsuki 1unmpul"
            pause 2
            "natsuki 1ucspul"
            pause 0.1
            "natsuki 1fcspolsbl"
            pause 4

        choice:
            "natsuki 1tslca"
            pause 4
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tslca"
            pause 1
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tsqca"
            pause 2
            "natsuki 1unmpul"
            pause 2
            "natsuki 1ucspul"
            pause 0.1
            "natsuki 2fslsmlsbl"
            pause 3
            "natsuki 2fcssmlsbl"
            pause 0.1

        choice:
            "natsuki 2ulrcal"
            pause 4
            "natsuki 2ucscal"
            pause 0.1
            "natsuki 2ulrcal"
            pause 4
            "natsuki 2ucscal"
            pause 0.1

        choice:
            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1

        choice:
            "natsuki 2ullfs"
            pause 4
            "natsuki 2ucsfs"
            pause 0.1
            "natsuki 2ulrfs"
            pause 4
            "natsuki 2ucsfs"
            pause 0.1

        repeat

# Idle images for NORMAL+
image natsuki idle normal:
    block:
        choice:
            "natsuki 2unmca"
            pause 1
            "natsuki 2ucsca"
            pause 0.1
            "natsuki 2unmca"
            pause 3
            "natsuki 2ucsca"
            pause 0.1
            "natsuki 2nllbosbl"
            pause 4
            "natsuki 2ncsbosbl"
            pause 0.1

        choice:
            "natsuki 2nllbo"
            pause 4
            "natsuki 2ncsbo"
            pause 0.1
            "natsuki 2nllbo"
            pause 4
            "natsuki 2ncsbo"
            pause 0.1

        choice:
            "natsuki 2nlrbo"
            pause 4
            "natsuki 2ncsbo"
            pause 0.1
            "natsuki 2nlrbo"
            pause 4
            "natsuki 2ncsbo"
            pause 0.1

        choice:
            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1

        choice:
            "natsuki 2nlrpu"
            pause 4
            "natsuki 2ncspu"
            pause 0.1
            "natsuki 2nlrpu"
            pause 4
            "natsuki 2ncspu"
            pause 0.1

        choice:
            "natsuki 2nllca"
            pause 4
            "natsuki 2ncsca"
            pause 0.1
            "natsuki 2nllca"
            pause 4
            "natsuki 2ncsca"
            pause 0.1

        choice:
            "natsuki 4nlrca"
            pause 4
            "natsuki 4ncsca"
            pause 0.1
            "natsuki 4nlrca"
            pause 4
            "natsuki 4ncsca"
            pause 0.1

        choice:
            "natsuki 2nnmca"
            pause 4
            "natsuki 2ncsca"
            pause 0.1
            "natsuki 2nnmca"
            pause 4
            "natsuki 2ncsca"
            pause 0.1

        choice:
            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1nlrpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1

        repeat

# Idle images for DISTRESSED+
image natsuki idle distressed:
    block:
        choice:
            "natsuki 2fllsl"
            pause 3
            "natsuki 2fcssl"
            pause 0.1

        choice:
            "natsuki 2flrsl"
            pause 3
            "natsuki 2fcssl"
            pause 0.1

        choice:
            "natsuki 1kcssl"
            pause 8

        choice:
            "natsuki 1kcssf"
            pause 8

        choice:
            "natsuki 2fcssf"
            pause 8

        choice:
            "natsuki 2fllsf"
            pause 3
            "natsuki 2fcssf"
            pause 0.1

        choice:
            "natsuki 2flrsf"
            pause 3
            "natsuki 2fcssf"
            pause 0.1

        choice:
            "natsuki 2fsqca"
            pause 3
            "natsuki 2fcsca"
            pause 0.1

        repeat

# Idle images for RUINED+
image natsuki idle ruined:
    block:
        choice:
            "natsuki 1fcsuntsa"
        choice:
            "natsuki 4fcsantsa"
        choice:
            "natsuki 4fslantsb"
        choice:
            "natsuki 2fcssrtsa"
        choice:
            "natsuki 4kcssrtsa"
        choice:
            "natsuki 1ksrsrtsb"
        choice:
            "natsuki 4fsrantse"

        pause 4
        repeat

# Idle images for the introduction sequence, after Natsuki and the player are introduced
image natsuki idle introduction:
    block:
        choice:
            "natsuki 4kllsr"
        choice:
            "natsuki 4klrsr"
        choice:
            "natsuki 2klrpu"
        choice:
            "natsuki 2kllpu"
        choice:
            "natsuki 1kcspu"
        choice:
            "natsuki 1kcssr"
        choice:
            "natsuki 1kcsun"
        choice:
            "natsuki 4kllun"
        choice:
            "natsuki 4klrun"
        pause 10
        repeat

image natsuki idle fluster:
    block:
        choice:
            "natsuki 1cllunlsbr"
            pause 2
            "natsuki 1ccsunlsbr"
            pause 0.1
            "natsuki 1clrunlsbr"
            pause 2
            "natsuki 1ccsunlsbr"
            pause 0.1

        choice:
            "natsuki 1clremlsbl"
            pause 2
            "natsuki 1ccsemlsbl"
            pause 0.1
            "natsuki 1cllemlsbl"
            pause 2
            "natsuki 1ccsemlsbl"
            pause 0.1

        choice:
            "natsuki 1cllfllsbr"
            pause 2
            "natsuki 1ccsfllsbr"
            pause 0.1
            "natsuki 1clrfllsbr"
            pause 2
            "natsuki 1ccsfllsbl"
            pause 0.1
            "natsuki 1clrfllsbl"
            pause 1.25
            "natsuki 1ccsfllsbl"
            pause 0.1
        repeat

init python:
    import random

    def jnShowNatsukiIdle(position, zorder=store.JN_NATSUKI_ZORDER):
        """
        Shows the appropriate Natsuki idle sprite based on the current affinity level.
        Avoids having to use a condition switch to constantly check and update the sprite,
        which is extremely expensive in CPU cycles.
        """
        renpy.show(Natsuki.getIdleImageTagsForAffinity(), at_list=[position], zorder=zorder)

    def jnShowNatsukiTalkMenu():
        """
        Shows the appropriate Natsuki sprite for the talk menu based on the current affinity level.
        Hack to work around Ren'Py issue where the sprite is not refreshed when showing again.
        """
        if Natsuki.isEnamored(higher=True):
            renpy.show("natsuki talk_menu_enamored", at_list=[jn_left])

        elif Natsuki.isAffectionate(higher=True):
            renpy.show("natsuki talk_menu_affectionate", at_list=[jn_left])

        elif Natsuki.isHappy(higher=True):
            renpy.show("natsuki talk_menu_happy", at_list=[jn_left])

        elif Natsuki.isNormal(higher=True):
            renpy.show("natsuki talk_menu_normal", at_list=[jn_left])

        elif Natsuki.isDistressed(higher=True):
            renpy.show("natsuki talk_menu_distressed", at_list=[jn_left])

        else:
            renpy.show("natsuki talk_menu_ruined", at_list=[jn_left])

    def jnGetNatsukiRandomStaticIdleSprite():
        """
        Returns a random idle sprite code based on the current affinity level.
        Hack to work around Ren'Py issue speeding up Nat's idle animation when a weather Dissolve transition took place.
        """
        if Natsuki.isEnamored(higher=True):
            return random.choice([
                "5csqsml",
                "7tsqsml",
                "1nchsmf",
                "4kwmsmf",
                "3kllsmf",
                "4klrsmf",
                "1knmsmf",
                "1kcssmf",
                "2kcssgf",
                "1kllsmf",
                "2kcssmf",
                "3uchsmfedz",
                "3nchsmfeme"
            ])

        elif Natsuki.isAffectionate(higher=True):
            return random.choice([
                "3unmcsl",
                "3ullcsl",
                "3ulrcsl",
                "3ullsml",
                "4ulrsml",
                "1unmsml",
                "1nllbol",
                "7nllpul"
            ])

        elif Natsuki.isHappy(higher=True):
            return random.choice([
                "3unmbo",
                "3ullbo",
                "1ulrbo",
                "2ullfs",
                "4ulrfs",
                "2ulrcal",
                "1nnmca",
                "2ullfs"
            ])

        elif Natsuki.isNormal(higher=True):
            return random.choice([
                "2unmca",
                "2nllbo",
                "2nlrbo",
                "1nllpu",
                "2nlrpu",
                "2nllca",
                "4nlrca",
                "2nnmca",
                "1nllpu"
            ])

        elif Natsuki.isDistressed(higher=True):
            return random.choice([
                "2fllsl",
                "2flrsl",
                "1kcssl",
                "1kcssf",
                "2fcssf",
                "2fllsf",
                "2flrsf",
                "2fsqca"
            ])

        else:
            return random.choice([
                "1fcsuntsa",
                "4fcsantsa",
                "4fslantsb",
                "2fcssrtsa",
                "4kcssrtsa",
                "1ksrsrtsb",
                "4fsrantse"
            ])

# Menu images for ENAMORED+
image natsuki talk_menu_enamored:
    block:
        choice:
            "natsuki 3nchbgl"
            pause 4
            repeat

        choice:
            "natsuki 4nnmbgl"
            pause 4
            "natsuki 4ncsbgl"
            pause 0.1
            repeat

        choice:
            "natsuki 3uchssl"
            pause 4
            repeat

        choice:
            "natsuki 3unmssl"
            pause 4
            "natsuki 3ucsssl"
            pause 0.1
            repeat

        choice:
            "natsuki 4uwltsl"
            pause 4
            "natsuki 4ucstsl"
            pause 0.1
            repeat

        choice:
            "natsuki 4fchbgl"
            pause 4
            repeat

        choice:
            "natsuki 3fchsml"
            pause 4
            repeat

        choice:
            "natsuki 7fchbgl"
            pause 4
            repeat

        choice:
            "natsuki 7fchsml"
            pause 4
            repeat

# Menu images for AFFECTIONATE+
image natsuki talk_menu_affectionate:
    block:
        choice:
            "natsuki 3unmsm"
            pause 4
            "natsuki 3ucssm"
            pause 0.1
            repeat

        choice:
            "natsuki 1unmbg"
            pause 4
            "natsuki 1ucsbg"
            pause 0.1
            repeat
        
        choice:
            "natsuki 4uchbg"

        choice:
            "natsuki 2nchbg"

        choice:
            "natsuki 2tchbg"

        choice:
            "natsuki 3tsqsm"
            pause 4
            "natsuki 3tcssm"
            pause 0.1
            repeat

        choice:
            "natsuki 7nchbg"

        choice:
            "natsuki 7tsqsm"
            pause 4
            "natsuki 7tcssm"
            pause 0.1
            repeat

# Menu images for HAPPY+
image natsuki talk_menu_happy:
    block:
        choice:
            "natsuki 1unmss"
            pause 4
            "natsuki 1ucsss"
            pause 0.1
            repeat

        choice:
            "natsuki 2unmfs"
            pause 4
            "natsuki 2ucsfs"
            pause 0.1
            repeat

        choice:
            "natsuki 2tnmfs"
            pause 4
            "natsuki 2tcsfs"
            pause 0.1
            repeat

        choice:
            "natsuki 4ullaj"
            pause 4
            "natsuki 4ucsaj"
            pause 0.1
            repeat

        choice:
            "natsuki 4unmbo"
            pause 4
            "natsuki 4ucsbo"
            pause 0.1
            repeat

# Menu images for NORMAL+
image natsuki talk_menu_normal:
    block:
        choice:
            "natsuki 1unmss"
            pause 4
            "natsuki 1ucsss"
            pause 0.1
            repeat

        choice:
            "natsuki 2unmaj"
            pause 4
            "natsuki 2ucsaj"
            pause 0.1
            repeat

        choice:
            "natsuki 2ulraj"
            pause 4
            "natsuki 2ucsaj"
            pause 0.1
            repeat

        choice:
            "natsuki 1ullaj"
            pause 4
            "natsuki 1ucsaj"
            pause 0.1
            repeat

        choice:
            "natsuki 2unmca"
            pause 4
            "natsuki 2ucsca"
            pause 0.1
            repeat

# Menu images for DISTRESSED+
image natsuki talk_menu_distressed:
    block:
        choice:
            "natsuki 2fcsun"

        choice:
            "natsuki 2fslun"
            pause 6
            "natsuki 2fcsun"
            pause 0.1
            repeat

        choice:
            "natsuki 2fsrbo"
            pause 6
            "natsuki 2fcsbo"
            pause 0.1
            repeat

        choice:
            "natsuki 2fcsbo"

        choice:
            "natsuki 2fcsaj"

# Menu images for RUINED+
image natsuki talk_menu_ruined:
    block:
        choice:
            "natsuki 2fcsantsb"

        choice:
            "natsuki 2fsluntse"
            pause 8
            "natsuki 2fcsuntsd"
            pause 0.1
            repeat

        choice:
            "natsuki 2fcssrtse"

        choice:
            "natsuki 2fnmantdr"
            pause 8
            "natsuki 2fcsantsa"
            pause 0.1
            repeat

image desk = "mod_assets/natsuki/desk/table/table_normal.png"
image chair = "mod_assets/natsuki/desk/chair/chair_normal.png"
