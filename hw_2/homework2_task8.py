# QApython Vitalii Feshchenko
# Homework #2 Task 7

def matching(a, b ,c):
    """ Даны три целых числа. Определите, сколько среди них совпадающих.
        Программа должна вывести одно из чисел:
        3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны) """

    if a == b == c:
        print(3)
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print(2)
    else:
        print(0)


matching(1, 1, 1)
matching(1, 1, 2)
matching(1, 2, 3)