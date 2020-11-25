import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
class maw(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(maw, self).__init__()
        self.conts()
    def conts(self):
        self.dm = QDateTime()
        print(self.dm.currentDateTime().toString(Qt.ISODate))
        print(QDate.currentDate().toString(Qt.DefaultLocaleShortDate))
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())
t = maw()
t.showtime()