# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         TEMPLATE button label toggle
# 
# Description:  toggles the button label of a button named "TEST BUTTON". 
#               IMPORTANT: Set the same name of the desired button in the variable 'targetButton' and in Maya!
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
    gShelfTopLevel = mel.eval("global string $gShelfTopLevel; $temp = $gShelfTopLevel;")
    currentShelf = cmds.tabLayout(gShelfTopLevel, q=True, st=True)
    buttons = cmds.shelfLayout(currentShelf, q=True, ca=True)
    targetButton = 'TEST BUTTON' # Button 'name' not 'icon label'
    # toggleIcons = ['showManip.png', 'globalManip.png']  # could be used to change icons as well?

    for b in buttons:
        if "separator" not in b:
            label = cmds.shelfButton(b, q=True, l=True)

            if label == targetButton:
                print('Found target button: `{}` -> {}'.format(targetButton, b))
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

    om.MGlobal.displayWarning("Couldn't find `{}` in current shelf! See console for more details.".format(targetButton))
    print('# Make sure to rename your button to `{}`'.format(targetButton))

if __name__ == "__main__":
    main()