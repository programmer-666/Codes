import sys
from PyQt5 import QtWidgets

class test(QtWidgets.QMainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        super(test, self).__init__()
        self.setGeometry(200, 200, 200, 200)
        self.conts()
    def conts(self):
        self.cb1 = QtWidgets.QCheckBox(self)
        self.cb1.setText("CheckBox1")
        self.cb1.move(0, 0)
        #
        self.cb2 = QtWidgets.QCheckBox(self)
        self.cb2.setText("CheckBox2")
        self.cb2.move(0, 20)
        self.cb2.setChecked(True)
        #
        self.cb3 = QtWidgets.QCheckBox(self)
        self.cb3.setText("CheckBox3")
        self.cb3.move(0, 40)
        self.cb3.setTristate(True)
        #
        self.cb4 = QtWidgets.QCheckBox(self)
        self.cb4.setText("CheckBox4")
        self.cb4.move(0, 60)
        self.cb4.stateChanged.connect(self.sstat)
        #
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("List")
        self.b1.move(0, 90)
        self.b1.clicked.connect(self.sptat)
    def sstat(self): # anlık olarak yapılan kontrol işlemi tek bir butona atanarak yapılabilir
        print(self.cb4.isChecked(), self.sender().text(), self.sender().isChecked())
    def sptat(self): # bu fonksiyon seçili olan elemanların referansını dizi biçiminde döndürür
        for i in self.findChildren(QtWidgets.QCheckBox):
            print(i.text(), i.isChecked())
    def showtime(self):
        self.show()
        sys.exit(self.app.exec_())
t = test()
t.showtime()