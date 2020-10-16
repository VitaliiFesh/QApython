# QApython Vitalii Feshchenko
# Homework #5 Task 4
import unittest

from .hw_5_task_1 import ITemployee


class Test_ITemployee(unittest.TestCase):
    """
    testing a class ITemployee
    """

    def setUp(self) -> None:
        self.emp1 = ITemployee('Alex', 'Doore', birth_year=1991, salary=5000, experience=3, position='Python Developer')
        self.emp2 = ITemployee('Ron', 'Foye', birth_year=1987, salary=7500, experience=9, position='Product owner',
                               skills = ['DOS', 'MS', 'Linux'])

    def test_name(self):
        self.assertEqual(self.emp1.get_name(), 'Alex')

    def test_last_name(self):
        self.assertEqual(self.emp1.get_last_name(), 'Doore')

    def test_full_name(self):
        self.assertEqual(self.emp1.full_name, 'Alex Doore')

    def test_birth_year(self):
        self.assertEqual(self.emp1.birth_year, 1991)

    def test_age_in(self):
        self.assertEqual(self.emp1.age_in(), 29)

    def test_salary(self):
        self.assertEqual(self.emp1.salary, 5000)

    def test_experience(self):
        self.assertEqual(self.emp1.experience, 3)
        self.assertEqual(self.emp2.experience, 9)

    def test_position(self):
        self.assertEqual(self.emp1.position, 'Python Developer')
        self.assertEqual(self.emp2.position, 'Product owner')

    def test_get_position(self):
        self.assertEqual(self.emp1.get_position(), f'Middle {self.emp1.position}')
        self.assertEqual(self.emp2.get_position(), f'Senior {self.emp2.position}')

    def test_raise_salary(self):
        self.assertEqual(self.emp1.raise_salary(100), 5100)

    def test_skills(self):
        expected_skills = ['DOS', 'MS', 'Linux']
        self.assertEqual(self.emp2.skills, expected_skills)

    def add_skills(self):
        expected_skills = ['DOS', 'MS', 'Linux','Python', 'C++', 'Java']
        self.assertEqual(self.emp2.add_skills('Python', 'C++', 'Java'), expected_skills)