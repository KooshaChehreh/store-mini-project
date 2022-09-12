from HW13.hw13.Core.models import DBModel
from HW13.hw13.file.files import Files
from HW13.hw13.Core.DBCreator import storedatabase3
from HW13.hw13.Core.managers import DBManagerMixin
from HW13.hw13 import Errors
from uuid import uuid4
from datetime import date
from HW13.hw13.log import store


class Order(DBModel):  # order model
    TABLE = 'orders'
    PK = 'userid'
    list_of_orderid = {}

    def __init__(self, userid, *files: Files) -> None:
        self.userid = userid
        self.files = files
        self.orderid = str(uuid4()).split('-')[0]
        for file in files:
            self.files_validation(file)
        """ an instance dict attr to update the users purchases in an order"""
        self.list_of_filename_price = {}
        for file in files:
            self.list_of_filename_price.update({file.filename: file.price})
        self.price_sum = 0
        for file in files:
            self.price_sum += file.price
        self.totalprice = self.price_sum
        self.qtyfiles = len(files)
        self.orderdate = date.today()
        self.__class__.list_of_orderid.update({self.userid: self.orderid})

    @staticmethod
    def DBManager():
        return DBManagerMixin(storedatabase3)

    @staticmethod
    def files_validation(file: object):
        if isinstance(file, Files):
            return None
        else:
            store.error(f'{file} is not an instance of class Files!')
            Errors.InstanceError()

    def read_order(self, value) -> tuple:
        record = self.DBManager().read(self.__class__.TABLE, self.__class__.PK, value)
        return record

    def insert_order(self, orderid) -> None:
        if orderid in self.__class__.list_of_orderid.values():
            raise Errors.DuplicateOrderId()
        else:
            self.DBManager().insert(self.__class__.TABLE, {'userid': self.userid,
                                                           'totalprice': self.totalprice,
                                                           'qtyfiles': self.qtyfiles, 'orderdate': self.orderdate,
                                                           'orderid': self.orderid})

    def delete_oder(self, orderid) -> None:
        self.DBManager().delete(self.__class__.TABLE, self.__class__.PK, orderid)

    def update_file(self, orderid, **kwargs) -> None:
        self.DBManager().update(self.__class__.TABLE, self.__class__.PK, orderid, **kwargs)
