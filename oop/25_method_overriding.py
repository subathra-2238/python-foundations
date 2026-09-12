class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def introduce(self):
        print("I am a student.")


person1 = Person()
student1 = Student()

person1.introduce()
student1.introduce()