# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication

from Side6的AIchat转ui import Ui_AIchat


class Demo(QWidget, Ui_AIchat):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()
