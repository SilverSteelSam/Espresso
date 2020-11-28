import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget.setFont(font)
        self.verticalLayout.addWidget(self.listWidget)
        self.refreshbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refreshbtn.setFont(font)
        self.refreshbtn.setObjectName("refreshbtn")
        self.verticalLayout.addWidget(self.refreshbtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.refreshbtn.clicked.connect(self.Refresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshbtn.setText(_translate("MainWindow", "Refresh"))

    def Refresh(self):
        self.db = sqlite3.connect('coffee.db')
        self.cur = self.db.cursor()
        res = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.listWidget.clear()
        self.listWidget.addItems(['Name, Roast, Grounded, Taste, Price, Vollume'] + [', '.join(el) for el in res])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
