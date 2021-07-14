# Method Overloading Task

class Animal():

    def talk(self):
        print("This is talk method derived from Animal class.")

class Cat(Animal):

    def talk(self):
        return 'Cats are mioowing...'


class Dog(Animal):

    def talk(self):
        return 'Dogs are barking....'


# create instance of Cat and Dog
example_cat = Cat()
print(example_cat) # <__main__.Cat object at 0x10281d790>
example_cat.talk()
print(example_cat.talk())  # 'Cats are mioowing...'


dog = Dog()
dog.talk()
print(dog.talk())


# Library Task
class Library():

    def __init__(self, name: str, books: list, authors: list):
        self.name = name
        self.books = list()
        self.author = list()

        def __repr__(self):
            return (self.name + ' ' + self.books + ' ' + self.authors)

       # def __str__(self):
        #    return f'Person(name={self.name}, and has those books {self.books} borrowed by this author {self.authors})

library1 = Library('Mel', ['Python Crash Course'], ['A. Anthony'])
print(library1.__repr__())  # <__main__.Library object at 0x101e13790>


books_list = []
authors_list = []

class Book():

    def __init__(self, name: str, year: int, author: str):
        self.name = name
        self.year = year
        self.author = author

    def new_book(self):
        return (self.name + self.year + self.author)[books_list]

books_list1 = ['Python Crash Course', 'Learn Python', 'Learn Python In One Day']
authors_list1 = ['A. Anthony', 'Samuel Gurkin', 'Aniela Molotov']





class Author():

    def __init__(self, name: str, country: str, birthday: int, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books


