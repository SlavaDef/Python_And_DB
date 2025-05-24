import pandas as pd
import sqlite3  # або інший конектор до вашої БД

from constants.constants import titanic

# Читаємо CSV файл
df = pd.read_csv(titanic)

# Підключаємося до бази даних
conn = sqlite3.connect('../titanic.db')
cursor = conn.cursor()  # Створюємо курсор


# Завантажуємо дані до таблиці
df.to_sql('table_name', conn, if_exists='append', index=False)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
cursor.execute("SELECT * FROM table_name")
people_fom = cursor.fetchall()
tables = cursor.fetchall()
print("Таблиці в базі даних:", tables)

for person in people_fom: print(person)

cursor.close()
conn.close()