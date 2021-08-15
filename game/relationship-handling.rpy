default persistent.trust = 1.0
default persistent.affinity = 1.0

init 0 python:
    def relationship(change, multiplier=1):
        def affinity_increase(multiplier=1):
            if persistent.trust > 0:
                persistent.affinity += multiplier*(persistent.trust/20)

        def affinity_decrease(multiplier=1):
            if persistent.trust-50 > 0:
                persistent.affinity -= multiplier*(5 - (persistent.trust-50)/25)
            else:
                persistent.affinity -= multiplier*5

        def trust_increase(multiplier=1):
            if persistent.trust < 100:
                persistent.trust += multiplier*0.8*(round(math.tanh((persistent.affinity-75)/30)+1, 4)+1)
            if persistent.trust > 100:
                persistent.trust = 100

        def trust_decrease(multiplier=1):
            if persistent.trust > -100:
                persistent.trust -= multiplier*2*(3 - round(math.tanh((persistent.affinity-75)/30)+1, 4))
            if persistent.trust < -100:
                persistent.trust = -100

        if change == "affinity+":
            affinity_increase(multiplier)
        elif change == "affinity-":
            affinity_decrease(multiplier)
        elif change == "trust+":
            trust_increase(multiplier)
        elif change == "trust-":
            trust_decrease(multiplier)
        else:
            raise Exception(change+" is not a valid argument!")

init python in jn_affinity:
    # Affinity levels, highest to lowest
    THRESHOLD_LOVE = 1250 # She happ
    THRESHOLD_ENAMORED = 1000
    THRESHOLD_AFFECTIONATE = 750
    THRESHOLD_HAPPY = 500
    THRESHOLD_NORMAL = 250
    THRESHOLD_UPSET = 100 # She amger
    THRESHOLD_DISTRESSED = 0
    THRESHOLD_BROKEN = -100
    THRESHOLD_RUINED = -250  # How could you : (

    #Affinity States (non-prefixed as these are used for affinity_range)
    RUINED = 1
    BROKEN = 2
    DISTRESSED = 3
    UPSET = 4
    NORMAL = 5
    HAPPY = 6
    AFFECTIONATE = 7
    ENAMORED = 8
    LOVE = 9

    _AFF_STATE_ORDER = [
        RUINED.
        BROKEN,
        DISTRESSED,
        UPSET,
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMORED,
        LOVE
    ]

    def _is_aff_state_valid(state):
        """
        Checks if the given state is valid (mapped in the)
        """
    def _compare_affinity(state_1, state_2):
        """
        Internal compareto function which compares two affinity states

        IN:
            state_1 - the first state
            state_2 - the second state

        OUT:
            integer:
                -1 if state_1 is less than state_2
                0 if either state is invalid or both states are the same
                1 if state_1 is greater than state_2
        """
        if state_1 == state_2:
            return 0

        if state_1 not in _AFF_STATE_ORDER or state_2 not in _AFF_STATE_ORDER:
            return 0

        if _AFF_STATE_ORDER.index(state_1) < _AFF_STATE_ORDER.index(state_2):
            return -1

        return 1


init python in jn_trust:
    # Trust levels, highest to lowest
    TRUST_ABSOLUTE = 100
    TRUST_COMPLETE = 75
    TRUST_FULL = 50
    TRUST_PARTIAL = 25
    TRUST_NEUTRAL = 0
    TRUST_SCEPTICAL = -25
    TRUST_DIMINISHED = -50
    TRUST_DISBELIEF = -75
    TRUST_SHATTERED = -100
