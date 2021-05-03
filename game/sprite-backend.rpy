#well here goes nothing..
#
## SPRITECODE SYSTEM
# natsuki 1_n_n_g_bl
#   - Default pose (1)
#   - Normal Eyebrows (n)
#   - Normal eyes (n)
#   - Grin mouth (g)
#   - Light blush (bl)

# TODO: Map all sprites to letter codes
# Finish building the Transform representing Natsuki's sprites
# Build clothes as an object
# Build accessories as an object

default persistent._clothes = "uniform"

init python:
    from enum import Enum

    SPR_PATH_SIT = "mod_assets/natsuki/sitting/"
    SPR_PATH_STAND = "mod_assets/natsuki/standing/"

    #Enums for different sprite parts
    class Pose(Enum):
        """
        Enum representing pose
        """
        default = 1

        fld = "base"
        def __str__(self):
            return self.name

    class Blush(Enum):
        """
        Enum representing blush types
        """
        NONE = 0
        light = 1
        full = 2

        fld = "blush"
        def __str__(self):
            return self.name

    class Eyebrows(Enum):
        """
        Enum representing eyebrows
        """
        normal = 1
        up = 2
        knit = 3
        furrowed = 4
        think = 5

        fld = "eyebrows"
        def __str__(self):
            return self.name

    class Eyes(Enum):
        """
        Enum representing eyes
        """
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

        fld = "eyes"
        def __str__(self):
            return self.name

    class Mouth(Enum):
        """
        Enum representing mouths
        """
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

        fld = "mouth"
        def __str__(self):
            return self.name

    def buildSpriteImgPath(spr_enum, is_face=True):
        """
        Builds a filepath to the given sprite
        """
        top_fld_path = ("face" if is_face else "") + "/" + spr_enum.fld.value
        return "{0}{1}/{2}.png".format(SPR_PATH_SIT, top_fld_path, spr_enum)

    def drawNatsuki(
        chara,
        body, #NOTE: None right now, so this is ignored. However we may add more in the future
        eyebrows,
        eyes,
        mouth,
        blush,
    ):
        """
        Builds a displayable for Natsuki
        """
        #Build the composite
        #NOTE: WIP AF
        return Transform(
            LiveComposite(
                "(1280, 850),",
                    #(0,0), ACCESSORY_FP_HERE,
                    "(0,0),"
                        "(1280, 850),"
                            #BODY THINGS HERE
                            #MORE ACCESSORIES,
                    "(0,0),",
                        #FACE THINGS

                    #MORE ACCESSORIES

            )
        )
#
    #    return Flatten(natsukicomp)

    class Natsuki(object):
        """
        Class representing Natsuki herself, including her clothes, accessories, etc.

        We can use this to modify her appearance and such, likewise her name if we wish
        """
        def __init__():
            self.sitting = True
            self.clothes = ""

        def change_clothes(self, new_clothes):
            """
            Function to change clothes
            """
            pass #TODO: ME
