class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __repr__(self):
        return f"Student(name='{self.name}', department='{self.department}')"


student1 = Student("Subathra", "AI & ML")

print(student1)