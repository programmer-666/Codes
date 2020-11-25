#!/usr/bin/python3
# -*- coidng: utf-8 -*-
#first2.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
class Test(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.win = QtWidgets.QMainWindow()
        self.win.setWindowTitle("Testing Title")
        self.win.setGeometry(710, 310, 500, 500) # x,y, width, height
        self.win.setWindowIcon(QIcon('test.png')) # icon atama
        self.win.setToolTip("Tools")
    def show_window(self):
        self.win.show()
    def execs(self):
        sys.exit(self.app.exec_()) # X butonuna basildiginda uygulama kapanir
t = Test()
t.show_window()
t.execs()