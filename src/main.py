from PySide6.QtWidgets import QApplication

from ui.controllers.gui_interface import MainWindow
import sys
import os

# UI Functions
from ui.controllers.ui_functions import *
from ui.controllers.splash_screen_interface import *


if __name__ == "__main__":
    try:
        from ctypes import windll
        myappid = 'IsmailKefokeris.CVVMA.030'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    app = QApplication(sys.argv)

    # splash = SplashScreen()
    # splash.show()

    # Splash Screen Image
    pixmap = QPixmap(r"src\assets\images\banner.webp")
    splash = QSplashScreen(pixmap)
    splash.show()

    splash.showMessage("Loading Main Window...", color="white")
    app.processEvents()

    window = MainWindow()

    window.show()

    splash.finish(window)

    app.exec()
