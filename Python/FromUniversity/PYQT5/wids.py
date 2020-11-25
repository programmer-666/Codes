#!/usr/bin/python3
# -*- coidng: utf-8 -*-
#wids.py
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
class Test(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.win = QtWidgets.QMainWindow()
        self.win.setWindowTitle("Testing Title")
        self.win.setGeometry(710, 310, 500, 500) # x,y, width, height
        self.win.setWindowIcon(QIcon('test.png')) # icon atama
        self.win.setToolTip("Tools")
        # Label
        self.lbl = QtWidgets.QLabel(self.win)
        self.lbl1 = QtWidgets.QLabel(self.win)
        self.lbl.setText("Deneme")
        self.lbl1.setText("Deneme1")
        self.lbl.move(20, 10) # x y
        self.lbl1.move(20, 30) # x y
        # Label
        # lineedit
        self.tx = QtWidgets.QLineEdit(self.win)
        self.tx.move(20, 55)
        # lineedit
        # pushbutton
        self.btn = QtWidgets.QPushButton(self.win)
        self.btn.move(20, 80)
        self.btn.setText("pButton")
        self.btn.clicked.connect(self.printm)
        # pushbutton
    def show_window(self):
        self.win.show()
    def printm(self):
        print(self.tx.text())
    def execs(self):
        sys.exit(self.app.exec_()) # X butonuna basildiginda uygulama kapanir
t = Test()
t.show_window()
t.execs()