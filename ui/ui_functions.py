from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect

# Import GUI File
from ui.gui_interface import *


class UIFunctions:
    # https://github.com/Wanderson-Magalhaes/Python_PySide2_Custom_Title_Bar/blob/master/ui_functions.py

    # Determines What the buttons on the top bar do and how the window works
    def uiDefinitions(self):
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
