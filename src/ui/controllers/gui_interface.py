# from threading import Thread

# Initial Modules to setup the Main Window Class
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui

from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from ui.views.DesignThree_ui import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QImage

# Modules required for screen capture
import numpy as np

# API's
from api.henrikdev_api import HenrikApi

# Annotator from Supervision
import supervision as sv

from ui.controllers.ui_functions import UIFunctions

# Hotkeys
import keyboard

from services.screen_capture import *
from services.generate_box import *
from services.screen_capture_worker import *
from services.module_loader import *
# import cv2 as cv
# Setup Main Window


class MainWindow(QMainWindow, Ui_MainWindow, UIFunctions):

    def __init__(self):
        super().__init__()

        ###################################################################################################
        # Init API
        ##################################################################################################

        self.henrik_api = HenrikApi()
        self.polygons_updated = True
        self.tracker_updated = True

        ####################################################################################################
        # Window Setup
        ####################################################################################################

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)

        # Define Behaviour of application
        self.uiDefinitions()

        # Set Window Title
        self.setWindowTitle("Valorant Map Analyser")

        # Set moving window functions for topBar
        self.topBar.mouseMoveEvent = self.moveWindow

        ####################################################################################################
        # Settings Initialise
        ####################################################################################################

        self.get_setting_values()

        ####################################################################################################
        # Card Generation
        ####################################################################################################

        self.cards = {}

        ####################################################################################################
        # Application Hotkeys
        ####################################################################################################
        self.hotkey = 'ctrl+alt+o'
        keyboard.add_hotkey(self.hotkey, self.toggle_visibility)

        # Enable mouse tracking to receive mouse move events even when no button is pressed
        self.setMouseTracking(True)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

    # Begin Capturing Thread
    def start_capture_thread(self):
        # self.thread = Thread(target=self.start_capture)

        # Update the Buttons
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
        self.capturing = True
        try:
            start_capture(self)
        except Exception as e:
            print(e)

    # Stop the Capture Process
    def stop_capture(self):
        # Stop Capturing
        self.capturing = False
        # Update Buttons
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)

    def get_setting_values(self):
        self.account_settings = qtc.QSettings("CV-VMA", "Account Information")
        self.setting_variables = qtc.QSettings("CV-VMA", "Varaibles")
        if len(self.account_settings.childKeys()) > 0:
            self.populate_accounts_settings()
        else:
            print("EMPTY Settings")

    def populate_accounts_settings(self):
        self.usernameInput.setText(self.account_settings.value("username"))
        self.username.setText(self.account_settings.value("full_username"))

        self.tagInput.setText(self.account_settings.value("tagline"))
        self.puuidInput.setText(self.account_settings.value("puuid"))

        self.regionInput.setText(self.account_settings.value("region"))
        self.shardInput.setText(self.account_settings.value("shard"))
        self.versionInput.setText(self.account_settings.value("version"))

        self.elo.setText(str(self.account_settings.value("elo")))
        self.rank.setText(str(self.account_settings.value("current_rank")))

        self.set_user_image(
            self.account_settings.value("username"),
            self.account_settings.value("tagline"))

    # Function to toggle side bar to expand or contract
    def toggleMenu(self, enable):
        if enable:

            # Get Width
            width = self.menuBar.width()
            maxExtend = 200
            standard = 0

            # Set Max Width
            if width == 0:
                widthExtend = maxExtend
            else:
                widthExtend = standard

            # Animation
            self.animation = QPropertyAnimation(self.menuBar, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.start()

    # Detect mouse Presses
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Window Drag Function
    def moveWindow(self, event):
        # https://learndataanalysis.org/source-code-how-to-move-a-frameless-window-with-a-mouse-pyqt5/

        # Check if Left Click
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.dragPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.dragPos = event.globalPos()
            event.accept()

    # Explicitly defining close event to ensure
    # nothing is running in the background after the application is shut down
    def closeEvent(self, event):
        _, cv, _, _, _ = load_modules([False, True, False, False, False])
        cv.destroyAllWindows()

        # Stop Capturing
        self.capturing = False

        # Close Application
        event.accept()
