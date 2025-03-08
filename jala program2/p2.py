def incdecfun(val):
    val1=val+1 
    val2=val-1 
    return val1, val2
n=int(input())
val1,val2= incdecfun(n)
print("Incremented value is:",val1)
print("Decremented value is:",val2)
