import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from msg_box import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = QWidget()
    msg_box = Ui_Form()
    msg_box.setupUi(ex)
    msg_box.ask_text.setText("hahah")
    ex.show()
    sys.exit(app.exec_())
    pass
