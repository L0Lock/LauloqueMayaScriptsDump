# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Maya Script Template
# 
# Description:  Script template for Maya.
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
print("########### Maya Script Template ###############")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=True, shapes=True) or []

    print(*selected, sep="\n")
    om.MGlobal.displayInfo("Success!")

if __name__ == "__main__":
    main()