import sys
import random
from PySide.QtCore import *
from PySide.QtWidgets import *
from PySide.QtMultimedia import *
from PySide.QtMultimediaWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setObjectName("MainWindow")
        self.resize(800, 596)
        self.mainWidget=MyWidget(self)

class MyWidget(QWidget):
    def __init__(self,MainWindow):
        super(MyWidget, self).__init__(None)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(10, 520, 781, 71))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button1 = QPushButton(self.frame)
        self.button1.setGeometry(QRect(10, 10, 90, 51))
        self.button1.setObjectName("button1")
        self.button2 = QPushButton(self.frame)
        self.button2.setGeometry(QRect(340, 10, 90, 51))
        self.button2.setObjectName("button2")
        self.button3 = QPushButton(self.frame)
        self.button3.setGeometry(QRect(680, 10, 90, 51))
        self.button3.setObjectName("button3")
        self.videoView = QCameraViewfinder(self.centralwidget)
        self.videoView.setGeometry(QRect(10, 10, 781, 501))
        self.videoView.setObjectName("videoView")
        self.online_webcams = QCameraInfo.availableCameras()
        if not self.online_webcams:
            pass  # quit
        self.camera = QCameraViewfinder(self.frame)
        self.get_webcam(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def get_webcam(self, i):
        self.webcam = QCamera(self.online_webcams[i])
        self.webcam.setViewfinder(self.videoView)
        self.webcam.setCaptureMode(QCamera.CaptureStillImage)
        self.webcam.error.connect(lambda: self.alert(self.webcam.errorString()))
        self.webcam.start()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Record"))
        self.button2.setText(_translate("MainWindow", "Yes"))
        self.button3.setText(_translate("MainWindow", "No"))

    def alert(self, s):
        """
        This handle errors and displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)

def main():
    app=QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()