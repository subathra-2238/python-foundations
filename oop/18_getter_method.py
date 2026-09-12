class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student1 = Student("Subathra", 85)

marks = student1.get_marks()

print("Name:", student1.name)
print("Marks:", marks)