import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QTextCursor, QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QDialog, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.message_box = QTextEdit(self)
        self.chat_box = ChatLineEdit(self)
        self.chat_box.setMaximumHeight(100)
        self.chat_box.setPlaceholderText("请输入消息")
        vbox = QVBoxLayout()
        vbox.addWidget(self.message_box)
        vbox.addWidget(self.chat_box)

        self.central_widget = QWidget()
        self.central_widget.setLayout(vbox)
        self.setCentralWidget(self.central_widget)

        self.options_widget = OptionsWidget(self.chat_box)
        self.options_widget.setWindowFlags(Qt.FramelessWindowHint)
        self.options_widget.setStyleSheet('background-color: rgba(255, 255, 255, 0.8);')
        self.options_widget.hide()

        self.chat_box.returnPressed.connect(self.handle_return_pressed)
        self.chat_box.slashPressed.connect(self.handle_slash_pressed)

    def handle_return_pressed(self):
        message = self.chat_box.text()
        if message:
            self.message_box.append(message)
            self.chat_box.clear()

    def handle_slash_pressed(self):
        self.options_widget.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.chat_box.returnPressed.emit()
        else:
            super().keyPressEvent(event)

class ChatLineEdit(QLineEdit):
    returnPressed = Signal()
    slashPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.returnPressed.emit()
        elif event.key() == Qt.Key_Slash:
            self.slashPressed.emit()
        else:
            super().keyPressEvent(event)

class OptionsWidget(QDialog):
    def __init__(self, chat_box):
        super().__init__()
        self.chat_box = chat_box
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(['/i am hero', '/i am potato'])
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_widget)
        self.list_widget.itemClicked.connect(self.insert_option)

        self.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.setFixedWidth(self.chat_box.width())
        self.adjustHeight()

    def adjustHeight(self):
        count = self.list_widget.count()
        row_height = self.list_widget.sizeHintForRow(0)
        margin = self.list_widget.contentsMargins().top() + self.list_widget.contentsMargins().bottom()
        height = row_height * count + margin
        self.setFixedHeight(height)

    def insert_option(self, item):
        self.chat_box.setText(self.chat_box.text() + item.text())
        self.chat_box.setFocus()
        self.chat_box.setCursorPosition(len(self.chat_box.text()))
        event = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_Return, Qt.NoModifier, "\n")
        QApplication.postEvent(self.chat_box, event)
        self.hide()

    def show(self):
        self.adjustHeight()
        pos = self.chat_box.mapToGlobal(self.chat_box.rect().bottomLeft())
        self.move(pos)
        super().show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
