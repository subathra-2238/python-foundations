class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying Python.")


class Teacher(Person):
    def teach(self):
        print("I am teaching Python.")


class ClassLeader(Student, Teacher):
    def lead(self):
        print("I am leading the class.")


leader = ClassLeader()

leader.introduce()
leader.study()
leader.teach()
leader.lead()