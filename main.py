



from PyQt5.QtWidgets import*
from conver import Ui_MainWindow
import sys
import time
import os
class app(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.one)
        self.ui.pushButton_2.clicked.connect(self.two)
        self.ui.pushButton_3.clicked.connect(self.third)
        self.ui.pushButton_4.clicked.connect(self.four)
    def one(self):
        self.ui.pushButton.setStyleSheet(
            "background-color: rgb(255, 0, 4);color: rgb(0, 0, 0);border-radius:10px;font: 14pt \"Arial Narrow\";")
        os.system("shutdown /s /t 1800")
    def two(self):
        self.ui.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 0, 4);color: rgb(0, 0, 0);border-radius:10px;font: 14pt \"Arial Narrow\";")
        os.system("shutdown /s /t 3600")
    def third(self):
        self.ui.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 0, 4);color: rgb(0, 0, 0);border-radius:10px;font: 14pt \"Arial Narrow\";")
        os.system("shutdown /s /t 5400")
    def four(self):
        self.ui.pushButton_4.setStyleSheet(
            "background-color: rgb(255, 0, 4);color: rgb(0, 0, 0);border-radius:10px;font: 14pt \"Arial Narrow\";")
        os.system("shutdown -s -t 7200")


application = QApplication(sys.argv)
QWidget = app()
QWidget.show()
application.exec_()

