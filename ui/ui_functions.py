from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect

# Importing Modules to help with feedback sending through Emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# .env
import os
from dotenv import load_dotenv


# Import GUI File
from ui.gui_interface import *

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
        self.screenTop = 30
        self.screenLeft = 52
        self.screenWidth = 320
        self.screenHeight = 350

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
        if self.descriptionBox.toPlainText():
            description = self.descriptionBox.toPlainText()
            self.descriptionBoxError.setText("")
        else:
            self.descriptionBoxError.setText("ERROR - Description is required")
            return

        # Setup Email Message
        try:
            message = MIMEMultipart()
            message["From"] = os.environ.get("ADMIN_EMAIL")
            message["To"] = os.environ.get("EMAIL_RECIPIENT")
            message["Subject"] = "Feedback from VMA Application"
            body = f"Report Type: {report} \n Title: {title} \nFeedback: {description}"

            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(os.environ.get("EMAIL_SERVER"), os.environ.get("EMAIL_PORT")) as server:
                server.starttls()
                server.login(os.environ.get("ADMIN_EMAIL"),
                             os.environ.get("ADMIN_PASSWORD"))
                server.sendmail(os.environ.get("ADMIN_EMAIL"),
                                os.environ.get("EMAIL_RECIPIENT"), message.as_string())

            self.descriptionBox.clear()
            self.reportTitle.clear()
            return True

        except Exception as e:
            print(e)

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
