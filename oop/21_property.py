class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


student1 = Student("Subathra", 85)

print("Marks:", student1.marks)

student1.marks = 95

print("Updated marks:", student1.marks)

student1.marks = 120