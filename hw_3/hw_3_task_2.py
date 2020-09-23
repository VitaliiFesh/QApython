# QApython Vitalii Feshchenko
# Homework #3 Task 2

s = input('Your string here: ')

def changer(s):

    """ Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а
    если длина строки нечётная, то длина первой части должна быть на один символ больше.
    Переставьте эти две части местами, результат запишите в новую строку и выведите на экран """

    if len(s) % 2 != 0:
        lenght = len(s)//2 + 1
    else:
        lenght = len(s) // 2


    changed_s = s[lenght:] + s[:lenght]
    print(changed_s)
    return changed_s


changer(s)

def testcases(changer):
    """ uncomment 38 string for enabling tescases function """
    count = 1

    for string in ('1234567', '12', 'Hello', '0'):
        expected_results = ('5671234', '21', 'loHel', '0')

        if changer(string) in expected_results:
            print(f'test_case{count} -- ok')
        else:
            print(f'test_case{count} -- failed')
        count += 1

#testcases(changer)

