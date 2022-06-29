from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from dope import *
from tri import *
from PyQt5.QtGui import *
class Xpshka():
    def __init__(self,fio ,yo,t1,t2,t3):
        self.fio = fio
        self.yo = int(yo)
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.state = 0
    def set_appear(self):
        self.setWindowTitle(title_text)
        self.resize(win_w,win_h)
        self.move(win_x,win_y)
    def initUI(self):
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
        self.hearth12 = QLineEdit(txt_hearth12)
        self.final_but = QPushButton(txt_final_but)
        self.timer_lab = QLabel(txt_timer)
        self.gay = QVBoxLayout()
        self.gay.addWidget(self.tfio,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.fio,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.tyo,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.yo,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.instr1,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.but1,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.hearth1,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.instr2,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.but2,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.timer_lab,alignment = Qt.AlignRight)
        self.timer_lab.setFont(QFont('Times',36,QFont.Bold))
        self.gay.addWidget(self.instr3,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.but3,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.hearth11,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.hearth12,alignment = Qt.AlignLeft)
        self.gay.addWidget(self.final_but,alignment = Qt.AlignCenter)
        self.setLayout(self.gay)
    def connects(self):
        self.final_but.clicked.connect(self.next_click)
        
        self.but1.clicked.connect(self.timer1_save)
        self.but2.clicked.connect(self.timer2_save)
        self.but3.clicked.connect(self.timer3_save)



    def next_click(self):
        self.xp = Xpshka(self.fio.text(),self.yo.text(),self.hearth1.text(),self.hearth11.text(),self.hearth12.text())
        self.ew = EndWin(self.xp)
        self.hide()
        
    def timer1_save(self):
        if self.state == 0:
            self.state = 1
            global time
            time = QTime(0,0,15)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer1Event)
            self.timer.start(1000)
        

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))

        self.timer_lab.setStyleSheet('color: rgb(0,0,244)')
        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()
            self.state = 0
    
    def timer2_save(self):
        if self.state == 0:
            self.state = 1
            global time
            time = QTime(0,0,30)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer2Event)
            self.timer.start(1000)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))

        self.timer_lab.setStyleSheet('color: rgb(0,220,0)')
        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()
            self.state = 0
    def timer3_save(self):
        if self.state == 0:
            self.state = 1
            global time
            time = QTime(0,1,0)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer3Event)
            self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_lab.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timer_lab.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timer_lab.setStyleSheet('color: rgb(0,255,0)')
        else:    
            self.timer_lab.setStyleSheet('color: rgb(0,0,0)')

        if time.toString('hh:mm:ss') <= '00:00:00':
            self.timer.stop()
            self.state = 0



    



