# Задание 1. Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).
a = int(input('Введите значение "а" '))
while True:
    b = int(input('Введите значение "b" '))
    if a >= b:
        print('Значение "b" должно быть больше значения "а"!')
    else:
        break
result = 0
for i in range(a, b + 1):
    result = result + i
print(result)

# Задание 2. Факториалом числа n называется число n! = 1 * 2 * 3 * ... * n. Создайте программу, которая
# вычисляет факториал введённого пользователем числа.
while True:
    n = int(input('Введите значение "n!" '))
    if n < 0:
        print('Значение "n!" не может быть отрицательным!')
    else:
        break
result = 1
for i in range(1, n + 1):
    result = result * i
print(result)

# Задание 3
# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите
# на экран прямоугольный треугольник.
for i in range(1, 8):
    for j in range(i):
        print('*', end='')
    print()

