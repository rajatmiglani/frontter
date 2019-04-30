# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Window1
import requests
class Ui_Window2(object):
    def loginwithc(self):
        user="sd"
        val=3 ##Implies for c
        user = self.code.toPlainText()
        f=open("input.txt","w")
        f.write("3"+'\n')
        f.close()
        f=open("input.txt","a")
        f.write(user)
        f.close()
    #print(user)       Just for debugging
    def loginwithpy(self):
        val=1 ##Implies for python
        user=self.code.toPlainText()
        f=open("input.txt","w")
        f.write("1"+'\n')
        f.close()
        f=open("input.txt","a")
        f.write(user)
        f.close()
    
    def loginwithcpp(self):
        val=2 ##Implies for cpp
        user=self.code.toPlainText()
        f=open("input.txt","w")
        f.write("2"+'\n')
        f.close()
        f=open("input.txt","a")
        f.write(user)
        f.close()
    
    def logout(self):
        print("Success")
        #self.welcomeWindow = QtWidgets.QMainWindow()
        #self.ui=Ui_MainWindow()
        #self.ui=Ui_Window1()
        #self.ui.setupUi(self.welcomeWindow)
        #self.welcomeWindow.show()
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(1003, 740)
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.Question = QtWidgets.QLabel(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(10, 30, 841, 41))
        self.Question.setObjectName("Question")
        self.scroller = QtWidgets.QScrollArea(self.centralwidget)
        self.scroller.setGeometry(QtCore.QRect(20, 70, 841, 441))
        self.scroller.setWidgetResizable(True)
        self.scroller.setObjectName("scroller")
        self.scrollContents = QtWidgets.QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 839, 439))
        self.scrollContents.setObjectName("scrollContents")
        self.code = QtWidgets.QPlainTextEdit(self.scrollContents)
        self.code.setGeometry(QtCore.QRect(0, 0, 841, 441))
        self.code.setObjectName("code")
        self.scroller.setWidget(self.scrollContents)
        
        self.submitwithc = QtWidgets.QPushButton(self.centralwidget)
        self.submitwithc.setGeometry(QtCore.QRect(682, 540, 151, 32))
        self.submitwithc.setObjectName("submitwithc")
        ## Submit with C function
        self.submitwithc.clicked.connect(self.loginwithc)
        ##
        self.submitwithpy = QtWidgets.QPushButton(self.centralwidget)
        self.submitwithpy.setGeometry(QtCore.QRect(70, 540, 151, 32))
        self.submitwithpy.setObjectName("submitwithpy")
        ## Submit with Python
        self.submitwithpy.clicked.connect(self.loginwithpy)
        ##
        self.submitwithcpp = QtWidgets.QPushButton(self.centralwidget)
        self.submitwithcpp.setGeometry(QtCore.QRect(372, 540, 151, 32))
        self.submitwithcpp.setObjectName("submitwithcpp")
        ##Submit with cpp
        self.submitwithcpp.clicked.connect(self.loginwithcpp)
        ##
        
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(700, 610, 113, 32))
        self.logout.setObjectName("logout")
        ##Logout button
        self.logout.clicked.connect(self.logout)
        
        Window2.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Window2)
        self.statusBar.setObjectName("statusBar")
        Window2.setStatusBar(self.statusBar)
        self.actionRun = QtWidgets.QAction(Window2)
        self.actionRun.setObjectName("actionRun")
        self.actionExit = QtWidgets.QAction(Window2)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "MainWindow"))
        URL="http://127.0.0.1:8000/quiz/"
        PARAMS={}
        r=requests.get(url=URL)
        #print(r.text)
        q=r.text
        q=q[10:]
        q=q[:-3]
        #print(q)

        self.Question.setText(_translate("Window2", q))
       # self.Question.setText(_translate("Window2", "Question: Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’?"))
        self.submitbutton.setText(_translate("Window2", "Submit"))
        self.actionRun.setText(_translate("Window2", "Run"))
        self.actionExit.setText(_translate("Window2", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2 = QtWidgets.QMainWindow()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    Window2.show()
    sys.exit(app.exec_())

