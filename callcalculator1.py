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
        self.ui.parentheses1.clicked.connect(self.bracketopen)
        self.ui.parentheses2.clicked.connect(self.bracketclose)
        self.ui.squarenum.clicked.connect(self.square)
        self.ui.equalsymbol.clicked.connect(self.result)

        self.ui.delsymbol.clicked.connect(self.delnum)
        self.ui.delonebyone.clicked.connect(self.deleteonebyone)
        self.ui.historylistwidget.itemClicked.connect(self.copying_data)

        self.ui.delbutton.clicked.connect(self.delhistory)
        self.ui.delallbutton.clicked.connect(self.delallhistory)

        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.showtime)
        # timer.start(1000)
        # self.showtime()
        self.show()

    """ Set count để tính mấy thứ ở dưới """
    # count = 1 là tại vì self.ui.displaycalculator đã có số 0 trước rồi nên đc thêm 1 vào
    count = 0

    """ Tạo 1 string lst để chứa history and use for display data from history """
    # cũng như cái count ở trên
    lst = ""

    # parentheses bug
    parentheses_sto = ""

    """ Display là của cái self.sqr_sto, còn tính là của self.lst"""
    # sqr() bug
    sqr_sto = ""

    # print(f"Basic: {count}")

    def num1(self):
        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("1")
                self.count += 1
                self.lst += "1"
                self.sqr_sto += "1"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "1")
                self.count += 1
                self.lst += "1"
                self.sqr_sto += "1"

        # a = self.lst.split(" ")
        # print(a)

    def num2(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("2")
                self.count += 1
                self.lst += "2"
                self.sqr_sto += "2"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "2")
                self.count += 1
                self.lst += "2"
                self.sqr_sto += "2"

    def num3(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("3")
                self.count += 1
                self.lst += "3"
                self.sqr_sto += "3"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "3")
                self.count += 1
                self.lst += "3"
                self.sqr_sto += "3"

    def num4(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("4")
                self.count += 1
                self.lst += "4"
                self.sqr_sto += "4"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "4")
                self.count += 1
                self.lst += "4"
                self.sqr_sto += "4"

    def num5(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("5")
                self.count += 1
                self.lst += "5"
                self.sqr_sto += "5"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "5")
                self.count += 1
                self.lst += "5"
                self.sqr_sto += "5"

    def num6(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("6")
                self.count += 1
                self.lst += "6"
                self.sqr_sto += "6"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "6")
                self.count += 1
                self.lst += "6"
                self.sqr_sto += "6"

    def num7(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("7")
                self.count += 1
                self.lst += "7"
                self.sqr_sto += "7"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "7")
                self.count += 1
                self.lst += "7"
                self.sqr_sto += "7"

    def num8(self):

        text = self.ui.displaycalculator.text()
        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("8")
                self.count += 1
                self.lst += "8"
                self.sqr_sto += "8"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "8")
                self.count += 1
                self.lst += "8"
                self.sqr_sto += "8"

    def num9(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                self.ui.displaycalculator.setText("9")
                self.count += 1
                self.lst += "9"
                self.sqr_sto += "9"

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "9")
                self.count += 1
                self.lst += "9"
                self.sqr_sto += "9"

        # a = self.lst.split(" ")
        # test = []
        # test.append(self.lst)
        # print(test)

    def num0(self):

        text = self.ui.displaycalculator.text()

        if text[-1] == ")":
            pass

        else:
            if len(self.lst) == 0:
                # self.ui.displaycalculator.setText("0")
                # self.count += 1
                # self.lst += "0"
                # self.sqr_sto += "0"
                pass

            elif len(self.lst) > 0:
                self.ui.displaycalculator.setText(text + "0")
                self.count += 1
                self.lst += "0"
                self.sqr_sto += "0"

    def addnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " + ")
        # self.count += 3
        # self.lst += " + "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " + ")
            self.count += 4
            self.lst += "0 + "
            self.sqr_sto += "0 + "

        # FIXING TWO OPERATOR IN A ROW
        elif "+" in text or "-" in text or "*" in text or "/" in text:
            # FIXING THAT IF THAT IS A NEGATIVE OPERATOR OR A NEGATIVE NUMBER
            if (self.lst[-1] == "1" or self.lst[-1] == "2"
                or self.lst[-1] == "3" or self.lst[-1] == "4"
                or self.lst[-1] == "5" or self.lst[-1] == "6"
                or self.lst[-1] == "7" or self.lst[-1] == "8"
                or self.lst[-1] == "9") and self.lst[-1] != ".":

                self.ui.displaycalculator.setText(text + " + ")
                self.count += 3
                self.lst += " + "
                self.sqr_sto += " + "

            elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/" or self.lst[
                -1] == "(":
                pass

            else:
                if self.lst[-1] == ".":
                    pass

                else:
                    self.ui.displaycalculator.setText(text + " + ")
                    self.count += 3
                    self.lst += " + "
                    self.sqr_sto += " + "

        else:
            if self.lst[-1] == ".":
                pass

            else:
                self.ui.displaycalculator.setText(text + " + ")
                self.count += 3
                self.lst += " + "
                self.sqr_sto += " + "

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
            self.sqr_sto += "0 - "

        # FIXING TWO OPERATOR IN A ROW
        elif "+" in text or "-" in text or "*" in text or "/" in text:
            # FIXING THAT IF THAT IS A NEGATIVE OPERATOR OR A NEGATIVE NUMBER
            if (self.lst[-1] == "1" or self.lst[-1] == "2"
                or self.lst[-1] == "3" or self.lst[-1] == "4"
                or self.lst[-1] == "5" or self.lst[-1] == "6"
                or self.lst[-1] == "7" or self.lst[-1] == "8"
                or self.lst[-1] == "9") and self.lst[-1] != ".":

                self.ui.displaycalculator.setText(text + " - ")
                self.count += 3
                self.lst += " - "
                self.sqr_sto += " - "

            elif self.lst[-2] == "-":
                pass

            else:
                if self.lst[-1] == ".":
                    pass

                else:
                    self.ui.displaycalculator.setText(text + " - ")
                    self.count += 3
                    self.lst += " - "
                    self.sqr_sto += " - "

        else:
            if self.lst[-1] == ".":
                pass

            else:
                self.ui.displaycalculator.setText(text + " - ")
                self.count += 3
                self.lst += " - "
                self.sqr_sto += " - "

    def mulnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " * ")
        # self.count += 3
        # self.lst += " * "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " * ")
            self.count += 4
            self.lst += "0 * "
            self.sqr_sto += "0 * "

        # FIXING TWO OPERATOR IN A ROW
        elif "+" in text or "-" in text or "*" in text or "/" in text:
            # FIXING THAT IF THAT IS A NEGATIVE OPERATOR OR A NEGATIVE NUMBER
            if (self.lst[-1] == "1" or self.lst[-1] == "2"
                or self.lst[-1] == "3" or self.lst[-1] == "4"
                or self.lst[-1] == "5" or self.lst[-1] == "6"
                or self.lst[-1] == "7" or self.lst[-1] == "8"
                or self.lst[-1] == "9") and self.lst[-1] != ".":

                self.ui.displaycalculator.setText(text + " * ")
                self.count += 3
                self.lst += " * "
                self.sqr_sto += " * "

            elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/" or self.lst[
                -1] == "(":
                pass

            else:
                if self.lst[-1] == ".":
                    pass

                else:
                    self.ui.displaycalculator.setText(text + " * ")
                    self.count += 3
                    self.lst += " * "
                    self.sqr_sto += " * "

        else:
            if self.lst[-1] == ".":
                pass

            else:
                self.ui.displaycalculator.setText(text + " * ")
                self.count += 3
                self.lst += " * "
                self.sqr_sto += " * "

    def divnum(self):
        text = self.ui.displaycalculator.text()
        # self.ui.displaycalculator.setText(text + " / ")
        # self.count += 3
        # self.lst += " / "

        if text[0] == "0":
            self.ui.displaycalculator.setText(text + " / ")
            self.count += 4
            self.lst += "0 / "
            self.sqr_sto += "0 / "

        # FIXING TWO OPERATOR IN A ROW
        # elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/":
        elif "+" in text or "-" in text or "*" in text or "/" in text:
            # FIXING THAT IF THAT IS A NEGATIVE OPERATOR OR A NEGATIVE NUMBER
            if (self.lst[-1] == "1" or self.lst[-1] == "2"
                or self.lst[-1] == "3" or self.lst[-1] == "4"
                or self.lst[-1] == "5" or self.lst[-1] == "6"
                or self.lst[-1] == "7" or self.lst[-1] == "8"
                or self.lst[-1] == "9") and self.lst[-1] != ".":
                
                self.ui.displaycalculator.setText(text + " / ")
                self.count += 3
                self.lst += " / "
                self.sqr_sto += " / "

            elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/" or self.lst[
                -1] == "(":
                pass

            else:
                if self.lst[-1] == ".":
                    pass

                else:
                    self.ui.displaycalculator.setText(text + " / ")
                    self.count += 3
                    self.lst += " / "
                    self.sqr_sto += " / "

        else:
            if self.lst[-1] == ".":
                pass

            else:
                self.ui.displaycalculator.setText(text + " / ")
                self.count += 3
                self.lst += " / "
                self.sqr_sto += " / "

    def result(self):

        text = self.ui.displaycalculator.text()

        if len(self.parentheses_sto) > 0:
            pass

        if len(self.lst) == 0:
            pass

        elif len(self.parentheses_sto) == 0:
            # print(self.lst == text)
            # print(self.lst == self.sqr_sto)
            # print(text == self.sqr_sto)
            # print(self.lst)
            # print(self.sqr_sto)
            # print(text)
            # print("")

            ans = str(eval(self.lst))

            self.ui.displaycalculator.setText(ans)

            self.ui.historylistwidget.addItem(f"{self.sqr_sto} = {self.ui.displaycalculator.text()}")

            """ Make the lst start with the previous ans"""
            if self.ui.displaycalculator.text() == "0":
                self.lst = ""
                self.sqr_sto = ""
                self.count = 0

            # elif self.ui.displaycalculator.text()[0] == "-":
            #     self.lst += "-"
            #     self.count += 1

            else:
                self.lst = f"{self.ui.displaycalculator.text()}"
                self.sqr_sto = f"{self.ui.displaycalculator.text()}"
                self.count = len(self.ui.displaycalculator.text())

    def delnum(self):
        self.ui.displaycalculator.setText("0")

        """ Make the lst empty"""
        self.lst = ""
        self.sqr_sto = ""
        self.count = 0

    def deleteonebyone(self):

        if self.count > 1:
            # print(f"Before: {self.count}")
            last = self.ui.displaycalculator.text()

            """ Delete all the operator """
            if self.lst[-1] == " " and self.lst[-3] == "*":
                last = last[:-3]
                self.count -= 4
                self.lst = self.lst[:-4]
                self.sqr_sto = self.sqr_sto[:-3]

            elif self.lst[-1] == " ":
                last = last[:-3]
                self.count -= 3
                self.lst = self.lst[:-3]
                self.sqr_sto = self.sqr_sto[:-3]

            elif self.lst[-2] == "-" and self.count == 2:
                last = last[:-2]
                last += "0"
                self.count = 0
                self.lst = ""
                self.sqr_sto = ""

            else:
                last = last[:-1]
                self.count -= 1
                self.lst = self.lst[:-1]
                self.sqr_sto = self.sqr_sto[:-1]

            self.ui.displaycalculator.setText(last)

            # print("Delete success!")
            # print(f"After: {self.count}")

        elif self.count == 1:
            self.delnum()
            # print("Back to 0")

        # print(self.lst)
        # print(self.count)

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
            self.sqr_sto += "."

    # def showtime(self):
    #     time = QtCore.QTime.currentTime()
    #     text = time.toString("hh:mm:ss")
    #     self.ui.timelable.display(text)

    def copying_data(self):
        # self.ui.testlable.clear()

        contants = ""
        contants += self.ui.historylistwidget.currentItem().text()

        wordlist = contants.split(" ")
        wordlist.remove("=")
        wordlist.pop()

        self.ui.displaycalculator.setText(" ".join(wordlist))

        self.lst = ""
        self.sqr_sto = ""

        self.count = 0

        self.lst += " ".join(wordlist)
        self.sqr_sto += " ".join(wordlist)

        self.count = len(self.lst)

    def bracketopen(self):

        text = self.ui.displaycalculator.text()

        if len(self.lst) == 0:

            self.ui.displaycalculator.setText("(")
            self.count += 1

            self.lst += "("
            self.sqr_sto += "("
            self.parentheses_sto += "("

        elif len(self.lst) > 0:

            if (self.lst[-1] == "1" or self.lst[-1] == "2"
                or self.lst[-1] == "3" or self.lst[-1] == "4"
                or self.lst[-1] == "5" or self.lst[-1] == "6"
                or self.lst[-1] == "7" or self.lst[-1] == "8"
                or self.lst[-1] == "9") and self.lst[-1] != ".":

                self.ui.displaycalculator.setText(text + " * (")
                self.count += 4

                self.lst += " * ("
                self.sqr_sto += " * ("
                self.parentheses_sto += "("

            elif self.lst[-1] == ")":

                self.ui.displaycalculator.setText(text + " * (")
                self.count += 4

                self.lst += " * ("
                self.sqr_sto += " * ("
                self.parentheses_sto += "("

            elif self.lst[-1] == ".":
                pass

            else:

                self.ui.displaycalculator.setText(text + "(")
                self.count += 1

                self.lst += "("
                self.sqr_sto += "("
                self.parentheses_sto += "("

        # print(self.parentheses_sto)

    def bracketclose(self):

        text = self.ui.displaycalculator.text()

        if len(self.lst) == 0:
            pass

        elif len(self.parentheses_sto) != 0 and self.parentheses_sto[-1] == "(":

            if self.lst[-1] == "(":

                self.lst += "0)"
                self.sqr_sto += "0)"
                self.count += 2
                self.parentheses_sto += ")"

                self.ui.displaycalculator.setText(self.lst)

                if self.parentheses_sto[-2] == "(" and self.parentheses_sto[-1] == ")":
                    self.parentheses_sto = self.parentheses_sto[:-2]

            elif (self.lst[-2] == "+" or self.lst[-2] == "-"
                  or self.lst[-2] == "*" or self.lst[-2] == "/"):

                # self.lst = self.lst[:-3]
                # self.sqr_sto = self.sqr_sto[:-3]
                #
                # self.lst += ")"
                # self.sqr_sto += ")"
                # self.parentheses_sto += ")"
                #
                # self.ui.displaycalculator.setText(self.lst)
                # self.count += -2
                #
                # if self.parentheses_sto[-2] == "(" and self.parentheses_sto[-1] == ")":
                #     self.parentheses_sto = self.parentheses_sto[:-2]

                pass

            elif self.lst[-1] == ".":

                self.lst = self.lst[:-1]
                self.sqr_sto = self.sqr_sto[:-1]

                self.lst += ")"
                self.sqr_sto += ")"
                self.parentheses_sto += ")"

                self.ui.displaycalculator.setText(self.lst)

                if self.parentheses_sto[-2] == "(" and self.parentheses_sto[-1] == ")":
                    self.parentheses_sto = self.parentheses_sto[:-2]

            else:

                self.ui.displaycalculator.setText(text + ")")
                self.count += 1

                self.lst += ")"
                self.sqr_sto += ")"
                self.parentheses_sto += ")"

                if self.parentheses_sto[-2] == "(" and self.parentheses_sto[-1] == ")":
                    self.parentheses_sto = self.parentheses_sto[:-2]

        else:
            pass

        # print(self.parentheses_sto)

    def square(self):

        text = self.ui.displaycalculator.text()

        if len(self.lst) > 0 and self.lst[-1] == ")":
            self.ui.displaycalculator.setText(text + " ^ ")
            self.sqr_sto += " ^ "
            self.lst += " ** "
            self.count += 4

        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
