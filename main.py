from PySide6.QtWidgets import QApplication

from ui.gui_interface import MainWindow
import sys

# UI Functions
from ui_functions import *


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    # Setting up UI Functions
    UIFunctions.uiDefinitions(window)

    window.show()
    app.exec()
