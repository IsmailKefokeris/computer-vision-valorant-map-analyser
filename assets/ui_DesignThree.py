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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
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
        self.leftPlusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls = QButtonGroup(MainWindow)
        self.screenCaptureControls.setObjectName(u"screenCaptureControls")
        self.screenCaptureControls.addButton(self.leftPlusBtn)
        self.leftPlusBtn.setObjectName(u"leftPlusBtn")
        self.leftPlusBtn.setMinimumSize(QSize(84, 24))
        self.leftPlusBtn.setMaximumSize(QSize(84, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Cascadia Mono SemiBold"])
        font5.setPointSize(12)
        self.leftPlusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.leftPlusBtn, 2, 3, 1, 1)

        self.heightMinusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.heightMinusBtn)
        self.heightMinusBtn.setObjectName(u"heightMinusBtn")
        self.heightMinusBtn.setMinimumSize(QSize(84, 24))
        self.heightMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.heightMinusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.heightMinusBtn, 4, 5, 1, 1)

        self.topPlusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.topPlusBtn)
        self.topPlusBtn.setObjectName(u"topPlusBtn")
        self.topPlusBtn.setMinimumSize(QSize(84, 24))
        self.topPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.topPlusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.topPlusBtn, 2, 2, 1, 1)

        self.heightValueLabel = QLineEdit(self.mainPage)
        self.heightValueLabel.setObjectName(u"heightValueLabel")
        self.heightValueLabel.setMinimumSize(QSize(84, 25))
        self.heightValueLabel.setMaximumSize(QSize(84, 25))
        font6 = QFont()
        font6.setFamilies([u"Cascadia Mono"])
        self.heightValueLabel.setFont(font6)

        self.gridLayout_3.addWidget(self.heightValueLabel, 1, 5, 1, 1)

        self.leftValueLabel = QLineEdit(self.mainPage)
        self.leftValueLabel.setObjectName(u"leftValueLabel")
        self.leftValueLabel.setMinimumSize(QSize(84, 25))
        self.leftValueLabel.setMaximumSize(QSize(84, 25))
        self.leftValueLabel.setFont(font6)

        self.gridLayout_3.addWidget(self.leftValueLabel, 1, 3, 1, 1)

        self.stopBtn = QPushButton(self.mainPage)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(174, 44))
        self.stopBtn.setMaximumSize(QSize(174, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Cascadia Mono SemiBold"])
        font7.setPointSize(20)
        self.stopBtn.setFont(font7)
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

        self.gridLayout_3.addWidget(self.stopBtn, 2, 1, 1, 1)

        self.widthPlusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.widthPlusBtn)
        self.widthPlusBtn.setObjectName(u"widthPlusBtn")
        self.widthPlusBtn.setMinimumSize(QSize(84, 24))
        self.widthPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.widthPlusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.widthPlusBtn, 2, 4, 1, 1)

        self.widthValueLabel = QLineEdit(self.mainPage)
        self.widthValueLabel.setObjectName(u"widthValueLabel")
        self.widthValueLabel.setMinimumSize(QSize(84, 25))
        self.widthValueLabel.setMaximumSize(QSize(84, 25))
        self.widthValueLabel.setFont(font6)

        self.gridLayout_3.addWidget(self.widthValueLabel, 1, 4, 1, 1)

        self.startBtn = QPushButton(self.mainPage)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(174, 44))
        self.startBtn.setMaximumSize(QSize(174, 16777215))
        self.startBtn.setFont(font7)
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

        self.gridLayout_3.addWidget(self.startBtn, 2, 0, 1, 1)

        self.leftMinusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.leftMinusBtn)
        self.leftMinusBtn.setObjectName(u"leftMinusBtn")
        self.leftMinusBtn.setMinimumSize(QSize(84, 24))
        self.leftMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.leftMinusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.leftMinusBtn, 4, 3, 1, 1)

        self.widthMinusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.widthMinusBtn)
        self.widthMinusBtn.setObjectName(u"widthMinusBtn")
        self.widthMinusBtn.setMinimumSize(QSize(84, 24))
        self.widthMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.widthMinusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.widthMinusBtn, 4, 4, 1, 1)

        self.topMinusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.topMinusBtn)
        self.topMinusBtn.setObjectName(u"topMinusBtn")
        self.topMinusBtn.setMinimumSize(QSize(84, 24))
        self.topMinusBtn.setMaximumSize(QSize(84, 16777215))
        self.topMinusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.topMinusBtn, 4, 2, 1, 1)

        self.topValueLabel = QLineEdit(self.mainPage)
        self.topValueLabel.setObjectName(u"topValueLabel")
        self.topValueLabel.setMinimumSize(QSize(84, 25))
        self.topValueLabel.setMaximumSize(QSize(84, 25))
        self.topValueLabel.setFont(font6)

        self.gridLayout_3.addWidget(self.topValueLabel, 1, 2, 1, 1)

        self.screenCaptureLabel = QLabel(self.mainPage)
        self.screenCaptureLabel.setObjectName(u"screenCaptureLabel")
        self.screenCaptureLabel.setMinimumSize(QSize(500, 500))
        self.screenCaptureLabel.setMaximumSize(QSize(500, 500))
        self.screenCaptureLabel.setTextFormat(Qt.MarkdownText)
        self.screenCaptureLabel.setPixmap(QPixmap(u":/assets/images/placeholder.PNG"))
        self.screenCaptureLabel.setScaledContents(True)

        self.gridLayout_3.addWidget(self.screenCaptureLabel, 0, 0, 1, 2)

        self.heightPlusBtn = QPushButton(self.mainPage)
        self.screenCaptureControls.addButton(self.heightPlusBtn)
        self.heightPlusBtn.setObjectName(u"heightPlusBtn")
        self.heightPlusBtn.setMinimumSize(QSize(84, 24))
        self.heightPlusBtn.setMaximumSize(QSize(84, 16777215))
        self.heightPlusBtn.setFont(font5)
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

        self.gridLayout_3.addWidget(self.heightPlusBtn, 2, 5, 1, 1)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.versionInput.sizePolicy().hasHeightForWidth())
        self.versionInput.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setFamilies([u"Cascadia Mono"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.versionInput.setFont(font8)
        self.versionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.versionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.versionInput, 9, 1, 1, 1)

        self.tagInput = QLineEdit(self.settingsAdjustment)
        self.tagInput.setObjectName(u"tagInput")
        sizePolicy1.setHeightForWidth(self.tagInput.sizePolicy().hasHeightForWidth())
        self.tagInput.setSizePolicy(sizePolicy1)
        self.tagInput.setFont(font8)
        self.tagInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tagInput, 1, 1, 1, 1)

        self.puuidLabel = QLabel(self.settingsAdjustment)
        self.puuidLabel.setObjectName(u"puuidLabel")
        self.puuidLabel.setMinimumSize(QSize(0, 30))
        self.puuidLabel.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Cascadia Mono ExtraLight"])
        font9.setPointSize(10)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.puuidLabel.setFont(font9)
        self.puuidLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.puuidLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.puuidLabel, 5, 0, 1, 1)

        self.saveSettingsBtn = QPushButton(self.settingsAdjustment)
        self.saveSettingsBtn.setObjectName(u"saveSettingsBtn")
        self.saveSettingsBtn.setMinimumSize(QSize(150, 30))
        self.saveSettingsBtn.setMaximumSize(QSize(150, 30))
        font10 = QFont()
        font10.setFamilies([u"Cascadia Mono"])
        font10.setPointSize(10)
        self.saveSettingsBtn.setFont(font10)
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
        font11 = QFont()
        font11.setFamilies([u"Cascadia Mono Light"])
        font11.setItalic(True)
        self.puuidError.setFont(font11)
        self.puuidError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.puuidError, 5, 2, 1, 1)

        self.regionLabel = QLabel(self.settingsAdjustment)
        self.regionLabel.setObjectName(u"regionLabel")
        self.regionLabel.setMinimumSize(QSize(0, 30))
        self.regionLabel.setMaximumSize(QSize(16777215, 30))
        self.regionLabel.setFont(font9)
        self.regionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.regionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.regionLabel, 6, 0, 1, 1)

        self.saveError = QLabel(self.settingsAdjustment)
        self.saveError.setObjectName(u"saveError")
        self.saveError.setMinimumSize(QSize(130, 15))
        self.saveError.setMaximumSize(QSize(200, 25))
        self.saveError.setFont(font11)
        self.saveError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.saveError, 10, 2, 1, 1)

        self.versionLabel = QLabel(self.settingsAdjustment)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMinimumSize(QSize(0, 30))
        self.versionLabel.setMaximumSize(QSize(16777215, 30))
        self.versionLabel.setFont(font9)
        self.versionLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.versionLabel, 9, 0, 1, 1)

        self.tagLabel = QLabel(self.settingsAdjustment)
        self.tagLabel.setObjectName(u"tagLabel")
        self.tagLabel.setMinimumSize(QSize(0, 30))
        self.tagLabel.setMaximumSize(QSize(16777215, 30))
        self.tagLabel.setFont(font9)
        self.tagLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tagLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tagLabel, 1, 0, 1, 1)

        self.puuidInput = QLineEdit(self.settingsAdjustment)
        self.puuidInput.setObjectName(u"puuidInput")
        self.puuidInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.puuidInput.sizePolicy().hasHeightForWidth())
        self.puuidInput.setSizePolicy(sizePolicy1)
        self.puuidInput.setFont(font8)
        self.puuidInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.puuidInput.setReadOnly(True)

        self.gridLayout.addWidget(self.puuidInput, 5, 1, 1, 1)

        self.usernameInput = QLineEdit(self.settingsAdjustment)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy1.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy1)
        self.usernameInput.setFont(font8)
        self.usernameInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.usernameInput, 0, 1, 1, 1)

        self.tagError = QLabel(self.settingsAdjustment)
        self.tagError.setObjectName(u"tagError")
        self.tagError.setMinimumSize(QSize(130, 15))
        self.tagError.setMaximumSize(QSize(200, 25))
        self.tagError.setFont(font11)
        self.tagError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.tagError, 1, 2, 1, 1)

        self.usernameLabel = QLabel(self.settingsAdjustment)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(0, 30))
        self.usernameLabel.setMaximumSize(QSize(16777215, 30))
        self.usernameLabel.setFont(font9)
        self.usernameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usernameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameError = QLabel(self.settingsAdjustment)
        self.usernameError.setObjectName(u"usernameError")
        self.usernameError.setMinimumSize(QSize(130, 15))
        self.usernameError.setMaximumSize(QSize(200, 15))
        self.usernameError.setFont(font11)
        self.usernameError.setStyleSheet(u"color: red;")

        self.gridLayout.addWidget(self.usernameError, 0, 2, 1, 1)

        self.shardLabel = QLabel(self.settingsAdjustment)
        self.shardLabel.setObjectName(u"shardLabel")
        self.shardLabel.setMinimumSize(QSize(0, 30))
        self.shardLabel.setMaximumSize(QSize(16777215, 30))
        self.shardLabel.setFont(font9)
        self.shardLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.shardLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.shardLabel, 8, 0, 1, 1)

        self.regionInput = QLineEdit(self.settingsAdjustment)
        self.regionInput.setObjectName(u"regionInput")
        self.regionInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.regionInput.sizePolicy().hasHeightForWidth())
        self.regionInput.setSizePolicy(sizePolicy1)
        self.regionInput.setFont(font8)
        self.regionInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.regionInput.setReadOnly(True)

        self.gridLayout.addWidget(self.regionInput, 6, 1, 1, 1)

        self.shardInput = QLineEdit(self.settingsAdjustment)
        self.shardInput.setObjectName(u"shardInput")
        self.shardInput.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.shardInput.sizePolicy().hasHeightForWidth())
        self.shardInput.setSizePolicy(sizePolicy1)
        self.shardInput.setFont(font8)
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
        font12 = QFont()
        font12.setFamilies([u"Cascadia Mono"])
        font12.setPointSize(11)
        self.eloLabel.setFont(font12)
        self.eloLabel.setLayoutDirection(Qt.LeftToRight)
        self.eloLabel.setStyleSheet(u"color: white;")
        self.eloLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eloLabel, 4, 0, 1, 1)

        self.username = QLabel(self.playerInformation)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 30))
        self.username.setFont(font12)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"color: white;")
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.username, 3, 0, 1, 3)

        self.elo = QLabel(self.playerInformation)
        self.elo.setObjectName(u"elo")
        self.elo.setMaximumSize(QSize(16777215, 30))
        self.elo.setFont(font12)
        self.elo.setLayoutDirection(Qt.LeftToRight)
        self.elo.setStyleSheet(u"color: white;")
        self.elo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.elo, 4, 1, 1, 2)

        self.profilePicture = QLabel(self.playerInformation)
        self.profilePicture.setObjectName(u"profilePicture")
        self.profilePicture.setMaximumSize(QSize(250, 250))
        self.profilePicture.setPixmap(QPixmap(u":/assets/images/Vertical_jett.png"))
        self.profilePicture.setScaledContents(True)

        self.gridLayout_2.addWidget(self.profilePicture, 0, 1, 1, 1)

        self.rankLabel = QLabel(self.playerInformation)
        self.rankLabel.setObjectName(u"rankLabel")
        self.rankLabel.setMaximumSize(QSize(16777215, 30))
        self.rankLabel.setFont(font12)
        self.rankLabel.setLayoutDirection(Qt.LeftToRight)
        self.rankLabel.setStyleSheet(u"color: white;")
        self.rankLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rankLabel, 5, 0, 1, 1)

        self.rank = QLabel(self.playerInformation)
        self.rank.setObjectName(u"rank")
        self.rank.setFont(font12)
        self.rank.setLayoutDirection(Qt.LeftToRight)
        self.rank.setStyleSheet(u"color: white;")
        self.rank.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rank, 5, 1, 1, 2)

        self.pushButton = QPushButton(self.playerInformation)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setFont(font10)
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
        self.leftPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Left +", None))
        self.heightMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Height -", None))
        self.topPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Top +", None))
        self.heightValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Height Value", None))
        self.leftValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Left Value", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.widthPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Width +", None))
        self.widthValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Width Value", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.leftMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Left -", None))
        self.widthMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Width -", None))
        self.topMinusBtn.setText(QCoreApplication.translate("MainWindow", u"Top -", None))
        self.topValueLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Top Value", None))
        self.screenCaptureLabel.setText("")
        self.heightPlusBtn.setText(QCoreApplication.translate("MainWindow", u"Height +", None))
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
    # retranslateUi

