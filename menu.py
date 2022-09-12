from menutools import Menu
from HW13.hw13.users.users import User
from HW13.hw13.file.files import Files


def about():
    print('Welcome To Chehreh Digital store! :D ')


def user_input_sign_up() -> None:
    username = input('Username: ')
    password = input('password: ')
    full_name = input('full_name: ')
    age = int(input('age: '))
    national_id = input('National_id: ')
    phone = input('phone: ')
    inp = input('are you owner of a file? yes or no: ')
    if inp.lower() == 'yes':
        u = User(username, password, full_name, age, national_id, phone, True)
        u.nominate()
        u.show_id()
    else:
        u = User(username, password, full_name, age, national_id, phone, False)
        u.nominate()
        u.show_id()


def file_input_insert() -> None:
    username = input('Enter your username: ')
    if username in logged_user_in_out and User.list_of_user[username]['is_owner'] is True:
        filename = input('filename: ')
        directory = input('directory: ')
        price = int(input('price: '))
        owner_name = input('owner_name: ')
        f = Files(filename, directory, price, owner_name)
        f.insert_file()
    else:
        print('You are not permitted to add file to our library!')


logged_user_in_out = []


def log_in():
    username = input('Enter your username: ')
    if username in User.list_of_user_pass.keys():
        password = input('Enter your password: ')
        if User.list_of_user_pass[username] == password:
            print('Login was Successful!')
            logged_user_in_out.append(username)
        else:
            print('Incorrect Password!')
    else:
        print('Incorrect Username! You should sign up first!')


def log_out():
    username = input('Enter your username: ')
    if username in logged_user_in_out:
        logged_user_in_out.remove(username)
    else:
        print('you are not logged in!')


def files_list():
    if len(Files.list_of_filename.keys()) == 0:
        print('No file added yet!')
    else:
        print(Files.list_of_filename)


def purchase_order():
    username = input('Enter your username: ')
    if username in logged_user_in_out:
        order = list(map(str, input('Enter File names: ').split(', ')))
        for file in order:
            if file not in Files.list_of_filename.keys():
                print(f"{file} is not in our list. Maybe it will be available soon! We appreciate your "
                      f"suggestions in Suggestion part! :)")
        total_price = 0
        total_qty = 0
        for i in range(len(order)):
            total_price += Files.list_of_filename[order[i]]['price']
            total_qty += 1
        print(f"You have ordered {total_qty} files with total price of {total_price} $")


def file_update():
    username = input('Enter your username: ')
    if username in logged_user_in_out and User.list_of_user[username]['is_owner'] is True:
        filename = input('File name You want to update: ')
        col_name = input('column name: ').strip()
        value = input('Value:')
        Files.list_of_filename_obj[username].update_file(filename, {col_name: value})


def delete_file():
    username = input('Enter your username: ')
    if username in logged_user_in_out and User.list_of_user[username]['is_owner'] is True:
        file_name = input('File name You want to update: ')
        Files.list_of_filename_obj[username].delete_file(file_name)


def suggestion():
    suggested_files = []
    s = input('suggest your file name please: ')
    if s in suggested_files:
        print('Some body suggested this file before, Thank U!')
    else:
        suggested_files.append(s)
        print('Thank you for your suggestion! :)')


menu = Menu(header='Chehreh File Store\n', align='center', prompt='--> ', splitter=')', border='----*',
            border_length=17)

menu.add(
    ('Main Menu', [('About', about), ('sign up', user_input_sign_up), ('Log in', log_in), ('files list', files_list),
                   ('Files menu', menu.next), ('Exit', menu.exit)]))
menu.add(
    ('File menu', [('Order a purchase', purchase_order), ('delete/update/insert a file', menu.next),
                   ('Back', menu.back), ('Log out', log_out), ('Exit menu', menu.exit)]))
menu.add(('Edit file menu', [('Insert File', file_input_insert), ('Update File', file_update),
                             ('Delete File', delete_file), ('Suggestion', suggestion), ('Back', menu.back),
                             ('Log out', log_out), ('Exit', menu.exit)]))

menu.execute()
