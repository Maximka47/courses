class Person():
    first_name = ""
    last_name = ""

    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        pass

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_first_name(self): #incapsulation is marked by __ before method
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_name(self, str_after=""):
        return self.get_first_name() +" "+self.get_last_name() + " name " + str_after
        

max_person = Person(first_name="Max", last_name="Ish")
petro_person = Person(first_name="Petro", last_name="Petrenko")
# print(max_person.first_name)
# print(petro_person.first_name)

# print(max_person)
print(max_person.get_name())
# print(max_person.get_name(" is my name"))