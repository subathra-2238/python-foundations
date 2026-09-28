class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


student1 = Student(
    "Subathra",
    ["Python", "Maths", "DS", "OOP"]
)

print("Student:", student1.name)
print("Number of subjects:", len(student1))