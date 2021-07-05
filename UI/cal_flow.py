# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal_flow.ui',
# licensing of 'cal_flow.ui' applies.
#
# Created: Sun Jul  4 21:13:01 2021
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_WDG_cal_flow(object):
    def setupUi(self, WDG_cal_flow):
        WDG_cal_flow.setObjectName("WDG_cal_flow")
        WDG_cal_flow.resize(1127, 392)
        self.verticalLayout = QtWidgets.QVBoxLayout(WDG_cal_flow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(WDG_cal_flow)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 1091, 261))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(970, 290, 106, 29))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(WDG_cal_flow)
        QtCore.QMetaObject.connectSlotsByName(WDG_cal_flow)

    def retranslateUi(self, WDG_cal_flow):
        WDG_cal_flow.setWindowTitle(QtWidgets.QApplication.translate("WDG_cal_flow", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("WDG_cal_flow", "Calibration Flow", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("WDG_cal_flow", "Instruction", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("WDG_cal_flow", "Next", None, -1))

