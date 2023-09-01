# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Create Display Layers
# 
# Description:  Creates common useful display layers for animation.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import maya.api.OpenMaya as om

print("################################################")
print("########### Create Display Layers ##############")
print("################################################")

def main():
    pm.createDisplayLayer(empty=False, name="lyr_alwaysHide", noRecurse=True)
    lyr_alwaysHide.displayType.set(2)
    lyr_alwaysHide.color.set(4)
    lyr_alwaysHide.overrideColorRGB.set(0 0 0)
    lyr_alwaysHide.overrideRGBColors.set(0)
    lyr_alwaysHide.visibility.set(0)

    try:
        pm.select(["__CAMS__"], replace=True):
    except:
        print("Couldn't find Camera group.")
    pm.createDisplayLayer(empty=False, name="lyr_camera", noRecurse=True)
    lyr_alwaysHide.displayType.set(2)
    lyr_alwaysHide.color.set(1)
    lyr_alwaysHide.overrideColorRGB.set(0 0 0)
    lyr_alwaysHide.overrideRGBColors.set(0)
    lyr_alwaysHide.visibility.set(1)

    try:
        pm.select(["__PROPS__", "__LOCATIONS__"], replace=True):
    except:
        print("Couldn't find daily geo groups.")
    pm.createDisplayLayer(empty=False, name="lyr_dailyGeo", noRecurse=True)
    lyr_dailyGeo.displayType.set(2)
    lyr_dailyGeo.color.set(19)
    lyr_dailyGeo.overrideColorRGB.set(0 0 0)
    lyr_dailyGeo.overrideRGBColors.set(0)
    lyr_alwaysHide.visibility.set(1)

if __name__ == "__main__":
    main()