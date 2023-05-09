import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个 QTextEdit 实例
        self.text_edit = QTextEdit()

        # 设置 QTextEdit 的最小尺寸为 100x60
        self.text_edit.setMinimumSize(100, 60)

        # 创建一个 QHBoxLayout 实例
        self.layout = QHBoxLayout()

        # 设置布局与窗口边框的距离为 30 像素
        self.layout.setContentsMargins(30, 30, 30, 30)

        # 将 QTextEdit 实例添加到 QHBoxLayout 中
        self.layout.addWidget(self.text_edit)

        # 将 QHBoxLayout 设置为窗口的主布局
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
