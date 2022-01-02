import sys

from PyQt5.QtWidgets import QDialog, QApplication

from calculator1 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button1.clicked.connect(self.num1)
        self.ui.button2.clicked.connect(self.num2)
        self.ui.button3.clicked.connect(self.num3)
        self.ui.button4.clicked.connect(self.num4)
        self.ui.button5.clicked.connect(self.num5)
        self.ui.button6.clicked.connect(self.num6)
        self.ui.button7.clicked.connect(self.num7)
        self.ui.button8.clicked.connect(self.num8)
        self.ui.button9.clicked.connect(self.num9)
        self.ui.button0.clicked.connect(self.num0)
        self.ui.dotbutton.clicked.connect(self.makefloat)

        self.ui.addsymbol.clicked.connect(self.addnum)
        self.ui.subsymbol.clicked.connect(self.subnum)
        self.ui.mulsymbol.clicked.connect(self.mulnum)
        self.ui.divsymbol.clicked.connect(self.divnum)
        self.ui.equalsymbol.clicked.connect(self.result)

        self.ui.delsymbol.clicked.connect(self.delnum)
        self.ui.delonebyone.clicked.connect(self.deleteonebyone)
        self.ui.historylistwidget.itemClicked.connect(self.copying_data)

        self.ui.delbutton.clicked.connect(self.delhistory)
        self.ui.delallbutton.clicked.connect(self.delallhistory)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        self.showtime()
        self.show()

    """ Set count để tính mấy thứ ở dưới """
    # count = 1 là tại vì self.ui.displaycalculator đã có số 0 trước rồi nên đc thêm 1 vào
    count = 0

    """ Tạo 1 string lst để chứa history and use for display data from history """
    # cũng như cái count ở trên
    lst = ""

    # print(f"Basic: {count}")

    def num1(self):
        """ dòng này là để mình convert nhũng gì ở trên lable aka ở trên displaycalculator thành string """
        text = self.ui.displaycalculator.text()
        # print(type(text)) -> <class: str>

        """ check giá trị đầu tiên trên màn hình có phải là số 0 không ?
            Nếu phải thì thay thế số đó với các số nhập từ "bàn phím". """

        """ sử dụng count để có thể tinh giá trị rồi delonebyone """

        """ WASTED """
        # if text[0] == "0":
        #     self.ui.displaycalculator.setText("1")
        #     self.count += 1
        #     self.lst += "1"
        #
        # else:
        #     self.ui.displaycalculator.setText(text + "1")
        #     self.count += 1
        #     self.lst += "1"

        """ FIXING BUG OF BEING 0 + SOMETHING """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("1")
            self.count += 1
            self.lst += "1"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "1")
            self.count += 1
            self.lst += "1"

        # a = self.lst.split(" ")
        # print(a)

    def num2(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        # if text[0] == "0":
        #     self.ui.displaycalculator.setText("2")
        #     self.count += 1
        #     self.lst += "2"
        #
        # else:
        #     self.ui.displaycalculator.setText(text + "2")
        #     self.count += 1
        #     self.lst += "2"

        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("2")
            self.count += 1
            self.lst += "2"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "2")
            self.count += 1
            self.lst += "2"

    def num3(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("3")
            self.count += 1
            self.lst += "3"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "3")
            self.count += 1
            self.lst += "3"

    def num4(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("4")
            self.count += 1
            self.lst += "4"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "4")
            self.count += 1
            self.lst += "4"

    def num5(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("5")
            self.count += 1
            self.lst += "5"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "5")
            self.count += 1
            self.lst += "5"

    def num6(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("6")
            self.count += 1
            self.lst += "6"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "6")
            self.count += 1
            self.lst += "6"

    def num7(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("7")
            self.count += 1
            self.lst += "7"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "7")
            self.count += 1
            self.lst += "7"

    def num8(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("8")
            self.count += 1
            self.lst += "8"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "8")
            self.count += 1
            self.lst += "8"

    def num9(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """

        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("9")
            self.count += 1
            self.lst += "9"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "9")
            self.count += 1
            self.lst += "9"

        # a = self.lst.split(" ")
        # test = []
        # test.append(self.lst)
        # print(test)

    def num0(self):

        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()

        """ cũng giống 1 """
        """ sử dụng count để có thể tinh giá trị rồi delonebyone """
        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("0")
            self.count += 1
            self.lst += "0"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "0")
            self.count += 1
            self.lst += "0"

    def addnum(self):
        """ cũng giống 1 """
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " + ")
        # self.count += 3
        # self.lst += " + "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " + ")
            self.count += 4
            self.lst += "0 + "

        # FIXING TWO OPERATOR IN A ROW
        elif self.lst[-2] == "+" or self.lst[-2] == "*" or self.lst[-2] == "/":
            pass

        else:
            self.ui.displaycalculator.setText(text + " + ")
            self.count += 3
            self.lst += " + "

        # # print(len(a))

    def subnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " - ")
        # self.count += 3
        # self.lst += " - "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " - ")
            self.count += 4
            self.lst += "0 - "

        # FIXING TWO OPERATOR IN A ROW
        elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/":
            pass

        else:
            self.ui.displaycalculator.setText(text + " - ")
            self.count += 3
            self.lst += " - "

    def mulnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " * ")
        # self.count += 3
        # self.lst += " * "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " * ")
            self.count += 4
            self.lst += "0 * "

        # FIXING TWO OPERATOR IN A ROW
        elif self.lst[-2] == "+" or self.lst[-2] == "*" or self.lst[-2] == "/":
            pass

        else:
            self.ui.displaycalculator.setText(text + " * ")
            self.count += 3
            self.lst += " * "

    def divnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " / ")
        # self.count += 3
        # self.lst += " / "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " / ")
            self.count += 4
            self.lst += "0 / "

        # FIXING TWO OPERATOR IN A ROW
        elif self.lst[-2] == "+" or self.lst[-2] == "*" or self.lst[-2] == "/":
            pass

        else:
            self.ui.displaycalculator.setText(text + " / ")
            self.count += 3
            self.lst += " / "

    def result(self):

        text = self.ui.displaycalculator.text()

        ans = str(eval(text))
        self.ui.displaycalculator.setText(ans)

        self.ui.historylistwidget.addItem(f"{self.lst} = {self.ui.displaycalculator.text()}")

        """ Make the lst start with the previous ans"""
        if self.ui.displaycalculator.text() == "0":
            self.lst = ""

        else:
            self.lst = f"{self.ui.displaycalculator.text()}"
            self.count = len(self.ui.displaycalculator.text())

    def delnum(self):
        self.ui.displaycalculator.setText("0")

        """ Make the lst empty"""
        self.lst = ""
        self.count = 0

    def deleteonebyone(self):

        if self.count > 1:
            # print(f"Before: {self.count}")
            last = self.ui.displaycalculator.text()
            if last[-1] == " ":
                last = last[:-3]
                self.count -= 3
                self.lst = self.lst[:-3]

            else:
                last = last[:-1]
                self.count -= 1
                self.lst = self.lst[:-1]

            self.ui.displaycalculator.setText(last)

            # print("Delete success!")
            # print(f"After: {self.count}")

        elif self.count == 1:
            self.delnum()
            # print("Back to 0")

        # print(self.lst)

    def delhistory(self):
        self.ui.historylistwidget.takeItem(self.ui.historylistwidget.currentRow())

    def delallhistory(self):
        self.ui.historylistwidget.clear()

    def makefloat(self):
        text = self.ui.displaycalculator.text()
        deximal_num = text.split(" ")

        if "." in deximal_num[-1]:
            pass

        else:
            self.ui.displaycalculator.setText(text + ".")
            self.count += 1
            self.lst += "."

    def showtime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm:ss")
        self.ui.timelable.display(text)

    def copying_data(self):
        # self.ui.testlable.clear()
        contants = ""
        contants += self.ui.historylistwidget.currentItem().text()
        wordlist = contants.split(" ")
        wordlist.remove("=")
        wordlist.pop()
        self.ui.displaycalculator.setText(" ".join(wordlist))
        self.lst = ""
        self.lst += " ".join(wordlist)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
