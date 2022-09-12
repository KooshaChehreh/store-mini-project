from unittest import TestCase
from HW13.hw13.file.files import Files
from HW13.hw13 import Errors


class FilesTest(TestCase):

    def setUp(self):
        self.file1 = Files('life is good', 'there.over there', 100000, 'Mohammad Akbar')
        self.file2 = Files('humanity', 'here.right there', 210000, 'Maryam Asghar')

    def test_filename(self) -> None:
        self.assertRegex(self.file1.filename, r'^[\w\d\-.\s]{1,50}$')
        self.assertRegex(self.file2.filename, r'^[\w\d\-.\s]{1,50}$')

    def test_directory(self) -> None:
        self.assertRegex(self.file1.filename, r"^[\w\d\-\\.\s]{4,255}$")
        self.assertRegex(self.file2.filename, r"^[\w\d\-\\.\s]{4,255}$")

    def test_price(self):
        self.assertIsInstance(self.file1.price, int)
        self.assertIsInstance(self.file2.price, int)

    def test_insert_file(self):  # Raises the Error.
        with self.assertRaises(Errors.DuplicateFilename):
            Files.list_of_filename.update({'humanity': vars(self.file2)})
            self.file2.insert_file()

    def test_read_file(self):

        """ This test has date variables and synchronised with datetime. So, we should create a new object whenever
            we want to test this part in order to pass the test. So, If the record exists we delete and create new one
            and if it does not exist we will run the test without delete!"""
        if self.file1.filename in self.file1.list_of_filename.keys():
            self.file1.delete_file(self.file1.filename)
        else:
            self.file1.insert_file()
            u = self.file1.read_file(f"{self.file1.filename}")[0]
            """ u gives us a list of tuples and our list just have one tuple! so I have gotten the first one
                        and converted type of v in order to be comparable!"""
            v = tuple(vars(self.file1).values())
            print(v, '\n', u)
            self.assertEqual(u, v)

    def test_delete_file(self):  # Raises the Error.
        with self.assertRaises(Errors.InvalidFilename):
            self.file1.delete_file('hi')

    def test_update_file(self):  # updates the price attribute of file1 object and compares it with unaltered price.
        self.file1.list_of_filename.update({'life is good': vars(self.file1)})
        f = self.file1.edit_date
        self.file1.update_file(self.file1.filename, price=520000)
        self.assertNotEqual(self.file1.edit_date, f)
