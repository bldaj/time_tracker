import sys

from PyQt5 import (
    QtSql, QtWidgets
)

from consts import TITLE
import design
import sql_queries


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_db()
        self.create_tables()
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

    def create_tables(self):
        query = QtSql.QSqlQuery()
        query.exec_(sql_queries.CREATE_TRACKER_TABLE)
        query.exec_(sql_queries.CREATE_TASK_TABLE)

    def start(self):
        query = QtSql.QSqlQuery()
        # print(query.exec_("select * from tracker;"))
        self.close()
        self.next = DataList()


class DataList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = TITLE
        self.top = 600
        self.left = 200
        self.width = 500
        self.height = 500

        self.init_window()

    def init_window(self):
        self.button = QtWidgets.QPushButton("Ok", self)
        self.button.move(100, 400)
        self.button.clicked.connect(self.ok)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def ok(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
