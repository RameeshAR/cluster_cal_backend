from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.choice_panel import Ui_WDG_choice_panel


# ==============================================================================
# ChoicePanelController
# ==============================================================================


class ChoicePanelController(QWidget):
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
        self._ui = Ui_WDG_choice_panel()
        self._ui.setupUi(self)
        self.set_up_connections()

# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    def set_up_connections(self):
        self._ui.PB_src_path.clicked.connect(self.get_src_folder_path)
        self._ui.PB_dest_path.clicked.connect(self.get_dest_folder_path)
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# get_src_folder_path
# |----------------------------------------------------------------------------|
    def get_src_folder_path(self):
        directory = QFileDialog.getExistingDirectory(self,
                                     "Select Folder",
                                     "./")
        self._ui.TXBX_src_path.setText(directory)
# |----------------------End of get_src_folder_path----------------------------|

# |----------------------------------------------------------------------------|
# get_dest_folder_path
# |----------------------------------------------------------------------------|
    def get_dest_folder_path(self):
        directory = QFileDialog.getExistingDirectory(self,
                                     "Select Folder",
                                     "./")
        self._ui.TXBX_dest_path.setText(directory)
# |----------------------End of get_dest_folder_path----------------------------|