from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def info(self):
        print("This is an animal")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
dog = Dog()
dog.info()  
dog.sound() 

cat = Cat()
cat.info()
cat.sound()
