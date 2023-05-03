# from PySide6.QtCore import Qt, QTimer
# from PySide6.QtGui import QPainter, QColor, QBrush
# from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
#
#
# class SelectWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # 在 __init__ 方法中添加一个属性来保存 MessageWindow 实例
#         self.message_window = None
#         self.ask_anything_window = None
#         self.setAutoFillBackground(False)
#         # 设置无边框
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         # 设置窗口背景透明
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         self.setWindowTitle("选项")
#
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
#
#         self.layout = QHBoxLayout()
#
#         self.translate_button = QPushButton("翻译")
#         self.explain_button = QPushButton("解释")
#         self.summarize_button = QPushButton("总结")
#         self.code_button = QPushButton("代码报错")
#         self.answer_button = QPushButton("Ask Anything")
#
#         self.layout.addWidget(self.translate_button)
#         self.layout.addWidget(self.explain_button)
#         self.layout.addWidget(self.summarize_button)
#         self.layout.addWidget(self.code_button)
#         self.layout.addWidget(self.answer_button)
#         # 设置ID，以便在QSS中使用
#         self.answer_button.setObjectName("answer_button")
#
#         self.setLayout(self.layout)
#
#
#
#     # 重写绘制,窗口圆角
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setBrush(QBrush(QColor("#777777")))
#         painter.setPen(Qt.NoPen)
#         painter.drawRoundedRect(self.contentsRect(), 15, 15)
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     window = SelectWindow()
#     window.show()
#
#     sys.exit(app.exec())
from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtGui import QFont, QTextOption, Qt

app = QApplication([])

# 创建一个 QTextEdit 组件
text_edit = QTextEdit()

# 设置字体和字号
font = QFont("Arial", 12)
text_edit.setFont(font)

# 设置行间距为 1.5 倍字体高度
text_edit.setStyleSheet("QTextEdit {line-height: 150%;}")

# 设置对齐方式为两端对齐
option = QTextOption()
option.setAlignment(Qt.AlignJustify)
text_edit.document().setDefaultTextOption(option)

# 设置文本
text_edit.setPlainText("这是一段测试文本，用于测试行间距和对齐方式。")

# 显示 QTextEdit 组件
text_edit.show()

app.exec()
