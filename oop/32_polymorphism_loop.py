class Student:
    def introduce(self):
        print("I am a student.")


class Teacher:
    def introduce(self):
        print("I am a teacher.")


people = [Student(), Teacher()]

for person in people:
    person.introduce()