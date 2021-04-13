# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = 'timmyliang'
__email__ = '820472580@qq.com'
__date__ = '2021-04-11 19:51:16'


import os
import re
import time
import string
import posixpath
from functools import partial
import unreal

from Qt import QtWidgets,QtCore

widget_lib = unreal.WidgetLibrary
level_lib = unreal.EditorLevelLibrary
asset_lib = unreal.EditorAssetLibrary
util_lib = unreal.EditorUtilityLibrary
asset_tool = unreal.AssetToolsHelpers.get_asset_tools()

def create_asset(asset_path="", unique_name=True, asset_class=None, asset_factory=None):
    
    if unique_name:
        asset_path, _ = asset_tool.create_unique_asset_name(asset_path,'')
    if not asset_lib.does_asset_exist(asset_path=asset_path):
        path, name = posixpath.split(asset_path)
        return asset_tool.create_asset(
            asset_name=name,
            package_path=path,
            asset_class=asset_class,
            factory=asset_factory,
        )
    return unreal.load_asset(asset_path)

material = unreal.load_asset('/Game/test/CubeTest.CubeTest')



directory = "/Game/test/widgetTest"
name = "TestWidget3"
path = posixpath.join(directory,name)
factory = unreal.EditorUtilityWidgetBlueprintFactory()
widget_BP = create_asset(path,True,unreal.EditorUtilityWidgetBlueprint,factory)
# NOTE rename force compile
widget_BP.rename("%s_" % name)

panel = unreal.find_object(None,'%s_C:WidgetTree.CanvasPanel_0' % widget_BP.get_path_name())
layout  = unreal.VerticalBox()
button = unreal.Button()
delegate = button.on_clicked
block = unreal.TextBlock()
block.set_text("test")
button.add_child(block)
layout.add_child(button)
button = unreal.Button()
layout.add_child(button)
# details = unreal.DetailsView()
# details.set_object(widget_BP)
# layout.add_child(details)

property_view = unreal.SinglePropertyView()
@unreal.uclass()
class PropertyObject(unreal.Object):
    mesh = unreal.uproperty(unreal.MaterialInstanceConstant)
obj = PropertyObject()
property_view.set_object(obj)
property_view.set_property_name("mesh")
layout.add_child(property_view)


slot = panel.add_child_to_canvas(layout)

slot.set_anchors(unreal.Anchors(maximum=[1,1]))
slot.set_offsets(unreal.Margin())


editor_sub = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
widget,id = editor_sub.spawn_and_register_tab_and_get_id(widget_BP)

delegate.add_callable(lambda:print("is_hovered %s" % widget.is_hovered()))
delegate.add_callable(lambda:print("has_keyboard_focus %s" % widget.has_keyboard_focus()))
delegate.add_callable(lambda:print("has_focused_descendants %s" % widget.has_focused_descendants()))

global __dialog_dict__
__dialog_dict__ = {
    id:{
        "widget":widget,
        "widget_BP":widget_BP,
    }
}

global __tick_delta__
__tick_delta__ = 0
def __slate_handler__(delta):
    global __tick_delta__
    if __tick_delta__ < 1:
        __tick_delta__ += delta
        return
    else:
        __tick_delta__ = 0

    editor_sub = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
    global __dialog_dict__
    remove_list = []
    
    for id,info in __dialog_dict__.items():
        widget = info.get("widget")
        widget_BP = info.get("widget_BP")
        if not editor_sub.does_tab_exist(id):
            remove_list.append(id)
            continue
        
        # Block
        print("is_hovered",widget.is_hovered())
        print("is_visible",widget.is_visible())
        print("is_interactable",widget.is_interactable())
        # print("is_focusable",widget.is_focusable())
        print("has_mouse_capture",widget.has_mouse_capture())
        print("is_in_viewport",widget.is_in_viewport())
        # if not widget.is_hovered():
        #     editor_sub.spawn_and_register_tab_and_get_id(widget_BP)
        #     time.sleep(0.2)
        
    # NOTE 自动清理本地资产
    for id in remove_list:
        info = __dialog_dict__[id]
        widget_BP = info.get("widget_BP")
        # NOTE rename force compile
        widget_BP.rename("%s__delete__" % widget_BP.get_name())
        QtCore.QTimer.singleShot(0,partial(asset_lib.delete_asset,widget_BP.get_path_name()))
        del __dialog_dict__[id]

tick_handle = unreal.register_slate_pre_tick_callback(partial(__slate_handler__))

unreal_app = QtWidgets.QApplication.instance()
__QtAppQuit__ = partial(unreal.unregister_slate_pre_tick_callback,tick_handle)
unreal_app.aboutToQuit.connect(__QtAppQuit__)



# print("is_hovered %s" % widget.is_hovered())
# print("has_keyboard_focus %s" % widget.has_keyboard_focus())
# print("has_focused_descendants %s" % widget.has_focused_descendants())


