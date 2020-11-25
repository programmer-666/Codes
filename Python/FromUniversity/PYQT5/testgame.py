import sys
from PyQt5 import QtWidgets
class game(QtWidgets.QMainWindow):
    def __init__(self):
        self.ap = QtWidgets.QApplication(sys.argv)
        super(game, self).__init__()
        self.setGeometry(100,100,200,200)
        self.conts()
        self.x = 50
        self.y = 50
    def moving(self):
        self.x+=10
        self.obj1.move(self.x, self.y)
    def conts(self):
        self.obj1 = QtWidgets.QLabel(self)
        self.obj1.setText("0")
        self.obj1.move(50,50)
        # object
        self.rb = QtWidgets.QPushButton(self)
        self.rb.clicked.connect(self.moving)
        # movement
    def showtime(self):
        self.show()
        sys.exit(self.ap.exec_())
test = game()
test.showtime()