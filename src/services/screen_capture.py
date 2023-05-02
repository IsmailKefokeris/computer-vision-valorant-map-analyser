# Initial Modules to setup the Main Window Class
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui

from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, QImage

# Modules required for screen capture
from mss import mss
import cv2 as cv
import numpy as np

# API's
from api.henrikdev_api import HenrikApi

# Modules required for Model and predictions
import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.utils.plotting import Annotator

# Annotator from Supervision
import supervision as sv

from PIL import Image

from services.generate_box import *


# Begin the Capture Process
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
            break


def crop_and_mask(self, frame):
    # Specific To Ascent
    map = cv.imread("ascent.png")
    grey_map = cv.cvtColor(map, cv.COLOR_BGR2GRAY)
    ret, binary_mask = cv.threshold(grey_map, 127, 255, cv.THRESH_BINARY)

    resized_mask = cv.resize(binary_mask, (frame.shape[1], frame.shape[0]))

    frame_masked = cv.bitwise_and(frame, frame, mask=resized_mask)
    return frame_masked


def draw_zones(self, frame):

    # print(f"type: {type(frame)}")

    if self.polygons_updated or len(self.all_polygons) > len(self.polygons):
        self.polygons = []
        for key, polygon in self.all_polygons.items():
            # print(polygon)
            print(f"before: {polygon}")
            poly = np.array(polygon)
            print(f"After: {poly}")

            self.polygons.append(poly)
        print("POLYGONS UPDATED")
        # Set polygons_updated to False after updating
        self.polygons_updated = False

    # Get Image Dimensions
    # (342, 348, 3)
    h, w, _ = frame.shape
    resoultion = (w, h)

    # zone = sv.PolygonZone(polygon=polygon, frame_resolution_wh=resoultion)
    zones = [sv.PolygonZone(
        polygon=polygon, frame_resolution_wh=resoultion) for polygon in self.polygons]

    # initiate annotators
    # zone_annotator = sv.PolygonZoneAnnotator(
    #     zone=zone, color=sv.Color.white(), thickness=2, text_thickness=3, text_scale=2)
    colors = sv.ColorPalette.default()

    zone_annotators = [sv.PolygonZoneAnnotator(zone=zone, color=colors.by_idx(
        index), thickness=2, text_thickness=3, text_scale=1) for index, zone in enumerate(zones)]

    if self.tracker_updated:
        for index, zone in enumerate(zones):
            tracker_generate(self, index)
        print("TRACKER UPDATED")
        self.tracker_updated = False

    box_annotators = [sv.BoxAnnotator(color=colors.by_idx(
        index), thickness=2, text_thickness=2, text_scale=1) for index in range(len(self.polygons))]

    return zones, zone_annotators, self.polygons, box_annotators


def tracker_generate(self, index):
    widget = generate_basic_layout(index)
    self.cards[f"card_{index}"] = widget
    self.gridLayout_7.addWidget(widget, index+1, 0)
    print("generated")


# Begin the predict
def predict(self, frame):
    try:
        zones, zone_annotators, polygons, box_annotators = draw_zones(
            self, frame)
        results = self.model(frame, verbose=False)
        result = results[0]

        # print(type(result))

        detections = sv.Detections.from_yolov8(result)
        # Filter out to only show What the User Selects
        # Had a NP.Bool Error: https://github.com/NVIDIA/TensorRT/issues/2557
        if self.filter:
            detections = detections[eval(self.filter)]
        else:
            detections = detections[(detections.class_id == 0) & (
                detections.confidence > 0.5)]

        labels = [
            f"{self.model.names[int(class_id)]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]

        for index, (zone, zone_annotator, box_annotator) in enumerate(zip(zones, zone_annotators, box_annotators)):
            mask = zone.trigger(detections=detections)
            detections_filtered = detections[mask]

            frame = box_annotator.annotate(
                scene=frame,
                detections=detections_filtered,
                labels=labels)

            frame = zone_annotator.annotate(scene=frame)

            # print(detections_filtered.class_id)

            for detection in detections_filtered:
                # print(detection[2])
                class_id = int(detection[2])
                class_name = self.model.names[class_id]

                # Increment the count for the detected class
                self.class_counts[class_name] += 1

            # type = self.model.names[int(detections_filtered.class_id)]

            # Print the counts for each class
            # print("Class counts:")
            # labels = self.findChildren(QLabel, f"desc")
            text = []

            for class_name, count in self.class_counts.items():
                text.append(f"{count} {class_name}s")
                # print(f"Zone {index}: {count} detections of class {class_name}")
            # print(text)
            cardLabel = self.cards[f"card_{index}"].findChild(
                QLabel, f"desc_{index}")
            cardLabel.setText(" ".join(text))

        return frame
    except Exception as e:
        print(e)
        self.stop_capture()

    # # Begin the predict
    # def predict(self, frame):
    #     # Predictions using YOLOv8

    #     results = self.model.predict(source=frame, conf=0.8)
    #     # print("RES: ", results)

    #     # get Boxes and draw them
    #     for r in results:

    #         annotator = Annotator(frame)

    #         boxes = r.boxes
    #         for box in boxes:

    #             # getting box coords (top, left, bottom, right) format
    #             b = box.xyxy[0]
    #             c = box.cls

    #             annotator.box_label(b, self.model.names[int(c)])

    #     frame = annotator.result()
    #     # print(frame)
    #     return frame
