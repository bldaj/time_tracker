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
        self.create_table()
        self.startButton.clicked.connect(self.start)

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

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tracker (
        id integer PRIMARY KEY, 
        datetime_start timestamp without time zone NOT NULL, 
        datetime_stop timestamp without time zone
        );
        """
        qt_query = QtSql.QSqlQuery()
        qt_query.exec_(query)

    def start(self):
        query = QtSql.QSqlQuery()
        print(query.exec_("select * from tracker;"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
