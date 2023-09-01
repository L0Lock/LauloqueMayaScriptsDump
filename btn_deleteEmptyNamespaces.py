# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Delete Empty Namespaces
# 
# Description:  Deletes all empty namespaces recursively.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.4

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om


print("################################################")
print("########## Delete Empty Namespaces #############")
print("################################################")

def delete_empty_namespace():
    total_count = 0

    while True:
        count = 0

        for nms in cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True):
            try:
                cmds.namespace(removeNamespace=nms)
                print("# Deleted '{}'".format(nms))
                count +=1
            except:
                pass

        total_count += count
        print("count: {}".format(count))
        print("total count: {}".format(total_count))

        if count == 0: break


    if cmds.window('namespaceEditor', exists=True):
        mel.eval("updateNamespaceEditor")
        print("Namespace editor refreshed.") 
    else:
        print("No Namespace editor to refresh.")
        
    return total_count

if __name__ == '__main__':
    om.MGlobal.displayInfo("Finished! Empty namespaces removed: {}".format(delete_empty_namespace()))