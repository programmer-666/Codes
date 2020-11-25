import sys
from PyQt5 import QtWidgets
from random import randint

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
        # Table #
        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        self.table.resize(250, 500)
        #self.table.setVerticalHeaderLabels(("Name", "Hash"))
        self.table.setHorizontalHeaderLabels(("Id", "RSA"))
        x = 117
        self.table.setColumnWidth(0, x)# col no, width
        self.table.setColumnWidth(1, x)# col no, width
        self.table.doubleClicked.connect(self.dclk)
        # Table #
        # Button #
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Add Random")
        self.btn.move(250, 0)
        self.btn.clicked.connect(self.tablefuller)
        # Button #
    def dclk(self):
        """
        tabloya dclick ile veri girişi yapmak için 2 metot kullanılabilir.
        1-hücreye çift tıklandığında ekrana gelen dialog
        2-hücreye veri girişi yapıldıktan sonra güncelle butonu gibi bir buton sayesinde girilen veriler kayıt edilebilir. 
        """
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Veri Ekle","", QtWidgets.QLineEdit.Normal, "")
        self.table.setItem(self.table.currentRow(), self.table.currentColumn(), QtWidgets.QTableWidgetItem(str(text)))
    def tablefuller(self):
        row, col = 100, 2
        for i in range(row):
            for j in range(col):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(randint(0, 1000000))))
    def ShowWindow(self):
        self.show()
        sys.exit(self.application.exec_())

if __name__ == "__main__":
    MainWindow().ShowWindow()