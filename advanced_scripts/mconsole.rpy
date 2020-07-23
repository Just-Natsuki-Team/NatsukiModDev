#This is a copy of console.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for console.rpy
#This script defines Monika's console. The one she uses to battle Natsuki.

#A gray semi-transparent overlay on the screen
image mconsole_bg:
    "#333"
    topright
    alpha 0.75 size (480,180)

#Styling for the console text
style mconsole_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#04FF00"
    size 18
    outlines []
    #slow_cps 20

style console_text_console is console_text:
    slow_cps 30

default mconsolehistory = []
image mconsole_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=830, ypos=10)
image mconsole_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=830, ypos=50)
image mconsole_caret = Text(">", style="console_text", anchor=(0,0), xpos=810, ypos=10)

#This defines a function that displays text in the console
label mupdateconsole(text="", history=""):
    show mconsole_bg zorder 100
    show mconsole_caret zorder 100
    show mconsole_text "_" as ctext zorder 100
    show mconsole_text "[text]" as ctext zorder 100
    $ pause(len(text) / 830.0 + 0.5)
    hide ctext
    show mconsole_text "_" as ctext zorder 100
    call mupdateconsolehistory(history)
    pause 0.5
    return

#This function clears the console history
label mupdateconsole_clearall(text="", history=""):
    $ pause(len(text) / 830.0 + 0.5)
    pause 0.5
    return

#Seems to be an unused alternative console function
label mupdateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label mupdateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole(drawtext=currenttext)
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
    call updateconsolehistory(history)
    pause 0.5
    return

    label mdrawconsole(drawtext=""):
        #$ cursortext = "_".rjust(len(drawtext) + 1)
        show console_text "[drawtext]_" as ctext zorder 100
        #show console_text cursortext as ccursor zorder 100
        return

#This adds the passed text to the console history
label mupdateconsolehistory(text=""):
    if text:
        python:
            mconsolehistory.insert(830, text)
            if len(mconsolehistory) > 5:
                del mconsolehistory[5:]
            mconsolehistorydisplay = '\n'.join(map(str, mconsolehistory))
        show mconsole_history "[mconsolehistorydisplay]" as chistory zorder 100
    return

#This hides all of the parts of the console
label mhideconsole:
    hide mconsole_bg
    hide mconsole_caret
    #hide mccursor
    hide ctext
    hide chistory
