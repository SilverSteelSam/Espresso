import sys
import sqlite3
from PyQt5 import uic  
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        self.db = sqlite3.connect('coffee.db')
        self.cur = self.db.cursor()
        super().__init__()
        uic.loadUi('main.ui', self)  
        self.find_btn.clicked.connect(self.find)
        self.add_btn.clicked.connect(self.add)
        self.set_btn.clicked.connect(self.set)

    def add(self):
        lst = [self.name.displayText(), self.roast.displayText(), self.beans.displayText(),
               self.taste.displayText(), self.price.displayText(), self.volume.displayText()]
        if all(lst):
            zap = """INSERT INTO coffee(name,roast,ground/beans,taste,price,package_vollume) VALUES(?,?,?,?,?,?)"""
            print(zap)
            self.cur.execute(zap, lst)
            self.db.commit()


    def set(self):
        pass
        
    def find(self):
        name = self.name.displayText()
        names = [el[0] for el in self.cur.execute('''SELECT name FROM coffee''').fetchall()]
        if self.name.displayText() and name in names:
            zap = """SELECT * FROM coffee WHERE name = '{}'""".format(name)
            lst = self.cur.execute(zap).fetchall()[0]
            self.roast.setText(lst[2])
            self.beans.setText(lst[3])
            self.taste.setText(lst[4])
            self.price.setText(lst[5])
            self.volume.setText(lst[2])
        else:
            self.roast.setText('None')
            self.beans.setText('None')
            self.taste.setText('None')
            self.price.setText('None')
            self.volume.setText('None')
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
