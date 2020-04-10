CREATE_TRACKER_TABLE = """
    CREATE TABLE IF NOT EXISTS tracker (
    id integer PRIMARY KEY, 
    datetime_start timestamp without time zone NOT NULL, 
    datetime_stop timestamp without time zone
    );
    """

CREATE_TASK_TABLE = """
    CREATE TABLE IF NOT EXISTS task (
    id integer PRIMARY KEY, 
    task varchar(20) NOT NULL,
    description varchar(400)
    );
    """
