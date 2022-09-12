from HW13.hw13.Core.models import DBModel
from HW13.hw13.order.order import Order
from uuid import uuid4
from HW13.hw13.Core.DBCreator import storedatabase3
from HW13.hw13.Core.managers import DBManagerMixin
from HW13.hw13.log import store
from HW13.hw13 import Errors


class OrderItem(DBModel):  # OrderItem model
    TABLE = 'orderitem'
    PK = 'orderitemid'
    list_of_items = {}

    def __init__(self, orderid, purchase: Order) -> None:
        self.orderid = orderid
        self.purchase = purchase

    @staticmethod
    def DBManager():
        return DBManagerMixin(storedatabase3)

    def read_item(self, orderitemid) -> tuple:
        record = self.DBManager().read(self.__class__.TABLE, self.__class__.PK, orderitemid)
        store.info('records of items are shown!')
        return record

    def insert_item(self) -> None:

        """ each row has 4 column which could be filled with some attributes of each file that have been added to
            be purchased! Moreover, I have dedicated a unique item ID to each row in order to read and delete if the
            user ordered to delete or read the items. """
        if self.orderid in Order.list_of_orderid:
            for item in self.purchase.list_of_filename_price:
                items = {'orderid': self.orderid,
                        'filename': self.purchase.list_of_filename_price.keys([item]),
                        'price': self.purchase.list_of_filename_price.values([item]),
                        'orderitemid': str(uuid4()).split('-')[0]}
                self.DBManager().insert(self.__class__.TABLE, items)
                self.__class__.list_of_items.update({items['orderitemid']: items})
            store.info('items inserted to the user\'s order')
        else:
            store.error('The order is not created yet!')
            raise Errors.InvalidOrderId()

    def delete_item(self, orderitemid) -> None:
        if orderitemid in self.__class__.list_of_items.keys():
            self.DBManager().delete(self.__class__.TABLE, self.__class__.PK, orderitemid)
        else:
            raise Errors.InvalidOrderItemId()

    def update_item(self, orderitemid, **kwargs) -> None:
        if orderitemid in self.__class__.list_of_items.keys():
            self.DBManager().update(self.__class__.TABLE, self.__class__.PK, orderitemid, **kwargs)
        else:
            raise Errors.InvalidOrderItemId()
