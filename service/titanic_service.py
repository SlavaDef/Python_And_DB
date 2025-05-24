import sqlite3

from constants.constants import read_all


def read_from_db(sql) -> list:
    try:
        with sqlite3.connect('../titanic.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Помилка: {e}")
        return []


for row in read_from_db(read_all): print(row)