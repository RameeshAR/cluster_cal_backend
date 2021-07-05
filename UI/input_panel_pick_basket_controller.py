from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.input_panel_pick_basket import Ui_WDG_input_panel_pick_basket
from PickBasketCal.pick_basket_cal import PickBasketCal
from Framework.app_context import AppContext

# ==============================================================================
# PickBasketPanelController
# ==============================================================================


class PickBasketPanelController(QWidget):
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
        self._ui = Ui_WDG_input_panel_pick_basket()
        self._ui.setupUi(self)
        self.set_up_connections()
        self._choice_panel = AppContext.get().get_choice_panel_controller()
        self._calibrate = PickBasketCal()

# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    def set_up_connections(self):
        self._ui.PB_calibrate.clicked.connect(self.calibrate_pick_basket)
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# calibrate_pick_basket
# |----------------------------------------------------------------------------|
    def calibrate_pick_basket(self):
        robot_movement_params = {}
        robot_movement_params["rx"] = self._choice_panel._ui.DSB_Rx.value()
        robot_movement_params["ry"] = self._choice_panel._ui.DSB_Ry.value()
        robot_movement_params["rz"] = self._choice_panel._ui.DSB_Rz.value()
        robot_movement_params["velocity"] = self._choice_panel._ui.DSB_velocity.value()
        robot_movement_params["time_out"] = self._choice_panel._ui.DSB_time_out.value()
        robot_movement_params["movement_type"] = self._choice_panel._ui.CBX_move_type.currentText
        robot_movement_params["force"] = self._choice_panel._ui.DSB_force.value()
        robot_movement_params["gripper_width"] = 7 #XML
        robot_movement_params["gripper_jaw_thickness"] = 1.5 #XML
        robot_movement_params["z_pick_speed"] = 0.5 #XML
        robot_movement_params["z_place_speed"] = 0.5 #XML
        robot_movement_params["z_offset_distance"] = 103 #XML
        robot_movement_params["z_place_pos"] = 0 #XML
        robot_movement_params["row_direction"] = 1 #XML
        robot_movement_params["column_direction"]= 0 #XML

        basket_dimensions = {}
        basket_dimensions["max_row_count"] = 3
        basket_dimensions["max_column_count"] = 29
        basket_dimensions["row_distance"] = 30
        basket_dimensions["column_distance"] = 7
        basket_dimensions["length"] = 222
        basket_dimensions["width"] = 124
        basket_dimensions["height"] = 72.64
        
        basket_num = self._choice_panel._ui.CBX_select_station.currentIndex()+1
        folder_path = self._choice_panel._ui.TXBX_src_path.text()
        dest_path = self._choice_panel._ui.TXBX_dest_path.text()
        print("-----------", len(folder_path))
        fiducial_1 = f"{self._ui.DSB_px_1.value()},{self._ui.DSB_py_1.value()},{self._ui.DSB_pz_1.value()}"
        fiducial_2 = f"{self._ui.DSB_px_2.value()},{self._ui.DSB_py_2.value()},{self._ui.DSB_pz_2.value()}"
        fiducial_3 = f"{self._ui.DSB_px_3.value()},{self._ui.DSB_py_3.value()},{self._ui.DSB_pz_3.value()}"
        fiducial_4 = f"{self._ui.DSB_px_4.value()},{self._ui.DSB_py_4.value()},{self._ui.DSB_pz_4.value()}"
        print(fiducial_1, fiducial_2, fiducial_3, fiducial_4)
        if len(folder_path) != 0 and len(dest_path) != 0:
            status, msg = \
                self._calibrate.calc_cal_outcomes(basket_num, folder_path,
                robot_movement_params, dest_path, basket_dimensions, fiducial_1,
                fiducial_2, fiducial_3, fiducial_4)
            print("=========")
            if status:
                QMessageBox.critical(msg, QMessageBox.Ok)
            else:
                QMessageBox.critical(f"Oops!, {msg}", QMessageBox.Ok)
        else:
            QMessageBox.critical("please select src and dest path",
                                        QMessageBox.Ok)
# -------------End of calibrate_pick_basket----------------------------|