class Father:
    def skills(self):
        print("Father: Driving")


class Mother:
    def qualities(self):
        print("Mother: Cooking")


class Student(Father, Mother):
    def study(self):
        print("Student: Studying Python")


student1 = Student()

student1.skills()
student1.qualities()
student1.study()