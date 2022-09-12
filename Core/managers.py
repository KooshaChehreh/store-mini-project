from DBCreator import storedatabase3
from HW13.hw13 import Errors
from HW13.hw13.Core.DBCreator import DBCreator
from HW13.hw13.log import store


class DBManagerMixin:
    """As I have prepared this mixin class for all databases, I should pass a database name to init which is
        an object from DBCreator class!"""

    def __init__(self, db_name=storedatabase3) -> None:
        self.db_name = db_name
        self.table_name_len = db_name.table_name_len
        self.db_connection = storedatabase3.connect_to_db()

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, name: object):
        if isinstance(name, DBCreator):
            self._db_name = name
        else:
            raise Errors.InstanceError()

    def read(self, table_name, col_name, value):
        with self.db_connection as cur:
            cur.execute(f"""SELECT * FROM {table_name} WHERE {col_name} = '{value}'""")
            records = cur.fetchall()
            store.info('record was read and shown!')
        return records

    """ first, checks if the table name is in list and the length of columns that given in kwargs are the same or not.
    second, updates the values of a new row in considered table."""

    def insert(self, table_name, a_dict) -> None:
        with self.db_connection as cur:
            cur.execute(
                f"""
                INSERT INTO {table_name} ({', '.join(a_dict.keys())}) VALUES {tuple(a_dict.values())}
                """)
        store.info(f'data was inserted in {table_name} table!')

        # store.error('The inserted table name is not valid!')
        # raise Errors.TableNameError()

    """rows of all records should be equal to rows of distinct records of a column with unique values!"""

    def delete(self, table_name, col_name, value) -> None:
        with self.db_connection as cur:
            cur.execute(f"""SELECT * FROM {table_name}""")
            all_rec = len(cur.fetchall())
            cur.execute(f"""SELECT DISTINCT {col_name} FROM {table_name}""")
            dist_rec = len(cur.fetchall())
            if all_rec == dist_rec:
                cur.execute(f"""DELETE FROM {table_name} WHERE {col_name} = '{value}'""")
                store.info(f'Data was deleted from {table_name} table')
            else:
                store.error('chosen column has duplicated values!')
                raise Errors.InvalidColumn()

    """ Notice that value should be a unique id or something and col_name helps to find the correct row!
        col_names are primary keys in each model and values are the given to update a specific row, like userid... .
        kwargs keys are old value and values are new value"""

    def update(self, table_name, col_name, value, **kwargs) -> None:
        with self.db_connection as cur:
            cur.execute(f"""SELECT * FROM {table_name};""")
            all_rec = len(cur.fetchall())
            cur.execute(f"""SELECT DISTINCT {col_name} FROM {table_name};""")
            dist_rec = len(cur.fetchall())
            if all_rec == dist_rec:
                for k, v in kwargs.items():
                    cur.execute(f"""UPDATE {table_name} SET {k} = {v} WHERE {col_name} = '{value}';""")
                store.info(f'{table_name} was updated!')
            else:
                store.error('chosen column has duplicated values and could not be updated!')
                raise Errors.InvalidColumn()


