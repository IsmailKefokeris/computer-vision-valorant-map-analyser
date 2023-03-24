# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignThree.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 127)")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.action_Prerequisites = QAction(MainWindow)
        self.action_Prerequisites.setObjectName(u"action_Prerequisites")
        self.action_Account_Details = QAction(MainWindow)
        self.action_Account_Details.setObjectName(u"action_Account_Details")
        self.action_Submit_a_Bug = QAction(MainWindow)
        self.action_Submit_a_Bug.setObjectName(u"action_Submit_a_Bug")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(68, 68, 102)")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameToggle = QFrame(self.topBar)
        self.frameToggle.setObjectName(u"frameToggle")
        self.frameToggle.setMaximumSize(QSize(70, 40))
        self.frameToggle.setStyleSheet(u"background-color: rgb(139, 139, 207)")
        self.frameToggle.setFrameShape(QFrame.StyledPanel)
        self.frameToggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameToggle)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleMenuBtn = QPushButton(self.frameToggle)
        self.toggleMenuBtn.setObjectName(u"toggleMenuBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleMenuBtn.sizePolicy().hasHeightForWidth())
        self.toggleMenuBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Cascadia Mono SemiBold"])
        font.setPointSize(10)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.toggleMenuBtn.setFont(font)
        self.toggleMenuBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout.addWidget(self.toggleMenuBtn)


        self.horizontalLayout.addWidget(self.frameToggle)

        self.frameBar = QFrame(self.topBar)
        self.frameBar.setObjectName(u"frameBar")
        self.frameBar.setFrameShape(QFrame.StyledPanel)
        self.frameBar.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frameBar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 361, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono Light"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.closeBtn = QPushButton(self.frameBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(1170, 0, 40, 40))
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: red;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/images/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.minBtn = QPushButton(self.frameBar)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setGeometry(QRect(1130, 0, 40, 40))
        self.minBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(133, 133, 199);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/images/icons/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.frameBar)


        self.verticalLayout_2.addWidget(self.topBar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBar = QFrame(self.content)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setMinimumSize(QSize(0, 0))
        self.menuBar.setMaximumSize(QSize(0, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Emoji"])
        font2.setPointSize(9)
        self.menuBar.setFont(font2)
        self.menuBar.setStyleSheet(u"background-color: rgb(68, 68, 102)")
        self.menuBar.setFrameShape(QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtns = QFrame(self.menuBar)
        self.menuBtns.setObjectName(u"menuBtns")
        self.menuBtns.setFrameShape(QFrame.StyledPanel)
        self.menuBtns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menuBtns)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 15, 0, 0)
        self.bugBtn = QPushButton(self.menuBtns)
        self.bugBtn.setObjectName(u"bugBtn")
        self.bugBtn.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Cascadia Mono SemiLight"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.bugBtn.setFont(font3)
        self.bugBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bugBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.verticalLayout_5.addWidget(self.bugBtn)

        self.mainPageBtn = QPushButton(self.menuBtns)
        self.mainPageBtn.setObjectName(u"mainPageBtn")
        self.mainPageBtn.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamilies([u"Cascadia Mono SemiLight"])
        font4.setPointSize(10)
        self.mainPageBtn.setFont(font4)
        self.mainPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainPageBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.verticalLayout_5.addWidget(self.mainPageBtn)

        self.prerequisitesBtn = QPushButton(self.menuBtns)
        self.prerequisitesBtn.setObjectName(u"prerequisitesBtn")
        self.prerequisitesBtn.setMinimumSize(QSize(0, 50))
        self.prerequisitesBtn.setFont(font4)
        self.prerequisitesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prerequisitesBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.verticalLayout_5.addWidget(self.prerequisitesBtn)

        self.accountSettingsBtn = QPushButton(self.menuBtns)
        self.accountSettingsBtn.setObjectName(u"accountSettingsBtn")
        self.accountSettingsBtn.setMinimumSize(QSize(0, 50))
        self.accountSettingsBtn.setFont(font4)
        self.accountSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountSettingsBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.verticalLayout_5.addWidget(self.accountSettingsBtn)


        self.verticalLayout_3.addWidget(self.menuBtns, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.menuBar)

        self.applicationPages = QFrame(self.content)
        self.applicationPages.setObjectName(u"applicationPages")
        self.applicationPages.setFrameShape(QFrame.StyledPanel)
        self.applicationPages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.applicationPages)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.applicationPages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(1280, 16777215))
        self.layoutWidget = QWidget(self.mainPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 1221, 571))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.screenCaptureLabel = QLabel(self.layoutWidget)
        self.screenCaptureLabel.setObjectName(u"screenCaptureLabel")
        self.screenCaptureLabel.setMinimumSize(QSize(500, 500))
        self.screenCaptureLabel.setMaximumSize(QSize(500, 500))
        self.screenCaptureLabel.setTextFormat(Qt.MarkdownText)
        self.screenCaptureLabel.setPixmap(QPixmap(u":/assets/images/placeholder.PNG"))
        self.screenCaptureLabel.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.screenCaptureLabel)

        self.screenVisualiser = QLabel(self.layoutWidget)
        self.screenVisualiser.setObjectName(u"screenVisualiser")
        self.screenVisualiser.setMinimumSize(QSize(500, 500))
        self.screenVisualiser.setMaximumSize(QSize(650, 500))
        self.screenVisualiser.setTextFormat(Qt.MarkdownText)
        self.screenVisualiser.setPixmap(QPixmap(u":/assets/images/placeholder.PNG"))
        self.screenVisualiser.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.screenVisualiser)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.startBtn = QPushButton(self.layoutWidget)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(170, 40))
        self.startBtn.setMaximumSize(QSize(170, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Cascadia Mono SemiBold"])
        font5.setPointSize(20)
        self.startBtn.setFont(font5)
        self.startBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.startBtn)

        self.stopBtn = QPushButton(self.layoutWidget)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(170, 40))
        self.stopBtn.setMaximumSize(QSize(170, 16777215))
        self.stopBtn.setFont(font5)
        self.stopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.stopBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.mainPage)
        self.accountSettingsPage = QWidget()
        self.accountSettingsPage.setObjectName(u"accountSettingsPage")
        self.horizontalLayout_4 = QHBoxLayout(self.accountSettingsPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.settingsAdjustment = QFrame(self.accountSettingsPage)
        self.settingsAdjustment.setObjectName(u"settingsAdjustment")
        self.settingsAdjustment.setFrameShape(QFrame.StyledPanel)
        self.settingsAdjustment.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.settingsAdjustment)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tagLabel = QLabel(self.settingsAdjustment)
        self.tagLabel.setObjectName(u"tagLabel")
        self.tagLabel.setMinimumSize(QSize(0, 30))
        self.tagLabel.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamilies([u"Cascadia Mono ExtraLight"])
        font6.setPointSize(10)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.tagLabel.setFont(font6)
        self.tagLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tagLabel, 1, 0, 1, 1)

        self.shardLabel = QLabel(self.settingsAdjustment)
        self.shardLabel.setObjectName(u"shardLabel")
        self.shardLabel.setMinimumSize(QSize(0, 30))
        self.shardLabel.setMaximumSize(QSize(16777215, 30))
        self.shardLabel.setFont(font6)
        self.shardLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.shardLabel, 8, 0, 1, 1)

        self.shardInput = QLineEdit(self.settingsAdjustment)
        self.shardInput.setObjectName(u"shardInput")
        self.shardInput.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.shardInput.sizePolicy().hasHeightForWidth())
        self.shardInput.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Cascadia Mono"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.shardInput.setFont(font7)
        self.shardInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.shardInput.setReadOnly(True)

        self.gridLayout.addWidget(self.shardInput, 8, 1, 1, 1)

        self.regionInput = QLineEdit(self.settingsAdjustment)
        self.regionInput.setObjectName(u"regionInput")
        self.regionInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.regionInput.sizePolicy().hasHeightForWidth())
        self.regionInput.setSizePolicy(sizePolicy1)
        self.regionInput.setFont(font7)
        self.regionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.regionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.regionInput, 6, 1, 1, 1)

        self.tagError = QLabel(self.settingsAdjustment)
        self.tagError.setObjectName(u"tagError")
        self.tagError.setMinimumSize(QSize(130, 15))
        self.tagError.setMaximumSize(QSize(200, 25))
        font8 = QFont()
        font8.setFamilies([u"Cascadia Mono Light"])
        font8.setItalic(True)
        self.tagError.setFont(font8)
        self.tagError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.tagError, 1, 2, 1, 1)

        self.ppuidLabel = QLabel(self.settingsAdjustment)
        self.ppuidLabel.setObjectName(u"ppuidLabel")
        self.ppuidLabel.setMinimumSize(QSize(0, 30))
        self.ppuidLabel.setMaximumSize(QSize(16777215, 30))
        self.ppuidLabel.setFont(font6)
        self.ppuidLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.ppuidLabel, 5, 0, 1, 1)

        self.regionLabel = QLabel(self.settingsAdjustment)
        self.regionLabel.setObjectName(u"regionLabel")
        self.regionLabel.setMinimumSize(QSize(0, 30))
        self.regionLabel.setMaximumSize(QSize(16777215, 30))
        self.regionLabel.setFont(font6)
        self.regionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.regionLabel, 6, 0, 1, 1)

        self.usernameLabel = QLabel(self.settingsAdjustment)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(0, 30))
        self.usernameLabel.setMaximumSize(QSize(16777215, 30))
        self.usernameLabel.setFont(font6)
        self.usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.versionLabel = QLabel(self.settingsAdjustment)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMinimumSize(QSize(0, 30))
        self.versionLabel.setMaximumSize(QSize(16777215, 30))
        self.versionLabel.setFont(font6)
        self.versionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.versionLabel, 9, 0, 1, 1)

        self.ppuidInput = QLineEdit(self.settingsAdjustment)
        self.ppuidInput.setObjectName(u"ppuidInput")
        self.ppuidInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ppuidInput.sizePolicy().hasHeightForWidth())
        self.ppuidInput.setSizePolicy(sizePolicy1)
        self.ppuidInput.setFont(font7)
        self.ppuidInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ppuidInput.setReadOnly(True)

        self.gridLayout.addWidget(self.ppuidInput, 5, 1, 1, 1)

        self.versionInput = QLineEdit(self.settingsAdjustment)
        self.versionInput.setObjectName(u"versionInput")
        self.versionInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.versionInput.sizePolicy().hasHeightForWidth())
        self.versionInput.setSizePolicy(sizePolicy1)
        self.versionInput.setFont(font7)
        self.versionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.versionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.versionInput, 9, 1, 1, 1)

        self.tagInput = QLineEdit(self.settingsAdjustment)
        self.tagInput.setObjectName(u"tagInput")
        sizePolicy1.setHeightForWidth(self.tagInput.sizePolicy().hasHeightForWidth())
        self.tagInput.setSizePolicy(sizePolicy1)
        self.tagInput.setFont(font7)
        self.tagInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tagInput, 1, 1, 1, 1)

        self.usernameInput = QLineEdit(self.settingsAdjustment)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy1.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy1)
        self.usernameInput.setFont(font7)
        self.usernameInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.usernameInput, 0, 1, 1, 1)

        self.ppuidError = QLabel(self.settingsAdjustment)
        self.ppuidError.setObjectName(u"ppuidError")
        self.ppuidError.setMinimumSize(QSize(130, 15))
        self.ppuidError.setMaximumSize(QSize(200, 25))
        self.ppuidError.setFont(font8)
        self.ppuidError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.ppuidError, 5, 2, 1, 1)

        self.usernameError = QLabel(self.settingsAdjustment)
        self.usernameError.setObjectName(u"usernameError")
        self.usernameError.setMinimumSize(QSize(130, 15))
        self.usernameError.setMaximumSize(QSize(200, 15))
        self.usernameError.setFont(font8)
        self.usernameError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.usernameError, 0, 2, 1, 1)

        self.saveSettingsBtn = QPushButton(self.settingsAdjustment)
        self.saveSettingsBtn.setObjectName(u"saveSettingsBtn")
        self.saveSettingsBtn.setMinimumSize(QSize(150, 30))
        self.saveSettingsBtn.setMaximumSize(QSize(150, 30))
        font9 = QFont()
        font9.setFamilies([u"Cascadia Mono"])
        font9.setPointSize(10)
        self.saveSettingsBtn.setFont(font9)
        self.saveSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveSettingsBtn.setToolTipDuration(-1)
        self.saveSettingsBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.gridLayout.addWidget(self.saveSettingsBtn, 10, 1, 1, 1)

        self.saveError = QLabel(self.settingsAdjustment)
        self.saveError.setObjectName(u"saveError")
        self.saveError.setMinimumSize(QSize(130, 15))
        self.saveError.setMaximumSize(QSize(200, 25))
        self.saveError.setFont(font8)
        self.saveError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.saveError, 10, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.settingsAdjustment)

        self.playerInformation = QFrame(self.accountSettingsPage)
        self.playerInformation.setObjectName(u"playerInformation")
        self.playerInformation.setFrameShape(QFrame.StyledPanel)
        self.playerInformation.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.playerInformation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.profilePicture = QLabel(self.playerInformation)
        self.profilePicture.setObjectName(u"profilePicture")
        self.profilePicture.setMaximumSize(QSize(250, 250))
        self.profilePicture.setPixmap(QPixmap(u":/assets/images/Vertical_jett.png"))
        self.profilePicture.setScaledContents(True)

        self.gridLayout_2.addWidget(self.profilePicture, 2, 0, 1, 1)

        self.mmr = QLabel(self.playerInformation)
        self.mmr.setObjectName(u"mmr")
        self.mmr.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setFamilies([u"Cascadia Mono"])
        font10.setPointSize(11)
        self.mmr.setFont(font10)
        self.mmr.setLayoutDirection(Qt.LeftToRight)
        self.mmr.setStyleSheet(u"color: white;")
        self.mmr.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.mmr, 3, 2, 1, 1)

        self.mmrLabel_2 = QLabel(self.playerInformation)
        self.mmrLabel_2.setObjectName(u"mmrLabel_2")
        self.mmrLabel_2.setMaximumSize(QSize(16777215, 30))
        self.mmrLabel_2.setFont(font10)
        self.mmrLabel_2.setLayoutDirection(Qt.LeftToRight)
        self.mmrLabel_2.setStyleSheet(u"color: white;")
        self.mmrLabel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.mmrLabel_2, 4, 0, 1, 1)

        self.mmrLabel = QLabel(self.playerInformation)
        self.mmrLabel.setObjectName(u"mmrLabel")
        self.mmrLabel.setMaximumSize(QSize(16777215, 30))
        self.mmrLabel.setFont(font10)
        self.mmrLabel.setLayoutDirection(Qt.LeftToRight)
        self.mmrLabel.setStyleSheet(u"color: white;")
        self.mmrLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.mmrLabel, 3, 0, 1, 1)

        self.mmr_2 = QLabel(self.playerInformation)
        self.mmr_2.setObjectName(u"mmr_2")
        self.mmr_2.setFont(font10)
        self.mmr_2.setLayoutDirection(Qt.LeftToRight)
        self.mmr_2.setStyleSheet(u"color: white;")
        self.mmr_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.mmr_2, 4, 2, 1, 1)

        self.username = QLabel(self.playerInformation)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 30))
        self.username.setFont(font10)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"color: white;")
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.username, 2, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.playerInformation)

        self.stackedWidget.addWidget(self.accountSettingsPage)
        self.submitBugPage = QWidget()
        self.submitBugPage.setObjectName(u"submitBugPage")
        self.verticalLayout_7 = QVBoxLayout(self.submitBugPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.submitBugPageFrame = QFrame(self.submitBugPage)
        self.submitBugPageFrame.setObjectName(u"submitBugPageFrame")
        self.submitBugPageFrame.setFrameShape(QFrame.StyledPanel)
        self.submitBugPageFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.submitBugPageFrame)

        self.stackedWidget.addWidget(self.submitBugPage)
        self.preRequisitesPage = QWidget()
        self.preRequisitesPage.setObjectName(u"preRequisitesPage")
        self.verticalLayout_11 = QVBoxLayout(self.preRequisitesPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.preRequisitesPageFrame = QFrame(self.preRequisitesPage)
        self.preRequisitesPageFrame.setObjectName(u"preRequisitesPageFrame")
        self.preRequisitesPageFrame.setFrameShape(QFrame.StyledPanel)
        self.preRequisitesPageFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.preRequisitesPageFrame)

        self.stackedWidget.addWidget(self.preRequisitesPage)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.applicationPages)


        self.verticalLayout_2.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.toggleMenuBtn, self.bugBtn)
        QWidget.setTabOrder(self.bugBtn, self.mainPageBtn)
        QWidget.setTabOrder(self.mainPageBtn, self.prerequisitesBtn)
        QWidget.setTabOrder(self.prerequisitesBtn, self.accountSettingsBtn)
        QWidget.setTabOrder(self.accountSettingsBtn, self.minBtn)
        QWidget.setTabOrder(self.minBtn, self.closeBtn)
        QWidget.setTabOrder(self.closeBtn, self.startBtn)
        QWidget.setTabOrder(self.startBtn, self.stopBtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_Prerequisites.setText(QCoreApplication.translate("MainWindow", u"&Prerequisites", None))
        self.action_Account_Details.setText(QCoreApplication.translate("MainWindow", u"&Account Details", None))
        self.action_Submit_a_Bug.setText(QCoreApplication.translate("MainWindow", u"&Submit a Bug", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.toggleMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Valorant Map Analyser", None))
        self.bugBtn.setText(QCoreApplication.translate("MainWindow", u"Submit a Bug", None))
        self.mainPageBtn.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.prerequisitesBtn.setText(QCoreApplication.translate("MainWindow", u"Pre-requisites", None))
        self.accountSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Account Settings", None))
        self.screenCaptureLabel.setText("")
        self.screenVisualiser.setText("")
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.settingsAdjustment.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tagLabel.setText(QCoreApplication.translate("MainWindow", u"Tag Line \n"
" Include (#)", None))
        self.shardLabel.setText(QCoreApplication.translate("MainWindow", u"Shard", None))
        self.shardInput.setText(QCoreApplication.translate("MainWindow", u"eu", None))
        self.regionInput.setText(QCoreApplication.translate("MainWindow", u"eu", None))
        self.tagError.setText("")
        self.ppuidLabel.setText(QCoreApplication.translate("MainWindow", u"PPUID", None))
        self.regionLabel.setText(QCoreApplication.translate("MainWindow", u"Region", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.ppuidInput.setText("")
        self.ppuidInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Generated after Saving", None))
        self.versionInput.setText(QCoreApplication.translate("MainWindow", u"v1", None))
        self.tagInput.setInputMask("")
        self.tagInput.setText("")
        self.tagInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Player Tagline", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Player Username", None))
        self.ppuidError.setText("")
        self.usernameError.setText("")
#if QT_CONFIG(tooltip)
        self.saveSettingsBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.saveSettingsBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.saveSettingsBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.saveSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.saveError.setText("")
        self.profilePicture.setText("")
        self.mmr.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.mmrLabel_2.setText(QCoreApplication.translate("MainWindow", u"Current Rank:", None))
        self.mmrLabel.setText(QCoreApplication.translate("MainWindow", u"MMR:", None))
        self.mmr_2.setText(QCoreApplication.translate("MainWindow", u"Gold 3", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username#Tagline", None))
    # retranslateUi

