# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Switch Playback Speed
# 
# Description:  Togles the playback speed between 24fps constant to playing every frame maxed at 24. In golaem, use the first then in cache replay, and the later when simulating.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

import pymel.core as pm
import maya.cmds as cmds
import os, subprocess
import maya.api.OpenMaya as om

def main():
    
    if pm.playbackOptions(q=True, playbackSpeed=True) == 1.0:
        pm.playbackOptions(e=True, playbackSpeed=0.0)
        pm.playbackOptions(e=True, maxPlaybackSpeed=1.0)
        return "Set Playback Speed to 'play every frame' maxed at '24 fps x 1'."
    else:
        pm.playbackOptions(e=True, playbackSpeed=1.0)
        return "Set Playback Speed to '24 fps x 1'."
    
    pm.savePrefs()
    
    if pm.window('PreferencesWindow', exists=True):
        pm.window.deleteUI('PreferencesWindow', window=True)
        pm.preferencesWnd("timeslider")

if __name__ == '__main__':
    om.MGlobal.displayInfo(main())