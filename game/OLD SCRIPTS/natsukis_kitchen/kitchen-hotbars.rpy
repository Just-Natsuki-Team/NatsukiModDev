


init python:


    def KITHideButtons():
        
        
        
        config.overlay_screens.remove("kit_overlay")
        renpy.hide_screen("kit_overlay")


    def KITShowButtons():
        
        
        
        config.overlay_screens.append("kit_overlay")

init -1 python in kit_button:



    enabled = True




screen kit_overlay:

    zorder 50

    style_prefix "hkb"

    vbox:
        xalign 0.05
        yalign 0.95


        if allow_dialogue:
            textbutton _("Talk") action Jump("kitchentalkmenu")
        else:
            textbutton _("Talk"):
                action NullAction()
                style "hkbd_button"
        if allow_dialogue:
            textbutton _("Bake") action Jump("bake")
        else:
            textbutton _("Bake"):
                action NullAction()
                style "hkbd_button"

    text "v[config.version]":
                xalign 1.0 yalign 1.0
                xoffset -10 yoffset -10
                style "main_menu_version"

    vbox:
        imagebutton:
            xpos 546 ypos 273
            idle "mod_assets/boopindicator.png"
            hover "mod_assets/boopindicator.png"
            action [If(allow_dialogue, true=Jump("ch30_boop"))]

screen fight:

    zorder 50

    style_prefix "hkb"


    vbox:
        xalign 0.05
        yalign 0.95


        textbutton _("Fight") action Jump("fight")
            
        textbutton _("Act") action Jump("act")

        textbutton _("Codes") action Jump("codes")

        textbutton _("Mercy") action Jump("mercy")

    xpos 424 ypos 814
    label _("HP: [hp]")

screen talking:

    zorder 50

    style_prefix "talk"


    vbox:
        xalign 500
        yalign 100

        vbox:
            textbutton _("1") action Jump("normaltalkmenu")
            xpos 867 ypos 137
            
            textbutton _("2") action Jump("normaltalkmenu2")

            textbutton _("3") action Jump("normaltalkmenu3")

            textbutton _("4") action Jump("normaltalkmenu4")

            textbutton _("5") action Jump("normaltalkmenu5")

            textbutton _("6") action Jump("normaltalkmenu6")

            textbutton _("7") action Jump("normaltalkmenu7")

            textbutton _("X") action Hide("talking"), Show("talking2")

screen talking2:

    zorder 50

    style_prefix "talk"


    vbox:
        xalign 500
        yalign 100

        vbox:
            textbutton _("X") action Hide("talking2"), Show("talking")
            xpos 867 ypos 137

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
