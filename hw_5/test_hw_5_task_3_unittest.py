# QApython Vitalii Feshchenko
# Homework #5 Task 3
import unittest

from QApython.hw_4.hw_4_task_3 import is_year_leap


class Test_is_year_leap(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_2020(self):
        res = is_year_leap(2020)
        self.assertEqual(res, True)

