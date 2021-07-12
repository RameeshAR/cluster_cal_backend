# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanner_fine.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_scanner_fine_input(object):
    def setupUi(self, scanner_fine_input):
        if not scanner_fine_input.objectName():
            scanner_fine_input.setObjectName(u"scanner_fine_input")
        scanner_fine_input.resize(1147, 180)
        self.horizontalLayout = QHBoxLayout(scanner_fine_input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(scanner_fine_input)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sf_lpx = QLabel(self.groupBox)
        self.sf_lpx.setObjectName(u"sf_lpx")

        self.gridLayout.addWidget(self.sf_lpx, 0, 1, 1, 1)

        self.sf_lpy = QLabel(self.groupBox)
        self.sf_lpy.setObjectName(u"sf_lpy")

        self.gridLayout.addWidget(self.sf_lpy, 0, 2, 1, 1)

        self.sf_lpz = QLabel(self.groupBox)
        self.sf_lpz.setObjectName(u"sf_lpz")

        self.gridLayout.addWidget(self.sf_lpz, 0, 3, 1, 1)

        self.sf_lrx = QLabel(self.groupBox)
        self.sf_lrx.setObjectName(u"sf_lrx")

        self.gridLayout.addWidget(self.sf_lrx, 0, 4, 1, 1)

        self.sf_lry = QLabel(self.groupBox)
        self.sf_lry.setObjectName(u"sf_lry")

        self.gridLayout.addWidget(self.sf_lry, 0, 5, 1, 1)

        self.sf_lrz = QLabel(self.groupBox)
        self.sf_lrz.setObjectName(u"sf_lrz")

        self.gridLayout.addWidget(self.sf_lrz, 0, 6, 1, 1)

        self.sf_fiducial = QLabel(self.groupBox)
        self.sf_fiducial.setObjectName(u"sf_fiducial")

        self.gridLayout.addWidget(self.sf_fiducial, 1, 0, 1, 1)

        self.sf_px = QDoubleSpinBox(self.groupBox)
        self.sf_px.setObjectName(u"sf_px")
        self.sf_px.setMinimum(-500.000000000000000)
        self.sf_px.setMaximum(500.000000000000000)
        self.sf_px.setSingleStep(0.050000000000000)
        self.sf_px.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sf_px, 1, 1, 1, 1)

        self.sf_py = QDoubleSpinBox(self.groupBox)
        self.sf_py.setObjectName(u"sf_py")
        self.sf_py.setMinimum(-500.000000000000000)
        self.sf_py.setMaximum(500.000000000000000)
        self.sf_py.setSingleStep(0.050000000000000)
        self.sf_py.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sf_py, 1, 2, 1, 1)

        self.sf_pz = QDoubleSpinBox(self.groupBox)
        self.sf_pz.setObjectName(u"sf_pz")
        self.sf_pz.setMinimum(-500.000000000000000)
        self.sf_pz.setMaximum(500.000000000000000)
        self.sf_pz.setSingleStep(0.050000000000000)
        self.sf_pz.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sf_pz, 1, 3, 1, 1)

        self.sf_rx = QDoubleSpinBox(self.groupBox)
        self.sf_rx.setObjectName(u"sf_rx")
        self.sf_rx.setMinimum(-7.000000000000000)
        self.sf_rx.setMaximum(7.000000000000000)
        self.sf_rx.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sf_rx, 1, 4, 1, 1)

        self.sf_ry = QDoubleSpinBox(self.groupBox)
        self.sf_ry.setObjectName(u"sf_ry")
        self.sf_ry.setMinimum(-7.000000000000000)
        self.sf_ry.setMaximum(7.000000000000000)
        self.sf_ry.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sf_ry, 1, 5, 1, 1)

        self.sf_rz = QDoubleSpinBox(self.groupBox)
        self.sf_rz.setObjectName(u"sf_rz")
        self.sf_rz.setMinimum(-7.000000000000000)
        self.sf_rz.setMaximum(7.000000000000000)
        self.sf_rz.setSingleStep(0.025000000000000)

        self.gridLayout.addWidget(self.sf_rz, 1, 6, 1, 1)

        self.sf_next = QPushButton(self.groupBox)
        self.sf_next.setObjectName(u"sf_next")

        self.gridLayout.addWidget(self.sf_next, 1, 7, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(scanner_fine_input)

        QMetaObject.connectSlotsByName(scanner_fine_input)
    # setupUi

    def retranslateUi(self, scanner_fine_input):
        scanner_fine_input.setWindowTitle(QCoreApplication.translate("scanner_fine_input", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("scanner_fine_input", u"Scanner Fine Input", None))
        self.sf_lpx.setText(QCoreApplication.translate("scanner_fine_input", u"Px (mm)", None))
        self.sf_lpy.setText(QCoreApplication.translate("scanner_fine_input", u"Py (mm)", None))
        self.sf_lpz.setText(QCoreApplication.translate("scanner_fine_input", u"Pz (mm)", None))
        self.sf_lrx.setText(QCoreApplication.translate("scanner_fine_input", u"Rx (radians)", None))
        self.sf_lry.setText(QCoreApplication.translate("scanner_fine_input", u"Ry (radians)", None))
        self.sf_lrz.setText(QCoreApplication.translate("scanner_fine_input", u"Rz (radians)", None))
        self.sf_fiducial.setText(QCoreApplication.translate("scanner_fine_input", u"Fine Fiducial", None))
        self.sf_next.setText(QCoreApplication.translate("scanner_fine_input", u"Next", None))
    # retranslateUi

