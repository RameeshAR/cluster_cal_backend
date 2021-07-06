from PySide2.QtCore import Slot, QTimer, QDateTime
from PySide2.QtWidgets import QWidget, QMessageBox, QFileDialog

from UI.input_panel_pick_basket import Ui_WDG_input_panel_pick_basket
from PickBasketCal.pick_basket_cal import PickBasketCal
from Framework.app_context import AppContext

from XMLTemplates.pick_basket import pick
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
        robot_movement_params["gripper_width"] = pick.arm("gripper_width") #XML
        robot_movement_params["gripper_jaw_thickness"] = pick.arm("gripper_jaw_thickness") #XML
        robot_movement_params["z_pick_speed"] = pick.arm("z_pick_speed") #XML
        robot_movement_params["z_place_speed"] = pick.arm("z_place_speed") #XML
        robot_movement_params["z_offset_distance"] = pick.arm("z_offset_distance") #XML
        robot_movement_params["z_place_pos"] = pick.arm("z_place_pos") #XML
        robot_movement_params["row_direction"] = pick.arm("row_direction") #XML
        robot_movement_params["column_direction"]= pick.arm("column_direction") #XML

        basket_dimensions = {}
        basket_dimensions["max_row_count"] = pick.basket_dims("max_row_count")
        basket_dimensions["max_column_count"] = pick.basket_dims("max_column_count")
        basket_dimensions["row_distance"] = pick.basket_dims("row_distance")
        basket_dimensions["column_distance"] = pick.basket_dims("column_distance")
        basket_dimensions["length"] = pick.basket_dims("length")
        basket_dimensions["width"] = pick.basket_dims("width")
        basket_dimensions["height"] = pick.basket_dims("height")
        
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
