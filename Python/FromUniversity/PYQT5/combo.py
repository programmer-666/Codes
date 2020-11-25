import sys
from PyQt5 import QtWidgets

class maw(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(maw, self).__init__()
        self.conts()
        self.getit()
    def conts(self):
        self.cx1 = QtWidgets.QComboBox(self)
        self.cx1.addItem("Doe")
        self.cx1.addItems(["John", "Steve", "Mark"])
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Add items")
        self.btn1.clicked.connect(self.adit)
        self.btn1.move(0, 30)
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("Get item")
        self.btn2.clicked.connect(self.getall)
        self.btn2.move(0, 60)
        self.cx1.currentIndexChanged.connect(self.sch) # indexi
        self.cx1.currentIndexChanged[str].connect(self.sch)# indexin textini
        self.clearb = QtWidgets.QPushButton(self)
        self.clearb.setText("Clear")
        self.clearb.clicked.connect(self.cln)
        self.clearb.move(0, 80)
        self.remi = QtWidgets.QPushButton(self)
        self.remi.move(100, 0)
        self.remi.setText("Remove Selected")
        self.remi.clicked.connect(self.remif)
    def remif(self):
        self.cx1.removeItem(self.cx1.currentIndex())
    def cln(self):
        self.cx1.clear() 
    def adit(self):
        self.cx1.addItems((["test", "1k3"]))
    def getit(self):
        print(self.cx1.currentText(), self.cx1.currentIndex(), self.cx1.count())# count eleman sayısını verir toplam index
        self.totalc = self.cx1.count()
    def getall(self):
        for i in range(self.totalc):
            print(self.cx1.itemText(i))
    def sch(self, text):
        print(text)
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())
t = maw()
t.showtime()

