# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Create Locators On Selected
# 
# Description:  Creates Locator objects on the selected objects with the same animation.
# 
# Author:       Loïc "Lauloque Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("######## Create Locators On Selected ###########")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=False, shapes=False) or []

    ## Locators Group Creation ##
    if not cmds.ls("_objectsLocators_"):
        trashLoc = cmds.spaceLocator(name="trashLocator")
        cmds.group(trashLoc, name="_objectsLocators_")
        cmds.delete("trashLocator")
        print("Created locators group '_objectsLocators_'")
    else:
        print("Locators group '_objectsLocators_' already exists.")
        pass

    ## Cycle through selected objects ##
    for obj in selected:
        print("Processing '{}'.".format(obj))
        slotsAttr = obj + ".numberParticles"
        ## Create Objects ##
        try:
            slots = str(cmds.getAttr(slotsAttr.format(obj)))
        except:
            slots = "0"
        if  slots != "0":
            locName = "Loc_{}_Slots{}_".format(str(obj),slots)
        else:
            locName = "Loc_" + str(obj)
        
        if cmds.ls(locName):
            cmds.delete(locName)
            print("    '{}' already exists, creating a new one.".format(locName))
        else:
            print("    Creating locator '{}'.".format(locName))
        newLoc = cmds.spaceLocator(name=locName)
        cmds.parent(newLoc, "_objectsLocators_")
        newConst = cmds.parentConstraint(obj, newLoc, mo = 0)
        cmds.delete(newConst)

        ## Copy Animation ##
        if cmds.copyKey(obj, animation="objects"):
            cmds.pasteKey(locName,animation="objects", option="replaceCompletely")
            print("    Copied animation from '{}' to '{}'".format(obj,locName))
        else:
            print("    '{}' has no animation to copy over '{}'".format(obj,locName))

if __name__ == "__main__":
    try:
        main()
        om.MGlobal.displayInfo("Success!")
    except Exception as e:
        ee = str(e).strip()
        print("Main function returned error :\n    {}".format(i,ee))
        om.MGlobal.displayError("Failure!")