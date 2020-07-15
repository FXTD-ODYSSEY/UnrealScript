import unreal
cube_target = unreal.EditorAssetLibrary.load_asset('/Game/test/NewTextureRenderTargetCube.NewTextureRenderTargetCube')
cube_texture = unreal.RedArtToolkitBPLibrary.render_target_cube_create_static_texture_cube(cube_target,'/Game/test/test2')
print(cube_texture)
# print(dir(cube_target))
