# coding:utf-8

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-01-09 12:57:22'

"""

"""

import sys
# import Tkinter
# import tkMessageBox
import unreal

def print_string(msg):
    unreal.SystemLibrary.print_string(None,msg,text_color=[255,0,0,255])

def getOrAddPossessableInSequenceAsset(sequence_path='', actor=None):
    sequence_asset = unreal.LevelSequence.cast(unreal.load_asset(sequence_path))
    possessable = sequence_asset.add_possessable(object_to_possess=actor)
    return possessable


# animation_path: str : The animation asset path
# possessable: obj unreal.SequencerBindingProxy : The actor binding you want to add the animation on
# return: obj unreal.SequencerBindingProxy : The actor binding
def addSkeletalAnimationTrackOnPossessable(animation_path='', possessable=None):
    # Get Animation
    animation_asset = unreal.AnimSequence.cast(unreal.load_asset(animation_path))
    params = unreal.MovieSceneSkeletalAnimationParams()
    params.set_editor_property('Animation', animation_asset)
    # Add track
    animation_track = possessable.add_track(track_type=unreal.MovieSceneSkeletalAnimationTrack)
    # Add section
    animation_section = animation_track.add_section()
    animation_section.set_editor_property('Params', params)
    animation_section.set_range(0, animation_asset.get_editor_property('sequence_length'))


def addSkeletalAnimationTrackOnActor_EXAMPLE():
    sequence_path = '/Game/test/testSeq' 
    animation_path = '/Game/ArtResources/Characters/90005/90005_L/Animations/90005+atk_1'
    actor_in_world = unreal.GameplayStatics.get_all_actors_of_class(unreal.EditorLevelLibrary.get_editor_world(), unreal.SkeletalMeshActor)()[0]
    possessable_in_sequence = getOrAddPossessableInSequenceAsset(sequence_path, actor_in_world)
    addSkeletalAnimationTrackOnPossessable(animation_path, possessable_in_sequence)
    
def addPreveiwAnim():
    unreal.SystemLibrary.begin_transaction("previwAnim","previwAnim",None)

    selected = unreal.EditorLevelLibrary.get_selected_level_actors()
    
    world = unreal.EditorLevelLibrary.get_editor_world()
    if not world:
        print_string("请打开一个场景")
        return unreal.SystemLibrary.end_transaction()

    if not selected:
        print_string("请选择一个物体")
        return unreal.SystemLibrary.end_transaction()

    selected = selected[0]
    if not type(selected) == unreal.SkeletalMeshActor:
        print_string("请选择一个场景动画骨架")
        return unreal.SystemLibrary.end_transaction()

    actor_class = unreal.EditorAssetLibrary.load_blueprint_class('/Game/test/RedCamAnimActor.RedCamAnimActor')
    camera = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class,unreal.Vector(0.0, 0.0, 0.0))

    # camera = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.CameraActor,unreal.Vector(0.0, 0.0, 0.0))
    # cam_comp = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.RedCamAnimComponent,unreal.Vector(0.0, 0.0, 0.0))
    # cam_comp.attach_to_component(camera.root_component, ' ', unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, False)

    camera.attach_to_actor(selected, ' ', unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, unreal.AttachmentRule.KEEP_WORLD, False)

    sequence_path = '/Game/test/RedSequence.RedSequence'
    sequence_asset = unreal.LevelSequence.cast(unreal.load_asset(sequence_path))
    
    print sequence_asset
    print dir(unreal.MovieSceneSequence)
    
    return unreal.SystemLibrary.end_transaction()

if __name__ == "__main__":
    addPreveiwAnim()

