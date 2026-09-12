class Student:
    def __init__(self, name, age, department, marks):
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)

    def get_result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"


student1 = Student("Subathra", 18, "AI & ML", 85)

student1.introduce()

print("Marks:", student1.marks)
print("Result:", student1.get_result())