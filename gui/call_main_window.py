import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from talking_window import *


class mMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    talking_win = mMainWindow()
    talking_win.show()
    sys.exit(app.exec_())
    pass
