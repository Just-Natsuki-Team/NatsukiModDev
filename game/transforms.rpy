#This is a copy of transforms.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for console.rpy
#This script defines the placements and animations used for putting images on
#screen. Useful for blocking with characters and other things

#########
####Transforms to place characters on the screen in proper positions based on whether there are 2, 3, or 4 characters in the scene.
transform categorized_menu_slide_in_right:
    xoffset 600
    easeout 0.4 xoffset 0
