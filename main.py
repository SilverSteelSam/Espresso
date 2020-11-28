import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.db = sqlite3.connect('coffee.db')
        self.cur = self.db.cursor()
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
        self.editbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refreshbtn.setFont(font)
        self.editbtn.setFont(font)
        self.refreshbtn.setObjectName("refreshbtn")
        self.editbtn.setObjectName("editbtn")
        self.verticalLayout.addWidget(self.refreshbtn)
        self.verticalLayout.addWidget(self.editbtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.refreshbtn.clicked.connect(self.Refresh)
        self.editbtn.clicked.connect(self.Edit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshbtn.setText(_translate("MainWindow", "Refresh"))
        self.editbtn.setText(_translate("MainWindow", "Edit"))

    def Refresh(self):
        res = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.listWidget.clear()
        self.listWidget.addItems(['Name, Roast, Grounded, Taste, Price, Vollume'] + [', '.join(el) for el in res])

    def Edit(self):
        try:
            widget = Ui_add_edit(self)
            widget.show
        except Exception as e:
            print(e)
    
class Ui_add_edit(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        self.db = MainWindow.db
        self.cur = self.db.cursor()
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_btn.clicked.connect(self.Add)

    def Add(self):
        lst = [self.name]
        print(lst)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
