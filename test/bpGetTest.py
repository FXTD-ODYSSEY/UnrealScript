import unreal

actors = unreal.EditorLevelLibrary.get_selected_level_actors()
 
# Blueprint'/Game/ArtResources/Test/Effects/testShanZhi_FootFX/Ice_hit/test_725/BP_test.BP_test'

for actor in actors:
    fx_comp = actor.get_component_by_class(unreal.RedEntityEffect_Transform)
    if not fx_comp:
        continue
    
    fx_comp.set_editor_property("CurveScale")
    fx_comp.set_editor_property("CurveRotation")
    fx_comp.set_editor_property("CurveLocation")

    