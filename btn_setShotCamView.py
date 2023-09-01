# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Set ShotCam View
# 
# Description:  Toggle the active viewport's camera between persp and shot cameras.
#               IMPORTANT: use the variable 'CAMERA_SEARCH' to set your shot camera
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.3

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import re

print("################################################")
print("############## Set ShotCam View ################")
print("################################################")


def main():
    CAMERA_SEARCH = "shot"

    cameraList = cmds.listCameras(p=True)
    print("Found the following perspective cameras in scene : \n    `{}`".format('\n    '.join(cameraList)))

    #### Camera Finder ####
    try:
        shotCam = [cam for cam in cameraList if re.search(CAMERA_SEARCH, cam)][0]
        print("Found shot camera :  `{}`".format(shotCam))
    except:
        shotCam = None
        print("Couldn't find shot camera")

    try:
        perspCam = [cam for cam in cameraList if re.search("persp", cam)][0]
        print("Found persp camera : `{}`".format(perspCam))
    except:
        print("Couldn't find persp camera")


    #### Set Viewport Camera ####
    try:
        currentCam = cmds.lookThru(q=True)
        print("Active viewport camera is '{}'".format(currentCam))
        if (currentCam == shotCam) or (shotCam == None):
            cmds.lookThru(perspCam)
            return "Switched active viewport to Persp Camera."

        else:
            cmds.lookThru(shotCam)
            return "Switched active viewport to Shot Camera."
    except:
        print("Couldn't find active viewport.")
        return "Couldn't switch active viewport camera."
        return False

if __name__ == "__main__":
    om.MGlobal.displayInfo(main())
