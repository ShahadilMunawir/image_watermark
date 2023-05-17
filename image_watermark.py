from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint
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
            QLabel {
                color: white;
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

        self.selectedFileLable = QLabel(self)

        self.uploadWatermark = QPushButton(self)
        self.uploadWatermark.setText("Upload WaterMark")
        self.uploadWatermark.adjustSize()

        self.watermarkLabel = QLabel(self)

        self.uploadBtn.clicked.connect(self.open_file_upload) # calling the file open methond when the button is clicked

        self.uploadWatermark.clicked.connect(self.open_file_watermark)
        self.UiPosition() # Made a seperate function in which all the ui elements location is adjusted. So i can call this function when ever the application resizes and the fucntion will update every elements possition accordingly.


    def UiPosition(self):
        self.halfWidth = round(self.width()/2) # to get the half of the window width. Rounding it to beacuse the move method only takes int as a argument and some times the half width return a float
        self.halfheight = round(self.height()/2) # same thing going on here
        self.settingsBtn.move(self.width() - 45, 20) # moving the settings icon accoding to the window width

        uploadBtnHalfWith = round(self.uploadBtn.width()/2)
        uploadBtnHalfHieght = round(self.uploadBtn.height()/2)
        self.uploadBtn.move(self.halfWidth - uploadBtnHalfWith, self.halfheight - uploadBtnHalfHieght) # Adjusting the upload button to the center of the screen

        self.selectedFileLable.move(self.uploadBtn.pos() + QPoint(110, 5) )

        watermarkBtnHalfWidth = round(self.uploadWatermark.width()/2)
        self.uploadWatermark.move(self.halfWidth - watermarkBtnHalfWidth, self.uploadBtn.pos().y() + 100)

        self.watermarkLabel.move(self.uploadWatermark.pos() + QPoint(130, 2))

    def resizeEvent(self, event): # This function will be called whenever the window is resized.
        self.setGeometry(0, 0, self.width(), self.height())
        self.UiPosition()

 

    def open_file_upload(self):

        self.selectedFileNameArray = [] 


        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle('Open Files')
        file_dialog.setNameFilter('Images (*.png *.jpg)') # Fileters the input files
        file_dialog.setFileMode(QFileDialog.ExistingFiles) # This line enables multi selection of files


        if file_dialog.exec_() == QFileDialog.Accepted: # Checking if the user selected a file
            selected_files = file_dialog.selectedFiles()
            
            for files in selected_files:
                filename = files.split("/").pop()
                self.selectedFileNameArray.append(filename)
            if(len(self.selectedFileNameArray) - 1 == 0):
                self.selectedFileLable.setText(self.selectedFileNameArray[0])
                self.selectedFileLable.adjustSize()
            else:
                self.selectedFileLable.setText("{} & {} more".format(self.selectedFileNameArray[0], len(self.selectedFileNameArray) - 1))
                self.selectedFileLable.adjustSize()

    def open_file_watermark(self):

        self.selectedWatermark = []

        file_watermark = QFileDialog(self)
        file_watermark.setWindowTitle("Select an image for watermaker")
        file_watermark.setNameFilter('Images (*.png *.jpg)')

        if file_watermark.exec_() == QFileDialog.Accepted:
            selected_watermark = file_watermark.selectedFiles()

            self.watermarkLabel.setText(selected_watermark[0].split("/").pop())
            self.watermarkLabel.adjustSize()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppUi()
    win.show()
    sys.exit(app.exec_())
