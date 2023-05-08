import sys
from PySide6 import QtCore, QtGui, QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口大小和标题
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("My Window")

        # 设置窗口背景色为白色
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)

        # 设置窗口图标
        icon = QtGui.QIcon("API 接口_api.svg")
        self.setWindowIcon(icon)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
