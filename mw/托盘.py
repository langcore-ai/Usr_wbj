import sys
import os
import subprocess
import threading
import keyboard
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QTextEdit, QPushButton, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy, QLineEdit, QPushButton, QTextEdit, QSystemTrayIcon, QMenu
from PySide6.QtCore import *
from PySide6.QtGui import QColor, QCursor, QAction

from PySide6.QtWidgets import QHBoxLayout, QToolButton, QApplication
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPaintEvent


# 创建托盘窗口
def create_system_tray_icon(app):
    tray_icon = QSystemTrayIcon(QIcon("E:\pyqt\AI资源\火箭.svg"), app)

    # 创建一个 QAction 对象
    tray_icon.settings_action = QAction("设置")
    tray_icon.settings_action.triggered.connect(open_settings_window)

    tray_icon.quit_action = QAction("退出")
    tray_icon.quit_action.triggered.connect(app.quit)

    # 创建一个 QMenu 对象并将其设置为 tray_icon 的属性
    tray_icon.menu = QMenu()
    tray_icon.menu.addAction(tray_icon.settings_action)
    tray_icon.menu.addSeparator()
    tray_icon.menu.addAction(tray_icon.quit_action)

    # 将 QMenu 对象设置为托盘图标的上下文菜单
    tray_icon.setContextMenu(tray_icon.menu)
    tray_icon.show()

    # 连接激活信号到 show_tray_icon_menu 槽函数
    tray_icon.activated.connect(lambda reason: show_tray_icon_menu(reason, tray_icon.menu))

    return tray_icon


# 定义托盘图标的槽函数，用于执行动作
def show_tray_icon_menu(reason, menu):
    if reason == QSystemTrayIcon.Trigger or reason == QSystemTrayIcon.DoubleClick:
        # 根据当前光标位置显示菜单
        menu.exec(QCursor.pos())



# 打开设置窗口
def open_settings_window():

    pass


def run_app(app, tray_icon):
    # 确保应用程序不会在最后一个窗口关闭时退出
    app.setQuitOnLastWindowClosed(False)


def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)



    # 将应用程序的图标设置为托盘图标作为持久化实例
    tray_icon = create_system_tray_icon(app)
    run_app(app, tray_icon)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()