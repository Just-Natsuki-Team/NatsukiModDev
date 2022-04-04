default persistent.trust = 10.0
default persistent.affinity = 25.0

default persistent.affinity_daily_gain = 5
default persistent.affinity_gain_reset_date = None

init -1 python in jn_affinity:
    import store
    import store.jn_utils as jn_utils
    import random

    # Affinity levels, highest to lowest
    AFF_THRESHOLD_LOVE = 1000
    AFF_THRESHOLD_ENAMORED = 500
    AFF_THRESHOLD_AFFECTIONATE = 250
    AFF_THRESHOLD_HAPPY = 100
    AFF_THRESHOLD_NORMAL = 0
    AFF_THRESHOLD_UPSET = -25
    AFF_THRESHOLD_DISTRESSED = -50
    AFF_THRESHOLD_BROKEN = -100
    AFF_THRESHOLD_RUINED = -125

    # Affinity States (non-prefixed as these are used for affinity_range)
    # RUINED - Natsuki is emotionally exhausted. She barely talks and holds nothing but hopelessness. Things can't get any worse.
    # BROKEN - Natsuki is an obvious state of sadness. She lacks confidence in herself, her player and their future.
    # DISTRESSED - Natsuki is clearly and visibly unhappy. She is distant and impersonal.
    # UPSET - Natsuki isn't particularly happy; generally to the point and somewhat cold.
    # NORMAL - Natsuki is generally cordial, but not particularly affectionate. This is the default state.
    # HAPPY - Natsuki is chipper and friendly, but still not particularly affectionate. Some teasing.
    # AFFECTIONATE - Natsuki is always glad to see her player, and feelings are beginning to obviously stir!
    # ENAMORED - Natsuki clearly has feelings for her player, and she tentatively expresses them.
    # LOVE - Natsuki is completely head-over-heels for her player, and wants nothing more than their love. Things can't get any better!
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
        RUINED,
        BROKEN,
        DISTRESSED,
        UPSET,
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMORED,
        LOVE
    ]

    def get_relationship_length_multiplier():
        """
        Gets the multiplier for affinity changes, based on the length of the relationship in months.

        OUT:
            - relationship multiplier value, capped at 1.5
        """
        relationship_length_multiplier = 1 + (jn_utils.get_total_gameplay_months() / 10)
        if relationship_length_multiplier > 1.5:
            relationship_length_multiplier = 1.5

        return relationship_length_multiplier

    def _isAffStateValid(state):
        """
        Checks if the given state is valid.

        IN:
            state - the integer representing the state we wish to check is valid

        OUT:
            True if valid state otherwise False
        """
        return (
            state in _AFF_STATE_ORDER
            or state is None
        )

    def _compareAffThresholds(value, threshold):
        """
        Generic compareto function for values
        """
        return value - threshold

    def _compareAffinityStates(state_1, state_2):
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

        if not _isAffStateValid(state_1) or not _isAffStateValid(state_2):
            return 0

        #If state 1 is less than state 2, return -1
        if _AFF_STATE_ORDER.index(state_1) < _AFF_STATE_ORDER.index(state_2):
            return -1

        #Else return 1
        return 1

    def _isAffRangeValid(affinity_range):
        """
        Checks if the given affinity range is valid

        IN:
            affinity_range - The affintiy_range structure used in Topics (a tuple of the format):
                [0] - low bound (Can be None)
                [1] - high bound (Can be None)

        OUT:
            True if affinity_range is valid, False if not
        """
        if affinity_range is None:
            return True

        #deconstruct the tuple
        low_bound, high_bound = affinity_range

        #No low bound and no high bound is equivalent to just no range
        if low_bound is None and high_bound is None:
            return True

        #Now test to see if the individual parts are valid
        if (
            not _isAffStateValid(low_bound)
            or not _isAffStateValid(high_bound)
        ):
            return False

        #Now if one side is None, and we know the other is valid, this is also valid
        if low_bound is None or high_bound is None:
            return True

        #Finally compare this to make sure we don't have an inversion
        return _compareAffinityStates(low_bound, high_bound) <= 0

    def _isAffStateWithinRange(affinity_state, affinity_range):
        """
        Checks if the given affinity_state is within the given affinity_range

        IN:
            affinity_state - the state value to check if is within the affinity_range
                (NOTE: The affinity_range is considered INCLUSIVE)
            affinity_range - a tuple of the form:
                [0] - low_bound
                [1] - high_bound
        """
        #Firstly, make sure the given affinity_state is even valid
        if affinity_state is None or not _isAffStateValid(affinity_state):
            return False

        #No affinity_range is a full range, so this is always True
        if affinity_range is None:
            return True

        #Now, deconstruct the tuple
        low_bound, high_bound = affinity_range

        #If low and high are none, it's also a full range, always True
        if low_bound is None and high_bound is None:
            return True

        #Now we run compareTo checks
        #Firstly, single-bounded checks (one side None)
        if low_bound is None:
            #We only care about the high bound
            return _compareAffinityStates(affinity_state, high_bound) <= 0

        if high_bound is None:
            #Only the low bound matters
            return _compareAffinityStates(affinity_state, low_bound) >= 0

        #If the range is only for the single level, so they should just be equal
        if low_bound == high_bound:
            return affinity_state == low_bound

        #With the outlier cases done, simply check if we're within the range
        return (
            _compareAffinityStates(affinity_state, low_bound) >= 0
            and _compareAffinityStates(affinity_state, high_bound) <= 0
        )
