from unittest import TestCase
from HW13.hw13.users.users import User
from HW13.hw13.file.files import Files
from HW13.hw13.order.order import Order
from datetime import date


class DBManagerTest(TestCase):

    def setUp(self):
        self.user1 = User('koosha', 'Koosha1234', 'Koosha Chehreh', 29, '2050426119', "09356195525", False)
        self.user2 = User('Akbar', 'Akbar123', 'Akbar Asghar', 40, '5060426119', "09356191111", True)
        self.file1 = Files('life is good', 'there.over there', 100000, 'Mohammad Akbar')
        self.file2 = Files('humanity', 'here.right there', 210000, 'Maryam Asghar')
        self.order1 = Order(self.user1.userid, self.file1, self.file2)
        self.order2 = Order(self.user2.userid, self.file1, self.file2)

    def test_userid(self):
        self.user1.nominate()
        self.user2.nominate()
        self.assertIn(self.order1.userid, User.list_of_userid)
        self.assertIn(self.order2.userid, User.list_of_userid)

    def test_file(self):
        for file in self.order1.files:
            self.assertIsInstance(file, Files)

    def test_price(self):
        p = self.file1.price + self.file2.price
        total_price = 0
        for file in self.order1.files:
            total_price += file.price

        self.assertEqual(p, total_price)

    def test_order_date(self):
        self.assertIsInstance(self.order1.orderdate, date)
        self.assertIsInstance(self.order2.orderdate, date)

