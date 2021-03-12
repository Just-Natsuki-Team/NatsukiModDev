#This is a copy of console.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for console.rpy
#This script defines the "fake console" that sometimes appears in the game when
#monika deletes characters

#A gray semi-transparent overlay on the screen
image console_bg:
    "#333"
    topleft
    alpha 0.75 size (480,180)

#Styling for the console text
style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []
    #slow_cps 20

style console_text_console is console_text:
    slow_cps 30

default consolehistory = []
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

#This defines a function that displays text in the console
label updateconsole(text="", history=""):
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    show console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory(history) from _call_updateconsolehistory
    pause 0.5
    return

#This function clears the console history
label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    pause 0.5
    return

#Seems to be an unused alternative console function
label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole(drawtext=currenttext) from _call_drawconsole
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ renpy.pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    pause 0.5
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory(history) from _call_updateconsolehistory_1
    pause 0.5
    return

    label drawconsole(drawtext=""):
        #$ cursortext = "_".rjust(len(drawtext) + 1)
        show console_text "[drawtext]_" as ctext zorder 100
        #show console_text cursortext as ccursor zorder 100
        return

#This adds the passed text to the console history
label updateconsolehistory(text=""):
    if text:
        python:
            consolehistory.insert(0, text)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history "[consolehistorydisplay]" as chistory zorder 100
    return

#This hides all of the parts of the console
label hideconsole:
    hide console_bg
    hide console_caret
    #hide ccursor
    hide ctext
    hide chistory
