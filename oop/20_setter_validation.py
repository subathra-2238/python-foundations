class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student1 = Student("Subathra", 85)

print("Before:", student1.get_marks())

student1.set_marks(95)
print("After:", student1.get_marks())

student1.set_marks(120)
print("Final:", student1.get_marks())