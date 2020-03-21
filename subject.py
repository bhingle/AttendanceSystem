# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#from newSem import Ui_Sem
from final_table import  *
from PyQt5 import QtCore, QtGui, QtWidgets
tableName=[]

class Ui_sub(object):
    '''def openWindow(self):
        #print(*tableName)
        self.window = QtWidgets.QMainWindow()

        self.ui = Ui_table(tableName)
        self.ui.setupUi(self.window)
        sub.hide()
        self.window.show()'''
    def AOA1(self):
        tableName.append("AOA")
        self.sub_selected.setText("AOA")
    def JAN1(self):
        tableName.append("JAN")
        self.month_selected.setText("JAN")

    def CG1(self):
        tableName.append("CG")
        self.sub_selected.setText("CG")
    def FEB1(self):
        tableName.append("FEB")
        self.month_selected.setText("FEB")

    def COA1(self):
        tableName.append("COA")
        self.sub_selected.setText("COA")
    def MAR1(self):
        tableName.append("MAR")
        self.month_selected.setText("MAR")

    def OS1(self):
        tableName.append("OS")
        self.sub_selected.setText("OS")
    def APR1(self):
        tableName.append("APR")
        self.month_selected.setText("APR")

    def MATH1(self):
        tableName.append("MATH4")
        self.sub_selected.setText("MATH4")
    def MAY1(self):
        tableName.append("MAY")
        self.month_selected.setText("MAY")

    def setupUi(self,sub):
        sub.setObjectName("sub")
        sub.resize(1376, 768)
        self.centralwidget = QtWidgets.QWidget(sub)
        self.centralwidget.setObjectName("centralwidget")
        self.AOA = QtWidgets.QPushButton(self.centralwidget)
        self.AOA.setGeometry(QtCore.QRect(350, 140, 89, 25))
        self.AOA.setObjectName("AOA")

        self.AOA.clicked.connect(self.AOA1)

        self.CG = QtWidgets.QPushButton(self.centralwidget)
        self.CG.setGeometry(QtCore.QRect(350, 190, 89, 25))
        self.CG.setObjectName("CG")

        self.CG.clicked.connect(self.CG1)

        self.COA = QtWidgets.QPushButton(self.centralwidget)
        self.COA.setGeometry(QtCore.QRect(350, 240, 89, 25))
        self.COA.setObjectName("COA")

        self.COA.clicked.connect(self.COA1)

        self.MATH_4 = QtWidgets.QPushButton(self.centralwidget)
        self.MATH_4.setGeometry(QtCore.QRect(350, 290, 89, 25))
        self.MATH_4.setObjectName("MATH_4")

        self.MATH_4.clicked.connect(self.MATH1)

        self.OS = QtWidgets.QPushButton(self.centralwidget)
        self.OS.setGeometry(QtCore.QRect(350, 340, 89, 25))
        self.OS.setObjectName("OS")

        self.OS.clicked.connect(self.OS1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 70, 300, 30))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("Ubuntu", 20))

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(650, 70, 151, 17))
        self.label1.setObjectName("label1")
        self.JAN = QtWidgets.QPushButton(self.centralwidget)
        self.JAN.setGeometry(QtCore.QRect(650, 140, 89, 25))
        self.JAN.setObjectName("JAN")

        self.JAN.clicked.connect(self.JAN1)

        self.FEB = QtWidgets.QPushButton(self.centralwidget)
        self.FEB.setGeometry(QtCore.QRect(650, 190, 89, 25))
        self.FEB.setObjectName("FEB")

        self.FEB.clicked.connect(self.FEB1)

        self.MAR = QtWidgets.QPushButton(self.centralwidget)
        self.MAR.setGeometry(QtCore.QRect(650, 240, 89, 25))
        self.MAR.setObjectName("MAR")

        self.MAR.clicked.connect(self.MAR1)

        self.APR = QtWidgets.QPushButton(self.centralwidget)
        self.APR.setGeometry(QtCore.QRect(650, 290, 89, 25))
        self.APR.setObjectName("APR")

        self.APR.clicked.connect(self.APR1)

        self.MAY = QtWidgets.QPushButton(self.centralwidget)
        self.MAY.setGeometry(QtCore.QRect(650, 340, 89, 25))
        self.MAY.setObjectName("MAY")

        self.MAY.clicked.connect(self.MAY1)

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(800, 400, 89, 25))
        self.next.setObjectName("next")
        sub.setCentralWidget(self.centralwidget)
        self.next.clicked.connect(self.table_scr)



        self.sub_selected = QtWidgets.QTextEdit(self.centralwidget)
        self.sub_selected.setGeometry(QtCore.QRect(330, 390, 104, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sub_selected.setFont(font)
        self.sub_selected.setObjectName("sub_selected")

        self.month_selected = QtWidgets.QTextEdit(self.centralwidget)
        self.month_selected.setGeometry(QtCore.QRect(650, 390, 104, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.month_selected.setFont(font)
        self.month_selected.setObjectName("month_selected")

        sub.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sub)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        sub.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sub)
        self.statusbar.setObjectName("statusbar")
        sub.setStatusBar(self.statusbar)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(350, 600, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back.setFont(font)
        self.back.setObjectName("back")

        self.back.clicked.connect(lambda :self.close_scr(sub))

        self.retranslateUi(sub)
        QtCore.QMetaObject.connectSlotsByName(sub)

    def close_scr(self,sub):
        sub.hide()
    def table_scr(self):
        self.table = QtWidgets.QMainWindow()
        self.ui = Ui_table(tableName)
        self.ui.setupUi(self.table)
        self.table.show()

    def retranslateUi(self, sub):
        _translate = QtCore.QCoreApplication.translate
        sub.setWindowTitle(_translate("sub", "subject"))
        self.AOA.setText(_translate("sub", "AOA"))
        self.CG.setText(_translate("sub", "CG"))
        self.COA.setText(_translate("sub", "COA"))
        self.MATH_4.setText(_translate("sub", "MATH_4"))
        self.label.setText(_translate("sub", "SELECT SUBJECT"))
        self.OS.setText(_translate("sub", "OS"))

        self.label1.setText(_translate("sub", "SELECT MONTH"))
        self.JAN.setText(_translate("sub", "JAN"))
        self.FEB.setText(_translate("sub", "FEB"))
        self.MAR.setText(_translate("sub", "MAR"))
        self.APR.setText(_translate("sub", "APR"))
        self.MAY.setText(_translate("sub", "MAY"))
        self.next.setText(_translate("sub", "NEXT"))
        self.back.setText(_translate("sub", "BACK"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sub = QtWidgets.QMainWindow()
    ui = Ui_sub()
    ui.setupUi(sub)
    sub.show()
    sys.exit(app.exec_())'''
