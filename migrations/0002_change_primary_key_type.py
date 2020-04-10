import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from PyQt5 import QtSql

from utils.db import db_connect

db = db_connect()

db.open()

create_tracker_sequence_query = """
CREATE SEQUENCE tracker_seq MINVALUE 1;
"""

change_tracker_id_type_query = """
ALTER TABLE tracker 
ALTER COLUMN id SET DEFAULT nextval('tracker_seq');
"""

create_task_sequence_query = """
CREATE SEQUENCE task_seq MINVALUE 1;
"""

change_task_id_type_query = """
ALTER TABLE tracker 
ALTER COLUMN id SET DEFAULT nextval('task_seq');
"""

qt_query = QtSql.QSqlQuery()

qt_query.exec_(create_tracker_sequence_query)
qt_query.exec_(change_tracker_id_type_query)


qt_query.exec_(create_task_sequence_query)
qt_query.exec_(change_task_id_type_query)

db.close()
