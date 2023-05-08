import sys
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor, QPalette, QPainter, QPen, QPainterPath, QBrush, QColorConstants, QRadialGradient
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class RoundedShadowWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置无边框窗口
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 设置窗口圆角半径
        self.rounded_radius = 10

        # 添加按钮并设置槽函数
        layout = QVBoxLayout()
        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        # 绘制阴影
        shadow_path = QPainterPath()
        shadow_path.addRoundedRect(self.rect(), self.rounded_radius, self.rounded_radius)

        shadow_gradient = QRadialGradient(self.rect().center(), max(self.rect().width(), self.rect().height()) / 2)
        shadow_gradient.setColorAt(0, QColor("#CAC8C8"))
        shadow_gradient.setColorAt(1, QColor("#ffffff"))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(shadow_gradient))
        painter.drawPath(shadow_path)

        # 绘制窗口背景
        path = QPainterPath()
        background_rect = QRectF(self.rect()).adjusted(3, 0, -3, -3)
        path.addRoundedRect(background_rect, self.rounded_radius, self.rounded_radius)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColorConstants.White)
        painter.drawPath(path)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RoundedShadowWindow()
    window.show()
    sys.exit(app.exec())
