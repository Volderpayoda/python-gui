# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(619, 449)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(10, 280, 601, 161))
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.trainingDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.trainingDataFrame.setGeometry(QtCore.QRect(10, 10, 601, 71))
        self.trainingDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainingDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trainingDataFrame.setObjectName("trainingDataFrame")
        self.layoutWidget = QtWidgets.QWidget(self.trainingDataFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.trainingData = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.trainingData.setContentsMargins(0, 0, 0, 0)
        self.trainingData.setObjectName("trainingData")
        self.title = QtWidgets.QVBoxLayout()
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.title.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.title.addWidget(self.line)
        self.trainingData.addLayout(self.title)
        self.trainingFileBrowser = QtWidgets.QHBoxLayout()
        self.trainingFileBrowser.setObjectName("trainingFileBrowser")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.trainingFileBrowser.addWidget(self.label_2)
        self.trainingLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.trainingLineEdit.setEnabled(False)
        self.trainingLineEdit.setAcceptDrops(False)
        self.trainingLineEdit.setObjectName("trainingLineEdit")
        self.trainingFileBrowser.addWidget(self.trainingLineEdit)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setObjectName("browseButton")
        self.trainingFileBrowser.addWidget(self.browseButton)
        self.classifyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.classifyButton.setEnabled(False)
        self.classifyButton.setObjectName("classifyButton")
        self.trainingFileBrowser.addWidget(self.classifyButton)
        self.trainingData.addLayout(self.trainingFileBrowser)
        self.testDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.testDataFrame.setEnabled(False)
        self.testDataFrame.setGeometry(QtCore.QRect(10, 90, 601, 71))
        self.testDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.testDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.testDataFrame.setObjectName("testDataFrame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.testDataFrame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 601, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.testData = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.testData.setContentsMargins(0, 0, 0, 0)
        self.testData.setObjectName("testData")
        self.title_2 = QtWidgets.QVBoxLayout()
        self.title_2.setObjectName("title_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.title_2.addWidget(self.label_3)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.title_2.addWidget(self.line_2)
        self.testData.addLayout(self.title_2)
        self.testFileBrowser = QtWidgets.QHBoxLayout()
        self.testFileBrowser.setObjectName("testFileBrowser")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.testFileBrowser.addWidget(self.label_4)
        self.testLineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.testLineEdit.setEnabled(False)
        self.testLineEdit.setAcceptDrops(False)
        self.testLineEdit.setObjectName("testLineEdit")
        self.testFileBrowser.addWidget(self.testLineEdit)
        self.testBrowseButton = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBrowseButton.sizePolicy().hasHeightForWidth())
        self.testBrowseButton.setSizePolicy(sizePolicy)
        self.testBrowseButton.setObjectName("testBrowseButton")
        self.testFileBrowser.addWidget(self.testBrowseButton)
        self.testTestButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.testTestButton.setEnabled(False)
        self.testTestButton.setObjectName("testTestButton")
        self.testFileBrowser.addWidget(self.testTestButton)
        self.testData.addLayout(self.testFileBrowser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Datos de entrenamiento"))
        self.label_2.setText(_translate("MainWindow", "Archivo:"))
        self.browseButton.setText(_translate("MainWindow", "Examinar"))
        self.classifyButton.setText(_translate("MainWindow", "Clasificar"))
        self.label_3.setText(_translate("MainWindow", "Datos de prueba"))
        self.label_4.setText(_translate("MainWindow", "Archivo:"))
        self.testBrowseButton.setText(_translate("MainWindow", "Examinar"))
        self.testTestButton.setText(_translate("MainWindow", "Probar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

