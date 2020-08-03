import unreal

def main():
    
    sequence_list = [a for a in unreal.EditorUtilityLibrary.get_selected_assets() if isinstance(a,unreal.LevelSequence)]

    for sequence in sequence_list:
        for binding in sequence.get_bindings():
            for track in binding.get_tracks():
                for section in track.get_sections():
                    for channel in section.get_channels():
                        print(channel)
                        print(channel.get_name())
                        for key in channel.get_keys():				
                            print(key)
        # continue
        # tracks = seq.get_master_tracks()
        # print(tracks)
        # if not tracks:
        #     continue
        # track = tracks[0]
        # for section in track.get_sections():
        #     pass
        # print(tracks)
        

if __name__ == "__main__":
    main()

    