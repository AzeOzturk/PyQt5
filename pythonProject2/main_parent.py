


from PyQt5.QtWidgets import *
from parent import Ui_Form
from main_child1 import Main_page1
from main_child2 import Main_page2
from main_child3 import Main_page3
class Main_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_first_tap)
        self.ui.pushButton_2.clicked.connect(self.open_second_tap)
        self.ui.pushButton_3.clicked.connect(self.open_third_tap)
        self.first = Main_page1()
        self.second = Main_page2()
        self.third = Main_page3()
    def open_first_tap(self):
        self.first.show()
        self.ui.label.setText('first')
    def open_second_tap(self):
        self.second.show()
        self.ui.label.setText('second')
    def open_third_tap(self):
        self.third.show()
        self.ui.label.setText('third')
