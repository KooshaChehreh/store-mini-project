from contextlib import contextmanager
import psycopg2
from HW13.hw13.configs import DB_CONNECTION, TABLES_QUERY
from HW13.hw13.log import store

""" Notice: Please run 1 time to create the database and after that deactivate lines starting 7 ends 18! """


def postgres_data_base_creator(dbname):
    conn = psycopg2.connect(user="postgres", host="localhost", port=5432, password="postgres")
    curr = conn.cursor()
    curr.execute(f"""CREATE DATABASE {dbname};""")
    curr.close()
    conn.commit()
    conn.close()
    store.info('Database created Successfully')
    return f'{dbname} database was created'


print(postgres_data_base_creator('storedatabase3'))


class DBCreator:
    table_name_len = {}
    HOST = DB_CONNECTION["HOST"]
    USER = DB_CONNECTION["USER"]
    PORT = DB_CONNECTION["PORT"]
    PASSWORD = DB_CONNECTION["PASSWORD"]
    DBNAME = DB_CONNECTION["DBNAME"]

    def __init__(self, dbname=DBNAME, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.dbname = dbname
        self.user = user
        self.host = host
        self.port = port
        self.password = password

    """1. creates all tables which queries are from configs
       2. updates the class attribute in order to use later"""

    def create_table(self, query=TABLES_QUERY) -> None:
        with self.connect_to_db() as cur:
            for k, v in query.items():
                cur.execute(f"""{v}""")
            store.info('tables were created Successfully')

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {vars(self)}>"

    @staticmethod
    @contextmanager
    def connect_to_db():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database='storedatabase3',  # database name
            user="postgres",  # database user
            password="postgres"  # database password
        )
        cursor = conn.cursor()
        yield cursor
        cursor.close()
        conn.commit()
        conn.close()


# if '__name__' == '__main__':
#     # postgres_data_base_creator('storedatabase3')

storedatabase3 = DBCreator()
storedatabase3.create_table()
