init -50 python:

    """
        Takes a numerical day value, returns the appropriate suffix for a given day.
        For example, 2 will return "nd".

        IN:
            day - the numerical day of the month.
        RETURNS:
            The corresponding mapped suffix for the given day number, or "th" if not found.
            
    """
    def jn_get_date_suffix(day):
        day_suffixes = {
            1: "st",
            2: "nd",
            3: "rd",
            11: "th",
            12: "th",
            13: "th"
        }

        if day in day_suffixes:
            return day_suffixes[day]
        else:
            return "th"