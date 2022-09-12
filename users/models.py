
from HW13.hw13.Core.models import DBModel


class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, first_name, last_name, phone, national_id, age, password, id=None) -> None:
        super().__init__()

        if id: self.id = id