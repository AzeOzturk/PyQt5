from PyQt5.QtWidgets import *
from child2 import Ui_MainWindow


class Main_page2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
