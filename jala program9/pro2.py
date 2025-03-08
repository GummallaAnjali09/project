from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def ftype(self):
        pass
    def info(self):
        print("This is a vehicle")

class Car(Vehicle): 
    def ftype(self):
        print("Petrol or Diesel")


mcar = Car()
mcar.info()
mcar.ftype()
