class ArithEx:
    def divide(self,a,b):
        try:
            res=a / b
            print(f"Result:",result)
        except ZeroDivisionError:
            print("Error: Division by zero")
ex = ArithEx()
ex.divide(10, 0)
