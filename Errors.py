class TableNameError(Exception):

    def __str__(self):
        return 'Table name not found!'


class InvalidColumn(Exception):

    def __str__(self):
        return 'The column has duplicated values! Values should be unique'


class InvalidFullname(Exception):

    def __str__(self):
        return 'Full name is not valid!'


class InvalidPhone(Exception):

    def __str__(self):
        return 'Phone number is not valid!'


class InvalidAge(Exception):

    def __str__(self):
        return 'age is not valid!'


class InvalidNationalId(Exception):

    def __str__(self):
        return 'Natinal ID is not valid!'


class InstanceError(Exception):

    def __str__(self):
        return 'This name is not DBCreator\'s instance!'


class DuplicateUser(Exception):

    def __str__(self):
        return 'This user exists in Database!'


class InvalidPassword(Exception):

    def __str__(self):
        return 'Invalid password you have chosen!'


class InvalidDirectory(Exception):

    def __str__(self):
        return 'Invalid Directory you have chosen!'


class InvalidFilename(Exception):

    def __str__(self):
        return 'Invalid Filename you have entered!'


class InvalidUsername(Exception):

    def __str__(self):
        return 'Invalid username you have entered!'


class InvalidDateType(Exception):

    def __str__(self):
        return 'Invalid username you have entered!'


class DuplicateFilename(Exception):

    def __str__(self):
        return 'This file were added before!'


class DuplicateOrderId(Exception):

    def __str__(self):
        return 'This order was closed before!'


class InvalidPrice(Exception):

    def __str__(self):
        return 'Price should contain digits!'


class BoolError(Exception):

    def __str__(self):
        return 'Not Boolean!'


class InvalidUserId(Exception):

    def __str__(self):
        return 'User id does not exists!'


class InvalidOrderId(Exception):

    def __str__(self):
        return 'Order id does not exists!'


class InvalidOrderItemId(Exception):

    def __str__(self):
        return 'Order item id does not exists!'
