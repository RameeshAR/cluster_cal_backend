# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui',
# licensing of 'layout.ui' applies.
#
# Created: Tue Jul  6 12:37:22 2021
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_WDG_layout(object):
    def setupUi(self, WDG_layout):
        WDG_layout.setObjectName("WDG_layout")
        WDG_layout.resize(1408, 992)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(WDG_layout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.FRM_calibration = QtWidgets.QFrame(WDG_layout)
        self.FRM_calibration.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRM_calibration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRM_calibration.setObjectName("FRM_calibration")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FRM_calibration)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slideframe = QtWidgets.QFrame(self.FRM_calibration)
        self.slideframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.slideframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.slideframe.setObjectName("slideframe")
        self.GDL_stage_frame = QtWidgets.QGridLayout(self.slideframe)
        self.GDL_stage_frame.setObjectName("GDL_stage_frame")
        self.horizontalLayout.addWidget(self.slideframe)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.upframe = QtWidgets.QFrame(self.FRM_calibration)
        self.upframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.upframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.upframe.setObjectName("upframe")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.upframe)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.scrollArea = QtWidgets.QScrollArea(self.upframe)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 993, 871))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LBL_gif_anime = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LBL_gif_anime.setGeometry(QtCore.QRect(160, 90, 721, 481))
        self.LBL_gif_anime.setText("")
        self.LBL_gif_anime.setObjectName("LBL_gif_anime")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_20.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.upframe)
        self.downframe = QtWidgets.QFrame(self.FRM_calibration)
        self.downframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.downframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.downframe.setObjectName("downframe")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.downframe)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_input_panel = QtWidgets.QFrame(self.downframe)
        self.frame_input_panel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_input_panel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_input_panel.setObjectName("frame_input_panel")
        self.GDL_cam_frame = QtWidgets.QGridLayout(self.frame_input_panel)
        self.GDL_cam_frame.setSpacing(2)
        self.GDL_cam_frame.setContentsMargins(2, 2, 2, 2)
        self.GDL_cam_frame.setObjectName("GDL_cam_frame")
        self.gridLayout_3.addWidget(self.frame_input_panel, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.downframe)
        self.verticalLayout.setStretch(0, 95)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 25)
        self.horizontalLayout.setStretch(1, 75)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.FRM_calibration)

        self.retranslateUi(WDG_layout)
        QtCore.QMetaObject.connectSlotsByName(WDG_layout)

    def retranslateUi(self, WDG_layout):
        WDG_layout.setWindowTitle(QtWidgets.QApplication.translate("WDG_layout", "Calibration", None, -1))

