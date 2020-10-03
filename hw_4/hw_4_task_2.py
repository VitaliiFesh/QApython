# QApython Vitalii Feshchenko
# Homework #4 Task 2


def find_second_min_element(*args):
    """ Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов
        (неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов """

    # find min element in list created by tuple 'args'

    ls = list(args)

    try:
        first_min_element = min(ls)
    except ValueError:
        message = 'Not applicable. Error 0x01. No arguments.'
        return message

    # remove min_element from list and all duplicates
    while True:
        if first_min_element in ls:
            ls.pop(ls.index(first_min_element))
        else:
            break


    try:
        second_min_element = min(ls)
    except ValueError:
        message = 'Not applicable. Error 0x02. All arguments have the same value.'
        return message
    return second_min_element


print(find_second_min_element(4,5,2))
