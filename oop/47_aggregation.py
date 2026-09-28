class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching Python.")


class College:
    def __init__(self, teacher):
        self.teacher = teacher

    def start_class(self):
        self.teacher.teach()


teacher1 = Teacher("Mr. Arun")

college1 = College(teacher1)

college1.start_class()

print("Teacher still exists:", teacher1.name)