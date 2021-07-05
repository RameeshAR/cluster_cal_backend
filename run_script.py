#!/usr/bin/python3

import os
import sys

from os.path import join, exists

from PySide2.QtWidgets import QApplication

from UI.main_window import MainWindow

from Framework.app_context import AppContext



if __name__ == '__main__':
    exit_status = -1

    app = QApplication(sys.argv)


    # Initialize Components.
    # Create instance for Main Widget.
    main_window_obj = MainWindow()

    # Show the widget.
    main_window_obj.showMaximized()

    # Close the application.
    sys.exit(app.exec_())
