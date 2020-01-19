import unreal
import sys
sys.path.append('C:/Python27/Lib/site-packages')
from PySide import QtGui, QtUiTools

WINDOW_NAME = 'Qt Window Two'
UI_FILE_FULLNAME = __file__.replace('.py', '.ui')

class QtWindowTwo(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowTwo, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed
		self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)
		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		self.setGeometry(100, 300, self.widget.width(), self.widget.height())
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
		self.widget.button_RotateRandom.clicked.connect(self.rotateRandomActorInScene)

	def rotateRandomActorInScene(self):
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
			speed = 90.0 * delta_seconds
			self.random_actor.add_actor_world_rotation(unreal.Rotator(0.0, 0.0, speed), False, False)