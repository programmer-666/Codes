import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Main_window(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(Main_window, self).__init__()
        self.setWindowTitle("First app wit class")
        self.setGeometry(500, 500, 500, 300)
        self.initUi()
    def initUi(self):
        self.lw = QtWidgets.QListWidget(self)
        self.lw.resize(200, 300)
        self.lw.addItem("Python")
        self.lw.addItem("Cpp")
        self.lw.addItems(["C", "Php"])
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(200, 0)
        self.btn.setText("Add item")
        self.btn.clicked.connect(self.adit)
        self.eb = QtWidgets.QPushButton(self)
        self.eb.move(200, 45)
        self.eb.setText("Edit")
        self.eb.clicked.connect(self.editit)
        self.de = QtWidgets.QPushButton(self)
        self.de.move(200, 90)
        self.de.setText("Remove")
        self.de.clicked.connect(self.rem)
        self.srt = QtWidgets.QPushButton(self)
        self.srt.move(200, 135)
        self.srt.setText("Sort")
        self.srt.clicked.connect(self.srtit)
    def srtit(self):
        self.lw.sortItems()
    def rem(self):
        item = self.lw.takeItem(self.lw.currentRow())
        del item
        
    def adit(self):
        text, okproc = QtWidgets.QInputDialog.getText(self, "Add Item", "Input same text:")
        if text and okproc != "":
            self.lw.insertItem(0, text)
            self.showerr()
    def editit(self):
        index = self.lw.currentRow()
        item = self.lw.item(index)
        if item != "":
            t,o = QtWidgets.QInputDialog.getText(self, "Edit", "Input a text", QtWidgets.QLineEdit.Normal, item.text())
            if t and o:
                item.setText(t)
    def showerr(self):
        mbx = QtWidgets.QMessageBox(self)
        mbx.setText("Warning")
        mbx.exec_()
    def  ShowTime(self):
        self.show()
        sys.exit(self.app.exec_())

testw = Main_window()
testw.ShowTime()