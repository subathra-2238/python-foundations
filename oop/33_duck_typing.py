class Student:
    def introduce(self):
        print("I am a student.")


class Teacher:
    def introduce(self):
        print("I am a teacher.")


def introduce_person(person):
    person.introduce()


student1 = Student()
teacher1 = Teacher()

introduce_person(student1)
introduce_person(teacher1)