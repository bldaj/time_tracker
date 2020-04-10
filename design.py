from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 150, 111, 34))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(123, 150, 111, 34))
        self.stopButton.setObjectName("stopButton")
        self.task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.task_input.setGeometry(QtCore.QRect(10, 10, 221, 32))
        self.task_input.setObjectName("task_input")
        self.description_input = QtWidgets.QTextEdit(self.centralwidget)
        self.description_input.setGeometry(QtCore.QRect(10, 50, 221, 84))
        self.description_input.setToolTipDuration(-1)
        self.description_input.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Tracker"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.task_input.setPlaceholderText(_translate("MainWindow", "Task name"))
        self.description_input.setToolTip(_translate("MainWindow", "Task description"))
        self.description_input.setPlaceholderText(_translate("MainWindow", "Task description"))
