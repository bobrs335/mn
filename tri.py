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
        if self.data.yo == 13 or self.data.yo == 14:
            if self.index >= 16.5:
                return txt_res1
            if self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            if self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            if self.index >= 2 and self.index <=7.4:
                return txt_res4
            if self.index <= 1.9:
                return txt_res5
        if self.data.yo == 11 or self.data.yo == 12:
            if self.index >= 18:
                return txt_res1
            if self.index >= 14 and self.index <= 17.9:
                return txt_res2
            if self.index >= 9 and self.index <= 13.9:
                return txt_res3
            if self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            if self.index <= 3.4:
                return txt_res5
        if self.data.yo == 9 or self.data.yo == 10:
            if self.index >= 19.5:
                return txt_res1
            if self.index >= 15.5 and self.index <= 19.4:
                return txt_res2
            if self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            if self.index >= 5 and self.index <= 10.4:
                return txt_res4
            if self.index <= 4.9:
                return txt_res5
        if self.data.yo == 7 or self.data.yo == 8:
            if self.index >= 21:
                return txt_res1
            if self.index >= 17 and self.index <= 20.9:
                return txt_res2
            if self.index >= 12 and self.index <= 16.9:
                return txt_res3
            if self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            if self.index <= 6.4:
                return txt_res5
        



