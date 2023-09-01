# Name:         Open maya scene folder
# Description:  Opens the current scene's folder (needs to be a saved file).
# 
# Author:       Loïc "Lauloque Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

import maya.cmds as cmds
import os
import maya.api.OpenMaya as om

def main():
    scenePath = os.path.dirname(os.path.abspath(cmds.file(q=True,sn=True,shn=False)))
    print(scenePath)
    os.system('xdg-open "%s"' % scenePath)

if __name__ == '__main__':
    try:
        main()
        om.MGlobal.displayInfo("Scene folder open.")
    except:
        om.MGlobal.displayWarning("Couldn't find scene folder. Make sure you have a scene open!")
