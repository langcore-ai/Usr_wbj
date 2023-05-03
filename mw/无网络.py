from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication()

if not is_network_available():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("无网络")
    msg_box.setText("网络不可用，请检查您的网络连接。")
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.exec()
