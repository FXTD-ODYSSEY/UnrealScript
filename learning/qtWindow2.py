import unreal
import sys

MODULE = r'C:\Python27\Lib\site-packages'
if MODULE not in sys.path:
    sys.path.append(MODULE)
	
from PySide import QtGui, QtUiTools
from Qt.QtCompat import loadUi
import os
WINDOW_NAME = 'Qt Window One'
# DIR = os.path.dirname(__file__)
UI_FILE_FULLNAME = __file__.replace(".py",".ui")

# This function will receive the tick from Unreal
def __QtAppTick__(delta_seconds):
	for window in opened_windows:
		window.eventTick(delta_seconds)

# This function will be called when the application is closing.
def __QtAppQuit__():
	unreal.unregister_slate_post_tick_callback(tick_handle)

# This function is called by the windows when they are closing. (Only if the connection is properly made.)
def __QtWindowClosed__(window=None):
	if window in opened_windows:
		opened_windows.remove(window)

# This part is for the initial setup. Need to run once to spawn the application.
unreal_app = QtGui.QApplication.instance()
if not unreal_app:
	unreal_app = QtGui.QApplication(sys.argv)
	# tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
	# unreal_app.aboutToQuit.connect(__QtAppQuit__)
	existing_windows = {}
	opened_windows = []


# desired_window_class: class QtGui.QWidget : The window class you want to spawn
# return: The new or existing window
def spawnQtWindow(desired_window_class=None):
	window = existing_windows.get(desired_window_class, None)
	if not window:
		window = desired_window_class()
		existing_windows[desired_window_class] = window
		# window.aboutToClose = __QtWindowClosed__
	if window not in opened_windows:
		opened_windows.append(window)
	window.show()
	window.activateWindow()
	return window

def run():
    spawnQtWindow(QtWindowOne)


class QtWindowOne(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowOne, self).__init__(parent)

		layout = QtGui.QVBoxLayout()
		self.setLayout(layout)
		
		self.label = QtGui.QLabel("Test")
		layout.addWidget(self.label)

		self.button = QtGui.QPushButton("click")
		self.button.clicked.connect(self.clickEvent)

		layout.addWidget(self.label)
		layout.addWidget(self.button)
		
		self.setWindowTitle(WINDOW_NAME)
		self.setGeometry(100, 100, self.width(), self.height())


		unreal.parent_external_window_to_slate(self.winId())


	def clickEvent(self):
		print "click"




	
# import sys
# PATH = r"F:\MayaTecent\UnrealScript\learning"
# if PATH not in sys.path:
#     sys.path.append(PATH)

# import qtWindow2
# reload(qtWindow2)

# qtWindow2.run()
   