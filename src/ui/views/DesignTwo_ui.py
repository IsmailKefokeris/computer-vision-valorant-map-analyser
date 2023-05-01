# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignTwo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import assets.resources_rc as resources_rc
import assets.resources_rc as resources_rc

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
        font.setFamilies([u"Cascadia Mono SemiLight"])
        font.setPointSize(10)
        font.setBold(True)
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
        self.label.setGeometry(QRect(10, 0, 281, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono SemiBold"])
        font1.setPointSize(15)
        font1.setBold(True)
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
        icon.addFile(u":/images/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u":/images/icons/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.menuBar.setMaximumSize(QSize(70, 16777215))
        self.menuBar.setStyleSheet(u"background-color: rgb(68, 68, 102)")
        self.menuBar.setFrameShape(QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtns = QFrame(self.menuBar)
        self.menuBtns.setObjectName(u"menuBtns")
        self.menuBtns.setFrameShape(QFrame.StyledPanel)
        self.menuBtns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menuBtns)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 20, 0, 0)
        self.bugBtnFrame = QFrame(self.menuBtns)
        self.bugBtnFrame.setObjectName(u"bugBtnFrame")
        self.bugBtnFrame.setMinimumSize(QSize(200, 40))
        self.bugBtnFrame.setMaximumSize(QSize(16777215, 40))
        self.bugBtnFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.bugBtnFrame.setStyleSheet(u"QFrame::hover{\n"
"	background-color: rgb(139, 139, 207);\n"
"	color: white;\n"
"}")
        self.bugBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.bugBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bugBtnFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.bugLabel = QLabel(self.bugBtnFrame)
        self.bugLabel.setObjectName(u"bugLabel")
        self.bugLabel.setMinimumSize(QSize(0, 0))
        self.bugLabel.setMaximumSize(QSize(50, 50))
        self.bugLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.bugLabel.setStyleSheet(u"background: transparent;")
        self.bugLabel.setFrameShape(QFrame.NoFrame)
        self.bugLabel.setFrameShadow(QFrame.Plain)
        self.bugLabel.setLineWidth(0)
        self.bugLabel.setPixmap(QPixmap(u":/images/icons/bug.png"))
        self.bugLabel.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.bugLabel)

        self.bugBtn = QPushButton(self.bugBtnFrame)
        self.bugBtn.setObjectName(u"bugBtn")
        self.bugBtn.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.bugBtn.setFont(font2)
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

        self.horizontalLayout_5.addWidget(self.bugBtn)


        self.verticalLayout_5.addWidget(self.bugBtnFrame)

        self.mainPageFrameBtn = QFrame(self.menuBtns)
        self.mainPageFrameBtn.setObjectName(u"mainPageFrameBtn")
        self.mainPageFrameBtn.setMinimumSize(QSize(200, 40))
        self.mainPageFrameBtn.setMaximumSize(QSize(16777215, 40))
        self.mainPageFrameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainPageFrameBtn.setStyleSheet(u"QFrame::hover{\n"
"	background-color: rgb(139, 139, 207);\n"
"	color: white;\n"
"}")
        self.mainPageFrameBtn.setFrameShape(QFrame.StyledPanel)
        self.mainPageFrameBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.mainPageFrameBtn)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.mainPageLabel = QLabel(self.mainPageFrameBtn)
        self.mainPageLabel.setObjectName(u"mainPageLabel")
        self.mainPageLabel.setMaximumSize(QSize(50, 50))
        self.mainPageLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainPageLabel.setStyleSheet(u"background: transparent;")
        self.mainPageLabel.setPixmap(QPixmap(u":/images/icons/home.png"))
        self.mainPageLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.mainPageLabel)

        self.mainPageBtn = QPushButton(self.mainPageFrameBtn)
        self.mainPageBtn.setObjectName(u"mainPageBtn")
        self.mainPageBtn.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(12)
        self.mainPageBtn.setFont(font3)
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

        self.horizontalLayout_4.addWidget(self.mainPageBtn)


        self.verticalLayout_5.addWidget(self.mainPageFrameBtn)

        self.preRequisitsBtnFrame = QFrame(self.menuBtns)
        self.preRequisitsBtnFrame.setObjectName(u"preRequisitsBtnFrame")
        self.preRequisitsBtnFrame.setMinimumSize(QSize(200, 40))
        self.preRequisitsBtnFrame.setMaximumSize(QSize(16777215, 40))
        self.preRequisitsBtnFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.preRequisitsBtnFrame.setStyleSheet(u"QFrame::hover{\n"
"	background-color: rgb(139, 139, 207);\n"
"	color: white;\n"
"}")
        self.preRequisitsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.preRequisitsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.preRequisitsBtnFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.prerequisitesLabel = QLabel(self.preRequisitsBtnFrame)
        self.prerequisitesLabel.setObjectName(u"prerequisitesLabel")
        self.prerequisitesLabel.setMaximumSize(QSize(50, 50))
        self.prerequisitesLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.prerequisitesLabel.setStyleSheet(u"background: transparent;")
        self.prerequisitesLabel.setPixmap(QPixmap(u":/images/icons/preRequisits.png"))
        self.prerequisitesLabel.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.prerequisitesLabel)

        self.prerequisitesBtn = QPushButton(self.preRequisitsBtnFrame)
        self.prerequisitesBtn.setObjectName(u"prerequisitesBtn")
        self.prerequisitesBtn.setMinimumSize(QSize(0, 40))
        self.prerequisitesBtn.setFont(font3)
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

        self.horizontalLayout_6.addWidget(self.prerequisitesBtn)


        self.verticalLayout_5.addWidget(self.preRequisitsBtnFrame)

        self.SettingsBtnFrame = QFrame(self.menuBtns)
        self.SettingsBtnFrame.setObjectName(u"SettingsBtnFrame")
        self.SettingsBtnFrame.setMinimumSize(QSize(200, 40))
        self.SettingsBtnFrame.setMaximumSize(QSize(16777215, 40))
        self.SettingsBtnFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.SettingsBtnFrame.setStyleSheet(u"QFrame::hover{\n"
"	background-color: rgb(139, 139, 207);\n"
"	color: white;\n"
"}")
        self.SettingsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.SettingsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.SettingsBtnFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.settingsLabel = QLabel(self.SettingsBtnFrame)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setMaximumSize(QSize(50, 50))
        self.settingsLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsLabel.setStyleSheet(u"background: transparent;")
        self.settingsLabel.setPixmap(QPixmap(u":/images/icons/settings.png"))
        self.settingsLabel.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.settingsLabel)

        self.settingsBtn = QPushButton(self.SettingsBtnFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 40))
        self.settingsBtn.setMaximumSize(QSize(200, 16777215))
        self.settingsBtn.setFont(font3)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.horizontalLayout_7.addWidget(self.settingsBtn)


        self.verticalLayout_5.addWidget(self.SettingsBtnFrame)


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
        self.verticalLayout_7 = QVBoxLayout(self.mainPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.screenCaptureLabel = QLabel(self.mainPage)
        self.screenCaptureLabel.setObjectName(u"screenCaptureLabel")
        self.screenCaptureLabel.setMinimumSize(QSize(500, 500))
        self.screenCaptureLabel.setMaximumSize(QSize(500, 500))
        self.screenCaptureLabel.setTextFormat(Qt.MarkdownText)
        self.screenCaptureLabel.setPixmap(QPixmap(u":/images/placeholder.PNG"))
        self.screenCaptureLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.screenCaptureLabel)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 25, 25, 25)
        self.startBtn = QPushButton(self.mainPage)
        self.startBtn.setObjectName(u"startBtn")
        font4 = QFont()
        font4.setFamilies([u"Maiandra GD"])
        font4.setPointSize(30)
        self.startBtn.setFont(font4)
        self.startBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: black;\n"
"	border: 2px solid white;\n"
"	border-radius: 25px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: white;\n"
"	color: black;\n"
"	widget-animation-duration: 5000;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.startBtn)

        self.stopBtn = QPushButton(self.mainPage)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setFont(font4)
        self.stopBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: black;\n"
"	border: 2px solid white;\n"
"	border-radius: 25px;\n"
"	color: white;\n"
"}\n"
"\n"
".QPushButton::hover {\n"
"  	background-color: white;\n"
"	color: black;\n"
"}")

        self.verticalLayout_4.addWidget(self.stopBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.mainPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.stackedWidget.addWidget(self.settingsPage)
        self.submitBugPage = QWidget()
        self.submitBugPage.setObjectName(u"submitBugPage")
        self.stackedWidget.addWidget(self.submitBugPage)
        self.preRequisitsPage = QWidget()
        self.preRequisitsPage.setObjectName(u"preRequisitsPage")
        self.stackedWidget.addWidget(self.preRequisitsPage)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.applicationPages)


        self.verticalLayout_2.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.action_Prerequisites.setText(QCoreApplication.translate("MainWindow", u"&Prerequisites", None))
        self.action_Account_Details.setText(QCoreApplication.translate("MainWindow", u"&Account Details", None))
        self.action_Submit_a_Bug.setText(QCoreApplication.translate("MainWindow", u"&Submit a Bug", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.toggleMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Valorant Map Analyser", None))
        self.bugBtn.setText(QCoreApplication.translate("MainWindow", u"Submit a Bug", None))
        self.mainPageBtn.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.prerequisitesBtn.setText(QCoreApplication.translate("MainWindow", u"Pre-requisites", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.screenCaptureLabel.setText("")
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

