import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from random import *


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.convertbutton.clicked.connect(self.converting)
        self.ui.optionbox.currentIndexChanged.connect(self.converting)
        self.show()

    def converting(self):

        text = self.ui.userinput.toPlainText()
        text_output = self.ui.output.clearHistory()
        selection = self.ui.optionbox.itemText(self.ui.optionbox.currentIndex())

        if selection == "Every words":
            if len(text) == 0:
                pass

            else:
                slice_text = text.split(" ")

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

                result = "\n".join([str(i) for i in slice_text])

                self.ui.output.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
