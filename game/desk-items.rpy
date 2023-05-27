init -60:
    default persistent._jn_desk_item_list = {} 

init -55 python in jn_desk_items:
    from Enum import Enum
    import store
    import store.jn_utils as jn_utils

    # List of all registered desk items
    __ALL_DESK_ITEMS = {}

    class JNDeskSlots(Enum):
        """
        The different slots that a given desk item can use for display.
        Only a single desk item can be in a given slot at a time.
        """
        left = 1
        centre = 2
        right = 3

    class JNDeskItem:
        """
        Describes a standalone object that Natsuki can have on her desk.
        Desk items are drawn along with Natsuki as a complete image, and share transforms/effects:
        use them when you need something to be persistently positioned through things like menus, etc.
        """
        def __init__(
            self,
            reference_name,
            desk_slot,
            unlocked,
            displayable
        ):
            """
            Constructor.

            IN:
                - reference_name - Str name used to uniquely identify this desk item and refer to it internally
                - desk_slot - JNDeskSlots slot this desk item will take up when displayed
                - unlocked - Bool unlock state of this desk item
                - displayable - Displayable to be shown when this desk item is displayed
            """
            self.reference_name = reference_name
            self.desk_slot = desk_slot
            self.unlocked = unlocked
            self.displayable = displayable

        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each desk item from the persistent.
            """
            global __ALL_DESK_ITEMS
            for desk_item in __ALL_DESK_ITEMS.values():
                desk_item.__load()

        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each desk item to the persistent.
            """
            global __ALL_DESK_ITEMS
            for desk_item in __ALL_DESK_ITEMS.values():
                desk_item.__save()

        def asDict(self):
            """
            Exports a dict representation of this desk item; this is for data we want to persist.

            OUT:
                dictionary representation of the desk item object
            """
            return {
                "unlocked": self.unlocked
            }

        def unlock(self):
            """
            Unlocks this desk item, making it available to the player.
            """
            self.unlocked = True
            self.__save()

        def lock(self):
            """
            Locks this desk item, making it unavailable to the player.
            """
            self.unlocked = False
            self.__save()

        def __load(self):
            """
            Loads the persisted data for this desk item from the persistent.
            """
            if store.persistent._jn_desk_item_list[self.reference_name]:
                self.unlocked = store.persistent._jn_desk_item_list[self.reference_name]["unlocked"]

        def __save(self):
            """
            Saves the persistable data for this desk item to the persistent.
            """
            store.persistent._jn_desk_item_list[self.reference_name] = self.asDict()

    def __registerDeskItem(desk_item):
        """
        Registers a new desk item in the list of all desk items, allowing in-game access and persistency.
        If the desk item has no existing corresponding persistent entry, it is saved.

        IN:
            - desk_item - the JNDeskItem to register.
        """
        if desk_item.reference_name in __ALL_DESK_ITEMS:
            jn_utils.log("Cannot register desk item name: {0}, as a desk item with that name already exists.".format(desk_item.reference_name))

        else:
            __ALL_DESK_ITEMS[desk_item.reference_name] = desk_item
            if desk_item.reference_name not in store.persistent._jn_desk_item_list:
                desk_item.__save()
            
            else:
                desk_item.__load()

    def getDeskItem(reference_name):
        """
        Returns the desk item for the given name, if it exists.

        IN:
            - reference_name - str reference name of the desk item to fetch

        OUT
            - Corresponding JNDeskItem if one exists, otherwise None
        """
        if reference_name in __ALL_DESK_ITEMS:
            return __ALL_DESK_ITEMS[reference_name]

        return None

    __registerDeskItem(JNDeskItem(
        reference_name="jn_joke_book_held",
        desk_slot=JNDeskSlots.centre,
        unlocked=True,
        displayable=store.Image("mod_assets/props/joke_book_held.png")  
    ))

    __registerDeskItem(JNDeskItem(
        reference_name="jn_hammie_damaged",
        desk_slot=JNDeskSlots.left,
        unlocked=False,
        displayable=store.Image("mod_assets/props/plush/hammie/hammie_damaged.png")  
    ))

    __registerDeskItem(JNDeskItem(
        reference_name="jn_hammie_fixed",
        desk_slot=JNDeskSlots.left,
        unlocked=False,
        displayable=store.Image("mod_assets/props/plush/hammie/hammie_fixed.png")  
    ))
