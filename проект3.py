from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
import sys


class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('проект.ui', self)
        w = 661
        h = 572
        self.setFixedSize(w, h)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.newW)

    def newW(self):
        self.hide()
        self.a = schema()
        self.a.show()


class schema(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('schema.ui', self)
        w = 661
        h = 572
        self.setFixedSize(w, h)
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = menu()
    ex.show()
    sys.exit(app.exec())


