from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.cal_flow import Ui_WDG_cal_flow

# ==============================================================================
# CalFlowController
# ==============================================================================


class CalFlowController(QWidget):
    '''
    Handles the operations of choice panel part.
    '''
# |----------------------------------------------------------------------------|
# Class Variables
# |----------------------------------------------------------------------------|
#        no class variables

# |----------------------------------------------------------------------------|
# Constructor
# |----------------------------------------------------------------------------|
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._ui = Ui_WDG_cal_flow()
        self._ui.setupUi(self)
