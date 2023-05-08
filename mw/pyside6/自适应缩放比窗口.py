import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

# 检测屏幕缩放比
screen = app.primaryScreen()
scaling_factor = screen.logicalDotsPerInch() / 96.0
print(scaling_factor)

# 根据缩放比调整窗口和控件大小
window = QMainWindow()
window.setWindowTitle('自适应缩放窗口')
window.resize(1000 / scaling_factor, 1000 / scaling_factor)

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

button1 = QPushButton("按钮1")
button2 = QPushButton("按钮2")

button1.setMinimumSize(100 / scaling_factor, 50 / scaling_factor)
button2.setMinimumSize(100 / scaling_factor, 50 / scaling_factor)

layout.addWidget(button1)
layout.addWidget(button2)

window.setCentralWidget(central_widget)
window.show()

sys.exit(app.exec())
