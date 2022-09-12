from unittest import TestCase
from users import User
from HW13.hw13 import Errors


class TestUser(TestCase):

    def setUp(self):
        self.user1 = User('koosha', 'Koosha1234', 'Koosha Chehreh', 29, '2050426119', "09356195525", False)
        self.user2 = User('Akbar', 'Akbar123', 'Akbar Asghar', 40, '5060426119', "09356191111", True)

    """ Regex tests are same as each other. So, I did not test all instance attribute in order to save time"""

    def test_username(self) -> None:  # This test checks whether the username matches the regex or not.
        self.assertRegex(self.user1.username, r'^[\w\-.]{3,20}$')
        self.assertRegex(self.user2.username, r'^[\w\-.]{3,20}$')

    def test_is_owner(self):  # Test checks whether is_owner is variable with type of bool class or not.
        self.assertIsInstance(self.user1.is_owner, bool)
        self.assertIsInstance(self.user2.is_owner, bool)

    def test_insert_user(self):  # this test tries to raise duplicate user error.
        with self.assertRaises(Errors.DuplicateUser):
            self.user1.nominate()
            self.user1.insert_user()

    def test_read_user(self):  # this test reads the record and compares it with the object in dictionary.
        self.user1.insert_user()
        u = self.user1.read_user(f"{self.user1.userid}")[0]
        """ u gives us a list of tuples and our list just have one tuple! so I have gotten the first one
                    and converted type of v in order to be comparable!"""
        v = tuple(vars(self.user1).values())
        self.assertEqual(u, v)

    def test_delete_user(self):  # the test tries to raise Invalid User ID.
        with self.assertRaises(Errors.InvalidUserId):
            self.user1.delete_user('1234')

    def test_update_user(self):  # the test tries to raise Invalid User ID.
        with self.assertRaises(Errors.InvalidUserId):
            self.user1.update_user('1234')
