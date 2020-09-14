# QApython Vitalii Feshchenko
# Homework #2 Task 7


def sorting():
    """ Дано три числа. Упорядочите их в порядке возрастания. Программа должна считывать три
        числа a, b, c, затем программа должна менять их значения в переменных так, чтобы стали
        выполнены условия a <= b <= c. Затем программа выводит тройку a, b, c """

    a = int(input('Type a = '))
    b = int(input('Type b = '))
    if a > b:
        a, b = b, a
    c = int(input('Type c = '))

    if b > c and a > c:
        a, c = c, a
        b, c = c, b
    elif b > c:
        b, c = c, b
    print(f'a = {a} b = {b} c = {c}')

sorting()

# testing of sorting(). Uncomment 96 string to enable test cases
def test_sorting(a, b, c):
    if a > b:
        a, b = b, a
    if b > c and a > c:
        a, c = c, a
        b, c = c, b
    elif b > c:
        b, c = c, b
    return a, b, c

def testcases(test_sorting):
    if test_sorting(1, 2, 3) == (1, 2, 3):
        print('1, 2, 3 -- Ok')
    else: print('Fail')

    if test_sorting(1, 3, 2) == (1, 2, 3):
        print('1, 3, 2 -- Ok')
    else:
        print('Fail')

    if test_sorting(2, 1, 3) == (1, 2, 3):
        print('2, 1, 3 -- Ok')
    else:
        print('Fail')

    if test_sorting(2, 3, 1) == (1, 2, 3):
        print('2, 3, 1 -- Ok')
    else:
        print('Fail')

    if test_sorting(3, 1, 2) == (1, 2, 3):
        print('3, 1, 2 -- Ok')
    else:
        print('Fail')

    if test_sorting(3, 2, 1) == (1, 2, 3):
        print('3, 2, 1 -- Ok')
    else:
        print('Fail')

    if test_sorting(1, 1, 2) == (1, 1, 2):
        print('1, 1, 2 -- Ok')
    else:
        print('Fail')

    if test_sorting(1, 2, 1) == (1, 1, 2):
        print('1, 2, 1 -- Ok')
    else:
        print('Fail')

    if test_sorting(2, 1, 1) == (1, 1, 2):
        print('2, 1, 1 -- Ok')
    else:
        print('Fail')

    if test_sorting(1, 2, 1) == (1, 1, 2):
        print('1, 2, 1 -- Ok')
    else:
        print('Fail')

    if test_sorting(2, 1, 2) == (1, 2, 2):
        print('2, 1, 2 -- Ok')
    else:
        print('Fail')

    if test_sorting(2, 2, 1) == (1, 2, 2):
        print('2, 2, 1 -- Ok')
    else:
        print('Fail')

#testcases(test_sorting) # uncomment for test running





