from threading import Thread

# Modules required for Model and predictions
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

# Modules required for screen capture
from mss import mss
import cv2 as cv
import numpy as np
from PySide6.QtGui import QPixmap, QImage


class ScreenCaptureService():

    def __init__(self):

        # Set Initial Capturing State
        self.capturing = False

        # Set Location & Size of screen capture then initialise it
        self.mon = {'top': 0, 'left': 0, 'width': 500, 'height': 500}
        self.sct = mss()

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        ultralytics.checks()

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

            # Conduct predictions
            frame = self.predict(frame)

            # Converts the frame into an Image for QT to read using QImage
            # Also ensures the colours are right
            qt_img = QImage(
                frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            return

            # Just a way to break out the loop incase we need to
            if cv.waitKey(1) == ord("q"):
                break
