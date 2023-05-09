# coding:utf-8
import sys

from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QTextOption
from PySide6.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel, QWidget, QTextBrowser

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, TextEdit)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar
from typing import re

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QPainterPath, QPen, QTextOption,
                           QFontMetrics, QAbstractTextDocumentLayout, QTextDocument)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QTextEdit, QScrollArea, QTextBrowser)
from nltk.inference.discourse import spacer

from qfluentwidgets import (PushButton, TextEdit, ToolButton)
import qtqtq_rc


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 隐藏边框
        self.setupUi(self)

        self.toolButton_3.clicked.connect(QApplication.quit)
        self.pushButton_2.clicked.connect(self.sendMessage)
        self.first_message = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._dragging:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor("#ffffff")))
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.addRoundedRect(self.contentsRect(), 6, 6)
        painter.drawPath(path)

    # 向滚动窗口加入信息
    def sendMessage(self):
        message = self.textEdit.toPlainText()
        if message:
            if self.first_message:  # 新增：如果是第一次发送消息
                self.verticalLayout_3.addStretch()  # 新增：添加一个可扩展的垂直间距器
                self.first_message = False  # 新增：设置first_message为False，以便不再重复添加可扩展的间距器
            chat_bubble = ChatBubbleWidget(message)
            self.verticalLayout_3.addSpacing(20)  # 在布局中添加20px的垂直间距
            self.verticalLayout_3.addWidget(chat_bubble)
            self.textEdit.clear()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(546, 945)
        Form.setMinimumSize(QSize(546, 908))

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(Form)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setMinimumSize(QSize(546, 70))
        self.gridLayout = QGridLayout(self.top_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.r = QWidget(self.top_widget)
        self.r.setObjectName(u"r")
        self.r.setMinimumSize(QSize(546, 69))
        self.horizontalLayout_5 = QHBoxLayout(self.r)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top_left = QWidget(self.r)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(58, 36))
        self.top_left.setMaximumSize(QSize(58, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.top_left)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.toolButton = ToolButton(self.top_left)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(36, 36))
        #         self.toolButton.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
        # "border:0px solid red;\n"
        # "border-radius:8px;")
        icon = QIcon()
        icon.addFile(u":/icon/test/\u7f16\u7ec4 10.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.horizontalLayout_5.addWidget(self.top_left)

        self.horizontalSpacer_8 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.label_2 = QLabel(self.r)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(198, 26))
        font = QFont()
        font.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 75 18pt \"\u601d\u6e90\u9ed1\u4f53\";")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_7 = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.top_right = QWidget(self.r)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(108, 36))
        self.top_right.setMaximumSize(QSize(36, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.top_right)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolButton_2 = ToolButton(self.top_right)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(36, 36))
        #         self.toolButton_2.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
        # "border:0px solid red;\n"
        # "border-radius:8px;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/test/\u7f16\u7ec4 8.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.toolButton_2)

        self.horizontalSpacer_9 = QSpacerItem(12, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.toolButton_3 = ToolButton(self.top_right)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(36, 36))

        #         self.toolButton_3.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
        # "border:0px solid red;\n"
        # "border-radius:8px;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/test/\u7f16\u7ec4 9.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.toolButton_3)

        self.horizontalSpacer_10 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_5.addWidget(self.top_right)

        self.gridLayout.addWidget(self.r, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.top_widget)

        self.mid = QWidget(Form)
        self.mid.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mid.setObjectName(u"mid")
        self.mid.setMinimumSize(QSize(546, 646))
        self.verticalLayout_4 = QVBoxLayout(self.mid)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.mid)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(10000, 1))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.scrollArea = QScrollArea(self.mid)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumSize(QSize(546, 644))
        self.scrollArea.setStyleSheet(u"border:0px solid")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 546, 644))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.scrollArea.raise_()
        self.scrollArea.raise_()
        self.line_3.raise_()

        self.verticalLayout.addWidget(self.mid)

        self.down = QWidget(Form)
        self.down.setObjectName(u"down")
        self.down.setMinimumSize(QSize(546, 194))
        self.verticalLayout_2 = QVBoxLayout(self.down)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.down)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(10000, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget_3 = QWidget(self.down)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(546, 58))
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.t5 = QSpacerItem(15, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.t5)

        self.pushButton = PushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        #         self.pushButton.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
        # "border:0px solid red;\n"
        # "border-radius:8px;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/test/\u6d88\u606f.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(327, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = PushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(64, 30))

        font1 = QFont()
        font1.setFamilies([u"\u601d\u6e90\u9ed1\u4f53"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        #         self.pushButton_2.setStyleSheet(u"background-color: rgb(27, 115, 232);\n"
        # "border:0px solid red;\n"
        # "border-radius:8px;\n"
        # "color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.t3 = QSpacerItem(19, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.t3)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.w = QWidget(self.down)
        self.w.setObjectName(u"w")
        self.w.setMinimumSize(QSize(546, 114))
        self.horizontalLayout_2 = QHBoxLayout(self.w)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.t6 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.t6)

        self.textEdit = TextEdit(self.w)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(498, 114))
        # 在 self.horizontalLayout_2 中的现有代码之后，添加以下内容：
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)  # 设置左、上、右、下边距为30像素

        # 设置TextEdit控件的大小策略
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout_2.setStretch(2, 1)  # w 的拉伸因子设置为1
        self.horizontalLayout_2.addWidget(self.textEdit)

        self.t1 = QSpacerItem(24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.t1)

        self.verticalLayout_2.addWidget(self.w)

        self.emty = QWidget(self.down)
        self.emty.setObjectName(u"emty")
        self.emty.setMinimumSize(QSize(0, 21))

        self.verticalLayout_2.addWidget(self.emty)

        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textEdit.raise_()
        self.w.raise_()
        self.emty.raise_()
        self.line_2.raise_()

        self.verticalLayout.addWidget(self.down)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.toolButton_2.setText("")
        self.toolButton_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u804a\u5929\u8bb0\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
    # retranslateUi


class TextEdit(TextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return and not event.modifiers() & QtCore.Qt.ShiftModifier:
            self.parent.sendMessage()
        else:
            super().keyPressEvent(event)


class ChatBubbleWidget(QTextBrowser):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.message = message
        self.init_ui()

    def init_ui(self):
        self.setReadOnly(True)  # 设置为只读
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(QTextBrowser.NoFrame)
        self.setWordWrapMode(QTextOption.WordWrap)

        # 修改文字颜色和字体
        text_color = QColor("#1B73E8")
        self.setTextColor(text_color)
        font = QFont()
        font.setFamily("思源黑体")
        font.setPointSize(16)  # 设置字号为16px
        self.setFont(font)

        # 修改背景颜色
        bubble_color = QColor("#E8F1FC")
        self.setStyleSheet(f"background-color: {bubble_color.name()};"
                           "border: 0px;"
                           "border-radius: 10px;"
                           "padding: 15px 17px;")  # 设置上下左右边距

        # 设置文本
        self.setPlainText(self.message)

        # 根据行数调整大小
        line_count = self.document().lineCount()
        new_height = 56 + (line_count - 1) * 42
        self.setMinimumHeight(new_height)


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 隐藏边框

        # #这一段代码创建了一个水平布局，称为self.hBoxLayout，并将其设置为该窗口的布局。然后创建了一个名为self.navigationInterface的导航接口和一个名为self.stackWidget
        # 的堆栈小部件。其中，NavigationInterface是一个用于管理导航栏的自定义类，而QStackedWidget是一个小部件，用于在单个界面上管理多个子界面。
        self.d = Ui_Form()
        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.searchInterface = Widget('Search Interface', self)
        self.musicInterface = Widget('Music Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = self.d

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._dragging:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor("#ffffff")))
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.addRoundedRect(self.contentsRect(), 6, 6)
        painter.drawPath(path)

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        # 它设置了 QStackedWidget 的伸展因子为1，以确保它占用整个窗口的剩余空间。
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music library')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video library')

        self.navigationInterface.addSeparator()

        # add navigation items to scroll area
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder library', NavigationItemPosition.SCROLL)

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(1)

    def initWindow(self):
        self.resize(546, 945)


        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text
        )

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

    def showMessageBox(self):
        w = MessageBox(
            'This is a help message',
            'You clicked a customized navigation widget. You can add more custom widgets by calling `NavigationInterface.addWidget()` 😉',
            self
        )
        w.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
