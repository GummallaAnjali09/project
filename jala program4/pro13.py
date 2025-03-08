def fsecl(a):
    a=list(set(a))
    a.sort()
    print("Second largest number:", a[-2])

print("Enter list values:")
l=list(map(int,input().split()))
fsecl(l)
