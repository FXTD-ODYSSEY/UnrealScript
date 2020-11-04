import unreal
widget_lib = unreal.WidgetLibrary()
# path = '/Game/sequence/RenderSequence(1).RenderSequence'
path = '/Game/test/Widget.Widget'
widget_BP = unreal.load_asset(path)

# widget = unreal.get_default_object(blueprint.get_class())
# print(widget)

# path = unreal.Paths.project_plugins_dir()
# print(path)

sub = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
widget = sub.spawn_and_register_tab(widget_BP)
print(widget)
print(widget.get_parent())

print (widget_lib.get_all_widgets_of_class(None,widget.get_class(),False))

# widget = sub.find_utility_widget_from_blueprint(blueprint)
# print (widget)