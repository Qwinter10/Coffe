import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM tastes''').fetchall()

        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Сорт", "Степень обжарки", "Молотый/в зёрнах",
                                                    "Описание вкуса", "Цена", "Объём упаковки"])

        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
