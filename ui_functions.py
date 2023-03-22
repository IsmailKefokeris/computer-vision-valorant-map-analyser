from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect

# Import GUI File
from common.gui_interface import *


class UIFunctions(MainWindow):
    # https://github.com/Wanderson-Magalhaes/Python_PySide2_Custom_Title_Bar/blob/master/ui_functions.py

    # Determines What the buttons on the top bar do and how the window works
    def uiDefinitions(self):

        # Remove Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Minimise
        self.minBtn.clicked.connect(lambda: self.showMinimized())

        # Close
        self.closeBtn.clicked.connect(lambda: self.close())

        # Bug Button Function
        # self.bugBtnFrame

        # Toggle Menu Extend Button
        self.toggleMenuBtn.clicked.connect(lambda: self.toggleMenu(True))
