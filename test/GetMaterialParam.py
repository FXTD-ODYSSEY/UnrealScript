# -*- coding: utf-8 -*-
"""
https://forums.unrealengine.com/development-discussion/python-scripting/1587906-is-it-possible-to-use-python-for-editing-material-graphs
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = 'timmyliang'
__email__ = '820472580@qq.com'
__date__ = '2020-07-06 10:45:39'


import unreal

def print_static_switch_params(asset_path):
    # asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    # all_assets = asset_registry.get_assets_by_path(asset_path, recursive=True)
    material = unreal.EditorAssetLibrary.load_asset(asset_path)
    color = unreal.LinearColor(r=0.0, g=0.0, b=0.0, a=0.0)
    unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(material,"BoxMax",color)
    # print (u"%s" % parameters)

    # for p in parameters:
    #     print (u"%s" % parameters)
        # static_switch_params = unreal.MaterialEditingLibrary.get_material_default_static_switch_parameter_value(material, p)
    # print(static_switch_params)

print_static_switch_params("/Game/RedApp/Base/Maps/Temp/BoxCube_Test/Floor.Floor")