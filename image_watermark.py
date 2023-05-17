from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from PIL import Image, ImageDraw


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
        self.uploadBtn.move(self.halfWidth - uploadBtnHalfWith, self.halfheight - uploadBtnHalfHieght) # Adjusting the upload button to the center of the screen

    def resizeEvent(self, event): # This function will be called whenever the window is resized.
        self.setGeometry(0, 0, self.width(), self.height())
        self.UiPosition()

 

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle('Open Files')
        file_dialog.setNameFilter('Images (*.png *.jpg);;All Files (*)') # Fileters the input files
        file_dialog.setFileMode(QFileDialog.ExistingFiles) # This line enables multi selection of files


        if file_dialog.exec_() == QFileDialog.Accepted: # Checking if the user selected a file
            selected_files = file_dialog.selectedFiles()
            i = 0
            for file_name in selected_files: # Looping through the selected image path 
                source_image = Image.open(file_name)
                watermark_image = Image.open('setting.png')

                watermark_size = (200, 200)
                watermark_image = watermark_image.resize(watermark_size, Image.ANTIALIAS)

                result_image = Image.new('RGBA', source_image.size)
                result_image.paste(source_image, (0, 0))

                position = (result_image.width - watermark_image.width - 30, result_image.height - watermark_image.height - 30)
                result_image.paste(watermark_image, position, watermark_image)

                result_image.save("result_image"+str(i)+".png")
                i += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppUi()
    win.show()
    sys.exit(app.exec_())
