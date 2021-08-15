init 0 python in affinity:

    def affinity_is_between_bounds(lower_bound, affinity, upper_bound):
        """
        Returns whether a given affinity is within two bounds
        IN:
            lower_bound - The lower value to test against; affinity must match/exceed this
            affinity - The affinity to test
            upper_bound - The upper value to test against; affinity must match/fall below this
        OUT:
            True if no bounds given, or if affinity is within bounds; otherwise False
        """
        # We assume affinity is within range if no bounds are given
        if lower_bound is None and upper_bound is None:
            return True

        # Set bounds if None is given for either upper or lower, as we need an integer comparison
        if lower_bound is None:
            lower_bound = -9999999

        if upper_bound is None:
            upper_bound = 9999999
        
        return affinity >= lower_bound and affinity < upper_bound

    def get_affinity_tier(affinity):
        """
        Returns the affinity tier of the given affinity
        IN:
            affinity - The affinity to test
        OUT:
            The numerical value of the closest affinity tier this affinity falls into
        """
        for affinity_tier in [
            AFFINITY_LOVE,
            AFFINITY_ENAMORED,
            AFFINITY_AFFECTIONATE,
            AFFINITY_HAPPY,
            AFFINITY_NORMAL,
            AFFINITY_UPSET,
            AFFINITY_DISTRESSED,
            AFFINITY_BROKEN,
            AFFINITY_RUINED]:
                if affinity >= affinity_tier:
                    return affinity_tier