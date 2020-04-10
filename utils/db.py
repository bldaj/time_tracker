from PyQt5 import QtSql


def db_connect():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')

    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('time_tracker')
    db.setUserName('time_tracker')
    db.setPassword('password')

    return db
