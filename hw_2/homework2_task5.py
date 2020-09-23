# QApython Vitalii Feshchenko
# Homework #2 Task 5

def intercalary_year():
    """ Пользователь вводит целое число. Требуется определить, является ли год с данным номером
        високосным. Если год является високосным, то выведите на экран YES, иначе выведите NO.
        Напомним, что в соответствии с григорианским календарём, год является високосным, если его
        номер кратен 4, но не кратен 100, а также если он кратен 400 """

    n = int(input("Type the integer: "))

    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print(f'{n} - Intercalary year')
    else:
        print(f'{n} - Non-Intercalary year')


intercalary_year()
