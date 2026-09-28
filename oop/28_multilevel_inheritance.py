class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying Python.")


class CollegeStudent(Student):
    def attend_class(self):
        print("I am attending college class.")


student1 = CollegeStudent()

student1.introduce()
student1.study()
student1.attend_class()