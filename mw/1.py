import requests
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QColor, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, \
    QTextEdit, QLineEdit, QPushButton, QTreeView
from langchain.chat_models import openai
from openai import Completion


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Chat with ChatGPT")

        # set up the UI
        self.chat_box = QStandardItemModel()
        self.message_box = QStandardItemModel()
        self.message_input = QTextEdit()
        self.send_button = QPushButton("Send")

        # layout the UI
        chat_view = QTreeView()
        chat_view.setModel(self.chat_box)
        chat_view.setEditTriggers(QTreeView.NoEditTriggers)
        chat_view.setSelectionBehavior(QTreeView.SelectRows)
        chat_view.header().setStretchLastSection(True)
        chat_view.header().setVisible(False)
        chat_view.setMaximumWidth(200)
        chat_view.setMinimumWidth(200)

        message_view = QTreeView()
        message_view.setModel(self.message_box)
        message_view.setEditTriggers(QTreeView.NoEditTriggers)
        message_view.setSelectionBehavior(QTreeView.SelectRows)
        message_view.header().setStretchLastSection(True)
        message_view.header().setVisible(False)
        message_view.setStyleSheet("background-color: #f6f6f6;")

        scroll_area = QScrollArea()
        scroll_area.setWidget(message_view)
        scroll_area.setWidgetResizable(True)

        chat_layout = QVBoxLayout()
        chat_layout.addWidget(QLabel("Chat History"))
        chat_layout.addWidget(chat_view)

        message_layout = QVBoxLayout()
        message_layout.addWidget(QLabel("Message History"))
        message_layout.addWidget(scroll_area)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(chat_layout)
        main_layout.addLayout(message_layout)

        input_widget = QWidget()
        input_widget.setLayout(input_layout)

        widget = QWidget()
        widget.setLayout(main_layout)

        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(input_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # add functionality
        self.send_button.clicked.connect(self.send_message)
        self.chatbot = ChatBot()
        self.chatbot.start_session()
    def add_chat(self, text):
        item = QStandardItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.chat_box.appendRow(item)

    def add_message(self, text, user="You", color="#0084ff"):
        message = f"{user}: {text}"
        item = QStandardItem(message)
        item.setForeground(QColor(color))
        self.message_box.appendRow(item)

    def send_message(self):
        message = self.message_input.toPlainText()
        if message.strip():
            self.add_message(message)

            response = self.chatbot.message(message)
            self.add_message(response, "ChatGPT", "#3b3b3b")

openai.api_key = "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"


class ChatBot:
    def __init__(self):
        self.session_id = None

    def start_session(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai.api_key}'
        }

        data = {
            'model': 'text-davinci-002',
            'prompt': 'Create a new session',
            'max_tokens': 1024,
        }

        response = requests.post('https://api.openai.com/v1/engines/text-davinci-002/completions', json=data, headers=headers)

        if response.status_code == 200:
            response_json = response.json()
            self.session_id = response_json['choices'][0]['text'].strip()

    def message(self, text):
        prompt = f"{self.session_id}: {text}\nAI:"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {"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"}'
        }

        data = {
            'model': 'text-davinci-002',
            'prompt': prompt,
            'max_tokens': 1024,
        }

        response = requests.post('https://api.openai.com/v1/engines/text-davinci-002/completions', headers=headers, json=data)

        response_json = response.json()

        if 'choices' in response_json:
            message = response_json['choices'][0]['text'].strip().replace("AI:", "")
        else:
            message = "Sorry, something went wrong. Please try again later."

        return message



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
