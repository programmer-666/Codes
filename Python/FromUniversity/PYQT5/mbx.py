import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
class mw(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(mw, self).__init__()
        self.initc()
    def initc(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("MBX")
        self.b1.clicked.connect(self.sdg)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("MBX2")
        self.b2.clicked.connect(self.sdg2)
        self.b2.move(0,50)
    def sdg2(self):
        x = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore, QMessageBox.No)
        if x == QMessageBox.Yes:
            print("ohk")
    def sdg(self):
        mbx = QtWidgets.QMessageBox()
        mbx.setWindowTitle("Are you sure about that?")
        mbx.setText("If you are pushed this button msgbx will be closed")
        mbx.setIcon(QtWidgets.QMessageBox.Warning)
        mbx.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore)
        mbx.setDefaultButton(QtWidgets.QMessageBox.Ok)
        mbx.setDetailedText("Detailed button")
        mbx.buttonClicked.connect(self.pup)
        x  = mbx.exec_()
        print(x) # aktif edilen butonlardan dönen değerleri tutar
    def pup(self, i): # i hangi butona tıklandığıyla ilgili
        print(i.text())
        if i.text() == "Cancel":
            QtWidgets.qApp.quit()
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())

t = mw()
t.showtime()        