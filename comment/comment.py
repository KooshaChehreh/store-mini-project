from HW13.Core.models import DBModel
from HW13.users.users import User
from HW13.file.files import Files
from uuid import uuid4
from HW13.Core.DBCreator import storedatabase3
from HW13.Core.managers import DBManagerMixin
from HW13.log import store
from HW13 import Errors


class FileComment(DBModel):  # FileComment model
    TABLE = 'filecomment'
    PK = 'cmid'
    list_of_items = {}

    def __init__(self, userid, filename, text: str) -> None:
        self.cmid = str(uuid4()).split('-')[0]
        self.userid = self.validate_userid(userid)
        self.filename = filename
        self.test = text

    @staticmethod
    def DBManager():
        return DBManagerMixin(storedatabase3)

    @staticmethod
    def validate_userid(value):
        if value not in User.list_of_userid:
            store.error('Invalid User Id inserted!')
            raise Errors.InvalidUserId()

    @staticmethod
    def validate_filename(value):
        if value not in Files.list_of_filename:
            store.error('Invalid file name inserted!')
            raise Errors.InvalidFilename()

    def insert_comment(self) -> None:
        self.DBManager().insert(self.__class__.TABLE, vars(self))
        store.info('Comment added!')
