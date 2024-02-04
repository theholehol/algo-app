# напиши здесь код для второго экрана приложения
import os

from final_win import *
from PyQt5.QtWidgets import *

class second_win(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()

        self.show()

    def set_appear(self):
        self.setWindowTitle("theholehol")
        self.resize(1000,600)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.text1 = QLabel("12345678:")
        self.text2 = QLabel("12345678:")
        self.text3 = QLabel("1234\n5678.")
        self.text4 = QLabel("1234\n5678.")
        self.text5 = QLabel("12\n34\n56\n78.")

        self.button1 = QPushButton("Начать первый тест")
        self.button2 = QPushButton("Начать делать пресидания")
        self.button3 = QPushButton("Начать финальный тест")
        self.button4 = QPushButton("отправить результаты")

        self.line_edit1 = QLineEdit("Ф.И.О.")
        self.line_edit2 = QLineEdit("0")
        self.line_edit3 = QLineEdit("0")
        self.line_edit4 = QLineEdit("0")
        self.line_edit5 = QLineEdit("0")
        
        self.l_line.addWidget(self.text1)
        self.l_line.addWidget(self.line_edit1)
        self.l_line.addWidget(self.text2)
        self.l_line.addWidget(self.line_edit2)
        self.l_line.addWidget(self.text3)
        self.l_line.addWidget(self.button1)
        self.l_line.addWidget(self.line_edit3)
        self.l_line.addWidget(self.text4)
        self.l_line.addWidget(self.button2)
        self.l_line.addWidget(self.text5)
        self.l_line.addWidget(self.button3)
        self.l_line.addWidget(self.line_edit4)
        self.l_line.addWidget(self.line_edit5)
        
        self.l_line.addWidget(self.button4)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    def connects(self):
        self.button4.clicked.connect( self.next_click)

    def next_click(self):
        self.hide()
        self.tw = final_win()
        os.error()

app = QApplication([])
mw = second_win()
app.exec_()
