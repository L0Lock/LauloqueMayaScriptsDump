# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Delete Empty Namespaces
# 
# Description:  Deletes all empty namespaces.
# 
# Author:       Loic Dautry Loic.Dautry@mikrosanimation.com
# 
# Version:      0.1

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("########## Delete Empty Namespaces #############")
print("################################################")

for nms in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True):
    try:
        cmds.namespace(removeNamespace=nms)
        print("# Deleted '{}'".format(nms))
    except:
        pass

om.MGlobal.displayInfo("Finished!")
