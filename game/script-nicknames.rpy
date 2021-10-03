init 0 python in nicknames:
    
    # Tracking
    bad_nickname_streak = 0

    # Nickname types
    NICKNAME_TYPE_LOVED = 0
    NICKNAME_TYPE_NEUTRAL = 1
    NICKNAME_TYPE_DISLIKED = 2
    NICKNAME_TYPE_HATED = 3
    NICKNAME_TYPE_PROFANITY = 4
    NICKNAME_TYPE_FUNNY = 5

    # Natsuki loves these nicknames; awarding them awards affinity/trust
    NICKNAME_LOVED_LIST = [
        "Babe",
        "Babycakes",
        "Boo",
        "Bun Bun",
        "Bun-Bun",
        "BunBun",
        "Bunny",
        "Cupcake",
        "Cutie Pie",
        "Cutie",
        "Darlin",
        "Darling",
        "Heart-string",
        "Heart-throb",
        "Heartstring",
        "Heartthrob",
        "Honey",
        "Hun",
        "Ki",
        "Kitten",
        "Kitty",
        "Love",
        "Nat Nat",
        "Nat",
        "NatNat",
        "Nat-Nat",
        "Natsu",
        "Natty",
        "Nattykins",
        "Precious",
        "Princess",
        "Qt Pie",
        "QT",
        "Su",
        "Sugar",
        "Suki",
        "Summer",
        "Sunshine",
        "Sweetheart",
        "Sweetie",
        "Sweetness",
        "Sweety"
    ]

    # Natsuki dislikes these nicknames; no penalty given but name will not be permitted
    NICKNAME_DISLIKED_LIST = [
        "Dad",
        "Daddy",
        "Lily",
        "Moni",
        "Monika",
        "MonMon",
        "Mon-Mon",
        "Papa",
        "Sayo",
        "Sayori",
        "Yuri"
    ]

    # Natsuki hates these (non-profanity) nicknames; awarding them detracts affinity/trust
    NICKNAME_HATED_LIST = [
        "Brat",
        "Child",
        "Gremlin",
        "Kid"
    ]

    # Being rude detracts affinity/trust
    NICKNAME_PROFANITY_LIST = [

    ]

    # Natsuki finds these nicknames funny, but name will not be permitted
    NICKNAME_FUNNY_LIST = [
        "Gorgeous",
        "Hot stuff",
        "Hottie",
        "Mama",
        "Mom",
        "Mommy",
        "Mother",
        "Mum",
        "Mummy",
        "Sexy"
    ]

    """
    Returns the nickname type for a given nickname, defaulting to NICKNAME_TYPE_NEUTRAL

    IN:
        nickname - The nickname to test if within type lists
    OUT:
        Nickname type, integer as defined in constant list
    """
    def get_nickname_approval(nickname):
        if nickname in NICKNAME_LOVED_LIST:
            return NICKNAME_TYPE_LOVED

        elif nickname in NICKNAME_DISLIKED_LIST:
            return NICKNAME_TYPE_DISLIKED

        elif nickname in NICKNAME_HATED_LIST:
            return NICKNAME_TYPE_HATED

        elif nickname in NICKNAME_PROFANITY_LIST:
            return NICKNAME_TYPE_PROFANITY

        elif nickname in NICKNAME_FUNNY_LIST:
            return NICKNAME_TYPE_FUNNY

        else:
            return NICKNAME_TYPE_NEUTRAL