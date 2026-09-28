class Student:
    def introduce(self):
        print("I am a student.")


class Teacher:
    def introduce(self):
        print("I am a teacher.")


person1 = Student()
person2 = Teacher()

person1.introduce()
person2.introduce()