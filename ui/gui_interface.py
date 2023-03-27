from threading import Thread

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

# API's
from api.henrikdev_api import HenrikApi
from api.henrikdev_api_no_class import *

# Modules required for Model and predictions
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

from ui.ui_functions import UIFunctions


# Setup Main Window
class MainWindow(QMainWindow, Ui_MainWindow, UIFunctions):

    def __init__(self):
        super().__init__()
        ####################################################################################################
        # Init API
        ####################################################################################################

        self.henrik_api = HenrikApi()

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
        # Screen Capture Setup
        ####################################################################################################

        # Set Initial Capturing State
        self.capturing = False

        # Update the Buttons
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)

        # Connect The Buttons to their appropriate functio
        self.startBtn.clicked.connect(self.start_capture_thread)
        self.stopBtn.clicked.connect(self.stop_capture)

        ####################################################################################################
        # Settings Initialise
        ####################################################################################################

        self.get_setting_values()
        # self.account_settings.value("Key")
        # self.setting_variables.value("Key")

    # Begin Capturing Thread
    def start_capture_thread(self):
        self.thread = Thread(target=self.start_capture)

        # Update the Buttons
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
        self.capturing = True
        try:
            self.thread.start()
        except Exception as e:
            print(e)

    # Begin the Capture Process
    def start_capture(self):
        ultralytics.checks()

        # Import Model Used in predicitons
        self.model = YOLO(
            "D:/Programming/Python/trainYolov8/runs/detect/train3/weights/best.pt")

        # Set Location & Size of screen capture then initialise it
        self.mon = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
        self.sct = mss()

        # Begin Capture loop
        while self.capturing:
            # Grabbing the Image
            sct_img = self.sct.grab(self.mon)
            # Get the colours right
            frame = cv.cvtColor(np.array(sct_img), cv.COLOR_BGR2RGB)
            # Ensuring the frame is readable for qtImage and most other things really
            frame = np.array(frame)
            frame = frame[..., :3]
            frame = np.ascontiguousarray(frame)

            # Attempt at using threading to predict
            # self.predict_thread = Thread(
            #     target=self.predict, args=(frame,))
            # self.predict_thread.start()
            # # Wait for Thread to finish and return its value
            # frame = self.predict_thread.
            # print("FRTAME ", frame)
            ######################################################################################

            # Conduct predictions
            frame = self.predict(frame)

            # Converts the frame into an Image for QT to read using QImage
            # Also ensures the colours are right
            qt_img = QImage(
                frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            # shows the frame on the display widget which is a QLabel
            self.screenCaptureLabel.setPixmap(
                QPixmap.fromImage(qt_img).scaledToHeight(480))

            # Just a way to break out the loop incase we need to
            if cv.waitKey(1) == ord("q"):
                break

    # Stop the Capture Process
    def stop_capture(self):
        # Stop Capturing
        self.capturing = False
        # Update Buttons
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)

    # Begin the predict
    def predict(self, frame):
        # Predictions using YOLOv8
        results = self.model.predict(source=frame, conf=0.2)
        # print("RES: ", results)

        # get Boxes and draw them
        for r in results:

            annotator = Annotator(frame)

            boxes = r.boxes
            for box in boxes:

                # getting box coords (top, left, bottom, right) format
                b = box.xyxy[0]
                c = box.cls

                annotator.box_label(b, self.model.names[int(c)])

        frame = annotator.result()
        # print(frame)
        return frame

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
        cv.destroyAllWindows()

        # Stop Capturing
        self.capturing = False

        # Close Application
        event.accept()