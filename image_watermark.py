from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QFileDialog
from PyQt5.QtGui import QIcon
import sys


class AppUi(QMainWindow): # inheriting from the QMainWindow to access all of its method
    def __init__(self):
        super(AppUi, self).__init__()
        self.setGeometry(0, 0, self.width(), self.height()) # Setting the width and height to the available device with and height
        self.setWindowTitle("Image Watermark Adder")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #262626;
            }

            QPushButton {
                background-color: #3D3D3D;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #727272;
            }
        """) # Stylesheet

        self.ui() # Calling the ui methond to render all the ui elements

    def ui(self):
        icon = QIcon("setting.png") # Loading the setting icon
        self.settingsBtn = QPushButton(self) # Creating a button for settings
        self.settingsBtn.setIcon(icon) # assigning the icon to the button
        self.settingsBtn.setFixedSize(30, 30)

        self.uploadBtn = QPushButton(self) # Creating a button fot uploading images
        self.uploadBtn.setText("Upload Image")

        self.uploadBtn.clicked.connect(self.open_file_dialog) # calling the file open methond when the button is clicked

        self.UiPosition() # Made a seperate function in which all the ui elements location is adjusted. So i can call this function when ever the application resizes and the fucntion will update every elements possition accordingly.

    def UiPosition(self):
        self.halfWidth = round(self.width()/2) # to get the half of the window width. Rounding it to beacuse the move method only takes int as a argument and some times the half width return a float
        self.halfheight = round(self.height()/2) # same thing going on here
        self.settingsBtn.move(self.width() - 45, 20) # moving the settings icon accoding to the window width

        uploadBtnHalfWith = round(self.uploadBtn.width()/2)
        uploadBtnHalfHieght = round(self.uploadBtn.height()/2)
        self.uploadBtn.move(self.halfWidth - uploadBtnHalfWith, self.halfheight - uploadBtnHalfHieght)

    def resizeEvent(self, event):
        self.setGeometry(0, 0, self.width(), self.height())
        self.UiPosition()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File")
        if file_path:
            print("Selected file:", file_path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppUi()
    win.show()
    sys.exit(app.exec_())
