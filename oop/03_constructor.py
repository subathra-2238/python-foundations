class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, I am", self.name)
        print("I am", self.age, "years old")


student1 = Student("Subathra", 18)

student1.introduce()