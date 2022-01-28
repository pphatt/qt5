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
                # print(slice_text)

                for i in range(len(slice_text)):

                    sto = ""

                    if "." in slice_text[i]:

                        if slice_text[i][-1] == ".":
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace(".", "")
                            slice_text.insert(i, remove_thing)

                        else:
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace(".", "\n")
                            slice_text.insert(i, remove_thing)

                    elif "," in slice_text[i]:

                        if slice_text[i][-1] == ",":
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace(",", "")
                            slice_text.insert(i, remove_thing)

                        else:
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace(",", "\n")
                            slice_text.insert(i, remove_thing)

                    elif "/" in slice_text[i]:

                        if slice_text[i][-1] == "/":
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("/", "")
                            slice_text.insert(i, remove_thing)

                        else:
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("/", "\n")
                            slice_text.insert(i, remove_thing)

                    elif "[" in slice_text[i] and "]" in slice_text[i]:
                        sto += slice_text[i]
                        slice_text.remove(slice_text[i])
                        remove_thing = ""
                        slice_text.insert(i, remove_thing)

                    elif "[" in slice_text[i]:

                        if slice_text[i][-1] == "[":
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("[", "")
                            slice_text.insert(i, remove_thing)

                        else:
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("[", "\n")
                            slice_text.insert(i, remove_thing)

                    elif "]" in slice_text[i]:

                        if slice_text[i][-1] == "]":
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("]", "")
                            slice_text.insert(i, remove_thing)

                        else:
                            sto += slice_text[i]
                            slice_text.remove(slice_text[i])
                            remove_thing = sto.replace("]", "\n")
                            slice_text.insert(i, remove_thing)

                result = "\n".join([str(i) for i in slice_text])

                self.ui.output.setText(result)

        # print(selection)
        # print(type(selection))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
