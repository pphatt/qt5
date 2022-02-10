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
        self.ui.optionbox.currentIndexChanged.connect(self.adding_choice)
        # self.ui.timesbox.currentIndexChanged.connect(self.converting)
        self.ui.userinput.textChanged.connect(self.adding_choice)
        self.ui.listWidget.itemDoubleClicked.connect(self.adjust_history)
        self.ui.tabWidget.setTabText(0, "Main")
        self.ui.tabWidget.setTabText(1, "History")
        self.ui.tabWidget.currentChanged.connect(self.tab_job)
        self.show()

    get_day = datetime.now()
    current_day = f"{get_day.day}-{get_day.month}-{get_day.year}"

    count2 = "wsc"

    count101 = 0
    count102 = 0

    slot_check = [[""]]

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

    def checking(self, thingy1: list[str]) -> list[str]:

        sto111 = []

        for i in range(len(thingy1)):

            if thingy1[i] == "":
                continue

            else:
                sto111.append(thingy1[i])

        return sto111

    def adding_choice(self):
        selection = self.ui.optionbox.itemText(self.ui.optionbox.currentIndex())
        self.ui.userinput.setUndoRedoEnabled(False)
        text = self.ui.userinput.toPlainText()

        text1 = [j for i in text.split(" ") for j in i.split("\n")]
        nums = self.ui.timesbox.count()

        space_count = text1.count("")
        for i in range(space_count):
            text1.remove("")

        if len(text1) < self.count101:
            pass

        else:
            self.count101 = len(text1)

        # print(text)
        # print(text1)

        if selection == "Without special characters":

            if self.count2 != "wsc":
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

                self.ui.userinput.selectAll()
                self.ui.userinput.cut()
                self.ui.output.clear()

                self.count2 = ""
                self.count2 += "wsc"

            if len(text1) == nums:
                self.ui.timesbox.addItem(f"{len(text1)}")

            elif len(text1) > nums:
                for i in range(nums, len(text1) + 1):
                    self.ui.timesbox.addItem(f"{i}")

            elif len(text1) == 0:
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

            elif len(text1) < self.count101:

                a = self.count101 - len(text1)

                for i in range(a + 1):
                    self.ui.timesbox.removeItem(self.count101 - i + 1)

                self.count101 = len(text1)

        elif selection == "Every words (including special characters)":

            if self.count2 != "ew":
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

                self.ui.userinput.selectAll()
                self.ui.userinput.cut()
                self.ui.output.clear()

                self.count2 = ""
                self.count2 = "ew"

            if len(text1) == nums:
                self.ui.timesbox.addItem(f"{len(text1)}")

            elif len(text1) > nums:
                for i in range(nums, len(text1) + 1):
                    self.ui.timesbox.addItem(f"{i}")

            elif len(text1) == 0:
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

            elif len(text1) < self.count101:

                a = self.count101 - len(text1)

                for i in range(a + 1):
                    self.ui.timesbox.removeItem(self.count101 - i + 1)

                self.count101 = len(text1)

        elif selection == "Last word (per line)":

            if self.count2 != "lw":
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

                self.ui.userinput.selectAll()
                self.ui.userinput.cut()
                self.ui.output.clear()

                self.count2 = ""
                self.count2 += "lw"

            text2 = text.split("\n")

            space_count1 = text2.count("")
            for i in range(space_count1):
                text2.remove("")

            if len(text2) < self.count102:
                pass

            else:
                self.count102 = len(text2)

            if len(text2) == nums:
                self.ui.timesbox.addItem(f"{len(text2)}")

            elif len(text2) > nums:
                for i in range(nums, len(text2) + 1):
                    self.ui.timesbox.addItem(f"{i}")

            elif len(text2) < self.count102:

                a = self.count102 - len(text2)

                for i in range(a + 1):
                    self.ui.timesbox.removeItem(self.count102 - i + 1)

                self.count102 = len(text2)

        elif selection == "Random line":

            if self.count2 != "rl":
                self.ui.timesbox.clear()
                self.ui.timesbox.addItem("All")

                self.ui.userinput.selectAll()
                self.ui.userinput.cut()
                self.ui.output.clear()

                self.count2 = ""
                self.count2 += "rl"

            text2 = text.split("\n")

            space_count1 = text2.count("")
            for i in range(space_count1):
                text2.remove("")

            if len(text2) < self.count102:
                pass

            else:
                self.count102 = len(text2)

            if len(text2) == nums:
                self.ui.timesbox.addItem(f"{len(text2)}")

            elif len(text2) > nums:
                for i in range(nums, len(text2) + 1):
                    self.ui.timesbox.addItem(f"{i}")

            elif len(text2) < self.count102:

                a = self.count102 - len(text2)

                for i in range(a + 1):
                    self.ui.timesbox.removeItem(self.count102 - i + 1)

                self.count102 = len(text2)

    def adjust_history(self):
        count_items = self.ui.listWidget.count()

        a = self.ui.listWidget.currentRow()
        # b = self.ui.listWidget.currentItem().text()

        if self.ui.listWidget.isRowHidden(a) is False and self.ui.listWidget.isRowHidden(a + 1) is True and a % 2 == 0:
            self.ui.listWidget.setRowHidden(a, True)
            self.ui.listWidget.setRowHidden(a + 1, False)

        elif self.ui.listWidget.isRowHidden(a) is False and self.ui.listWidget.isRowHidden(
                a - 1) is True and a % 2 != 0:
            self.ui.listWidget.setRowHidden(a, True)
            self.ui.listWidget.setRowHidden(a - 1, False)

    def converting(self):
        timess = self.ui.timesbox.itemText(self.ui.timesbox.currentIndex())
        selection = self.ui.optionbox.itemText(self.ui.optionbox.currentIndex())

        if selection == "Without special characters":
            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing(" ")

                count = slice_text.count("")

                for i in range(count):
                    slice_text.remove("")

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

                        string_count = 0
                        for i in range(11):
                            string_count += len(random_result[i])

                        if [result] == self.slot_check[-1]:
                            pass

                        else:
                            if len(random_result) > 11:

                                quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                if 40 < len(random_result):
                                    string_count_2 = 0
                                    for i in range(41):
                                        string_count_2 += len(random_result[i])

                                    self.ui.listWidget.addItem(
                                        f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                                else:
                                    self.ui.listWidget.addItem(
                                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            self.slot_check.append([result])

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

                    string_count = 0
                    for i in range(11):
                        string_count += len(random_result[i])

                    if [result] == self.slot_check[-1]:
                        pass

                    else:
                        if len(random_result) > 11:

                            quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                            self.ui.listWidget.addItem(
                                f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            if 40 < len(random_result):
                                string_count_2 = 0
                                for i in range(41):
                                    string_count_2 += len(random_result[i])

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                        else:
                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            count_items = self.ui.listWidget.count()
                            self.ui.listWidget.setRowHidden(count_items - 1, True)

                        self.slot_check.append([result])

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

                count = slice_text.count("")

                for i in range(count):
                    slice_text.remove("")

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

                        string_count = 0
                        for i in range(11):
                            string_count += len(random_result[i])

                        if [result] == self.slot_check[-1]:
                            pass

                        else:
                            if len(random_result) > 11:

                                quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                if 40 < len(random_result):
                                    string_count_2 = 0
                                    for i in range(41):
                                        string_count_2 += len(random_result[i])

                                    self.ui.listWidget.addItem(
                                        f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                                else:
                                    self.ui.listWidget.addItem(
                                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            self.slot_check.append([result])

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

                    string_count = 0
                    for i in range(11):
                        string_count += len(random_result[i])

                    if [result] == self.slot_check[-1]:
                        pass

                    else:
                        if len(random_result) > 11:

                            quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                            self.ui.listWidget.addItem(
                                f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            if 40 < len(random_result):
                                string_count_2 = 0
                                for i in range(41):
                                    string_count_2 += len(random_result[i])

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                        else:
                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            count_items = self.ui.listWidget.count()
                            self.ui.listWidget.setRowHidden(count_items - 1, True)

                        self.slot_check.append([result])

                    self.ui.output.setText(result)

        if selection == "Last word (per line)":

            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing("\n")

                count = slice_text.count("")

                for i in range(count):
                    slice_text.remove("")

                for i in range(len(slice_text)):
                    slice_text_2 = slice_text[i].split(" ")
                    slice_text.remove(slice_text[i])
                    slice_text.insert(i, slice_text_2[-1])

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

                        string_count = 0
                        for i in range(11):
                            string_count += len(random_result[i])

                        if [result] == self.slot_check[-1]:
                            pass

                        else:
                            if len(random_result) > 11:

                                quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                if 40 < len(random_result):
                                    string_count_2 = 0
                                    for i in range(41):
                                        string_count_2 += len(random_result[i])

                                    self.ui.listWidget.addItem(
                                        f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                                else:
                                    self.ui.listWidget.addItem(
                                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            self.slot_check.append([result])

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

                    string_count = 0
                    for i in range(11):
                        string_count += len(random_result[i])

                    if [result] == self.slot_check[-1]:
                        pass

                    else:
                        if len(random_result) > 11:

                            quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                            self.ui.listWidget.addItem(
                                f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            if 40 < len(random_result):
                                string_count_2 = 0
                                for i in range(41):
                                    string_count_2 += len(random_result[i])

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                        else:
                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            count_items = self.ui.listWidget.count()
                            self.ui.listWidget.setRowHidden(count_items - 1, True)

                        self.slot_check.append([result])

                    self.ui.output.setText(result)

            # pass

        if selection == "Random line":

            if self.condition() is True:
                pass

            else:
                slice_text = self.split_thing("\n")

                count = slice_text.count("")

                for i in range(count):
                    slice_text.remove("")

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
                        output_result = self.dis_result("\n\n", random_result)
                        result = self.dis_result("\n", random_result)

                        string_count = 0
                        for i in range(11):
                            string_count += len(random_result[i])

                        if [result] == self.slot_check[-1]:
                            pass

                        else:
                            if len(random_result) > 11:

                                quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                if 40 < len(random_result):
                                    string_count_2 = 0
                                    for i in range(41):
                                        string_count_2 += len(random_result[i])

                                    self.ui.listWidget.addItem(
                                        f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                                else:
                                    self.ui.listWidget.addItem(
                                        f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                    count_items = self.ui.listWidget.count()
                                    self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            self.slot_check.append([result])

                        self.ui.output.setText(output_result)

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
                    output_result = self.dis_result("\n\n", random_result)
                    result = self.dis_result("\n", random_result)

                    string_count = 0
                    for i in range(11):
                        string_count += len(random_result[i])

                    if [result] == self.slot_check[-1]:
                        pass

                    else:
                        if len(random_result) > 11:

                            quote = f"EXTEND FOR MORE INFORMATION -> REMAND {len(random_result) - 11}"

                            self.ui.listWidget.addItem(
                                f"{result[:(string_count + 10)]}\n{quote}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            if 40 < len(random_result):
                                string_count_2 = 0
                                for i in range(41):
                                    string_count_2 += len(random_result[i])

                                self.ui.listWidget.addItem(
                                    f"{result[:(string_count_2 + 40)]}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                            else:
                                self.ui.listWidget.addItem(
                                    f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                                count_items = self.ui.listWidget.count()
                                self.ui.listWidget.setRowHidden(count_items - 1, True)

                        else:
                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            self.ui.listWidget.addItem(
                                f"{result}\n{selection} ({self.ui.timesbox.currentText()}) ({self.get_time()})")

                            count_items = self.ui.listWidget.count()
                            self.ui.listWidget.setRowHidden(count_items - 1, True)

                        self.slot_check.append([result])

                    self.ui.output.setText(output_result)

            # pass


"""
Note (I am too lazy to do these update so .... Whoever can do it, just do a pull request or folk the project):
- We can make the delete button for history. Both delete one by one or delete all
- Changing UI for better
- Changing the history display when there are more than 40 answers
- Maybe, there are more options that are not here so..... like I said it above. Goodluck !  
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
