import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from clock_window import *
from register_window import *

class mMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.is_odd = False


    def update_time(self):
        time = QDateTime.currentDateTime()
        time_text = time.toString("hh:mm")
        if self.is_odd:
            time_text = time_text.replace(":", " ")
            self.is_odd = False
        else:
            self.is_odd = True
        self.time_display.setText(time_text)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            #self.close()
            register_win.show()


            


class mRegisterWindow(QMainWindow, Ui_register_window):
    def __init__(self, parent = None):
        super(mRegisterWindow, self).__init__(parent)
        self.setupUi(self)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    clock_win = mMainWindow()
    register_win = mRegisterWindow()
    clock_win.show()
    sys.exit(app.exec_())
    pass