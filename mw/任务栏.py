import pystray
from PIL import Image

def on_quit(icon, item):
    icon.stop()

image = Image.open("E:/Usr_wbj/pyqt5仿交易软件无边框拉伸/Copying_1007/img/img/443px.png")

menu = pystray.Menu(pystray.MenuItem("退出", on_quit))

icon = pystray.Icon("appname", image, "应用名称", menu)
icon.run()
