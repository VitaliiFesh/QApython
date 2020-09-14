# QApython Vitalii Feshchenko
# Homework #2 Task 3

ls = ['The', 'world', 'is', 'clothing', 'in']

# Выведите 3-е с конца слово из списка
print(ls[-3])

# Выведите 1-ю букву второго слова из списка
print(ls[1][0])

# Выведите последнюю букву последнего слова из списка
print(ls[-1][-1])

# Добавьте в конец списка еще одно слово
ls.append('here')
print(ls)

# Вставьте в середину списка еще одно слово
ls.insert((len(ls) // 2), 'absolutely')
print(ls)

# Удалите первое слово из списка
ls.pop(0) # second method - del ls[0]
print(ls)

# Удалите слово «world» из списка, если оно есть в списке
if 'world' in ls:
    ls.remove('world')
print(ls)