# QApython Vitalii Feshchenko
# Homework #5 Task 1

from datetime import datetime

current_year = datetime.now().year

class Person:

    def __init__(self, name, last_name, birth_year):
        self.full_name = str(name).strip() + ' ' + str(last_name).strip()
        self.birth_year = birth_year
        try:
            assert 1900 < self.birth_year < current_year
        except:
            self.birth_year = f'Please type another birth year for {self.full_name}'
            print(self.birth_year)


    def get_name(self):

        # full_name >> string, so find index of ' ' and take string[:index]. It's a name.
        self.name = self.full_name[:self.full_name.index(' ')]
        return self.name

    def get_last_name(self):

        # find index of ' ' and take string[index+1 :]. +1 in order to skip space at the start.
        self.last_name = self.full_name[self.full_name.index(' ')+1:]
        return self.last_name

    def age_in(self, year=current_year):

        """ вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
            если не передавать параметр, по умолчанию, сколько лет в этом году"""

        try:
            self.age = year - self.birth_year
            return self.age
        except TypeError:
            return f'Error 0x02. Original birth year is not valid.'


class Employee(Person):

    def __init__(self, name, last_name, birth_year, position, experience, salary):
        super().__init__(name, last_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary

        try:
            assert self.experience and self.salary >= 0

        except:
            print('Salary and experience must be a positive value')

    def get_position(self):

        if self.experience < 3:
            return f'Junior {self.position}'
        elif 3 <= self.experience < 6:
            return f'Middle {self.position}'
        elif self.position >= 6:
            return f'Senior {self.position}'
        else:
            return f'{self.experience} might got a wrong value'

#p1 = Person('Michael', 'Lopez', 1989)
e1 = Employee(name='Alex', last_name='Kooler', birth_year=1992, position='Support Engineer', experience=4, salary=1700)

print(e1.get_position())

