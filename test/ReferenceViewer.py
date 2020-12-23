import unreal
asset_lib = unreal.EditorAssetLibrary()
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
options = unreal.AssetRegistryDependencyOptions(True,True,True,True,True)
# options.set_editor_property("include_hard_management_references",True)
# options.set_editor_property("include_hard_package_references",True)
# options.set_editor_property("include_searchable_names",True)
# options.set_editor_property("include_soft_management_references",True)
# options.set_editor_property("include_soft_package_references",True)
data = asset_lib.find_asset_data('/Game/ArtResources/Characters/A_Nami01/Materials/A_Nami01_L.A_Nami01_L')
print(data.package_name )
dependencies = asset_registry.get_dependencies(data.package_name,options)
referencers = asset_registry.get_referencers(data.package_name,options)

print(dependencies)

