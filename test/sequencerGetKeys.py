import unreal

def main():
    
    sequence_list = [a for a in unreal.EditorUtilityLibrary.get_selected_assets() if isinstance(a,unreal.LevelSequence)]

    for sequence in sequence_list:
        for binding in sequence.get_bindings():
            # print(binding.get_name())
            for track in binding.get_tracks():
                # print(track.get_name())
                for section in track.get_sections():
                    # print(section.get_name())
                    for channel in section.get_channels():
                        # print(channel)
                        print(channel.get_name())
                        # for key in channel.get_keys():                
                        #     print(key)
        

if __name__ == "__main__":
    main()

    