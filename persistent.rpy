#This is for anything that must happen CONSTANTLY in game.

init python:
    import subprocess
    import os
    import datetime
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass


    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if persistent.monika_persistent:
            if not os.path.isfile(basedir + "/characters/monika.chr"):
                renpy.call("monikareturn")


label monikareturn:
    python:
        try: renpy.file(config.basedir + "../(monika).chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    return