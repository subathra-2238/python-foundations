class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Subathra", 18)

student1.introduce()