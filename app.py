from PyQt5 import *
from PyQt5.QtGui import QtWidgets
import sys
import frontend

class ExampleApp(QtWidgets.QMainWindow, frontend.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()