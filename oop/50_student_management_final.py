class Student:
    college = "VCEW"

    def __init__(self, name, age, department, marks):
        self.name = name
        self.age = age
        self.department = department
        self.__marks = marks

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("College:", self.college)

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_result(self):
        if self.__marks >= 40:
            return "Pass"
        return "Fail"


student1 = Student("Subathra", 18, "AI & ML", 85)

student1.introduce()

print("Marks:", student1.get_marks())
print("Result:", student1.get_result())

student1.set_marks(95)

print("Updated Marks:", student1.get_marks())
print("Updated Result:", student1.get_result())