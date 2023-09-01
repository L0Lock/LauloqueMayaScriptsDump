# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Clear Drawing Overrides
# 
# Description:  Recursively removes Drawing Overrides on the selection and its children.
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
print("########## Clear Drawing Overrides #############")
print("################################################")

def get_selected_nodes():
    selected_nodes = pm.ls(selection=True)
    return selected_nodes

def get_child_nodes(parent_object):
    child_nodes = parent_object.getChildren(ad=True) or []
    return child_nodes

def create_nodes_list():
    selected_nodes = get_selected_nodes()
    nodes_list = []

    for obj in selected_nodes:
        nodes_list.append(obj)
        child_nodes = get_child_nodes(obj)

        for child_obj in child_nodes:
            nodes_list.append(child_obj)

    return nodes_list

def main():
    count = 0
    nodes_list = create_nodes_list()
    original_nodes_list = get_selected_nodes()

    # Disable Drawing override options
    if not nodes_list:
        om.MGlobal.DrawingWarning("Selection is empty.")
        return

    print("  |  Disabling Drawing Override:")
    for obj in nodes_list:
        try:
            obj.overrideEnabled.set(0)
            print("  |  -- SUCCESS -- '{}'".format(obj))
            count += 1
        except:
            print("  |  -- FAILED  -- '{}'".format(obj))

    pm.select(original_nodes_list)
    om.MGlobal.displayInfo("Successfully disabled {} Drawing overries.".format(count))

if __name__ == "__main__":
    main()