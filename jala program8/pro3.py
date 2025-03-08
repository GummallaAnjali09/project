class MClass:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def dinfo(self):
        return f"Name: {self.name}, Age: {self.age}"

class AccessClass:
    def amclass(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        obj = MClass(name, age) 
        print("Accessed Public Field - Name:", obj.name, ", Age:", obj.age)
        print("Accessed Public Method - Info:", obj.dinfo())

aobj = AccessClass()
aobj.amclass()
