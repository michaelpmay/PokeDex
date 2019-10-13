import sys
import PySide
from PySide import QtGui
from PySide.QtGui import *
from PySide.QtCore import *
import picamera
import numpy as np
class Camera:
    def __init__(self):
        self.cam=picamera.PiCamera();
        self.previewResolution=(128,128)
        self.fullResolution=(1920,1080)
        self.cam.resolution=self.fullResolution
        
    def capture(self):
        self.cam.start_recording("Temp.h264")
        self.cam.wait_recording(self.videoLength)
        self.cam.stop_recording()
        pass
        
    def startPreview(self):
        self.cam.resolution = self.previewResolution
        self.cam.start_preview()
        pass
    
    def stopPreview(self):
        self.cam.stop_preview()
        pass
    
    def startTimedRecord(self,videoLength):
        self.cam.start_recording("Temp.h264")
        self.cam.wait_recording(videoLength)
        self.cam.stop_recording()
        pass
    
class CameraDisplay(QtGui.QLabel):
    def __init__(self,args):
        super(CameraDisplay,self).__init__(args)
        self.camera=Camera()
        self.camera.resolution=(320,240)
    def updateFrame(self):
        self.camera.cam.capture('temp.jpg')
        output=np.zeros((240,320,3),dtype=np.uint8)
        self.camera.cam.capture(output,'rgb')
        self.setPixmap(QtGui.QPixmap(output))
        
  
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.startUI()
    def startUI(self):
        button1=QPushButton('Begin Recording',self)
        button1.move(50,500)
        button2=QPushButton('Yes',self)
        button2.move(250,500)
        button3=QPushButton('No',self)
        button3.move(400,500)
        frame=QFrame(self)
        frame.setFrameStyle(QFrame.StyledPanel)
        frame.move(10,10)
        frame.setGeometry(10,10,780,480)
        
        label1=QLabel('Image Window',self)
        label1.move(15,10)
        self.setGeometry(500,500,800,550)
        self.setWindowTitle('PokeDex')
        cDisplay=CameraDisplay(frame)
        timer=QTimer(self)
        timer.timeout.connect(cDisplay.updateFrame)
        timer.start(1)
        cDisplay.updateFrame()
        self.show()
        
app = QApplication(sys.argv)
window=MainWindow()
app.exec_()
