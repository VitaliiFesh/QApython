# QApython Vitalii Feshchenko
# Homework #4 Task 2


def find_second_min_element(*args):
    """ Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов
        (неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов """

    # find min element in list created by tuple 'args'

    ls = list(args)
    first_min_element = min(ls)

    # remove min_element from list and all duplicates
    while True:
        if first_min_element in ls:
            ls.pop(ls.index(first_min_element))
        else:
            break

    return min(ls)


print(find_second_min_element(-2,3,5,-44,-44,7,-2,1,0,-44,5,-1))
