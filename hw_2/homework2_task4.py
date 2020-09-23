# QApython Vitalii Feshchenko
# Homework #2 Task 4


dic = {'title':'airplane', 'price':100, 'ingredients':['engine', 'wing', 'body', 'chassis']}

# 1 Добавьте еще одну пару ключ-значение - «description»: какой-то текст
dic['description'] = 'Antonov Airlines'


# 2 Увеличьте цену на 100
dic.update({'price': dic['price'] + 100})


# 3 Добавьте в список ингредиентов еще один ингредиент
#dict.update({'ingredients':['engine', 'wing', 'body', 'chassis', 'illuminators']})
dic['ingredients'].append('illuminators')

# 4 Выделите на экран количество ингредиентов продукта
#print(dic.get('ingredients'))
print(dic['ingredients'])

# 5 Удалите из словаря значение с ключом «description»
#dic.pop('description')
print(dic)
