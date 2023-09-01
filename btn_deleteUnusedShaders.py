# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         deleteUnusedShaders
# 
# Description:  Deletes unused shaders
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
import sys, re
from os.path import expanduser

print("################################################")
print("############ deleteUnusedShaders ###############")
print("################################################")

def main():
    cnt = 0
    oldLines = []
    home = expanduser("~")
    filePath = cmds.file(q=True, sn=True)
    rawPath = os.path.dirname(os.path.abspath(filePath))
    outputPath = "{}/output.txt".format(home)
    file = open(outputPath, 'a')

    cmds.scriptEditorInfo(historyFilename=outputPath, writeHistory=True, clearHistoryFile=True)
    pm.mel.MLdeleteUnused()
    try:
        pm.mel.MLdeleteUnused()
    except Exception as e:
        ee = str(e).strip()
        print("# try/except returned error :\n#    {}".format(i,ee))

    
    with open(outputPath, 'r') as lines:
        for line in lines:
            if line not in oldLines:
                if re.match(r'^delete', line):
                    cnt += 1
                    print("+1")
                if 'Non-deletable node' in line:
                    cnt -=1
                    print("-1")
                oldLines.append(line)

    file.close()
    os.remove(file.name)
    om.MGlobal.displayInfo("Deleted {} shader nodes.".format(cnt))

if __name__ == "__main__":
    main()