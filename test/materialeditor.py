import json
import unreal
py_lib = unreal.PyToolkitBPLibrary()


objects = py_lib.get_all_objects()

res_list = []
for obj in objects:
    try:
        res_list.append(obj.get_path_name())
    except:
        print("error -> %s" % obj)

path = r"F:\MayaTecent\UnrealScript\test\object_list.json"
with open(path,'w') as f:
    json.dump(res_list,f,indent=4)


# UMaterialInstanceConstant *URedArtToolkitBPLibrary::GetMaterialEditorSourceInstance(UMaterialEditorInstanceConstant *Editor)
# {
#     return Editor->SourceInstance;
# }

red_lib = unreal.RedArtToolkitBPLibrary()
def list_material_editor(num=1000):
    material_editor = {}
    for i in range(num):
        editor = unreal.load_object(None,"/Engine/Transient.MaterialEditorInstanceConstant_%s" % i)
        if editor:
            material = red_lib.get_material_editor_source_instance(editor)
            if material:
                material_editor[material] = editor
    return material_editor

edit_asset = red_lib.get_focused_edit_asset()
material_editor = list_material_editor()
editor = material_editor.get(edit_asset)
if editor:
    pass

menu = unreal.load_object(None,"/Engine/Transient.ToolMenus_0:ToolMenu_61")
print(menu.menu_name)

section = unreal.load_object(None,"/Engine/Transient.Selection_3")
print(section)

material = unreal.load_object(None,'/Game/ArtResource/Assets/Weapon/Sniper/M82/M82_D1/Default/Material/MI_Wp_Snp_M82_D1_TPS.MI_Wp_Snp_M82_D1_TPS')
obj = material.get_base_material()
print(material)
editor = unreal.MaterialEditorInstanceConstant.cast(material)


assets = red_lib.get_assets_opened_in_editor()
print(assets)

for asset in assets:
    editor = red_lib.get_focus_material_editor_instance(asset)
    print(editor)
    # instance = unreal.MaterialInstance.cast(asset)
    print(asset.parent())
    print(instance)


['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_post_init', '_wrapper_meta_data', 'call_method', 'cast', 'font_parameter_values', 'get_base_material', 'get_class', 'get_default_object', 'get_editor_property', 'get_fname', 'get_full_name', 'get_name', 'get_outer', 'get_outermost', 'get_parameter_info', 'get_path_name', 'get_physical_material', 'get_physical_material_from_map', 'get_physical_material_mask', 'get_scalar_parameter_value', 'get_texture_parameter_value', 'get_typed_outer', 'get_vector_parameter_value', 'get_world', 'modify', 'override_subsurface_profile', 'parent', 'phys_material', 'rename', 'runtime_virtual_texture_parameter_values', 'scalar_parameter_values', 'set_editor_properties', 'set_editor_property', 'set_force_mip_levels_to_be_resident', 'static_class', 'subsurface_profile', 'texture_parameter_values', 'vector_parameter_values']

# section = unreal.load_class(None,"/Game/RedApp/Base/Effects/BP_RedEffectView.BP_RedEffectView_C")
# print(section)

# Blueprint'/Game/RedApp/Base/Effects/BP_RedEffectView.BP_RedEffectView'
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_post_init', '_wrapper_meta_data', 'call_method', 'cast', 'get_class', 'get_default_object', 'get_editor_property', 'get_fname', 'get_full_name', 'get_name', 'get_outer', 'get_outermost', 'get_path_name', 'get_typed_outer', 'get_world', 'modify', 'rename', 'set_editor_properties', 'set_editor_property', 'static_class']


