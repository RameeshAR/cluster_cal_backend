from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.input_panel_drop_basket import Ui_WDG_input_panel_drop_basket
from DropBasketCal.drop_basket_cal import DropBasketCalibration
from Framework.app_context import AppContext

from XMLTemplates.drop_basket import drop
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
        drop_basket_details["basket_width"] = drop.basket_dims("width") #XML
        drop_basket_details["basket_depth"] = drop.basket_dims("depth") #XML
        drop_basket_details["z_offset"] = drop.arm("z_offset") #XML
        drop_basket_details["basket_height"] = drop.basket_dims("height") #XML
        drop_basket_details["basket_gap"] = drop.basket_dims("basket_gap") #XML
        drop_basket_details["wall_thickness"] = drop.basket_dims("wall_thickness") #XML
        gripper_width = drop.arm("gripper_width") #XML
        gripper_jaw_thickness = drop.arm("gripper_jaw_thickness") #XML
        std_slide_height = drop.arm("std_slide_height") #XML
        
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
            QMessageBox.critical(self, "Alert", "please select src and dest folders",
            QMessageBox.Ok)
