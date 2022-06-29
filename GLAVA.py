from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dope import *
from SECHAND import *
from tri import *
from PyQt5.QtGui import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI(self):
        self.hello = QLabel(txt_hello)
        self.instr = QLabel(txt_instr)
        self.but = QPushButton(txt_but)
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.hello,alignment = Qt.AlignCenter)
        self.lay.addWidget(self.instr,alignment = Qt.AlignCenter)
        self.lay.addWidget(self.but,alignment = Qt.AlignCenter)
        self.setLayout(self.lay)
    def connects(self):
        self.but.clicked.connect(self.next_click)
    def next_click(self):
        self.tw = TestWin()
        self.hide()

app = QApplication([])
mw = MainWin()
app.exec_()