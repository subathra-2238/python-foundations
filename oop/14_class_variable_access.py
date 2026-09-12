class Student:
    college = "VCEW"

    def __init__(self, name):
        self.name = name


student1 = Student("Subathra")
student2 = Student("Sivasri")

print(student1.name)
print(student1.college)

print(student2.name)
print(Student.college)