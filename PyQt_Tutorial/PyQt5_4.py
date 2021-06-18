import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()  

    def initUI(self):
        self.statusBar().showMessage('Ready')

        QToolTip.setFont(QFont('SansSerif',15))
        self.setToolTip('setToolTip')
        
        btn = QPushButton('종료', self)
        btn.setToolTip('btn.setToolTip')

        btn.move(235,145)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    
    sys.exit(app.exec_())