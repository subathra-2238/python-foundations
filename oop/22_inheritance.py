class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying Python.")


student1 = Student()

student1.introduce()
student1.study()