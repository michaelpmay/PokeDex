# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 520, 781, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button1 = QtWidgets.QPushButton(self.frame)
        self.button1.setGeometry(QtCore.QRect(10, 10, 90, 51))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.frame)
        self.button2.setGeometry(QtCore.QRect(340, 10, 90, 51))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.frame)
        self.button3.setGeometry(QtCore.QRect(680, 10, 90, 51))
        self.button3.setObjectName("button3")
        self.videoView = QtWidgets.QGraphicsView(self.centralwidget)
        self.videoView.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.videoView.setObjectName("videoView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Record"))
        self.button2.setText(_translate("MainWindow", "Yes"))
        self.button3.setText(_translate("MainWindow", "No"))

