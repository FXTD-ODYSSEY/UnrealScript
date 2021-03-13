import unreal

@unreal.uclass()
class ScirptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        super(ScirptObject, self).execute(context)
        # print("context",context)
        obj = context.find_by_class(unreal.Object)
        print (obj)

        return False

    # @unreal.ufunction(override=True)
    # def can_execute(self,context):
    #     super(ScirptObject,self).can_execute(context)
    #     return True

    @unreal.ufunction(override=True)
    def get_label(self, context):
        super(ScirptObject, self).get_label(context)
        return "测试 entry script"


menus = unreal.ToolMenus.get()

menu_name = "ContentBrowser.AddNewContextMenu"
menu = menus.find_menu(menu_name)

# NOTE 如果已经注册则删除 | 否则无法执行 register_menu
if menus.is_menu_registered(menu_name):
    menus.remove_menu(menu_name)

menu = menus.register_menu(menu_name)
entry = unreal.ToolMenuEntry(type=unreal.MultiBlockType.MENU_ENTRY)
entry.set_label("测试 entry")
entry.set_string_command(
    unreal.ToolMenuStringCommandType.PYTHON, "", 'import unreal;unreal.log("menu call")'
)
menu.add_menu_entry("", entry)

script = ScirptObject()
menu.add_menu_entry_object(script)
