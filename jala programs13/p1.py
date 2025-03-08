class OverloadExample:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b
obj=OverloadExample()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Do you want to enter a third number? (yes/no): ")

if choice.lower() == "yes":
    num3 = int(input("Enter third number: "))
    result = obj.add(num1, num2, num3)
else:
    result = obj.add(num1, num2)

print("Result:", result)    
