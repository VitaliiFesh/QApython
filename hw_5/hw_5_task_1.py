# QApython Vitalii Feshchenko
# Homework #5 Task 1

from datetime import datetime

current_year = datetime.now().year

class Person:
    """
        Basic class of all persons. Using as parent for all child classes
        Three methods: get_name(), get_last_name() and age_in()
    """

    def __init__(self, name, last_name, birth_year=None):
        self.full_name = str(name).strip() + ' ' + str(last_name).strip()
        self.birth_year = birth_year
        try:
            assert 1900 < self.birth_year < current_year
        except:
            self.birth_year = f'Please type a valid birth year for {self.full_name}'



    def __str__(self):
        return f'{self.full_name}'


    def get_name(self):
        """
        segregating name from full_name

        """

        # full_name >> string, so find index of ' ' and take string[:index]. It's a name.
        self.name = self.full_name[:self.full_name.index(' ')]
        return self.name

    def get_last_name(self):

        # find index of ' ' and take string[index+1 :]. +1 in order to skip space at the start.
        self.last_name = self.full_name[self.full_name.index(' ')+1:]
        return self.last_name

    def age_in(self, year=current_year):

        """
        вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
        если не передавать параметр, по умолчанию, сколько лет в этом году
        """

        try:
            self.age = year - self.birth_year
            if year == current_year:
                return self.age
        except TypeError:
            return f'Error 0x02. Original birth year: {self.birth_year}({type(self.birth_year)}) or year: {year}({type(year)}) is not int value.'


class Employee(Person):

    """
        Employee - the second level class in the parents tree.
        Two additional methods: get_position() and raise_salary()
    """

    def __init__(self, name, last_name, birth_year=None, position=None, salary=0, experience=0):
        super().__init__(name, last_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary

        try:
            assert self.experience and self.salary >= 0

        except:

            if self.salary < 0 and self.experience < 0:
                print(f'Salary: {self.salary} and Experience: {self.experience} were modified as positive values.')

            elif self.salary < 0:
                print(f'Salary: {self.salary} was modified as positive value.')
            elif self.experience < 0:
                print(f'Experience: {self.experience} was modified as positive value.')

            self.experience = abs(self.experience)
            self.salary = abs(self.salary)

    def __str__(self):
        return f'Employee: {self.full_name}, possition: {self.position}, salary: {self.salary}'

    def get_position(self):
        """
        If employee works less then 3 years >> Junior.
        if from 3 to 6 years >> Middle
        if 6 and more >> Senior
        """

        if self.experience < 3:
            return f'Junior {self.position}'
        elif 3 <= self.experience < 6:
            return f'Middle {self.position}'
        elif self.experience >= 6:
            return f'Senior {self.position}'
        else:
            return f'{self.experience} might got a wrong value'

    def raise_salary(self, dollars):
        """
        We can raise the salary by argument in this function
        """
        self.salary += dollars
        return self.salary



class ITemployee(Employee):

    """
        IT employee - the third level class in the parents tree.
        One additional method add_skills().
    """

    def __init__(self, name, last_name, birth_year=None, position=None, salary=0, experience=0, skills = []):
        super().__init__(name, last_name, birth_year, position, salary, experience)
        self.skills = skills

    def __str__(self):

        return f'IT employee: {self.full_name}, position: {self.position}, with {self.experience} years of experience, salary: {self.salary}$.' \
               f' His main skills: {self.skills}'

    def add_skills(self, *args):
        """
        This method allows to add one or several skills in the list.
        """

        for i in args:

            self.skills.append(i)
        return self.skills



p1 = Person('Michael', 'Lopez', 1995)
e2 = Employee('Hovard', 'Fort')
it_e2 = ITemployee('Ralph', 'Kyzmenko', 1991, salary=550)


# ==================================
# e4 = Employee('Ralph', 'Kyzmenko', 1991, position='Engineer', salary=4)
# print(f'{e4.full_name}, salary:{e4.salary}; experience: {e4.experience}; age: {e4.age_in()}; position: {e4.position}')

# ==================================


