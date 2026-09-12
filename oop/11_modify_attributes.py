class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age = self.age + 1


student1 = Student("Subathra", 18)

print("Before:", student1.age)

student1.celebrate_birthday()

print("After:", student1.age)
