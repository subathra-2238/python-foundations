class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def introduce(self):
        print("Name:", self.name)
        print("Department:", self.department)


student1 = Student("Subathra", "AI & ML")

student1.introduce()