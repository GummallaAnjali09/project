def evenodd(a):
    e=0
    o=0
    for n in a:
        if n%2==0:
            e+=1
        else:
            o+=1
    print("Even numbers:", e)
    print("Odd numbers:", o)

print("Enter the list elements:")
l=list(map(int,input().split()))
evenodd(l)
