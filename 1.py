# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QTextBrowser,
    QToolButton, QWidget)

from qfluentwidgets import PushButton
import AI_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 841)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 630, 431, 101))
        self.textBrowser.setStyleSheet(u"background-color: rgb(245, 244, 246);\n"
"border:1px solid;\n"
"border-color: rgb(206, 206, 206);\n"
"border-radius:14px;")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-5, 51, 481, 521))
        font1 = QFont()
        font1.setFamilies([u"\u7231\u5947\u827a\u9ed1\u4f53 Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.listView.setFont(font1)
        self.listView.setStyleSheet(u"border:1px solid;\n"
"border-color: rgb(232, 232, 232);")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 10, 141, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pdf = QPushButton(self.layoutWidget)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setEnabled(True)
        self.pdf.setMaximumSize(QSize(50, 28))
        self.pdf.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/pdf.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdf.setIcon(icon)
        self.pdf.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pdf)

        self.rocket = QPushButton(self.layoutWidget)
        self.rocket.setObjectName(u"rocket")
        self.rocket.setEnabled(True)
        self.rocket.setMaximumSize(QSize(50, 29))
        self.rocket.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u706b\u7bad.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rocket.setIcon(icon1)
        self.rocket.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.rocket)

        self.outlog = QPushButton(self.layoutWidget)
        self.outlog.setObjectName(u"outlog")
        self.outlog.setEnabled(True)
        self.outlog.setMaximumSize(QSize(50, 28))
        self.outlog.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u9000\u51fa.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.outlog.setIcon(icon2)
        self.outlog.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.outlog)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 161, 31))
        self.frame.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"\n"
"border:0px solid red;\n"
"border-radius:14px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(80, 0, 81, 28))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(131, 93, 255);\n"
"\n"
"border:0px solid red;\n"
"border-radius:14px;")
        icon3 = QIcon()
        icon3.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u6c14\u6ce1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 81, 28))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"color: rgb(166, 166, 166);\n"
"\n"
"border:0px solid red;\n"
"border-radius:14px;")
        icon4 = QIcon()
        icon4.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u968f\u673a\u7528\u6237.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 750, 471, 121))
        self.frame_3.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.danao = PushButton(self.frame_3)
        self.danao.setObjectName(u"danao")
        self.danao.setGeometry(QRect(20, 11, 40, 51))
        self.danao.setMinimumSize(QSize(40, 40))
        self.danao.setMaximumSize(QSize(40, 16777215))
        self.danao.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon5 = QIcon()
        icon5.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u667a\u6167\u5927\u8111.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.danao.setIcon(icon5)
        self.danao.setIconSize(QSize(40, 40))
        self.layoutWidget1 = QWidget(self.frame_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(360, 15, 84, 42))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.layoutWidget1)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(40, 40))
        self.toolButton.setMaximumSize(QSize(40, 40))
        self.toolButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        icon6 = QIcon()
        icon6.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u8bbe\u7f6e.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QSize(22, 22))

        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"color: rgb(44, 65, 255);\n"
"\n"
"border:0px solid red;\n"
"border-radius:14px;\n"
"")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 431, 61))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 590, 241, 31))
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_7 = QPushButton(self.splitter)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(131, 93, 255);\n"
"\n"
"border:0px solid red;\n"
"border-radius:14px;")
        icon7 = QIcon()
        icon7.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u6e05\u9664\u6570\u636e\u5e93.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.splitter.addWidget(self.pushButton_7)
        self.pushButton_8 = QPushButton(self.splitter)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"font: 75 9pt \"\u7b49\u7ebf\";\n"
"border:0px solid red;\n"
"border-radius:14px;")
        icon8 = QIcon()
        icon8.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u63d0\u793a.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.splitter.addWidget(self.pushButton_8)
        self.pushButton_9 = QPushButton(self.splitter)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"font: 75 9pt \"\u7b49\u7ebf\";\n"
"border:0px solid red;\n"
"border-radius:14px;")
        icon9 = QIcon()
        icon9.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u4efb\u52a1\u8fdb\u7a0b.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.splitter.addWidget(self.pushButton_9)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(402, 700, 31, 28))
        self.pushButton_2.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon10 = QIcon()
        icon10.addFile(u":/\u5c0f\u56fe\u6807/AI\u8d44\u6e90/\u53d1\u9001.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI\u5bf9\u8bdd", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ffffff;\">1</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bababa;\"> </span><span style=\" font-size:11pt; color:#bababa;\">\u8f93\u5165\u6d88\u606f...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#bababa;\"><br /></p>\n"
"<p style=\"-qt-paragraph-ty"
                        "pe:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#bababa;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bababa;\"> 0/2000</span></p></body></html>", None))
        self.pdf.setText("")
        self.rocket.setText("")
        self.outlog.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u804a\u5929", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u95ee", None))
        self.danao.setText("")
        self.toolButton.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">ChitChat\uff1aSidebar\u56e2\u961f\u7ed9\u60a8\u5f00\u53d1\u7684ChatGPT IOS app\uff01</span></p><p><span style=\" font-size:9pt;\">\u5feb\u6765\u8bd5\u8bd5\u5427\uff01</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u804a\u5929", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u804a\u5929\u8bb0\u5f55", None))
        self.pushButton_2.setText("")
    # retranslateUi

