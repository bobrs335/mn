from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dope import *

class EndWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI(self):
        self.induk = QLabel('Индекс Руфье:' + txt_ind)
        self.work = QLabel('Работоспособность сердца:' + txt_work)
        self.day = QVBoxLayout()
        self.day.addWidget(self.induk, alignment = Qt.AlignCenter)
        self.day.addWidget(self.work, alignment = Qt.AlignCenter)
        self.setLayout(self.day)


