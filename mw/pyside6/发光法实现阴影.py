from argparse import Action

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QRegion
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QPushButton, QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon as FIF, SplitPushButton, SplitToolButton, RoundMenu


class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QVBoxLayout(self)

        self.button = QPushButton("Close")
        self.button.clicked.connect(self.close)
        self.layout.addWidget(self.button)

        # # split button
        # self.splitPushButton = SplitPushButton('Split push button', self, FIF.GITHUB)
        # self.splitToolButton = SplitToolButton(FIF.GITHUB, self)
        # self.splitMenu = RoundMenu(parent=self)
        # self.splitMenu.addAction(Action(FIF.BASKETBALL, 'Basketball'))
        # self.splitMenu.addAction(Action(FIF.ALBUM, 'Sing'))
        # self.splitMenu.addAction(Action(FIF.MUSIC, 'Music'))
        # self.splitPushButton.setFlyout(self.splitMenu)
        # self.splitToolButton.setFlyout(self.splitMenu)
        # self.layout.addWidget(self.splitPushButton)


        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setOffset(5, 5)
        shadow_effect.setBlurRadius(15)
        shadow_effect.setColor(QColor(0, 0, 0, 80))

        self.setGraphicsEffect(shadow_effect)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor("#fff"))
        painter.setPen(Qt.NoPen)

        rect = self.contentsRect()
        rounded_rect = rect.adjusted(5, 5, -5, -5)
        painter.drawRoundedRect(rounded_rect, 6, 6)

        # Clip the painter to the rounded rect for child widgets
        region = QRegion(rounded_rect, QRegion.Rectangle)
        painter.setClipRegion(region)

if __name__ == "__main__":
    app = QApplication([])

    window = CustomWindow()
    window.resize(300, 200)
    window.show()

    app.exec()
