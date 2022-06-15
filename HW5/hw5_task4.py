import datetime
import statistics
import math

class Area:
    """Class can calculate area and perimetr."""

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f'Area(side_a={self.side_a}, side_b={self.side_b})'

    def calculate_area(self):
        """Returns area."""
        return self.side_a * self.side_b

    def perimetr(self):
        """Returns perimetr."""
        return (self.side_a * 2) + (self.side_b * 2)


class Student:
    """Class creates an student object"""

    def __init__(self, full_name='T M', speciality='Teacher', start_study_year=1984, marks_list=[3, 5]):
        self.full_name = full_name
        self.speciality = speciality
        self.start_study_year = start_study_year
        self.marks_list = marks_list

    def __str__(self):
        return f'Student(full_name={self.full_name}, speciality={self.speciality}, ' \
               f'start_study_year={self.start_study_year}, marks_list={self.marks_list}'

    def add_mark(self, mark):
        """Add mark to the student`s mark list."""
        self.marks_list.append(mark)

    def avarage_score(self):
        """Mean score in mark list."""
        return statistics.mean(self.marks_list)

    def years_in_school(self):
        """How many years student in school."""
        this_year = datetime.datetime.now()
        return this_year.year - self.start_study_year


class MapDot:
    """Dots on map."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'MapDot(x={self.x}, y={self.y})'

    def coord_start(self):
        """Find the distance from dot to beginning of coordinate."""
        return math.sqrt(self.x**2 + self.y**2)
