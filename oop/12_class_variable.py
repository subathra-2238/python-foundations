class Student:
    college = "VCEW"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name, "studies at", self.college)


student1 = Student("Subathra")
student2 = Student("Sivasri")

student1.introduce()
student2.introduce()