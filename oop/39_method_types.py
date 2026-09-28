class Student:
    college = "VCEW"

    def __init__(self, name):
        self.name = name

    # Instance method
    def introduce(self):
        print("Name:", self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to the Student class")


student1 = Student("Subathra")

student1.introduce()
Student.show_college()
Student.welcome()