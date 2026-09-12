from abc import ABC, abstractmethod


class Animal(ABC):

    def breathe(self):
        print("Animal is breathing.")

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says Woof.")


dog1 = Dog()

dog1.breathe()
dog1.sound()