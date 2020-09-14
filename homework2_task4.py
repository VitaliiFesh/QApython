# QApython Vitalii Feshchenko
# Homework #2 Task 4


dict = {'title':'airplane', 'price':100, 'ingredients':['engine', 'wing', 'body', 'chassis']}

# 1 Добавьте еще одну пару ключ-значение - «description»: какой-то текст
dict['description'] = 'Antonov Airlines'


# 2 Увеличьте цену на 100
dict.update({'price': dict['price'] + 100})


# 3 Добавьте в список ингредиентов еще один ингредиент
dict.update({'ingredients':['engine', 'wing', 'body', 'chassis', 'illuminators']})


# 4 Выделите на экран количество ингредиентов продукта
print(dict.get('ingredients'))


# 5 Удалите из словаря значение с ключом «description»
dict.pop('description')

