from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("DOg barks")
    def cinstance(self):
        dog = Dog()
        dog.sound()

mdog = Dog()
mdog.cinstance()
