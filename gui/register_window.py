# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mumumushi/Programs/schedule_face_manager/Smart/gui/res/register_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_window(object):
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(register_window.sizePolicy().hasHeightForWidth())
        register_window.setSizePolicy(sizePolicy)
        register_window.setMinimumSize(QtCore.QSize(1280, 800))
        register_window.setMaximumSize(QtCore.QSize(1280, 800))
        self.centralwidget = QtWidgets.QWidget(register_window)
        self.centralwidget.setObjectName("centralwidget")
        self.reg_background = QtWidgets.QLabel(self.centralwidget)
        self.reg_background.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg_background.sizePolicy().hasHeightForWidth())
        self.reg_background.setSizePolicy(sizePolicy)
        self.reg_background.setMinimumSize(QtCore.QSize(1280, 800))
        self.reg_background.setMaximumSize(QtCore.QSize(1280, 800))
        self.reg_background.setText("")
        self.reg_background.setPixmap(QtGui.QPixmap(":/background/background.png"))
        self.reg_background.setScaledContents(True)
        self.reg_background.setAlignment(QtCore.Qt.AlignCenter)
        self.reg_background.setObjectName("reg_background")
        self.pic_face = QtWidgets.QLabel(self.centralwidget)
        self.pic_face.setGeometry(QtCore.QRect(200, 200, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_face.sizePolicy().hasHeightForWidth())
        self.pic_face.setSizePolicy(sizePolicy)
        self.pic_face.setMinimumSize(QtCore.QSize(400, 400))
        self.pic_face.setMaximumSize(QtCore.QSize(400, 400))
        self.pic_face.setText("")
        self.pic_face.setPixmap(QtGui.QPixmap(":/other/pic_people.png"))
        self.pic_face.setScaledContents(True)
        self.pic_face.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_face.setObjectName("pic_face")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(830, 320, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_name.setObjectName("edit_name")
        self.verticalLayout.addWidget(self.edit_name)
        self.btn_camera = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_camera.setObjectName("btn_camera")
        self.verticalLayout.addWidget(self.btn_camera)
        self.btn_register = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_register.setObjectName("btn_register")
        self.verticalLayout.addWidget(self.btn_register)
        register_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "RegisterWindow"))
        self.btn_camera.setText(_translate("register_window", "启动相机"))
        self.btn_register.setText(_translate("register_window", "注册"))

import source_rc
