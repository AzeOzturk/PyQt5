from PyQt5.QtWidgets import *
from child3 import Ui_MainWindow


class Main_page3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
