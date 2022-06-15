import unittest
from HW3.hw3_task_9 import is_year_leap, is_triangle
from HW4.hw4_task3 import is_triangle_type as triangle_type

class MyTest(unittest.TestCase):

    def test_year_is_leap(self):
        year = 1984
        self.assertTrue(is_year_leap(year), f'Year {year} is not leap.')

    def test_is_triangle(self):
        a, b, c = 7, 1, 1
        self.assertTrue(is_triangle(a, b, c), f'Figure is not triangle.')

    def test_triangle_type(self):
        a, b, c = 3, 4, 3
        type_trngl = triangle_type(a, b, c)
        trngl_list = ['Equilateral triangle', 'Isosceles triangle', 'Versatile triangle']
        self.assertIn(type_trngl, trngl_list, 'Not Triangle')
        print('\nTriangle type is: ', type_trngl)


if __name__ == '__main__':
    unittest.main()
