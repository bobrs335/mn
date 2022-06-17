from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear():
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI():
        self.tfio = QLabel(txt_tfio)
        self.fio = QLineEdit(txt_fio)
        self.tyo = QLabel(txt_tyo)
        self.yo = QLineEdit(txt_yo)
        self.instr1 = QLabel(txt_instr1)
        self.but1 = QPushButton(txt_but1)
        self.hearth1 = QLineEdit(txt_hearth1)
        self.instr2 = QLabel(txt_instr2)
        self.but2 = QPushButton(txt_but2)
        self.instr3 = QLabel(txt_instr3)
        self.but3 = QPushButton(txt_but3)
        self.hearth11 = QLineEdit(txt_hearth11)
        self.hearht12 = QlineEdit(txt_hearth12)
        self.final_but = QPushButton(txt_final_but)
        self.timer = QLabel(txt_timer)



