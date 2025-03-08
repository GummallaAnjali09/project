def gender(l):
    l = l.upper()  
    if l== "M":
        return "Male"
    elif l== "F":
        return "Female"
    else:
        return "Invalid input"
l= input()
print(gender(l))
