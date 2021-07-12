# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanner_coarse.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_coarse_input(object):
    def setupUi(self, coarse_input):
        if not coarse_input.objectName():
            coarse_input.setObjectName(u"coarse_input")
        coarse_input.resize(1149, 249)
        self.verticalLayout = QVBoxLayout(coarse_input)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(coarse_input)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sc_rz = QDoubleSpinBox(self.groupBox)
        self.sc_rz.setObjectName(u"sc_rz")
        self.sc_rz.setMinimum(-7.000000000000000)
        self.sc_rz.setMaximum(7.000000000000000)
        self.sc_rz.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sc_rz, 2, 13, 1, 1)

        self.sc_rx = QDoubleSpinBox(self.groupBox)
        self.sc_rx.setObjectName(u"sc_rx")
        self.sc_rx.setMinimum(-7.000000000000000)
        self.sc_rx.setMaximum(7.000000000000000)
        self.sc_rx.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sc_rx, 2, 8, 1, 1)

        self.sc_lpz = QLabel(self.groupBox)
        self.sc_lpz.setObjectName(u"sc_lpz")

        self.gridLayout.addWidget(self.sc_lpz, 0, 6, 1, 1)

        self.sc_px = QDoubleSpinBox(self.groupBox)
        self.sc_px.setObjectName(u"sc_px")
        self.sc_px.setMinimum(-500.000000000000000)
        self.sc_px.setMaximum(500.000000000000000)
        self.sc_px.setSingleStep(0.050000000000000)
        self.sc_px.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sc_px, 2, 2, 1, 1)

        self.sc_py = QDoubleSpinBox(self.groupBox)
        self.sc_py.setObjectName(u"sc_py")
        self.sc_py.setMinimum(-500.000000000000000)
        self.sc_py.setMaximum(500.000000000000000)
        self.sc_py.setSingleStep(0.050000000000000)
        self.sc_py.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sc_py, 2, 4, 1, 1)

        self.sc_ry = QDoubleSpinBox(self.groupBox)
        self.sc_ry.setObjectName(u"sc_ry")
        self.sc_ry.setMinimum(-7.000000000000000)
        self.sc_ry.setMaximum(7.000000000000000)
        self.sc_ry.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sc_ry, 2, 10, 1, 1)

        self.sc_pz = QDoubleSpinBox(self.groupBox)
        self.sc_pz.setObjectName(u"sc_pz")
        self.sc_pz.setMinimum(-500.000000000000000)
        self.sc_pz.setMaximum(500.000000000000000)
        self.sc_pz.setSingleStep(0.050000000000000)
        self.sc_pz.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sc_pz, 2, 6, 1, 1)

        self.sc_lry = QLabel(self.groupBox)
        self.sc_lry.setObjectName(u"sc_lry")

        self.gridLayout.addWidget(self.sc_lry, 0, 10, 1, 1)

        self.sc_lpy = QLabel(self.groupBox)
        self.sc_lpy.setObjectName(u"sc_lpy")

        self.gridLayout.addWidget(self.sc_lpy, 0, 4, 1, 1)

        self.sc_lrx = QLabel(self.groupBox)
        self.sc_lrx.setObjectName(u"sc_lrx")

        self.gridLayout.addWidget(self.sc_lrx, 0, 8, 1, 1)

        self.sc_lpx = QLabel(self.groupBox)
        self.sc_lpx.setObjectName(u"sc_lpx")

        self.gridLayout.addWidget(self.sc_lpx, 0, 2, 1, 1)

        self.sc_lrz = QLabel(self.groupBox)
        self.sc_lrz.setObjectName(u"sc_lrz")

        self.gridLayout.addWidget(self.sc_lrz, 0, 13, 1, 1)

        self.sc_fiducial = QLabel(self.groupBox)
        self.sc_fiducial.setObjectName(u"sc_fiducial")

        self.gridLayout.addWidget(self.sc_fiducial, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.sc_next = QPushButton(coarse_input)
        self.sc_next.setObjectName(u"sc_next")

        self.verticalLayout.addWidget(self.sc_next)


        self.retranslateUi(coarse_input)

        QMetaObject.connectSlotsByName(coarse_input)
    # setupUi

    def retranslateUi(self, coarse_input):
        coarse_input.setWindowTitle(QCoreApplication.translate("coarse_input", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("coarse_input", u"Scanner Coarse Input", None))
        self.sc_lpz.setText(QCoreApplication.translate("coarse_input", u"Pz (mm)", None))
        self.sc_lry.setText(QCoreApplication.translate("coarse_input", u"Ry (radians)", None))
        self.sc_lpy.setText(QCoreApplication.translate("coarse_input", u"Py (mm)", None))
        self.sc_lrx.setText(QCoreApplication.translate("coarse_input", u"Rx (radians)", None))
        self.sc_lpx.setText(QCoreApplication.translate("coarse_input", u"Px (mm)", None))
        self.sc_lrz.setText(QCoreApplication.translate("coarse_input", u"Rz (radians)", None))
        self.sc_fiducial.setText(QCoreApplication.translate("coarse_input", u"Coarse Fiducial", None))
        self.sc_next.setText(QCoreApplication.translate("coarse_input", u"Next", None))
    # retranslateUi

