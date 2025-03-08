class Animal:
    def __init__(self, name="Unknown", species="Unknown"):
        print("Animal Constructor Called")
        self.name = name
        self.species = species
    def display(self):
        print(f"Name:", self.name, "Species:", self.species)

class Dog(Animal):
    def __init__(self, name="Unknown", species="Dog", breed="Unknown"):
        super().__init__(name, species)  
        print("Dog Constructor Called")
        self.breed = breed
    def display(self):
        super().display()
        print(f"Breed: {self.breed}")
dog1 = Dog()
dog1.display()

dog2 = Dog("Buddy")  
dog2.display()

dog3 = Dog("Max", "Dog", "Golden Retriever")
dog3.display()
