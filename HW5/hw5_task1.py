import datetime


THIS_YEAR = datetime.datetime.now()


class Person:

    def __init__(self, full_name='', birthyear=None):

        self.full_name = self._is_valid_full_name(full_name)
        self.birthyear = self._valid_birthyear(birthyear)

    def __str__(self):
        return f'This is Person class.'


    def _is_valid_full_name(self, full_name):
        if len(full_name.split()) != 2:
            raise ValueError('Should be name and sirname.')
        return full_name

    def _valid_birthyear(self, birthyear):
        if not birthyear:
            return birthyear
        if birthyear > THIS_YEAR.year or birthyear < 1900:
            raise ValueError('Birth day is inconsits')
        return birthyear

    def get_name(self):
        return self.full_name.split()[0]

    def get_sirname(self):
        return self.full_name.split()[1]

    def age_in(self, year=None):
        if not year:
            return f'{self.full_name} is {THIS_YEAR.year - self.birthyear} years old'
        if year < self.birthyear:
            return f'{self.full_name} will be born in {self.birthyear - year} years.'
        if year > self.birthyear:
            return f'{self.full_name} is {year - self.birthyear} years old'

