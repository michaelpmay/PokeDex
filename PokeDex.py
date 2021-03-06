import sys
import PySide
from PySide import QtGui
from PySide.QtGui import *
from PySide.QtCore import *
import picamera
import numpy as np

from gpiozero import Button
import picamera
import datetime as date
from signal import pause
from time import sleep
import os
import pathlib

ioPin1=4
ioPin2=17
ioPin3=27
class TimeStamper:
    @staticmethod
    def getTimeStamp():
        stamp=str(TimeStamper.getEpochSeconds());
        return stamp
    @staticmethod
    def getEpochSeconds():
        epoch=date.datetime.utcfromtimestamp(0)
        currentTime=date.datetime.now()
        return (currentTime-epoch).total_seconds()
    
class MetaData:
    dict={}
    def __init__(self,dictionary={}):
        self.dict=dictionary
        self.dict['timestamp']=self.getTimeStamp()
        self.dict['nId']=self.dict['timestamp'].replace('.','')
    def getMetaData(self):
        return self.dict
    def writeTxt(self):
        string=''
        for key in self.dict:
            string=string+key+','+str(self.dict[key])+','
        string=string[0:(len(string)-1)]
        string=string+'\n'
        return string
    def getTimeStamp(self):
        timeStamp=TimeStamper.getTimeStamp()
        return timeStamp
    def add(self,key,value):
        self.dict[key]=value
class NatureViewerGui:
    def __init__(self):
        natview=NatureViewer()
    
class ToggleButton:
    def __init__(self,gpio):
        self.button=Button(gpio);
        self.state=[False];
        state=self.is_pressed()
        self.previousState=[state]
        self.previousState[0]
        pass
    def getState(self):
        currentState=self.is_pressed()
        if ((self.previousState[0]==False)&(currentState==True)):
            self.swapToggleState()
        self.previousState[0]=currentState
        return self.state
    def swapToggleState(self):
        if (self.state[0]==True):
            self.state[0]=False
        else:
            self.state[0]=True
        pass
    def is_pressed(self):
        return self.button.is_pressed
    
class ClickButton:
    def __init__(self,gpio):
        self.button=Button(gpio)
        self.state=False;
        pass
    def getState(self):
        return self.is_pressed()
    def is_pressed(self):
        return self.button.is_pressed
        
class Camera:
    def __init__(self):
        self.cam=picamera.PiCamera();
        self.previewResolution=(128,128)
        self.fullResolution=(1920,1080)
        self.cam.resolution=self.fullResolution
        
    def capture(self):
        self.cam.start_recording("Temp.h264")
        self.cam.stop_recording()
        pass
    def snap(self):
        self.cam.resolution=self.fullResolution
        self.cam.cap
    def startPreview(self):
        self.cam.resolution = self.previewResolution
        self.cam.start_preview()
        pass
    
    def stopPreview(self):
        self.cam.stop_preview()
        pass
    
    def startTimedRecord(self,videoLength):
        self.cam.start_recording("Temp.h264")
        self.cam.stop_recording()
        pass
        
class FileSystem:
    def __init__(self):
        self.folder='/home/pi/Videos/'
        self.metaFileName='meta.txt'
        self.metaFilePath=self.folder+self.metaFileName
        
    def saveVideo(self,name,metaData):
        newName,nid=self.getUniqueName(name,metaData)
        self.rename(name,newName)
        self.saveMetaData(metaData)
        return nid
    
    def saveMetaData(self,metaData):
        file=open(self.metaFilePath,'a')
        file.write(metaData.writeTxt())
        file.close()
        
    def getUniqueName(self,name,metaData):
        if metaData.dict['nId']:
            timeStamp=metaData.dict['nId']
        else:
            timeStamp=str(TimeStamper.getTimeStamp())
            timeStamp.replace('.','')
        extInd=name.find('.')
        name=name[:extInd]+'_'+timeStamp+name[extInd:]
        return name,timeStamp
        
    def getMetaData(self,metadata):
        return metaData.getMetaData
    
    def rename(self,name,newName):
        os.system("mv "+name+" "+self.folder+newName)

class Camera:
    def __init__(self):
        try:
            self.cam=picamera.PiCamera()
        except:
            self.cam=TestCam()
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
    
    def startTimedRecord(self,videoLength,name):
        self.cam.start_recording(name)
        self.cam.wait_recording(videoLength)
        self.cam.stop_recording()
        pass
class TestCam:
    def start_recording(self,name):
        pass
    def stop_recording(self):
        pass
    def wait_recording(self,time):
        pass
    def start_preview(self):
        pass
    def stop_preview(self):
        pass
    def capture(self,output,formatType):
        pass
class CameraDisplay(QtGui.QLabel):
    resolution=(1280,720)
    output=np.zeros((resolution[1],resolution[0],3),dtype=np.uint8)
    def __init__(self,args):
        super(CameraDisplay,self).__init__(args)
        self.camera=Camera()
        self.camera.cam.resolution=self.resolution
    def updateFrame(self):
        qImg=self.snapQImage()
        self.setPixmap(QtGui.QPixmap.fromImage(qImg))
    def snapQImage(self):
        self.camera.cam.capture(self.output,'rgb')
        qImg=QImage(self.output.data,self.resolution[0],self.resolution[1], QtGui.QImage.Format_RGB888)
        return qImg
    
class Worker(QRunnable):
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        self.fn = fn
        self.args=args
        self.kwargs=kwargs
    def run(self):
        result=self.fn(*self.args,**self.kwargs)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.filesystem=FileSystem()
        self.startUI()
    def startUI(self):
        self.threadpool=QThreadPool()
        self.button1=QPushButton('Begin Recording',self)
        self.button1.move(50,500)
        self.button1.setShortcut('R')
        self.button1.clicked.connect(self.eventBeginRecord)
        self.button2=QPushButton('Yes',self)
        self.button2.move(250,500)
        self.button2.setShortcut('y')
        self.button3=QPushButton('No',self)
        self.button3.move(400,500)
        self.button3.setShortcut('n')
        self.frame=QFrame(self)
        self.frame.setFrameStyle(QFrame.StyledPanel)
        self.frame.move(10,10)
        self.frame.setGeometry(10,10,780,440)
        self.recordLabel=QLabel('',self)
        self.recordLabel.move(15,10)
        self.outputLabel=QLabel('Output Window',self)
        self.outputLabel.move(100,450)
        self.outputLabel.setGeometry(10,460,780,40)
        self.outputLabel.setFrameStyle(QFrame.StyledPanel)
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle('PokeDex')
        self.cDisplay=CameraDisplay(self.frame)
        timer=QTimer(self)
        timer.timeout.connect(self.cDisplay.updateFrame)
        timer.start(100)
        self.cDisplay.updateFrame()
        self.show()
    def queue(self,fn,*args,**kwargs):
        worker=Worker(fn,args,awargs)
        self.threadpool.start(worker)
    def eventBeginRecord(self):
        self.recordLabel.setText('Recording...')
        self.recordLabel.setStyleSheet('QLabel {color:red; font: bold 16pt;}')
        self.recordLabel.update()
        QApplication.processEvents()
        self.cDisplay.camera.startTimedRecord(15,'vid.h264')
        self.eventInputMetaDataTree()
    def eventInputMetaDataTree(self):
        metaData=MetaData()
        self.outputLabel.setText('Did you see movement?')
        self.outputLabel.show()
        trueCall=lambda:self.eventInputMetaMovement(metaData,True)
        falseCall=lambda:self.eventInputMetaMovement(metaData,False)
        self.button2.clicked.connect(trueCall)
        self.button3.clicked.connect(falseCall)
        pass
    def eventInputMetaMovement(self,metaData,tfBool):
        metaData.add('movement',tfBool)
        self.outputLabel.setText("Thank you!")
        self.filesystem.saveVideo('vid.h264',metaData)
              
#fileSystem=FileSystem()
#mData=MetaData()
#mData.add('movement',True)
#fileSystem.saveVideo('test.vid',mData)
app = QApplication(sys.argv)
window=MainWindow()
app.exec_()
