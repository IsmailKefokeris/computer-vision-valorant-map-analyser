from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect

# Import GUI File
from common.gui_interface import *


class UIFunctions(MainWindow):
    # https://github.com/Wanderson-Magalhaes/Python_PySide2_Custom_Title_Bar/blob/master/ui_functions.py

    # Determines What the buttons on the top bar do and how the window works
    def uiDefinitions(self):
        ####################################################################################################
        # Title Bar Buttons
        ####################################################################################################

        # Remove Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Minimise
        self.minBtn.clicked.connect(lambda: self.showMinimized())

        # Close
        self.closeBtn.clicked.connect(lambda: self.close())

        # Toggle Menu Extend Button
        self.toggleMenuBtn.clicked.connect(lambda: self.toggleMenu(True))

        ####################################################################################################
        # Page Buttons
        ####################################################################################################

        # Home Page
        self.mainPageBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.mainPage))

        # Pre-Requisites Page
        self.prerequisitesBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.preRequisitesPage))

        # Settings Page
        self.accountSettingsBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.accountSettingsPage))

        # Bug Submission Page
        self.bugBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.submitBugPage))

        ####################################################################################################
        # Settings Page Buttons
        ####################################################################################################

        # Generate PPUID
        self.ppuidBtn.clicked.connect(lambda: self.get_user_details())
