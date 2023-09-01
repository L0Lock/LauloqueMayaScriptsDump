# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         legPrintsEnable
# 
# Description:  In Golaem, set the characterMaker's legPrint to 1 for the whole loaded motion.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.2

import pymel.core as pm
import maya.api.OpenMaya as om

def main():

    try:
        pm.select("characterMakerLocator1", r=True)
        
    except:
        return om.MGlobal.displayWarning("Couldn't find 'characterMakerLocator1'")
    
    pm.selectKey("characterMakerLocatorShape1_cf1", add=True,k=True)
    pm.selectKey("characterMakerLocatorShape1_cf3", add=True,k=True)
    pm.keyframe(animation="keys", absolute=True, valueChange=1)
    om.MGlobal.displayInfo("Set 'characterMakerLocator1' leg footprints to 1")
        
if __name__ == '__main__':
    main()