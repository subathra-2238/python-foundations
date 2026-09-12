class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


student1 = Student("Subathra", 18, "AI & ML")

student1.introduce()