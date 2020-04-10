from PyQt5 import QtSql

from utils.db import db_connect

db = db_connect()

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
