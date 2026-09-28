class Student:
    college = "VCEW"   # Class variable

    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age     # Instance variable

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", self.college)


student1 = Student("Subathra", 18)
student2 = Student("Sivasri", 18)

student1.introduce()
print()
student2.introduce()