# QApython Vitalii Feshchenko
# Homework #3 Task 4_1 and 4_2

# У вас есть список чисел.

print('First task:', end='\n\n')
ls = [i for i in range(10)]
print(f'Original list: {ls}')

# 1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не
# останется пустым

count = 0
while len(ls) > 0:
    ls.pop(0)
    count += 1
    print(f'{count} iteration, list: {ls}')

print()


# 2. ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
# «удаляет» первый символ строки, пока она не станет пустой?
print('Second task:', end='\n\n')

s = '0123456789'
print(f"Original string: '{s}'")
count = 0
while len(s) > 0:
    s = s[1:]
    count += 1
    print(f'{count} iteration, string: {s}')

