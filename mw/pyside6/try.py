# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'try.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import TextEdit
import copyask_icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 715)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")
        self.up = QWidget(Form)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(0, 0, 521, 71))
        self.horizontalLayoutWidget = QWidget(self.up)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 6, 481, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cebianlan = QPushButton(self.horizontalLayoutWidget)
        self.cebianlan.setObjectName(u"cebianlan")
        self.cebianlan.setMinimumSize(QSize(30, 30))
        self.cebianlan.setMaximumSize(QSize(30, 30))
        self.cebianlan.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(131, 93, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")
        icon = QIcon()
        icon.addFile(u":/icon/AI\u8d44\u6e90/\u5217\u8868.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cebianlan.setIcon(icon)
        self.cebianlan.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.cebianlan)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(131, 93, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/AI\u8d44\u6e90/\u56fe\u9489.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"color: rgb(131, 93, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/AI\u8d44\u6e90/s-\u9519\u8bef-\u5173\u95ed.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.line = QFrame(self.up)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-20, 63, 550, 1))
        self.line.setMinimumSize(QSize(550, 0))
        self.line.setMaximumSize(QSize(400, 1))
        self.line.setStyleSheet(u"\n"
"background-color: rgb(195, 195, 195);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.mid = QFrame(Form)
        self.mid.setObjectName(u"mid")
        self.mid.setGeometry(QRect(-10, 64, 521, 521))
        self.mid.setFrameShape(QFrame.StyledPanel)
        self.mid.setFrameShadow(QFrame.Raised)
        self.down = QFrame(Form)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(-1, 554, 521, 161))
        self.down.setFrameShape(QFrame.StyledPanel)
        self.down.setFrameShadow(QFrame.Raised)
        self.line_2 = QFrame(self.down)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 0, 550, 1))
        self.line_2.setMinimumSize(QSize(550, 0))
        self.line_2.setMaximumSize(QSize(400, 1))
        self.line_2.setStyleSheet(u"\n"
"background-color: rgb(195, 195, 195);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.textEdit = TextEdit(self.down)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(14, 47, 490, 100))
        self.textEdit.setMinimumSize(QSize(490, 100))
        self.textEdit.setMaximumSize(QSize(490, 100))
        self.textEdit.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"color: rgb(131, 93, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")
        self.widget = QWidget(self.down)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(5, 4, 501, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icon/AI\u8d44\u6e90/\u5bf9\u8bdd\u6846.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(60, 28))
        self.pushButton_4.setMaximumSize(QSize(60, 28))
        self.pushButton_4.setStyleSheet(u"\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"border-radius:8%;")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cebianlan.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u663e\u793a\u6700\u957f\u957f\u5ea6...", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u804a\u5929\u8bb0\u5f55", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QWidget()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    # MainWindow = QtWidgets.QWidget()        # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Form()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec())  # 使用exit()或者点击关闭按钮退出QApplication