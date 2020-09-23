# QApython Vitalii Feshchenko
# Homework #2 Task 6

def triangel_check():
    """ Даны три числа a, b, c.
        Определите, существует ли треугольник с такими сторонами.
        Если треугольник существует, выведите строку YES,
        иначе выведите строку NO """

    a = int(input('Type a = '))
    b = int(input('Type b = '))
    c = int(input('Type c = '))

    if a + b > c and a + c > b and b + c > a:
        print("YES")
    else:
        print("NO")

triangel_check()