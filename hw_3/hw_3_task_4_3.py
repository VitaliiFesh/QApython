# QApython Vitalii Feshchenko
# Homework #3 Task 4_3

from random import randint

# 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого
# маленького до самого большого, пока он не останется пустым.

# creating a random list
ls = []
for i in range(0, 5):
    ls.append(randint(0, 64))

print(f'Random list: {ls}')


while len(ls) > 0:
    # find a min value
    mini = ls[0]
    for i in ls:
        if i < mini:
            mini = i

    # remove a min value from ls
    ls.pop(ls.index(mini))
    print(ls)


