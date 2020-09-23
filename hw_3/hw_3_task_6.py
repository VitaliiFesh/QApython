# QApython Vitalii Feshchenko
# Homework #3 Task 6


def foo():

    """ Пишем программу, которая попросит пользователя ввести слово (строка без пробелов в середине,
        а вначале и в конце пробелы могут быть), состоящее только из символов букв. Пока он не введёт
        правильно, просите его ввести """

    while True:

        inp = input('Type without spaces: ')
        inp = inp.strip()
        if inp.count(' ') > 0:
            continue
        else:
            break

    print('Thank you! Goodbye.')

foo()
