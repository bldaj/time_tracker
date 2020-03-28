import sys

from PyQt5 import (
    QtSql, QtWidgets
)

import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_db()
        self.startButton.clicked.connect(self.get_rows)

    def connect_db(self):
        db = QtSql.QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('time_tracker')
        db.setUserName('time_tracker')
        db.setPassword('password')

        if db.isOpen():
            db.close()

        if not db.open():
            raise Exception("Error opening database: {0}".format(db.lastError().text()))

    def get_rows(self):
        query = QtSql.QSqlQuery()
        print(query.exec_("select * from time_tracker;"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
