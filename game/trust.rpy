init 0 python in trust:

    def trust_is_between_bounds(lower_bound, trust, upper_bound):
        """
        Returns whether a given trust is within two bounds
        IN:
            lower_bound - The lower value to test against; trust must match/exceed this
            trust - The trust to test
            upper_bound - The upper value to test against; trust must match/fall below this
        OUT:
            True if no bounds given, or if trust is within bounds; otherwise False
        """
        # We assume trust is within range if no bounds are given
        if lower_bound is None and upper_bound is None:
            return True

        # Set bounds if None is given for either upper or lower, as we need an integer comparison
        if lower_bound is None:
            lower_bound = -9999999

        if upper_bound is None:
            upper_bound = 9999999
        
        return trust >= lower_bound and trust < upper_bound

    def get_trust_tier(trust):
        """
        Returns the trust tier of the given trust
        IN:
            trust - The trust to test
        OUT:
            The numerical value of the closest trust tier this trust falls into
        """
        for trust_tier in [
            TRUST_ABSOLUTE,
            TRUST_COMPLETE,
            TRUST_FULL,
            TRUST_PARTIAL,
            TRUST_NEUTRAL,
            TRUST_SCEPTICAL,
            TRUST_DIMINISHED,
            TRUST_DISBELIEF,
            TRUST_SHATTERED]:
                if trust >= trust_tier:
                    return trust_tier