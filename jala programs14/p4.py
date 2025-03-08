def dividenum(a, b):
    return a / b

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = dividenum(num1, num2)
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid  Please enter only numbers.")
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("End of the program.")
