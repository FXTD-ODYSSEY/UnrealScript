# coding=utf8
# Copyright (c) 2020 GVF

import unreal
import os

@unreal.uclass()
class BPFunctionLibrary(unreal.BlueprintFunctionLibrary):
    @unreal.ufunction(ret=bool, params=[str], static=True, meta=dict(Category="Render Sequence"))
    def RenderSequence(path):
        capture_settings = unreal.AutomatedLevelSequenceCapture()
        capture_settings.level_sequence_asset = unreal.SoftObjectPath(path)
        try:
            unreal.SequencerTools.render_movie(capture_settings, unreal.OnRenderMovieStopped())
            return True
        except Exception as e:
            print("Python Caught Exception:")
            print(e)
            return False
        unreal.log("Render Sequence...")

    @unreal.ufunction(params=[str, str], static=True, meta=dict(Category="Render Sequence Controller"))
    def render_sequence_to_movie(sequence_path, sequence_name):

        def on_render_movie_finished(success):
            print("Movie has finished rendering. Python can now invoke another movie render if needed. Sucess: " + str(
                success))

        on_finished_callback = unreal.OnRenderMovieStopped()
        on_finished_callback.bind_callable(on_render_movie_finished)

        file_path = sequence_path + "/" + sequence_name

        capture_settings = unreal.AutomatedLevelSequenceCapture()

        # out put path
        capture_settings.settings.output_directory = unreal.DirectoryPath("../../../Game/Saved/VideoCaptures/")

        capture_settings.settings.game_mode_override = None

        # out put name
        capture_settings.settings.output_format = sequence_name

        capture_settings.settings.overwrite_existing = False
        capture_settings.settings.use_relative_frame_numbers = False
        capture_settings.settings.handle_frames = 0
        capture_settings.settings.zero_pad_frame_numbers = 4

        capture_settings.settings.use_custom_frame_rate = True

        capture_settings.settings.custom_frame_rate = unreal.FrameRate(24, 1)
        capture_settings.settings.resolution.res_x = 1280
        capture_settings.settings.resolution.res_y = 720

        capture_settings.settings.enable_texture_streaming = False
        capture_settings.settings.cinematic_engine_scalability = True
        capture_settings.settings.cinematic_mode = True
        capture_settings.settings.allow_movement = False
        capture_settings.settings.allow_turning = False
        capture_settings.settings.show_player = False
        capture_settings.settings.show_hud = False
        capture_settings.use_separate_process = False
        capture_settings.close_editor_when_capture_starts = False
        capture_settings.additional_command_line_arguments = "-NOSCREENMESSAGES"
        capture_settings.inherited_command_line_arguments = ""

        capture_settings.use_custom_start_frame = False
        capture_settings.use_custom_end_frame = False
        capture_settings.custom_start_frame = unreal.FrameNumber(0)
        capture_settings.custom_end_frame = unreal.FrameNumber(0)
        capture_settings.warm_up_frame_count = 0.0
        capture_settings.delay_before_warm_up = 0
        capture_settings.delay_before_shot_warm_up = 0.0
        capture_settings.write_edit_decision_list = True

        # Change format
        capture_settings.set_image_capture_protocol_type(
            unreal.load_class(None, "/Script/MovieSceneCapture.ImageSequenceProtocol_JPG"))
        capture_settings.get_image_capture_protocol().compression_quality = 100

        capture_settings.level_sequence_asset = unreal.SoftObjectPath(file_path)
        unreal.SequencerTools.render_movie(capture_settings, on_finished_callback)

        # i = 0
        # length = len(sequence_path)
        # on_finished_callback = unreal.OnRenderMovieStopped()
        # capture_settings.level_sequence_asset = unreal.SoftObjectPath(sequence_path)
        # unreal.SequencerTools.render_movie(capture_settings, on_finished_callback)
        # print(str(length) + "======================================================================================================")
        # on_finished_callback.bind_callable(lambda: render_next_sequence(i, sequence_path))
        #
        # def render_next_sequence(i, sequencer_asset_path):
        #     print(str(i) + "**************************************************************************************")
        #     i += 1
        #     if i < length:
        #         on_finished_callback = unreal.OnRenderMovieStopped()
        #         capture_settings.level_sequence_asset = unreal.SoftObjectPath(sequence_path[i])
        #         unreal.SequencerTools.render_movie(capture_settings, on_finished_callback)
        #         on_finished_callback.bind_callable(lambda: render_next_sequence(i, sequence_path))

    @unreal.ufunction(ret=str, params=[str, str], static=True, meta=dict(Category="Create folder"))
    def create_folder(path, name):

        folder_path = path + "\\" + name
        isExists = os.path.exists(folder_path)
        if not isExists:
            os.makedirs(folder_path)
            return folder_path
        else:
            return folder_path

    @unreal.ufunction(ret=str, params=[str], static=True, meta=dict(Category="Get Project Directory Path"))
    def get_project_directory_path(path):

        x = unreal.Paths.get_project_file_path()
        y = unreal.Paths.make_standard_filename(x)

        project_name = y.split("/")[-1]
        project_path = y.split(project_name)[0]

        return project_path

    @unreal.ufunction(ret=str, params=[str], static=True, meta=dict(Category="Convert UE4 Path To Standard Path"))
    def convert_UE4_path_to_standard_path(path):
        x = unreal.Paths.make_standard_filename(path)
        return x

    # @unreal.ufunction(ret=str, params=[str], static=True, meta=dict(Category="Convert Standard Path To UE4 Path"))
    # def convert_standard_path_to_UE4_path(path):
    #     x = unreal.Paths.make_platform_filename(path)
    #     return x

    @unreal.ufunction(ret=unreal.Array(str), params=[unreal.Array(str)], static=True, meta=dict(Category="Ergodic Folder"))
    def ergodic_folder(paths):
        standard_path_list = []

        for path in paths:
            standard_path = unreal.Paths.make_standard_filename(path)
            standard_path_list.append(standard_path)

        return standard_path_list



unreal.log("BPFunctionLibrary was loaded")