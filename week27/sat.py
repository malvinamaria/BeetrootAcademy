# task1 
class Person():        # class called Person.

    def __init__(self, first_name, last_name, age):    # Make the __init__() method take firstname, lastname, and age as parameters
        self.first_name = first_name
        self.last_name = last_name          # parameters from line 3 add as attributes.
        self.age = age

    def talk(self, eval):
        pass
        print("Hello" + new_person1.first_name + new_person1.last_name + new_person1.age) # this does not work

new_person = Person('Carl', 'Johnson', '29')
print(new_person)    # <__main__.Person object at 0x101112730>

print(new_person.last_name)   #Johnson


new_person1 = Person('Carla', 'John', '99')
print(new_person1.last_name)
new_person2 = Person('Lara', 'Dorsey', '9')
print(new_person2.first_name)

print("Hello" + ' ' + new_person1.first_name + ' ' + new_person1.last_name + ' ' + new_person1.age)


#task 2
class Dog():

    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age
        Dog.age_factor += 7

    def human_age(self, human_age):
        self.human_age = human_age


print(Dog.age_factor)
human_1 = Dog('4')
print(human_1.dog_age)
human_2 = Dog('7')
print(human_2.dog_age)
print(Dog.age_factor)

human_3 = Dog('10')
print(human_3.dog_age)

