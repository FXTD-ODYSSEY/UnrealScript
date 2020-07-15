import unreal

selected_list = unreal.EditorLevelLibrary.get_selected_level_actors()

for actor in selected_list:
    if not isinstance(actor,unreal.StaticMeshActor):
        continue
    component = actor.get_component_by_class(unreal.StaticMeshComponent)
    # TODO 复制一个 static_mesh 进行高模编辑
    static_mesh = component.get_editor_property("static_mesh")
    
    # desc = static_mesh.create_static_mesh_description()

    mesh = unreal.EditableMeshFactory.make_editable_mesh(component,0)

    modify_type = unreal.MeshModificationType.INTERIM
    topo_change = unreal.MeshTopologyChange.TOPOLOGY_CHANGE
    mesh.start_modification(modify_type,topo_change)

    polygon_count = mesh.get_polygon_count()
    polygon_list = [unreal.PolygonID(i) for i in range(polygon_count-1)]
    mode = unreal.TriangleTessellationMode.THREE_TRIANGLES

    mesh.tessellate_polygons(polygon_list,mode)

    mesh.initialize_adapters()
    mesh.commit()
    mesh.rebuild_render_mesh()

    # mesh.end_modification(False)


    # poly_count = mesh.get_polygon_count()
    # print(poly_count)
    # subd_count = mesh.get_subdivision_count()
    # print(subd_count)

    # mesh.set_subdivision_count()
    # poly_count = mesh.get_polygon_count()
    # print(poly_count)
    # subd_count = mesh.get_subdivision_count()
    # print(subd_count)
    # preview = mesh.is_previewing_subdivisions()
    # print(preview)

    # mesh.tessellate_polygons([unreal.PolygonID(i) for i in range(8)],unreal.TriangleTessellationMode.FOUR_TRIANGLES)
