from PyQt5.QtWidgets import *
from child1 import Ui_MainWindow

class Main_page1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
