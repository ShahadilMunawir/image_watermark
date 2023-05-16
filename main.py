from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1000, 200, 800, 600)
    win.setWindowTitle("Image Watermark")
    
    win.show()
    sys.exit(app.exec())

window()
