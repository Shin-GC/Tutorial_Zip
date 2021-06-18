import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
    QToolTip.setFont(QFont('SansSerif',10))
    self.setToolTip('Tool Tip Text -self') #이건 왜 있는거지..?

    btn = QPushButton('Btn', self) #이 버튼 (btn)은 QPushButton 클래스의 인스턴스입니다.
    #생성자 (QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다.
    btn.setToolTip('Tool Tip Text -btn')
    
    btn.move(110, 140)
    btn.resize(btn.sizeHint())
    btn.clicked.connect(QCoreApplication.instance().quit)
    #instance() 메서드는 현재 인스턴스를 반환합니다.
    #'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
    #이렇게 발신자 (Sender)와 수신자 (Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
    self.setWindowTitle('Quit Button')
    self.setGeometry(300, 300, 300, 200)
    self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())