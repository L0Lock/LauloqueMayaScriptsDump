# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Object Renamer
# 
# Description:  Pops up a popup to rename the selected object. Install as a custom script hotkey.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

import maya.mel as mel
import maya.cmds as cmds

def refreshName():
    selection = cmds.ls(sl=True)[0]
    cmds.refresh()
    return selection

def main():

    try:
        selection = cmds.ls(sl=True)[0]
    except:
        return


    popUp = cmds.promptDialog(
        title = "Rename Object",
        text = selection,
        button = ['Rename','Quit'],
        defaultButton = 'Rename',
        cancelButton = 'Quit',
        )

    if popUp == 'Rename':
        selection = cmds.ls(sl=True)[0]
        text = cmds.promptDialog(query=True, text=True)
        cmds.rename(selection, text)

if __name__ == "__main__":
    try:
        main()
        om.MGlobal.displayInfo("Renamed to '{}'".format(selection))
    except:
        om.MGlobal.displayInfo("Couldn't rename '{}'".format(selection))
        pass