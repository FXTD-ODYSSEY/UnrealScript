import unreal
for actor in unreal.EditorLevelLibrary.get_selected_level_actors():
    if not isinstance(actor,unreal.StaticMeshActor):
        continue
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    mesh = unreal.EditableMeshFactory.make_editable_mesh(component,0)
    poly_count = mesh.get_polygon_count()
    print(poly_count)
    subd_count = mesh.get_subdivision_count()
    print(subd_count)

    mesh.set_subdivision_count()
    poly_count = mesh.get_polygon_count()
    print(poly_count)
    subd_count = mesh.get_subdivision_count()
    print(subd_count)
    preview = mesh.is_previewing_subdivisions()
    print(preview)
    # mesh.tessellate_polygons([unreal.PolygonID(i) for i in range(poly_count-10)],unreal.TriangleTessellationMode.FOUR_TRIANGLES)
    # mesh.tessellate_polygons([unreal.PolygonID(i) for i in range(8)],unreal.TriangleTessellationMode.FOUR_TRIANGLES)
    # print(poly_count)
