# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         create frameRangeGroup
# 
# Description:  Creates an empty group with the current time slider's frame range
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.3

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
from os.path import basename

def create_group(name):
    cmds.group(empty=True, name=name)

def main():
    try:
        cmds.delete("*FRAME_RANGE__*")
    except:
        pass

    startTime = str(int(cmds.playbackOptions(minTime=True, q=True))).zfill(3)
    endTime = str(int(cmds.playbackOptions(maxTime=True, q=True))).zfill(3)

    frame_group_name = "__FRAME_RANGE__" + startTime + "_" + endTime + "__"
    create_group(frame_group_name)
    print("Success: Created group '{}'".format(frame_group_name))

    om.MGlobal.displayInfo("Created anim conversion info groups.")

if __name__ == "__main__":
    main()