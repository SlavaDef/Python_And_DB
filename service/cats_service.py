from connection.py_mysqlconektor import UseDatabase
from constants.constants import db_config


# Створення таблиці за допомогою Python але сама бд і користувач створені окремо через термінал
def create_tables():
    with UseDatabase(**db_config) as cursor:
        # Створення таблиці
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cat (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cat_name VARCHAR(50) NOT NULL UNIQUE,
                cat_owner VARCHAR(100) NOT NULL UNIQUE,
                cat_year INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")


# Функція для додавання кота
def add_cat(cat_name, cat_owner, cat_year ):
    with UseDatabase(**db_config) as cursor:
        sql = "INSERT INTO cat (cat_name, cat_owner, cat_year) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cat_name, cat_owner, cat_year))


# Функція для отримання всіх котів
def get_all_cats():
    with UseDatabase(**db_config) as cursor:
        cursor.execute("SELECT * FROM cat")
        return cursor.fetchall()


# перевели час у більш читабельний формат
def get_all_cats2():
    with UseDatabase(**db_config) as cursor:
        cursor.execute("""
            SELECT id, cat_name, cat_owner, cat_year, 
            DATE_FORMAT(created_at, '%d.%m.%Y %H:%i:%s') as formatted_date 
            FROM cat
        """)
        return cursor.fetchall()



def get_all_universal(sql):
    with UseDatabase(**db_config) as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def get_by_id(id):
    with UseDatabase(**db_config) as cursor:
        cursor.execute("SELECT * FROM cat WHERE id = %s", (id,))
        return cursor.fetchone()


def delete_by_id(id):
    with UseDatabase(**db_config) as cursor:
        cursor.execute("DELETE FROM cat WHERE id = %s", (id,))


def update_by_id(id, cat_name, cat_owner, cat_year):
    with UseDatabase(**db_config) as cursor:
        cursor.execute("UPDATE cat SET cat_name = %s, cat_owner = %s, cat_year = %s WHERE id = %s",
                       (cat_name, cat_owner, cat_year, id))


def update_owner_by_id(id, cat_owner):
    with UseDatabase(**db_config) as cursor:
        cursor.execute("UPDATE cat SET cat_owner = %s WHERE id = %s",
                       (cat_owner, id))


def delete_all():
    with UseDatabase(**db_config) as cursor:
        cursor.execute("DELETE FROM cat")


for row in get_all_cats2(): print(row)

#update_ovwer_by_id(1, "Kate")
#print(get_by_id(1))
