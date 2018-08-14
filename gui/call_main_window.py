import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from chat_window import *


class mMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mMainWindow, self).__init__(parent)
        self.setupUi(self)

        print(self.grid_schedule.count())


        self.add_grid("时间：", 0, 0)
        self.add_grid("83y28389", 0, 1)
        self.add_grid("事件：", 1, 0)
        self.add_grid("ndowncdow",1, 1)

        print(self.grid_schedule.count())

        item = self.grid_schedule.takeAt(3)
        w = item.widget()
        w.deleteLater()
        print(self.grid_schedule.count())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


    def add_schedule(self, schedule, row):
        self.add_grid("时间：", row, 0)
        self.add_grid(schedule.get_time(), row, 1)
        self.add_grid("事件：", row+1, 0)
        self.add_grid(schedule.get_thing(), row+1, 1)

    def add_grid(self, text, x, y):
        item = QtWidgets.QLabel()
        item.setText(text)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        item.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(75)
        item.setFont(font)
        item.setObjectName("item_" + str(x) + "_" + str(y))
        print("item_" + str(x) + "_" + str(y))
        self.grid_schedule.addWidget(item, x, y,)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    chat_win = mMainWindow()
    #chat_win.setWindowFlags(Qt.FramelessWindowHint)
    
    chat_win.show()
    sys.exit(app.exec_())
    pass
