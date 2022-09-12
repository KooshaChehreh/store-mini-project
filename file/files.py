from HW13.hw13.Core.models import DBModel
from HW13.hw13 import Errors
from HW13.hw13.Core.managers import DBManagerMixin
from HW13.hw13.Core.DBCreator import storedatabase3
import re
from datetime import datetime
from HW13.hw13.log import store


class Files(DBModel):  # File model
    TABLE = 'files'
    PK = 'filename'
    list_of_filename = {}
    list_of_filename_obj = {}

    def __init__(self, filename, directory, price: int, owner_name) -> None:
        self.filename = self.filename_validation(filename)
        self.directory = self.directory_validation(directory)
        self.price = price
        self.add_file_date = datetime.now().strftime('%Y, %m, %d')
        self.edit_date = datetime.now().strftime('%Y, %m, %d')
        self.owner_name = self.owner_name_validation(owner_name)
        self.__class__.list_of_filename.update({self.filename: vars(self)})
        self.__class__.list_of_filename_obj.update({self.filename: self})

    @staticmethod
    def DBManager():
        return DBManagerMixin(storedatabase3)

    @staticmethod
    def directory_validation(directory: str):
        directory_regex = re.compile(r"^[\w\d\-\\.\s]{4,255}$")
        if re.match(directory_regex, directory) is None:
            store.error('Directory was not found!')
            raise Errors.InvalidDirectory()
        else:
            return directory

    def filename_validation(self, filename):
        filename_regex = re.compile(r'^[\w\d\-.\s]{1,50}$')
        if re.match(filename_regex, filename) is not None and filename not in self.__class__.list_of_filename.values():
            return filename
        store.error('file name is not valid!')
        raise Errors.InvalidFilename()

    @staticmethod
    def price_validation(value):
        directory_regex = re.compile(r"[1-9]\d{1,10}$")
        if re.match(directory_regex, value) is None:
            store.error('price should be a valid digit!')
            raise Errors.InvalidPrice()
        else:
            return value

    @staticmethod
    def edit_date_validation(edit_date: str):
        first_regex = re.compile(r'^[\d{4}]-[\d{2}]-[\d{2}]')
        if first_regex.match(edit_date) is not None and \
                datetime.strptime(edit_date, '%Y-%M-%d').date <= datetime.now().date:
            return edit_date
        store.error('Date was not acceptable!')
        raise Errors.InvalidDateType()

    @staticmethod
    def owner_name_validation(owner_name: str):
        first_regex = re.compile(r'^[A-Za-z\s]{4,30}$')
        if first_regex.match(owner_name) is not None:
            return owner_name
        else:
            store.error('owner name is not acceptable!')
            raise Errors.InvalidFullname()

    @staticmethod
    def add_file_date_validation(add_file_date: str):
        first_regex = re.compile(r'^[\d{4}]-[\d{2}]-[\d{2}]$')
        if first_regex.match(add_file_date) is not None and \
                datetime.strptime(add_file_date, '%Y-%M-%d').date <= datetime.now().date:
            return add_file_date
        store.error('Date was not acceptable!')
        raise Errors.InvalidDateType()

    def read_file(self, value) -> tuple:
        record = self.DBManager().read(self.__class__.TABLE, self.__class__.PK, value)
        return record

    def insert_file(self):
        if self.filename in self.__class__.list_of_filename.keys():
            raise Errors.DuplicateFilename()
        else:
            self.DBManager().insert(self.__class__.TABLE, vars(self))

    def delete_file(self, filename) -> None:
        if filename in self.__class__.list_of_filename:
            self.DBManager().delete(self.__class__.TABLE, self.__class__.PK, filename)
        else:
            store.error('File deletion was not successful!')
            raise Errors.InvalidFilename

    def update_file(self, filename, **kwargs) -> None:
        if filename in self.__class__.list_of_filename:
            self.DBManager().update(self.__class__.TABLE, self.__class__.PK, filename, **kwargs)
            self.edit_date = datetime.now()
        else:
            store.error('Unsuccessful update!')
            raise Errors.InvalidFilename()


if '__name__' == '__main__':
    f = Files('koosha', 'koosha.ads', 1234, 'koosha chehreh')
    f.insert_file()
