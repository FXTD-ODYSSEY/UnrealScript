import unreal

selected = unreal.EditorLevelLibrary.get_selected_level_actors()

for sel in selected:
    if type(sel) is unreal.StaticMeshActor:
        break

mesh = unreal.EditableMeshFactory.make_editable_mesh(sel,0)
print(mesh)

# NOTE 获取 StaticMeshComponent
component = sel.get_component_by_class(unreal.StaticMeshComponent)
material = component.get_materials()[0]
# material = material.get_base_material()
print material.get_editor_property("shading_model")

options = unreal.MaterialOptions()
options.set_editor_property()
merge_options = unreal.MaterialMergeOptions()

unreal.EditorTestsUtilityLibrary.bake_materials_for_component(component)



