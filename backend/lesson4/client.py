from person import Person
from employee import Employee


class Client(Person):
    project_name=""

    def __init__(self, project_name, **kwargs):
        Person.__init__(self, **kwargs)
        self.project_name = project_name
    
    def get_name(self):
        return self.get_first_name() + ' ' +self.get_last_name() + ' client ' + self.project_name

petro_client = Client(first_name="Petro", last_name="Petrenko", project_name="I")
print(petro_client.get_name())
max_employee = Employee(first_name="Max", last_name="Ish", experience=8, program_langs = ["Python", "HTML"])

persons = [petro_client, max_employee]

for person in persons:
    print(person.get_name())