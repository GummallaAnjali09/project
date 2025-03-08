def arithoper(a, b):
    add=a + b
    sub=a - b
    multi=a * b
    divi= a / b if b != 0 else "Cannot divide by zero"
    
    return add, sub, multi, divi
a=int(input())
b=int(input())
add, sub, mul, div = arithoper(a, b)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
