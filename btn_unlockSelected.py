# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Unlock Selected
# 
# Description:  Unlocks the selected nodes.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("############### Unlock Selected ################")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=True, shapes=True) or []

    for obj in selected:
    	try:
        	cmds.lockNode(obj, lock=False)
        	print("Unlocked '{}'".format(obj))

    	except Exception as e:
            ee = str(e).strip()
            print("Object '{}' returned error :\n    {}".format(i,ee))

if __name__ == "__main__":
    try:
        main()
        om.MGlobal.displayInfo("Unlocked selection!")
    except:
        om.MGlobal.displayError("Couldn't unlock selection! See console for more info.")