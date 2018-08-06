#!python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Example Icon")
        self.setWindowIcon(QIcon("app.png"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Example()
    sys.exit(app.exec_())
