class Student:
    def __init__(self, name):
        self.name = name

    def show_marks(self, subject, marks):
        print(self.name, "scored", marks, "in", subject)


student1 = Student("Subathra")

student1.show_marks("Python", 95)
student1.show_marks("Mathematics", 90)