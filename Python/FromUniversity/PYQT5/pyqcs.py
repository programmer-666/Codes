import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Main_window(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(Main_window, self).__init__()
        self.setWindowTitle("First app wit class")
        self.setGeometry(500, 500, 300, 70)
        self.initUi()
    def initUi(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Enter Code")
        self.label1.move(10, 10)
        self.label1.resize(100, 50)# Resizing iste aciklamaya gerek yok.
        # Label
        self.pbutton1 = QtWidgets.QPushButton(self)
        self.pbutton1.setText("Submit")
        self.pbutton1.move(190, 10)
        self.pbutton1.resize(100, 50)
        # PushButton
        self.ledit = QtWidgets.QLineEdit(self)
        self.ledit.move(90, 10)
        self.ledit.resize(100, 50)
        # Text
    def  ShowTime(self):
        self.show()
        sys.exit(self.app.exec_())

testw = Main_window()
testw.ShowTime()