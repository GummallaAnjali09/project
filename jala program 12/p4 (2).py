class Person1:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    def display(self):
        print(f"Name:",self.name, "Age: ",self.age)
p1 = Person1("Ram", 25)
p1.display()
p2 = Person1("Raj", 30)
p2.display()
p1.age = 26
print("After modifying age")
p1.display()
