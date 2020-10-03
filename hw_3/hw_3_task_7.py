# QApython Vitalii Feshchenko
# Homework #3 Task 7


# Создайте строку, в которой написан, какой-то текст. Пример:

s = 'We are not what we should be! We are not what we need to be. But at least we are not what we used to be.'


# Посчитайте сколько слов в тексте

words = s.strip().count(' ') + 1
print(f'Words = {words}', end='\n\n')


# Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)

string = s.lower()
ls = string.split()
for i in range(0, len(ls)):
    if '!' or '.' in ls[i]:
        ls[i] = ls[i].strip(".!")

print(f'Updated clear list: \n{ls}', end='\n\n')


# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)

ls.sort()
print(f'Sorted list: \n{ls}', end='\n\n')


# Посчитать, сколько раз встречается каждое слово

# creating a dict from list with 'None' values for each key
d = dict.fromkeys(ls)

# counting each repetition in the list and presenting that number to keys respectively
for i in d:
    d[i] = ls.count(i)


print(f'Final dict: \n{d}')





