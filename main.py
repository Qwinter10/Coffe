import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
