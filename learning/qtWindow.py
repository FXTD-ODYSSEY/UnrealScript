import unreal

# import os
# plugin_path = r"D:\Anaconda2\pkgs\qt-5.6.2-vc9hc26998b_12\Library\plugins\platforms"
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import sys
sys.path.append('D:\Anaconda2\Lib\site-packages')
# from PySide2 import QtGui
# from PySide2 import QtCore
# from PySide2 import QtWidgets
# from PySide2 import QtUiTools

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import uic

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
unreal_app = QtWidgets.QApplication.instance()
if not unreal_app:
	unreal_app = QtWidgets.QApplication(sys.argv)
	tick_handle = unreal.register_slate_post_tick_callback(__QtAppTick__)
	unreal_app.aboutToQuit.connect(__QtAppQuit__)
	existing_windows = {}
	opened_windows = []

# desired_window_class: class QtGui.QWidget : The window class you want to spawn
# return: The new or existing window
def spawnQtWindow(desired_window_class=None):
	window = existing_windows.get(desired_window_class, None)
	if not window:
		window = desired_window_class()
		existing_windows[desired_window_class] = window
		window.aboutToClose = __QtWindowClosed__
	if window not in opened_windows:
		opened_windows.append(window)
	window.show()
	window.activateWindow()
	return window

def run():
    spawnQtWindow(QtWindowOne)

WINDOW_NAME = 'Qt Window One'
UI_FILE_FULLNAME = __file__.replace('.py', '.ui')

class QtWindowOne(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowOne, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed
		# self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)
		self.widget = uic.loadUi(UI_FILE_FULLNAME)
		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		self.setGeometry(100, 100, self.widget.width(), self.widget.height())
		self.initialiseWidget()

	def closeEvent(self, event):
		if self.aboutToClose:
			self.aboutToClose(self)
		event.accept()

	def eventTick(self, delta_seconds):
		self.myTick(delta_seconds)


	##########################################


	def initialiseWidget(self):
		self.time_while_this_window_is_open = 0.0
		self.random_actor = None
		self.random_actor_is_going_up = True
		self.widget.button_MoveRandom.clicked.connect(self.moveRandomActorInScene)

	def moveRandomActorInScene(self):
		import random
		import WorldFunctions
		all_actors = WorldFunctions.getAllActors(use_selection = False, actor_class = unreal.StaticMeshActor, actor_tag = None)
		rand = random.randrange(0, len(all_actors))
		self.random_actor = all_actors[rand]

	def myTick(self, delta_seconds):
		# Set Time
		self.time_while_this_window_is_open += delta_seconds
		self.widget.lbl_Seconds.setText("%.1f Seconds" % self.time_while_this_window_is_open)
		# Affect Actor
		if self.random_actor:
			actor_location = self.random_actor.get_actor_location()
			speed = 300.0 * delta_seconds
			if self.random_actor_is_going_up:
				if actor_location.z > 1000.0:
					self.random_actor_is_going_up = False
			else:
				speed = -speed
				if actor_location.z < 0.0:
					self.random_actor_is_going_up = True
			self.random_actor.add_actor_world_offset(unreal.Vector(0.0, 0.0, speed), False, False)

	
if __name__ == '__main__':
   run()

# import sys
# PATH = r"F:\MayaTecent\UnrealScript\learning"
# if PATH not in sys.path:
#     sys.path.append(PATH)

# import qtWindow
# reload(qtWindow)

   