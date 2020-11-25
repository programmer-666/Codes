import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
# The code that takes the mean of 2 numbers
class basic_w(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(basic_w, self).__init__()
        self.setWindowTitle("Ortalama")
        self.setGeometry(200, 200, 220, 121)
        self.initUi()
    def aveprint(self):
        self.tb3.setText(str((float(self.tb1.text())+float(self.tb2.text()))/2))
        print(self.sender()) # metot sayesinde anlik olarak aktif olan butonun referansi return olur
        print(self.sender().text())
    def initUi(self):
        self.tb1 = QtWidgets.QLineEdit(self)
        self.tb2 = QtWidgets.QLineEdit(self)
        self.tb3 = QtWidgets.QLineEdit(self)
        self.tb1.move(10, 10)
        self.tb2.move(110, 10)
        self.tb3.move(10, 80)
        self.tb3.resize(200, 30)
        #textboxes
        self.pb = QtWidgets.QPushButton(self)
        self.pb.setText("Calc")
        self.pb.move(10, 40)
        self.pb.resize(200, 40)
        self.pb.clicked.connect(self.aveprint)
        #pushbutton
    def ShowW(self):
        self.show()
        sys.exit(self.app.exec_())
testw = basic_w()
testw.ShowW() 