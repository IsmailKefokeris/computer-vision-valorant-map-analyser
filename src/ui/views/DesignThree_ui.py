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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
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
        self.applicationPages.setMaximumSize(QSize(16777215, 680))
        self.applicationPages.setFrameShape(QFrame.StyledPanel)
        self.applicationPages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.applicationPages)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.applicationPages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(1280, 16777215))
        self.gridLayout_3 = QGridLayout(self.mainPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.startBtn = QPushButton(self.mainPage)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(174, 44))
        self.startBtn.setMaximumSize(QSize(174, 16777215))
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
"	min-width: 170px;\n"
"	max-width: 170px;\n"
"	min-height: 40px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.startBtn, 3, 0, 1, 1)

        self.screenCaptureLabel = QLabel(self.mainPage)
        self.screenCaptureLabel.setObjectName(u"screenCaptureLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.screenCaptureLabel.sizePolicy().hasHeightForWidth())
        self.screenCaptureLabel.setSizePolicy(sizePolicy1)
        self.screenCaptureLabel.setMinimumSize(QSize(500, 500))
        self.screenCaptureLabel.setMaximumSize(QSize(600, 500))
        self.screenCaptureLabel.setStyleSheet(u"#screenCaptureLabel{\n"
"	min-width: 500px;\n"
"	max-width: 600px;\n"
"	min-height: 500px;\n"
"	max-height: 500px;\n"
"}")
        self.screenCaptureLabel.setTextFormat(Qt.MarkdownText)
        self.screenCaptureLabel.setPixmap(QPixmap(u":/assets/images/placeholder.PNG"))
        self.screenCaptureLabel.setScaledContents(True)

        self.gridLayout_3.addWidget(self.screenCaptureLabel, 0, 0, 1, 3)

        self.setPolygonBtn = QPushButton(self.mainPage)
        self.setPolygonBtn.setObjectName(u"setPolygonBtn")
        self.setPolygonBtn.setMinimumSize(QSize(134, 24))
        self.setPolygonBtn.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Cascadia Mono Light"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.setPolygonBtn.setFont(font6)
        self.setPolygonBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setPolygonBtn.setStyleSheet(u"QPushButton{\n"
"	font: 300 10pt \"Cascadia Mono Light\";\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 130px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.setPolygonBtn, 1, 2, 1, 1)

        self.polygonName = QLineEdit(self.mainPage)
        self.polygonName.setObjectName(u"polygonName")
        self.polygonName.setStyleSheet(u"#polygonName{\n"
"	font: 300 10pt \"Cascadia Mono Light\";\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 130px;\n"
"	max-width: 130px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"")
        self.polygonName.setReadOnly(True)

        self.gridLayout_3.addWidget(self.polygonName, 1, 1, 1, 1)

        self.createPolygonBtn = QPushButton(self.mainPage)
        self.createPolygonBtn.setObjectName(u"createPolygonBtn")
        self.createPolygonBtn.setMinimumSize(QSize(134, 24))
        self.createPolygonBtn.setMaximumSize(QSize(16777215, 16777215))
        self.createPolygonBtn.setFont(font6)
        self.createPolygonBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createPolygonBtn.setStyleSheet(u"QPushButton{\n"
"	font: 300 10pt \"Cascadia Mono Light\";\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 130px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.createPolygonBtn, 1, 0, 1, 1)

        self.polygonLabel = QLabel(self.mainPage)
        self.polygonLabel.setObjectName(u"polygonLabel")
        self.polygonLabel.setMaximumSize(QSize(600, 25))
        self.polygonLabel.setStyleSheet(u"#polygonLabel {\n"
"	font: 10pt \"Cascadia Code\";\n"
"	color: rgb(170, 0, 0);\n"
"	max-height: 25px;\n"
"}")
        self.polygonLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.polygonLabel, 2, 0, 1, 3)

        self.stopBtn = QPushButton(self.mainPage)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(174, 44))
        self.stopBtn.setMaximumSize(QSize(174, 16777215))
        self.stopBtn.setFont(font5)
        self.stopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"	min-width: 170px;\n"
"	max-width: 170px;\n"
"	min-height: 40px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.stopBtn, 3, 2, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.mainPage)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(735, 16777215))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.heightMinusBtn = QPushButton(self.page_3)
        self.screenCaptureControls = QButtonGroup(MainWindow)
        self.screenCaptureControls.setObjectName(u"screenCaptureControls")
        self.screenCaptureControls.addButton(self.heightMinusBtn)
        self.heightMinusBtn.setObjectName(u"heightMinusBtn")
        self.heightMinusBtn.setMinimumSize(QSize(84, 24))
        self.heightMinusBtn.setMaximumSize(QSize(84, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Cascadia Mono SemiBold"])
        font7.setPointSize(12)
        self.heightMinusBtn.setFont(font7)
        self.heightMinusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.heightMinusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.heightMinusBtn, 6, 3, 1, 1)

        self.topPlusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.topPlusBtn)
        self.topPlusBtn.setObjectName(u"topPlusBtn")
        self.topPlusBtn.setMinimumSize(QSize(84, 24))
        self.topPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.topPlusBtn.setFont(font7)
        self.topPlusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.topPlusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.topPlusBtn, 5, 0, 1, 1)

        self.topValueLabel = QLineEdit(self.page_3)
        self.topValueLabel.setObjectName(u"topValueLabel")
        self.topValueLabel.setMinimumSize(QSize(84, 25))
        self.topValueLabel.setMaximumSize(QSize(84, 25))
        font8 = QFont()
        font8.setFamilies([u"Cascadia Mono"])
        self.topValueLabel.setFont(font8)

        self.gridLayout_6.addWidget(self.topValueLabel, 3, 0, 1, 1)

        self.widthValueLabel = QLineEdit(self.page_3)
        self.widthValueLabel.setObjectName(u"widthValueLabel")
        self.widthValueLabel.setMinimumSize(QSize(84, 25))
        self.widthValueLabel.setMaximumSize(QSize(84, 25))
        self.widthValueLabel.setFont(font8)

        self.gridLayout_6.addWidget(self.widthValueLabel, 3, 2, 1, 1)

        self.widthMinusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.widthMinusBtn)
        self.widthMinusBtn.setObjectName(u"widthMinusBtn")
        self.widthMinusBtn.setMinimumSize(QSize(84, 24))
        self.widthMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.widthMinusBtn.setFont(font7)
        self.widthMinusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.widthMinusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.widthMinusBtn, 6, 2, 1, 1)

        self.previousBtn = QPushButton(self.page_3)
        self.previousBtn.setObjectName(u"previousBtn")
        self.previousBtn.setMinimumSize(QSize(82, 22))
        self.previousBtn.setMaximumSize(QSize(82, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Cascadia Code"])
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setItalic(False)
        self.previousBtn.setFont(font9)
        self.previousBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousBtn.setStyleSheet(u"QPushButton{\n"
"	font: 10pt \"Cascadia Code\";\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.previousBtn, 7, 1, 1, 1)

        self.widthPlusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.widthPlusBtn)
        self.widthPlusBtn.setObjectName(u"widthPlusBtn")
        self.widthPlusBtn.setMinimumSize(QSize(84, 24))
        self.widthPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.widthPlusBtn.setFont(font7)
        self.widthPlusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.widthPlusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.widthPlusBtn, 5, 2, 1, 1)

        self.leftMinusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.leftMinusBtn)
        self.leftMinusBtn.setObjectName(u"leftMinusBtn")
        self.leftMinusBtn.setMinimumSize(QSize(84, 24))
        self.leftMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.leftMinusBtn.setFont(font7)
        self.leftMinusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.leftMinusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.leftMinusBtn, 6, 1, 1, 1)

        self.heightPlusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.heightPlusBtn)
        self.heightPlusBtn.setObjectName(u"heightPlusBtn")
        self.heightPlusBtn.setMinimumSize(QSize(84, 24))
        self.heightPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.heightPlusBtn.setFont(font7)
        self.heightPlusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.heightPlusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.heightPlusBtn, 5, 3, 1, 1)

        self.leftPlusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.leftPlusBtn)
        self.leftPlusBtn.setObjectName(u"leftPlusBtn")
        self.leftPlusBtn.setMinimumSize(QSize(84, 24))
        self.leftPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.leftPlusBtn.setFont(font7)
        self.leftPlusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.leftPlusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.leftPlusBtn, 5, 1, 1, 1)

        self.topMinusBtn = QPushButton(self.page_3)
        self.screenCaptureControls.addButton(self.topMinusBtn)
        self.topMinusBtn.setObjectName(u"topMinusBtn")
        self.topMinusBtn.setMinimumSize(QSize(84, 24))
        self.topMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.topMinusBtn.setFont(font7)
        self.topMinusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.topMinusBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.topMinusBtn, 6, 0, 1, 1)

        self.heightValueLabel = QLineEdit(self.page_3)
        self.heightValueLabel.setObjectName(u"heightValueLabel")
        self.heightValueLabel.setMinimumSize(QSize(84, 25))
        self.heightValueLabel.setMaximumSize(QSize(84, 25))
        self.heightValueLabel.setFont(font8)

        self.gridLayout_6.addWidget(self.heightValueLabel, 3, 3, 1, 1)

        self.leftValueLabel = QLineEdit(self.page_3)
        self.leftValueLabel.setObjectName(u"leftValueLabel")
        self.leftValueLabel.setMinimumSize(QSize(84, 25))
        self.leftValueLabel.setMaximumSize(QSize(84, 25))
        self.leftValueLabel.setFont(font8)

        self.gridLayout_6.addWidget(self.leftValueLabel, 3, 1, 1, 1)

        self.classSelectorFrame = QFrame(self.page_3)
        self.classSelectorFrame.setObjectName(u"classSelectorFrame")
        self.classSelectorFrame.setStyleSheet(u"#classSelectorFrame{\n"
"	max-width: 615px;\n"
"	max-height:500px;\n"
"	min-width: 250px;\n"
"	min-height:500px;\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"}")
        self.classSelectorFrame.setFrameShape(QFrame.StyledPanel)
        self.classSelectorFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.classSelectorFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(10, 0, 5, 0)
        self.enemiesCheckBox = QCheckBox(self.classSelectorFrame)
        self.enemiesCheckBox.setObjectName(u"enemiesCheckBox")
        self.enemiesCheckBox.setStyleSheet(u"#enemiesCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.enemiesCheckBox, 7, 0, 1, 1)

        self.spikePlantedCheckBox = QCheckBox(self.classSelectorFrame)
        self.spikePlantedCheckBox.setObjectName(u"spikePlantedCheckBox")
        self.spikePlantedCheckBox.setStyleSheet(u"#spikePlantedCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.spikePlantedCheckBox, 6, 2, 1, 1)

        self.friendliesDeadCheckBox = QCheckBox(self.classSelectorFrame)
        self.friendliesDeadCheckBox.setObjectName(u"friendliesDeadCheckBox")
        self.friendliesDeadCheckBox.setStyleSheet(u"#friendliesDeadCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.friendliesDeadCheckBox, 7, 2, 1, 1)

        self.enemiesDeadCheckBox = QCheckBox(self.classSelectorFrame)
        self.enemiesDeadCheckBox.setObjectName(u"enemiesDeadCheckBox")
        self.enemiesDeadCheckBox.setStyleSheet(u"#enemiesDeadCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.enemiesDeadCheckBox, 11, 0, 1, 1)

        self.spikeCheckBox = QCheckBox(self.classSelectorFrame)
        self.spikeCheckBox.setObjectName(u"spikeCheckBox")
        self.spikeCheckBox.setStyleSheet(u"#spikeCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.spikeCheckBox, 7, 1, 1, 1)

        self.checkBoxDescriptionLabel = QLabel(self.classSelectorFrame)
        self.checkBoxDescriptionLabel.setObjectName(u"checkBoxDescriptionLabel")
        self.checkBoxDescriptionLabel.setStyleSheet(u"#checkBoxDescriptionLabel{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 350px;\n"
"	max-height: 40px;\n"
"	min-width: 350px;\n"
"	min-height: 40px;\n"
"}")
        self.checkBoxDescriptionLabel.setWordWrap(True)

        self.gridLayout_5.addWidget(self.checkBoxDescriptionLabel, 5, 0, 1, 1)

        self.classesSelectorLabel = QLabel(self.classSelectorFrame)
        self.classesSelectorLabel.setObjectName(u"classesSelectorLabel")
        self.classesSelectorLabel.setStyleSheet(u"#classesSelectorLabel{\n"
"	font: 25pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-height: 50px;\n"
"	min-width: 350px;\n"
"	min-height: 50px;\n"
"}")
        self.classesSelectorLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.classesSelectorLabel, 3, 0, 1, 3)

        self.friendliesCheckBox = QCheckBox(self.classSelectorFrame)
        self.friendliesCheckBox.setObjectName(u"friendliesCheckBox")
        self.friendliesCheckBox.setStyleSheet(u"#friendliesCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.friendliesCheckBox, 6, 1, 1, 1)

        self.lastSeenCheckBox = QCheckBox(self.classSelectorFrame)
        self.lastSeenCheckBox.setObjectName(u"lastSeenCheckBox")
        self.lastSeenCheckBox.setStyleSheet(u"#lastSeenCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.lastSeenCheckBox, 11, 2, 1, 1)

        self.playersCheckBox = QCheckBox(self.classSelectorFrame)
        self.playersCheckBox.setObjectName(u"playersCheckBox")
        self.playersCheckBox.setStyleSheet(u"#playersCheckBox{\n"
"	font: 10pt \"Cascadia Mono\";\n"
"	color: rgb(255, 255, 255);\n"
"	max-width: 150px;\n"
"	max-height: 20px;\n"
"	min-width: 150px;\n"
"	min-height: 20px;\n"
"}")
        self.playersCheckBox.setChecked(True)

        self.gridLayout_5.addWidget(self.playersCheckBox, 6, 0, 1, 1)


        self.gridLayout_6.addWidget(self.classSelectorFrame, 1, 0, 1, 4)

        self.nextBtn = QPushButton(self.page_3)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMinimumSize(QSize(82, 22))
        self.nextBtn.setMaximumSize(QSize(82, 16777215))
        self.nextBtn.setFont(font9)
        self.nextBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextBtn.setStyleSheet(u"QPushButton{\n"
"	font: 10pt \"Cascadia Code\";\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	min-width: 80px;\n"
"	max-width: 80px;\n"
"	min-height: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.nextBtn, 7, 2, 1, 1)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_7 = QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.title = QLabel(self.page_4)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"#title{\n"
"	font: 700 16pt \"Cascadia Code\";\n"
"	color: white;\n"
"	max-height: 40px;\n"
"	min-height: 25px;\n"
"	min-width: 130px;\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.title, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_4)

        self.gridLayout_3.addWidget(self.stackedWidget_2, 0, 3, 4, 1)

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
        self.versionInput = QLineEdit(self.settingsAdjustment)
        self.versionInput.setObjectName(u"versionInput")
        self.versionInput.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.versionInput.sizePolicy().hasHeightForWidth())
        self.versionInput.setSizePolicy(sizePolicy2)
        font10 = QFont()
        font10.setFamilies([u"Cascadia Mono"])
        font10.setPointSize(10)
        font10.setBold(True)
        self.versionInput.setFont(font10)
        self.versionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.versionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.versionInput, 9, 1, 1, 1)

        self.tagInput = QLineEdit(self.settingsAdjustment)
        self.tagInput.setObjectName(u"tagInput")
        sizePolicy2.setHeightForWidth(self.tagInput.sizePolicy().hasHeightForWidth())
        self.tagInput.setSizePolicy(sizePolicy2)
        self.tagInput.setFont(font10)
        self.tagInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tagInput, 1, 1, 1, 1)

        self.puuidLabel = QLabel(self.settingsAdjustment)
        self.puuidLabel.setObjectName(u"puuidLabel")
        self.puuidLabel.setMinimumSize(QSize(0, 30))
        self.puuidLabel.setMaximumSize(QSize(16777215, 30))
        font11 = QFont()
        font11.setFamilies([u"Cascadia Mono ExtraLight"])
        font11.setPointSize(10)
        font11.setItalic(False)
        font11.setUnderline(False)
        font11.setStyleStrategy(QFont.PreferAntialias)
        self.puuidLabel.setFont(font11)
        self.puuidLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.puuidLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.puuidLabel, 5, 0, 1, 1)

        self.saveSettingsBtn = QPushButton(self.settingsAdjustment)
        self.saveSettingsBtn.setObjectName(u"saveSettingsBtn")
        self.saveSettingsBtn.setMinimumSize(QSize(150, 30))
        self.saveSettingsBtn.setMaximumSize(QSize(150, 30))
        font12 = QFont()
        font12.setFamilies([u"Cascadia Mono"])
        font12.setPointSize(10)
        self.saveSettingsBtn.setFont(font12)
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

        self.puuidError = QLabel(self.settingsAdjustment)
        self.puuidError.setObjectName(u"puuidError")
        self.puuidError.setMinimumSize(QSize(130, 15))
        self.puuidError.setMaximumSize(QSize(200, 25))
        font13 = QFont()
        font13.setFamilies([u"Cascadia Mono Light"])
        font13.setItalic(True)
        self.puuidError.setFont(font13)
        self.puuidError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.puuidError, 5, 2, 1, 1)

        self.regionLabel = QLabel(self.settingsAdjustment)
        self.regionLabel.setObjectName(u"regionLabel")
        self.regionLabel.setMinimumSize(QSize(0, 30))
        self.regionLabel.setMaximumSize(QSize(16777215, 30))
        self.regionLabel.setFont(font11)
        self.regionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.regionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.regionLabel, 6, 0, 1, 1)

        self.saveError = QLabel(self.settingsAdjustment)
        self.saveError.setObjectName(u"saveError")
        self.saveError.setMinimumSize(QSize(130, 15))
        self.saveError.setMaximumSize(QSize(200, 25))
        self.saveError.setFont(font13)
        self.saveError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.saveError, 10, 2, 1, 1)

        self.versionLabel = QLabel(self.settingsAdjustment)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMinimumSize(QSize(0, 30))
        self.versionLabel.setMaximumSize(QSize(16777215, 30))
        self.versionLabel.setFont(font11)
        self.versionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.versionLabel, 9, 0, 1, 1)

        self.tagLabel = QLabel(self.settingsAdjustment)
        self.tagLabel.setObjectName(u"tagLabel")
        self.tagLabel.setMinimumSize(QSize(0, 30))
        self.tagLabel.setMaximumSize(QSize(16777215, 30))
        self.tagLabel.setFont(font11)
        self.tagLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tagLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tagLabel, 1, 0, 1, 1)

        self.puuidInput = QLineEdit(self.settingsAdjustment)
        self.puuidInput.setObjectName(u"puuidInput")
        self.puuidInput.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.puuidInput.sizePolicy().hasHeightForWidth())
        self.puuidInput.setSizePolicy(sizePolicy2)
        self.puuidInput.setFont(font10)
        self.puuidInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.puuidInput.setReadOnly(True)

        self.gridLayout.addWidget(self.puuidInput, 5, 1, 1, 1)

        self.usernameInput = QLineEdit(self.settingsAdjustment)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy2.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy2)
        self.usernameInput.setFont(font10)
        self.usernameInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.usernameInput, 0, 1, 1, 1)

        self.tagError = QLabel(self.settingsAdjustment)
        self.tagError.setObjectName(u"tagError")
        self.tagError.setMinimumSize(QSize(130, 15))
        self.tagError.setMaximumSize(QSize(200, 25))
        self.tagError.setFont(font13)
        self.tagError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.tagError, 1, 2, 1, 1)

        self.usernameLabel = QLabel(self.settingsAdjustment)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(0, 30))
        self.usernameLabel.setMaximumSize(QSize(16777215, 30))
        self.usernameLabel.setFont(font11)
        self.usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usernameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameError = QLabel(self.settingsAdjustment)
        self.usernameError.setObjectName(u"usernameError")
        self.usernameError.setMinimumSize(QSize(130, 15))
        self.usernameError.setMaximumSize(QSize(200, 15))
        self.usernameError.setFont(font13)
        self.usernameError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.usernameError, 0, 2, 1, 1)

        self.shardLabel = QLabel(self.settingsAdjustment)
        self.shardLabel.setObjectName(u"shardLabel")
        self.shardLabel.setMinimumSize(QSize(0, 30))
        self.shardLabel.setMaximumSize(QSize(16777215, 30))
        self.shardLabel.setFont(font11)
        self.shardLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.shardLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.shardLabel, 8, 0, 1, 1)

        self.regionInput = QLineEdit(self.settingsAdjustment)
        self.regionInput.setObjectName(u"regionInput")
        self.regionInput.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.regionInput.sizePolicy().hasHeightForWidth())
        self.regionInput.setSizePolicy(sizePolicy2)
        self.regionInput.setFont(font10)
        self.regionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.regionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.regionInput, 6, 1, 1, 1)

        self.shardInput = QLineEdit(self.settingsAdjustment)
        self.shardInput.setObjectName(u"shardInput")
        self.shardInput.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.shardInput.sizePolicy().hasHeightForWidth())
        self.shardInput.setSizePolicy(sizePolicy2)
        self.shardInput.setFont(font10)
        self.shardInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.shardInput.setReadOnly(True)

        self.gridLayout.addWidget(self.shardInput, 8, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.settingsAdjustment)

        self.playerInformation = QFrame(self.accountSettingsPage)
        self.playerInformation.setObjectName(u"playerInformation")
        self.playerInformation.setStyleSheet(u"")
        self.playerInformation.setFrameShape(QFrame.StyledPanel)
        self.playerInformation.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.playerInformation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.eloLabel = QLabel(self.playerInformation)
        self.eloLabel.setObjectName(u"eloLabel")
        self.eloLabel.setMaximumSize(QSize(16777215, 30))
        font14 = QFont()
        font14.setFamilies([u"Cascadia Mono"])
        font14.setPointSize(11)
        self.eloLabel.setFont(font14)
        self.eloLabel.setLayoutDirection(Qt.LeftToRight)
        self.eloLabel.setStyleSheet(u"color: white;")
        self.eloLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eloLabel, 4, 0, 1, 1)

        self.username = QLabel(self.playerInformation)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 30))
        self.username.setFont(font14)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"color: white;")
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.username, 3, 0, 1, 3)

        self.elo = QLabel(self.playerInformation)
        self.elo.setObjectName(u"elo")
        self.elo.setMaximumSize(QSize(16777215, 30))
        self.elo.setFont(font14)
        self.elo.setLayoutDirection(Qt.LeftToRight)
        self.elo.setStyleSheet(u"color: white;")
        self.elo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.elo, 4, 1, 1, 2)

        self.profilePicture = QLabel(self.playerInformation)
        self.profilePicture.setObjectName(u"profilePicture")
        self.profilePicture.setMaximumSize(QSize(250, 250))
        self.profilePicture.setPixmap(QPixmap(u":/images/Vertical_jett.png"))
        self.profilePicture.setScaledContents(True)

        self.gridLayout_2.addWidget(self.profilePicture, 0, 1, 1, 1)

        self.rankLabel = QLabel(self.playerInformation)
        self.rankLabel.setObjectName(u"rankLabel")
        self.rankLabel.setMaximumSize(QSize(16777215, 30))
        self.rankLabel.setFont(font14)
        self.rankLabel.setLayoutDirection(Qt.LeftToRight)
        self.rankLabel.setStyleSheet(u"color: white;")
        self.rankLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rankLabel, 5, 0, 1, 1)

        self.rank = QLabel(self.playerInformation)
        self.rank.setObjectName(u"rank")
        self.rank.setFont(font14)
        self.rank.setLayoutDirection(Qt.LeftToRight)
        self.rank.setStyleSheet(u"color: white;")
        self.rank.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rank, 5, 1, 1, 2)

        self.pushButton = QPushButton(self.playerInformation)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setFont(font12)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(139, 139, 207)\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton, 6, 1, 1, 1)


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
        self.gridLayout_4 = QGridLayout(self.submitBugPageFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pageTitle = QLabel(self.submitBugPageFrame)
        self.pageTitle.setObjectName(u"pageTitle")
        self.pageTitle.setMaximumSize(QSize(16777215, 50))
        self.pageTitle.setFont(font5)
        self.pageTitle.setStyleSheet(u"color: white;")

        self.gridLayout_4.addWidget(self.pageTitle, 0, 0, 1, 4)

        self.reportType = QComboBox(self.submitBugPageFrame)
        self.reportType.addItem("")
        self.reportType.addItem("")
        self.reportType.addItem("")
        self.reportType.setObjectName(u"reportType")
        self.reportType.setMinimumSize(QSize(100, 30))
        self.reportType.setMaximumSize(QSize(400, 30))
        font15 = QFont()
        font15.setFamilies([u"Cascadia Mono"])
        font15.setBold(True)
        self.reportType.setFont(font15)
        self.reportType.setStyleSheet(u"\n"
"#reportType {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(68, 68, 102);\n"
"	padding-left: 5px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"#reportType::drop-down{\n"
"	border:0px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#reportType::down-arrow{\n"
"	image: url(:/assets/images/icons/arrowDown.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"#reportType QListView{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 9px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.reportType, 1, 1, 1, 3)

        self.reportTypeLabel = QLabel(self.submitBugPageFrame)
        self.reportTypeLabel.setObjectName(u"reportTypeLabel")
        self.reportTypeLabel.setMinimumSize(QSize(100, 20))
        self.reportTypeLabel.setMaximumSize(QSize(100, 20))
        font16 = QFont()
        font16.setFamilies([u"Cascadia Mono SemiBold"])
        font16.setPointSize(12)
        font16.setBold(True)
        self.reportTypeLabel.setFont(font16)
        self.reportTypeLabel.setStyleSheet(u"color: white;")

        self.gridLayout_4.addWidget(self.reportTypeLabel, 1, 0, 1, 1)

        self.descriptionLabel = QLabel(self.submitBugPageFrame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setMinimumSize(QSize(115, 20))
        self.descriptionLabel.setMaximumSize(QSize(115, 20))
        self.descriptionLabel.setFont(font16)
        self.descriptionLabel.setStyleSheet(u"color: white;")

        self.gridLayout_4.addWidget(self.descriptionLabel, 3, 0, 1, 1)

        self.reportTitle = QLineEdit(self.submitBugPageFrame)
        self.reportTitle.setObjectName(u"reportTitle")
        self.reportTitle.setMinimumSize(QSize(100, 30))
        self.reportTitle.setMaximumSize(QSize(200, 30))
        self.reportTitle.setFont(font8)
        self.reportTitle.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 68, 102);\n"
"padding-left: 5px;\n"
"padding-right: 20px;\n"
"\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.reportTitle, 2, 1, 1, 1)

        self.reportTitleLabel = QLabel(self.submitBugPageFrame)
        self.reportTitleLabel.setObjectName(u"reportTitleLabel")
        self.reportTitleLabel.setMinimumSize(QSize(100, 20))
        self.reportTitleLabel.setMaximumSize(QSize(100, 20))
        self.reportTitleLabel.setFont(font16)
        self.reportTitleLabel.setStyleSheet(u"color: white;")

        self.gridLayout_4.addWidget(self.reportTitleLabel, 2, 0, 1, 1)

        self.submitReportBtn = QPushButton(self.submitBugPageFrame)
        self.submitReportBtn.setObjectName(u"submitReportBtn")
        self.submitReportBtn.setMinimumSize(QSize(174, 44))
        self.submitReportBtn.setMaximumSize(QSize(174, 30))
        self.submitReportBtn.setFont(font12)
        self.submitReportBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitReportBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 48, 71);\n"
"	border: 2px solid white;\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"	min-width: 170px;\n"
"	max-width: 170px;\n"
"	min-height: 40px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  	background-color: rgb(139, 139, 207);\n"
"	widget-animation-duration: 400;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.submitReportBtn, 6, 2, 1, 1)

        self.descriptionBox = QTextEdit(self.submitBugPageFrame)
        self.descriptionBox.setObjectName(u"descriptionBox")
        self.descriptionBox.setMaximumSize(QSize(520, 230))
        self.descriptionBox.setFont(font8)
        self.descriptionBox.setStyleSheet(u"#descriptionBox{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(68, 68, 102);\n"
"	padding-left: 5px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"#descriptionBox::handle::vertical{\n"
"	min-height:30px;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.descriptionBox.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.descriptionBox.setLineWrapColumnOrWidth(50)

        self.gridLayout_4.addWidget(self.descriptionBox, 5, 0, 1, 4)

        self.descriptionText = QLabel(self.submitBugPageFrame)
        self.descriptionText.setObjectName(u"descriptionText")
        self.descriptionText.setMinimumSize(QSize(0, 30))
        self.descriptionText.setMaximumSize(QSize(520, 30))
        self.descriptionText.setFont(font8)
        self.descriptionText.setStyleSheet(u"color: white;")
        self.descriptionText.setScaledContents(False)
        self.descriptionText.setWordWrap(True)

        self.gridLayout_4.addWidget(self.descriptionText, 4, 0, 1, 4)

        self.descriptionBoxError = QLabel(self.submitBugPageFrame)
        self.descriptionBoxError.setObjectName(u"descriptionBoxError")
        self.descriptionBoxError.setStyleSheet(u"color:red;")

        self.gridLayout_4.addWidget(self.descriptionBoxError, 3, 1, 1, 1)

        self.reportTitleError = QLabel(self.submitBugPageFrame)
        self.reportTitleError.setObjectName(u"reportTitleError")
        self.reportTitleError.setStyleSheet(u"color:red;")

        self.gridLayout_4.addWidget(self.reportTitleError, 2, 2, 1, 1)


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
        QWidget.setTabOrder(self.closeBtn, self.usernameInput)
        QWidget.setTabOrder(self.usernameInput, self.tagInput)
        QWidget.setTabOrder(self.tagInput, self.puuidInput)
        QWidget.setTabOrder(self.puuidInput, self.regionInput)
        QWidget.setTabOrder(self.regionInput, self.shardInput)
        QWidget.setTabOrder(self.shardInput, self.versionInput)
        QWidget.setTabOrder(self.versionInput, self.saveSettingsBtn)
        QWidget.setTabOrder(self.saveSettingsBtn, self.pushButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


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
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.screenCaptureLabel.setText("")
        self.setPolygonBtn.setText(QCoreApplication.translate("MainWindow", u"Set Zone", None))
        self.polygonName.setPlaceholderText("")
        self.createPolygonBtn.setText(QCoreApplication.translate("MainWindow", u"Create Tracking  Zone", None))
        self.polygonLabel.setText("")
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.heightMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Height -", None))
        self.topPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Top +", None))
        self.topValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Top Value", None))
        self.widthValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Width Value", None))
        self.widthMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Width -", None))
        self.previousBtn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.widthPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Width +", None))
        self.leftMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Left -", None))
        self.heightPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Height +", None))
        self.leftPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Left +", None))
        self.topMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Top -", None))
        self.heightValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Height Value", None))
        self.leftValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Left Value", None))
#if QT_CONFIG(tooltip)
        self.enemiesCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(tooltip)
        self.enemiesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enemies", None))
#if QT_CONFIG(tooltip)
        self.spikePlantedCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(tooltip)
        self.spikePlantedCheckBox.setText(QCoreApplication.translate("MainWindow", u"Spike Planted", None))
#if QT_CONFIG(tooltip)
        self.friendliesDeadCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(tooltip)
        self.friendliesDeadCheckBox.setText(QCoreApplication.translate("MainWindow", u"Friendlies Dead", None))
#if QT_CONFIG(tooltip)
        self.enemiesDeadCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(tooltip)
        self.enemiesDeadCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enemies Dead", None))
#if QT_CONFIG(tooltip)
        self.spikeCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(tooltip)
        self.spikeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Spike", None))
        self.checkBoxDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Select Classes you want the model to predict from", None))
        self.classesSelectorLabel.setText(QCoreApplication.translate("MainWindow", u"Classes Selector", None))
#if QT_CONFIG(tooltip)
        self.friendliesCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(tooltip)
        self.friendliesCheckBox.setText(QCoreApplication.translate("MainWindow", u"Friendlies", None))
#if QT_CONFIG(tooltip)
        self.lastSeenCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(tooltip)
        self.lastSeenCheckBox.setText(QCoreApplication.translate("MainWindow", u"Last Seen", None))
#if QT_CONFIG(tooltip)
        self.playersCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(tooltip)
        self.playersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Players", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Label Tracker", None))
#if QT_CONFIG(tooltip)
        self.settingsAdjustment.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.versionInput.setText(QCoreApplication.translate("MainWindow", u"v1", None))
        self.tagInput.setInputMask("")
        self.tagInput.setText("")
        self.tagInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Player Tagline", None))
        self.puuidLabel.setText(QCoreApplication.translate("MainWindow", u"PUUID:", None))
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
        self.puuidError.setText("")
        self.regionLabel.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.saveError.setText("")
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.tagLabel.setText(QCoreApplication.translate("MainWindow", u"Tag Line: #", None))
        self.puuidInput.setText("")
        self.puuidInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Generated after Saving", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Player Username", None))
        self.tagError.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.usernameError.setText("")
        self.shardLabel.setText(QCoreApplication.translate("MainWindow", u"Shard:", None))
        self.regionInput.setText(QCoreApplication.translate("MainWindow", u"eu", None))
        self.shardInput.setText(QCoreApplication.translate("MainWindow", u"eu", None))
        self.eloLabel.setText(QCoreApplication.translate("MainWindow", u"ELO (Estimate):", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username#Tagline", None))
        self.elo.setText("")
        self.profilePicture.setText("")
        self.rankLabel.setText(QCoreApplication.translate("MainWindow", u"Current Rank:", None))
        self.rank.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Profile", None))
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Issue Reporter", None))
        self.reportType.setItemText(0, QCoreApplication.translate("MainWindow", u"Bug Report", None))
        self.reportType.setItemText(1, QCoreApplication.translate("MainWindow", u"Feature Request", None))
        self.reportType.setItemText(2, QCoreApplication.translate("MainWindow", u"Performance Issue", None))

        self.reportTypeLabel.setText(QCoreApplication.translate("MainWindow", u"This is a", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Description<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.reportTitleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Title<span style=\" color:#ff0000;\">*</span></p></body></html>", None))
        self.submitReportBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.descriptionBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe Steps to replicate or what feature you want!", None))
        self.descriptionText.setText(QCoreApplication.translate("MainWindow", u"If applicable how would I replicate/reproduce what you did to have the same problem?", None))
        self.descriptionBoxError.setText("")
        self.reportTitleError.setText("")
    # retranslateUi

