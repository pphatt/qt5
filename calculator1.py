# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\Python\Stuff\Qt5\Project\calculator1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 291)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_6.setContentsMargins(9, 3, 3, 3)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.displaycalculator = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.displaycalculator.setFont(font)
        self.displaycalculator.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displaycalculator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displaycalculator.setObjectName("displaycalculator")
        self.gridLayout_4.addWidget(self.displaycalculator, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_4, 0, 0, 1, 2)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.equalsymbol = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalsymbol.sizePolicy().hasHeightForWidth())
        self.equalsymbol.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equalsymbol.setFont(font)
        self.equalsymbol.setObjectName("equalsymbol")
        self.gridLayout.addWidget(self.equalsymbol, 4, 3, 2, 1)
        self.mulsymbol = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mulsymbol.setFont(font)
        self.mulsymbol.setObjectName("mulsymbol")
        self.gridLayout.addWidget(self.mulsymbol, 0, 3, 1, 1)
        self.delsymbol = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delsymbol.setFont(font)
        self.delsymbol.setObjectName("delsymbol")
        self.gridLayout.addWidget(self.delsymbol, 0, 0, 1, 1)
        self.delonebyone = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delonebyone.setFont(font)
        self.delonebyone.setObjectName("delonebyone")
        self.gridLayout.addWidget(self.delonebyone, 0, 1, 1, 1)
        self.divsymbol = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.divsymbol.setFont(font)
        self.divsymbol.setObjectName("divsymbol")
        self.gridLayout.addWidget(self.divsymbol, 0, 2, 1, 1)
        self.subsymbol = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subsymbol.setFont(font)
        self.subsymbol.setObjectName("subsymbol")
        self.gridLayout.addWidget(self.subsymbol, 1, 3, 1, 1)
        self.dotbutton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dotbutton.setFont(font)
        self.dotbutton.setObjectName("dotbutton")
        self.gridLayout.addWidget(self.dotbutton, 5, 2, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 2, 2, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 4, 0, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 1, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 4, 1, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 1, 1, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 2, 0, 1, 1)
        self.addsymbol = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addsymbol.setFont(font)
        self.addsymbol.setObjectName("addsymbol")
        self.gridLayout.addWidget(self.addsymbol, 2, 3, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 2, 1, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 4, 2, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 1, 2, 1, 1)
        self.timelable = QtWidgets.QLCDNumber(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timelable.sizePolicy().hasHeightForWidth())
        self.timelable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timelable.setFont(font)
        self.timelable.setObjectName("timelable")
        self.gridLayout.addWidget(self.timelable, 6, 0, 1, 2)
        self.button0 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.gridLayout.addWidget(self.button0, 5, 1, 1, 1)
        self.minusbutton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusbutton.sizePolicy().hasHeightForWidth())
        self.minusbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minusbutton.setFont(font)
        self.minusbutton.setObjectName("minusbutton")
        self.gridLayout.addWidget(self.minusbutton, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.historylistwidget = QtWidgets.QListWidget(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.historylistwidget.setFont(font)
        self.historylistwidget.setObjectName("historylistwidget")
        self.gridLayout_2.addWidget(self.historylistwidget, 0, 0, 1, 2)
        self.delbutton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delbutton.setFont(font)
        self.delbutton.setObjectName("delbutton")
        self.gridLayout_2.addWidget(self.delbutton, 1, 0, 1, 1)
        self.delallbutton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delallbutton.setFont(font)
        self.delallbutton.setObjectName("delallbutton")
        self.gridLayout_2.addWidget(self.delallbutton, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.delsymbol.clicked.connect(self.displaycalculator.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.displaycalculator.setText(_translate("Dialog", "0"))
        self.equalsymbol.setText(_translate("Dialog", "="))
        self.mulsymbol.setText(_translate("Dialog", "*"))
        self.delsymbol.setText(_translate("Dialog", "C"))
        self.delonebyone.setText(_translate("Dialog", "X"))
        self.divsymbol.setText(_translate("Dialog", "/"))
        self.subsymbol.setText(_translate("Dialog", "-"))
        self.dotbutton.setText(_translate("Dialog", "."))
        self.button6.setText(_translate("Dialog", "6"))
        self.button1.setText(_translate("Dialog", "1"))
        self.button7.setText(_translate("Dialog", "7"))
        self.button2.setText(_translate("Dialog", "2"))
        self.button8.setText(_translate("Dialog", "8"))
        self.button4.setText(_translate("Dialog", "4"))
        self.addsymbol.setText(_translate("Dialog", "+"))
        self.button5.setText(_translate("Dialog", "5"))
        self.button3.setText(_translate("Dialog", "3"))
        self.button9.setText(_translate("Dialog", "9"))
        self.button0.setText(_translate("Dialog", "0"))
        self.minusbutton.setText(_translate("Dialog", "+/-"))
        self.delbutton.setText(_translate("Dialog", "Delete"))
        self.delallbutton.setText(_translate("Dialog", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
