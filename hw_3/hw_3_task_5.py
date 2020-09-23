# QApython Vitalii Feshchenko
# Homework #3 Task 5

inp1 = input('First: ')
inp2 = input('Second: ')

def foo(inp1, inp2):
    """ Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не
        является числом (любым), то должна выполняться конкатенация, т. е. соединение, строк. В
        остальных случаях введённые числа суммируются """
    try:
        print(int(inp1) + int(inp2))
    except ValueError:
        print(inp1 + inp2)


foo(inp1, inp2)