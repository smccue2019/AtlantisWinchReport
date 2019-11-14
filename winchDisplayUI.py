# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winchDisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(20, 20, 180, 50))
        self.groupBox1.setObjectName("groupBox1")
        self.gb1_text_display = QtWidgets.QLabel(self.groupBox1)
        self.gb1_text_display.setGeometry(QtCore.QRect(60, 20, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gb1_text_display.setFont(font)
        self.gb1_text_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gb1_text_display.setAlignment(QtCore.Qt.AlignCenter)
        self.gb1_text_display.setObjectName("gb1_text_display")
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(20, 100, 180, 50))
        self.groupBox2.setObjectName("groupBox2")
        self.gb2_text_display = QtWidgets.QLabel(self.groupBox2)
        self.gb2_text_display.setGeometry(QtCore.QRect(60, 20, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gb2_text_display.setFont(font)
        self.gb2_text_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gb2_text_display.setAlignment(QtCore.Qt.AlignCenter)
        self.gb2_text_display.setObjectName("gb2_text_display")
        self.groupBox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox3.setGeometry(QtCore.QRect(20, 180, 180, 50))
        self.groupBox3.setObjectName("groupBox3")
        self.gb3_text_display = QtWidgets.QLabel(self.groupBox3)
        self.gb3_text_display.setGeometry(QtCore.QRect(60, 20, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gb3_text_display.setFont(font)
        self.gb3_text_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gb3_text_display.setAlignment(QtCore.Qt.AlignCenter)
        self.gb3_text_display.setObjectName("gb3_text_display")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(220, 220, 45, 27))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox1.setTitle(_translate("MainWindow", "Tension"))
        self.gb1_text_display.setText(_translate("MainWindow", "text"))
        self.groupBox2.setTitle(_translate("MainWindow", "Wire Out"))
        self.gb2_text_display.setText(_translate("MainWindow", "text"))
        self.groupBox3.setTitle(_translate("MainWindow", "Payout Rate"))
        self.gb3_text_display.setText(_translate("MainWindow", "text"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))

