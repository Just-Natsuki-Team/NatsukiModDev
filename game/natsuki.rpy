default persistent.affinity = 25.0
default persistent._jn_player_confession_accepted = False

init 0 python:
    import store.jn_outfits as jn_outfits

    class Natsuki(object):
        """
        Qeeb class for handling actions related to Natsuki such as affinity checks/gains/losses, clothing, etc.

        NNNNNNXK0OOKXNXXKKK0000O00KKKKK000OO0Okxooooodoollccc:;;:ok000000K00000OOO00Kkl::oxkxl,,:oOK00KKKKKK
        NNNNNNNK00XXXXKK000000000O00KK0000O00000KKKKKKKKK0000OOkxddk0000000K00000OOOOkxxo:cdkko:,ckKOk0KKKKK
        NNNNNNX0KXXKKKKKKKXKK0000KKKXXKKKK00KKKKKKKK000000000KKKKKKKKKK00OO00000000OOkxxOkoccdkd:ckKOdkKKKKK
        NNNXX00KXXXXXXXXXXKKKKKKKKKKKKKKKKKKKKKKKKKKK0000000000KKKKKKKKKK0000000K000OOkkk00kl:oxddOKkox0KKKK
        XXXXK0KXNNNNNXXXKKXXXKKKKKKKKKKKKKKKKKKKKKKKKK000000000000KKKXXKKKKK00000000000OOOO0Oo:cok0OoldkKKKK
        XXXXXNNNNNX00KKKKXXKK0KKKKKKKKKKKKKKKKKKKKKKKK0K0000KK000000KKXKKKKK0KK0000O0000OOkOOOo;o0Oxoodx0KK0
        XKXXNNXKOxdxOK0KXXK00KKKKKKKKKKKKKKKKKKKKKKKKKKK000000KK000O00KXKK00KK00KK000OOOOOOOkkxxkxddxxxOKKK0
        XXNXKkdlclk0000KXK00KKKKKKKKKKKKKKKKKK000KKKKKKKKK0000KK0KKOkkKXKKK00KKKKK00K00OOOOOkxxkd:lxxxk0KK00
        XXXOocccdOK000KK00KKKK000KKKKKKKKKKKKK00000KKK0KKKKK000KKK00Okk00000000K0KKK00000OkkkkOkxodkxxO0KK00
        XKKkcclx0000000OOKXXK000KKKKKKKKKKKKKK00000KKKK0KKKK00000K0OKKkxk0K00OO0000K00KK000OOOOOkkkkxk0K0000
        XK0xclkK0OOOO0OO0KKK0O0KKKKKKKKKKKKKKK000KKKKKKKKKKK00KKKKKOOK0kxxOKK0OOO0K00K00K0000OOOOkxxk0000OOk
        KK0dlkK0OOOOOOkO0KKOk0KKKKKK000KKKKKK000K0KK0KKK00KK00KKKXKkxO0Okdx0KK0OkO0K0000KKK000OOOOkO000OOkdl
        K0OxkK0OOOOOOkk0KK0kOKKKKKKK00000KKKK000KKKKKKKKKKK00KXXXKkdxO00kxdk00K0kxk00K00K00K0000OO00Okxdolll
        K0O0KKkkOOkkkkO0KOkk0XXKKKK0OO0KKKKKK00KKKKKKKK0KKK00KXK0kdxkk00kxkkO000OxxkO0K0K00K0OOOOkkxollllood
        000KXOkkOOkkxxO00kkO0KXXXXK0OOKKK0KKK0KKKKKKKKKKXK0O0KKOkddkOkO0kOK0OO00OkxxxO00K0K00OOOkkkxdoodxxxx
        000XKkkOOkkxxxkOOkkO00KKXNN0k0KKKKKXKKKKXXKKXXXNX0kk000kxdx0KOOOk0NX0OOOOkxxxxk00KK00000000OOxxxkkkk
        00KX0kkOOkxxxxkkkkkOO0K0KKX0kKNXXNXXXXNNNKKXXKKK0xdk0Okxddk00kxdx0KK0OOkkkxkOkxk0KK00000K000Okxxxkkk
        00KKOkOOkxxxdxxxxxkOOO00KK0OkKXKKXKKKKKXK0KKKK0OxxxkxxdddkKXXOdx0NNNXK0kxdx0XKOxxOKKK0OO0K000Okxxkkk
        O0KKkxOOkxxddxxxxxkOkkO0000kk0KK0000KK0000KKK0OkdddddxxxkKNNNOdONNNNNXK0xoOXNNX0kk0KKKOO0KK00OkxdkOk
        k0KKkxOOkxxddxxdxxkkkkkO00Okk00Oxk0KK0000KKK0Okddxxddddx0XNNXkOXNNNNNNXX0x0NNNNNKOO0K00kO0000Oxxdx00
        k0XKkkOOkxxddxxddxkkkkkkOOkxkO0d;:dO0O000K00OxxdddddddxOKNNNXKXNNNNNNNXXXOKNNNNNNKO0KK0kO0000kodddO0
        x0XXOkOOkxxddxxddxxkxxxkkkxdkkko,,;:ok0K00OkxxdddooodxOKNNNNNNNXXXNNXNNNNNNNNNNNNX0O000kk0000kooddkO
        k0NXOkOOOkxddxxddxxxxxxxkxddkkOk::ol:;coxxkxxxdoooldxk0XXXNNXXXXXNNXX0Okxdollodk0XX0000xdO00OxlldxxO
        OKNX0kO0Okxddxxddxxxxxxxxxddk00Oc;dkdl;'';coxdooddxkOOKKKXXXXXX0koc:;'...  'cl::oKNK00Odok00kdllxkxk
        OKNXKkk0Okxdddddddddxxxxxdllddoc;',:;;;,,,cdooxxkOOOOKXXXXXKKkl,. .....''..'xNXOOXNX0Okolk0kxdookOkx
        OKNXKOkO0Oxodddddddddxxxd:,,;;:c;',lddddodxooxOOOOOOKNNNNNNXk:.'cxOl''',',clo0WNXNNX0kxllxkxdkxd00kx
        xKNXXOkO00kdodddoodoodddol;,;cdxd;,okkxxxxdxkOOOOO0KXNNNNNNXxco0NNOc:c:'':xOx0NNNNNX0xocldxdkOkO00kd
        xKXKX0kkO0Oxoodooooollodddoc;,;ldc'cddxkkkOOOOOO0KKXNNNNNNNNX0KNWNOlokOxxOXKOKNNNNNXkoocldxk00000Odo
        OXX0KKOxkOOkolooolllldxdddxxdl:,,,.,lxkkOOOOOO00KXXNNNNNNNNNNNNNNNNKkxOKK0OOKNNNNNNKxooclxk000000koo
        OX0OKK0xxkOOkoooocldxxddxxxxxxxo:,;cdxkOOOO0000KXNNNNNNNNNNNNNNNNNNNNK0OOO0KXNXXXXXkdxolxO0000000xod
        0Xkx0KKkdxkOOkdolodxdddxxxxxxxdlccodxkkOOO0000KXXNNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXX0kOxok00000000Odlx
        0KkxOKK0xdxkOkxddooddxxxxxxxdlccllooxkOO00000KXNNNNNNNNNNNNNNNNNNNNNNNXXXXXKKKKKKXKKOdk00OO00000kodO
        0OxxOKK0Oxddxxdooodddddddddlc:;,'...';lk0000KXNNNNNNNNNNNNNNNNNNNNNNXXXXXXKKKKKKKXXKkk0Okk000000kdOK
        OxxxkKK00xdddooodxddddddolc:,..........;dO0KKXNNNNNNNNNNNNNNNNNNNNNXXXXXXXKKKKKKXXK0O0kxx0000O0OkOK0
        xxxxk00Okdlcldxxdddddolccc:...cl:......';d0KXNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXX0O00kxk000OOOO00Ox
        xxxddkOkkxooxxxdddolc:clol,.'dOk:..''';lco0XXNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXK0KK0kxO00OkkkOkddo
        dddddk0OOkkkxxdollccllolodc.;xOOko:,':odldKNNNNNNNNNNNNNNNNNNNNNNNXXXXXXXXXXXXXXXXXXKOdxO0Okkxdddddd
        ddddoxkkkxxdol:;;cllodxdddo:;lxOO0OxdddxkKXNNNNNXXXXNNNNNNNNNNNNNNNNXXXXXXXXNNNNNNNKOodk00OOkxxkxdoo
        doodddxxxdl::::;;:cllodxxxdooodkO00KK00KXNNNNNNXK00KXNNNNNNNNNNNNNNNNNNNNNNNNNNNNXKkooxO0Okxdxxxolod
        ooooodxOkkdcccc:;::ccloodxxdllldkO000KKXXXNNNNNNNXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0xooxOOkxooxxdllddx
        oooloodOK0koccc:;::c::cloddxxdodxkO0KKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoodxkOxxdooodOxlldx
        lllclolkKKOdllcc::cccc:ccloooddxxxxxk0KXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXOdoodxkkkxddxdlxK0olxx
        cclcllcd0K0kolllc:cccccccccccccllllcok0XXXNNNNNNNNNNNNNNNNXXXXNNNNNNNNNNNNNX0xooodxxxkkkkkkkOKX0ddkx
        ccccllclkXKOdllllcccllllcclllllllcccclx0XNNNNNWWWWWNNNNNNXXXXXNNNNNNNNNNNNKxoloodxxxkkkkkO0KXXK0xdxk
        ccccclccdKXKkoooollllllllllllloooollllllx0NNWWWWWWWWNNNNNNNNNNNNNNNNNNNX0xlcloodkkkkkkO0KXNNXKKOddxx
        :::::lcclkXK0kdooooooooooooolllooddddxkkxkO0KXNWWWWWWNNNNNNNNNNNNNNNNXKOxc;clodxkO00KXNNNNNNWXKkoddx
        ;::::cc::lOXK0OxdddddddodddxxddodxxxxxkOkdocclodxkkOO0KKXXXXKKKKKKKK00OkxolxO0KXXNNWWWWWWWWWWXOolddd
        ;:::cccccclOX0kkkxddddddddodxOOOO000Oxdllc::;;;,,'',,;::ccccc::cdO00OxoooxXWWWWWWNNNWWWWWWWWXklldddd
        ::::ccccccclk0kddxxddddddddddxkO00Okxollcc::;;;;,,,,,,,,,,,,,,,lOKOxolddo0NWWWWWNNNNNNNWWNXkoloddddo
        ::::cccccccclxkxddddxxdddxxdxkkOOOxoollccc::::;;,;;;,,,,,,,,,,;d0xccldkodKWWWWWWNNNNNNNWN0oclddddddo
        """

        # Tracks whether Natsuki is currently in some topic flow
        __is_in_conversation = False

        # Tracks whether Natsuki is currently playing a game
        __is_in_game = False

        # START: Outfit functionality

        # Tracks Natsuki's currently worn outfit
        _outfit = None

        @staticmethod
        def getOutfitName():
            """
            Returns the reference name of the outfit Natsuki is currently wearing.
            """
            return Natsuki._outfit.reference_name

        @staticmethod
        def setOutfit(outfit, persist=True):
            """
            Assigns the specified jn_outfits.JNOutfit outfit to Natsuki.

            IN:
                - outfit - The jn_outfits.JNOutfit outfit for Natsuki to wear.
                - persist - True if the outfit should be remembered so Natsuki will be wearing it on next boot
            """
            Natsuki._outfit = outfit

            if persist:
                store.persistent.jn_natsuki_outfit_on_quit = Natsuki._outfit.reference_name

        @staticmethod
        def isWearingOutfit(reference_name):
            """
            Returns True if Natsuki is wearing the specified outfit, otherwise False.

            IN: 
                - reference_name - outfit reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified outfit, otherwise False
            """
            return Natsuki._outfit.reference_name == reference_name

        @staticmethod
        def isWearingClothes(reference_name):
            """
            Returns True if Natsuki is wearing the specified clothes, otherwise False.

            IN: 
                - reference_name - The clothes reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified clothes, otherwise False
            """
            return Natsuki._outfit.clothes.reference_name == reference_name

        @staticmethod
        def isWearingHairstyle(reference_name):
            """
            Returns True if Natsuki is wearing the specified hairstyle, otherwise False.

            IN: 
                - reference_name - The hairstyle reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified hairstyle, otherwise False
            """
            return Natsuki._outfit.hairstyle.reference_name == reference_name

        #TODO: Adjust these functions in a proper acs system
        @staticmethod
        def isWearingAccessory(reference_name):
            """
            Returns True if Natsuki is wearing the specified accessory, otherwise False.

            IN: 
                - reference_name - The accessory reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified accessory, otherwise False
            """
            return Natsuki._outfit.accessory.reference_name == reference_name

        @staticmethod
        def isWearingEyewear(reference_name):
            """
            Returns True if Natsuki is wearing the specified eyewear, otherwise False.

            IN: 
                - reference_name - The eyewear reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified eyewear, otherwise False
            """
            return Natsuki._outfit.eyewear.reference_name == reference_name

        @staticmethod
        def isWearingHeadgear(reference_name):
            """
            Returns True if Natsuki is wearing the specified headgear, otherwise False.

            IN: 
                - reference_name - The headgear reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified headgear, otherwise False
            """
            return Natsuki._outfit.headgear.reference_name == reference_name

        @staticmethod
        def isWearingNecklace(reference_name):
            """
            Returns True if Natsuki is wearing the specified necklace, otherwise False.

            IN: 
                - reference_name - The necklace reference name to check if Natsuki is wearing

            OUT:
                - True if Natsuki is wearing the specified necklace, otherwise False
            """
            return Natsuki._outfit.necklace.reference_name == reference_name

        # Start: Relationship functionality

        @staticmethod
        def calculatedAffinityGain(base=1, bypass=False):
            """
            Adds a calculated amount to affinity, based on the player's relationship with Natsuki and daily cap state.

            NOTE:
                If the player has not confessed to Natsuki via the talk_i_love_you topic, further affinity gain is not possible
                until the confession has been made! This is to prevent players having Natsuki tell them she loves them unwarranted
                by accidentally crossing the boundary into LOVE.

            IN:
                - base - The base amount to use for the calculation
                - bypass - If the daily cap should be bypassed for things like one-time gifts, events, etc.
            """
            to_add = base * jn_affinity.get_relationship_length_multiplier()

            if (
                not persistent._jn_player_confession_accepted 
                and (persistent.affinity + to_add) > (jn_affinity.AFF_THRESHOLD_LOVE -1)
            ):
                # Player cannot reach LOVE without having confessed to Natsuki successfully
                persistent.affinity = jn_affinity.AFF_THRESHOLD_LOVE -1
                jn_utils.log("Affinity blocked - CN!")
                return

            if bypass and persistent._affinity_daily_bypasses > 0:
                # Ignore the daily gain and just award the full affinity
                persistent.affinity += to_add
                persistent._affinity_daily_bypasses -= 1
                jn_utils.log("Affinity+ (B)")

            elif persistent.affinity_daily_gain > 0:
                # Award the full affinity if any cap remains
                persistent.affinity_daily_gain -= to_add
                persistent.affinity += to_add

                if persistent.affinity_daily_gain < 0:
                    persistent.affinity_daily_gain = 0
                
                jn_utils.log("Affinity+")

            else:
                jn_utils.log("Daily affinity cap reached!")

        @staticmethod
        def calculatedAffinityLoss(base=1):
            """
            Subtracts a calculated amount from affinity, based on the player's relationship with Natsuki.

            IN:
                - base - The base amount to use for the calculation
            """
            persistent.affinity -= base * jn_affinity.get_relationship_length_multiplier()
            jn_utils.log("Affinity-")

        @staticmethod
        def percentageAffinityGain(percentage_gain):
            """
            Adds a percentage amount to affinity, with the percentage based on the existing affinity value.
            This bypasses the usual check, so this should only be used for one-off big gains.

            NOTE:
                If the player has not confessed to Natsuki via the talk_i_love_you topic, further affinity gain is not possible
                until the confession has been made! This is to prevent players having Natsuki tell them she loves them unwarranted
                by accidentally crossing the boundary into LOVE.

            IN:
                - percentage_gain - The integer percentage the affinity should increase by
            """
            to_add = persistent.affinity * (float(percentage_gain) / 100)
            if (not persistent._jn_player_confession_accepted and (persistent.affinity + to_add) > (jn_affinity.AFF_THRESHOLD_LOVE -1)):
                # Player cannot reach LOVE without having confessed to Natsuki successfully
                persistent.affinity = jn_affinity.AFF_THRESHOLD_LOVE -1
                jn_utils.log("Affinity blocked - CN!")

            else:
                persistent.affinity += to_add
                jn_utils.log("Affinity+")

        @staticmethod
        def percentageAffinityLoss(percentage_loss):
            """
            Subtracts a percentage amount to affinity, with the percentage based on the existing affinity value.

            IN:
                - percentage_loss - The integer percentage the affinity should decrease by
            """
            if persistent.affinity == 0:
                persistent.affinity -= (float(percentage_loss) / 10)

            else:
                persistent.affinity -= abs(persistent.affinity * (float(percentage_loss) / 100))
            
            jn_utils.log("Affinity-")

        @staticmethod
        def checkResetDailyAffinityGain():
            """
            Resets the daily affinity cap, if 24 hours has elapsed.
            """
            current_date = datetime.datetime.now()

            if not persistent.affinity_gain_reset_date:
                persistent.affinity_gain_reset_date = current_date

            elif current_date.day is not persistent.affinity_gain_reset_date.day:
                persistent.affinity_daily_gain = 5 * jn_affinity.get_relationship_length_multiplier()
                persistent.affinity_gain_reset_date = current_date
                persistent._affinity_daily_bypasses = 5
                jn_utils.log("Daily affinity cap reset; new cap is: {0}".format(persistent.affinity_daily_gain))

        @staticmethod
        def __isStateGreaterThan(aff_state):
            """
            Internal method to check if Natsuki's current affinity state is greater than the given amount
            """
            return jn_affinity._isAffStateWithinRange(
                Natsuki._getAffinityState(),
                (aff_state, None)
            )

        @staticmethod
        def __isStateLessThan(aff_state):
            """
            Internal method to check if Natsuki's current affinity state is less than or equal to the given amount
            """
            return jn_affinity._isAffStateWithinRange(
                Natsuki._getAffinityState(),
                (None, aff_state)
            )

        @staticmethod
        def __isAff(aff_state, higher=False, lower=False):
            """
            Internal comparison to check if Natsuki's current affection matches the given state,
            or is lower/higher as specified by arguments

            IN:
                aff_state - The affection state to check if Natsuki is at
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            #For completion, if both higher and lower are true, we should just return True as
            #The given aff_state must be within the range
            if higher and lower:
                return True

            if higher:
                return Natsuki.__isStateGreaterThan(aff_state)

            elif lower:
                return Natsuki.__isStateLessThan(aff_state)

            return Natsuki._getAffinityState() == aff_state

        #START: Natsuki's Affection State checks
        @staticmethod
        def isRuined(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is ruined, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.RUINED, higher, lower)

        @staticmethod
        def isBroken(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is broken, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.BROKEN, higher, lower)

        @staticmethod
        def isDistressed(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is distressed, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.DISTRESSED, higher, lower)

        @staticmethod
        def isUpset(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is upset, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.UPSET, higher, lower)

        @staticmethod
        def isNormal(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is normal, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.NORMAL, higher, lower)

        @staticmethod
        def isHappy(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is happy, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.HAPPY, higher, lower)

        @staticmethod
        def isAffectionate(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is affectionate, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.AFFECTIONATE, higher, lower)

        @staticmethod
        def isEnamored(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is enamored, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.ENAMORED, higher, lower)

        @staticmethod
        def isLove(higher=False, lower=False):
            """
            Checks if Natsuki's affection state is love, or is lower/higher as specified by arguments

            IN:
                higher - bool, if Natsuki's affection can be greater than the current state
                    (Default: False)
                lower - bool, if Natsuki's affection can be less than the current state
                    (Default: False)
            """
            return Natsuki.__isAff(jn_affinity.LOVE, higher, lower)

        @staticmethod
        def _getAffinityState():
            """
                returns current affinity state

                states:
                    RUINED = 1
                    BROKEN = 2
                    DISTRESSED = 3
                    UPSET = 4
                    NORMAL = 5
                    HAPPY = 6
                    AFFECTIONATE = 7
                    ENAMORED = 8
                    LOVE = 9

                OUT:
                    current affinity state
            """
            #iterate through all thresholds
            i = 1
            for threshold in [
                jn_affinity.AFF_THRESHOLD_LOVE,
                jn_affinity.AFF_THRESHOLD_ENAMORED,
                jn_affinity.AFF_THRESHOLD_AFFECTIONATE,
                jn_affinity.AFF_THRESHOLD_HAPPY,
                jn_affinity.AFF_THRESHOLD_NORMAL,
                jn_affinity.AFF_THRESHOLD_UPSET,
                jn_affinity.AFF_THRESHOLD_DISTRESSED,
                jn_affinity.AFF_THRESHOLD_BROKEN,
                jn_affinity.AFF_THRESHOLD_RUINED
            ]:
                #if affinity is higher than threshold return it's state
                #else check lower threshold
                if jn_affinity._compareAffThresholds(persistent.affinity, threshold) >= 0:
                    return jn_affinity._AFF_STATE_ORDER[-i]

                # We can't go any further beyond ruined; return it
                if threshold == jn_affinity.AFF_THRESHOLD_RUINED:
                    return jn_affinity._AFF_STATE_ORDER[0]

                i += 1

        def _getAffinityTierName():
            affinity_state = Natsuki._getAffinityState()
            if affinity_state == jn_affinity.ENAMORED:
                return "LOVE"

            elif affinity_state == jn_affinity.ENAMORED:
                return "ENAMORED"

            elif affinity_state == jn_affinity.AFFECTIONATE:
                return "AFFECTIONATE"

            elif affinity_state == jn_affinity.HAPPY:
                return "HAPPY"

            elif affinity_state == jn_affinity.NORMAL:
                return "NORMAL"

            elif affinity_state == jn_affinity.UPSET:
                return "UPSET"

            elif affinity_state == jn_affinity.DISTRESSED:
                return "DISTRESSED"

            elif affinity_state == jn_affinity.BROKEN:
                return "BROKEN"

            elif affinity_state == jn_affinity.RUINED:
                return "RUINED"

            else:
                store.jn_utils.log(
                    message="Unable to get tier name for affinity {0}; affinity_state was {1}".format(
                        store.persistent.affinity,
                        Natsuki._getAffinityState()
                    ),
                    logseverity=store.jn_utils.SEVERITY_WARN
                )
                return "UNKNOWN"

        @staticmethod
        def addApology(apology_type):
            """
            Adds a new apology possiblity to the list of pending apologies.
            If the apology type is already present in the list, ignore it.

            IN:
                apology_type - The jn_apologies.ApologyTypes type to add.
            """
            if not isinstance(apology_type, int) and not isinstance(apology_type, jn_apologies.ApologyTypes):
                raise TypeError("apology_type must be of types int or jn_apologies.ApologyTypes")

            if not int(apology_type) in store.persistent._jn_player_pending_apologies:
                store.persistent._jn_player_pending_apologies.append(int(apology_type))

        @staticmethod
        def setQuitApology(apology_type):
            """
            Sets the jn_apologies.ApologyTypes type to be checked on loading the game after quitting.

            IN:
                apology_type - The jn_apologies.ApologyTypes type to add.
            """
            if not isinstance(apology_type, int) and not isinstance(apology_type, jn_apologies.ApologyTypes):
                raise TypeError("apology_type must be of types int or jn_apologies.ApologyTypes")

            store.persistent._jn_player_apology_type_on_quit = int(apology_type)

        @staticmethod
        def removeApology(apology_type):
            """
            Removes an apology from the list of pending apologies, if it exists.

            IN:
                apology_type - The jn_apologies.ApologyTypes type to add.
            """
            if not isinstance(apology_type, int) and not isinstance(apology_type, jn_apologies.ApologyTypes):
                raise TypeError("apology_type must be of types int or jn_apologies.ApologyTypes")

            if int(apology_type) in store.persistent._jn_player_pending_apologies:
                store.persistent._jn_player_pending_apologies.remove(int(apology_type))

        @staticmethod
        def setInConversation(is_in_conversation):
            """
            Marks Natsuki as being in a conversation with the player, or another dialogue flow.
            While in conversation, the hotkey buttons are disabled.

            IN:
                - is_in_conversation - The bool in conversation flag to set
            """
            if not isinstance(is_in_conversation, bool):
                raise TypeError("is_in_conversation must be of type bool")

            Natsuki.__is_in_conversation = is_in_conversation

        @staticmethod
        def setInGame(is_in_game):
            """
            Marks Natsuki as being in a game with the player.
            While in a game, the player is marked as a cheater if they force quit, and can later apologize for it.

            IN:
                - is_in_game - The bool in game flag to set
            """
            if not isinstance(is_in_game, bool):
                raise TypeError("is_in_game must be of type bool")

            Natsuki.__is_in_game = is_in_game

        @staticmethod
        def isInConversation():
            """
            Gets whether Natsuki is or is not currently in a conversation.
            While in conversation, the hotkey buttons are disabled.
            
            OUT:
                - True if in conversation, otherwise False
            """
            return Natsuki.__is_in_conversation

        @staticmethod
        def isInGame():
            """
            Gets whether Natsuki is or is not currently playing a game.
            While in a game, the player is marked as a cheater if they force quit, and can later apologize for it.
            
            OUT:
                - True if in game, otherwise False
            """
            return Natsuki.__is_in_game

# KWWWMMMMMMMWNNNNNNXXXKKKKK00KKXXKKK0KK0000KKKKKK000Okkxdoodk0KKKKKXKKKK0000KOxoccdkko;,cOX00XXXXXXXX
# KNWWWWWMMWWNNNNNXXXXXXXXKKKKKXXXXXXKKKKXXXXXXXKKKXXKKKKKKXKKKXXK00KKKKKKK000OxOOdclxOx:;kXOxKXXXXXKK
# KNWWWWWWNXKXNNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXKKKXKKKKKKXXKXXXXXKKKKKKKKKK00Ok0KOo:oxddOXkdOXXXXXKK
# KNWWWNNNXKXNWWWWWNNXXNNXXXXXXXXXXXXXXXXXXXXXXXXKKKKKXKKKKKXXXNNNXXXXKKKKKKKKK0000KKx:cdkK0olx0XXXXKK
# 0NWWNNNNWWWWWNXKXNXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKXXKKKKKXNNXXXXXXXXKKKKKKK00OO00x:l0KkooxOXXXKK0
# 0NNNNXXNWWN0kdxOKKKXNXKKXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKXKKK00XXNXXXXXXXXXXKK000000OOOkOxdxkkk0XXKKK0
# 0XKXNNNNKkolcd0KKKXXXKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKXXXKOOXNXXXKKXXXXXXXKK00000OkOx:lkkkOKXXKK0O
# kdkXNNN0occokKK0KKK0KXXXXKKKXXXXXXXXXXXXXXXXXXXXXXXXKKKKKXXKKOk0KXKKKKKXXXXXXKKK0OOO0OkxkOkkKXXKKKOx
# loOXNNXOlco0XK000K00KNNK0KKKXXXXXXXXXXXKKKXXXXXXXXKXXKKXXXK0KX0kkKXKK00KXXXXXXXXKK00000OOkk0XKKK0Odl
# lx0KXXXkcd0XK000000KXXX00KXKXXXKXXXXXXXKKKKXXXXXXXXXKKKXXXN0OKK0xk0KKK0OKXXXKXXXXKKK0000kk0KK000kooo
# ok00XXKxd0X000000O0KXK00KXXKXXKKKXXXXXXKKKKKKKXXXXXXKKXNXNXkx0XKOxk0KKKOO0KXXXXXXKKXK0000KKK0Okdlooo
# O000KK0OKX0O000OOOKXK0OKNNXKKXK0KKXXXXKKKXXKXXXXXXXXKKNNNKkxkOKKOkkOKKK0kk0KKXXXXXXKK0000Oxxdolloodx
# 00OO0KKXNKO00OOOOOKK0O0XNNNXXX00KXXKKXXKXXKXXXXXXNNX0KNX0kxkOO0KOOK00KKKOkkO0KKXXKK0OOOOkdoloddxxkkk
# 0Okk0KKNXOO00OOkkOK0OO0KXNNNNN00XXXXXXXXXXNNXNNNNNNK0KX0kxk0K000OKNX00000kxkO0KXKXKKKKKK00OxxkOkkkkk
# 0kkO0KKNKOO0OOkkkOOOkO0KKKXXNX0KNNNNNNNWWWNXNNNNNKOk0K0kxxx0KOkxkKXX00OOOkOOkkOKXXXKKKKKKK0OxkkOOOOO
# 0Okk0KXX0kO0OkxxxkkkkO00KKXXXKOKNNNNXXNNNNXXXXXKKkxkOkxxdx0XN0xxKNNNXK0kxkKNKOkOKXXKK0KXKK00kxkOkOOO
# 00OkOKXXOk00OkxxxkxxkO0OOKKKK0O0XKKKKKKKKKKKXKKKOxoxxxkxkKNWW0d0WWWMWNXOdkNWWN0kOKXKK0KXKXK0Oxk00Okk
# XKOkOKXXOk00OxxxxkxxkOOOOO0KKOO0K0xkKXKK0KKXXK0Oxxxxxxxx0XWWNOONWMMMMNNXk0WWMWWX0KXKK00KXKKOkxxOK0Ok
# NXOkk0XXOk00OxxxxkxxkkOOkkO00kk00x;:d000KXKKK0OkxxxdddxOXWWWNNNWMMMWWWWWKXWMWWWWX0KKKOOKXKKkddxkKK0O
# WX0kxONN0k00OkxxxkxxkkkkkkOOkxkOOd;,::lkKKK0OkkxddxddxOKNWWWWMMWWWMMWMWWWWWMWWWWNK0KKOkKXKKkodxx0KKO
# WN0kOKWN0k00OkxxxkxxxkkkkkkOxdkO0Oc:dd:;cldkxkkdddooxOKNWMMWMMMMMMWWWWMMMWWWWWWWWXKKKkdOXK0xldkkOKK0
# NXkOKXWNKOO00kxxxxxxxxxkkkkkxdk00Oc,oxo:,..,lxdodxxkO0XWWMMMMMWWWWWWWWWWMWWWWWWWWWKK0xokK0OxloOOk0KK
# X0dkKXWWXOO00Oxdxxxdxxxxxkkxlcllc:,.';;::::ldodkOOO00XWWMWWWWWWWWWWWWNXK000O000KNWX0Odlk0OkxdxKOkOKK
# KOxokKWNX0O00Oxddxxddxddxxxo;',:ldl';xOkkxkxdxO00000KNWMMWWWWWWWNKxl:,'..''';:d0NWX0kolxOxkOkOK0kkKK
# K0Oxd0NNNKkO00kooxddoddodddxo:,;lxx:'okxxkkkO00000KKNWWMMWWWWNN0d:;:ldkOO0000XNWWWXkdllxkk000KKOxk0K
# K0OOOKNXXXOkO00xodddoolldxxddxdc,,:;.;dxOO000000KKXNWWMWMWWWWWKxkKNWWWWWWWWWWWWWWW0ddllxk0XKKKKkokKX
# kOOO0XX0KX0xkO0Ododdlloxxxdxkkkkdl;''cxOO00000KKKXNWWWWWWWWWWWNNWWWWMWWWWWWWWWWWWXkxdcdOKKKKKK0doOKK
# okOO0N0kKXKkxO00OdoooxxxxxkkkkkkxdlldkO0000KKKKKNWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNN0OOdd0KKKKKKKOoo0XK
# okOk0XOx0XX0xxk0OkddxddxxxxxkkxdoodkkkkO00KKKKXNWWWWWMMWWWWWWWWWWWWWWWWWNNNNXXXNXXKkx0K00KKKKKkokKXK
# oxOOKKOk0XXKOxxkkkdoodxxxxxxxdlldxkOOO000KKKKXNWWMMMWWMWWWWWWWWWWWWWWWNNNXXXXXXNNN0k00OOKKKKK0xxKKKK
# lxkO0OkkOXXK0xdxdodxxxxxxxdolldxkOOOOkkkkO0KXXNWWWWWWWMMWWWWWWWWWWWWWWNNNNXXXXNNNX000kk0KKK000OKK0Ok
# lxkkkkkkkKK0kdlldxkxxxxdollloxkkkxo:,',clxOKXNWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNNNX00K0kOKKK0000K0kxdo
# cdxxkkkxxO0OOxdxkkxxdolc:codkkkxc...;oxOKKXXNWWWWWWWWWWWWWWWWWWWWWWWWNWNNNNNNWWNXKNXOkOK0OOkkkxddooo
# :lxxxxxxxOK0OOOkxdolccllododkkd;.'cx0KKKKXXNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0xx0K0kkxdxxxxood
# :oxxxxxxxkOkkxdlc:;;clloxkkxxxddxk0KKKKKKXNWWWWWWNXXNWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0ddOKK0Okxkkxdooxx
# :oxdddddxxkkxxl::::;;cclodxkxdodxkO0KKKXXNNWWWWWWXXXNWWWWWWWWWWWWNN0OXWWWWWWWWWWNOddk00Okxxkxdooxkkx
# 'cddddddddOK00xlcc:;;::ccodxxxdolok0KKXXNNWWWWWWWWWWWMWWWWWWWNXKOkOkxKWWWWWWWWWKkodkO0kxddxxxllxxxkk
# .:oooddoddx0XKkoccc:;::::clodxxkkxkkO0KXNNWWWWWWWMMMWWMMWWXOddxkkOOOOKWWWWWWWXOdoxkOOkxdxdckNkcokxxk
# .:oooooooooOXX0dlllc:cccccccllllloodooxKXNNWWWWMWWWMMWWNOl,.:xOOOOOO0NWWWWWN0dooxkkOOkkkOkkKNOdxOxxk
# .:oollllloldKXKkolllccccclcclllllllc:clxKNNWWWWMMWMMMWWNOl;,lOOOOO00XWWWWN0xoodxxkkOOOOO0KNNN0dkOxox
# .;::::ccclcckNX0doooollllllllllooddolccclxKNWMMMMMMMMMMMWWNK0KKKKXNWWWWNKdllodxkkkOOO0KXNNNNNOdxkxod
# ',,,,,;;:l:,l0NXOxdddooooooolllloddxxddxxdk0KXWMMMMMMMMMWWWWWWWWWWWWWNX0l;codxkO0KKXNWMMWWWNXkdxkxol
# ',,,,,,;;cc;,oKXK0kxxdddddddddxdoooxxxxxOOxdlcodxkOO0KXNNNWNNNXXXXXXXKOOdldO0KXNWWMMMMMMMMMWOodxxdoo
# '''',,,,;;::::xKXOOOkxxddxxdddxkOOOOOOOxolc::;;,,''',;:cccclccclkKKKOxdoxXWWMMMMMMMMMMMMMMNkloxxdoox
# ''''''''''',;;;lOOolxxxxxxxxdddxkkO0Oxdollc::;;;,,,,,,,,'',,,,,oKX0xodxdOWMMMMMMMMMMMMMWXkolddddoodd
# ''...........''',clccodxxxddddddxkkxdooollcc::;;,,,,,,,'',,''';dxc;cxOddXMMMMMMMMMMMMWKkdlodddddoodd
# '''''''''''''',,,,,;:lxkkkkxxxdxkxxxdoolllcc::;;,;;,,,,....'..''..,:lo:xWMMMMMMMMMWX0xdodddddddooddd
# '''''''''''',',,,,,,;lxkkOOOOkkkkxxxdoollcc::;;;,,,,,,'..''',,'..,oo:cxXMMMMMMWWX0kdododdddoddoldddd
# '',,'''''''''',,,;;,:ldkkkkkkkkxxddddoollcc::,,;,,,,,,....':llc,'o0KxcOMMMWNX0Oxdooooooddddddoloddoo
# '',,,,,,''',,:codkkOO00OkOOkxxxxddddooollccc:;,;,,,,,,....':dkd;:0XXOckWNKOxdooooooooooodddooooddooo