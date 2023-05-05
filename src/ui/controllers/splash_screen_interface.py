# Initial Modules to setup the Main Window Class
import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QColor
from PySide6.QtCore import *
from PySide6.QtWidgets import *


# Import View
from ui.views.splash_screen_ui import *
from ui.controllers.gui_interface import *


class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)

        # Remove Title Bar
        self.setWindowFlag(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()

    window.show()

    sys.exit(app.exec_())
