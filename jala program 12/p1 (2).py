class Rectangle:
    def __init__(self, length=5, width=5):
        if length == 1 and width == 1:
            print("Default Constructor Called")
        elif width == 1:
            print("One-Argument Constructor Called")
        else:
            print("Two-Argument Constructor Called")
        
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"Length:", self.length, " Width:" ,self.width, "Area:" ,self.area())
rect1 = Rectangle() 
rect1.display()

rect2 = Rectangle(5)
rect2.display()

rect3 = Rectangle(5, 10)  
rect3.display()
