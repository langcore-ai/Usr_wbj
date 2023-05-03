# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ai.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import RoundMenu, setTheme, Theme


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 841)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 630, 431, 101))
        self.textBrowser.setStyleSheet("background-color: rgb(245, 244, 246);\n"
                                       "border:1px solid;\n"
                                       "border-color: rgb(206, 206, 206);\n"
                                       "border-radius:14px;")
        self.textBrowser.setObjectName("textBrowser")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-5, 51, 481, 521))
        font = QtGui.QFont()
        font.setFamily("爱奇艺黑体 Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listView.setFont(font)
        self.listView.setStyleSheet("border:1px solid;\n"
                                    "border-color: rgb(232, 232, 232);")
        self.listView.setObjectName("listView")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 10, 141, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pdf = QtWidgets.QPushButton(self.layoutWidget)
        self.pdf.setEnabled(True)
        self.pdf.setMaximumSize(QtCore.QSize(50, 28))
        self.pdf.setStyleSheet("border:none;\n"
                               "background-color: rgba(255, 255, 255, 0);")
        self.pdf.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/小图标/AI资源/pdf.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pdf.setIcon(icon)
        self.pdf.setIconSize(QtCore.QSize(25, 25))
        self.pdf.setObjectName("pdf")
        self.horizontalLayout.addWidget(self.pdf)
        self.rocket = QtWidgets.QPushButton(self.layoutWidget)
        self.rocket.setEnabled(True)
        self.rocket.setMaximumSize(QtCore.QSize(50, 29))
        self.rocket.setStyleSheet("border:none;\n"
                                  "background-color: rgba(255, 255, 255, 0);")
        self.rocket.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/小图标/AI资源/火箭.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rocket.setIcon(icon1)
        self.rocket.setIconSize(QtCore.QSize(25, 25))
        self.rocket.setObjectName("rocket")
        self.horizontalLayout.addWidget(self.rocket)
        self.outlog = QtWidgets.QPushButton(self.layoutWidget)
        self.outlog.setEnabled(True)
        self.outlog.setMaximumSize(QtCore.QSize(50, 28))
        self.outlog.setStyleSheet("border:none;\n"
                                  "background-color: rgba(255, 255, 255, 0);")
        self.outlog.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/小图标/AI资源/退出.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.outlog.setIcon(icon2)
        self.outlog.setIconSize(QtCore.QSize(25, 25))
        self.outlog.setObjectName("outlog")
        self.horizontalLayout.addWidget(self.outlog)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                 "\n"
                                 "border:0px solid red;\n"
                                 "border-radius:14px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 0, 81, 28))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "color: rgb(131, 93, 255);\n"
                                        "\n"
                                        "border:0px solid red;\n"
                                        "border-radius:14px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/小图标/AI资源/气泡.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                        "color: rgb(166, 166, 166);\n"
                                        "\n"
                                        "border:0px solid red;\n"
                                        "border-radius:14px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/小图标/AI资源/随机用户.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 750, 471, 121))
        self.frame_3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.danao = PushButton(self.frame_3)
        self.danao.setGeometry(QtCore.QRect(20, 11, 51, 51))
        self.danao.setStyleSheet("border:none;\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.danao.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/小图标/AI资源/智慧大脑.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.danao.setIcon(icon5)
        self.danao.setIconSize(QtCore.QSize(40, 40))
        self.danao.setObjectName("danao")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 15, 84, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget1)
        self.toolButton.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-radius:20px;")
        self.toolButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/小图标/AI资源/设置.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QtCore.QSize(22, 22))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(44, 65, 255);\n"
                                      "\n"
                                      "border:0px solid red;\n"
                                      "border-radius:14px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 431, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "border-radius: 10px;\n"
                                 "background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
                                 "border: 1px outset rgb(153, 117, 219)")
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 590, 241, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_7.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "color: rgb(131, 93, 255);\n"
                                        "\n"
                                        "border:0px solid red;\n"
                                        "border-radius:14px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/小图标/AI资源/清除数据库.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_8.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                        "font: 75 9pt \"等线\";\n"
                                        "border:0px solid red;\n"
                                        "border-radius:14px;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/小图标/AI资源/提示.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_9.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                        "font: 75 9pt \"等线\";\n"
                                        "border:0px solid red;\n"
                                        "border-radius:14px;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/小图标/AI资源/任务进程.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(402, 700, 31, 28))
        self.pushButton_2.setStyleSheet("border:none;\n"
                                        "background-color: rgba(255, 255, 255, 0);")
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/小图标/AI资源/发送.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def contextMenuEvent(self, e):
        menu = RoundMenu(parent=self)

        # add actions
        menu.addAction(QAction(FIF.COPY.icon(), 'Copy'))
        menu.addAction(QAction(FIF.CUT.icon(), 'Cut'))

        # add sub menu
        submenu = RoundMenu("Add to", self)
        submenu.setIcon(FIF.ADD.icon())
        submenu.addActions([
            QAction(FIF.VIDEO.icon(), 'Video'),
            QAction(FIF.MUSIC.icon(), 'Music'),
        ])
        menu.addMenu(submenu)

        # add actions
        menu.addActions([
            QAction(FIF.PASTE.icon(), 'Paste'),
            QAction(FIF.CANCEL.icon(), 'Undo')
        ])

        # add separator
        menu.addSeparator()
        menu.addAction(QAction(f'Select all'))

        # insert actions
        menu.insertAction(
            menu.menuActions()[-1], QAction(FIF.SETTING.icon(), 'Settings'))
        menu.insertActions(
            menu.menuActions()[-1],
            [QAction(FIF.HELP.icon(), 'Help'), QAction(FIF.FEEDBACK.icon(), 'Feedback')]
        )

        # show menu
        menu.exec(e.globalPos(), ani=True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI对话"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ffffff;\">1</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bababa;\"> </span><span style=\" font-size:11pt; color:#bababa;\">输入消息...</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#bababa;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#bababa;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bababa;\"> 0/2000</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "聊天"))
        self.pushButton_4.setText(_translate("MainWindow", "提问"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:9pt;\">ChitChat：Sidebar团队给您开发的ChatGPT IOS app！</span></p><p><span style=\" font-size:9pt;\">快来试试吧！</span></p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "新聊天"))
        self.pushButton_8.setText(_translate("MainWindow", "提示"))
        self.pushButton_9.setText(_translate("MainWindow", "聊天记录"))


from qfluentwidgets import PushButton, RoundMenu
import AI_rc
from qfluentwidgets import PushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())