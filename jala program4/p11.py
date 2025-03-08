def commonval(arr1, arr2):
    l=[]
    for num in arr1:
        if num in arr2 and num not in l:
            l.append(num)
    return l
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
l=commonval(arr1, arr2)
print("Common values:",l)
