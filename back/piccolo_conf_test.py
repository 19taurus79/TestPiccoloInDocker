from piccolo_conf import *  # noqa


DB = PostgresEngine(
    config={
        "database": "test_db",
        "user": "admin",
        "password": "root",
        "port": "5432",
        "host": "localhost",
    }
)
