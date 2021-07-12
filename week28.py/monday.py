# task 1 
class Person():

    def __init__(self, name, salary, language, family, kids, homework, study_time, exams):
        self.name = name
        self.salary = salary
        self.language = language
        self.family = family
        self.kids = kids
        self.homework = homework
        self.study_time = study_time
        self.exams = exams

    def has_family(self, family):
        self.family = family

    #def __repr__(self):
     #   return (self.name + ' ' + self.salary + ' ' + self.language + ' ' + self.family + ' ' + self.kids)

class Student(Person):

    def __init__(self, name, salary, language, family, kids, homework, study_time, exams, weed):
        super().__init__(name, salary, language, family, kids, homework, study_time, exams)
        self.weed = weed

    def smoke_weed(self, smoking_weed=1):
        self.weed += smoking_weed

    def not_smoke_weed(self, smoking_weed=1):
        self.weed -= smoking_weed


student1 = Student('Jan','no', 'english', 'yes', 'no', 'A', '90', 'passed', '0')
print(student1.weed)
student1.has_family('yes')
print(student1.family)


student1.smoke_weed()
print(student1.smoke_weed)
#student1.not_smoke_weed()
#print(student1.not_smoke_weed)

class Teacher(Person):

    def __init__(self, name, salary, language, family, kids, homework, study_time, exams, higher_education):
        super().__init__(name, salary, language, family, kids, homework, study_time, exams)
        self.higher_education = higher_education

    def years_in_university(self, higher_education = 5):
        self.higher_education += years

teacher1 = Teacher('Thomas', '200000', 'swedish', 'yes', 'yes', 'no', '0', 'no', '3' )
print(teacher1)
