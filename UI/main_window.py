import sys
from PySide2.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout,\
    QMessageBox

from UI.layout_controller import LayoutController
from Framework.app_context import AppContext

# ==============================================================================
# MainWindow
# ==============================================================================


class MainWindow(QMainWindow):
    '''
    MainWindow is the parent window of all the Widgets and connects the
    widgets
    '''
# |----------------------------------------------------------------------------|
# Class Variables
# |----------------------------------------------------------------------------|
#        no class variables

# |----------------------------------------------------------------------------|
# Constructor
# |----------------------------------------------------------------------------|
    def __init__(self):
        super().__init__()

        self.setup_ui()

# |---------------------------End of Constructor------------------------------|

# |----------------------------------------------------------------------------|
# setup_ui
# |----------------------------------------------------------------------------|
    def setup_ui(self):
        # Create Main Window.
        self.WND_main = QMainWindow()

        # Add Vertical Layout to Main window.
        self.VBL_main = QVBoxLayout(self.WND_main)

        # Create Tab Widget.
        self.TWG_tab = QTabWidget(self.WND_main)

        # Add Calibration Tab.
        calibration_controller_obj = LayoutController()
        self.TWG_tab.addTab(calibration_controller_obj, "RoboCal")

        # Set First tab as Current page.
        self.TWG_tab.setCurrentIndex(0)

        # Add Tab Widget to Vertical layout of MainWindow.
        self.VBL_main.addWidget(self.TWG_tab)

        # Set Tab Widget as Central Widget.
        self.setCentralWidget(self.TWG_tab)

# |----------------------End of setup_ui--------------------------------------|

# |----------------------------------------------------------------------------|
# closeEvent
# |----------------------------------------------------------------------------|
    def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Window Close',
                    'Are you sure you want to close the window?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
                print('Window closed')
            else:
                event.ignore()

# |----------------------End of closeEvent------------------------------------|
