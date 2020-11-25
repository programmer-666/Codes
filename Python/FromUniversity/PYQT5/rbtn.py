import sys
from PyQt5 import QtWidgets

class rbtw(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(rbtw, self).__init__()
        self.conts()
    def conts(self):
        self.rb1 = QtWidgets.QRadioButton(self)
        self.rb1.setText("RadioButton1")
        self.rb1.setChecked(True)
        self.rb1.toggled.connect(self.getwinfo)
        self.rb2 = QtWidgets.QRadioButton(self)
        self.rb2.move(0, 30)
        self.rb2.setText("RadioButton2")
        self.rb2.setChecked(True)
        self.rb2.toggled.connect(self.getwinfo)
        self.btn = QtWidgets.QPushButton("All", self)
        self.btn.move(0,60)
        self.btn.clicked.connect(self.btnf)
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())
    def getwinfo(self):
        print("\t",self.sender().isChecked(), self.sender().text())
    def btnf(self):
        for i in self.findChildren(QtWidgets.QRadioButton):#eğer rbler groupbox veya layout içindeyse ona göre seçim bu widgetların içerisinden yapılır
            if i.isChecked():
                print(i.text())#referans.text() - referansın textini döndürür
t = rbtw()
t.showtime()
