#Start off in the clubroom
default persistent._current_location = "classroom"

# These determine when the sun rises/sets
default persistent.jn_sunrise_hour = 6
default persistent.jn_sunset_hour = 19

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

            #Make the tags
            self.day_image_tag = "{0}_day".format(id)
            self.night_image_tag = "{0}_night".format(id)

            #Register the images
            renpy.display.image.images.update({
                (self.day_image_tag,): Image(day_image_fp),
                (self.night_image_tag,): Image(night_image_fp)
            })

            if allowed_deco_categories is None:
                self.allowed_deco_categories = list()

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
            self.day_to_night_event = JNEvent()
            self.night_to_day_event = JNEvent()

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
            if room is not None and not renpy.showing("main_bg"):
                renpy.show(room, tag="main_bg", zorder=1)

            renpy.show("natsuki idle", at_list=[jn_center], zorder=3)

            # dissolving everything means dissolve last
            if dissolve_all or full_redraw:
                renpy.hide("black")
                renpy.with_statement(Dissolve(1.0))
            return

        def appear(self, natsuki_sprite_code=""):
            """
            Draws the location without any transition/scene effects.

            IN:
                - natsuki_sprite_code - Optional sprite code for Natsuki
            """
            room = self.location.get_current_room_image()
            if room is not None and not renpy.showing("main_bg"):
                renpy.show(room, tag="main_bg", zorder=1)
            
            natsuki_sprite = "natsuki {0}".format(natsuki_sprite_code) if natsuki_sprite_code else "natsuki idle"
            renpy.show(natsuki_sprite, at_list=[jn_center], zorder=3)
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
            persistent._current_location = self.location.id

init python:

    main_background = JNRoom(
        sunrise_hour=int(store.persistent.jn_sunrise_hour),
        sunset_hour=int(store.persistent.jn_sunset_hour)
    )

    classroom = Location(
        id="classroom",
        image_dir="classroom"
    )

    beach = Location(
        id="beach",
        image_dir="beach"
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

    if persistent._current_location in locations.LOCATION_MAP:
        main_background.change_location(persistent._current_location)
