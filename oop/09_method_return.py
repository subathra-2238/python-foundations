class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"


student1 = Student("Subathra", 85)

result = student1.get_result()

print(student1.name, "-", result)