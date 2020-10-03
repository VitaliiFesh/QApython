# QApython Vitalii Feshchenko
# Homework #4 Task 3
from math import sqrt


# task 3.1
def input_number():
    """ Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите
        его ввести. Функция возвращает введённое число """

    while True:
        number = input("Type the number: ")

        try:
            float(number)
            #print(f'Your number is {number}')
            break
        except ValueError:
            print('This is not a number!')
            continue

    return number

#print(input_number())



# task 3.2
def input_word():

    """ Пишем функцию, которая попросит пользователя ввести слово (строка из буквенных
        символов без пробелов в середине, а вначале и в конце пробелы могут быть). Пока он не
        введёт правильно, просите его ввести. Функция возвращает введённое слово """

    while True:

        inp = input('Type without spaces: ')
        inp = inp.strip()

        try:
            if inp.count(' ') < 0:
                break


        except:
            print('Do not use space inside')


            # for i in inp:
            #     if not i.isalpha():
            #         print('Only letters!')




    return inp

print(input_word())



# task 3.3
def is_year_leap(year):
    """ Пользователь вводит целое число. Требуется определить, является ли год с данным номером
        високосным. Если год является високосным, то выведите на экран YES, иначе выведите NO.
        Напомним, что в соответствии с григорианским календарём, год является високосным, если его
        номер кратен 4, но не кратен 100, а также если он кратен 400 """

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


#print(is_year_leap(2006))



# task 3.4
def triangel_check(a:float, b:float ,c:float):
    """ Функция принимает три числа a, b, c. Функция должна определить, существует ли
        треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False """
    try:
        float(a)
        float(b)
        float(c)

    except ValueError:
        print('Type error. At least one value is not a number!')
        return -1
    else:
        if a + b > c and a + c > b and b + c > a:
            return True
        return False


#print(triangel_check(3,45,5))



# task 3.5
def type_of_triangel(a:float, b:float, c:float):
    """ Функция принимает три числа a, b, c. Функция должна определить, существует ли
        треугольник с такими сторонами и если существует, то возвращает тип треугольника
        Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
        (разносторонний) или не треугольник (Not a triangle) """

    # declare default value for triangel
    triangel = 'Not a triangle'

    # in try-except block checking a,b,c are float values
    try:
        float(a)
        float(b)
        float(c)

    except ValueError:
        print('ValueError. At least one value is not a number!')
        return -1

    # when no exception:
    else:
        # checking if triangel exist. If yes, what type:
        if a + b > c and a + c > b and b + c > a:

            if a == b == c:
                triangel = 'Equilateral triangle'
            elif a == b or b == c or a == c:
                triangel = 'Isosceles triangle'
            else:
                triangel = 'Versatile triangle'
            return triangel

        # triangel not exist (return default value):
        else:
            return triangel

#print(type_of_triangel(3,4,5))



# task 3.6

def distance(x1, y1, x2, y2):
    """ Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2,
        y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
        *Считайте четыре действительных числа от пользователя (перед запуском функции, не
        внутри функции) и выведите результат работы этой функции """

    dist = sqrt((x1-x2)**2 + (y1-y2)**2)

    return dist

#print(distance(1,2,3,4))