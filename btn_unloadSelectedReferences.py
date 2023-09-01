# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Unload Selected References
# 
# Description:  Unloads the selected references.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.1

from __future__ import print_function
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

print("################################################")
print("######### Unload Selected References ###########")
print("################################################")


def unload_ref_within_selection():
    selected_nodes = cmds.ls(selection=True)
    if selected_nodes:
        cmds.select(hierarchy=True)
    nodes = get_reference_nodes_within_hierarchy()
    if not nodes:
        om.MGlobal.displayWarning("No reference nodes found in selection.")
        return
    for node in nodes:
        try:
            cmds.file(unloadReference=node)
            print("Unloaded reference: {}".format(node))
        except Exception as e:
            print("Error unloading reference: {}. {}".format(node, str(e)))
    om.MGlobal.displayInfo("Unloaded references from selection.")

def get_reference_nodes_within_hierarchy():
    selected_nodes = cmds.ls(selection=True)
    if not selected_nodes:
        return []
    reference_nodes = []
    for node in selected_nodes:
        try:
            reference_node = cmds.referenceQuery(node, referenceNode=True)
            if reference_node and reference_node not in reference_nodes:
                reference_nodes.append(reference_node)
        except:
            pass
    return reference_nodes

if __name__ == "__main__":
    try:
        unload_ref_within_selection()
    except:
        om.MGlobal.displayWarning("No references removed from selection")