# Initial Modules to setup the Main Window Class
from PySide6 import QtCore
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
        # Setup Page Buttons
        ####################################################################################################

        # Home Page
        self.mainPageBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.mainPage))

        # Pre-Requisites Page
        self.prerequisitesBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.preRequisitesPage))

        # Settings Page
        self.settingsBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.settingsPage))

        # Bug Submission Page
        self.bugBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.submitBugPage))

    def start_capture(self):
        pass

    def stop_capture(self):
        pass

    def predict(self, frame):
        pass

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

    # Explicitly defining close event to ensure
    # nothing is running in the background after the application is shut down
    def closeEvent(self, event):
        # cv.destroyAllWindows()

        # Stop Capturing
        self.capturing = False

        # Close Application
        event.accept()

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
