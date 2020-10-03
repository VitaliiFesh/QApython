

class Person:

    def __init__(self, name='Bob', age=19, last_name='ff', value=85):
        self.name = name
        self.age = age
        self.last_name = last_name
        self.__value = value


    def show_full_name(self):
        return self.name + ' ' + self.last_name





class Employee(Person):

    def __init__(self, name, age, last_name, value, back):
        super().__init__(name, age, last_name, value)
        self.back = back



e1 = Employe(name='ughj', age=87, last_name='ghj', value=99, back='hjk')

e1.show_full_name()

p1 = Person('Bob', 25, 'Dilan', 'Very important')
print(Person._Person__value)
print(p1.show_full_name())
print(p1.get_older(5))

p1.get_older(10)