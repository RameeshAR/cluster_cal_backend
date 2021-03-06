from PySide2.QtCore import Slot
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QMovie

from UI.choice_panel_controller import ChoicePanelController
from UI.layout import Ui_WDG_layout
from UI.cal_flow_controller import CalFlowController
from UI.input_panel_pick_basket_controller import PickBasketPanelController 
from UI.input_panel_drop_basket_controller import DropBasketPanelController
from Framework.app_context import AppContext

# ==============================================================================
# LayoutController
# ==============================================================================
class LayoutController(QWidget):
    '''
    CalibrationController is the controller which talks to the UI Components of
    Calibration Utility
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
        self._ui = Ui_WDG_layout()
        self._ui.setupUi(self)
        self.set_up_ui()
        self._cal_type = self.choice_panel._ui.CBX_select_cal_type.currentText().lower()
        self.set_up_connections()

# |----------------------------------------------------------------------------|
# set_up_ui
# |----------------------------------------------------------------------------|
    def set_up_ui(self):
        self.movie = QMovie("/home/adminspin/office/cluster_cal_backend/UI/"+
        "Gifs/UR3_Wave.gif")
        self._ui.LBL_gif_anime.setMovie(self.movie)
        print(self.movie.start())
        # self.resize()

        self.choice_panel = ChoicePanelController()
        self._ui.GDL_stage_frame.addWidget(self.choice_panel)
        AppContext.get().set_choice_panel_controller(self.choice_panel)

        # self.cal_flow = CalFlowController()
        # self._ui.GDL_cam_frame_2.addWidget(self.cal_flow)
        # AppContext.get().set_cal_flow_controller(self.cal_flow)
        
        self.drop_basket_input_panel = DropBasketPanelController()
        self._ui.GDL_cam_frame.addWidget(self.drop_basket_input_panel)
        AppContext.get().set_drop_basket_panel_controller(self.drop_basket_input_panel)
        self.drop_basket_input_panel.hide()
        
        self.pick_basket_input_panel = PickBasketPanelController()
        self._ui.GDL_cam_frame.addWidget(self.pick_basket_input_panel)
        AppContext.get().set_pick_basket_panel_controller(self.pick_basket_input_panel)

# |----------------------End of set_up_ui----------------------------|

# |----------------------------------------------------------------------------|
# set_up_connections
# |----------------------------------------------------------------------------|
    def set_up_connections(self):
        self.choice_panel._ui.CBX_select_cal_type.currentTextChanged.connect(
            self._onCalTypeChange)
# |----------------------End of set_up_connections----------------------------|

# |----------------------------------------------------------------------------|
# _onCalTypeChange
# |----------------------------------------------------------------------------|
    def _onCalTypeChange(self):
        if "pick" in self._cal_type:
            print("pick removed")
            self.pick_basket_input_panel.hide()
        if "drop" in self._cal_type:
            self.drop_basket_input_panel.hide()
        self._cal_type = self.choice_panel._ui.CBX_select_cal_type.currentText().lower()
        print("cal_type", self._cal_type)
        if "pick" in self._cal_type:
            self.pick_basket_input_panel.show()
            self.movie = QMovie(
                "/home/adminspin/office/cluster_cal_backend/UI/Gifs/UR3_Wave.gif")
            self._ui.LBL_gif_anime.setMovie(self.movie)
            self.movie.start()
        if "drop" in self._cal_type:
            print("add drop")
            self.drop_basket_input_panel.show()
            self.movie = QMovie(
                "/home/adminspin/office/cluster_cal_backend/UI/Gifs/coming_soon.gif")
            self._ui.LBL_gif_anime.setMovie(self.movie)
            self.movie.start()
# |----------------------End of set_up_connections----------------------------|