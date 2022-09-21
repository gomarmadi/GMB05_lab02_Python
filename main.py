import math
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('GMB05_lab02')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.label_img.setPixmap(QPixmap('Main.png'))
        self.label_img.setScaledContents(True)

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x >= 5:
                answer = x * (math.pow(a,2) + math.pow(b,2)) / 6 * a
            else:
                answer = 6 * a * b - 5 * x
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
            self.label_answer.setStyleSheet("background: rgb(0, 255, 0,0.5);")
        except:
            self.label_answer.setText('Ошибка!')
            self.label_answer.setStyleSheet('background: rgb(255, 0, 0, 0.5);')
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')
        self.label_answer.setStyleSheet('')

app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
