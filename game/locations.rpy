#Start off in the clubroom
default persistent._current_location = "clubroom"

init python in locations:
    import store
    LOCATION_MAP = dict()

init -20 python:
    import os
    class Location(object):
        """
        PROPERTIES:
            - id
            - img_file_path (directory to point to images, ideally names would be derived via id-<time_of_day>)
            - entry_pp
            - exit_pp
            - can_have_deco
            (works for room since the flags and stuff, also sets things up for future. Maybe change this to 'allowed_deco_categories', and we can have decorations via category)
        """

        T_DAY = "-day"
        T_NIGHT = "-night"

        IMG_EXT = ".png"

        def __init__(
            self,
            id,
            image_dir,
            image_fallback=None,
            allowed_deco_categories=None,
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
                allowed_deco_categories - List of strings representing categories for decorations which are supported for this Location
                    If None, this is set to an empty list. Empty lists mean no decorations are supported
                    (Default: None)
                on_entry - Function to run when changing into this Location. If None, nothing is done.
                    (Default: None)
                on_exit - Function to run when leaving this Location. If None, nothing is done.
                    (Default: None)
            """
            #Initial checks to make sure this can be loaded
            if id in store.locations.LOCATION_MAP:
                raise Exception("[ERROR]: A Location with id '{0}' already exists.".format(id))

            if not os.path.isdir(renpy.config.gamedir + "/mod_assets/backgrounds/{0}".format(image_dir)):
                raise Exception(
                    "[ERROR]: Image dir '{0}' is not a directory.".format(
                        os.path.join(renpy.config.gamedir, "mod_assets", "backgrounds", image_dir)
                    )
                )

            #Build the image FPs
            day_image_fp = "mod_assets/backgrounds/{0}/{1}".format(image_dir, id + Location.T_DAY + Location.IMG_EXT)
            night_image_fp = "mod_assets/backgrounds/{0}/{1}".format(image_dir, id + Location.T_NIGHT + Location.IMG_EXT)

            #Verify the day image is loadable
            if not renpy.loadable(day_image_fp):
                raise Exception("[ERROR]: Day image ('{0}') is not loadable.".format(day_image_fp))

            #And the night
            if not renpy.loadable(night_image_fp):
                raise Exception("[ERROR]: Night image ('{0}') is not loadable.".format(night_image_fp))

            #Now that all checks have passed, we should create the object
            self.id = id
            self.day_image = Image(day_image_fp)
            self.night_image = Image(night_image_fp)

            if allowed_deco_categories is None:
                self.allowed_deco_categories = list()

            self.on_entry = on_entry
            self.on_exit = on_exit

        def getCurrentRoomImage(self, Room):
            """
            Gets the current room image

            IN:
                Room - the current Room
            """
            if Room.is_day():
                return self.day_image
            return self.night_image

    class Room(object):
        """
        The main representation of the room.
        """
        def __init__(self):
            """
            Room constructor

            This will be the object which represents the current location, managing decorations for the room and everything
            """
            self.location = None
            self.deco = dict()
            #TODO: make this dynamic
            self.sunrise = datetime.time(6)
            self.sunset = datetime.time(19)
            self.__is_showing_day_image = None

        def setLocation(self, new_location, **kwargs):
            """
            Sets the location. Does NOT run exit prog points for the current location

            IN:
                new_location - new location
                **kwargs - keword arguments to pass to the prog points
            """
            #Run entry prog points
            if new_location.on_entry is not None:
                new_location.on_entry(self.location, **kwargs)

            self.location = new_location

        def changeLocation(self, new_location, **kwargs):
            """
            Changes the location

            IN:
                new_location - new location
                **kwargs - keyword arguments to pass to the prog points
            """
            if self.location.on_exit is not None:
                self.location.on_exit(new_location, **kwargs)

            self.setLocation(new_location, **kwargs)

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

            if full_redraw:
                room = self.location.getCurrentRoomImage()

            if room is not None and not renpy.showing(room):
                renpy.show(room, tag="main_bg", zorder=1)

            # dissolving everything means dissolve last
            if dissolve_all or full_redraw:
                renpy.with_statement(Dissolve(1.0))
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
            if self.is_day() and not self.is_showing_day_room():
                self.draw(full_redraw=True)
                self.__is_showing_day_image = True

            #If it's night and we're showing the day room, we should do a full redraw to show the night room
            elif not self.is_day() and self.is_showing_day_room():
                self.draw(full_redraw=True)
                self.__is_showing_day_image = False

init python:
    main_background = Room()

    classroom = Location(
        id="classroom",
        image_dir="classroom"
    )

    main_background.setLocation(classroom)
