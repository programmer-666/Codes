# -*- coding: utf-8 -*-
import sys # Sistemle ilgili, programlara mudehale icin
from PyQt5 import QtWidgets
mainw = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("First PyQt5 Code");
window.show()
mainw.exec_()