import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from PyQt5 import QtSql

from utils.db import db_connect

db = db_connect()

db.open()


add_task_unique_constraint = """
ALTER TABLE task 
ADD CONSTRAINT unique_task UNIQUE (task);
"""

qt_query = QtSql.QSqlQuery()

qt_query.exec_(add_task_unique_constraint)

db.close()
