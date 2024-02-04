# напиши здесь код третьего экрана приложения

from PyQt5.QtWidgets import *

class final_win(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.l_line = QVBoxLayout()

        self.text1 = QLabel("Индекс Руфье:")
        self.text2 = QLabel("работоспасобность сердца:")

        self.l_line.addWidget(self.text1)
        self.l_line.addWidget(self.text2)

        self.setLayout(self.l_line)

app = QApplication([])
mw = final_win()
app.exec_()

