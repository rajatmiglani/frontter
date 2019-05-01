# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow3(object):
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")
        Window3.resize(847, 548)
        self.centralwidget = QtWidgets.QWidget(Window3)
        self.centralwidget.setObjectName("centralwidget")
        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setGeometry(QtCore.QRect(290, 190, 261, 51))
        self.pbar.setProperty("value", 24)
        self.pbar.setObjectName("pbar")
        self.scoreText = QtWidgets.QLabel(self.centralwidget)
        self.scoreText.setGeometry(QtCore.QRect(400, 270, 60, 16))
        self.scoreText.setObjectName("scoreText")
        Window3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 22))
        self.menubar.setObjectName("menubar")
        Window3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window3)
        self.statusbar.setObjectName("statusbar")
        Window3.setStatusBar(self.statusbar)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "MainWindow"))
        self.scoreText.setText(_translate("Window3", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(Window3)
    Window3.show()
    sys.exit(app.exec_())

