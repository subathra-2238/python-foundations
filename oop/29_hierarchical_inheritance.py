class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying Python.")


class Teacher(Person):
    def teach(self):
        print("I am teaching Python.")


student1 = Student()
teacher1 = Teacher()

student1.introduce()
student1.study()

print()

teacher1.introduce()
teacher1.teach()