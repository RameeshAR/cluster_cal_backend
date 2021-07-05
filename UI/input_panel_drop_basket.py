# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_panel_drop_basket.ui',
# licensing of 'input_panel_drop_basket.ui' applies.
#
# Created: Mon Jul  5 00:06:53 2021
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_WDG_input_panel_drop_basket(object):
    def setupUi(self, WDG_input_panel_drop_basket):
        WDG_input_panel_drop_basket.setObjectName("WDG_input_panel_drop_basket")
        WDG_input_panel_drop_basket.resize(1131, 303)
        self.horizontalLayout = QtWidgets.QHBoxLayout(WDG_input_panel_drop_basket)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(WDG_input_panel_drop_basket)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.LBL_fiducial_1 = QtWidgets.QLabel(self.groupBox)
        self.LBL_fiducial_1.setObjectName("LBL_fiducial_1")
        self.gridLayout.addWidget(self.LBL_fiducial_1, 1, 0, 1, 1)
        self.LBL_fiducial_2 = QtWidgets.QLabel(self.groupBox)
        self.LBL_fiducial_2.setObjectName("LBL_fiducial_2")
        self.gridLayout.addWidget(self.LBL_fiducial_2, 2, 0, 1, 1)
        self.LBL_Pz = QtWidgets.QLabel(self.groupBox)
        self.LBL_Pz.setObjectName("LBL_Pz")
        self.gridLayout.addWidget(self.LBL_Pz, 0, 3, 1, 1)
        self.LBL_Px = QtWidgets.QLabel(self.groupBox)
        self.LBL_Px.setObjectName("LBL_Px")
        self.gridLayout.addWidget(self.LBL_Px, 0, 1, 1, 1)
        self.DSB_pz_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_pz_2.setMinimum(-500.0)
        self.DSB_pz_2.setMaximum(500.0)
        self.DSB_pz_2.setSingleStep(0.05)
        self.DSB_pz_2.setObjectName("DSB_pz_2")
        self.gridLayout.addWidget(self.DSB_pz_2, 2, 3, 1, 1)
        self.DSB_pz_1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_pz_1.setMinimum(-500.0)
        self.DSB_pz_1.setMaximum(500.0)
        self.DSB_pz_1.setSingleStep(0.05)
        self.DSB_pz_1.setObjectName("DSB_pz_1")
        self.gridLayout.addWidget(self.DSB_pz_1, 1, 3, 1, 1)
        self.DSB_px_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_px_2.setMinimum(-500.0)
        self.DSB_px_2.setMaximum(500.0)
        self.DSB_px_2.setSingleStep(0.05)
        self.DSB_px_2.setObjectName("DSB_px_2")
        self.gridLayout.addWidget(self.DSB_px_2, 2, 1, 1, 1)
        self.DSB_py_1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_py_1.setMinimum(-500.0)
        self.DSB_py_1.setMaximum(500.0)
        self.DSB_py_1.setSingleStep(0.05)
        self.DSB_py_1.setObjectName("DSB_py_1")
        self.gridLayout.addWidget(self.DSB_py_1, 1, 2, 1, 1)
        self.PB_calibrate = QtWidgets.QPushButton(self.groupBox)
        self.PB_calibrate.setObjectName("PB_calibrate")
        self.gridLayout.addWidget(self.PB_calibrate, 3, 4, 1, 1)
        self.DSB_px_1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_px_1.setMinimum(-500.0)
        self.DSB_px_1.setMaximum(500.0)
        self.DSB_px_1.setSingleStep(0.05)
        self.DSB_px_1.setObjectName("DSB_px_1")
        self.gridLayout.addWidget(self.DSB_px_1, 1, 1, 1, 1)
        self.DSB_py_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.DSB_py_2.setMinimum(-500.0)
        self.DSB_py_2.setMaximum(500.0)
        self.DSB_py_2.setSingleStep(0.05)
        self.DSB_py_2.setObjectName("DSB_py_2")
        self.gridLayout.addWidget(self.DSB_py_2, 2, 2, 1, 1)
        self.LBL_Py = QtWidgets.QLabel(self.groupBox)
        self.LBL_Py.setObjectName("LBL_Py")
        self.gridLayout.addWidget(self.LBL_Py, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(WDG_input_panel_drop_basket)
        QtCore.QMetaObject.connectSlotsByName(WDG_input_panel_drop_basket)

    def retranslateUi(self, WDG_input_panel_drop_basket):
        WDG_input_panel_drop_basket.setWindowTitle(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Input  panel", None, -1))
        self.LBL_fiducial_1.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Fiducial 1", None, -1))
        self.LBL_fiducial_2.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Fiducial 2", None, -1))
        self.LBL_Pz.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Pz (mm)", None, -1))
        self.LBL_Px.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Px (mm)", None, -1))
        self.PB_calibrate.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Calibrate", None, -1))
        self.LBL_Py.setText(QtWidgets.QApplication.translate("WDG_input_panel_drop_basket", "Py (mm)", None, -1))

