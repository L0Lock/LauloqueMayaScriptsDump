# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         glm Locator Display Setup
# 
# Description:  Sets golaem locators display settings as I like: 10% opacity, no fake height and 10% size.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.2

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("######### glm Locator Display Setup ############")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=False, shapes=False) or []

    for obj in selected:
        shapes = cmds.listRelatives(obj, shapes=True)
        if shapes:
            shape = shapes[0]
            print("Working on '{}'".format(shape))

            # Transparency
            if "popTool" in shape:
                try:
                    cmds.setAttr("{}.displayTransparency".format(shape), 0.9)
                    print("    | '{}.displayTransparency' => 0.9".format(shape))
                except:
                    print("    | '{}.displayTransparency' doesn't exists".format(shape))
                    pass
            else:
                try:
                    cmds.setAttr("{}.displayTransparency".format(shape), 0.1)
                    print("    | '{}.displayTransparency' => 0.1".format(shape))
                except:
                    print("    | '{}.displayTransparency' doesn't exists".format(shape))
                    pass

            # Locator Height
            try:
                cmds.setAttr("{}.locatorHeight".format(shape), 0)
                print("    | '{}.locatorHeight' => 0".format(shape))
            except:
                print("    | '{}.locatorHeight' doesn't exists".format(shape))
                pass

            # Scale
            try:
                cmds.setAttr("{}.locatorScaleFactor".format(shape), 0.04)
                print("    | '{}.locatorScaleFactor' => 0.04".format(shape))
            except:
                print("    | '{}.locatorHeight' doesn't exists".format(shape))
                pass

        # Manip Scale
        if "popTool" in obj:
            children = cmds.listRelatives(obj, children=True) or []
            print("    | '{} have the following children: \n        {}".format(obj,children))
            for child in children:
                if "Manip" in child:
                    cmds.setAttr("{}.visibility".format(child), 0)
                    print("    | '{}.visibility' => 0".format(child))

    om.MGlobal.displayInfo("Success!")

if __name__ == "__main__":
    main()