DB_CONNECTION = {
    "HOST": "localhost",
    "USER": "postgres",
    "PORT": 5432,
    "PASSWORD": "postgres",
    "DBNAME": "storedatabase3"
}


TABLES_QUERY = {
    'users': """CREATE TABLE IF NOT EXISTS users
                (
                username varchar(50) NOT NULL,
                pass_word varchar(50) NOT NULL,
                userid VARCHAR(255) PRIMARY KEY,
                fullname varchar(150) NOT NULL,
                age int NOT NULL,
                national_id varchar(20) NOT NULL,
                phone varchar(20) NOT NULL,
                is_owner boolean NOT NULL
                );""",
    'orderitem': """CREATE TABLE IF NOT EXISTS orderitem
                (
                orderid VARCHAR(255) NOT NULL,
                filename varchar(150) NOT NULL,
                price VARCHAR(255) NOT NULL,
                orderitemid VARCHAR(255) PRIMARY KEY
                );""",
    'orders': """CREATE TABLE IF NOT EXISTS orders
                (
                userid VARCHAR(255) PRIMARY KEY,
                totalprice int NOT NULL,
                qtyfiles int NOT NULL,
                orderdate date NOT NULL,
                orderid VARCHAR(255) NOT NULL
                );""",
    'files': """CREATE TABLE IF NOT EXISTS files
                (
                filename VARCHAR(100) PRIMARY KEY,
                directory varchar(255) NOT NULL,
                price int NOT NULL,
                add_file_date date NOT NULL,
                edit_date date NOT NULL,
                owner_name VARCHAR(50)
                );""",
    'filecomment': """CREATE TABLE IF NOT EXISTS filecomment
                (
                cmid VARCHAR(255) PRIMARY KEY,
                userid VARCHAR(20) NOT NULL,
                filename VARCHAR(100) NOT NULL,
                description Text NOT NULL
                );"""
}


