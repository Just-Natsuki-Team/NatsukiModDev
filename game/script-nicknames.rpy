# Nickname data
default persistent.jn_player_nicknames_allowed = True
default persistent.jn_player_nicknames_current_nickname = "Natsuki"
default persistent.jn_player_nicknames_bad_given_total = 0

init 0 python in jn_nicknames:
    import store.jn_globals as jn_globals
    
    # Nickname types
    TYPE_INVALID = 0
    TYPE_LOVED = 1
    TYPE_NEUTRAL = 2
    TYPE_DISLIKED = 3
    TYPE_HATED = 4
    TYPE_PROFANITY = 5
    TYPE_FUNNY = 6
    TYPE_NOU = 7
    
    # Natsuki loves these nicknames; awarding them awards affinity/trust
    NICKNAME_LOVED_LIST = {
        "babe",
        "amazing",
        "angel",
        "babygirl",
        "baby",
        "babycakes",
        "beautiful",
        "bestgirl",
        "betterhalf",
        "boo",
        "bunbun",
        "bun-bun",
        "bunny",
        "buttercup",
        "butterscotch",
        "candy",
        "cookie",
        "cupcake",
        "cuteypie",
        "cutey",
        "cutiepie",
        "cutie",
        "darlin",
        "darling",
        "doll",
        "dollface",
        "dove",
        "gem",
        "gorgeous",
        "heartstring",
        "heart-string",
        "heartthrob",
        "heart-throb",
        "heaven",
        "honey",
        "honeybun",
        "hun",
        "ki",
        "kitten",
        "kitty",
        "love",
        "mine",
        "myflower",
        "mylove",
        "mylovely",
        "myprincess",
        "myqueen",
        "myrose",
        "natnat",
        "nat",
        "nat-nat",
        "natsu",
        "natsukitten",
        "natsukitty",
        "natty",
        "nattykins",
        "numberone",
        "precious",
        "princess",
        "qtpie",
        "qt",
        "queen",
        "snooki",
        "snookums",
        "special",
        "squeeze",
        "starlight",
        "starshine",
        "su",
        "sugar",
        "sugarlump",
        "sugarplum",
        "'suki",
        "suki",
        "summer",
        "sunny",
        "sunshine",
        "sweetcakes",
        "sweetpea",
        "sweetheart",
        "sweetie",
        "sweetness",
        "sweety"
        "thebest"
    }

    # Natsuki dislikes these nicknames; no penalty given but name will not be permitted
    NICKNAME_DISLIKED_LIST = {
        "dad",
        "daddy",
        "father",
        "lily",
        "moni",
        "monika",
        "monikins",
        "monmon",
        "mon-mon",
        "papa",
        "sayo",
        "sayori",
        "yori",
        "yuri",
        "weeb"
    }

    # Natsuki hates these (non-profanity) nicknames; awarding them detracts affinity/trust
    NICKNAME_HATED_LIST = {
        "arrogant",
        "brat",
        "bratty",
        "bonebag",
        "bonehead",
        "breadboard",
        "child",
        "clown",
        "cuttingboard",
        "dog",
        "dunce",
        "dumbo",
        "dimwit",
        "disgusting",
        "dumb",
        "dumbo",
        "dwarf",
        "dweeb",
        "fat",
        "fatso",
        "fatty",
        "flat",
        "flatty",
        "flatso",
        "gremlin",
        "halfling",
        "halfwit",
        "half-pint",
        "halfpint",
        "horrible",
        "horrid",
        "hungry",
        "gross",
        "idiot",
        "ignoramus",
        "ignorant",
        "imbecile",
        "imp",
        "ironingboard",
        "kid",
        "midget",
        "moron",
        "nasty",
        "neckcrack",
        "necksnap",
        "neck-crack",
        "neck-snap",
        "nerd",
        "nimrod",
        "nuisance",
        "pest",
        "punchbag",
        "punch-bag",
        "punching-bag",
        "punchingbag",
        "putrid",
        "short",
        "shorty",
        "shortstuff",
        "sick",
        "simpleton",
        "skinny",
        "slave",
        "smelly",
        "starved",
        "starving",
        "stinky",
        "stuck-up",
        "stupid",
        "tiny",
        "twerp",
        "twit",
        "useless",
        "vendingmachine",
        "vomit",
        "washboard",
        "wretch"
    }

    # Natsuki finds these nicknames funny
    NICKNAME_FUNNY_LIST = {
        "catsuki",
        "gorgeous",
        "hot",
        "hotstuff",
        "hottie",
        "nyatsuki",
        "mama",
        "mom",
        "mommy",
        "mother",
        "mum",
        "mummy",
        "sexy",
        "smol",
        "snack"
    }

    NICKNAME_NOU_LIST = {
        "adorkable",
        "baka",
        "booplicate",
        "booplic8",
        "booplik8",
        "boopliqeeb",
        "boopliqeb",
        "dummy",
        "qab",
        "qeb",
        "qeeb",
        "qebqeb",
        "qebweb",
        "qib",
        "qob",
        "qoob",
        "qub",
        "web",
        "webqeb",
        "woob",
        "wob"
    }

    def get_nickname_type(nickname):
        """
        Returns the nickname type for a given string nickname, defaulting to TYPE_NEUTRAL

        IN:
            nickname - The nickname to test
        OUT:
            Nickname type, integer as defined in constant list
        """

        if not isinstance(nickname, basestring):
            return TYPE_INVALID
        
        else:
            nickname = nickname.lower().replace(" ", "")

            if nickname in NICKNAME_LOVED_LIST:
                return TYPE_LOVED

            elif nickname in NICKNAME_DISLIKED_LIST:
                return TYPE_DISLIKED

            elif nickname in NICKNAME_HATED_LIST:
                return TYPE_HATED

            elif nickname in jn_globals.PROFANITY_LIST:
                return TYPE_PROFANITY

            elif nickname in NICKNAME_FUNNY_LIST:
                return TYPE_FUNNY

            elif nickname in NICKNAME_NOU_LIST:
                return TYPE_NOU

            else:
                return TYPE_NEUTRAL
