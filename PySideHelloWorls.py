import sys
import PySide
from PySide.QtGui import QMessageBox
from PySide.QtGui import QApplication
app = QApplication(sys.argv)
msgBox = QMessageBox()
msgBox.setText("hello world")
msgBox.exec_()