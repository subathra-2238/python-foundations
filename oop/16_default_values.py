class Student:
    def __init__(self, name, department="AI & ML"):
        self.name = name
        self.department = department

    def introduce(self):
        print("Name:", self.name)
        print("Department:", self.department)


student1 = Student("Subathra")
student2 = Student("Sivasri", "AI & ML")

student1.introduce()
print()
student2.introduce()