import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        # super = 자식 클래스에서 부모클래스의 내용을 사용하고 싶을경우 사용
        self.initUI() 

    def initUI(self): #초기 UI 설정
        self.setWindowTitle('My First Application') #창 재목
        self.setWindowIcon(QIcon('/Users/shin/Desktop/python/title.png')) #QIcon 을 이용하여 타이틀바에 아이콘 넣기
        self.move(500, 200) # 위젯이 나오는 위치 설정                           #! 다만 맥에서는 보이지 않는다..
        self.resize(500, 500) #위젯의 크기
        
        self.show() # 위젯을 스크린에 보여준다.


if __name__ == '__main__':  #여기가 메인일시 시작
   app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 객체를 생성해야 한다.
   # sys.argv 인자는 현재 작업중인 .py파일의 절대경로를 인자로 넣어주는 것으로  객체가 실행할 파일이 현재 파이썬 코드라는것을 알려주는 것으로 생각할 수 있다.
   ex = MyApp() # 
   sys.exit(app.exec_())
   
   #이 객체를 생성만 하면, python은 “나는 할 일 다했어.” 라고 생각을 하고 프로그램을 종료하는데, 
   #나는 이 프로그램이 종료되길 원하는 것이 아니라, 내가 어떠한 명령을 취할때 그에 맞는 행동을 해주길 기대하기 때문에, 대기 상태에 있어야 한다. 
   # 즉 프로그램이 꺼지면 안되는데, 이를 구현하기 위해 무한 루프상태로 만들게 되는데 그것이 바로 app.exec_() 이다. 
   # execute의 약자이며, app이 종료되면 0을 return한다.
   # 이 return된 0을 sys.exit(0)로 받으면 python은 루프에서 빠져나와 정상종료를 하게된다.
   # app생성 -> app무한루프 -> 무한루프 탈출 시 → 정상종료 sys.exit(0)

