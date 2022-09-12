from HW13.hw13.Core.models import DBModel
from HW13.hw13.Core.DBCreator import storedatabase3
from HW13.hw13 import Errors
from HW13.hw13.Core.managers import DBManagerMixin
import re
from uuid import uuid4
from HW13.hw13.log import store


class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'userid'
    list_of_user = {}
    list_of_user_pass = {}
    list_of_userid = {}
    list_of_id = []

    def __init__(self, username, pass_word, fullname, age, national_id, phone, is_owner: bool):
        self.username = self.username_validation(username)
        self.pass_word = self.pass_word_validation(pass_word)
        self.userid = str(uuid4()).split('-')[0]
        self.fullname = self.fullname_validation(fullname)
        self.age = self.age_validation(age)
        self.national_id = self.national_id_validation(national_id)
        self.phone = self.phone_validation(phone)
        self.is_owner = self.is_owner_validation(is_owner)

    @staticmethod
    def DBManager():
        return DBManagerMixin(storedatabase3)

    @staticmethod
    def is_owner_validation(value):
        if isinstance(value, bool):
            return value
        else:
            raise Errors.BoolError()

    @staticmethod
    def pass_word_validation(a_pass: str):
        pass_regex = re.compile(r"^[\w\d.@&]{4,20}$")
        if re.match(pass_regex, a_pass) is not None:
            return a_pass
        else:
            store.error('password is invalid!')
            raise Errors.InvalidPassword()

    @staticmethod
    def fullname_validation(fullname: str):
        fullname_regex = re.compile(r"^[a-zA-Z\s]{4,30}$")
        if re.match(fullname_regex, fullname) is None:
            store.error('fullname is invalid!')
            raise Errors.InvalidFullname()
        return fullname

    def username_validation(self, username):
        username_regex = re.compile(r'^[\w\-.]{3,20}$')
        if re.match(username_regex, username) is not None and username not in self.__class__.list_of_user.values():
            return username
        else:
            store.error('username is duplicated or invalid!')
            raise Errors.InvalidUsername()

    @staticmethod
    def phone_validation(phone_no):
        first_regex = re.compile(r'^(\+98\d{10})|(09\d{9})')
        if first_regex.match(phone_no) is not None:
            return phone_no
        else:
            store.error('phone number is invalid!')
            raise Errors.InvalidPhone()

    @staticmethod
    def age_validation(age: int):
        first_regex = re.compile(r'^\d{1,3}$')
        if first_regex.match(str(age)) is not None:
            return str(age)
        else:
            store.error('age is invalid!')
            raise Errors.InvalidAge()

    @staticmethod
    def national_id_validation(national_id):
        first_regex = re.compile(r'^\d{10}$')
        if first_regex.match(national_id) is not None:
            return national_id
        else:
            store.error('national ID should be 10 digits!')
            raise Errors.InvalidNationalId()

    def show_id(self):
        self.list_of_id.append(self.userid)
        return self.userid

    def nominate(self) -> None:
        if self.username in self.list_of_user.keys():
            raise Exception('User were nominated before!')
        else:
            self.insert_user()
            self.list_of_user_pass.update({self.username: self.pass_word})
            self.list_of_user[self.username] = vars(self)
            self.list_of_userid.update({self.userid: vars(self)})
            print(f'your UserID is {self.show_id()} and keep it secret!')
            store.info(f'User {self.fullname} was nominated successfully!')

    def read_user(self, value):
        record = self.DBManager().read(self.__class__.TABLE, self.__class__.PK, value)
        return record

    def insert_user(self):
        if self.username in self.__class__.list_of_user.keys():
            raise Errors.DuplicateUser()
        else:
            self.DBManager().insert(self.__class__.TABLE, vars(self))

    def delete_user(self, userid) -> None:
        if userid in self.__class__.list_of_userid:
            self.DBManager().delete(self.__class__.TABLE, self.__class__.PK, userid)
        else:
            store.error('User deletion was not successful!')
            raise Errors.InvalidUserId()

    def update_user(self, userid, **kwargs) -> None:
        if userid in self.__class__.list_of_userid:
            self.DBManager().update(self.__class__.TABLE, self.__class__.PK, userid, **kwargs)
        else:
            raise Errors.InvalidUserId()



