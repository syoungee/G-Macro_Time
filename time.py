import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5 import uic, QtCore, QtGui
from collections import defaultdict
import win32gui, win32api

macro_list = defaultdict(list)

class ShowDialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('mouse.ui', self)

        self.timer = timer = QtCore.QTimer() # 실시간 연결
        timer.setInterval(8)
        timer.timeout.connect(self.tick)
        timer.start()

    def tick(self):  # 마우스 위치 실시간 받기
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowDialog()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

    sys.exit(app.exec_())
