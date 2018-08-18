# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yuanc\Desktop\aiui\schedule_face_manager\gui\res\qrcode_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qrcode_dialog(object):
    def setupUi(self, qrcode_dialog):
        qrcode_dialog.setObjectName("qrcode_dialog")
        qrcode_dialog.setWindowModality(QtCore.Qt.WindowModal)
        qrcode_dialog.resize(400, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qrcode_dialog.sizePolicy().hasHeightForWidth())
        qrcode_dialog.setSizePolicy(sizePolicy)
        qrcode_dialog.setMinimumSize(QtCore.QSize(400, 320))
        qrcode_dialog.setMaximumSize(QtCore.QSize(400, 320))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        qrcode_dialog.setFont(font)
        qrcode_dialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(qrcode_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(qrcode_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 464, 258))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pic_qrcode = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_qrcode.sizePolicy().hasHeightForWidth())
        self.pic_qrcode.setSizePolicy(sizePolicy)
        self.pic_qrcode.setMinimumSize(QtCore.QSize(200, 200))
        self.pic_qrcode.setMaximumSize(QtCore.QSize(200, 200))
        self.pic_qrcode.setText("")
        self.pic_qrcode.setPixmap(QtGui.QPixmap(":/other/qrcode.jpg"))
        self.pic_qrcode.setScaledContents(True)
        self.pic_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_qrcode.setObjectName("pic_qrcode")
        self.verticalLayout.addWidget(self.pic_qrcode)
        self.instroduction = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instroduction.sizePolicy().hasHeightForWidth())
        self.instroduction.setSizePolicy(sizePolicy)
        self.instroduction.setMaximumSize(QtCore.QSize(380, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.instroduction.setFont(font)
        self.instroduction.setScaledContents(True)
        self.instroduction.setWordWrap(True)
        self.instroduction.setObjectName("instroduction")
        self.verticalLayout.addWidget(self.instroduction)

        self.retranslateUi(qrcode_dialog)
        self.buttonBox.accepted.connect(qrcode_dialog.accept)
        self.buttonBox.rejected.connect(qrcode_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(qrcode_dialog)

    def retranslateUi(self, qrcode_dialog):
        _translate = QtCore.QCoreApplication.translate
        qrcode_dialog.setWindowTitle(_translate("qrcode_dialog", "qrcode_dialog"))
        self.instroduction.setText(_translate("qrcode_dialog", "      你想要添加微信机器人吗？微信机器人可以帮助您随时随地都能够获得日程提醒"))

import source_rc
