import sys

from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication

from theverytest import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.adding)
        self.show()

    def adding(self):
        self.ui.listWidget.addItem("double ||")
        self.ui.listWidget.addItem("clicked ||")
        self.ui.listWidget.addItem("vaow    ||")
        self.ui.listWidget.addItem("vao       ||")
        self.ui.listWidget.addItem("va         ||")
        self.ui.listWidget.addItem("1           ||")
        self.ui.listWidget.addItem("clicked ||")
        self.ui.listWidget.addItem("double ||")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())