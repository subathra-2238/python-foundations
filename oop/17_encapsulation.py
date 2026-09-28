class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)


student1 = Student("Subathra", 85)

print("Name:", student1.name)
student1.show_marks()