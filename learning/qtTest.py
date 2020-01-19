import sys

import os
plugin_path = r"C:\Program Files\Autodesk\Maya2017\qt-plugins\platforms"
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets


def window():
   app = QtWidgets.QApplication(sys.argv)
   w = QtWidgets.QWidget()
   b = QtWidgets.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
