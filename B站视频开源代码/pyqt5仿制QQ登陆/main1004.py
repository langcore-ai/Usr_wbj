# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1004.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(279, 342)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("QFrame{\n"
"    border:none;\n"
"    background-color: rgb(234, 237, 239);\n"
"border-radius:5px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setMinimumSize(QtCore.QSize(255, 318))
        self.frame.setMaximumSize(QtCore.QSize(255, 318))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 6, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(12, 12))
        self.pushButton_5.setMaximumSize(QtCore.QSize(12, 12))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(232, 59, 35);\n"
"}\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        self.toolButton_6.setStyleSheet("border:none;\n"
"")
        self.toolButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttom/img/buttom/二维码_two-dimensional-code-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_4.addWidget(self.toolButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.widget_2 = QtWidgets.QWidget(self.frame_3)
        self.widget_2.setMinimumSize(QtCore.QSize(131, 131))
        self.widget_2.setMaximumSize(QtCore.QSize(131, 131))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 110, 16, 16))
        self.pushButton_7.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(35, 158, 33);\n"
"border:1px solid rgb(113, 255, 124);\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"}\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(7, 0, 120, 120))
        self.widget.setMinimumSize(QtCore.QSize(120, 120))
        self.widget.setMaximumSize(QtCore.QSize(120, 120))
        self.widget.setStyleSheet("\n"
"\n"
"QWidget{\n"
"    image: url(:/png/img/svg/篮球.png);\n"
"border:1px solid rgba(0, 0, 0,20);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:60px;\n"
"}\n"
"QWidget:hover {\n"
"border:1px solid rgb(79, 209, 255);\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.pushButton_7.raise_()
        self.horizontalLayout_3.addWidget(self.widget_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 24)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(193, 193, 193,150);\n"
"border-bottom:1px solid rgba(0, 0, 0,40);\n"
"padding:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(193, 193, 193,150);\n"
"border-bottom:1px solid rgba(0, 0, 0,40);\n"
"padding:8px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setMinimumSize(QtCore.QSize(24, 0))
        self.toolButton.setStyleSheet("QToolButton{\n"
"border:none\n"
"}\n"
"\n"
"\n"
"QToolButton:hover {\n"
"    padding:3px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    padding:0px;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttom/img/buttom/下_down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        spacerItem7 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 0))
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_14.setMaximumSize(QtCore.QSize(16777215, 32))
        self.pushButton_14.setStyleSheet("border:none;\n"
"color: rgba(0, 0, 0, 158);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_15.setMaximumSize(QtCore.QSize(16777215, 32))
        self.pushButton_15.setStyleSheet("border:none;\n"
"color: rgba(0, 0, 0, 158);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_4.addWidget(self.pushButton_15)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_8.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入账号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "输入密码"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.radioButton.setText(_translate("MainWindow", "记住密码"))
        self.radioButton_2.setText(_translate("MainWindow", "自动登录"))
        self.pushButton_14.setText(_translate("MainWindow", "忘记密码"))
        self.pushButton_15.setText(_translate("MainWindow", "注册账号"))
import resources_rc
