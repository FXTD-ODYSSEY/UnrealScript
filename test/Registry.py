import unreal
reg_helper = unreal.AssetRegistryHelpers()
asset_reg = reg_helper.get_asset_registry()
asset_tool = unreal.AssetToolsHelpers.get_asset_tools()


packages_to_check = unreal.load_package('/Game/RedApp/Content/ArtResources/PendingModels/A_Arlong01/L/Skel_Mesh/Skel_Arlong01_L_rig.Skel_Arlong01_L_rig')

origin = unreal.SoftObjectPath('/Game/ArtResources/Characters/A_Arlong01/L/Skel_Mesh/Skel_Arlong01_L_rig_Skeleton.Skel_Arlong01_L_rig_Skeleton')
target = unreal.SoftObjectPath('/Game/RedApp/Content/ArtResources/PendingModels/A_Arlong01/L/Skel_Mesh/Skel_Arlong01_L_rig_Skeleton.Skel_Arlong01_L_rig_Skeleton')

asset_tool.rename_referencing_soft_object_paths([packages_to_check],{
    origin:target
})

path = "/Game/ArtResources/MaterialLibrary"
assets = asset_reg.get_assets_by_path(path,True)

ar_filter = unreal.ARFilter(package_paths=["/Game/ArtResources/MaterialLibrary/MaterialFunction"])
assets = asset_reg.use_filter_to_exclude_assets(assets,ar_filter)
print(assets)

asset = unreal.load_asset('/Game/ArtResources/Characters/A_Boodle01/Materials/Boodle01.Boodle01')
data = reg_helper.create_asset_data(asset)
assets = asset_reg.get_assets_by_package_name(data.package_name,True)
assets = asset_reg.get_assets_by_package_name('/Game/ArtResources/Characters/A_Boodle01/Materials')
print(assets)

ar_filter = unreal.ARFilter(package_paths=['/Game/ArtResources/Characters/A_Boodle01/Materials'])
assets = asset_reg.get_assets(ar_filter)
print(assets)


