from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.scanner_fine import Ui_scanner_fine_input # ask rameesh
from scanner.fine import sf_Calibration 
from Framework.app_context import AppContext

from XMLTemplates.scanner_input import scanner

class sf_controller(QWidget):
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
        self._ui = Ui_scanner_fine_input() #check ui
        self._ui.setupUi(self)
        self.set_up_connections()
        self._choice_panel = AppContext.get().get_choice_panel_controller()
        self._calibrate = sf_Calibration() 

# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    def set_up_connections(self):
        self._ui.sf_next.clicked.connect(self.calibrate_sf) 
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# calibrate_scanner_coarse
# |----------------------------------------------------------------------------|
    def calibrate_sf(self):
        sf_details = {}
        sf_details["Px"] = scanner.fine_input("Px") #XML
        sf_details["Py"] = scanner.fine_input("Py") #XML
        sf_details["Pz"] = scanner.fine_input("Pz") #XML
        sf_details["Rx"] = scanner.fine_input("Rx") #XML
        sf_details["Ry"] = scanner.fine_input("Ry") #XML
        sf_details["Rz"] = scanner.fine_input("Rz") #XML
        
        
        sf_fiducial = f"{self._ui.sf_px.value()},{self._ui.sf_px.value()},{self._ui.sf_px.value()},{self._ui.sf_rx.value()},{self._ui.sf_ry.value()},{self._ui.sf_rz.value()}"
        

        folder_path = self._choice_panel._ui.TXBX_src_path.text()
        dest_path = self._choice_panel._ui.TXBX_dest_path.text()
        if folder_path and dest_path is not None:
            status, msg = self._calibrate.calculate_sf_values(
                sf_details, folder_path,dest_path, sf_fiducial)
            if status:
                QMessageBox.critical(self, "Alert", msg, QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Alert", f"Oops!, {msg}", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Alert", "please select src and dest folders",
            QMessageBox.Ok)