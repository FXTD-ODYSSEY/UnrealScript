import unreal

path = '/Game/test/sequencer_test/RenderSequence.RenderSequence'
blueprint = unreal.load_asset(path)
# print(blueprint)

# blueprint = unreal.EditorUtilityWidgetBlueprint()

sub = unreal.EditorUtilitySubsystem()
widget = sub.spawn_and_register_tab_and_get_id(blueprint)
print(widget)
# widget = sub.find_utility_widget_from_blueprint(blueprint)
# print (widget)