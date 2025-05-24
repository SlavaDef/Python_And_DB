import pymysql

from connection.py_mysqlconektor import UseDatabase
from constants.constants import  db_config2



# створення бд та таблиці з налаштуваннями для адмін користувача root + пароль
def create_db_and_table(db_name):

        # Підключення до MySQL сервера
        try:
            # Спочатку створюємо базу даних
            with pymysql.connect(host='127.0.0.1',user='root',password='1234') as connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                connection.commit()
                print("База даних створена успішно")

            with UseDatabase(**db_config2) as cursor:

                cursor.execute("""
                           CREATE TABLE IF NOT EXISTS ball (
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               ball_name VARCHAR(50) NOT NULL,
                               ball_owner VARCHAR(100) NOT NULL,
                               ball_year INT NOT NULL,
                               date DATE )""")
                print("Таблиця створена успішно")
        except Exception as e:
            print(f"Помилка: {e}")


#  додавання мяча
def add_ball(ball_name, ball_owner, ball_year ):
    with UseDatabase(**db_config2) as cursor:
        sql = "INSERT INTO ball (ball_name, ball_owner, ball_year, date) VALUES (%s, %s, %s, CURDATE())"
        cursor.execute(sql, (ball_name, ball_owner, ball_year))


def get_all_balls():
    with UseDatabase(**db_config2) as cursor:
        cursor.execute("SELECT * FROM ball")
        return cursor.fetchall()

def get_by_id(id):
    with UseDatabase(**db_config2) as cursor:
        cursor.execute("SELECT * FROM ball WHERE id = %s", (id,))
        return cursor.fetchone()

def delete_by_id(id):
    with UseDatabase(**db_config2) as cursor:
        cursor.execute("DELETE FROM ball WHERE id = %s", (id,))


def update_by_id(id, ball_name, ball_owner, ball_year):
    with UseDatabase(**db_config2) as cursor:
        cursor.execute("UPDATE ball SET ball_name = %s, ball_owner = %s, ball_year = %s WHERE id = %s",
                       (ball_name, ball_owner, ball_year, id))

def update_by_name(ball_name, ball_owner, ball_year):
    with UseDatabase(**db_config2) as cursor:
        cursor.execute("UPDATE ball SET ball_name = %s, ball_owner = %s, ball_year = %s WHERE ball_name = %s",
                       (ball_name, ball_owner, ball_year, ball_name))


#create_db_and_table('balls')

#add_ball("Ball1", "Bob1", 2023)
#add_ball("Ball2", "Bob2", 2022)
#add_ball("Ball2", "Bob3", 2020)

#delete_by_id(7)

for ball in get_all_balls(): print(ball)

#print(get_by_id(7))




