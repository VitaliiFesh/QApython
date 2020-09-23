# QApython Vitalii Feshchenko
# Homework #2 Task 2

from math import sqrt


#1
def count_hypotenuse():
    """ Вычислите длину гипотенузы в прямоугольном треугольнике
        со сторонами 367 и 127 """

    leg1 = 367
    leg2 = 127
    hypotenuse = sqrt(leg1**2 + leg2**2)
    print(f'#1 hypotenuse = {hypotenuse:.2f}')


count_hypotenuse()


#2
def count_decades(n:int):
    """ Дано двузначное число. Найдите число десятков в нем """

    decades = n // 10
    print(f'#2 n = {n}, decades = {decades}')


count_decades(52)



#3
def sum_of_digits(n:int):
    """ Дано трёхзначное число. Найдите сумму его цифр """

    summ = 0
    n = (str(n)) # convert n:int to str

    for i in n:
        summ += int(i) # get iter of n:str and convert back to int
    print(f'#3 n = {n}, summ = {summ}')


sum_of_digits(254)



#4
def next_even_number(n:int):
    """ Дано целое число n. Выведите следующее за ним чётное число """


    if n%2 == 0:
        next_even = n + 2
    elif n%2 == 1:
        next_even = n + 1
    else: print('Not applicable')

    print(f'#4 n = {n}, next_even = {next_even}')


next_even_number(99)



#5
def fractinal_part(X:float):
    """ Дано положительное действительное число X.
        Выведите его дробную часть"""
    fractinal = X - int(X)  # first way
    fractinal = X % 1  # second way
    print(f'#5 X={X}, fractinal part = {fractinal}')


fractinal_part(6.66666)


#6
def first_digit_part(X:float):
    """ Дано положительное действительное число X. Выведите его первую цифру после
# десятичной точки """
    fractinal = X % 1
    first_digit = str(fractinal)[2]
    print(f'#6 X={X}, first_digit = {first_digit}')

first_digit_part(3/7)