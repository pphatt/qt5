from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(844, 572)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.InputYear = QtWidgets.QLineEdit(Dialog)
        self.InputYear.setGeometry(QtCore.QRect(250, 60, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InputYear.setFont(font)
        self.InputYear.setObjectName("InputYear")
        self.NameProgram = QtWidgets.QLabel(Dialog)
        self.NameProgram.setGeometry(QtCore.QRect(20, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameProgram.setFont(font)
        self.NameProgram.setObjectName("NameProgram")
        self.NameProgram_2 = QtWidgets.QLabel(Dialog)
        self.NameProgram_2.setGeometry(QtCore.QRect(80, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameProgram_2.setFont(font)
        self.NameProgram_2.setObjectName("NameProgram_2")
        self.InputName = QtWidgets.QLineEdit(Dialog)
        self.InputName.setGeometry(QtCore.QRect(250, 120, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InputName.setFont(font)
        self.InputName.setObjectName("InputName")
        self.Sex = QtWidgets.QLabel(Dialog)
        self.Sex.setGeometry(QtCore.QRect(80, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex.setFont(font)
        self.Sex.setObjectName("Sex")
        self.Sex_2 = QtWidgets.QLabel(Dialog)
        self.Sex_2.setGeometry(QtCore.QRect(80, 250, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Sex_2.setFont(font)
        self.Sex_2.setObjectName("Sex_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(261, 251, 111, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cap1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cap1.setFont(font)
        self.cap1.setObjectName("cap1")
        self.verticalLayout.addWidget(self.cap1)
        self.cap2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cap2.setFont(font)
        self.cap2.setObjectName("cap2")
        self.verticalLayout.addWidget(self.cap2)
        self.cap3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cap3.setFont(font)
        self.cap3.setObjectName("cap3")
        self.verticalLayout.addWidget(self.cap3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 170, 64, 62))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MaleButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MaleButton.setFont(font)
        self.MaleButton.setObjectName("MaleButton")
        self.verticalLayout_2.addWidget(self.MaleButton)
        self.FemaleButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FemaleButton.setFont(font)
        self.FemaleButton.setObjectName("FemaleButton")
        self.verticalLayout_2.addWidget(self.FemaleButton)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 410, 401, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.result_name = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_name.setFont(font)
        self.result_name.setText("")
        self.result_name.setObjectName("result_name")
        self.horizontalLayout_3.addWidget(self.result_name)
        self.result_year = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_year.setFont(font)
        self.result_year.setText("")
        self.result_year.setObjectName("result_year")
        self.horizontalLayout_3.addWidget(self.result_year)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.result_sex = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_sex.setFont(font)
        self.result_sex.setText("")
        self.result_sex.setObjectName("result_sex")
        self.horizontalLayout.addWidget(self.result_sex)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.result_education = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_education.setFont(font)
        self.result_education.setText("")
        self.result_education.setObjectName("result_education")
        self.horizontalLayout_2.addWidget(self.result_education)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(620, 30, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pizza_lable = QtWidgets.QLabel(Dialog)
        self.pizza_lable.setGeometry(QtCore.QRect(480, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pizza_lable.setFont(font)
        self.pizza_lable.setObjectName("pizza_lable")
        self.groupBox_pizza = QtWidgets.QGroupBox(Dialog)
        self.groupBox_pizza.setGeometry(QtCore.QRect(590, 100, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_pizza.setFont(font)
        self.groupBox_pizza.setCheckable(True)
        self.groupBox_pizza.setObjectName("groupBox_pizza")
        self.widget = QtWidgets.QWidget(self.groupBox_pizza)
        self.widget.setGeometry(QtCore.QRect(10, 30, 164, 95))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pepperoni_check = QtWidgets.QCheckBox(self.widget)
        self.pepperoni_check.setObjectName("pepperoni_check")
        self.verticalLayout_3.addWidget(self.pepperoni_check)
        self.cheese_check = QtWidgets.QCheckBox(self.widget)
        self.cheese_check.setObjectName("cheese_check")
        self.verticalLayout_3.addWidget(self.cheese_check)
        self.fish_check = QtWidgets.QCheckBox(self.widget)
        self.fish_check.setObjectName("fish_check")
        self.verticalLayout_3.addWidget(self.fish_check)
        self.groupBox_bread = QtWidgets.QGroupBox(Dialog)
        self.groupBox_bread.setGeometry(QtCore.QRect(590, 290, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_bread.setFont(font)
        self.groupBox_bread.setCheckable(True)
        self.groupBox_bread.setObjectName("groupBox_bread")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_bread)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 164, 95))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hot_check = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.hot_check.setObjectName("hot_check")
        self.verticalLayout_4.addWidget(self.hot_check)
        self.long_check = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.long_check.setObjectName("long_check")
        self.verticalLayout_4.addWidget(self.long_check)
        self.big_check = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.big_check.setObjectName("big_check")
        self.verticalLayout_4.addWidget(self.big_check)
        self.bread_lable = QtWidgets.QLabel(Dialog)
        self.bread_lable.setGeometry(QtCore.QRect(480, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bread_lable.setFont(font)
        self.bread_lable.setObjectName("bread_lable")
        self.result_food = QtWidgets.QLabel(Dialog)
        self.result_food.setGeometry(QtCore.QRect(490, 480, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result_food.setFont(font)
        self.result_food.setText("")
        self.result_food.setObjectName("result_food")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 250, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(590, 440, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Tính"))
        self.NameProgram.setText(_translate("Dialog", "Nhập số năm muốn tính"))
        self.NameProgram_2.setText(_translate("Dialog", "Nhập tên"))
        self.Sex.setText(_translate("Dialog", "Giới tính"))
        self.Sex_2.setText(_translate("Dialog", "Giáo dục"))
        self.cap1.setText(_translate("Dialog", "Cấp 1"))
        self.cap2.setText(_translate("Dialog", "Cấp 2"))
        self.cap3.setText(_translate("Dialog", "Cấp 3"))
        self.MaleButton.setText(_translate("Dialog", "Nam"))
        self.FemaleButton.setText(_translate("Dialog", "Nữ"))
        self.label.setText(_translate("Dialog", "Sell Food"))
        self.pizza_lable.setText(_translate("Dialog", "Pizza"))
        self.groupBox_pizza.setTitle(_translate("Dialog", "Topping"))
        self.pepperoni_check.setText(_translate("Dialog", "Pepperoni for 4$"))
        self.cheese_check.setText(_translate("Dialog", "Cheese for 5$ "))
        self.fish_check.setText(_translate("Dialog", "Fish for 10$"))
        self.groupBox_bread.setTitle(_translate("Dialog", "Topping"))
        self.hot_check.setText(_translate("Dialog", "Hot for 4$"))
        self.long_check.setText(_translate("Dialog", "Long for 5$ "))
        self.big_check.setText(_translate("Dialog", "Big for 10$"))
        self.bread_lable.setText(_translate("Dialog", "Bread"))
        self.label_2.setText(_translate("Dialog", "Basic Pizza is for 10$"))
        self.label_3.setText(_translate("Dialog", "Basic Bread  is for 5$"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())