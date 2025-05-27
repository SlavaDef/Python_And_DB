import numpy as np

# create masivs
a = np.array([1, 2, 3])           # 1D масив
b = np.array([[1, 2], [3, 4]])    # 2D масив
print(a)
print(b)

# Це називається векторизація — обчислення без циклів.
a2 = np.array([1, 2, 3])
b2 = np.array([4, 5, 6])

print(a2 + b2)  # [5 7 9] один масив додаєтьс до другого
print(a2 * b2)  # [ 4 10 18]
print(a2 ** 2) # [1 4 9] кожне число в масиві множиться на себе

ex = [2,3,4,5,6,7,8,9,10]
ex2 = list(i**2 for i in ex)
print(ex2)

# cтатистика
a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))  # Середнє значення
print(np.median(a))  # Медіана
print(np.std(a))  # Стандартне відхилення

print('-----------------------------------------')

# створення спеіальних масивів

print(np.zeros((2, 3)))  # 2x3 масив з нулів
print(np.ones((3, 3)))   # 3x3 масив з одиниць
print(np.eye(3))         # 3x3 одинична матриця
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5)  # [0.  0.25 0.5 0.75 1.]


digl = np.array([90, 80, 70, 100])
print("Середній бал:", np.mean(digl))

# Згенеруємо 10 випадкових чисел від 1 до 100
random_integers = np.random.randint(1, 101, size=10)
print("Випадкові цілі числа:", random_integers)
print("Випадкові цілі числа:", np.random.randint(1, 101, size=10))

student_grades = np.random.randint(0, 101, size=100)
print("Оцінки студентів:", student_grades)

# Статистика
print("Середнє:", np.mean(student_grades))
print("Мінімум:", np.min(student_grades))
print("Максимум:", np.max(student_grades))
print("Стандартне відхилення:", np.std(student_grades))


# Температура 30 днів у межах від 10 до 30 градусів
temperature = np.random.uniform(10.0, 30.0, size=30)
print("Температура по днях:", temperature)

# Середня температура
print("Середня температура:", round(np.mean(temperature), 2))

np.random.seed(42)
print(np.random.randint(0, 10, 5))  # завжди буде однаково
