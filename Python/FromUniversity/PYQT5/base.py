import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Application #
        self.application = QtWidgets.QApplication(sys.argv)
        # Application #
        super(MainWindow, self).__init__()
        self.InitContents()
        # MainWindow Settings #
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("MainWindow")
        # MainWindow Settings #
    def InitContents(self):
        pass
    def ShowWindow(self):
        self.show()
        sys.exit(self.application.exec_())
if __name__ == "__main__":
    MainWindow().ShowWindow()