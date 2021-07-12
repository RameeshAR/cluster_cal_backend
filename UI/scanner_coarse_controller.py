from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide2.QtGui import QMovie

from UI.scanner_coarse import Ui_coarse_input # ask rameesh
from scanner.coarse import sc_Calibration 
from Framework.app_context import AppContext
from XMLTemplates.scanner_input import scanner
from UI.scanner_coarse import Ui_coarse_input

class sc_controller(QWidget):
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
        self._ui = Ui_coarse_input() #check Ui
        self._ui.setupUi(self)
        self.set_up_connections()
        self._choice_panel = AppContext.get().get_choice_panel_controller()
        self._calibrate = sc_Calibration()
        self.count = 0
        self.flag = 0

        self._layout_controller = AppContext.get().get_layout_controller()
        #self._layout_controller._ui.GDL_cam_frame.addWidget(self._layout_controller)
        #AppContext.get().get_layout_controller()
# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    
    def set_up_connections(self):
        self._ui.sc_next.clicked.connect(self.calibrate_sc)
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# calibrate_scanner_coarse
# |----------------------------------------------------------------------------|

    def calibrate_sc(self):
        if self.count == 0:
            sc_details = {}
            sc_details["Px"] = scanner.coarse_input("Px") #XML
            sc_details["Py"] = scanner.coarse_input("Py") #XML
            sc_details["Pz"] = scanner.coarse_input("Pz") #XML
            sc_details["Rx"] = scanner.coarse_input("Rx") #XML
            sc_details["Ry"] = scanner.coarse_input("Ry") #XML
            sc_details["Rz"] = scanner.coarse_input("Rz") #XML
            
            
            sc_fiducial = f"{self._ui.sc_px.value()},{self._ui.sc_px.value()},{self._ui.sc_px.value()},{self._ui.sc_rx.value()},{self._ui.sc_ry.value()},{self._ui.sc_rz.value()}"
            

            folder_path = self._choice_panel._ui.TXBX_src_path.text()
            dest_path = self._choice_panel._ui.TXBX_dest_path.text()
            if folder_path and dest_path is not None:
                status, msg = self._calibrate.calculate_sc_values(
                    sc_details, folder_path,dest_path, sc_fiducial)
                if status:
                    QMessageBox.critical(self, "Alert", msg, QMessageBox.Ok)
                    self.count += 1
                else:
                    QMessageBox.critical(self, "Alert", f"Oops!, {msg}", QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Alert", "please select src and dest folders",
                QMessageBox.Ok)

