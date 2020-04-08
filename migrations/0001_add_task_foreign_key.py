from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QPSQL')

db.setHostName('localhost')
db.setPort(5432)
db.setDatabaseName('time_tracker')
db.setUserName('time_tracker')
db.setPassword('password')

db.open()

add_column = """
ALTER TABLE tracker 
ADD COLUMN task INT;
"""

add_foreign_key = """
ALTER TABLE tracker 
ADD CONSTRAINT task FOREIGN KEY (task)
REFERENCES task(id)
ON DELETE CASCADE;
"""

qt_query = QtSql.QSqlQuery()
qt_query.exec_(add_column)

qt_query = QtSql.QSqlQuery()
qt_query.exec_(add_foreign_key)

db.close()
