from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication()
import socket

def is_network_available():
    try:
        # 建立一个新的套接字连接到 Google DNS
        s = socket.create_connection(("8.8.8.8", 53), 2)
        s.close()
        return True
    except OSError:
        pass
    return False

if not is_network_available():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("无网络")
    msg_box.setText("网络不可用，请检查您的网络连接。")
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.exec()
