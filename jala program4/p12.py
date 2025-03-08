def removedup(arr):
    l=[]
    for num in arr:
        if num not in l:
            l.append(num)
    return l
arr=list(map(int,input().split()))
l=removedup(arr)
print("After removing duplicates:",l)
