# QApython Vitalii Feshchenko
# Homework #2 Task 1

# Задание 1

# 1. Определите является ли строка записью числа. (Подсказка: ищите как это
# сделать с помощью методов строк)
s = '123'
s.isdecimal() # True
# -------


# 2. Посчитайте сколько у вас пробелов в строке.
s = '34t rgg 67'
s.count(' ') # 2
# -------


# 3. Посчитайте сколько у вас символов точки '.' в строке.
s = 'tgtgrg.rthrth.th'
s.count('.') # 2
# -------


# 4. Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена
# пробелами. Выведите её на экран. Убедитесь, что у вас 100 символов
# (посчитайте длину).
s = 'Homework'
s.center(100) # '                                              Homework                                              '
len(s.center(100)) # 100
# -------


# 5. Сделайте первые буквы слов строки большими (upper case).
s = 'i am learning python 3'
s.title() # 'I Am Learning Python 3'
# -------


# 6. Определите заканчивается ли ваша строка подстрокой “ing”.
s = 'learning'
s.endswith('ing') # True
# -------


# 7. Определите индекс первого вхождения символа “a” в вашей строке.
s = 'Hello dear Alibaba'
s.index('a') # 8
s.find('a') # 8
# -------

# 8. Разбейте строку на список подстрок по символу пробела.
s = 'Hello dear Alibaba'
#s.split(' ') # ['Hello', 'dear', 'Alibaba']
s.split(' ')
print(s.split(' '))
print(s.split())
# 9. Пусть у вас строка имеет пробельные символы. Найдите метод, который удаляет
# пробельные символы вначале и в конце, но не посередине.
s = '   Hello dear Alibaba   '
s = s.lstrip()
s = s.rstrip() # 'Hello dear Alibaba'
