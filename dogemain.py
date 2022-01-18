#import packages
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import csv

#extract list of DOGE values from file
file = open('dogecoin_prediction.csv')
type(file)
csvreader = csv.reader(file)
value = []
for row in csvreader: 
    value.append(row[22])

#x-axis: days elapsed since date input
daysElapsed = [float(0), float(1), float(2), float(3), float(4), float(5), float(6)]

#extract list of dates from file
file = open('dogecoin_prediction.csv')
type(file)
csvreader = csv.reader(file)
date = []
for row in csvreader: 
    date.append(row[1])

#main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 325)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 351, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 160, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #what happens when the button is pressed
    def openWindow(self):
        global dateStart
        dateStart = self.lineEdit.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DOGEData()
        self.ui.setupUi(self.window)
        self.window.show()


    #declare text of labels, buttons
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.label.setText(_translate("MainWindow", "DOGE Prediction"))
        self.label_2.setText(_translate("MainWindow", "Start Date (YYYY-MM-DD)"))

#output window
class Ui_DOGEData(object):
    #'OK' Button closes window
    def close(self):
        sys.exit(app.exec_())

    #main setup for window
    def setupUi(self, DOGEData):
        #find the index of the date entered
        indexDate = date.index(dateStart)
        #create new lists with only the data of interest
        global valueOutput
        valueOutput = []
        for x in range(7):
            valueOutput.append(float(value[indexDate + x]))
        DOGEData.setObjectName("DOGEData")
        DOGEData.resize(745, 586)
        self.centralwidget = QtWidgets.QWidget(DOGEData)
        self.centralwidget.setObjectName("centralwidget")
        self.GraphWidget = PlotWidget(self.centralwidget)
        self.GraphWidget.plot(daysElapsed, valueOutput)
        self.GraphWidget.setGeometry(QtCore.QRect(10, 70, 721, 481))
        self.GraphWidget.setObjectName("GraphWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.close())
        self.pushButton.setGeometry(QtCore.QRect(590, 10, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        DOGEData.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DOGEData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        DOGEData.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DOGEData)
        self.statusbar.setObjectName("statusbar")
        DOGEData.setStatusBar(self.statusbar)

        self.retranslateUi(DOGEData)
        QtCore.QMetaObject.connectSlotsByName(DOGEData)

    def retranslateUi(self, DOGEData):
        _translate = QtCore.QCoreApplication.translate
        DOGEData.setWindowTitle(_translate("DOGEData", "MainWindow"))
        self.pushButton.setText(_translate("DOGEData", "OK"))
        self.label.setText(_translate("DOGEData", "Projected DOGE Value for "+ str(dateStart)))

#initiate
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())