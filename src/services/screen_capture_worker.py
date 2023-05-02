from PySide6.QtCore import QObject, QThread, Signal, QObject, Slot

from services.screen_capture import *


class CaptureWorker(QObject):

    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self = main_window

    @Slot()
    def start_capture(self):
        ultralytics.checks()

        self.lastIndex = 0

        # initiate polygons list
        self.polygons = []

        # Import Model Major Classes Used in predicitons
        self.model = YOLO(
            r"src\models\firstLevel\train4\best.pt")

        self.CLASS_NAMES_DICT = self.model.model.names

        # Set Location & Size of screen capture then initialise it
        # self.mon = {'top': 0, 'left': 0, 'width': 500, 'height': 500}

        # self.mon = {'top': 55, 'left': 33, 'width': 348, 'height': 342} Ascent Map Capture

        self.mon = {'top': self.screenTop, 'left': self.screenLeft,
                    'width': self.screenWidth, 'height': self.screenHeight}
        self.sct = mss()

        self.set_screen_capture_dimensions_label()

        # Annotator settings
        self.box_annotator = sv.BoxAnnotator(
            thickness=2, text_thickness=2, text_scale=1)

        # Begin Capture loop
        while self.capturing:
            # Updating Screen Capture Area if needed
            self.mon = {'top': self.screenTop, 'left': self.screenLeft,
                        'width': self.screenWidth, 'height': self.screenHeight}

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
            self.class_counts = {
                self.model.names[class_id]: 0 for class_id in self.model.names}
            frame = predict(self, frame)

            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(
                frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888))

            # Scales the frame to fit the QLabel
            scaled_pixmap = pixmap.scaled(
                self.screenCaptureLabel.size(), qtc.Qt.IgnoreAspectRatio, qtc.Qt.SmoothTransformation)

            # shows the frame on the display widget which is a QLabel
            self.screenCaptureLabel.setPixmap(scaled_pixmap)

            # Just a way to break out the loop incase we need to
            if cv.waitKey(1) == ord("q"):
                print('Stopping the worker object')
                self._worker.stop()
                break
