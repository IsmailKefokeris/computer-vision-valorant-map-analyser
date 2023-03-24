# Initial Modules to setup the Main Window Class
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from assets.ui_DesignThree import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QImage

# Modules required for screen capture
from mss import mss
import cv2 as cv
import numpy as np

# Modules required for Model and predictions
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

# ultralytics.checks()


# Setup Main Window
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        # Set Initial Capturing State
        self.capturing = False

        ####################################################################################################
        # Window Setup
        ####################################################################################################

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)
        # Set Window Title
        self.setWindowTitle("Valorant Map Analyser")

        # Set moving window functions for topBar
        self.topBar.mouseMoveEvent = self.moveWindow

        ####################################################################################################
        # Settings Initialise
        ####################################################################################################

        self.get_setting_values()
        # self.account_settings.value("Key")
        # self.setting_variables.value("Key")

    def start_capture(self):
        pass

    def stop_capture(self):
        pass

    def predict(self, frame):
        pass

    def save_account_settings(self):
        username = self.get_username()
        tagline = self.get_tagline()
        if(username and tagline):
            # Save new settings to registry
            self.set_setting_values()
            # Update Settings Page
            self.populate_accounts_settings()
            # Update Error Message
            self.saveError.setText("")

        self.saveError.setText("Unable To Save Double Check Values!!")
        return False

    # Get Username From Input Function
    def get_username(self):
        username = self.usernameInput.text()
        if username:
            self.usernameError.setText("")
            return username
        self.usernameError.setText("Username Must be filled in")
        return False

    # Get TagLine From Input Function
    def get_tagline(self):
        tagline = self.tagInput.text()
        if tagline:
            if tagline.startswith("#", 0):
                if len(tagline) <= 5:
                    self.tagError.setText("")
                    return tagline
                self.tagError.setText(
                    "Must be 5 characters \n long (Including #)")
                return False
            self.tagError.setText("Must Include `#` At the Start")
            return False
        self.tagError.setText("TagLine Must be filled in")
        return False

    # Get PPUID From Input Function
    def get_ppuid(self):
        # Generate Fake PPUID
        self.ppuidInput.setText("0920499468938490584634623853")
        ppuid = self.ppuidInput.text()
        if ppuid:
            self.ppuidError.setText("")
            return ppuid
        self.ppuidError.setText(
            "Unable to Generate PPUID \n Double check Tagline and Username")
        return False

    def get_setting_values(self):
        self.account_settings = qtc.QSettings("CV-VMA", "Account Information")
        self.setting_variables = qtc.QSettings("CV-VMA", "Varaibles")
        if len(self.account_settings.childKeys()) > 0:
            self.populate_accounts_settings()
        else:
            print("EMPTY")

    def populate_accounts_settings(self):
        self.usernameInput.setText(self.account_settings.value("username"))
        self.username.setText(self.account_settings.value("full_username"))

        self.tagInput.setText(self.account_settings.value("tagline"))
        self.ppuidInput.setText(self.account_settings.value("ppuid"))

        self.regionInput.setText(self.account_settings.value("region"))
        self.shardInput.setText(self.account_settings.value("shard"))
        self.versionInput.setText(self.account_settings.value("version"))

    def set_setting_values(self):
        # Retrieve User Information from Input Fields
        username = self.get_username()
        tagline = self.get_tagline()
        ppuid = self.get_ppuid()
        full_username = f"{username}{tagline}"
        region = "eu"
        shard = "eu"
        version = "v1"

        # Save all information to the settings in registry
        self.account_settings.setValue("username", username)
        self.account_settings.setValue("tagline", tagline)
        self.account_settings.setValue("ppuid", ppuid)
        self.account_settings.setValue("full_username", full_username)

        self.account_settings.setValue("region", region)
        self.account_settings.setValue("shard", shard)
        self.account_settings.setValue("version", version)

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

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

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
        # cv.destroyAllWindows()

        # Stop Capturing
        self.capturing = False

        # Close Application
        event.accept()
