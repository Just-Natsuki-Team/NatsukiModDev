init -30:
    #Start off in the clubroom
    default persistent._current_location = "classroom"
    default persistent._jn_furniture_list = {}

    # These determine when the sun rises/sets
    default persistent._jn_sunrise_hour = 6
    default persistent._jn_sunset_hour = 19

init -20 python in jn_locations:
    import datetime
    import os
    import store
    import store.jn_utils as jn_utils

    LOCATION_MAP = dict()
    __LOCATION_ZORDER = 1
    __FURNITURE_ZORDER = 2

    __ALL_FURNITURE = {}

    class JNLocation(object):
        """
        PROPERTIES:
            - id
            - img_file_path (directory to point to images, ideally names would be derived via id-<time_of_day>)
            - entry_pp
            - exit_pp
            (works for room since the flags and stuff, also sets things up for future. Maybe change this to 'allowed_deco_categories', and we can have decorations via category)
        """

        T_DAY = "-day"
        T_NIGHT = "-night"

        IMG_EXT = ".png"

        def __init__(
            self,
            id,
            image_dir,
            furniture=None,
            image_fallback=None,
            on_entry=None,
            on_exit=None,
        ):
            """
            Location constructor

            IN:
                id - a unique id for this background. Will raise exceptions if a Location with a duplicate initialized
                image_dir - a filepath containing the day and night (and other) associated images for this Location
                image_fallback - a dict of image tags with the following keys:
                    "DAY", "NIGHT", these will have image tags as their values, which should be used to display
                on_entry - Function to run when changing into this Location. If None, nothing is done.
                    (Default: None)
                on_exit - Function to run when leaving this Location. If None, nothing is done.
                    (Default: None)
            """
            #Initial checks to make sure this can be loaded
            if id in LOCATION_MAP:
                raise Exception("[ERROR]: A Location with id '{0}' already exists.".format(id))

            if not os.path.isdir(renpy.config.gamedir + "/mod_assets/backgrounds/{0}".format(image_dir)):
                raise Exception(
                    "[ERROR]: Image dir '{0}' is not a directory.".format(
                        os.path.join(renpy.config.gamedir, "mod_assets", "backgrounds", image_dir)
                    )
                )

            #Build the image FPs
            day_image_fp = "mod_assets/backgrounds/{0}/{1}".format(image_dir, id + JNLocation.T_DAY + JNLocation.IMG_EXT)
            night_image_fp = "mod_assets/backgrounds/{0}/{1}".format(image_dir, id + JNLocation.T_NIGHT + JNLocation.IMG_EXT)

            #Verify the day image is loadable
            if not renpy.loadable(day_image_fp):
                raise Exception("[ERROR]: Day image ('{0}') is not loadable.".format(day_image_fp))

            #And the night
            if not renpy.loadable(night_image_fp):
                raise Exception("[ERROR]: Night image ('{0}') is not loadable.".format(night_image_fp))

            #Now that all checks have passed, we should create the object
            self.id = id

            #Make the tags
            self.day_image_tag = "{0}_day".format(id)
            self.night_image_tag = "{0}_night".format(id)

            #Register the images
            renpy.display.image.images.update({
                (self.day_image_tag,): store.Image(day_image_fp),
                (self.night_image_tag,): store.Image(night_image_fp)
            })

            self.furniture = furniture
            for furniture_item in self.furniture:
                furniture_item.register_images_for_location(self.id)

            self.on_entry = on_entry
            self.on_exit = on_exit

        def get_current_room_image(self):
            """
            Gets the current room image
            """
            if store.main_background.is_day():
                return self.day_image_tag
            return self.night_image_tag

    class JNRoom(object):
        """
        The main representation of the room.
        """
        def __init__(self, sunrise_hour, sunset_hour):
            """
            Room constructor

            This will be the object which represents the current location, managing decorations for the room and everything
            """
            self.location = None
            self.deco = dict()
            self.sunrise = datetime.time(sunrise_hour)
            self.sunset = datetime.time(sunset_hour)

            #States
            self.__is_showing_day_image = self.is_day()

            #Eventhandlers
            self.day_to_night_event = store.JNEvent()
            self.night_to_day_event = store.JNEvent()

        def set_location(self, new_location, **kwargs):
            """
            Sets the location. Does NOT run exit prog points for the current location

            Also does not set persistent

            IN:
                new_location - new location
                **kwargs - keword arguments to pass to the prog points
            """
            #Run entry prog points
            if new_location.on_entry is not None:
                new_location.on_entry(self.location, **kwargs)

            self.location = new_location

        def change_location(self, new_location, **kwargs):
            """
            Changes the location

            IN:
                new_location - new location
                **kwargs - keyword arguments to pass to the prog points
            """
            if self.location.on_exit is not None:
                self.location.on_exit(new_location, **kwargs)

            self.set_location(new_location, **kwargs)

        def is_day(self):
            """
            Checks if it's day right now

            OUT:
                True if day
                False if night
            """
            return self.sunrise <= datetime.datetime.now().time() < self.sunset

        def draw(self, dissolve_all=False, full_redraw=False):
            """
            Draws the location

            IN:
                dissolve_all - Whether or not we should dissolve the entire draw
                full_redraw - Whether or not we wish to redraw entirely
            """
            renpy.with_statement(None)

            if full_redraw:
                renpy.scene()
                renpy.show("black")

            room = None

            if dissolve_all or full_redraw:
                room = self.location.get_current_room_image()

            #Draw the room if we're not showing it already
            if room is not None:
                renpy.show(room, tag="main_bg", zorder=__LOCATION_ZORDER)
                if self.location.furniture:
                    for furniture in self.location.furniture:
                        furniture.show(self.location.id)

            else:
                jn_utils.log("Unable to draw room: no room image was found.")

            # dissolving everything means dissolve last
            if dissolve_all or full_redraw:
                renpy.hide("black")
                renpy.with_statement(store.Dissolve(1.0))
            return

        def show(self):
            """
            Draws the location without any transition/scene effects.
            """
            room = self.location.get_current_room_image()
            if room is not None:
                renpy.show(room, tag="main_bg", zorder=__LOCATION_ZORDER)

                if self.location.furniture:
                    for furniture in self.location.furniture:
                        furniture.show(self.location.id)

            else:
                jn_utils.log("Unable to show room: no room image was found.")
            
            return

        def is_showing_day_room(self):
            """
            Checks if we're showing the day room
            """
            return self.__is_showing_day_image

        def check_redraw(self):
            """
            Checks if we need to redraw the room for a time change
            """
            #If it's day and we're showing the night room, we should full redraw to show day room again
            if self.is_day() and self.__is_showing_day_image is False:
                self.__is_showing_day_image = True
                self.draw(dissolve_all=True)

                #Run events
                self.night_to_day_event()

            #If it's night and we're showing the day room, we should do a full redraw to show the night room
            elif not self.is_day() and self.__is_showing_day_image is True:
                self.__is_showing_day_image = False
                self.draw(dissolve_all=True)

                #Run events
                self.day_to_night_event()

        def save(self):
            """
            Saves room related into to persistent
            """
            store.persistent._current_location = self.location.id

    class JNFurniture():
        def __init__(
            self,
            reference_name,
            display_name,
            unlocked,
            marked_interactive=False,
            label=None
        ):
            """
            Initialises a new instance of JNFurniture.

            IN:
                - reference_name - The name used to uniquely identify this furniture item and refer to it internally
                - display_name - Name displayed to the user
                - unlocked - Whether or not this furniture can be seen ingame
                - marked_interactive - Whether hovering over this furniture should display a highlight, and play a sound
                - label - Optional label to jump to when this furniture item is clicked
            """
            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = unlocked
            self.marked_interactive = marked_interactive
            self.label = label

        def __load(self):
            """
            Loads the persisted data for this furniture item from the persistent.
            """
            if store.persistent._jn_furniture_list[self.reference_name]:
                self.unlocked = store.persistent._jn_furniture_list[self.reference_name]["unlocked"]

        def __save(self):
            """
            Saves the persistable data for this furniture item to the persistent.
            """
            store.persistent._jn_furniture_list[self.reference_name] = self.as_dict()

        @staticmethod
        def load_all():
            """
            Loads all persisted data for each furniture item from the persistent.
            """
            global __ALL_FURNITURE
            for furniture in __ALL_FURNITURE.itervalues():
                furniture.__load()

        @staticmethod
        def save_all():
            """
            Saves all persistable data for each furniture item to the persistent.
            """
            global __ALL_FURNITURE
            for furniture in __ALL_FURNITURE.itervalues():
                furniture.__save()

        def as_dict(self):
            """
            Exports a dict representation of this furniture item; this is for data we want to persist.

            OUT:
                dictionary representation of the furniture object
            """
            return {
                "unlocked": self.unlocked
            }

        def lock(self):
            """
            Locks this furniture item, making it unavailable to the player.
            """
            self.unlocked = False
            self.__save()

        def unlock(self):
            """
            Unlocks this furniture item, making it available to the player.
            """
            self.unlocked = True
            self.__save()

        def register_images_for_location(self, location):
            """
            For a given location, create the images for this piece of furniture for day and night.

            IN:
                - location - The location id to create images for
            """
            day_image_path = "mod_assets/furniture/{0}/{1}/day.png".format(self.reference_name, location)
            night_image_path = "mod_assets/furniture/{0}/{1}/night.png".format(self.reference_name, location)

            if not renpy.loadable(day_image_path):
                raise Exception("[ERROR]: Day image ('{0}') is not loadable.".format(day_image_path))

            if not renpy.loadable(night_image_path):
                raise Exception("[ERROR]: Night image ('{0}') is not loadable.".format(night_image_path))

            day_image_tag = "furniture_{0} {1} day".format(self.reference_name, location)
            night_image_tag = "furniture_{0} {1} night".format(self.reference_name, location)
            renpy.image(day_image_tag, store.Image(day_image_path))
            renpy.image(night_image_tag, store.Image(night_image_path))

        def show(self, location):
            """
            Shows this furniture in the room.
            """
            self.hide(location)
            if self.unlocked:
                time_tag = "day" if store.jn_is_day() else "night"
                renpy.show(name="furniture_{0} {1} {2}".format(self.reference_name, location, time_tag), zorder=__FURNITURE_ZORDER)

        def hide(self, location):
            """
            Hides this furniture in the room.
            """
            renpy.hide("furniture_{0}".format(self.reference_name))

    def __register_furniture(furniture):
        """
        Registers a new furniture item in the list of all furniture, allowing in-game access and persistency.
        If the furniture has no existing corresponding persistent entry, it is saved.

        IN:
            - furniture - the JNFurniture to register.
        """
        store.jn_utils.log("type of store.persistent._jn_furniture_list is {0}".format(type(store.persistent._jn_furniture_list)))

        if furniture.reference_name in __ALL_FURNITURE:
            jn_utils.log("Cannot register furniture name: {0}, as an furniture item with that name already exists.".format(furniture.reference_name))

        else:
            __ALL_FURNITURE[furniture.reference_name] = furniture
            if furniture.reference_name not in store.persistent._jn_furniture_list:
                furniture.__save()

    def furniture_exists(furniture_name):
        """
        Returns whether the given furniture exists in the list of registered furniture items.

        IN:
            - furniture_name - str furniture name to search for

        OUT: True if it exists, otherwise False
        """
        return furniture_name in __ALL_FURNITURE

    def get_furniture(furniture_name):
        """
        Returns the furniture for the given name, if it exists.

        IN:
            - furniture_name - str furniture name to fetch

        OUT: Corresponding JNFurniture if the furniture exists, otherwise None 
        """
        if furniture_exists(furniture_name):
            return __ALL_FURNITURE[furniture_name]

        return None

    __register_furniture(JNFurniture(
        reference_name="jn_malta_beanbag",
        display_name="Malta beanbag",
        unlocked=False
    ))
    __register_furniture(JNFurniture(
        reference_name="jn_pink_bookcase",
        display_name="Pink bookcase",
        unlocked=False
    ))

init python:
    import datetime
    import store.jn_locations as jn_locations

    main_background = jn_locations.JNRoom(
        sunrise_hour=int(store.persistent._jn_sunrise_hour),
        sunset_hour=int(store.persistent._jn_sunset_hour)
    )

    classroom = jn_locations.JNLocation(
        id="classroom",
        image_dir="classroom",
        furniture=[
            jn_locations.get_furniture("jn_malta_beanbag"),
            jn_locations.get_furniture("jn_pink_bookcase"),
        ]
    )

    beach = jn_locations.JNLocation(
        id="beach",
        image_dir="beach",
        furniture=list()
    )

    main_background.set_location(classroom)

    #Register the event handlers to handle button sounds
    def __change_to_night_button_sounds():
        gui.hover_sound = "mod_assets/buttons/sounds/button_hover_night.ogg"
        gui.activate_sound = "mod_assets/buttons/sounds/button_click_night.ogg"

    def __change_to_day_button_sounds():
        gui.hover_sound = "mod_assets/buttons/sounds/button_hover_day.ogg"
        gui.activate_sound = "mod_assets/buttons/sounds/button_click_day.ogg"

    main_background.day_to_night_event += __change_to_night_button_sounds
    main_background.night_to_day_event += __change_to_day_button_sounds

    #Now, run the appropriate eventhandler
    #If it's day now, we need to run night to day, and vice versa
    if main_background.is_day():
        main_background.night_to_day_event()

    else:
        main_background.day_to_night_event()

    if persistent._current_location in jn_locations.LOCATION_MAP:
        main_background.change_location(persistent._current_location)
