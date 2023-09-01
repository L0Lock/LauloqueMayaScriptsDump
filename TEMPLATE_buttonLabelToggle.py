# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         TEMPLATE button label toggle
# 
# Description:  toggles the button label of a button named "TEST BUTTON". 
#               IMPORTANT: Set the same name of the desired button in the variable 'TARGET_BUTTON' and in Maya!
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      1.0

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

def main():
    TARGET_BUTTON = 'TEST BUTTON' # Button 'name' not 'icon label'
    
    gShelfTopLevel = mel.eval("global string $gShelfTopLevel; $temp = $gShelfTopLevel;")
    currentShelf = cmds.tabLayout(gShelfTopLevel, q=True, st=True)
    buttons = cmds.shelfLayout(currentShelf, q=True, ca=True)
    # toggleIcons = ['showManip.png', 'globalManip.png']  # could be used to change icons as well?

    for b in buttons:
        if "separator" not in b:
            label = cmds.shelfButton(b, q=True, l=True)

            if label == TARGET_BUTTON:
                print('Found target button: `{}` -> {}'.format(TARGET_BUTTON, b))
                currentLabel = cmds.shelfButton(b, q=True, imageOverlayLabel=True)
                if currentLabel == "A":
                    newLabel = "B"
                elif currentLabel == "B":
                    newLabel = "C"
                elif currentLabel == "C":
                    newLabel = "A"
                else: ### This one is in case the button didn't had the correct name to begin with
                    newLabel = "A"

                om.MGlobal.displayInfo('Icon label: `{}` -> `{}`'.format(currentLabel, newLabel))
                cmds.shelfButton(b, e=True, imageOverlayLabel=newLabel)
                return
            else:
                print('Passed `{}`'.format(label))

    om.MGlobal.displayWarning("Couldn't find `{}` in current shelf! See console for more details.".format(TARGET_BUTTON))
    print('# Make sure to rename your button to `{}`'.format(TARGET_BUTTON))

if __name__ == "__main__":
    main()