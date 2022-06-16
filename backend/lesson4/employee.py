from person import Person

class Employee(Person):
    years_experience = 0
    program_langs = ["adam"]

    def __init__(self, experience=0, program_langs=[], **kwargs):
        Person.__init__(self, **kwargs)
        self.years_experience = experience
        self.program_langs = program_langs
        print(experience)

    # def get_first(self):
    #     name = self.__get_first_name()
    #     return name

max_employee = Employee(first_name="Max", last_name="Ish", experience=8, program_langs = ["Python", "HTML"])
petro_employee = Employee(first_name="Petro", last_name="Petrenko", experience=10, program_langs=["Java", "CSS"])
print(max_employee.program_langs)
print(max_employee.get_name())
# print(max_employee.get_first())
