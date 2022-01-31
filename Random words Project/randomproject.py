import sys

from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication

from random1 import *

import random


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.convertbutton.clicked.connect(self.converting)
        self.ui.optionbox.currentIndexChanged.connect(self.converting)
        self.ui.timesbox.currentIndexChanged.connect(self.converting)
        self.ui.tabWidget.setTabText(0, "Main")
        self.ui.tabWidget.setTabText(1, "History")
        self.ui.tabWidget.currentChanged.connect(self.tab_job)
        self.show()

    get_day = datetime.now()
    current_day = f"{get_day.day}-{get_day.month}-{get_day.year}"

    def dis_result(self, gap_for_join: str, sto: list[str]) -> str:
        result = f"{gap_for_join}".join([str(i) for i in sto])
        return result

    def split_thing(self, gap_for_split: str) -> list[str]:
        text = self.ui.userinput.toPlainText()
        a = text.split(f"{gap_for_split}")
        return a

    def condition(self):
        text = self.ui.userinput.toPlainText()

        if len(text) == 0:
            return True

        else:
            return False

    def tab_job(self):

        if self.ui.tabWidget.currentIndex() == 0:
            pass

        elif self.ui.tabWidget.currentIndex() == 1:
            pass

    def get_time(self):
        time = QtCore.QTime.currentTime()
        current_time = time.toString("hh:mm:ss")
        current_time_line = f"{current_time} {self.current_day}"
        return current_time_line

    def random_choice(self, times: int, thing: list[str]) -> list[str]:
        choices = []

        for i in range(times):
            choices.append(random.choice(thing))

        return choices

    def fxing_split(self, thing1: str) -> list[str]:
        thing2 = thing1.split("\n")
        return thing2

    def converting(self):
        # print(self.ui.tabWidget.currentIndex())
        # text = self.ui.userinput.toPlainText()
        # text_output = self.ui.output.clearHistory()
        timess = self.ui.timesbox.itemText(self.ui.timesbox.currentIndex())
        selection = self.ui.optionbox.itemText(self.ui.optionbox.currentIndex())

        if selection == "Without special characters":
            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing(" ")

                for i in range(len(slice_text)):

                    for j in range(len(slice_text[i])):

                        try:
                            sto = ""
                            a = slice_text[i][-1].isdigit()
                            b = slice_text[i][-1].isalpha()
                            while a is False and b is False:
                                sto1 = ""
                                sto1 += slice_text[i]
                                slice_text.remove(slice_text[i])
                                sto1 = sto1[:-1]
                                slice_text.insert(i, sto1)
                                a = slice_text[i][-1].isdigit()
                                b = slice_text[i][-1].isalpha()

                            # sto += sto1

                            if slice_text[i][j] == ".":

                                try:
                                    check = slice_text[i][j + 1].isdigit()
                                    check_alpha = slice_text[i][j + 1].isalpha()

                                    if check is True or check_alpha is True:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace(".", "\n", 1)
                                        slice_text.insert(i, remove_thing)

                                    elif check is False or check_alpha is False:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace(".", " ", 1)
                                        slice_text.insert(i, remove_thing)

                                # Try except the last special character(Ex: the dot ".") -> fixing the out of range
                                except IndexError:
                                    sto += slice_text[i]
                                    slice_text.remove(slice_text[i])
                                    remove_thing = sto.replace(".", " ", 1)
                                    slice_text.insert(i, remove_thing)

                            elif slice_text[i][j] == ",":

                                try:
                                    check = slice_text[i][j + 1].isdigit()
                                    check_alpha = slice_text[i][j + 1].isalpha()

                                    if check is True or check_alpha is True:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace(",", "\n", 1)
                                        slice_text.insert(i, remove_thing)

                                    elif check is False or check_alpha is False:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace(",", " ", 1)
                                        slice_text.insert(i, remove_thing)

                                except IndexError:
                                    sto += slice_text[i]
                                    slice_text.remove(slice_text[i])
                                    remove_thing = sto.replace(",", " ", 1)
                                    slice_text.insert(i, remove_thing)

                            elif slice_text[i][j] == "/":

                                try:
                                    check = slice_text[i][j + 1].isdigit()
                                    check_alpha = slice_text[i][j + 1].isalpha()

                                    if check is True or check_alpha is True:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("/", "\n", 1)
                                        slice_text.insert(i, remove_thing)

                                    elif check is False or check_alpha is False:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("/", " ", 1)
                                        slice_text.insert(i, remove_thing)

                                except IndexError:
                                    sto += slice_text[i]
                                    slice_text.remove(slice_text[i])
                                    remove_thing = sto.replace("/", " ", 1)
                                    slice_text.insert(i, remove_thing)

                            elif slice_text[i][j] == "[":

                                try:
                                    check = slice_text[i][j + 1].isdigit()
                                    check_alpha = slice_text[i][j + 1].isalpha()

                                    if check is True or check_alpha is True:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("[", "\n", 1)
                                        slice_text.insert(i, remove_thing)

                                    elif check is False or check_alpha is False:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("[", " ", 1)
                                        slice_text.insert(i, remove_thing)

                                except IndexError:
                                    sto += slice_text[i]
                                    slice_text.remove(slice_text[i])
                                    remove_thing = sto.replace("[", " ", 1)
                                    slice_text.insert(i, remove_thing)

                            elif slice_text[i][j] == "]":

                                try:
                                    check = slice_text[i][j + 1].isdigit()
                                    check_alpha = slice_text[i][j + 1].isalpha()

                                    if check is True or check_alpha is True:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("]", "\n", 1)
                                        slice_text.insert(i, remove_thing)

                                    elif check is False or check_alpha is False:
                                        sto += slice_text[i]
                                        slice_text.remove(slice_text[i])
                                        remove_thing = sto.replace("]", " ", 1)
                                        slice_text.insert(i, remove_thing)

                                except IndexError:
                                    sto += slice_text[i]
                                    slice_text.remove(slice_text[i])
                                    remove_thing = sto.replace("]", " ", 1)
                                    slice_text.insert(i, remove_thing)

                        except IndexError:
                            continue

                try:
                    if timess == f"{self.ui.timesbox.currentText()}":
                        sto101 = []

                        # slice_text -> list[str] bc of the split build_in func
                        for i in slice_text:
                            if "\n" in i:
                                split_for_random = self.fxing_split(i)
                                for j in split_for_random:
                                    sto101.append(j)
                            else:
                                sto101.append(i)

                        random_result = self.random_choice(int(self.ui.timesbox.currentText()), sto101)
                        result = self.dis_result("\n", random_result)
                        self.ui.listWidget.addItem(
                            f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                        self.ui.output.setText(result)

                except ValueError:
                    sto102 = []

                    for i in slice_text:
                        if "\n" in i:
                            split_for_random = self.fxing_split(i)
                            for j in split_for_random:
                                sto102.append(j)
                        else:
                            sto102.append(i)

                    random_result = self.random_choice(len(sto102), sto102)
                    result = self.dis_result("\n", random_result)
                    self.ui.listWidget.addItem(
                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                    self.ui.output.setText(result)

                # Do not delete it
                # Note for the previous version
                #               |
                #               |
                #               |
                #              \/
                # result = self.dis_result("\n", slice_text)
                # self.ui.listWidget.addItem(f"{result}\n{selection} ({self.get_time()})")
                # self.ui.output.setText(result)

        if selection == "Every words (including special characters)":

            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing(" ")
                # result = self.dis_result("\n", slice_text)
                # self.ui.listWidget.addItem(f"{result}\n{selection} ({self.get_time()})")
                # self.ui.output.setText(result)

                try:
                    if timess == f"{self.ui.timesbox.currentText()}":
                        sto103 = []

                        for i in slice_text:
                            if "\n" in i:
                                split_for_random = self.fxing_split(i)
                                for j in split_for_random:
                                    sto103.append(j)
                            else:
                                sto103.append(i)

                        random_result = self.random_choice(int(self.ui.timesbox.currentText()), sto103)
                        result = self.dis_result("\n", random_result)
                        self.ui.listWidget.addItem(
                            f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                        self.ui.output.setText(result)

                except ValueError:
                    sto104 = []

                    for i in slice_text:
                        if "\n" in i:
                            split_for_random = self.fxing_split(i)
                            for j in split_for_random:
                                sto104.append(j)
                        else:
                            sto104.append(i)

                    random_result = self.random_choice(len(sto104), sto104)
                    result = self.dis_result("\n", random_result)
                    self.ui.listWidget.addItem(
                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                    self.ui.output.setText(result)

        if selection == "Last word (per line)":

            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing("\n")

                for i in range(len(slice_text)):
                    slice_text_2 = slice_text[i].split(" ")
                    slice_text.remove(slice_text[i])
                    slice_text.insert(i, slice_text_2[-1])

                # result = self.dis_result("\n", slice_text)
                # self.ui.listWidget.addItem(f"{result}\n{selection} ({self.get_time()})")
                # self.ui.output.setText(result)

                try:
                    if timess == f"{self.ui.timesbox.currentText()}":
                        sto105 = []

                        for i in slice_text:
                            if "\n" in i:
                                split_for_random = self.fxing_split(i)
                                for j in split_for_random:
                                    sto105.append(j)
                            else:
                                sto105.append(i)

                        random_result = self.random_choice(int(self.ui.timesbox.currentText()), sto105)
                        result = self.dis_result("\n", random_result)
                        self.ui.listWidget.addItem(
                            f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                        self.ui.output.setText(result)

                except ValueError:
                    sto106 = []

                    for i in slice_text:
                        if "\n" in i:
                            split_for_random = self.fxing_split(i)
                            for j in split_for_random:
                                sto106.append(j)
                        else:
                            sto106.append(i)

                    random_result = self.random_choice(len(sto106), sto106)
                    result = self.dis_result("\n", random_result)
                    self.ui.listWidget.addItem(
                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                    self.ui.output.setText(result)

            # pass

        if selection == "Random line":

            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing("\n")
                # result = self.dis_result("\n", slice_text)
                # self.ui.listWidget.addItem(f"{result}\n{selection} ({self.get_time()})")
                # self.ui.output.setText(result)

                try:
                    if timess == f"{self.ui.timesbox.currentText()}":
                        sto105 = []

                        for i in slice_text:
                            if "\n" in i:
                                split_for_random = self.fxing_split(i)
                                for j in split_for_random:
                                    sto105.append(j)
                            else:
                                sto105.append(i)

                        random_result = self.random_choice(int(self.ui.timesbox.currentText()), sto105)
                        result = self.dis_result("\n", random_result)
                        self.ui.listWidget.addItem(
                            f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                        self.ui.output.setText(result)

                except ValueError:
                    sto106 = []

                    for i in slice_text:
                        if "\n" in i:
                            split_for_random = self.fxing_split(i)
                            for j in split_for_random:
                                sto106.append(j)
                        else:
                            sto106.append(i)

                    random_result = self.random_choice(len(sto106), sto106)
                    result = self.dis_result("\n", random_result)
                    self.ui.listWidget.addItem(
                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")
                    self.ui.output.setText(result)

            # pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
