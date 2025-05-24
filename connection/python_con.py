import pymysql
from pymysql import Error

try:
    # Підключення до MySQL сервера
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='1234'
    )

    with connection.cursor() as cursor:
        # Створення бази даних
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
        print("База даних створена успішно")

        cursor.execute("SELECT user FROM mysql.user WHERE user = 'new_user'")
        result = cursor.fetchone()

        # Якщо користувача не існує - створюємо
        if not result:
            cursor.execute("CREATE USER 'new_user'@'127.0.0.1' IDENTIFIED BY 'password123'")
            print("Користувач створений успішно")
        else:
            print("Користувач вже існує")

        # Надання прав
        cursor.execute("GRANT ALL PRIVILEGES ON test_db.* TO 'new_user'@'127.0.0.1'")
        cursor.execute("FLUSH PRIVILEGES")

        print("Користувач створений та права надані успішно")

    connection.commit()

except Error as e:
    print(f"Помилка: {e}")

finally:
    if connection:
        connection.close()
        print("З'єднання з MySQL закрито")
