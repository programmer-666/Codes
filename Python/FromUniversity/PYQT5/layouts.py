#grid, horizontal, vertical
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor

class Colorr(QtWidgets.QWidget):
    def __init__(self, color):
        super(Colorr, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class mainw(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainw, self).__init__()
        self.setGeometry(200,200, 800,500)
        layout = QtWidgets.QGridLayout()
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("b1")
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("b2")
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("b3")
        layout.addWidget(Colorr('red'), 0, 0)
        layout.addWidget(Colorr('blue'), 0, 1)
        layout.addWidget(Colorr('black'), 0, 2)
        #layout.setContentsMargins(20, 20, 20, 20) # saat yonu boyunca layouta margin ekler
        #layout.setSpacing(50) # widgetlar arası boşluk
        wgt = QtWidgets.QWidget()
        wgt.setLayout(layout)
        self.setCentralWidget(wgt) # layout için widget oluşturulur ve merkeze sabitlenir
        
def apl():
    apln = QtWidgets.QApplication(sys.argv)
    w = mainw()
    w.show()
    sys.exit(apln.exec_())

apl()