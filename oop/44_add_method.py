class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


student1 = Student(85)
student2 = Student(90)

total = student1 + student2

print("Total marks:", total)