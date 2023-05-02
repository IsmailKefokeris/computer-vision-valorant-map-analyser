from PySide6.QtCore import *
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QGraphicsDropShadowEffect

# Importing Service to send email
from services.emailing_service import *
from services.email_verification_service import *

# .env
import os
from dotenv import load_dotenv

# Import services Mouse Tracker
from services.MouseTracker import MouseTracker
from services.screen_capture import *

# Import Paintable Label
from ui.widgets.PaintableLabel import PaintableLabel


# Import GUI File
from ui.controllers.gui_interface import *

import requests


class UIFunctions:
    # https://github.com/Wanderson-Magalhaes/Python_PySide2_Custom_Title_Bar/blob/master/ui_functions.py

    # Determines What the buttons on the top bar do and how the window works
    def uiDefinitions(self):
        load_dotenv()

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

        # Generate PUUID
        self.saveSettingsBtn.clicked.connect(
            lambda: self.save_account_settings())

        ####################################################################################################
        # Screen Capture Setup
        ####################################################################################################

        # Screen Capture Variables

        # self.mon = {'top': 55, 'left': 33, 'width': 348, 'height': 342} Ascent Map Capture

        # self.screenTop = 55
        # self.screenLeft = 33
        # self.screenWidth = 348
        # self.screenHeight = 342

        self.screenTop = 55
        self.screenLeft = 33
        self.screenWidth = 596
        self.screenHeight = 505

        # Set Initial Capturing State
        self.capturing = False

        # Update the Buttons
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)

        # Connect The Buttons to their appropriate functio
        self.startBtn.clicked.connect(self.start_capture_thread)
        self.stopBtn.clicked.connect(self.stop_capture)

        self.screenCaptureControls.buttonClicked.connect(
            self.screen_capture_adjustments)

        # Connecting Line Edits to update Screen Capture Values

        self.topValueLabel.returnPressed.connect(
            lambda name=self.topValueLabel: self.screen_capture_adjustments_line_edit(name))

        self.leftValueLabel.returnPressed.connect(
            lambda name=self.leftValueLabel: self.screen_capture_adjustments_line_edit(name))

        self.widthValueLabel.returnPressed.connect(
            lambda name=self.widthValueLabel: self.screen_capture_adjustments_line_edit(name))

        self.heightValueLabel.returnPressed.connect(
            lambda name=self.heightValueLabel: self.screen_capture_adjustments_line_edit(name))

        ####################################################################################################
        # Main Page CheckBox Logic
        ####################################################################################################

        self.filter = None

        self.enemiesCheckBox.stateChanged.connect(self.checkbox_state_change)
        self.enemiesDeadCheckBox.stateChanged.connect(
            self.checkbox_state_change)
        self.friendliesCheckBox.stateChanged.connect(
            self.checkbox_state_change)
        self.friendliesDeadCheckBox.stateChanged.connect(
            self.checkbox_state_change)
        self.lastSeenCheckBox.stateChanged.connect(self.checkbox_state_change)
        self.playersCheckBox.stateChanged.connect(self.checkbox_state_change)
        self.spikeCheckBox.stateChanged.connect(self.checkbox_state_change)
        self.spikePlantedCheckBox.stateChanged.connect(
            self.checkbox_state_change)

        ####################################################################################################
        # Submit a Report/Bug Page
        ####################################################################################################

        self.submitReportBtn.clicked.connect(self.submit_feedback)

        ####################################################################################################
        # Polygon Customisation
        ####################################################################################################

        self.createPolygonBtn.clicked.connect(self.init_polygon)
        self.setPolygonBtn.clicked.connect(self.set_polygon)

        self.polygon = []
        self.all_polygons = {}

        # Painting
        self.paintable_widget = PaintableLabel(self.screenCaptureLabel)
        self.paintable_widget.setGeometry(QRect(0, 0, 594, 500))
        self.paintable_widget.setAttribute(
            QtCore.Qt.WA_TransparentForMouseEvents)

        # Setting Mouse Tracking to Image Label
        self.tracker = MouseTracker(self.paintable_widget)
        # self.tracker.positionChanged.connect(
        #     self.on_positionChanged)  # Debug Conect
        self.tracker.clicked.connect(self.on_labelClicked)
        self.tracker.set_enabled(False)

####################################################################################################
# Functions
####################################################################################################

    def init_polygon(self):
        if self.createPolygonBtn.text() == "Create Tracking Zone":
            self.paintable_widget.setAttribute(
                QtCore.Qt.WA_TransparentForMouseEvents, False)
            self.createPolygonBtn.setText("Cancel")
            self.tracker.set_enabled(True)

        else:
            self.paintable_widget.setAttribute(
                QtCore.Qt.WA_TransparentForMouseEvents, True)
            self.paintable_widget.clear_circles()
            self.createPolygonBtn.setText("Create Tracking Zone")
            self.tracker.set_enabled(False)
            self.polygon = []

    def set_polygon(self):
        if self.polygonName.text() == "":
            num = len(self.all_polygons) + 1

            self.all_polygons[num] = self.polygon

            self.init_polygon()
        else:
            name = self.polygonName.text()

            if name in self.all_polygons:
                self.polygonLabel.setText("Pick a unique Polygon Name!")
                return

            self.all_polygons[name] = self.polygon

            self.init_polygon()

        self.tracker_updated = True
        self.polygons_updated = True
        self.polygonLabel.setText("")
        # print(self.all_polygons)
        # print(self.polygon)

    def on_positionChanged(self, pos):
        # DEBUG FUNCTION
        delta = QtCore.QPoint(30, -15)
        # self.label_position.show()
        # self.label_position.move(pos + delta)
        # self.label_position.setText("(%d, %d)" % (pos.x(), pos.y()))
        # self.label_position.adjustSize()
        print("(%d, %d)" % (pos.x(), pos.y()))
        print(self.all_polygons)

    def on_labelClicked(self, pos):
        if len(self.polygon) < 4:
            # Calculating Scaling
            x_scale = self.screenWidth / self.screenCaptureLabel.width()
            y_scale = self.screenHeight / self.screenCaptureLabel.height()

            # Adjust the X and Y Depending on the scale
            x = int(pos.x() * x_scale)
            y = int(pos.y() * y_scale)

            if not self.paintable_widget.testAttribute(QtCore.Qt.WA_TransparentForMouseEvents):
                self.paintable_widget.add_circle(pos)
            self.polygon.append([x, y])
        else:
            self.polygonLabel.setText("Polygon Dimensions Full, Set Polygon")

        # print(f"Mouse clicked on QLabel at position: ({pos.x()}, {pos.y()})")

    def checkbox_state_change(self):
        self.filter = None

        checked_boxes = [int(checkbox.toolTip()) for checkbox in self.findChildren(
            QCheckBox) if checkbox.isChecked()]
        # print('Checked boxes:', checked_boxes)

        # Updates the Filter Options for the model
        if len(checked_boxes) < 1:
            self.filter = None
            self.playersCheckBox.setCheckState(Qt.Checked)
            return

        for checked_box in checked_boxes:
            if self.filter:
                self.filter += f" | (detections.class_id == {checked_box})"
            else:
                self.filter = f"(detections.class_id == {checked_box})"

        return self.filter

    def submit_feedback(self):
        # Submit Feedback Function
        report = self.reportType.currentText()
        if self.reportTitle.text():
            title = self.reportTitle.text()
            self.reportTitleError.setText("")
        else:
            self.reportTitleError.setText("ERROR - Title is required")
            return
        if self.reportEmail.text():
            if is_valid_email(self.reportEmail.text()):
                email = self.reportEmail.text()
                self.reportEmailError.setText("")
            else:
                self.reportEmailError.setText(
                    "ERROR - Valid Email is required")
                return
        else:
            self.reportEmailError.setText("ERROR - Email is required")
            return
        if self.descriptionBox.toPlainText():
            description = self.descriptionBox.toPlainText()
            self.descriptionBoxError.setText("")
        else:
            self.descriptionBoxError.setText("ERROR - Description is required")
            return

        if send_email(self, report, title, email, description):
            self.descriptionBox.clear()
            self.reportTitle.clear()
            self.reportSendError.setStyleSheet("QLabel { color: green }")
            self.reportSendError.setText("Email Sent!")
        else:
            self.reportSendError.setStyleSheet("QLabel { color: red }")
            self.reportSendError.setText(
                "ERROR SENDING EMAIL, TRY AGAIN OR GET IN CONTACT VIA DISCORD: R3D#1371")

    def save_account_settings(self):
        username = self.get_username()
        tagline = self.get_tagline()

        if(username and tagline):
            validate = self.henrik_api.account_validate(username, tagline)
            if validate:
                # Save new settings to registry
                self.set_setting_values()
                # Update Settings Page
                self.populate_accounts_settings()
                # Update Error Message
                self.saveError.setText("")
                return True
            return self.saveError.setText("Unable To Validate your \n account Details \n Ensure they are correct!!")

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
            if len(tagline) <= 5:
                self.tagError.setText("")
                return tagline
            self.tagError.setText(
                "Must be 5 characters \n long")
            return False
        self.tagError.setText("TagLine Must be filled in")
        return False

    # Get PuUID From Input Function
    def get_puuid(self, username, tagline):
        # Generate Fake PuUID
        validate = self.henrik_api.account_validate(username, tagline)

        if validate:
            puuid = self.henrik_api.get_general_account_data(username, tagline)
            p = str(puuid["data"]["puuid"])
            if puuid:
                self.puuidInput.setText(p)
                self.puuidError.setText("")
                return puuid

            self.puuidError.setText(
                "Unable to Generate PuUID \n Double check Tagline and Username")
            return False
        return self.saveError.setText("Unable To Validate your \n account Details \n Ensure they are correct!!")

    def get_elo(self, version, region, username, tagline):
        if self.elo.text():
            return self.elo.text()
        elo_raw = self.henrik_api.get_elo_data(
            version, region, username, tagline)
        return elo_raw["data"]["elo"]

    def get_rank(self, version, region, username, tagline):
        if self.rank.text():
            return self.rank.text()
        rank_raw = self.henrik_api.get_elo_data(
            version, region, username, tagline)
        return rank_raw["data"]["currenttierpatched"]

    def set_user_image(self, username, tagline):
        raw_user_data = self.henrik_api.get_general_account_data(
            username, tagline)
        image = raw_user_data["data"]["card"]["large"]
        request = requests.get(image)

        pixmap = QPixmap()
        pixmap.loadFromData(request.content)

        self.profilePicture.setPixmap(pixmap)

    def set_setting_values(self):
        # Clear any previous settings
        self.account_settings.remove("username")
        self.account_settings.remove("tagline")
        self.account_settings.remove("puuid")
        self.account_settings.remove("full_username")
        self.account_settings.remove("region")
        self.account_settings.remove("shard")
        self.account_settings.remove("version")
        self.account_settings.remove("elo")
        self.account_settings.remove("current_rank")

        # Retrieve User Information from Input Fields
        username = self.get_username()
        tagline = self.get_tagline()
        raw_puuid = self.get_puuid(username, tagline)
        puuid = str(raw_puuid["data"]["puuid"])
        full_username = f"{username}#{tagline}"
        region = "eu"
        shard = "eu"
        version = "v1"

        elo = self.get_elo(version, region, username, tagline)
        rank = self.get_rank(version, region, username, tagline)

        # Save all information to the settings in registry
        self.account_settings.setValue("username", username)
        self.account_settings.setValue("tagline", tagline)
        self.account_settings.setValue("puuid", puuid)
        self.account_settings.setValue("full_username", full_username)

        self.account_settings.setValue("elo", elo)
        self.account_settings.setValue("current_rank", rank)

        self.account_settings.setValue("region", region)
        self.account_settings.setValue("shard", shard)
        self.account_settings.setValue("version", version)

    ####################################################################################################
    # Screen Capture Functions
    ####################################################################################################

    def screen_capture_adjustments_line_edit(self, edit):
        # print(edit.objectName())
        # print(edit.text())
        try:
            lineEditText = int(edit.text())
            # print(len(lineEditText))

            if edit.objectName() == "topValueLabel":
                self.screenTop = lineEditText

            elif edit.objectName() == "leftValueLabel":
                self.screenLeft = lineEditText

            elif edit.objectName() == "widthValueLabel":
                self.screenWidth = lineEditText

            elif edit.objectName() == "heightValueLabel":
                self.screenHeight = lineEditText

        except ValueError:
            print("Numbers Only No Characters (0..9)")

    def screen_capture_adjustments(self, btn):

        if btn.objectName() == "topPlusBtn":
            self.screenTop += 1
        elif btn.objectName() == "topMinusBtn":
            self.screenTop -= 1

        elif btn.objectName() == "leftPlusBtn":
            self.screenLeft += 1
        elif btn.objectName() == "leftMinusBtn":
            self.screenLeft -= 1

        elif btn.objectName() == "widthPlusBtn":
            self.screenWidth += 1
        elif btn.objectName() == "widthMinusBtn":
            self.screenWidth -= 1

        elif btn.objectName() == "heightPlusBtn":
            self.screenHeight += 1
        elif btn.objectName() == "heightMinusBtn":
            self.screenHeight -= 1

        self.set_screen_capture_dimensions_label()

    def set_screen_capture_dimensions_label(self):
        self.topValueLabel.setText(f"{self.screenTop}")
        self.leftValueLabel.setText(f"{self.screenLeft}")
        self.widthValueLabel.setText(f"{self.screenWidth}")
        self.heightValueLabel.setText(f"{self.screenHeight}")
