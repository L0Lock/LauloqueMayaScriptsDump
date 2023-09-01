# SPDX-License-Identifier: GPL-3.0-or-later
# Name:         Toggle Selection Masks
# 
# Description:  Togles the selection masks between 'curves only' and 'all' types.
# 
# Author:       Loïc "Lauloque" Dautry
#
# Source:       https://github.com/L0Lock/LauloqueMayaScriptsDump
# 
# Version:      0.2

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

if 'LD_selectionState' not in globals():
    LD_selectionState = False

def main():
    global LD_selectionState

    if LD_selectionState == True: # if masked to curve > enable all objects
        pm.selectMode(object=True)
        pm.selectType(handle=1, ikHandle=1, joint=1, nurbsCurve=1, cos=1, stroke=1, nurbsSurface=1, polymesh=1, subdiv=1, plane=1, lattice=1, cluster=1, sculpt=1, nonlinear=1, particleShape=1, emitter=1, field=1, spring=1, rigidBody=1, fluid=1, hairSystem=1, follicle=1, nCloth=1, nRigid=1, dynamicConstraint=1, rigidConstraint=1, collisionModel=1, light=1, camera=1, texture=1, ikEndEffector=1, locator=1, dimension=1)
        mel.eval('selectType -byName gpuCache true')

        LD_selectionState = False
        return "Set selection mask to All objects types"


    else: # else mask to curves
        pm.selectMode(object=True)
        pm.selectType(handle=0, ikHandle=0, joint=0, nurbsCurve=1, cos=1, stroke=1, nurbsSurface=0, polymesh=0, subdiv=0, plane=0, lattice=0, cluster=0, sculpt=0, nonlinear=0, particleShape=0, emitter=0, field=0, spring=0, rigidBody=0, fluid=0, hairSystem=0, follicle=0, nCloth=0, nRigid=0, dynamicConstraint=0, rigidConstraint=0, collisionModel=0, light=0, camera=0, texture=0, ikEndEffector=0, locator=0, dimension=0)
        mel.eval('selectType -byName gpuCache true')

        LD_selectionState = True
        return "Set selection mask to Curves only"

if __name__ == '__main__':
    om.MGlobal.displayInfo(main())