from PySide6.QtWidgets import QApplication

from ui.controllers.gui_interface import MainWindow
import sys
import os

# UI Functions
from ui.controllers.ui_functions import *


if __name__ == "__main__":
    try:
        from ctypes import windll
        myappid = 'IsmailKefokeris.CVVMA.030'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    app = QApplication(sys.argv)

    window = MainWindow()

    # # Setting up UI Functions
    # UIFunctions.uiDefinitions(window)

    window.show()
    app.exec()
