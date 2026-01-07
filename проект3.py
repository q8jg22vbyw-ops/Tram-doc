from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QUrl, QFileInfo
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
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
        self.pushButton_2.clicked.connect(self.admin)

    def newW(self):
        self.hide()
        self.a = schema()
        self.a.show()

    def admin(self):
        self.hide()
        self.b = adm()
        self.b.show()


class schema(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('schema.ui', self)
        w = 661
        h = 572
        self.setFixedSize(w, h)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.newW2)
        self.pushButton_2.clicked.connect(self.lastW2)

    def lastW2(self):
        self.hide()
        self.d = menu()
        self.d.show()

    def newW2(self):
        self.hide()
        self.b = model1()
        self.b.show()

class model1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('модель 1.ui', self)
        w = 1022
        h = 812
        self.setFixedSize(w, h)
        self.initUI()

    def initUI(self):
        self.pushButton_2.clicked.connect(self.lastW)
        self.pushButton_3.clicked.connect(self.dow1)

    def dow1(self):
        self.hide()
        self.d = doc1()
        self.d.show()

    def lastW(self):
        self.hide()
        self.c = schema()
        self.c.show()

class doc1(model1):
    def __init__(self):
        super().__init__()
        uic.loadUi('dow1.ui', self)
        w = 661
        h = 572
        self.setFixedSize(w, h)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.newW)
        self.pushButton_2.clicked.connect(self.admin)

    def newW(self):
        self.hide()
        self.a = model1()
        self.a.show()

class adm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('вход.ui', self)
        w = 661
        h = 572
        self.setFixedSize(w, h)
        self.initUI()

    def initUI(self):
        self.pushButton_2.clicked.connect(self.lastW3)
        self.pushButton.clicked.connect(self.vchod)

    def vchod(self):
        self.parol = self.plainTextEdit.toPlainText()
        

    def lastW3(self):
        self.hide()
        self.a = menu()
        self.a.show()
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = menu()
    ex.show()
    sys.exit(app.exec())
