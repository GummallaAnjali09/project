class par:
    def __init__(self, name, age):
        self.name1 = name 
        self.age1 = age   

    def pmethod(self): 
        print("This is a private method: Name = ",self.name1,", Age =",self.age1)

    def dis(self):
        print("Name:",self.name1, ",Age:" ,self.age1)
        self.pmethod()  

if __name__ == "__main__":
    obj = par("Anjali", 10)
    obj.dis() 

class Chi(par):
    def __init__(self, name, age):
        super().__init__(name, age)

    def tap(self):
        print("Private fields and methods are not accessible from the child class.")

child = Chi("Phani", 25)
child.tap()
