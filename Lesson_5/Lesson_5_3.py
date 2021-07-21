def division(a, b):
    x = a / b
    print('Результат вычисления - ' + str(x))


def multiplication(a, b):
    x = a * b
    print('Результат вычисления - ' + str(x))


def subtraction(a, b):
    x = a - b
    print('Результат вычисления - ' + str(x))


def addition(a, b):
    x = a + b
    print('Результат вычисления - ' + str(x))


while True:
    first_number = input('Введите первое число - ')
    second_number = input('Введите второе число - ')
    if first_number == 'exit' or second_number == 'exit':
        break
    else:
        while True:
            operator = input('Введите оператор - ')
            if operator == '/' or operator == '*' or operator == '-' or operator == '+':
                break
            else:
                print('Введен не корректный оператор! Повторите попытку')

        if operator == '/' and int(second_number) == 0:
            print('Деление на ноль не возможно!')
        elif operator == '/':
            division(int(first_number), int(second_number))
        elif operator == '*':
            multiplication(int(first_number), int(second_number))
        elif operator == '-':
            subtraction(int(first_number), int(second_number))
        elif operator == '+':
            addition(int(first_number), int(second_number))
        else:
            print('Введены не корректные данные!')


