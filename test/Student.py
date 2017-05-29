class Student(object):
    def __init__(self,name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_major(self, major):
        self.major = major

class MasterStudent(Student):
    intership = 'mandatory, from March to June'

anna = Student('anna')
anna.set_age(21)
anna.set_major('physics')
anna.age
anna.major

james = MasterStudent('james')
james.intership
james.set_age(23)
