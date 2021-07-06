from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.input_panel_drop_basket import Ui_WDG_input_panel_drop_basket
from DropBasketCal.drop_basket_cal import DropBasketCalibration
from Framework.app_context import AppContext

# ==============================================================================
# DropBasketPanelController
# ==============================================================================


class DropBasketPanelController(QWidget):
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
        self._ui = Ui_WDG_input_panel_drop_basket()
        self._ui.setupUi(self)
        self.set_up_connections()
        self._choice_panel = AppContext.get().get_choice_panel_controller()
        self._calibrate = DropBasketCalibration()

# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    def set_up_connections(self):
        self._ui.PB_calibrate.clicked.connect(self.calibrate_drop_basket)
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# calibrate_drop_basket
# |----------------------------------------------------------------------------|
    def calibrate_drop_basket(self):
        drop_basket_details = {}
        drop_basket_details["basket_width"] = 48 #XML
        drop_basket_details["basket_depth"] = 83.5 #XML
        drop_basket_details["z_offset"] = 10 #XML
        drop_basket_details["basket_height"] = 225 #XML
        drop_basket_details["basket_gap"] = 14 #XML
        drop_basket_details["wall_thickness"] = 4 #XML
        gripper_width = 7 #XML
        gripper_jaw_thickness = 1.5 #XML
        std_slide_height = 75 #XML
        
        fiducial_1 = f"{self._ui.DSB_px_1.value()},{self._ui.DSB_py_1.value()},{self._ui.DSB_pz_1.value()}"
        fiducial_2 = f"{self._ui.DSB_px_2.value()},{self._ui.DSB_py_2.value()},{self._ui.DSB_pz_2.value()}"

        folder_path = self._choice_panel._ui.TXBX_src_path.text()
        dest_path = self._choice_panel._ui.TXBX_dest_path.text()
        if folder_path and dest_path is not None:
            status, msg = self._calibrate.calculate_cal_values(
                drop_basket_details, folder_path,
                gripper_width, gripper_jaw_thickness,
                std_slide_height, dest_path, fiducial_1, fiducial_2)
            if status:
                QMessageBox.critical(self, "Alert", msg, QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Alert", f"Oops!, {msg}", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Alert",
              "Invalid Path", QMessageBox.Ok)