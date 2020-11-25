import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class maw(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(maw, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.conts()
    def conts(self):
        self.clr = QtWidgets.QCalendarWidget(self)
        self.clr.resize(200,160)
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())
t = maw()
t.showtime()