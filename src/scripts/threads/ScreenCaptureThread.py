from typing import Optional
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThread

from services.screen_capture import *


class ScreenCaptureThread(QThread):
    def __init__(self, parent: QMainWindow | None = ...) -> None:
        super().__init__(parent)
        self.parent = parent

    def run(self):
        # Update the Buttons
        self.parent.startBtn.setEnabled(False)
        self.parent.stopBtn.setEnabled(True)
        self.parent.capturing = True
        try:
            self.parent.polygonLabel.setText(
                "Starting Screen Capture, Please Wait...")
            start_capture(self.parent)
        except Exception as e:
            print(e)

    def stop(self):
        # Stop Capturing
        self.parent.capturing = False
        # Update Buttons
        self.parent.startBtn.setEnabled(True)
        self.parent.stopBtn.setEnabled(False)
        self.terminate()
