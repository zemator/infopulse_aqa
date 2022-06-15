from hw5_task2 import Employee


class ITEmployee(Employee):
    """
    Use this class to add one skill add_skill() or many add_skills()
    """

    def __init__(self, salary, skills):
        # super().__init__(salary)
        self.skills = skills
        self.salary = salary

    def __str__(self):
        return f'This is ITEmployee class.'

    def add_skill(self, new_skill):
        """Add one skill.

        Arguments:
            new_skill -- new skill name
        """
        self.skills.append(new_skill)

    def add_skills(self, *args):
        """Add many skills.

        Arguments:
            *args -- tuple of new skills
        """
        for skill in args:
            self.skills.append(skill)


p = ITEmployee(1500, ['plumber', 'military'])


