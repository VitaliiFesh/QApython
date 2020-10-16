# QApython Vitalii Feshchenko
# Homework #5 Task 2

from datetime import datetime



class Rectange:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a}, {self.b} '

    def calc_square(self):
        self.square = self.a * self.b

        return self.square

    def calc_perimeter(self):
        self.perimeter = 2 * self.a + 2 * self.b

        return self.perimeter

class Student:

    current_year = datetime.now().year

    def __init__(self, full_name, occupation, year_of_start, marks=[]):

        self.full_name = full_name
        self.occupation = occupation
        self.year_of_start = year_of_start
        self.marks = marks

    def __str__(self):
        return f'{self.full_name}, {self.occupation}'

    def add_new_mark(self, new_mark):
        self.marks.append(new_mark)

        return self.marks

    def calc_avr_mark(self):
        self.avg = sum(self.marks) / len(self.marks)
        self.avg = round(self.avg, 2)
        return self.avg

    def how_long_is_student(self, current_year=current_year):
        self.years_of_student = current_year - self.year_of_start
        return self.years_of_student

s1 = Student('Vitalii Feshchenko', 'engineering', 2007, marks=[4,5,5,5,4,3,2,4,2,4,1])

class Point:

    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print('Point values must be digits')

    def __str__(self):
        try:
            return f'{self.x}, {self.y}'
        except:
            return f'At least one value is not digit'

    def distance_to_0_0(self):
        self.distance = ((self.x)**2 + (self.y)**2)**0.5
        return self.distance

    def distance_to_another_point(self, another_point):
        try:
            self.distance_to_another_point = ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5
            return self.distance_to_another_point
        except:
            return f'Another point is not defined'


p1 = Point(3, 4)
p2 = Point(5, 4)



