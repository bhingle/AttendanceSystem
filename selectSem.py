# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sem.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from subject import *

class Ui_Sem(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_sub()
        self.ui.setupUi(self.window)
        Sem.hide()
        self.window.show()
    def setupUi(self, Sem):
        Sem.setObjectName("Sem")
        Sem.resize(1376, 768)
        self.centralwidget = QtWidgets.QWidget(Sem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 90, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(300, 230, 251, 231))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.three.setFont(font)
        self.three.setObjectName("three")

        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(800, 230, 251, 231))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.four.setFont(font)
        self.four.setObjectName("four")

        self.four.clicked.connect(self.openWindow)

        Sem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Sem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sem)
        self.statusbar.setObjectName("statusbar")
        Sem.setStatusBar(self.statusbar)

        self.retranslateUi(Sem)
        QtCore.QMetaObject.connectSlotsByName(Sem)

    def retranslateUi(self, Sem):
        _translate = QtCore.QCoreApplication.translate
        Sem.setWindowTitle(_translate("Sem", "Sem"))
        self.label.setText(_translate("Sem", "SELECT SEMESTER"))
        self.three.setText(_translate("Sem", "III"))
        self.four.setText(_translate("Sem", "IV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sem = QtWidgets.QMainWindow()
    ui = Ui_Sem()
    ui.setupUi(Sem)
    Sem.show()
    sys.exit(app.exec_())

