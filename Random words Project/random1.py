# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\Python\Qt5\Random words Project\random1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userinput = QtWidgets.QPlainTextEdit(self.frame)
        self.userinput.setMinimumSize(QtCore.QSize(300, 521))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userinput.setFont(font)
        self.userinput.setObjectName("userinput")
        self.horizontalLayout.addWidget(self.userinput)
        self.widget = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(250, 727))
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionbox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionbox.sizePolicy().hasHeightForWidth())
        self.optionbox.setSizePolicy(sizePolicy)
        self.optionbox.setMinimumSize(QtCore.QSize(100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.optionbox.setFont(font)
        self.optionbox.setObjectName("optionbox")
        self.optionbox.addItem("")
        self.optionbox.addItem("")
        self.optionbox.addItem("")
        self.optionbox.addItem("")
        self.verticalLayout.addWidget(self.optionbox)
        self.timesbox = QtWidgets.QComboBox(self.widget)
        self.timesbox.setObjectName("timesbox")
        self.timesbox.addItem("")
        self.verticalLayout.addWidget(self.timesbox)
        self.convertbutton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convertbutton.setFont(font)
        self.convertbutton.setObjectName("convertbutton")
        self.verticalLayout.addWidget(self.convertbutton)
        self.horizontalLayout.addWidget(self.widget)
        self.output = QtWidgets.QTextBrowser(self.frame)
        self.output.setMinimumSize(QtCore.QSize(300, 521))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.horizontalLayout.addWidget(self.output)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_5.addWidget(self.listWidget)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Main"))
        self.optionbox.setItemText(0, _translate("MainWindow", "Without special characters"))
        self.optionbox.setItemText(1, _translate("MainWindow", "Every words (including special characters)"))
        self.optionbox.setItemText(2, _translate("MainWindow", "Last word (per line)"))
        self.optionbox.setItemText(3, _translate("MainWindow", "Random line"))
        self.timesbox.setItemText(0, _translate("MainWindow", "All"))
        self.convertbutton.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
