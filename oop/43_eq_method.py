class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


student1 = Student("Subathra", 18)
student2 = Student("Subathra", 18)
student3 = Student("Sivasri", 19)

print(student1 == student2)
print(student1 == student3)