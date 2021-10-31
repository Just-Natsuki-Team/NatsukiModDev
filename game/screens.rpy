## Initialization
################################################################################

init offset = -1

init python:
    import random

    # These dialogue sets are used on the Quit modal, where the indexes of each set are used as follows:
    # [0]: Confirm prompt header
    # [1]: Response on choosing to leave via Continue
    # [2]: Response on choosing to stay via Go Back
    QUIT_HIGH_AFFINITY_DIALOGUE = [
        [
            "Wait, you're leaving? You could at least say goodbye first, you know...",
            "[player]...\n {0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Ehehe. Thanks, [player]~ \n{0}".format(random.choice(jn_globals.DEFAULT_HAPPY_EMOTICONS))
        ],
        [
            "W-wait, what? Aren't you going to say goodbye first, [player]?",
            "Come on, [player]...\n{0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Thanks, [player]! \n{0}".format(random.choice(jn_globals.DEFAULT_HAPPY_EMOTICONS))
        ],
        [
            "Come on, [player]... at least say goodbye to me first?",
            "Why, [player]...? \n{0}".format(random.choice(jn_globals.DEFAULT_SAD_EMOTICONS)),
            "Thanks a bunch, [player]~ \n{0}".format(random.choice(jn_globals.DEFAULT_HAPPY_EMOTICONS)),
        ]
    ]

    QUIT_MEDIUM_AFFINITY_DIALOGUE = [
        [
            "H-huh? You're leaving? You could at least say goodbye properly!",
            "[player]! Come on...\n {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "Y-yeah! That's what I thought. Ahaha..."
        ],
        [
            "W-wait, what? At least say goodbye if you're leaving, [player]!",
            "Ugh... [player]...\n {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "G-good! Good..."
        ],
        [
            "H-hey! You aren't just going to leave like that, are you?",
            "...Really, [player]?\n {0}".format(random.choice(jn_globals.DEFAULT_ANGRY_EMOTICONS)),
            "T-thanks, [player]."
        ]
    ]

    QUIT_LOW_AFFINITY_DIALOGUE = [
        [
            "...Really? I don't even get a 'goodbye' now?",
            "...Jerk.",
            "...Thanks, [player]. I guess."
        ],
        [
            "...You're not even going to bother saying goodbye?",
            "Heh. Yeah. You have a {i}wonderful{/i} day too.",
            "Thanks.",
        ],
        [
            "...Is it really {i}that{/i} much effort to say goodbye properly?",
            "Don't let the door hit you on the way out. \nJerk.",
            "Thank you.",
        ]
    ]

    QUIT_ZERO_AFFINITY_DIALOGUE = [
        [
            "...Going?",
            "...Good riddance.",
            "...Whatever."
        ],
        [
            "...Oh. You're leaving.",
            "...Maybe you shouldn't come back.",
            "Uh huh.",
        ],
        [
            "...Leaving?",
            "Don't hurry back.",
            "Whatever.",
        ]
    ]

    def get_affinity_quit_dialogue():
        """
        Returns a list containing quit dialogue when exiting via game window/main menu quit option, where indexes:
        0: Dialogue before selecting an option
        1: Dialogue for choosing to quit
        2: Dialogue for choosing to stay

        OUT:
            List containing quit dialogue
        """
        if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
            return random.choice(QUIT_HIGH_AFFINITY_DIALOGUE)

        elif jn_affinity.get_affinity_state() >= jn_affinity.NORMAL:
            return random.choice(QUIT_MEDIUM_AFFINITY_DIALOGUE)

        elif jn_affinity.get_affinity_state() >= jn_affinity.DISTRESSED:
            return random.choice(QUIT_LOW_AFFINITY_DIALOGUE)

        else:
            return random.choice(QUIT_ZERO_AFFINITY_DIALOGUE)

################################################################################
## Custom Screens
################################################################################

# Categorized menu
## Similar to MAS' twopane_scrollable menu.
## NOTE: This is meant to be called within a loop so long as the user hasn't clicked `Nevermind`
### PARAMETERS:
#   menu_items: dict
#       { key: category, value: Topic[] }
#
#   category_pane_space: tuple
#       [0] top-left x coord of the category pane
#       [1] top-left y coord of the category pane
#       [2] width of the category pane
#       [3] height of the category pane
#
#   option_list_space:
#       [0] top-left x coord of the options pane
#       [1] top-left y coord of the options pane
#       [2] width of the options pane
#       [3] height of the options pane
#
#   category_length:
#       length of the category, used to calculat
define prev_adjustment = ui.adjustment()
define main_adjustment = ui.adjustment()
define selected_category = None
define scroll_align = -0.1

style categorized_menu_button is choice_button:
    xysize (250, None)
    padding (25, 5, 25, 5)

style categorized_menu_button_text is choice_button_text:
    align (0.0, 0.0)
    text_align 0.0

screen categorized_menu(menu_items, category_pane_space, option_list_space, category_length):
    at categorized_menu_slide_in_right
    style_prefix "categorized_menu"

    #Just entered this menu so just need to list categories
    fixed:
        anchor (0, 0)
        pos (category_pane_space[0], category_pane_space[1])
        xsize category_pane_space[2]
        ysize category_pane_space[3]

        bar:
            adjustment prev_adjustment
            style "classroom_vscrollbar"
            xalign -0.1

        vbox:
            ypos 0
            yanchor 0

            viewport:
                #Apply the old adjustment to keep the style the same
                yadjustment prev_adjustment
                yfill False
                #Allow mousewheel and arrow keys for navigation
                mousewheel True
                arrowkeys True
                vbox:
                    if category_length != 1:
                        if category_length == 0:
                            textbutton _("Nevermind."):
                                action [
                                    Return(False),
                                    Function(prev_adjustment.change, 0),
                                    SetVariable("selected_category", None)
                                ]

                        elif category_length > 1:
                            python:
                                import random

                                go_back_text = "Go back"
                                if random.randint(0, 999) == 999:
                                    go_back_text = "Go baka"

                            textbutton _(go_back_text):
                                style "categorized_menu_button"
                                action [ Return(-1), Function(prev_adjustment.change, 0) ]

                        null height 20

                    for button_name in menu_items.iterkeys():
                        textbutton button_name:
                            style "categorized_menu_button"
                            #Set the selected category
                            action SetVariable("selected_category", button_name)

                        null height 5

    #Safely wrap this check so this screen cannot crash
    #If we have a selected category and need to display the options within it (if there are any)
    if menu_items.get(selected_category):
        fixed:
            area option_list_space

            bar:
                adjustment main_adjustment
                style "classroom_vscrollbar"
                xalign -0.1

            vbox:
                ypos 0
                yanchor 0

                viewport:
                    yadjustment main_adjustment
                    yfill False
                    mousewheel True
                    arrowkeys True

                    vbox:
                        textbutton _("Nevermind."):
                            action [
                                Return(False),
                                Function(prev_adjustment.change, 0),
                                SetVariable("selected_category", None)
                            ]

                        null height 20

                        for _topic in menu_items.get(selected_category):
                            #NOTE: This should be preprocessed such that Topics without prompts aren't passed into this menu
                            textbutton _topic.prompt:
                                style "categorized_menu_button"
                                #Return the label so it can be called
                                action [ Return(_topic.label), Function(prev_adjustment.change, 0), SetVariable("selected_category", None) ]

                            null height 5


screen scrollable_choice_menu(items, last_item=None):
    fixed:
        area (680, 40, 560, 440)
        vbox:
            ypos 0
            yanchor 0

            if last_item:
                textbutton last_item[0]:
                    style "categorized_menu_button"
                    xsize 560
                    action Return(last_item[1])

                null height 20

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    for prompt, _value in items:
                        textbutton prompt:
                            style "categorized_menu_button"
                            xsize 560
                            action Return(_value)

                        null height 5

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align

################################################################################
## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style default_slow is normal:
    slow_cps 10

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


#style bar:
#    ysize gui.bar_size
#    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

#style vscrollbar:
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_up is window:
    background Image("gui/textbox.png", xalign=0.5, yalign=-5.0)

style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"


    window:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items, scroll="viewport"):
    style_prefix "choice"

    vbox:
        xalign 0.9
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style choice_bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style choice_scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style choice_vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style choice_slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style choice_vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style choice_frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 295]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
        elif currentpos[1] > targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
    def RigMouse2():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
    def RigMouse3():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 0]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)


screen force_mouse_move():

    on "show":
        action MouseMove(x=600, y=600, duration=.3)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)
screen rigged_choice3(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse2)
screen rigged_choice2(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse3)


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            if config.developer:
                textbutton _("Restart"):
                    action Show(
                        screen="confirm_editable_closable",
                        message="Do you want to RELOAD or RESET?",
                        yes_text="Reload",
                        no_text="Reset",
                        yes_action=Jump("ch30_autoload"),
                        no_action=Jump("restart")
                    )
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen indicator(message):
    key "mouseup_3" action Return()
    style_prefix "game_menu"

    text (message):
        style "return_button"
        xpos 10 ypos 70

init python:
    def FinishEnterName():
        global player

        if not player:
            return

        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

    def DLC():
        renpy.jump_out_of_context("dlcmenu")

    def FinishEnterAge():
        if not age: return
        return

    def FinishEnterMonth():
        if not month: return
        persistent.bday_month = month
        renpy.hide_screen("month_input")

    def FinishEnterDay():
        if not day: return
        persistent.bday_day = day
        renpy.hide_screen("day_input")

    def DeleteName():
        persistent.playername = ""

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("New Game"):
                action If(
                    persistent.playername,
                    true=Start(),
                    false=Show(
                        screen="name_input",
                        message="Please enter your name",
                        ok_action=Function(FinishEnterName)
                    )
                )

        else:
            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

            textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action Help("README.html")

            ## The quit button is banned on iOS and unnecessary on Android.
            python:
                # Quit message based on affinity
                if jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                    quit_message = "Wait, you're leaving? You could at least say goodbye first, you know..."

                elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                    quit_message = "H-huh? You're leaving? You could at least say goodbye properly!"

                elif jn_affinity.get_affinity_state() >= jn_affinity.ENAMORED:
                    quit_message = "...Really? I don't even get a 'goodbye' now?"

                else:
                    quit_message = "...Going?"

            textbutton _("Quit") action Show(screen="quit", message=quit_message, ok_action=Hide(screen="quit", transition=None))


        textbutton _("Credits") action Show(screen="credits", message="Credits:\nWriting: Edgar.\nArt: u/Aida_Hwedo.\nBeach Art: etched\nBeach Background: Kimagure After Background Material Storage\nPark and Manga Store Background: mugenjohncel (On LemmaSoft forums)\nBakery, Clothes Store and Mall Background: u/SovietSpartan\nTypo and Bug Reporting: Willie\nNatsuki clothing store outfit #1: Eg85_MkWii\nCat Ears: DearWolf\nPriceVille Gallery: Flower\nClipart Library: Cake\nJMO: Original Clothing Art\nJparnaud: Sprite Editing\nKevin Macleod: Spooky Music(Day of Chaos)\nPinclpart: Bats\nNatsuki Low Affinity Beach Outfit: -Http_Bxbygirl-(Reddit)\nNatsuki High Affinity Beach Outfit: Huniepop (Rizky Prahesa)\nNatsuki White Tank: DestinyPveGal\nGlasses: Unknown as of now", ok_action=Hide(screen="credits", transition=None))

        #textbutton _("Latest Update") action OpenURL("https://justnatsukidev.wixsite.com/justnatsuki/latest")

        #if not main_menu and not persistent.prologue:
        #    textbutton _("DLC") action Function(DLC)

        #else:
        #    timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"
    add "menu_bg"
    add "menu_art_n"

    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"

    add "menu_particles"
    if persistent.playthrough != 4:
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):

    # Add the backgrounds.
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="You wont be needing to save anymore,\nBesides it doesn't work when we're sitting doing nothing like this...", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

                #textbutton _("{#auto_page}A") action FilePage("auto")

                #textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

define persistent.room_animation = True

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            vbox:
                yoffset 20

                vbox:
                    style_prefix "check"
                    label _("Random Talking")
                    textbutton _("Enabled") action Show(screen="dialog", message="This will control weather or not Natsuki\nstrikes up conversations oh her own.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"random_talk", True, False)

            vbox:
                yoffset 20

                vbox:
                    style_prefix "check"
                    label _("Youtuber Mode")
                    textbutton _("Enabled") action Show(screen="dialog", message="This will make Natsuki start conversations faster.\nThis is useful for YouTubers who want to get through everything faster.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"youtuber_mode", True, False)

            vbox:
                yoffset -150
                xoffset 250

                vbox:
                    style_prefix "check"
                    label _("Room Animated")
                    textbutton _("Enabled") action Show(screen="reload", message="This will turn off the moving fire\nas some people have reported lag.\nRestart is required.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"room_animated", True, False)

                vbox:
                    style_prefix "check"
                    label _("Resume Music")
                    textbutton _("Enabled") action Show(screen="dialog", message="Turning this on will cause music to resume playing when you return\ninstead of restarting.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"save_music_place", True, False)

            vbox:
                yoffset -320
                xoffset 500

                vbox:
                    style_prefix "check"
                    label _("New Topics")
                    textbutton _("Enabled") action Show(screen="dialog", message="This will cause Natsuki to only say topics added in the update.\nThis ONLY has her say topics in that update.\nSo don't be surprised if it doesn't change for a while.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"new_topics", True, False)

                vbox:
                    style_prefix "check"
                    label _("New Emotions")
                    textbutton _("Enabled") action Show(screen="dialog", message="This will cause Natsuki's emotions to change over time. Turning this off sets her emotion to normal.", ok_action=Hide(screen="dialog", transition=None)), ToggleField(persistent,"dynamic_emotions", True, False), SetField(persistent,"natsuki_emotion", "Happy")

                if not persistent.dynamic_emotions:
                    vbox:
                        style_prefix "navigation"
                        textbutton _("Choose Emotion") action Show(screen="emotion", message="If you turn off Natsuki's new emotion system\nyou can always just pick an emotion for her to use!\n(The change is not instant, just wait.)", close=Hide(screen="emotion", transition=None))

                vbox:
                    style_prefix "navigation"
                    textbutton _("Debug") action Show(screen="confirm", message="This action will hard reset Just Natsuki!\nYou're only supposed to use it if the game starts up, Natsuki greets you, and then it given an exception.\nThe best way to fix this is to reset the game after an update patches the issue.\nThis option allows you to do that.\nAre you sure you want to PERMANENTLY erase all your Just Natsuki save data?", yes_action=Jump("restart"), no_action=Hide("confirm"))

            vbox:
                yoffset 20

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    #bar value Preference("text speed")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Help"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
#
#            if device == "keyboard":
#                use keyboard_help
#            elif device == "mouse":
#                use mouse_help
#            elif device == "gamepad":
#                use gamepad_help
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Space")
#        text _("Advances dialogue without selecting choices.")
#
#    hbox:
#        label _("Arrow Keys")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Escape")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Skips dialogue while held down.")
#
#    hbox:
#        label _("Tab")
#        text _("Toggles dialogue skipping.")
#
#    hbox:
#        label _("Page Up")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Page Down")
#        text _("Rolls forward to later dialogue.")
#
#    hbox:
#        label "H"
#        text _("Hides the user interface.")
#
#    hbox:
#        label "S"
#        text _("Takes a screenshot.")
#
#    hbox:
#        label "V"
#        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Left Click")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Middle Click")
#        text _("Hides the user interface.")
#
#    hbox:
#        label _("Right Click")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Mouse Wheel Up\nClick Rollback Side")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Mouse Wheel Down")
#        text _("Rolls forward to later dialogue.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Right Trigger\nA/Bottom Button")
#        text _("Advance dialogue and activates the interface.")
#
#    hbox:
#        label ("Left Trigger\nLeft Shoulder")
#        text _("Roll back to earlier dialogue.")
#
#    hbox:
#        label _("Right Shoulder")
#        text _("Roll forward to later dialogue.")
#
#    hbox:
#        label _("D-Pad, Sticks")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Start, Guide")
#        text _("Access the game menu.")
#
#    hbox:
#        label _("Y/Top Button")
#        text _("Hides the user interface.")
#
#    textbutton _("Calibrate") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Additional screens
################################################################################

screen flower:
    imagebutton:
        idle "mod_assets/JustNatsuki/flower.png"
        hover "mod_assets/JustNatsuki/flower.png"
        action [If(allow_dialogue, true=Jump("ch30_flower"))]

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen name_input(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen month_input(ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Please enter your birth month\n(Enter the month with the first letter capitalized, eg January, February, etc)"):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("month") length 15 allow "ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuv"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Confirm") action ok_action

screen day_input(ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Please enter your birth day\n(Enter as a number, eg 22)"):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("day") length 2 allow "123456789"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Confirm") action ok_action

screen age_input(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("age") length 12 allow "don'twanttoanswer1234567890 "

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen dialog(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen start_dlc_check(message):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

screen reload(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Restart") action Quit(confirm=True)


            hbox:
                xalign 0.5
                spacing 50

                textbutton _("I'll do it myself") action Hide("reload")

screen custommusic(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Don't show again") action ToggleField(persistent,"show_again", False, True)


            hbox:
                xalign 0.5
                spacing 50

                textbutton _("OK") action ok_action

screen emotion(message, close):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Happy") action SetField(persistent,"natsuki_emotion", "Happy")

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Casual") action SetField(persistent,"natsuki_emotion", "Casual")

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Angry") action SetField(persistent,"natsuki_emotion", "Angry")

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Sad") action SetField(persistent,"natsuki_emotion", "Sad")


            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Nevermind") action close

screen dlc(message):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            #hbox:
                #xalign 0.5
                #spacing 50
                #style_prefix "check"
                #textbutton _("Natsuki's Kitchen!") action If(persistent.using_space_dlc, true=ToggleField(persistent,"using_space_dlc", True, False), false=Jump("space_dlc_check"))

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Natsuki's Kitchen!") action Show(screen="dialog", message="This DLC is not released yet.", ok_action=Hide("dialog"))

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Natsuki's Night Out!") action Show(screen="dialog", message="This DLC is not released yet.", ok_action=Hide("dialog"))

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("Natsuki's Magical Adventure!") action Show(screen="dialog", message="This DLC is not released yet.", ok_action=Hide("dialog"))

            hbox:
                xalign 0.5
                spacing 50
                style_prefix "check"
                textbutton _("(Unavailable)") action NullAction()


            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Close") action Return

screen quit(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("No") action ok_action

screen endgame(message): # No spoilers, promise!

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

screen credits(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Good work!") action ok_action

screen credits2(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("FAJNCAKJ") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen memory:

    text "Monika will remember that...":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"



screen confirm(message, yes_action, no_action):

    # If this is a quit confirmation, begin personification so we can work Natsuki into this
    if message == layout.QUIT:
        python:
            confirm_is_quit = True
            quit_dialogue = get_affinity_quit_dialogue()
            message = quit_dialogue[0]

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                if confirm_is_quit:
                    textbutton _("Continue") action Show(screen="confirm_quit", is_quitting=True)
                    textbutton _("Go back") action Show(screen="confirm_quit", is_quitting=False)

                else:
                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action

screen confirm_quit(is_quitting):
    modal True

    zorder 300

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    action Hide("confirm")

    if is_quitting:
        $ quit_label = get_affinity_quit_dialogue()[1]
    else:
        $ quit_label = get_affinity_quit_dialogue()[2] 

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(quit_label):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                
                if is_quitting:
                    textbutton _("...") action [
                        # Player has decided to ditch Natsuki; add a pending apology then quit
                        apologies.add_new_pending_apology(apologies.APOLOGY_TYPE_SUDDEN_LEAVE),
                        SetField(persistent, "jn_player_apology_type_on_quit", apologies.APOLOGY_TYPE_SUDDEN_LEAVE),
                        relationship("affinity-"),
                        Quit(confirm=False)
                    ]
                else:
                    textbutton _("OK") action [
                        # Player is a decent person; hide the screens
                        Hide("confirm"),
                        Hide("confirm_quit")
                    ]

screen confirm_editable(message, yes_text, no_text, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _(yes_text) action yes_action
                textbutton _(no_text) action no_action

screen confirm_editable_closable(message, yes_text, no_text, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch" xalign 0.5

            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5
                textbutton _("Close") action Hide("confirm_editable_closable"):
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _(yes_text) action yes_action
                textbutton _(no_text) action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size
