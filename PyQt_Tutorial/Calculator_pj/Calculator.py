import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
class MyApp(QMainWindow):
    number = ''
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('My Calculator')
        self.statusBar().showMessage('대기 중')
        
        self.label_num = QLabel(MyApp.number, self)
        self.label_num.move(40,40)
        font_num = self.label_num.font()
        font_num.setPointSize(50)
        self.label_num.setStyleSheet("color: black;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"  
                             "border-radius: 3px")
        self.label_num.resize(150,30)
        btn1 = QPushButton('1', self)
        btn1.move(0,100)
        btn1.clicked.connect(lambda: self.add_str('1'))
        btn1.resize(55,30)

        btn2 = QPushButton('2', self)
        btn2.move(55,100)
        btn2.clicked.connect(lambda: self.add_str('2'))
        btn2.resize(55,30)

        btn3 = QPushButton('3', self)
        btn3.move(110,100)
        btn3.clicked.connect(lambda: self.add_str('3'))
        btn3.resize(55,30)

        btn4 = QPushButton('4', self)
        btn4.move(0,130)
        btn4.clicked.connect(lambda: self.add_str('4'))
        btn4.resize(55,30)

        btn5 = QPushButton('5', self)
        btn5.move(55,130)
        btn5.clicked.connect(lambda: self.add_str('5'))
        btn5.resize(55,30)

        btn6 = QPushButton('6', self)
        btn6.move(110,130)
        btn6.clicked.connect(lambda: self.add_str('6'))
        btn6.resize(55,30)

        btn7 = QPushButton('7', self)
        btn7.move(0,160)
        btn7.clicked.connect(lambda: self.add_str('7'))
        btn7.resize(55,30)

        btn8 = QPushButton('8', self)
        btn8.move(55,160)
        btn8.clicked.connect(lambda: self.add_str('8'))
        btn8.resize(55,30)

        btn9 = QPushButton('9', self)
        btn9.move(110,160)
        btn9.clicked.connect(lambda: self.add_str('9'))
        btn9.resize(55,30)
        
        btn0 = QPushButton('0', self)
        btn0.move(0, 190)
        btn0.resize(55,30)
        btn0.clicked.connect(lambda: self.add_str('0'))

        decimal = QPushButton('.', self)
        decimal.move(55, 190)
        decimal.resize(55,30)
        decimal.clicked.connect(lambda: self.add_str('.'))
        

        equals_btn = QPushButton('=', self)
        equals_btn.move(110, 190)
        equals_btn.resize(55,30)
        equals_btn.clicked.connect(lambda: self.print_num())
        
        add_btn = QPushButton('+', self)
        add_btn.move(165, 190)
        add_btn.resize(55,30)
        add_btn.clicked.connect(lambda: self.add_str('+'))

        sub_btn = QPushButton('-', self)
        sub_btn.move(165, 160)
        sub_btn.resize(55,30)
        sub_btn.clicked.connect(lambda: self.add_str('-'))

        mal_btn = QPushButton('*', self)
        mal_btn.move(165, 130)
        mal_btn.resize(55,30)
        mal_btn.clicked.connect(lambda: self.add_str('*'))
        
        div_btn = QPushButton('/', self)
        div_btn.move(165, 100)
        div_btn.resize(55,30)
        div_btn.clicked.connect(lambda: self.add_str('/'))
        
        clear_btn = QPushButton('C', self)
        clear_btn.move(0, 220)
        clear_btn.resize(55,30)
        clear_btn.clicked.connect(lambda: self.key_clean())
        #메뉴 추가
        exitaction = QAction('Exit',self)
        exitaction.setShortcut('Ctrl+Q')
        exitaction.setStatusTip('Exit Application')
        exitaction.triggered.connect(self.exit_Action)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitaction)
    
        self.center()
        self.resize(250, 300)
        self.show()

    def add_str(self,add):
        MyApp.number += add
        self.label_num.setText(MyApp.number)
        self.label_num.repaint()
    
    def print_num(self):
        try:
            print(eval(MyApp.number))
            MyApp.number = '=' + str(eval(MyApp.number))
            self.label_num.setText(MyApp.number)
            self.label_num.repaint()
            MyApp.number = ''
        except SyntaxError:
            self.label_num.setText('올바른 식을 입력해주세요!')
            self.label_num.repaint()
            MyApp.number = ''

    def exit_Action(self):
        self.close()
        print('close')
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):         # keyboard 를 눌렀을 때 발생하는 함수, e는 입력한 key를 받는다.
        if e.key() == Qt.Key_0:    
            self.add_str('0')               
        elif e.key() == Qt.Key_1:      
            self.add_str('1')
        elif e.key() == Qt.Key_2:
            self.add_str('2')
        elif e.key() == Qt.Key_3:
            self.add_str('3')
        elif e.key() == Qt.Key_4:
            self.add_str('4')
        elif e.key() == Qt.Key_5:
            self.add_str('5')
        elif e.key() == Qt.Key_6:
            self.add_str('6')
        elif e.key() == Qt.Key_7:
            self.add_str('7')
        elif e.key() == Qt.Key_8:
            self.add_str('8')
        elif e.key() == Qt.Key_9:
            self.add_str('9')
        elif e.key() == Qt.Key_Plus:
            self.add_str('+')
        elif e.key() == Qt.Key_Minus:
            self.add_str('-')
        elif e.key() == Qt.Key_Asterisk:
            self.add_str('*')
        elif e.key() == Qt.Key_Percent:
            self.add_str('/')
        elif e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.print_num()
        elif e.key() == Qt.Key_C:  
            self.key_clean()
          

    def key_clean(self):
        MyApp.number = ''
        self.label_num.setText(MyApp.number)





    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())