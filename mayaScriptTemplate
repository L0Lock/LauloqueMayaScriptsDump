# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Maya Script Template
# 
# Description:  Script template for Maya.
# 
# Author:       Loic Dautry Loic.Dautry@mikrosanimation.com
# 
# Version:      0.1

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("########### Maya Script Template ###############")
print("################################################")

def main():
    selected = cmds.ls(selection=True,long=True, shapes=True) or []

    print(*selected, sep="\n")
    om.MGlobal.displayInfo("Success!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        ee = str(e).strip()
        print("Main function returned error :\n    {}".format(i,ee))
        om.MGlobal.displayError("Failure!")
