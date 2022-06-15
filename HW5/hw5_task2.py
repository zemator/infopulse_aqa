from hw5_task1 import Person


class Employee(Person):

    def __init__(self, full_name='', birthyear=None, position=None, experience=0, salary=0):
        super().__init__(full_name, birthyear)
        self.position = position
        self.experience = self._exp_not_negative(experience)
        self.salary = self._salary_not_negative(salary)

    def __str__(self):
        return f'This is Employee class.'

    def _exp_not_negative(self, experience):
        if experience <= -1:
            raise ValueError('Salary can not be negative.')
        return experience

    def _salary_not_negative(self, salary):
        if salary <= -1:
            raise ValueError('Salary can not be negative.')
        return salary

    def seniority(self):
        if self.experience <= 3:
            emp_seniority = 'Junior '
        elif 3 < self.experience <= 6:
            emp_seniority = 'Middle '
        else:
            emp_seniority = 'Senior '

        return emp_seniority + self.position

    def salary_raise(self, bonus):
        self.salary += bonus
        return self.salary


emp = Employee(full_name='Tom Hanks', birthyear=1980, position='Mother Lover', experience=2, salary=6969)

