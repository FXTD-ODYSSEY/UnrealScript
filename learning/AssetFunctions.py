import unreal

texture_tga = r"C:\Users\timmyliang\Desktop\Snipaste_2019-12-20_09-57-53.png"
sound_wav = r"C:\Users\timmyliang\Desktop\techniques_menu_audio.mp3"
# sound_wav = ""

def importMyAssets():
    texture_task = buildImportTask(texture_tga,'/Game/Textures')
    # sound_task = buildImportTask(sound_wav,'/Game/Sounds')
    executeImportTasks([texture_task])
    
def buildImportTask(filename,destionation_path):
    
    task = unreal.AssetImportTask()
    task.set_editor_property('automated',True)
    task.set_editor_property('destination_name','')
    task.set_editor_property('destination_path',destionation_path)
    task.set_editor_property('filename',filename)
    task.set_editor_property('replace_existing',True)
    task.set_editor_property('save',True)
    task.set_editor_property('test',True)
    return task

def executeImportTasks(tasks):
    print "tasks",tasks
    tool = unreal.AssetToolsHelpers.get_asset_tools()
    tool.import_asset_tasks(tasks)

    # for task in tasks:
    #     for path in task.get_editor_property('imported_object_paths'):
    #         print 'Imported: %s' % path

# import AssetFunctions
# reload(AssetFunctions)
# AssetFunctions.importMyAssets()

['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_post_init', '_wrapper_meta_data', 'automated', 'cast', 'destination_name', 'destination_path', 'factory', 'filename', 'get_class', 'get_default_object', 'get_editor_property', 'get_fname', 'get_full_name', 'get_name', 'get_outer', 'get_outermost', 'get_path_name', 'get_typed_outer', 'get_world', 'imported_object_paths', 'modify', 'options', 'rename', 'replace_existing', 'result', 'save', 'set_editor_property', 'static_class']
