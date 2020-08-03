import unreal

path = '/Game/sequence/RenderSequence(1).RenderSequence'
blueprint = unreal.load_asset(path)

# path = unreal.Paths.project_plugins_dir()
# print(path)

sub = unreal.EditorUtilitySubsystem()
widget,widget_id = sub.spawn_and_register_tab_and_get_id(blueprint)
print(widget)
print(widget_id)


# widget = sub.find_utility_widget_from_blueprint(blueprint)
# print (widget)