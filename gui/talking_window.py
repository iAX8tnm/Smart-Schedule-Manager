# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talking_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 800))
        self.centralwidget.setStatusTip("")
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setMinimumSize(QtCore.QSize(1280, 800))
        self.background.setMaximumSize(QtCore.QSize(1280, 800))
        self.background.setAutoFillBackground(True)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/background/zentree_1.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.btn_record = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record.setGeometry(QtCore.QRect(640, 660, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_record.sizePolicy().hasHeightForWidth())
        self.btn_record.setSizePolicy(sizePolicy)
        self.btn_record.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_record.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btn_record.setFont(font)
        self.btn_record.setAutoFillBackground(False)
        self.btn_record.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/btn_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_record.setIcon(icon)
        self.btn_record.setIconSize(QtCore.QSize(50, 50))
        self.btn_record.setFlat(True)
        self.btn_record.setObjectName("btn_record")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import source_rc
