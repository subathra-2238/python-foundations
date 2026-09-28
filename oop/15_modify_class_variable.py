class Student:
    college = "VCEW"

    def __init__(self, name):
        self.name = name


student1 = Student("Subathra")
student2 = Student("Sivasri")

print("Before:", Student.college)

Student.college = "Vivekanandha College"

print("After:", Student.college)

print(student1.name, "-", student1.college)
print(student2.name, "-", student2.college)