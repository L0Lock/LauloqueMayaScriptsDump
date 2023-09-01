# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Copy Animation To Selected
# 
# Description:  Copies the animation from the first selected object to the second selected object.
# 
# Author:       Loïc "Lauloque Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.2

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("######## Copy Animation To Selected ############")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=False, shapes=False) or []
    if len(selected) == 2:
        ## Snap objects ##
        newConst = cmds.parentConstraint(selected[0], selected[1], mo = 0)
        cmds.delete(newConst)


        ## Copy Animation ##
        if cmds.copyKey(selected[0], animation="objects"):
            cmds.pasteKey(selected[1],animation="objects", option="replaceCompletely")
            om.MGlobal.displayInfo("Copied animation from '{}' to '{}'".format(selected[0],selected[1]))
        else:
            om.MGlobal.displayWarning("'{}' has no animation to copy over '{}'".format(selected[0],selected[1]))
    else:
        om.MGlobal.displayWarning("Please select two objects to copy animation from and to.")

if __name__ == "__main__":
    main()