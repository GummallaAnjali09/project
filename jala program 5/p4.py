class Class:
    a=10  

obj1=Class()
obj2=Class()

Class.a = 20  

print(obj1.a)  
print(obj2.a)
print(Class.a)  
