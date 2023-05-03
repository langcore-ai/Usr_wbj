import sys
import threading

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication

from main1004 import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.pushButton_5.clicked.connect(self.close)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)  # 去掉lineEdit焦点
        self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)  # 去掉lineEdit焦点
        self.button_list_even = threading.Event()
        self.toolButton.clicked.connect(self.button_list)
        self.frame.setStyleSheet("""
        QFrame{
        background-color: rgb(255, 255, 255);
        border-top-left-radius:5px;
        border-top-right-radius:5px;
        border-bottom-right-radius:5px;
        border-bottom-left-radius:5px;
        }
        """)
        self.effect_shadow_style(self.frame)
        self.setGeometry(self.x(), self.y(), self.width(), 342)

    def button_list(self):
        if self.button_list_even.is_set():
            self.button_list_even.clear()
            self.frame.setStyleSheet("""
                                QFrame{
                                background-color: rgb(255, 255, 255);
                                border-top-left-radius:5px;
                                border-top-right-radius:5px;
                                border-bottom-right-radius:5px;
                                border-bottom-left-radius:5px;
                                }
                                """)
            self.animation_exit()
        else:
            self.button_list_even.set()
            self.frame.setStyleSheet("""
                    QFrame{
                    background-color: rgb(255, 255, 255);
                    border-top-left-radius:5px;
                    border-top-right-radius:5px;
                    border-bottom-right-radius:0px;
                    border-bottom-left-radius:0px;
                    }
                    """)
            self.animation_start()

    def animation_start(self):
        widget_geometry = QPropertyAnimation(self, b"geometry", self)
        widget_geometry.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        widget_geometry.setEndValue(QRect(self.x(), self.y(), self.width(), 414))
        widget_geometry.setDuration(320)
        widget_geometry.finished.connect(self.animation_start_signal)
        widget_geometry.start()

    def animation_start_signal(self):
        self.frame_5.setMaximumHeight(1555)

    def animation_exit(self):
        self.frame_5.setMaximumHeight(0)
        widget_geometry = QPropertyAnimation(self, b"geometry", self)
        widget_geometry.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        widget_geometry.setEndValue(QRect(self.x(), self.y(), self.width(), 342))
        widget_geometry.setDuration(320)
        widget_geometry.finished.connect(self.animation_exit_signal)
        widget_geometry.start()

    def animation_exit_signal(self):
        ...

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 5)  # 偏移
        effect_shadow.setBlurRadius(12)  # 阴影半径
        effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
