import unreal
widget_lib = unreal.WidgetLibrary()
level_lib = unreal.EditorLevelLibrary
# path = '/Game/sequence/RenderSequence(1).RenderSequence'
path = '/Game/test/widgetTest/TestButtonWidget.TestButtonWidget'
widget_BP = unreal.load_asset(path)

sub = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
widget = sub.spawn_and_register_tab(widget_BP)
# print(widget)
# print(widget.get_parent())

world = level_lib.get_editor_world()
print (widget_lib.get_all_widgets_of_class(world,widget.get_class(),False))
print (widget_lib.get_all_widgets_of_class(world,unreal.UserWidget,False))

widget = sub.find_utility_widget_from_blueprint(widget_BP)

tree = unreal.find_object(None,'%s.WidgetTree_0' % widget.get_path_name())
print(tree.get_editor_property("RootWidget"))

panel = unreal.find_object(None,'%s.WidgetTree_0.VerticalBox_0' % widget.get_path_name())
layout  = unreal.HorizontalBox()
button = unreal.Button()
layout.add_child_to_horizontal_box(button)
button = unreal.Button()
layout.add_child_to_horizontal_box(button)
panel.add_child_to_vertical_box(layout)


slot = unreal.find_object(None,'/Game/RedApp/Base/Maps/LoginMain.LoginMain:TestButtonWidget_C_5.WidgetTree_0.VerticalBox_0.VerticalBoxSlot_1')
print(slot)

panel = unreal.find_object(None,'%s:WidgetTree_0.VerticalBox_0' % widget.get_path_name())
layout_lib = unreal.WidgetLayoutLibrary
slot = layout_lib.slot_as_vertical_box_slot(panel)
print(slot)


