from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dope import *

class EndWin(QWidget):
    def __init__(self,data):
        super().__init__()
        self.data = data
        self.set_appear()
        self.initUI()
        self.show()       
        self.results()
    def set_appear(self):
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI(self):
        self.induk = QLabel('Индекс Руфье:' )
        self.work = QLabel('Работоспособность сердца:')
        self.day = QVBoxLayout()
        self.day.addWidget(self.induk, alignment = Qt.AlignCenter)
        self.day.addWidget(self.work, alignment = Qt.AlignCenter)
        self.setLayout(self.day)
    def results(self):
        #self.index = ((4*(int(self.data.t1)+int(self.data.t2)+int(self.data.t3))-200)/10)
        self.index = ((4*((60+80+90)-200))/10)
        self.induk.setText('Индекс Руфье:'+str(self.index))
        
        self.work.setText('Работоспособность сердца:'+self.ifi())
    def ifi(self):
        if self.data.yo >= 15:
            if self.index >= 15:
                return txt_res1
            if self.index <= 14.9 and self.index >= 11:
                return txt_res2
            if self.index <= 10.9 and self.index >= 6:
                return txt_res3
            if self.index <= 5.9 and self.index >= 0.5:
                return txt_res4
            if self.index <= 0.4:
                return txt_res5
        



