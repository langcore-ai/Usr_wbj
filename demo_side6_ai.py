import sys
from PySide6.QtWidgets import QWidget, QApplication
from Side6的AIchat转ui import Ui_AIchat

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AIchat()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
