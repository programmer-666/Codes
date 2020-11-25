from PyQt5 import QtWidgets
import sys
from sayapple import Ui_MainWindow

class wdow(QtWidgets.QMainWindow):
    def __init__(self):
        super(wdow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.apple)
    def apple(self):
        self.ui.label.setText("Apple!")
pla = QtWidgets.QApplication(sys.argv)
test = wdow()
test.show()
sys.exit(pla.exec_())