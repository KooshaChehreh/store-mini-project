from unittest import TestCase
from HW13.hw13.users.users import User
from HW13.hw13.file.files import Files
from orderitem import OrderItem
from HW13.hw13.order.order import Order
from HW13.hw13 import Errors


class DBManagerTest(TestCase):

    def setUp(self):
        self.user1 = User('koosha', 'Koosha1234', 'Koosha Chehreh', 29, '2050426119', "09356195525", False)
        self.user2 = User('Akbar', 'Akbar123', 'Akbar Asghar', 40, '5060426119', "09356191111", True)
        self.file1 = Files('life is good', 'there.over there', 100000, 'Mohammad Akbar')
        self.file2 = Files('humanity', 'here.right there', 210000, 'Maryam Asghar')
        self.order1 = Order(self.user1.userid, self.file1, self.file2)
        self.order2 = Order(self.user2.userid, self.file1, self.file2)
        self.orderitem1 = OrderItem(self.order1.orderid, self.order1)
        self.orderitem2 = OrderItem(self.order2.orderid, self.order2)

    """ Regex tests are same as each other. So, I did not test all instance attributes in order to save time"""

    def test_purchase(self) -> None:
        self.assertIsInstance(self.orderitem1.purchase, Order)
        self.assertIsInstance(self.orderitem2.purchase, Order)

    def test_orderid(self):
        self.assertIn(self.orderitem1.orderid, self.order1.list_of_orderid.values())

    def test_insert_orderitem(self):  # This test will pass because I did not insert setup objects to appropriate dicts.
        with self.assertRaises(Errors.InvalidOrderId):
            self.orderitem1.insert_item()

    def test_read_item(self):
        self.orderitem1.insert_item()
        self.order1.list_of_orderid.update({self.order1.orderid: vars(self.order1)})
        """ u gives us a list of tuples and our list just have one tuple! so I have gotten the first one
            and converted type of v in order to be comparable!"""
        u = self.orderitem1.read_item(f"{self.orderitem1.orderid}")
        v = tuple(vars(self.orderitem1).values())
        self.assertEqual(u, v)

    def test_delete_user(self):
        with self.assertRaises(Errors.InvalidOrderItemId):
            self.orderitem1.delete_item('1234')

    def test_update_user(self):
        with self.assertRaises(Errors.InvalidOrderItemId):
            self.orderitem1.update_item('1234')

