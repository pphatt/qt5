from PyQt5.QtWidgets import QDialog, QApplication
from Test import *
import sys

list_time = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
list_animal = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']


class MyUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.count_year)
        self.ui.pushButton.clicked.connect(self.show_name)
        self.ui.pushButton.clicked.connect(self.Sex_type)
        self.ui.MaleButton.toggled.connect(self.Sex_type)
        self.ui.FemaleButton.toggled.connect(self.Sex_type)
        self.ui.cap1.toggled.connect(self.Education_level)
        self.ui.cap2.toggled.connect(self.Education_level)
        self.ui.cap3.toggled.connect(self.Education_level)
        self.ui.groupBox_pizza.clicked.connect(self.food_chek)
        self.ui.groupBox_bread.clicked.connect(self.food_chek)
        self.ui.pepperoni_check.stateChanged.connect(self.food_chek)
        self.ui.cheese_check.stateChanged.connect(self.food_chek)
        self.ui.fish_check.stateChanged.connect(self.food_chek)
        self.ui.hot_check.stateChanged.connect(self.food_chek)
        self.ui.long_check.stateChanged.connect(self.food_chek)
        self.ui.big_check.stateChanged.connect(self.food_chek)
        self.show()

    @staticmethod
    def age_cal(list_time, year1):
        time = year1 % 10
        return list_time[time]

    @staticmethod
    def animal_cal(list_animal, year1):
        animal = year1 % 12
        return list_animal[animal]

    def count_year(self):
        a = self.ui.InputYear.text()
        self.ui.result_year.setText(self.age_cal(list_time, int(a)) + " " + self.animal_cal(list_animal, int(a)))

    def show_name(self):
        self.ui.result_name.setText(str(self.ui.InputName.text()))

    def Sex_type(self):
        sex_type = ""
        if self.ui.MaleButton.isChecked():
            sex_type = "Male"
        if self.ui.FemaleButton.isChecked():
            sex_type = "Female"
        self.ui.result_sex.setText(sex_type)

    def Education_level(self):
        education_level = ""
        if self.ui.cap1.isChecked():
            education_level = "Primary"
        if self.ui.cap2.isChecked():
            education_level = "Secondary"
        if self.ui.cap3.isChecked():
            education_level = "Highschool"
        self.ui.result_education.setText(education_level)

    def food_chek(self):
        amount = 0
        if self.ui.groupBox_pizza.isChecked():
            amount += 10

            if self.ui.pepperoni_check.isChecked():
                amount += 4

            if self.ui.cheese_check.isChecked():
                amount += 5

            if self.ui.fish_check.isChecked():
                amount += 10

        if self.ui.groupBox_bread.isChecked():
            amount += 5

            if self.ui.hot_check.isChecked():
                amount += 4

            if self.ui.long_check.isChecked():
                amount += 5

            if self.ui.big_check.isChecked():
                amount += 10

        self.ui.result_food.setText(f"Total is {amount}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyUI()
    ui.show()
    sys.exit(app.exec_())
