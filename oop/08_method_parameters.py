class Student:
    def __init__(self, name):
        self.name = name

    def study(self, subject):
        print(self.name, "is studying", subject)


student1 = Student("Subathra")

student1.study("Python")
student1.study("Mathematics")