
titanic = 'C:/Users/Admin/Desktop/Files/titanic.csv'

read_all = 'SELECT * FROM table_name'

select_id = 'SELECT * FROM cat WHERE id > 2'


db_config = {
    'host': '127.0.0.1',
    'user': 'Bob',
    'password': '1234',
    'database': 'cat88',
    'port': 3306,  # стандартний порт MySQL
    'charset': 'utf8mb4'
}

db_config2 = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'balls',
    'port': 3306,  # стандартний порт MySQL
    'charset': 'utf8mb4'
}



#mysql -u root -p вхід до mySql в терміналі
#CREATE DATABASE cat88 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
#CREATE USER 'Bob'@'127.0.0.1' IDENTIFIED BY '1234';
#GRANT ALL PRIVILEGES ON cat88.* TO 'Bob'@'127.0.0.1';
#SHOW DATABASES;
#mysql -u root -p вхід до mySql в терміналі
