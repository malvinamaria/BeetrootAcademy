import os

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        #self.full_name = first_name.title() + ' ' + last_name.title()
        #self.initials = first_name[0].upper() + last_name[0].upper()

    @property  # with using property we can remove line 6 and 7. full_name is now a method so we can access it as atribute
    def full_name(self, firt_name: str) -> None:
        return self.first_name.title() + ' ' + self.last_name.title()

    @property # this is usefull if we want to change with change in first name we get the change in full name as well.
    def initials(self, first_name: str, last_name: str) -> None:
        return self.first_name[0].upper() + self.last_name[0].upper()

    @full_name.setter
    def full_name(self, name: str) -> None:
        first, last = name.split(' ')
        self.first_name = first.title()
        self.last_name = last.title()

    @full_name.deleter  #can activate # del mp.full_name  with del key :)
    def full_name(self, first_name: str, last_name: str) -> None:
        self.first_name = None
        self.last_name = None
        print("Deleted")


mp = Person('mlawina', 'polak')
mp.full_name = 'Maria Polak'
print(mp.first_name, mp.last_name)
