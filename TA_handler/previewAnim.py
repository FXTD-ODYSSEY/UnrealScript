# coding:utf-8

__author__ =  'timmyliang'
__email__ =  '820472580@qq.com'
__date__ = '2020-01-09 12:57:22'

"""

"""

import sys
import Tkinter
import tkMessageBox
import unreal


win = Tkinter.Tk()
win.withdraw()
unreal.parent_external_window_to_slate(win.winfo_id())
# tkMessageBox.showerror("错误", sys.argv[0])
win.mainloop()
win.destroy()



# class Error(object,tk.Toplevel):
#     def __init__(self, root ,message):
#         tk.Toplevel.__init__(self)

#         tk.Label(self, text=message).grid(row=0, column=0)
#         tk.Button(self, command=self.destroy, text="OK").grid(row=1, column=0)
#         self.lift()  # Puts Window on top
#         self.grab_set()  # Prevents other Tkinter windows from being used
        
#         self.root = root

#     def destroy(self):
#         super(Error,self).destroy()
#         # tk.Toplevel.destroy()
#         self.root.destroy()



# if __name__ == '__main__':
#     w = tk.Tk()
#     w.withdraw()
#     Error(w,"Help!")
#     w.mainloop()
