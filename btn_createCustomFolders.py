# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Create Custom Folders
# 
# Description:  Creates my custom folders in the scene folder.
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
import os

print("################################################")
print("############ Create Custom Folders #############")
print("################################################")

def pathGen(newPath, rawPath):
    if not (os.path.exists(newPath)):
        os.makedirs(newPath)
        print ("# Created:           '{}'".format(newPath.replace(rawPath, ".")))
    else:
        print ("# Already exists:    '{}'".format(newPath.replace(rawPath, ".")))

def main():

    ### BASE PATH
    filePath = cmds.file(q=True, sn=True)
    fileName = os.path.basename(filePath)
    rawName, extension = os.path.splitext(fileName)
    rawPath = os.path.dirname(os.path.abspath(filePath))

    print("# file path      :  '{}'".format(filePath))
    print("# file name      :  '{}'".format(fileName))
    print("# raw name       :  '{}'".format(rawName))
    print("# extension      :  '{}'".format(extension))
    print("# raw path       :  '{}'".format(rawPath))

    ### CUSTOM PATH
    pathGen("{}\\alembicCaches".format(rawPath), rawPath)
    pathGen("{}\\animationRefferences".format(rawPath), rawPath)
    pathGen("{}\\playblasts".format(rawPath), rawPath)

    om.MGlobal.displayInfo("Created Custom Folders!")

if __name__ == "__main__":
    main()
    